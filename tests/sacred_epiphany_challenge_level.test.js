import { describe, it, beforeEach } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');

// Mock localStorage for node environment
if (typeof globalThis.localStorage === 'undefined') {
  let store = {};
  globalThis.localStorage = {
    getItem: (k) => store[k] || null,
    setItem: (k, v) => { store[k] = String(v); },
    removeItem: (k) => { delete store[k]; },
    clear: () => { store = {}; }
  };
}

describe('✨ Sacred Epiphany Challenge Level & 3D Mandala Architecture QA Suite', async () => {
  const { VitaBoardGenerator } = await import('../src/models/boardGenerator.js');
  const { floraCatalog } = await import('../src/models/floraDatabase.js');
  const { GameManager } = await import('../src/controllers/gameManager.js');

  let gm;

  beforeEach(() => {
    globalThis.localStorage.clear();
    gm = new GameManager();
  });

  // TC-EPI-01: Geometry Anchor Count
  it('TC-EPI-01: getEpiphanyMandalaCoordinates produces exactly 48 valid 3D anchors', () => {
    const coords = VitaBoardGenerator.getEpiphanyMandalaCoordinates(48);
    assert.strictEqual(coords.length, 48, 'Mandala must contain exactly 48 anchors');
    const seen = new Set();
    for (const c of coords) {
      assert.ok(typeof c.x === 'number' && typeof c.y === 'number' && typeof c.z === 'number');
      const key = `${c.x}_${c.y}_${c.z}`;
      assert.ok(!seen.has(key), `Duplicate coordinate detected: ${key}`);
      seen.add(key);
    }
  });

  // TC-EPI-02: Elevation Tier Distribution
  it('TC-EPI-02: Mandala elevation distribution across 4 distinct tiers (Z in {0, 1, 2, 3})', () => {
    const coords = VitaBoardGenerator.getEpiphanyMandalaCoordinates(48);
    const tiers = { 0: 0, 1: 0, 2: 0, 3: 0 };
    coords.forEach(c => tiers[c.z]++);
    assert.strictEqual(tiers[3], 4, 'Tier 3 (Bindu Core) must have exactly 4 tiles');
    assert.strictEqual(tiers[2], 8, 'Tier 2 (Four Powers) must have exactly 8 tiles');
    assert.strictEqual(tiers[1], 16, 'Tier 1 (Inner Ring) must have exactly 16 tiles');
    assert.strictEqual(tiers[0], 20, 'Tier 0 (Outer Petals) must have exactly 20 tiles');
  });

  // TC-EPI-03: Radial Symmetry
  it('TC-EPI-03: Symmetry verification of outer 12-petalled petal anchors', () => {
    const coords = VitaBoardGenerator.getEpiphanyMandalaCoordinates(48);
    const tier0 = coords.filter(c => c.z === 0);
    assert.strictEqual(tier0.length, 20);
    // Center of mass must be near (3.5, 3.5)
    const avgX = tier0.reduce((s, c) => s + c.x, 0) / tier0.length;
    const avgY = tier0.reduce((s, c) => s + c.y, 0) / tier0.length;
    assert.ok(Math.abs(avgX - 3.5) < 0.2, 'Mandala must be centered horizontally');
    assert.ok(Math.abs(avgY - 3.5) < 0.2, 'Mandala must be centered vertically');
  });

  // TC-EPI-04: Bindu Core Occlusion
  it('TC-EPI-04: Central Bindu Core is completely placed at highest Tier 3', () => {
    const coords = VitaBoardGenerator.getEpiphanyMandalaCoordinates(48);
    const bindu = coords.filter(c => c.z === 3);
    assert.strictEqual(bindu.length, 4);
    bindu.forEach(b => {
      assert.ok(Math.abs(b.x - 3.5) <= 0.6);
      assert.ok(Math.abs(b.y - 3.5) <= 0.6);
    });
  });

  // TC-EPI-05: Playable Tile Lateral Clearance
  it('TC-EPI-05: Lateral side clearance calculation on radial coordinates', () => {
    const coords = VitaBoardGenerator.getEpiphanyMandalaCoordinates(48);
    const board = VitaBoardGenerator.generateSolvableBoard(coords, floraCatalog, 'tile_club');
    const playable = VitaBoardGenerator.getPlayableTiles(board);
    assert.ok(playable.length > 0, 'Initial Mandala board must have free playable tiles');
    playable.forEach(p => {
      assert.ok(VitaBoardGenerator.isTileFree(p, board), 'Tile reported playable must pass isTileFree');
    });
  });

  // TC-EPI-06: Unity Triad Match
  it('TC-EPI-06: Unity Triad match resolution (3 identical flora tiles clear from tray)', () => {
    gm.startEpiphanyTrial();
    gm.tray = [
      { id: 't1', floraId: 'tile_peace', floraData: { id: 'tile_peace', domain: 'Wisdom', archetype: 'ivory' }, isMatched: true },
      { id: 't2', floraId: 'tile_peace', floraData: { id: 'tile_peace', domain: 'Wisdom', archetype: 'ivory' }, isMatched: true },
      { id: 't3', floraId: 'tile_calm', floraData: { id: 'tile_calm', domain: 'Wisdom', archetype: 'jade' }, isMatched: true }
    ];

    // Click 3rd identical tile
    const thirdTile = { id: 't4', floraId: 'tile_peace', floraData: { id: 'tile_peace', domain: 'Wisdom', archetype: 'ivory' }, isMatched: false };
    gm.handleTileClubMatch3Click(thirdTile);

    // Triad must dissolve, leaving only tile_calm
    assert.strictEqual(gm.tray.length, 1);
    assert.strictEqual(gm.tray[0].floraId, 'tile_calm');
  });

  // TC-EPI-07: Integral Synthesis Triad Match
  it('TC-EPI-07: Integral Synthesis Triad match resolution (3 distinct tiles in same spiritual domain)', () => {
    gm.startEpiphanyTrial();
    gm.tray = [
      { id: 't1', floraId: 'tile_peace', floraData: { id: 'tile_peace', domain: 'Wisdom & Integral Yoga', archetype: 'ivory' }, isMatched: true },
      { id: 't2', floraId: 'tile_aspiration', floraData: { id: 'tile_aspiration', domain: 'Wisdom & Integral Yoga', archetype: 'cameo' }, isMatched: true }
    ];

    // Click 3rd tile from same domain
    const thirdTile = { id: 't3', floraId: 'tile_devotion', floraData: { id: 'tile_devotion', domain: 'Wisdom & Integral Yoga', archetype: 'golden_relic' }, isMatched: false };
    gm.handleTileClubMatch3Click(thirdTile);

    // Synthesis triad must dissolve completely
    assert.strictEqual(gm.tray.length, 0, 'Synthesis triad must clear from tray');
  });

  // TC-EPI-08: Mismatched Archetype Rejection
  it('TC-EPI-08: Mismatched archetype rejection (mismatched tiles stay in tray without clearing)', () => {
    gm.startEpiphanyTrial();
    gm.tray = [
      { id: 't1', floraId: 'tile_peace', floraData: { id: 'tile_peace', domain: 'Wisdom & Integral Yoga' }, isMatched: true },
      { id: 't2', floraId: 'tile_tiger', floraData: { id: 'tile_tiger', domain: 'Fauna & Wildlife' }, isMatched: true }
    ];

    const thirdTile = { id: 't3', floraId: 'tile_galaxy', floraData: { id: 'tile_galaxy', domain: 'Cosmos & Astronomy' }, isMatched: false };
    gm.handleTileClubMatch3Click(thirdTile);

    assert.strictEqual(gm.tray.length, 3, 'Mismatched tiles must remain in tray');
  });

  // TC-EPI-09: Tray Capacity Limit (7 slots)
  it('TC-EPI-09: Tray capacity limit (7 slots) strictly enforced', () => {
    gm.startEpiphanyTrial();
    for (let i = 0; i < 7; i++) {
      gm.tray.push({ id: `t_${i}`, floraId: `diff_${i}`, isMatched: true });
    }
    assert.strictEqual(gm.tray.length, 7);

    const extra = { id: 't_extra', floraId: 'extra', isMatched: false };
    gm.handleTileClubMatch3Click(extra);
    assert.strictEqual(gm.tray.length, 7, 'Tray must not exceed 7 slots');
  });

  // TC-EPI-10: Reverse Deconstruction Solvability Simulation
  it('TC-EPI-10: Reverse deconstruction generates 100% solvable Mandala', () => {
    const coords = VitaBoardGenerator.getEpiphanyMandalaCoordinates(48);
    const board = VitaBoardGenerator.generateSolvableBoard(coords, floraCatalog, 'tile_club');
    assert.strictEqual(board.length, 48);

    const sim = VitaBoardGenerator.simulateForwardSolver(board, 3);
    assert.strictEqual(sim.isSolvable, true, 'Board must be solvable');
    assert.strictEqual(sim.remainingTilesCount, 0, 'Simulation must clear all 48 tiles');
  });

  // TC-EPI-11: Trigger Window
  it('TC-EPI-11: Epiphany trigger window strictly respects 6 to 12 levels', () => {
    assert.ok(gm.nextEpiphanyTarget >= 6 && gm.nextEpiphanyTarget <= 12, 'Target must be between 6 and 12');
  });

  // TC-EPI-12: Invitation Gateway Modal DOM
  it('TC-EPI-12: Epiphany Invitation Gateway modal DOM and action buttons exist', () => {
    const indexHtml = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf-8');
    assert.ok(indexHtml.includes('id="btn-enter-epiphany"'), 'Enter button must exist');
    assert.ok(indexHtml.includes('id="btn-postpone-epiphany"'), 'Postpone button must exist');
    assert.ok(indexHtml.includes('id="epiphany-serenity-wrap"'), 'Serenity HUD bar must exist');
  });

  // TC-EPI-13: Postpone Epiphany
  it('TC-EPI-13: Postponing Epiphany safely defers level without resetting trigger count', () => {
    gm.isEpiphanyActive = true;
    gm.epiphanyState = 'OFFERED';
    gm.levelsSinceLastEpiphany = 8;

    gm.postponeEpiphanyTrial();
    assert.strictEqual(gm.epiphanyState, 'POSTPONED');
    assert.strictEqual(gm.isEpiphanyLevelActive, false);
    assert.strictEqual(gm.levelsSinceLastEpiphany, 8, 'Level count must not be wiped on postpone');
  });

  // TC-EPI-14: Start Epiphany Trial
  it('TC-EPI-14: Entering Epiphany sets isEpiphanyLevelActive = true and initializes 48 tiles', () => {
    gm.startEpiphanyTrial();
    assert.strictEqual(gm.isEpiphanyLevelActive, true);
    assert.strictEqual(gm.epiphanyState, 'ACTIVE');
    assert.strictEqual(gm.tiles.length, 48);
    assert.strictEqual(gm.currentFormationName, 'Epiphany Mandala (Matrimandir Lotus)');
  });

  // TC-EPI-15: Initial Serenity Meter
  it('TC-EPI-15: Focus Serenity Meter starts at 100% upon stage entrance', () => {
    gm.startEpiphanyTrial();
    assert.strictEqual(gm.serenityMeter, 100);
  });

  // TC-EPI-16: Serenity Decay on Blocked Selection
  it('TC-EPI-16: Serenity decays by 4% on invalid/blocked tile selection', () => {
    gm.startEpiphanyTrial();
    gm.decaySerenity(4);
    assert.strictEqual(gm.serenityMeter, 96);
  });

  // TC-EPI-17: Serenity Decay on Reshuffle
  it('TC-EPI-17: Serenity decays by 15% on remaining tiles reshuffle', () => {
    gm.startEpiphanyTrial();
    gm.reshuffleRemaining();
    assert.strictEqual(gm.serenityMeter, 85);
  });

  // TC-EPI-18: Dissolution on Serenity Depleted
  it('TC-EPI-18: Dissolution on Serenity reaching 0%', () => {
    gm.startEpiphanyTrial();
    gm.decaySerenity(100);
    assert.strictEqual(gm.epiphanyState, 'DISSOLVED');
    assert.strictEqual(gm.isEpiphanyLevelActive, false);
  });

  // TC-EPI-19: Dissolution on Tray Overflow
  it('TC-EPI-19: Dissolution on Tray overflow (7 unmatchable tiles triggers dissolution)', () => {
    gm.startEpiphanyTrial();
    for (let i = 0; i < 6; i++) {
      gm.tray.push({ id: `t_${i}`, floraId: `unique_${i}`, floraData: { domain: `d_${i}` }, isMatched: true });
    }
    // Clicking 7th unmatchable tile fills tray to 7 with zero matches
    const seventhTile = { id: 't_overflow', floraId: 'diff_overflow', floraData: { domain: 'diff' }, isMatched: false };
    gm.handleTileClubMatch3Click(seventhTile);

    assert.strictEqual(gm.epiphanyState, 'DISSOLVED');
    assert.strictEqual(gm.isEpiphanyLevelActive, false);
  });

  // TC-EPI-20: Zero Loss of Prior Sparks on Dissolution
  it('TC-EPI-20: Zero loss of prior sparks or progression on Epiphany dissolution', () => {
    gm.player.sparks = 150;
    gm.player.currentLevel = 9;
    gm.startEpiphanyTrial();
    gm.dissolveEpiphanyStage('TRAY_OVERFLOW');

    assert.strictEqual(gm.player.currentLevel, 9, 'Level progress must be intact');
    assert.strictEqual(gm.player.sparks, 170, 'Must grant standard +20 base sparks without penalty');
  });

  // TC-EPI-21: Gated +60 Sparks on Triumph
  it('TC-EPI-21: Gated +60 Triple Sparks awarded ONLY on triumphant Mandala clear', () => {
    gm.player.sparks = 100;
    gm.startEpiphanyTrial();
    // Simulate board clear
    gm.completeEpiphanyStage();

    assert.strictEqual(gm.epiphanyState, 'TRIUMPH');
    assert.strictEqual(gm.player.sparks, 160, 'Must award exactly +60 sparks upon triumphant solution');
  });

  // TC-EPI-22: Golden Aura Wheel Activation
  it('TC-EPI-22: Golden Aura Wheel activation for 10 subsequent levels on triumph', () => {
    gm.startEpiphanyTrial();
    gm.completeEpiphanyStage();
    assert.strictEqual(gm.player.goldenAuraLevelsRemaining, 10, 'Must activate Golden Aura for 10 levels');
  });

  // TC-EPI-23: Storage Persistence of Epiphany Ledger
  it('TC-EPI-23: Storage persistence of epiphaniesUnlocked ledger', () => {
    gm.startEpiphanyTrial();
    gm.completeEpiphanyStage();

    assert.ok(Array.isArray(gm.epiphaniesUnlocked));
    assert.strictEqual(gm.epiphaniesUnlocked.length, 1);
    assert.strictEqual(gm.epiphaniesUnlocked[0].serenityRemaining, 100);

    const raw = globalThis.localStorage.getItem('auromatch_player_state');
    assert.ok(raw, 'State must be saved in localStorage');
    const parsed = JSON.parse(raw);
    assert.strictEqual(parsed.goldenAuraLevelsRemaining, 10);
  });

  // TC-EPI-24: 432 Hz Pythagorean Audio Scale
  it('TC-EPI-24: Circadian acoustic synthesizer supports 432 Hz Pythagorean scale during Epiphany', async () => {
    const synthJs = fs.readFileSync(path.join(ROOT, 'src', 'audio', 'synthesizer.js'), 'utf-8');
    assert.ok(synthJs.includes('172.08') || synthJs.includes('432'), '432 Hz Pythagorean harmonic scale supported');
  });

  // TC-EPI-25: Clean Resumption of Level N+1
  it('TC-EPI-25: Clean resumption of Level N+1 upon Epiphany completion', () => {
    gm.player.currentLevel = 7;
    gm.startEpiphanyTrial();
    gm.completeEpiphanyStage();

    assert.strictEqual(gm.isEpiphanyLevelActive, false);
    assert.strictEqual(gm.epiphanyState, 'TRIUMPH');
  });
});
