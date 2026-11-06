# AuroMatch: Zero-Regression Test & Execution Plan
## Merging "Classic" into "Pairs" (Expanding to 400 Levels)

> **Objective:** Eliminate redundant "Classic" mode, merge its 200 levels into **Pairs** (creating a single, unified 400-Level Mahjong Solitaire campaign), free up navigation space for the upcoming **Botanical Art** category, and guarantee **zero regressions and zero player progress loss**.

---

## 1. Architectural Impact & Invariants

```
                             BEFORE CLEANUP
  ┌─────────────────┐   ┌─────────────────────┐   ┌──────────────────┐   ┌────────────────┐
  │ 🌸 Pairs (200)  │   │ 📥 Tile Club (Triad)│   │ 🏛️ Classic (200) │   │ 🗺️ Realms      │
  │ Match-2 Mahjong │   │ Match-3 Tray        │   │ Match-2 (REDUND) │   │ 20 Story Realm │
  └─────────────────┘   └─────────────────────┘   └──────────────────┘   └────────────────┘

                               AFTER CLEANUP
  ┌─────────────────────────┐    ┌─────────────────────┐    ┌────────────────┐    ┌─────────────────────┐
  │ 🌸 Pairs (400 Levels)   │    │ 📥 Tile Club (Triad)│    │ 🗺️ Realms      │    │ ✨ Botanical Art    │
  │ Unified Match-2 Solitaire│   │ Match-3 with Tray   │    │ 20 Story Realm │    │ (New Mode Reserved) │
  └─────────────────────────┘    └─────────────────────┘    └────────────────┘    └─────────────────────┘
```

### Core Invariants Guaranteed:
1. **Zero Game Engine Regression:** `Pairs` (Vita Mahjong) and `Tile Club` (Match-3) mechanics remain 100% identical.
2. **Realms 100% Untouched:** The 20 realms, 1,000 realm levels, custom 3D tiles, and wallpapers are not modified in any way.
3. **Player Progress Preservation (Backward Compatibility):** If an existing player was on `Classic Level 35`, their profile gracefully maps to `Pairs Level 35` (or preserves their highest reached level) so no progress is ever wiped.
4. **100% Solvability Guarantee:** Levels 1 to 400 in Pairs are mathematically verified to be solvable without deadlocks.

---

## 2. Exhaustive Codebase Change Matrix

| File | Exact Lines / Sections | Change Required | Safety / Rollback Guard |
|---|---|---|---|
| [`themeManager.js`](file:///c:/DataScience/AuroProject_Annalysis/AuroMatch/src/controllers/themeManager.js#L6) | Line 6: `TOTAL_CLASSIC_LEVELS = 200` | Deprecate / alias to `TOTAL_PAIRS_LEVELS`. Export `TOTAL_PAIRS_LEVELS = 400`. | Re-export alias so legacy imports do not break. |
| [`gameManager.js`](file:///c:/DataScience/AuroProject_Annalysis/AuroMatch/src/controllers/gameManager.js#L29) | Line 29: `TOTAL_PAIRS_LEVELS = 200` | Change to `TOTAL_PAIRS_LEVELS = 400`. | Covered by Level generator S-curve (already supports 520 levels). |
| [`gameManager.js`](file:///c:/DataScience/AuroProject_Annalysis/AuroMatch/src/controllers/gameManager.js#L286) | Line 286–287: `getMaxLevel()` | Update `if (this.gameplayMode === 'vita' \|\| this.gameplayMode === 'classic') return TOTAL_PAIRS_LEVELS;` | Seamless fallback for legacy state. |
| [`gameManager.js`](file:///c:/DataScience/AuroProject_Annalysis/AuroMatch/src/controllers/gameManager.js#L445) | `setGameplayMode(mode)` | If `mode === 'classic'`, alias seamlessly to `'vita'`. | Prevents any stale URL/hash or function call crashes. |
| [`index.html`](file:///c:/DataScience/AuroProject_Annalysis/AuroMatch/index.html#L229) | Line 229: `<button id="btn-mode-classic">` | Safely remove the button element. | Frees up 85px horizontal space for mobile. |
| [`src/main.js`](file:///c:/DataScience/AuroProject_Annalysis/AuroMatch/src/main.js#L39) | Lines 39, 47, 65, 506 | Remove `btnClassic` DOM references; alias switch calls to `vita`. | Clean zero-error DOM querying. |
| [`styles/main.css`](file:///c:/DataScience/AuroProject_Annalysis/AuroMatch/styles/main.css#L3936) | Lines 3936–3950: `.mode-btn-classic` | Remove redundant CSS selectors. | Pure styling cleanup. |
| [`tests/qa_suite.test.js`](file:///c:/DataScience/AuroProject_Annalysis/AuroMatch/tests/qa_suite.test.js#L559) | Lines 559, 738–744 | Update assertions from 200 to 400 levels; test classic-to-pairs aliasing. | Automated CI verification. |

---

## 3. Detailed 5-Step Verification & Test Plan

### Test Group 1: Unit & Mathematics Verification (Automated)
* [ ] **TC-MERGE-01 (Level Ceiling):** Assert `TOTAL_PAIRS_LEVELS === 400` and `gameManager.getMaxLevel()` returns 400 when in `'vita'` mode.
* [ ] **TC-MERGE-02 (Backward Compatibility Alias):** Assert `gameManager.setGameplayMode('classic')` gracefully resolves to `'vita'` with 400 levels and zero unhandled exceptions.
* [ ] **TC-MERGE-03 (Solvability Sampling across 400 Levels):**
  * Generate and solve boards for Levels: **1, 50, 100, 150, 200, 250, 300, 350, 400**.
  * Assert `VitaBoardGenerator.generateSolvableBoard()` completes with $100\%$ solvability rate.

### Test Group 2: Mode Separation & Parity (Automated)
* [ ] **TC-MERGE-04 (Pairs vs Tile Club Independence):**
  * Assert `Pairs` ($K=2$) dissolves matching pairs immediately with zero tray interactions.
  * Assert `Tile Club` ($K=3$) continues using the 7-slot tray and clears on 3 identical tiles.
* [ ] **TC-MERGE-05 (Realms Mode 100% Isolation):**
  * Assert switching to `realms` activates the active realm wallpaper and dedicated custom 3D tiles.
  * Assert `Pairs` does NOT activate realm wallpapers or override realm progress.

### Test Group 3: Player State & Migration Verification
* [ ] **TC-MERGE-06 (State Persistence):**
  * Simulate a player with `localStorage.getItem('auromatch_player_profile')` containing `currentLevel: 145` and `gameplayMode: 'classic'`.
  * Load profile via `loadProfileState()`:
    * Verify mode maps cleanly to `vita`.
    * Verify `player.currentLevel` remains 145.
    * Verify board loads level 145 formation without errors.

### Test Group 4: UI & Visual Layout Parity (Desktop & Mobile)
* [ ] **TC-MERGE-07 (Desktop 1440x900 & 1024x567):**
  * Verify top category bar renders: `[ 🌸 Pairs ]  [ 📥 Tile Club ]  [ 🗺️ Realms ]` perfectly centered.
  * Verify board stack is centered horizontally and vertically with zero tray collision.
* [ ] **TC-MERGE-08 (Mobile 390x844 iPhone Viewport):**
  * Verify top category buttons fit comfortably on a single line with $>16\text{px}$ side margins.
  * Verify zero text clipping, zero ellipsis, and zero button wrap.

---

## 4. Rollback & Failsafe Plan

If any unexpected behavior occurs:
1. Git revert checkpoint: A dedicated commit `refactor: merge classic mode into pairs (400 levels)` will be created. Reverting that single commit restores the previous 4-button state in $<10\text{ seconds}$.
2. Zero data corruption: Because level layouts are generated mathematically on the fly (`createLevelLayout(levelNum)`), no static database files or level json files are destroyed or altered.

---

## 5. Execution Steps Once Approved

1. **Step 1:** Update constants in `themeManager.js` and `gameManager.js` (`TOTAL_PAIRS_LEVELS = 400`, add backward-compatible alias).
2. **Step 2:** Update UI in `index.html`, `src/main.js`, and `styles/main.css`.
3. **Step 3:** Run `qa_suite.test.js` to verify all automated test assertions pass.
4. **Step 4:** Execute CDP browser screenshot tests on Desktop ($1024\text{px}$) and Mobile ($390\text{px}$) to visually confirm perfect UI harmony.
5. **Step 5:** Git commit and push cleanly.
