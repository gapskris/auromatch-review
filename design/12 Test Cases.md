# AuroMatch: The Triple Garden of Significances — Test Cases Document

---

## 1. Test Suite A: Stacking Matching Board Engine

### TC_001: Tile Occlusion & Bounding Selection
* **Steps:**
  1. Open the board (e.g. Samadhi Garden level).
  2. Tap a tile that is visually dimmed and covered by another layer (e.g., Layer 0 tile covered by Layer 1 tile).
* **Expected Result:**
  * The board rejects the click.
  * A low, warning tone (196Hz) plays.
  * The tile remains on the board.
  * Tapping the covering Layer 1 tile successfully moves it into the tray, which automatically makes the underlying Layer 0 tile bright and active.

### TC_002: Tray Clustering & Triple Match Validation
* **Steps:**
  1. The tray contains: `[Jasmine, Lotus]`.
  2. Tap a bright, active `Jasmine` tile on the board.
* **Expected Result:**
  * The selected `Jasmine` tile slides into the tray.
  * The tray automatically sorts, resulting in: `[Jasmine, Jasmine, Lotus]`.
  * Tap a third `Jasmine` tile.
  * The tray updates to `[Jasmine, Jasmine, Jasmine, Lotus]`.
  * The three `Jasmine` tiles fade out immediately.
  * The Ashram Meditation Gong (110Hz with decay) plays.
  * The **Match Reflection Card** for Jasmine overlays the board.
  * The user is awarded $+5$ Lotus Petals.

### TC_003: Tray Overfill & Auto-Reshuffle
* **Steps:**
  1. Fill the tray with 7 unmatched tiles (e.g., all different qualities).
  2. Observe the state of the board.
* **Expected Result:**
  * The board detects the full tray (7 items) with no matches.
  * A low warning tone (196Hz) plays.
  * An alert informs the user that the garden must be re-aligned.
  * The board automatically reshuffles the remaining active tiles and clears the tray, restarting the level layout with progress intact.

---

## 2. Test Suite B: Audio & Voice Synthesis

### TC_004: Generative Raga Synth & Audio Layering
* **Steps:**
  1. Boot the application. Verify the system time is set to `20:00` (Night cycle).
  2. Complete an instrument tile match (e.g., Sitar).
* **Expected Result:**
  * The background audio initializes a deep, calming Darbari Raga drone (composed of fundamental 110Hz, 165Hz, and 220Hz oscillators).
  * Matching the Sitar tile dynamically overlays a slow, synthesized sitar loop onto the active drone, changing the ambient background in real-time.

### TC_005: Meditative Slow-Cadence TTS
* **Steps:**
  1. Open a Match Reflection Card.
  2. Select the `fr-FR` voice option in Settings.
  3. Click "Listen".
* **Expected Result:**
  * The quote is read with a soft, French-accented voice, mimicking the Mother's cadence.
  * The speech rate is noticeably slow (rate factor `0.70`).
  * Clicking "Pause" halts narration; clicking "Resume" plays the text from the last spoken word.

---

## 3. Test Suite C: Consecration Journal & Persistence

### TC_006: Consecration Dissolution & Star Map
* **Steps:**
  1. Complete a matching board.
  2. Open the Consecration Jar screen.
  3. Type in the journal: "Feeling restless today."
  4. Click "Consecrate Worry".
* **Expected Result:**
  * The text in the input box breaks apart into floating gold canvas particle dots that float downward and vanish inside the brass jar.
  * The journal saves to the encrypted LocalStorage/SQLite key `auro_match_consecrations` for the current date.
  * The user is redirected to the calendar view, where the current day's star is pulsing with a bright golden light.
  * Clicking the pulsing star displays the notes: "Feeling restless today."

### TC_007: Onboarding Path Selection & On-Device Encryption
* **Steps:**
  1. Wipe browser local storage/SQLite databases to trigger a fresh cold boot.
  2. Launch the app. On the Onboarding overlay, click "Secular Path".
  3. Complete the level and verify the headers on screens.
* **Expected Result:**
  * App detects the empty profile on boot and halts on the Onboarding Selection overlay.
  * Clicking "Secular Path" generates a fresh user profile structure, initializes settings, and enters the Sanctuary.
  * Headers on the board translate (e.g., showing "Mindful Sounds" instead of "Sanskrit Seed Words").
  * Verify that personal data keys are encrypted locally using AES-256-GCM.

### TC_008: Darshan Day Cards & Milestone Halos
* **Steps:**
  1. Adjust the device system date to `02-21` (February 21).
  2. Launch the app online or offline.
  3. After viewing the welcome screen, verify the overlays.
  4. Go to the Constellation screen and look at Day 21.
* **Expected Result:**
  * The welcome screen automatically triggers a gold-bordered Darshan Card displaying "The Mother's Birthday" and a dedicated quote by Sri Aurobindo.
  * Entering the Constellation view shows Day 21 highlighted with a pulsing golden halo (`.event-halo`).
  * Tapping the halo star slides up a bottom-sheet modal detailing the Mother's birthday milestone history.
