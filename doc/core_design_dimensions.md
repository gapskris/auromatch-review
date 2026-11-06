# AuroMatch: The Triple Garden of Significances — Functional & Non-Functional Requirements

---

## 1. Functional Requirements

### 1.1 The Stacking Matching Board (Puzzle Engine)
* **3D Coordinate Generation:** The board must render tiles on coordinates `(x, y, layer)`. Layers are stacked sequentially (Layer 0 at bottom, Layer 3 at top).
* **Occlusion Verification (Blocked State):**
  * A tile at layer $L$ is blocked if any active tile at layer $L' > L$ overlaps it.
  * Overlap occurs if $\left| x_{other} - x_{tile} \right| < W_{\text{threshold}}$ and $\left| y_{other} - y_{tile} \right| < H_{\text{threshold}}$, where $W_{\text{threshold}} = 42\text{ px}$ and $H_{\text{threshold}} = 56\text{ px}$.
  * Blocked tiles must render with a darker, desaturated filter (`filter: brightness(0.65) contrast(0.95)`) and be unclickable.
* **Tray Navigation & Sorting:**
  * Clicking an unblocked tile slides it dynamically from the board into a 7-slot tray at the top.
  * The tray array is sorted alphabetically by tile ID on every tap:
    ```javascript
    gameState.tray.push(selectedTile);
    gameState.tray.sort((a, b) => a.flower.id.localeCompare(b.flower.id));
    ```
  * Sorting ensures identical tiles cluster adjacent to each other.
* **Triple Matching & Removal:**
  * The engine checks the sorted tray for three consecutive identical tiles.
  * If found, they are removed (faded out) from the tray, and a **Match Reflection Card** overlays the board.
* **Fail State & Reshuffle:**
  * If the tray reaches 7 tiles and no match is found, the board triggers a warning chime and reshuffles the remaining active tiles, placing them back on coordinates.
* **Sound Synthesis:**
  * Completing a match synthesizes an authentic **Ashram Meditation Gong** tone (110Hz fundamental with overtones at 165Hz, 220.8Hz, and 290Hz) decaying exponentially over 5 seconds.
  * Tapping a blocked tile triggers a low warning tone (196Hz).

### 1.2 The Teachings Module (Match Reflections)
* **wisdom Cards:** Glassmorphic modal overlays showing the spiritual description, common name, botanical name, and quotes by Sri Aurobindo or the Mother for the matched quality.
* **Slow-Rate Voice Synthesis (TTS):**
  * Invokes browser `window.speechSynthesis` with fixed parameters:
    * Meditative rate: `0.70` (slow)
    * Meditative pitch: `0.95` (calm)
  * Includes a toggle for a soft French-accented voice (`fr-FR`) to emulate the reading voice of the Mother.
* **SABDA Links & Glossary:**
  * Displays links to download the source books from the Ashram archives.
  * Sanskrit terms (e.g. *Sadhana*, *Ananda*, *Tapas*) are wrapped in underline tags. Clicking them opens a glossary sheet defining the yogic concept.
* **Secular Toggle:**
  * A settings toggle translates title headers into secular terms (e.g., "Sanskrit Seed Words" $\rightarrow$ "Mindful Sounds", "Spiritual Quality" $\rightarrow$ "Inner Strength") for secular users, while keeping quote bodies original.

### 1.3 Daily Aspiration & Consecration Jar
* **Morning Draw:** The user clicks a velvet bag to draw a random tile.
  * Displays a daily quality, description, and morning prompt.
  * Provides a system shortcut to pin the quality as a launcher widget.
* **Consecration Journal:**
  * An input text field labeled "What vital storm, worry, or friction would you like to consecrate today?".
  * Submitting triggers a HTML5 Canvas particle explosion: the written characters dissolve into floating gold sparks that fall into a brass jar container.
  * **Consciousness Points:** Saves the entry and awards $+10$ points to the profile progress.
  * Earning points (+5 per level, +10 per journal) adds petals to a vector SVG outline on the profile page, eventually triggering a full gold-burst bloom animation.
* **Darshan Day Greetings:** The app checks the device date on boot. If it is a sacred Ashram Darshan Day (Feb-21, Apr-24, Aug-15, Nov-24, Dec-05), the app overlays a dedicated, gold-bordered greetings card with an offline quote and plays a warm organ transition.

### 1.4 Constellation Calendar
* **Star Grid Map:**
  * Renders monthly days as stars. Dim dots represent empty days, while pulsing glowing stars represent logged reflections.
  * Clicking a pulsing star loads that day's logged consecrations and unlocked tiles.
  * **Vector Path Constellations:** At month's end, the app draws svg lines connecting the stars to outline sacred geometries (Mother's Symbol, Lotus shape).
  * **Ashram Events Halos & Occasions List:** Stars matching milestone dates in the local events database render with a pulsing golden ring outline (`.event-halo`). Tapping these nodes triggers a bottom-sheet modal detailing the milestone history. A list renders below the star grid showing all occasions for the selected month.

---

## 2. Non-Functional Requirements

### 2.1 Performance & Aesthetics
* **Soothing Palettes:** Sober dark-mode backing. Screen brightness shifts dynamically based on local clock (Dawn = rose/gold gradient, Twilight = copper/saffron, Night = deep teal/navy).
* **Frame Rate:** Canvas and SVG particle animations must run at **60fps** to avoid vital irritation.
* **Load Time:** App must boot and render the main board in under **1 second** from cold launch.

### 2.2 Offline Resilience & Storage
* **Zero Tracking:** The app runs 100% offline, making no network calls to external analytical trackers or clouds. No user diaries leave the device.
* **Version Mismatch Sync:** When online at startup, a non-blocking check calls `version.json`. If a new version exists, the app fetches `teachings_repository.json` and merges new tiles into the local cache. If the fetch fails, it times out in 2 seconds and defaults to offline assets.
* **Data Protection & Key Enclaves:**
  * Personal stores (`reflections`, `user_profile`) are encrypted locally using AES-256-GCM.
  * The master key is generated on first launch and written directly to the device Secure Key store (**Keychain Services** on iOS, **Android Keystore** TEE provider on Android) via Capacitor, preventing extraction by root users.
* **Manual Portability:** Settings screen allows downloading a password-protected JSON backup file containing progress logs, encrypted locally using PBKDF2 with 10,000 iterations and AES-256-CBC.
* **Absolute Purge & Reset Protocol:** Triggered from Settings under "Reset Sanctuary & Purge All Data". The action is enabled only after typing `"PURGE"` in a confirmation input, dropping SQLite databases, deleting the master keys from the Keystore/Keychain, and reloading the app.
* **Centered Frame:** On desktop screens, the workspace is confined to a vertical box (`360px` to `412px`) centered horizontally, against a drifting twilight starfield background to maintain an intimate mobile experience.
