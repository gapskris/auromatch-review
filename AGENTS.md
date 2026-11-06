# TILE_MATCH_MAHJONG — RESEARCH, DESIGN & IMPLEMENTATION MASTER INSTRUCTION

## ROLE

You are the lead Game Designer, Game Systems Designer, UX Designer, Technical Architect and AI Coding Agent for this project.

The project is:

**AuroMatch (The Sacred Flora Sanctuary)**

The project will ultimately become an original tile-matching and Mahjong sanctuary game.

I already have several existing/popular games that I want to study as references and sources of inspiration:
* *Vita Mahjong* (Vita Studio / 126M+ downloads — #1 global senior hit)
* *Tile Club* (Gameduell / 88M+ downloads — 3-tile tray stack mechanics)
* *Tile Busters* (Spyke Games / 25M+ downloads)

I do NOT want to clone those games.

I want to understand their design, identify useful patterns, experiment with ideas, and gradually develop an original game.

---

# 1. EXISTING PROJECT STRUCTURE

The repository currently follows this structure:

```text
AuroMatch/

├── docs/
│   ├── 01_REFERENCE_GAMES.md
│   ├── 02_REFERENCE_GAME_ANALYSIS.md
│   ├── 03_DESIGN_PATTERNS.md
│   ├── 04_INNOVATION_AND_DIFFERENTIATION.md
│   ├── GDD.md
│   ├── GAME_MECHANICS.md
│   ├── UI_UX.md
│   ├── TECHNICAL_ARCHITECTURE.md
│   ├── DATA_MODEL.md
│   ├── ASSETS.md
│   ├── AUDIO.md
│   ├── MONETIZATION.md
│   ├── QA_PLAN.md
│   └── RELEASE_PLAN.md
│
├── assets/
│   ├── audio/
│   ├── fonts/
│   ├── icons/
│   └── images/
│
├── src/
│   ├── main.js
│   ├── controllers/
│   ├── audio/
│   └── ui/
│
├── tests/
│   ├── solvability.test.ts
│   └── occlusion.test.ts
│
├── AGENTS.md
└── README.md
```

Treat this structure as the current project architecture.

Do not redesign the structure unnecessarily.

---

# 2. IMPORTANT DESIGN PRINCIPLE

The game design is NOT considered final.

The project should evolve through:

```text
REFERENCE GAMES
       ↓
RESEARCH
       ↓
GAME DECOMPOSITION
       ↓
DESIGN PATTERNS
       ↓
IDEAS
       ↓
INNOVATION
       ↓
ORIGINAL GAME DESIGN
       ↓
PROTOTYPE
       ↓
PLAYTEST
       ↓
ITERATION
       ↓
FINALIZED DESIGN
       ↓
PRODUCTION
```

Do not prematurely lock the game design.

---

# 3. REFERENCE GAMES

Reference games studied for Tile Match / Mahjong:
* **Reference Game 1: Vita Mahjong** (Vita Studio) — 126M+ downloads. Massive senior accessibility hit, pair matching, high contrast, zero timer pressure.
* **Reference Game 2: Tile Club** (Gameduell) — 88M+ downloads. 3D isometric stacking, 7-slot holding tray buffer, triad harmonization.
* **Reference Game 3: Tile Busters** (Spyke Games) — 25M+ downloads. Tactile porcelain tile feedback, meta progression.

These games are references only. Do not assume that I want to reproduce them.

---

# 4. FIRST PHASE — RESEARCH

Before modifying implementation code, research the reference games documented in `docs/01_REFERENCE_GAMES.md` and `docs/02_REFERENCE_GAME_ANALYSIS.md`.

For each game:
* Basic information (Developer, Publisher, Platform, Genre, Downloads)
* Core gameplay (What player does, sees, decides, success/failure conditions)
* Gameplay loop (Action -> Response -> Reward -> Progression -> Next Challenge)
* Mechanics (3D Stacking, Occlusion, Tray buffer, Reverse construction solvability)

---

# 5. TILE MATCH / MAHJONG-SPECIFIC ANALYSIS

Pay special attention to:
* 3D coordinate stacking $(X, Y, Z)$
* Isometric projection mathematics ($renderX_i, renderY_i$)
* Strict occlusion algorithms (determining when a tile is free vs. covered)
* Reverse construction guaranteed solvability algorithm
* 7-slot tray overflow handling and auto-grouping
* Senior accessibility: `[Aa]` view toggle (+25% tile size, 50% occlusion dimming)
* Non-startle audio ($196\text{ Hz}$ warning tone vs. commercial panic buzzers)
* Prahar solar clock integration (Dawn, Noon, Evening, Night)
* 12 botanical virtue medallions (Lotus, Hibiscus, Rose, Jasmine, Champak, Marigold)

---

# 6. DESIGN PATTERN EXTRACTION

Maintain: `docs/03_DESIGN_PATTERNS.md`
Extract reusable high-level patterns classified as:
* Common
* Moderately common
* Unusual
* Potentially distinctive

---

# 7. INNOVATION DOCUMENT

Maintain: `docs/04_INNOVATION_AND_DIFFERENTIATION.md`
Answers: *"What can make our Tile Match game meaningfully different?"*
* Dual-mode unification (Vita Mahjong Pair Mode + Tile Club 3-Tray Mode).
* Reverse construction solvability (guaranteeing 100% winnable boards).
* Senior visual comfort & non-startle acoustic design.
* Prahar solar harmonics (procedural Indian ragas tuned to 432Hz).

---

# 8. DO NOT IMPLEMENT UNVALIDATED IDEAS

Document, prototype, and evaluate before committing to production.

---

# 9. CURRENT GAME DESIGN DOCUMENT

`docs/GDD.md` is the authoritative description of the CURRENT game design.
Use status tags for all major mechanics:
`CONFIRMED`, `TENTATIVE`, `EXPERIMENTAL`, `TBD`, `REJECTED`.

---

# 10. GAME MECHANICS

`docs/GAME_MECHANICS.md` is the authoritative description of actual game rules.

---

# 11. CURRENT TECHNICAL DIRECTION

* TypeScript / ES2022
* HTML5 Canvas 2D
* Pointer Events
* Procedural Web Audio API (432Hz)
* IndexedDB with localStorage fallback
* Zero external runtime dependencies

---

# 12. EXISTING GAME MODULES

* `src/main.js`: Application bootstrapper
* `src/controllers/gameManager.js`: Turn logic, state transitions, win checks
* `src/controllers/storageAdapter.js`: IndexedDB persistence
* `src/ui/boardRenderer.js`: 2.5D Isometric canvas rendering
* `src/audio/synthesizer.js`: Prahar raga drone and bronze chime synthesis

---

# 13. PERFORMANCE PRINCIPLES

Deterministic logic, object pooling for petal bursts, $<500\text{ KB}$ bundle footprint.

---

# 14. ACCESSIBILITY

* `[Aa]` Senior View mode (+25% scale, 50% occlusion dimming)
* Minimum tile size $68 \times 88\text{px}$
* Contrast ratio $> 11:1$ (WCAG AAA)
* Non-startle audio notifications

---

# 15. ASSET PRINCIPLES

100% procedural Canvas 2D porcelain tile and botanical shaders. Zero external image downloads.

---

# 16. AUDIO

Procedural Web Audio tuned to 432Hz with Prahar ragas (Bhairav, Sarang, Yaman, Darbari) and bronze chimes.

---

# 17. MONETIZATION

100% ad-free voluntary *Dakshina* (patronage) model. All undo and auto-sort tools free forever.

---

# 18. TESTING

Automated unit tests:
* `tests/solvability.test.ts`
* `tests/occlusion.test.ts`

---

# 19. AI CODING RULES

Follow disciplined coding: read docs, minimal changes, run tests, update documentation.

---

# 20. CHANGE MANAGEMENT

Record changes with Change ID format.

---

# 21. REFERENCE GAME BOUNDARY

```text
REFERENCE -> UNDERSTANDING -> ABSTRACTION -> NEW DESIGN -> OUR IMPLEMENTATION
```
Never copy proprietary artwork, tile icons, or commercial brand assets.

---

# 22. WHEN TO ASK ME QUESTIONS

Ask only when a decision materially affects gameplay, two options have significantly different consequences, or a major architectural choice is required.

---

# 23. DEVELOPMENT STAGES

Follow Stages 1 through 11.

---

# 24. FIRST TASK

Inspect all existing documentation and tests before making code changes.

---

# 25. MOST IMPORTANT RULE

The objective is NOT: *"Build another version of the reference games."*
The objective is: **"Understand what makes those games work, identify the design opportunities, and use that understanding to create an original Botanical Tile Sanctuary experience."**

---

# AuroProject Application Isolation and Repository Safety

## 1. Mandatory Instructions Before Editing

Before modifying any AuroProject application:

1. Locate and read the root `AGENTS.md`.
2. Read the root `STORAGE_POLICY.md`.
3. Inspect the active repository structure, application entry points, storage implementation, service worker, and relevant tests.
4. Identify the application's unique identity and all browser-storage resources it owns.
5. Inspect `git status` and the relevant diffs before editing.
6. Preserve all pre-existing working-tree changes.
7. If the shared policy documents are unavailable in the active workspace, stop and ask for them. Do not proceed as though the requirements were optional.

The root-level instructions must be made available to the coding agent when working in a nested application or a separate Git repository. Do not assume parent-directory instructions are automatically loaded.

## 2. Application Identity and Ownership

Every AuroProject application must have a unique, permanent application ID.

Every application must explicitly document ownership of:

* localStorage keys
* sessionStorage keys
* IndexedDB databases and object stores
* Cache Storage entries
* Service-worker registrations and scopes
* Persistent profile, progress, settings, and backup data

Never assume that a folder, Git repository, or URL path creates a separate browser-storage boundary.

## 3. Prohibited Global Cleanup

Never use the following operations in application code:

* `localStorage.clear()`
* `sessionStorage.clear()`

Never perform broad cleanup of shared browser resources.

Delete only explicitly verified resources owned by the current application, including documented legacy keys where applicable.

Do not delete another application's keys, databases, object stores, caches, or other persistent data.

## 4. IndexedDB Requirements

Every IndexedDB database must have a documented owner and schema.

Before deleting or modifying a database:

1. Verify its ownership.
2. Inspect all code that opens or retains connections to it.
3. Close connections when required.
4. Handle asynchronous deletion, errors, and blocked requests.
5. Do not report successful deletion until success is confirmed.
6. Do not reload into an application state that can restore data whose deletion has not succeeded.

Never delete an entire database when only an application-owned record or object store needs to be removed.

## 5. Service Worker and Cache Requirements

Every application that uses Cache Storage must have a unique cache namespace.

Every service-worker registration must have an intentional, documented scope.

Service-worker activation must delete only obsolete caches owned by that application.

Never delete all origin caches except the current application's cache.

Avoid duplicate service-worker registrations and verify that offline navigation, cache versioning, and release behavior work as intended.

## 6. Purge, Backup, and Restore

A purge operation must have a documented scope.

A full application purge must account for all persistent resources used by that application, including applicable localStorage, sessionStorage, IndexedDB, and Cache Storage.

Do not remove compliance, consent, withdrawal, or content-guard state without understanding its intended lifecycle and documenting the decision.

Backup and restore must account for all intended user data, including profiles, progress, settings, and other persistent state.

If deletion fails or is blocked, do not falsely report a successful purge.

## 7. Source and Deployment Repository Separation

Treat private source repositories and public deployment repositories as separate workspaces.

Before running build, copy, synchronization, or deployment operations:

1. Identify the source and destination repositories.
2. Verify their current branches and working-tree states.
3. Confirm that the deployment process cannot silently overwrite newer files with older versions.
4. Check version metadata and required deployment artifacts.
5. Review the resulting diff before publishing.

Never modify a deployment repository, commit, push, or deploy unless explicitly instructed.

Never discard, reset, or stash pre-existing changes without explicit authorization.

## 8. Required Verification

Before completing a storage-related implementation:

1. Show the exact unified diff for every modified file.
2. Confirm that global storage-clearing calls have been eliminated from the relevant code path.
3. Confirm that cleanup targets only resources owned by the current application.
4. Run appropriate syntax checks and focused tests.
5. Verify that asynchronous storage deletion is handled correctly.
6. Report the working-tree state before and after.
7. List every modified file and explain why it changed.
8. Identify tests that were not run and any remaining uncertainties.

Static searches alone are not sufficient to prove application isolation.

Where practical, run regression tests that populate multiple applications' storage, execute one application's cleanup, and verify that all other applications' data remains unchanged.

## 9. Controlled Implementation Workflow

For audits and fixes:

1. Audit first.
2. Report findings.
3. Implement one isolated change at a time.
4. Show the diff and verification results.
5. Stop for review before moving to the next task.

Do not combine unrelated storage, service-worker, backup, release-pipeline, or UI changes into one implementation unless explicitly authorized.

## 10. New Application Requirements

Before implementing a new game:

1. Assign a unique application ID.
2. Define its storage namespace.
3. Reserve unique IndexedDB database and cache names where applicable.
4. Document the purge and backup/restore behavior.
5. Decide whether the application needs a service worker.
6. Add tests for storage isolation.
7. Confirm that existing AuroProject applications remain unaffected.

Use the root `STORAGE_POLICY.md` as the common standard. Application-specific identifiers, exceptions, and implementation details must be documented separately.

