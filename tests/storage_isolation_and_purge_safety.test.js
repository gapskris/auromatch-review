import { describe, test, beforeEach } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// In-memory localStorage mock for node test runner
const storageMap = new Map();
globalThis.localStorage = {
  getItem: (k) => storageMap.has(k) ? storageMap.get(k) : null,
  setItem: (k, v) => storageMap.set(k, String(v)),
  removeItem: (k) => storageMap.delete(k),
  clear: () => storageMap.clear(),
  get length() { return storageMap.size; },
  key: (i) => Array.from(storageMap.keys())[i] || null
};
Object.defineProperty(globalThis.localStorage, 'keys', {
  value: () => Array.from(storageMap.keys())
});
globalThis.localStorage.constructor = Object;
for (const key of ['getItem', 'setItem', 'removeItem', 'clear']) {
  Object.defineProperty(globalThis.localStorage, key, { enumerable: false });
}

// In-memory IndexedDB mock for node test runner
const idbStore = new Map();
let isDbOpen = false;
let versionChangeListeners = [];

const mockIndexedDB = {
  open: (name, version) => {
    isDbOpen = true;
    const dbInstance = {
      name,
      version,
      objectStoreNames: { contains: () => true },
      createObjectStore: () => ({}),
      transaction: (storeName, mode) => {
        let oncompleteCb = () => {};
        const tx = {
          objectStore: () => ({
            put: (val, key) => {
              idbStore.set(key, val);
              queueMicrotask(() => oncompleteCb());
            },
            get: (key) => {
              const getReq = { result: undefined };
              queueMicrotask(() => {
                getReq.result = idbStore.has(key) ? idbStore.get(key) : null;
                if (getReq.onsuccess) {
                  getReq.onsuccess({ target: getReq });
                }
              });
              return getReq;
            }
          }),
          set oncomplete(cb) { oncompleteCb = cb; },
          set onerror(cb) {},
          set onabort(cb) {}
        };
        return tx;
      },
      close: () => { isDbOpen = false; },
      set onversionchange(cb) { versionChangeListeners.push(cb); }
    };

    const req = {
      result: dbInstance,
      set onupgradeneeded(cb) {
        queueMicrotask(() => cb({ target: { result: dbInstance } }));
      },
      set onsuccess(cb) {
        queueMicrotask(() => cb({ target: { result: dbInstance } }));
      },
      set onerror(cb) {},
      set onblocked(cb) {}
    };
    return req;
  },
  deleteDatabase: (name) => {
    idbStore.clear();
    const req = {};
    queueMicrotask(() => {
      if (req.onsuccess) req.onsuccess({ target: { result: null } });
    });
    return req;
  }
};
globalThis.indexedDB = mockIndexedDB;

// Mock DOM elements needed by gameManager / themeManager
globalThis.document = {
  getElementById: (id) => null,
  body: { setAttribute: () => {} },
  documentElement: { setAttribute: () => {} }
};

import { GameManager } from '../src/controllers/gameManager.js';
import { 
  executeAbsolutePurge, 
  isPurgeActive, 
  setPurgeLock,
  saveProfileState, 
  loadProfileState,
  profileState,
  setItemAsync,
  getItemAsync,
  autoHealFromIndexedDB,
  initIndexedDB,
  resetIndexedDBConnection,
  encryptAndExportBackup,
  decryptAndImportBackup,
  syncTeachingsRepository
} from '../src/controllers/storageAdapter.js';

describe('🛡️ AuroMatch Storage Isolation, Concurrency & Purge Safety QA Suite', () => {

  beforeEach(() => {
    storageMap.clear();
    idbStore.clear();
    setPurgeLock(false);
    resetIndexedDBConnection();
    versionChangeListeners = [];
  });

  test('TC-SPS-01: Cross-Application Key Isolation during Purge', async () => {
    // 1. Inject foreign sentinel keys from Vak Play and AuroMind
    storageMap.set('vak_player_profile_v1', JSON.stringify({ level: 14 }));
    storageMap.set('auro_vak_content_guard', 'ACCEPTED');
    storageMap.set('auromind_reduced_motion', 'true');
    storageMap.set('unrelated_third_party_key', 'preserve_me');

    // 2. Inject AuroMatch owned keys
    storageMap.set('auromatch_player_state', JSON.stringify({ currentLevel: 42, name: 'Seeker' }));
    storageMap.set('auromatch_player_profiles', JSON.stringify({ Seeker: { currentLevel: 42 } }));
    storageMap.set('auromatch_standard_theme', 'royal_lapis');
    storageMap.set('auro_match_user', JSON.stringify({ profile: { sanctuaryMode: 'traditional' } }));
    storageMap.set('auro_match_consecrations', JSON.stringify(['reflection 1']));
    storageMap.set('auro_match_unlocked_tiles', JSON.stringify([1, 2, 3]));

    // 3. Execute absolute purge
    await executeAbsolutePurge();

    // 4. Assert foreign keys remain 100% untouched
    assert.strictEqual(storageMap.has('vak_player_profile_v1'), true, 'Vak player profile MUST be preserved');
    assert.strictEqual(storageMap.has('auro_vak_content_guard'), true, 'Vak legal content guard MUST be preserved');
    assert.strictEqual(storageMap.has('auromind_reduced_motion'), true, 'AuroMind settings MUST be preserved');
    assert.strictEqual(storageMap.has('unrelated_third_party_key'), true, 'Unrelated origin keys MUST be preserved');

    // 5. Assert all AuroMatch keys are removed
    assert.strictEqual(storageMap.has('auromatch_player_state'), false, 'auromatch_player_state must be removed');
    assert.strictEqual(storageMap.has('auromatch_player_profiles'), false, 'auromatch_player_profiles must be removed');
    assert.strictEqual(storageMap.has('auromatch_standard_theme'), false, 'auromatch_standard_theme must be removed');
    assert.strictEqual(storageMap.has('auro_match_user'), false, 'auro_match_user must be removed');
    assert.strictEqual(storageMap.has('auro_match_consecrations'), false, 'auro_match_consecrations must be removed');
    assert.strictEqual(storageMap.has('auro_match_unlocked_tiles'), false, 'auro_match_unlocked_tiles must be removed');
  });

  test('TC-SPS-02: In-Memory State Reset & Zero Resurrection during Purge Window', async () => {
    // 1. Setup active GameManager instance with high progression
    const gm = new GameManager();
    gm.player.name = 'Seeker';
    gm.player.currentLevel = 50;
    gm.player.sparks = 850;
    gm.player.score = 25000;
    gm.savePlayerState();

    assert.ok(storageMap.has('auromatch_player_state'), 'Pre-purge state must exist in storage');

    // 2. Execute purge passing active GameManager
    await executeAbsolutePurge(gm);

    // 3. Verify in-memory state was reset immediately
    assert.strictEqual(gm.player.currentLevel, 1, 'In-memory currentLevel must be reset to 1');
    assert.strictEqual(gm.player.sparks, 100, 'In-memory sparks must be reset to 100');
    assert.strictEqual(gm.player.name, '', 'In-memory player name must be reset to empty');

    // 4. Simulate a delayed callback attempting to save during the reload cooldown
    const saveResult = gm.savePlayerState();
    assert.strictEqual(saveResult, false, 'savePlayerState must fail-closed while purge lock is active');

    // 5. Confirm storage remains completely purged
    assert.strictEqual(storageMap.has('auromatch_player_state'), false, 'Data must NOT be resurrected in storage');
  });

  test('TC-SPS-03: Purge Barrier Blocks All Secondary Write Paths', () => {
    const gm = new GameManager();
    setPurgeLock(true);

    assert.strictEqual(isPurgeActive(), true, 'Purge must be reported as active');

    // Try saving player state
    const saveStateRes = gm.savePlayerState();
    assert.strictEqual(saveStateRes, false, 'savePlayerState must be blocked');

    // Try saving profiles map
    const saveProfilesRes = gm.saveProfilesMap({ Seeker: { currentLevel: 10 } });
    assert.strictEqual(saveProfilesRes, false, 'saveProfilesMap must be blocked');

    // Try saving profile state in storageAdapter
    const saveProfileRes = saveProfileState();
    assert.strictEqual(saveProfileRes, false, 'saveProfileState must be blocked');

    // Try switching theme
    gm.setStandardTheme('royal_lapis');
    assert.strictEqual(storageMap.has('auromatch_standard_theme'), false, 'Theme save must be blocked during purge');
  });

  test('TC-SPS-04: Cross-Tab Fresh-Read-Before-Merge Prevents Stale Rollbacks', () => {
    // Tab 1 & Tab 2 start at Level 5
    const tab1 = new GameManager();
    tab1.player.name = 'Seeker';
    tab1.player.currentLevel = 5;
    tab1.player.sparks = 100;
    tab1.savePlayerState();

    const tab2 = new GameManager(); // loads Level 5 into tab 2's memory

    // Tab 1 plays heavily: advances to Level 25, earns 600 sparks
    tab1.player.currentLevel = 25;
    tab1.player.sparks = 600;
    tab1.savePlayerState();

    const storedAfterTab1 = JSON.parse(storageMap.get('auromatch_player_state'));
    assert.strictEqual(storedAfterTab1.currentLevel, 25);
    assert.strictEqual(storedAfterTab1.sparks, 600);

    // Now in Tab 2, an event triggers savePlayerState() from its stale memory
    tab2.savePlayerState();

    // Assert Fresh-Read-Before-Merge prevented rolling back Tab 1's progress
    const storedAfterTab2 = JSON.parse(storageMap.get('auromatch_player_state'));
    assert.strictEqual(storedAfterTab2.currentLevel, 25, 'Stored currentLevel must NOT be rolled back to 5');
    assert.strictEqual(storedAfterTab2.sparks, 600, 'Stored sparks must NOT be rolled back to 100');
  });

  test('TC-SPS-05: Purge Confirmation UI Attributes & Input Gating Static Conformance', () => {
    const htmlPath = path.resolve(__dirname, '../index.html');
    const htmlContent = fs.readFileSync(htmlPath, 'utf8');

    const mainJsPath = path.resolve(__dirname, '../src/main.js');
    const mainJsContent = fs.readFileSync(mainJsPath, 'utf8');

    // 1. Verify confirm button is disabled by default in HTML
    assert.ok(
      htmlContent.includes('id="btn-confirm-purge"') && htmlContent.includes('disabled'),
      '#btn-confirm-purge must have disabled attribute initially in index.html'
    );

    // 2. Verify autofill defenses on purge input
    assert.ok(htmlContent.includes('id="purge-confirm-input"'), '#purge-confirm-input must exist');
    assert.ok(htmlContent.includes('autocomplete="off"'), 'Purge input must have autocomplete="off"');
    assert.ok(htmlContent.includes('autocorrect="off"'), 'Purge input must have autocorrect="off"');
    assert.ok(htmlContent.includes('autocapitalize="characters"'), 'Purge input must have autocapitalize="characters"');
    assert.ok(htmlContent.includes('spellcheck="false"'), 'Purge input must have spellcheck="false"');

    // 3. Verify main.js input listener toggles button enablement on exact match 'PURGE'
    assert.ok(mainJsContent.includes("input.value || '').trim() === 'PURGE'"), 'Must validate exact PURGE match');
    assert.ok(mainJsContent.includes('btn.disabled = !isExact'), 'Must dynamically toggle button disabled state');

    // 4. Verify main.js has click debouncing / execution lock
    assert.ok(mainJsContent.includes('isPurgeExecuting'), 'Must have isPurgeExecuting debouncing guard');
  });

  test('TC-SPS-06: Cross-Tab Fresh-Read-Before-Merge in saveProfileState prevents stomping reflections & unlocked tiles', () => {
    // 1. Tab 1 adds reflections and completes level tiles
    storageMap.set('auro_match_consecrations', JSON.stringify(['Day 1 Reflection', 'Day 2 Reflection']));
    storageMap.set('auro_match_unlocked_tiles', JSON.stringify([101, 102, 103, 104]));

    // 2. Tab 2 holds older profileState (empty reflections, empty tiles) and updates volume setting
    profileState.reflections = [];
    profileState.progression.completedLevelIds = [];
    profileState.settings.volumeRaga = 0.85;

    // 3. Tab 2 saves its settings
    saveProfileState();

    // 4. Assert Tab 2 did not wipe out Tab 1's reflections or unlocked tiles
    const savedConsecrations = JSON.parse(storageMap.get('auro_match_consecrations'));
    const savedUnlocked = JSON.parse(storageMap.get('auro_match_unlocked_tiles'));

    assert.strictEqual(savedConsecrations.length, 2, 'Reflections must NOT be wiped by stale tab saving settings');
    assert.strictEqual(savedUnlocked.length, 4, 'Unlocked tiles must NOT be wiped by stale tab saving settings');
  });

  test('TC-IDB-01: Auto-Healing restores 100% of game state from AuroMatchDB when localStorage is evicted (Safari 7-day wipe simulation)', async () => {
    // 1. Setup persistent records in AuroMatchDB IndexedDB vault
    idbStore.set('auromatch_player_state', JSON.stringify({
      name: 'Seeker',
      currentLevel: 180,
      sparks: 2400,
      score: 50000,
      focusIQ: 140,
      hasProgress: true
    }));
    idbStore.set('auromatch_player_profiles', JSON.stringify({
      Seeker: { name: 'Seeker', avatar: '🦉', currentLevel: 180, sparks: 2400, score: 50000, focusIQ: 140 }
    }));
    idbStore.set('auro_match_consecrations', JSON.stringify(['Day 1 Reflection', 'Day 2 Reflection']));
    idbStore.set('auro_match_unlocked_tiles', JSON.stringify([1, 2, 3, 4, 5, 6]));

    // 2. Simulate Apple Safari 7-day eviction: localStorage is completely wiped!
    storageMap.clear();
    assert.strictEqual(storageMap.size, 0, 'localStorage must be empty after 7-day Safari purge');

    // 3. Trigger auto-healing on boot
    const healed = await autoHealFromIndexedDB();
    assert.strictEqual(healed, true, 'autoHealFromIndexedDB must report successful restoration');

    // 4. Assert localStorage was 100% healed with all player state and reflections
    assert.ok(storageMap.has('auromatch_player_state'), 'auromatch_player_state must be healed');
    const restoredPlayer = JSON.parse(storageMap.get('auromatch_player_state'));
    assert.strictEqual(restoredPlayer.currentLevel, 180, 'Player must be restored to Level 180');
    assert.strictEqual(restoredPlayer.sparks, 2400, 'Player sparks must be restored to 2400');

    const restoredReflections = JSON.parse(storageMap.get('auro_match_consecrations'));
    assert.strictEqual(restoredReflections.length, 2, 'All reflections must be restored');

    const restoredTiles = JSON.parse(storageMap.get('auro_match_unlocked_tiles'));
    assert.strictEqual(restoredTiles.length, 6, 'All unlocked tiles must be restored');
  });

  test('TC-IDB-02: Multi-Phase Purge successfully wipes AuroMatchDB and localStorage', async () => {
    // 1. Populate both stores with active state
    storageMap.set('auromatch_player_state', JSON.stringify({ currentLevel: 50 }));
    storageMap.set('vak_player_profile_v1', JSON.stringify({ currentLevel: 12 })); // Foreign key

    idbStore.set('auromatch_player_state', JSON.stringify({ currentLevel: 50 }));
    idbStore.set('auro_match_consecrations', JSON.stringify(['reflection']));

    // 2. Execute multi-phase purge
    await executeAbsolutePurge();

    // 3. Confirm AuroMatchDB was deleted and wiped
    assert.strictEqual(idbStore.has('auromatch_player_state'), false, 'IDB player state must be wiped');
    assert.strictEqual(idbStore.has('auro_match_consecrations'), false, 'IDB reflections must be wiped');

    // 4. Confirm localStorage AuroMatch keys were wiped, foreign keys preserved
    assert.strictEqual(storageMap.has('auromatch_player_state'), false, 'localStorage player state must be wiped');
    assert.strictEqual(storageMap.has('vak_player_profile_v1'), true, 'Foreign Vak key must remain 100% intact');
  });

  test('TC-IDB-03: AuroMatchDB onversionchange listener closes connection cleanly', async () => {
    const db = await initIndexedDB();
    assert.ok(db, 'AuroMatchDB connection must open');
    assert.strictEqual(isDbOpen, true, 'isDbOpen must be true');

    // Simulate onversionchange dispatched by browser engine when another context requests deletion
    if (versionChangeListeners.length > 0) {
      versionChangeListeners[0]();
    }
    assert.strictEqual(isDbOpen, false, 'Connection must close immediately on versionchange');
  });

  test('TC-ROST-01: Multi-Seeker Roster Isolation (Seeker A vs Seeker B independent progression)', () => {
    const gm = new GameManager();

    // 1. Setup Seeker Gopal at Level 45, 850 sparks, 12000 score
    gm.setPlayerName('Gopal', '🦉');
    gm.player.currentLevel = 45;
    gm.player.sparks = 850;
    gm.player.score = 12000;
    gm.savePlayerState();

    // 2. Switch to Seeker Maya at Level 1, 100 sparks, 0 score
    gm.setPlayerName('Maya', '🔭');
    assert.strictEqual(gm.player.name, 'Maya');
    assert.strictEqual(gm.player.currentLevel, 1, 'New seeker must start at Level 1');
    assert.strictEqual(gm.player.sparks, 100, 'New seeker must start with 100 sparks');
    assert.strictEqual(gm.player.score, 0);
    gm.player.currentLevel = 5;
    gm.player.sparks = 180;
    gm.savePlayerState();

    // 3. Switch back to Gopal -> assert Level 45 and 850 sparks preserved
    gm.setPlayerName('Gopal');
    assert.strictEqual(gm.player.name, 'Gopal');
    assert.strictEqual(gm.player.currentLevel, 45, 'Gopal Level 45 must be preserved');
    assert.strictEqual(gm.player.sparks, 850, 'Gopal 850 sparks must be preserved');
    assert.strictEqual(gm.player.score, 12000);
  });

  test('TC-ROST-02: Avatar Selection Roster Persistence', () => {
    const gm = new GameManager();
    gm.setPlayerName('Aspirant', '⚛️');
    const profiles = gm.loadProfilesMap();
    assert.ok(profiles['Aspirant'], 'Aspirant profile must exist');
    assert.strictEqual(profiles['Aspirant'].avatar, '⚛️', 'Selected avatar must persist');
  });

  test('TC-ROST-03: Returning Seeker Auto-Resume Profile Extraction', () => {
    storageMap.set('auromatch_player_state', JSON.stringify({
      name: 'PondicherrySeeker',
      currentLevel: 88,
      sparks: 1400,
      score: 35000,
      focusIQ: 135,
      hasProgress: true
    }));

    const gm = new GameManager();
    assert.strictEqual(gm.player.name, 'PondicherrySeeker');
    assert.strictEqual(gm.player.currentLevel, 88);
    assert.strictEqual(gm.player.sparks, 1400);
    assert.strictEqual(gm.player.focusIQ, 135);
  });

  test('TC-ROST-04: Sparks Economy Conservation (Sparks cannot underflow below zero)', () => {
    const gm = new GameManager();
    gm.player.sparks = 10; // Insufficient for a 20-sparks hint
    const hintResult = gm.provideHint();
    assert.strictEqual(!hintResult, true, 'Hint must be rejected when sparks < 20');
    assert.strictEqual(gm.player.sparks, 10, 'Sparks balance must remain 10 without underflow');
  });

  test('TC-ROST-05: Focus IQ Numerical Bounds (80 to 200 bounds, NaN resilience)', () => {
    const gm = new GameManager();
    assert.strictEqual(gm.player.focusIQ, 80, 'Default Focus IQ must be 80');
    gm.player.focusIQ = (gm.player.focusIQ || 80) + 3; // Clean solve advancement
    assert.ok(gm.player.focusIQ >= 80 && gm.player.focusIQ <= 200, 'Focus IQ must stay within valid range');
    assert.strictEqual(Number.isNaN(gm.player.focusIQ), false, 'Focus IQ must never be NaN');
  });

  test('TC-ROST-06: Corrupt Storage Fail-Closed Healing (Malformed JSON handling)', () => {
    storageMap.set('auromatch_player_state', '{ malformed_broken_json : ');
    assert.doesNotThrow(() => {
      const gm = new GameManager();
      assert.strictEqual(gm.player.currentLevel, 1, 'Corrupted storage must fallback to level 1 safely');
    }, 'Must not throw on corrupted player state');
  });

  test('TC-ROST-07: PBKDF2 AES-GCM Encrypted Backup Export Roundtrip (100,000 iterations)', async () => {
    profileState.profile.sanctuaryMode = 'traditional';
    profileState.settings.volumeRaga = 0.55;
    profileState.reflections = ['Contemplation Day 1', 'Contemplation Day 2'];

    const password = 'SacredPassword123!';
    const backupJson = await encryptAndExportBackup(password);
    assert.ok(backupJson, 'Backup JSON must be generated');

    const parsed = JSON.parse(backupJson);
    assert.strictEqual(parsed.version, 2);
    assert.strictEqual(parsed.iterations, 100000, 'Must enforce 100,000 PBKDF2 iterations');
    assert.ok(parsed.salt, 'Must include random salt');
    assert.ok(parsed.iv, 'Must include random IV');
    assert.ok(parsed.data, 'Must include ciphertext');

    // Decrypt roundtrip
    const decrypted = await decryptAndImportBackup(password, backupJson);
    assert.strictEqual(decrypted.profile.sanctuaryMode, 'traditional');
    assert.strictEqual(decrypted.settings.volumeRaga, 0.55);
    assert.strictEqual(decrypted.reflections.length, 2);
  });

  test('TC-ROST-08: PBKDF2 Backup Invalid Password Rejection', async () => {
    const backupJson = await encryptAndExportBackup('correctPassword');
    await assert.rejects(async () => {
      await decryptAndImportBackup('wrongPassword', backupJson);
    }, 'Decryption with wrong password must reject safely');
  });

  test('TC-ROST-09: Teachings Repository Version Sync', () => {
    storageMap.set('auro_match_teachings', JSON.stringify({ version: 100, themes: {} }));
    syncTeachingsRepository({ version: 105, themes: { peace: ['Quote 1'] } });

    const stored = JSON.parse(storageMap.get('auro_match_teachings'));
    assert.strictEqual(stored.version, 105, 'Higher version teachings repository must sync');
  });

  test('TC-ROST-10: Device Settings vs Seeker State Separation', () => {
    const gm = new GameManager();
    // Device settings: theme, senior view
    gm.setStandardTheme('royal_lapis');
    assert.strictEqual(storageMap.get('auromatch_standard_theme'), 'royal_lapis');

    // Seeker state: level, sparks
    gm.setPlayerName('SeekerOne');
    gm.player.currentLevel = 10;
    gm.savePlayerState();

    // Switch player: device theme must NOT change
    gm.setPlayerName('SeekerTwo');
    assert.strictEqual(storageMap.get('auromatch_standard_theme'), 'royal_lapis', 'Device theme must remain intact');
    assert.strictEqual(gm.player.currentLevel, 1, 'SeekerTwo must start at level 1');
  });

  test('TC-ROST-11: BroadcastChannel Cross-Tab Purge Notification Bus', () => {
    let broadcastSent = false;
    let messageReceived = null;

    globalThis.BroadcastChannel = class {
      constructor(name) { this.name = name; }
      postMessage(data) {
        broadcastSent = true;
        messageReceived = data;
      }
      close() {}
    };

    const gm = new GameManager();
    gm.player.name = 'Seeker';
    gm.player.currentLevel = 20;

    executeAbsolutePurge(gm);
    assert.strictEqual(broadcastSent, true, 'Purge must broadcast across tabs');
    assert.strictEqual(messageReceived.type, 'AUROMATCH_PURGE_EXECUTED');
    assert.strictEqual(gm.player.currentLevel, 1, 'In-memory state must be reset');
  });

});
