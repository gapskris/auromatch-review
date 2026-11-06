# AuroMatch — Implementation Review Instructions
### Run in Claude Code, against the actual codebase and any deployed build

**Purpose:** verify by *executing and reading code*, not by re-reading the specs. The specs disagree with each other in several places (documented below) — your job is to find out what the code actually does, not what any one document says it should do.

Paste findings back section by section, in plain text, in the message body. Where you can't verify something (no build available, feature not yet implemented), say so explicitly rather than inferring from the spec.

---

## 1. Scope Resolution — do this first, it gates everything else

The design documents contradict each other on the app's basic scope:
- `01_Vision.md`, `02_PRD.md`, `05_UX_Flow.md`, `07_Game_Design.md` describe **4** Garden Sanctuaries (Samadhi, Playground, Matrimandir Chamber, Lake Estate).
- `implementation_plan.md`, the 15-themes catalog, and the technical Bible describe **15**.

Grep the codebase for garden/theme definitions (level configs, `teachings_repository.json`, any `GARDENS` or `THEMES` constant). Report:
- How many gardens are actually defined/implemented right now?
- Do the implemented gardens match the 4-garden set, the 15-garden set, a subset of either, or something else entirely?
- Is there any code comment, TODO, or commit history indicating which scope is current intent?

## 2. Board Occlusion Engine
- Confirm the actual tile bounding box dimensions in code. Three documents give slightly different numbers (`core_design_dimensions.md` implies via threshold only; `AuroMatch_Detailed_Concepts_and_Specs.md` states `W=50px, H=66px` explicitly). What does the code use?
- Confirm the occlusion threshold values match spec: `W_threshold ≈ 42px`, `H_threshold ≈ 56px`.
- Verify the blocked-tile filter is actually applied: `filter: brightness(0.65) contrast(0.95)`.
- Trace what happens on a tap of a blocked tile — does it reject the tap and play the 196Hz warning tone, or silently no-op?

## 3. Tray Sorting & Match Verification
- Confirm the tray is a 7-slot structure and sorts by `flower.id` (alphabetical `localeCompare`) on every insertion.
- Confirm the triple-match check correctly identifies 3 consecutive identical IDs and removes them.
- Confirm the reshuffle fallback: when the tray reaches 7 with no match, does it actually trigger the warning chime and reshuffle remaining board tiles? Test this path directly — it's easy to leave unimplemented since it only fires in a specific failure state.

## 4. Audio Synthesis
Two documents give **different** gong specifications:
- `11_Architecture_Design.md`: single fixed 110Hz fundamental with overtones at 165Hz, 220.8Hz, 290Hz.
- `auromatch_technical_documentation.md`: adaptive dual-fundamental — 172.08Hz (morning) / 110Hz (evening).

Which does the code implement? Confirm actual oscillator frequencies and the exponential decay envelope (should be ~5.0s decay constant).

Two documents also give **different** raga/Prahar systems:
- `core_design_dimensions.md`: 4 periods (Bhairav/Sarang/Yaman/Darbari).
- `AuroMatch_Detailed_Concepts_and_Specs.md`: 5 periods (adds Bhimpalasi for afternoon).

Confirm which is implemented, and whether the time-boundary logic (system hour → scale selection) actually fires correctly at each boundary.

Confirm instrument-tile layering: matching an instrument tile should add its loop to the active drone at low gain (~0.04 max) without replacing the existing drone.

## 5. TTS & Voice Selection — likely bug
`auromatch_technical_documentation.md` Section 4.6 defines `sanctuaryMode` as `["traditional", "secular", "youth"]`. Section 4.3 of the *same document* describes voice-selection logic keyed on `userVoicePref` values `"traditional"` vs `"devotee"` — a value that doesn't appear in the `sanctuaryMode` enum it's supposedly reading.

- Find the actual voice-selection code. What variable does it read, and what values does that variable actually take?
- Is the French-accented (`fr-FR`) voice path reachable at all through the current UI, or is it dead code behind a value nothing ever sets?
- Confirm the separate `voiceTonePreference: ["english", "french_cadence"]` setting mentioned in the same section — is this the actual mechanism, and if so, does Section 4.3's logic correctly read *that* variable instead?
- Confirm slow-rate parameters are applied regardless: `rate = 0.70`, `pitch = 0.95`.

## 6. Consecration Jar — Particle Physics
Verify against `core_design_dimensions.md`'s formulas:
- Particle density: 1 per 4×4px of active text stroke.
- Initial vertical velocity: −0.5 to −2.0 px/frame (randomized).
- Gravity: 0.15 px/frame².
- Horizontal drift toward jar center: `a_x = (x_jar − x_t) × 0.005`.
- Opacity decay: `α_t = α_(t-1) × (0.95 + random(0, 0.03))`, particle removed at `α ≤ 0.01`.

Confirm the text-to-particle conversion actually reads the entered text and generates particles from character strokes, rather than a generic placeholder animation.

## 7. Data Persistence & Non-Destructive Sync
This is the highest-stakes correctness item in the app — a bug here deletes someone's private reflections.
- Confirm the version-check flow: local `auro_match_teachings` version compared against remote `version.json`.
- **Critically**: confirm the merge logic touches *only* the teachings/vocabulary keys and never writes to, resets, or overwrites `auro_match_consecrations`, `auro_match_user`, or `auro_match_unlocked_tiles`.
- Write a test: seed local consecration logs, simulate a teachings update, confirm logs survive untouched.
- Confirm the 2-second timeout fallback to offline assets actually works (kill network mid-fetch, verify no hang or crash).

## 8. Security & Encryption
- Confirm AES-256-GCM is actually used for personal data at rest (not just referenced in comments).
- Confirm the master key is written to iOS Keychain / Android Keystore, not to a plain file or localStorage alongside the encrypted data.
- **PBKDF2 iteration count**: confirm the actual value in the backup-export key derivation code. Spec says 10,000, which is below current OWASP guidance for PBKDF2-HMAC-SHA256. This is the same open item flagged in Vak's review — worth resolving once for both projects rather than twice. Not urgent pre-launch, but should be a documented decision (bump it, or explicitly accept it for now) rather than left unexamined.

## 9. Backup, Restore & Purge
- Test a full export → import round trip with a password. Confirm data integrity after restore.
- Test the Purge flow: confirm it requires typing "PURGE" verbatim, confirm it actually calls `localStorage.clear()`, drops SQLite tables, and deletes the AES key from Keychain/Keystore (not just app-level state reset).

## 10. Scout Crawler / Content Ingestion Pipeline
`implementation_plan.md` Phase 8 and the technical Bible describe a weekly GitHub Actions job that crawls Ashram sitemaps, classifies vocabulary, and commits directly to `teachings_repository.json`, which the app then auto-syncs on launch.
- Confirm whether any human-approval gate exists between crawl and commit (e.g. a PR requiring review, vs. a direct push to main).
- If there is no gate: this mirrors the exact concern already flagged for Vak's crawler — an unreviewed pipeline that can push content attributed to Sri Aurobindo or the Mother straight to devices. Flag this explicitly rather than assuming it's fine because the app is pre-launch; recommend it join the consolidated crawler-governance conversation with Vijay ji.
