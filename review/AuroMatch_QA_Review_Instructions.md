# AuroMatch — Game Quality & QA Review Instructions
### Companion to the Implementation and Design Reviews — run in Claude Code

**This review is about playing the whole thing, breaking it on purpose, and reading every quote it shows a real person.** The other two reviews check whether the code is sound and whether it looks right in isolated screenshots. This one checks whether a full session — start to finish, across the actual content — holds together and doesn't misattribute anything to Sri Aurobindo or the Mother along the way.

Paste findings back section by section, plain text, in the message body. Log anything that can't be tested (missing build, feature not implemented) rather than skipping silently.

---

## 1. Full Playthrough
- Play through every garden actually implemented (see Implementation Review Section 1 for the resolved count — don't assume 4 or 15, use what's actually there).
- For each garden, complete at least one full board clear, one Wisdom Card reveal, and reach the Consecration Jar.
- Note pacing: does a full session feel unhurried, or does any part (loading, transitions, the reshuffle wait) create friction that undercuts the "sanctuary" framing?

## 2. Content Accuracy Audit — highest priority
This is the item the document review couldn't resolve without a running build. Two source documents disagree with each other on the colors and spiritual significances assigned to overlapping Qualities and Flowers (see the analysis: Humility, Perseverance, Progress, Equality colors; Marigold and Periwinkle significances).

- Go through **every** Quality, Flower, Sanskrit seed, and Symbol reflection actually displayed in-app during play. Record the exact text, color, and attribution (Mother / Sri Aurobindo, book reference) shown on screen.
- Flag every instance where the displayed content doesn't clearly match either source document, or matches one but contradicts the other.
- This audit does not need to determine which version is *correct* — that requires checking against the actual SABDA-published source (*Flowers and Their Messages*, *The Mother's Symbol* pamphlets), which is a task for Gopal ji or Vijay ji, not for this review. Its job is to produce a complete, accurate inventory of what the app currently claims, so that verification step has something concrete to check.

## 3. Negative Testing
- Tap a blocked tile repeatedly — confirm it never becomes selectable through rapid tapping or timing exploits.
- Fill the tray to 7 with no match — confirm reshuffle fires reliably, not just on the first occurrence.
- Try submitting an empty Consecration Jar entry — confirm graceful handling (no crash, no silent no-op that looks like it saved).
- Try extremely long journal entries — confirm the dissolution animation and storage both handle it without breaking.
- Kill network mid-launch during a version-check — confirm the 2-second timeout fallback actually resumes offline play rather than hanging.

## 4. Darshan Day & Milestone Testing
Mock the system date to each of the 5 configured dates and confirm the correct greeting, quote, and constellation halo appear:
- Feb-21 (Mother's Birthday), Apr-24 (Mother's Final Arrival), Aug-15 (Sri Aurobindo's Birthday), Nov-24 (Siddhi Day), Dec-05 (Sri Aurobindo's Mahasamadhi).
- Confirm no false positives on adjacent dates (Feb-20, Feb-22, etc.).

## 5. Data Preservation Under Real Use
- Play several sessions across simulated days, accumulating consecration logs and unlocked tiles.
- Simulate a teachings-content update (new `version.json`). Confirm personal logs, unlocked tiles, and profile survive completely intact.
- Export a backup, clear the app state, import the backup, confirm full restoration.
- Run the Purge flow end to end; confirm it actually removes everything (re-launch should look like first install, not a soft reset).

## 6. Cross-Device & Performance
- Test at 320px width (small phone) and confirm no text overflow or layout breakage, per the `clamp()` typography spec.
- Test the desktop centered-box behavior (should stay bounded to 360–412px, not stretch full width).
- Confirm canvas/SVG animations (particles, star pulse, dissolution) hold close to 60fps — note any visible stutter, especially on the Consecration Jar animation, which is the most animation-heavy screen.
- Time cold launch to first interactive board — spec claims under 1 second; report actual.

## 7. Voice / TTS Behavior
- Test the TTS path under both onboarding paths (Traditional and whatever the actual French/devotee toggle turns out to be, per the Implementation Review's naming-bug finding).
- Confirm speech rate/pitch actually sound like `0.70`/`0.95` (noticeably slow and calm) rather than default browser TTS speed.
- If the French-accented voice is unreachable due to the naming bug, confirm that clearly rather than assuming it works because the spec describes it.

## 8. Release-Readiness Inventory
Before this app is presented for Vijay ji's review, the following need an explicit decision or sign-off — not silence:

- [ ] **Garden scope** — 4 or 15 (or other) confirmed as current intent, all specs updated to match.
- [ ] **Quality-color and flower-significance content** — verified against actual SABDA source material, not against either internal document.
- [ ] **The "Mother encouraged matching games" claim** (Section 7.1 of the Concepts doc) — sourced or removed before being used as justification to leadership.
- [ ] **sanctuaryMode / voice-selection naming bug** — fixed, and French-accented voice path confirmed reachable or intentionally removed.
- [ ] **TTS emulating the Mother's reading cadence** — reverence question raised with Vijay ji, alongside the DivineSearch "Read by Mother" labelling decision already pending.
- [ ] **Scout crawler human-review gate** — confirmed present, or flagged to join the consolidated crawler-governance conversation.
- [ ] **PBKDF2 iteration count** — documented decision (bump or accept), shared with the same decision pending for Vak.
