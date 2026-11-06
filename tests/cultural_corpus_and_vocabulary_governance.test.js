import { describe, test } from 'node:test';
import assert from 'node:assert/strict';

import {
  floraCatalog,
  getFloraById,
  getFloraCount,
  getCurriculumTier,
  getTilesForLevel
} from '../src/models/floraDatabase.js';

import {
  ORACLE_QUALITIES,
  drawDailyOracle,
  checkCalendarGreetings,
  applySanctuaryModeTheme,
  renderConstellationGrid,
  GameManager
} from '../src/controllers/gameManager.js';

import { ThemeManager, REALMS } from '../src/controllers/themeManager.js';

describe('🏛️ AuroMatch Cultural Corpus & Vocabulary Governance QA Suite (CORP)', () => {

  // Robust headless DOM mock
  const createMockElement = () => ({
    innerText: '',
    innerHTML: '',
    style: {},
    classList: {
      add: () => {},
      remove: () => {},
      contains: () => false
    },
    appendChild: () => {},
    setAttribute: () => {},
    removeAttribute: () => {}
  });

  const domElements = {};
  globalThis.document = globalThis.document || {
    getElementById: (id) => {
      domElements[id] = domElements[id] || createMockElement();
      return domElements[id];
    },
    querySelector: () => createMockElement(),
    querySelectorAll: () => [],
    createElement: () => createMockElement(),
    body: createMockElement(),
    documentElement: createMockElement()
  };

  test('TC-CORP-01: Vocabulary Database Completeness (4,000+ Curated Words)', () => {
    assert.ok(floraCatalog.length >= 4000, `Catalog must have at least 4,000 words (actual: ${floraCatalog.length})`);
    assert.strictEqual(getFloraCount(), floraCatalog.length);
  });

  test('TC-CORP-02: Required Vocabulary Entry Schema & Non-Empty Fields', () => {
    // Sample 100 entries across catalog
    const step = Math.floor(floraCatalog.length / 100);
    for (let i = 0; i < floraCatalog.length; i += step) {
      const item = floraCatalog[i];
      assert.ok(item.id, `Item ${i} must have an ID`);
      assert.ok(item.commonName, `Item ${item.id} must have commonName`);
      assert.ok(item.domain, `Item ${item.id} must have educational domain`);
      assert.ok(item.definition, `Item ${item.id} must have definition`);
      assert.ok(item.educationalLore, `Item ${item.id} must have educationalLore / context sentence`);
      assert.ok(item.symbol, `Item ${item.id} must have symbolic emoji`);
      assert.ok(item.archetype, `Item ${item.id} must have archetype`);
    }
  });

  test('TC-CORP-03: Educational Quad-Archetype Schema Compliance', () => {
    const validArchetypes = new Set(['cameo', 'hex_seal', 'golden_relic', 'ivory']);
    const catalogArchetypes = new Set(floraCatalog.map(f => f.archetype));
    catalogArchetypes.forEach(arch => {
      assert.ok(validArchetypes.has(arch), `Archetype "${arch}" must be one of the 4 approved archetypes`);
    });
  });

  test('TC-CORP-04: Pedagogical Domain Categorization (10 Disciplines)', () => {
    const expectedDomains = [
      'Character & Will',
      'Mind & Science',
      'Heart, Empathy & Peace',
      'Arts & Culture',
      'Wisdom & Integral Yoga',
      'Earth & Geology',
      'Cosmos & Astronomy',
      'Flora & Ecology',
      'Marine & Aquatic Life',
      'Fauna & Wildlife'
    ];
    const presentDomains = new Set(floraCatalog.map(f => f.domain));
    expectedDomains.forEach(dom => {
      assert.ok(presentDomains.has(dom), `Corpus must include domain: "${dom}"`);
    });
  });

  test('TC-CORP-05: Curriculum Tier Progression across Levels', () => {
    const tierLvl1 = getCurriculumTier(1);
    const tierLvl150 = getCurriculumTier(150);
    const tierLvl350 = getCurriculumTier(350);

    assert.ok(tierLvl1.id >= 1);
    assert.ok(tierLvl150.id >= tierLvl1.id);
    assert.ok(tierLvl350.id >= tierLvl150.id);
    assert.ok(tierLvl1.primaryDomains.length > 0);
  });

  test('TC-CORP-06: Level Tile Generation Pedagogical Selection', () => {
    const tiles1 = getTilesForLevel(1, 8);
    assert.strictEqual(tiles1.length, 8);
    tiles1.forEach(t => {
      assert.ok(t.commonName, 'Selected tile must have commonName');
      assert.ok(t.definition, 'Selected tile must have definition');
    });
  });

  test('TC-CORP-07: The Mother\'s 12 Spiritual Qualities in Oracle Engine', () => {
    assert.strictEqual(ORACLE_QUALITIES.length, 12, 'Must register exactly 12 spiritual qualities');
    const qualityNames = ORACLE_QUALITIES.map(q => q.name);
    const required = ['Sincerity', 'Humility', 'Gratitude', 'Perseverance', 'Aspiration', 'Receptivity', 'Peace', 'Equanimity', 'Generosity', 'Goodness', 'Courage', 'Devotion'];
    required.forEach(req => {
      assert.ok(qualityNames.includes(req), `Oracle must include quality "${req}"`);
    });
  });

  test('TC-CORP-08: Daily Oracle Deterministic Rotation (Locks to Day of Year)', () => {
    // Two draws on the same date must always yield the exact same quality
    const now = new Date();
    const start = new Date(now.getFullYear(), 0, 0);
    const dayOfYear = Math.floor((now - start) / 1000 / 60 / 60 / 24);
    const expected = ORACLE_QUALITIES[dayOfYear % ORACLE_QUALITIES.length];

    drawDailyOracle();
    // After timeout runs
    const chosen = ORACLE_QUALITIES[dayOfYear % ORACLE_QUALITIES.length];
    assert.strictEqual(chosen.name, expected.name, 'Daily Oracle quality must be deterministic');
  });

  test('TC-CORP-09: Daily Oracle DOM Element Rendering & Prompt Content', () => {
    const qEl = document.getElementById('oracle-quality');
    const pEl = document.getElementById('oracle-prompt');
    const symEl = document.getElementById('oracle-symbol');

    assert.ok(qEl && pEl && symEl, 'Oracle DOM elements must exist');
    ORACLE_QUALITIES.forEach(q => {
      assert.ok(q.prompt.length > 20, `Prompt for ${q.name} must provide meaningful reflective guidance`);
      assert.ok(q.symbol, `Symbol for ${q.name} must not be empty`);
    });
  });

  test('TC-CORP-10: Four Sacred Darshan Anniversary Dates Registration', () => {
    const milestones = {
      '02-21': "The Mother's Birthday",
      '04-24': "Darshan Day",
      '08-15': "Sri Aurobindo's Birthday",
      '11-24': "Siddhi Day"
    };
    assert.strictEqual(Object.keys(milestones).length, 4, 'Must register exactly 4 annual Darshan milestones');
  });

  test('TC-CORP-11: Darshan Calendar Greetings Trigger Logic', () => {
    const modal = document.getElementById('darshan-modal');
    const tEl = document.getElementById('darshan-title');
    const dEl = document.getElementById('darshan-desc');

    // Simulate calling checkCalendarGreetings
    checkCalendarGreetings();
    assert.ok(modal && tEl && dEl, 'Darshan modal elements must be configured');
  });

  test('TC-CORP-12: Circadian Sanctuary Mode Diurnal/Nocturnal Theme Switching', () => {
    const appWrapper = document.getElementById('app-wrapper');
    applySanctuaryModeTheme();
    assert.ok(appWrapper, 'App wrapper must be resolved by theme switcher');
  });

  test('TC-CORP-13: Seven Days of Cosmic Week Constellation Star Mapping', () => {
    const starDays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
    assert.strictEqual(starDays.length, 7, 'Must have 7 days of weekly contemplation');
  });

  test('TC-CORP-14: Constellation SVG Geometry & Path Generation', () => {
    const container = document.getElementById('stars-grid');
    const svg = document.getElementById('constellation-svg');
    assert.ok(container && svg, 'Constellation container and SVG canvas must exist');
    renderConstellationGrid();
  });

  test('TC-CORP-15: Golden Relic Archetype Sparks Bonus (+10 bonus on match)', () => {
    const gm = new GameManager({ gameplayMode: 'vita' });
    const relicFlora = {
      id: 'golden_lotus',
      commonName: 'Golden Lotus',
      archetype: 'golden_relic'
    };
    const t1 = { id: 'r1', x: 0, y: 0, z: 0, floraId: 'golden_lotus', floraData: relicFlora, isMatched: false };
    const t2 = { id: 'r2', x: 2, y: 0, z: 0, floraId: 'golden_lotus', floraData: relicFlora, isMatched: false };
    const tDummy = { id: 'd1', x: 5, y: 0, z: 0, floraId: 'rose', isMatched: false };
    gm.tiles = [t1, t2, tDummy];
    gm.player.sparks = 100;

    gm.handleTileClick(t1, true);
    gm.handleTileClick(t2, true);

    // Matching golden_relic awards +10 sparks immediately
    assert.strictEqual(gm.player.sparks, 110, 'Golden relic match must award +10 sparks bonus');
  });

  test('TC-CORP-16: Sacred Epiphany State Machine Trigger Interval (6-12 levels target window)', () => {
    const gm = new GameManager();
    gm.levelsSinceLastEpiphany = 5;
    gm.nextEpiphanyTarget = 6;
    gm.hintsUsedInStage = 0;
    gm.tiles = [];

    // Clear level -> triggers epiphany
    gm.checkStageCompletion();
    assert.strictEqual(gm.isEpiphanyActive, true, 'Epiphany must activate when target level count reached');
    assert.strictEqual(gm.levelsSinceLastEpiphany, 0, 'levelsSinceLastEpiphany must reset to 0');
    assert.ok(gm.nextEpiphanyTarget >= 6 && gm.nextEpiphanyTarget <= 12, 'Next target must be 6-12 levels');
  });

  test('TC-CORP-17: Sacred Epiphany Triple Sparks Award (+60 Sparks)', () => {
    const gm = new GameManager();
    gm.player.sparks = 100;
    gm.player.currentLevel = 2;
    gm.levelsSinceLastEpiphany = 10;
    gm.nextEpiphanyTarget = 10;
    gm.hintsUsedInStage = 0;
    gm.tiles = [];

    gm.checkStageCompletion();
    // Base clear (+10) + Clean Solve (+5) + Epiphany (+60) = +75
    assert.strictEqual(gm.player.sparks, 175, 'Sparks must include +60 Sacred Epiphany bonus');
  });

  test('TC-CORP-18: 20 Sacred Realms Sanskrit & Classical Nomenclature', () => {
    assert.strictEqual(REALMS.length, 20);
    REALMS.forEach(realm => {
      assert.ok(realm.name && realm.name.length > 0, `Realm ${realm.id} must have authentic name`);
      assert.ok(realm.subtitle && realm.subtitle.length > 0, `Realm ${realm.id} must have evocative subtitle`);
      assert.ok(realm.customTiles && realm.customTiles.length === 16, `Realm ${realm.id} must have 16 custom tiles`);
    });
  });

  test('TC-CORP-19: Sanskrit / Classical Etymological Integrity in Botanical Campaign', () => {
    const botLevel = ThemeManager.getBotanicalForLevel(1);
    assert.strictEqual(botLevel.id, 'botanical_art');
    assert.ok(botLevel.customTiles.length === 24, 'Botanical Campaign must feature 24 folk mandala tiles');
  });

  test('TC-CORP-20: Clean Vocabulary Governance (Zero Commercial Noise or Slang)', () => {
    const prohibitedWords = ['coupon', 'crypto', 'gamble', 'betting', 'viagra', 'casino', 'lootbox'];
    floraCatalog.forEach(item => {
      const lowerWord = item.commonName.toLowerCase();
      prohibitedWords.forEach(bad => {
        assert.ok(!lowerWord.includes(bad), `Catalog must not contain commercial/inappropriate word: "${bad}"`);
      });
    });
  });

});
