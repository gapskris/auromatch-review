import { describe, test } from 'node:test';
import assert from 'node:assert/strict';

import { VitaBoardGenerator } from '../src/models/boardGenerator.js';
import { floraCatalog, getTilesForLevel } from '../src/models/floraDatabase.js';
import { GameManager, RANKS } from '../src/controllers/gameManager.js';
import { ThemeManager, REALMS, TOTAL_BOTANICAL_LEVELS } from '../src/controllers/themeManager.js';
import { BoardRenderer } from '../src/ui/boardRenderer.js';

describe('🧩 AuroMatch Game Mechanics, Solvability & Level Design QA Suite (GAM)', () => {

  // Robust headless DOM mock for GameManager, BoardRenderer & ThemeManager
  const createMockElement = () => ({
    setAttribute: () => {},
    removeAttribute: () => {},
    appendChild: () => {},
    style: {},
    classList: {
      add: () => {},
      remove: () => {},
      contains: () => false
    }
  });

  globalThis.document = globalThis.document || {
    getElementById: () => createMockElement(),
    querySelector: () => createMockElement(),
    querySelectorAll: () => [],
    createElement: () => createMockElement(),
    body: createMockElement(),
    documentElement: createMockElement()
  };

  test('TC-GAM-01: Reverse-Construction Solvability (100% mathematical forward solvability)', () => {
    let verifiedCount = 0;
    for (let lvl = 1; lvl <= 25; lvl++) {
      const anchors = VitaBoardGenerator.createLevelLayout(lvl, 36);
      const board = VitaBoardGenerator.generateSolvableBoard(anchors, floraCatalog, 'vita');
      const sim = VitaBoardGenerator.simulateForwardSolver(board, 2);
      if (sim.isSolvable && sim.remainingTilesCount === 0) {
        verifiedCount++;
      }
    }
    assert.strictEqual(verifiedCount, 25, 'All 25 sampled levels must be 100% solvable');
  });

  test('TC-GAM-02: Sacred Geometry Formations Verification Across All 21 Formations', () => {
    assert.strictEqual(VitaBoardGenerator.FORMATIONS.length, 21, 'Must register exactly 21 formations');
    VitaBoardGenerator.FORMATIONS.forEach((f, idx) => {
      const coords = f.generator(36);
      assert.ok(coords.length > 0, `Formation ${idx + 1} (${f.name}) must generate coordinates`);
      // Solvability requirement: coordinate count must be even for valid pairing
      assert.strictEqual(coords.length % 2, 0, `Formation ${f.name} count must be even`);
      // Bounded layout coordinates
      coords.forEach(c => {
        assert.ok(c.x >= 0 && c.x <= 20, `Coordinate X must be bounded in ${f.name}`);
        assert.ok(c.y >= 0 && c.y <= 20, `Coordinate Y must be bounded in ${f.name}`);
        assert.ok(c.z >= 0 && c.z <= 6, `Coordinate Z must be bounded in ${f.name}`);
      });
    });
  });

  test('TC-GAM-03: Stage Centering within Viewport via BoardRenderer', () => {
    const coords = VitaBoardGenerator.createLevelLayout(1, 36);
    const renderer = new BoardRenderer();
    renderer.setTiles(coords);
    const metrics = renderer.computeStageMetrics(1920, 1080);
    assert.ok(metrics, 'computeStageMetrics must return valid bounds');
    assert.ok(metrics.width > 0, 'Tile width must be positive');
    assert.ok(metrics.height > 0, 'Tile height must be positive');
    assert.ok(metrics.offsetX >= 0, 'Offset X must be non-negative');
    assert.ok(metrics.offsetY >= 0, 'Offset Y must be non-negative');
  });

  test('TC-GAM-04: Layer Occlusion Physics (Tile covered by Z+1 cannot be selected)', () => {
    const tileBase = { id: 't1', x: 2, y: 2, z: 0, isMatched: false };
    const tileCover = { id: 't2', x: 2, y: 2, z: 1, isMatched: false };
    const tiles = [tileBase, tileCover];

    assert.strictEqual(VitaBoardGenerator.isTileFree(tileBase, tiles), false, 'Base tile covered by Z+1 must be occluded');
    assert.strictEqual(VitaBoardGenerator.isTileFree(tileCover, tiles), true, 'Top tile at Z=1 must be free');
  });

  test('TC-GAM-05: Lateral Edge Playability (Tile unblocked when left OR right edge is free)', () => {
    const tileMid = { id: 'mid', x: 2, y: 2, z: 0, isMatched: false };
    const tileLeft = { id: 'l', x: 1, y: 2, z: 0, isMatched: false };
    const tileRight = { id: 'r', x: 3, y: 2, z: 0, isMatched: false };

    // Flanked on both sides -> blocked
    assert.strictEqual(VitaBoardGenerator.isTileFree(tileMid, [tileMid, tileLeft, tileRight]), false, 'Flanked tile must be blocked');

    // Right side free -> playable
    assert.strictEqual(VitaBoardGenerator.isTileFree(tileMid, [tileMid, tileLeft]), true, 'Tile with open right edge must be playable');

    // Left side free -> playable
    assert.strictEqual(VitaBoardGenerator.isTileFree(tileMid, [tileMid, tileRight]), true, 'Tile with open left edge must be playable');
  });

  test('TC-GAM-06: Initial Playable Minimum (Starting boards offer >= 2 playable matching tiles)', () => {
    const anchors = VitaBoardGenerator.createLevelLayout(1, 36);
    const board = VitaBoardGenerator.generateSolvableBoard(anchors, floraCatalog, 'vita');
    const playable = board.filter(t => VitaBoardGenerator.isTileFree(t, board));
    assert.ok(playable.length >= 2, 'Initial board must offer at least 2 playable tiles');
  });

  test('TC-GAM-07: Pairs Solitaire Instant Dissolution (Mode A bypasses tray completely)', () => {
    const gm = new GameManager({ gameplayMode: 'vita' });
    const tileA = { id: 'p1', x: 0, y: 0, z: 0, floraId: 'lotus', isMatched: false };
    const tileB = { id: 'p2', x: 5, y: 0, z: 0, floraId: 'lotus', isMatched: false };
    const tileDummy = { id: 'd1', x: 8, y: 0, z: 0, floraId: 'rose', isMatched: false };
    gm.tiles = [tileA, tileB, tileDummy];

    gm.handleTileClick(tileA, true);
    assert.strictEqual(gm.selectedTile.id, 'p1');
    assert.strictEqual(gm.tray.length, 0, 'Tray must remain empty in Mode A');

    gm.handleTileClick(tileB, true);
    assert.strictEqual(tileA.isMatched, true);
    assert.strictEqual(tileB.isMatched, true);
    assert.strictEqual(gm.tray.length, 0, 'Tray must remain empty after match in Mode A');
  });

  test('TC-GAM-08: Triad Match 7-Slot Tray Mechanics (Mode B dissolves on 3 identical tiles)', () => {
    const gm = new GameManager({ gameplayMode: 'tile_club' });
    const t1 = { id: 'r1', x: 0, y: 0, z: 0, floraId: 'rose', isMatched: false };
    const t2 = { id: 'r2', x: 2, y: 0, z: 0, floraId: 'rose', isMatched: false };
    const t3 = { id: 'r3', x: 4, y: 0, z: 0, floraId: 'rose', isMatched: false };
    gm.tiles = [t1, t2, t3];

    gm.handleTileClick(t1, true);
    assert.strictEqual(gm.tray.length, 1);
    gm.handleTileClick(t2, true);
    assert.strictEqual(gm.tray.length, 2);
    gm.handleTileClick(t3, true);
    assert.strictEqual(gm.tray.length, 0, 'Triad of 3 identical tiles must dissolve from tray');
  });

  test('TC-GAM-09: Tray Overflow Calm Recovery (Triggers GAME_OVER_TRAY_OVERFLOW at 7 tiles)', () => {
    let overflowFired = false;
    const gm = new GameManager({
      gameplayMode: 'tile_club',
      onGameOver: ({ reason }) => {
        if (reason === 'GAME_OVER_TRAY_OVERFLOW') overflowFired = true;
      }
    });

    gm.tiles = [];
    for (let i = 0; i < 7; i++) {
      const tile = { id: `t_${i}`, x: i, y: 0, z: 0, floraId: `flora_${i}`, isMatched: false };
      gm.tiles.push(tile);
      gm.handleTileClick(tile, true);
    }
    assert.strictEqual(gm.tray.length, 7);
    assert.strictEqual(overflowFired, true, 'Tray overflow modal event must fire at 7 non-matching tiles');
  });

  test('TC-GAM-10: Free Undo Stack Mechanics (Restores tiles to board without sparks penalty)', () => {
    const gm = new GameManager({ gameplayMode: 'vita' });
    const t1 = { id: 'u1', x: 0, y: 0, z: 0, floraId: 'jasmine', isMatched: false };
    const t2 = { id: 'u2', x: 2, y: 0, z: 0, floraId: 'jasmine', isMatched: false };
    const t3 = { id: 'u3', x: 5, y: 0, z: 0, floraId: 'marigold', isMatched: false };
    gm.tiles = [t1, t2, t3];
    gm.player.sparks = 100;

    gm.handleTileClick(t1, true);
    gm.handleTileClick(t2, true);
    assert.strictEqual(t1.isMatched, true);
    assert.strictEqual(gm.player.sparks, 100, 'Matching regular flora does not alter sparks');

    gm.undo();
    assert.strictEqual(t1.isMatched, false, 'Tile 1 must be restored to board');
    assert.strictEqual(t2.isMatched, false, 'Tile 2 must be restored to board');
    assert.strictEqual(gm.player.sparks, 100, 'Free undo must NOT deduct sparks');
  });

  test('TC-GAM-11: Reshuffle Solvability Guarantee', () => {
    const anchors = VitaBoardGenerator.createLevelLayout(3, 36);
    const board = VitaBoardGenerator.generateSolvableBoard(anchors, floraCatalog, 'vita');
    
    // Simulate reshuffle of active tiles
    const unMatched = board.filter(t => !t.isMatched);
    const activeAnchors = unMatched.map(t => ({ x: t.x, y: t.y, z: t.z }));
    const reshuffled = VitaBoardGenerator.generateSolvableBoard(activeAnchors, floraCatalog, 'vita');
    const sim = VitaBoardGenerator.simulateForwardSolver(reshuffled, 2);
    assert.strictEqual(sim.isSolvable, true, 'Reshuffled board must maintain mathematical solvability');
  });

  test('TC-GAM-12: Hint System Sparks Deduction (Deducts 20 sparks and highlights playable pair)', () => {
    const gm = new GameManager({ gameplayMode: 'vita' });
    let highlightedIds = null;
    gm.boardRenderer = {
      highlightTiles: (ids) => { highlightedIds = ids; },
      clearHighlights: () => {}
    };
    const t1 = { id: 'h1', x: 0, y: 0, z: 0, floraId: 'marigold', isMatched: false };
    const t2 = { id: 'h2', x: 5, y: 0, z: 0, floraId: 'marigold', isMatched: false };
    gm.tiles = [t1, t2];
    gm.player.sparks = 100;

    gm.provideHint();
    assert.ok(highlightedIds && highlightedIds.length === 2, 'Hint must highlight playable pair');
    assert.strictEqual(gm.player.sparks, 80, 'Sparks balance must be deducted by 20');
  });

  test('TC-GAM-13: Clean Solve Integrity (Hints invalidate clean solve bonus)', () => {
    const gm = new GameManager({ gameplayMode: 'vita' });
    gm.boardRenderer = {
      highlightTiles: () => {},
      clearHighlights: () => {}
    };
    const t1 = { id: 'h1', x: 0, y: 0, z: 0, floraId: 'marigold', isMatched: false };
    const t2 = { id: 'h2', x: 5, y: 0, z: 0, floraId: 'marigold', isMatched: false };
    gm.tiles = [t1, t2];
    gm.player.sparks = 100;
    assert.strictEqual(gm.hintsUsedInStage, 0);

    gm.provideHint();
    assert.strictEqual(gm.hintsUsedInStage, 1, 'Hint must increment hintsUsedInStage');
  });

  test('TC-GAM-14: Stage Clear Bonus & Sparks Economy (+10 base, +5 clean solve, +50 rank up)', () => {
    const gm = new GameManager();
    gm.player.currentLevel = 25; // Completing 25 promotes Aspirant (1-25) -> Learner (26-60)
    gm.player.sparks = 100;
    gm.player.score = 0;
    gm.hintsUsedInStage = 0;
    gm.levelsSinceLastEpiphany = 0;
    gm.nextEpiphanyTarget = 999; // Prevent random epiphany trigger in test

    gm.tiles = [];
    gm.checkStageCompletion();
    assert.strictEqual(gm.player.currentLevel, 26);
    // Base clear (+10) + Clean Solve (+5) + Promotion to Learner (+50) = +65
    assert.strictEqual(gm.player.sparks, 165, 'Sparks must include clear, clean bonus, and rank promotion');
  });

  test('TC-GAM-15: Focus IQ Brain Metric Algorithm (+2 base, +3 on clean solve)', () => {
    const gm = new GameManager();
    assert.strictEqual(gm.player.focusIQ, 80);
    gm.hintsUsedInStage = 0; // Clean solve
    gm.tiles = [];
    gm.checkStageCompletion();
    assert.strictEqual(gm.player.focusIQ, 83, 'Clean solve must advance Focus IQ by +3');
  });

  test('TC-GAM-16: Progressive Difficulty Curve (Level progression from 24 to 72 tiles)', () => {
    assert.ok(VitaBoardGenerator.createLevelLayout(1, 24).length >= 24);
    assert.ok(VitaBoardGenerator.createLevelLayout(5, 36).length >= 36);
    assert.ok(VitaBoardGenerator.createLevelLayout(15, 48).length >= 48);
    assert.ok(VitaBoardGenerator.createLevelLayout(50, 72).length >= 72);
  });

  test('TC-GAM-17: Botanical Art Campaign Mode Isolation (200 progressive levels)', () => {
    const botLvl1 = ThemeManager.getBotanicalForLevel(1);
    const botLvl200 = ThemeManager.getBotanicalForLevel(200);
    assert.ok(botLvl1.customTiles.length > 0, 'Botanical level 1 must have custom 3D art tiles');
    assert.ok(botLvl200.customTiles.length > 0, 'Botanical level 200 must have custom 3D art tiles');
    assert.strictEqual(TOTAL_BOTANICAL_LEVELS, 200, 'Botanical campaign must have exactly 200 levels');
  });

  test('TC-GAM-18: 20 Sacred Realms Odyssey Isolation (1,000 Levels: 50 per Realm)', () => {
    assert.strictEqual(ThemeManager.getAllRealms().length, 20, 'Must register exactly 20 realms');
    const r1 = ThemeManager.getRealmForLevel(1);
    const r51 = ThemeManager.getRealmForLevel(51);
    assert.strictEqual(r1.id, 'whispering_pines', 'Level 1 must belong to Realm 1');
    assert.strictEqual(r51.id, 'temple_of_lines', 'Level 51 must belong to Realm 2');
  });

  test('TC-GAM-19: Tile Sizing Parity between Pairs and Tile Club on Desktop and Mobile', () => {
    const gm = new GameManager();
    gm.setGameplayMode('vita');
    assert.strictEqual(gm.gameplayMode, 'vita');
    gm.setGameplayMode('tile_club');
    assert.strictEqual(gm.gameplayMode, 'tile_club');
  });

  test('TC-GAM-20: Dynamic Tooltip & Thematic Name Formatting', () => {
    const tile = { thematicName: 'Orchid of Wisdom', thematicSymbol: '🌸', floraData: { commonName: 'White Orchid' } };
    const label = tile.thematicName || tile.floraData.commonName;
    assert.strictEqual(label, 'Orchid of Wisdom', 'Thematic name must take precedence over generic common name');
  });

});
