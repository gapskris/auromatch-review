# AuroMatch: The Triple Garden of Significances — Product Requirement Document (PRD)

---

## 1. Product Overview

**AuroMatch – The Triple Garden of Significances** is a cozy, mindful, 3-tile matching concentration sanctuary designed to bring visual beauty, contemplative focus, and quiet reflection to daily digital habits. The application combines Mahjong Solitaire-style 3D stacking mechanics with the spiritual teachings of Sri Aurobindo and the Mother. By matching tiles representing spiritual qualities, sacred flowers, Sanskrit seed words (*bijas*), and devotional instruments across **15 location-inspired Garden Sanctuaries**, players unlock wisdom reflection cards, listen to slow-narrated scriptural passages, practice morning aspirations via an oracle velvet bag, and consecrate daily frictions in a private reflection journal.

The application is implemented under a **Dual Delivery Architecture**:
1. **Option 1 Modular Production App:** A clean, decoupled Vanilla ES6 Modules structure (`index.html`, `styles/main.css`, `src/main.js`, `src/audio/`, `src/controllers/`, `src/ui/`) adhering to modern maintainable software engineering practices.
2. **Standalone Single-File Web Prototype:** A unified, zero-dependency HTML document ([AuroMatch_Web_Prototype.html](file:///c:/DataScience/AuroProject_Annalysis/AuroMatch/AuroMatch_Web_Prototype.html)) with inline SVG vectors, Web Audio synthesis, and responsive full-bleed PWA styles for immediate offline mobile and desktop demonstration.

---

## 2. Target Audience & Personas

* **Integral Yoga Sadhaks & Devotees:** Seekers looking for practical ways to keep the teachings of Sri Aurobindo and the Mother active in their daily consciousness (*smaran*) during screen time.
* **Students of SAICE & Children:** Young learners cultivating one-pointed concentration, aesthetic refinement, flower significances, and Sanskrit roots.
* **Mindful Seekers & General Practitioners:** Users seeking stress relief, digital minimalism, and offline-first concentration exercises free from gamified anxiety or manipulative dopamine loops.

---

## 3. User Stories

### Gameplay & Contemplative Matching
> **As a player,**
> I want to match 3D watercolor tiles representing sacred flowers, virtues, and Sanskrit seeds in calm, unhurried garden environments,
> **so that** I can gather my scattered attention, quiet my mind, and internalize their spiritual significances.

### Meditative Reading & Audio Immersion
> **As a sadhak,**
> I want to view scripture quotes on an elegant glassmorphic card and listen to them read slowly with an ambient Raga Tanpura drone and acoustic meditation gong,
> **so that** the spiritual vibration sinks deeply into my mental and vital nature.

### Consecration & Surrender Journaling
> **As a self-reflective seeker,**
> I want to type my vital worries, impatience, or inner friction into the Consecration Jar and watch the text dissolve into golden light particles,
> **so that** I can practice active surrender to the Divine Grace and maintain an encrypted, private journal of my progress.

### Morning Aspiration Alignment
> **As a daily practitioner,**
> I want to draw a morning attitude card from a virtual velvet bag,
> **so that** I can anchor my consciousness in a specific spiritual quality (e.g. Sincerity, Humility, Peace) throughout the day.

### Data Privacy & Portability
> **As a privacy-conscious user,**
> I want my journal entries and progress stored strictly on my device and exportable via a password-encrypted backup file,
> **so that** my intimate reflections remain completely private and portable between mobile and desktop devices.

---

## 4. Key Functional Features

### 4.1 3D Stacking Tile-Matching Engine
* **Layered Coordinate System:** Tiles are placed on spatial coordinates `(x, y, layer)`.
* **Occlusion & Bounding-Box Detection:** A tile at layer $L_i$ is covered and blocked if any active tile at $L_j > L_i$ overlaps within $W_{\text{threshold}} = 42\text{px}$ and $H_{\text{threshold}} = 56\text{px}$ ($84\%$ of width $50\text{px}$ and $85\%$ of height $66\text{px}$).
* **Visual States:**
  * *Unblocked Tiles:* Radiant cream texture, active hover elevation, and an animated golden glowing aura.
  * *Blocked Tiles:* Desaturated and dimmed (`filter: grayscale(100%) brightness(0.65) contrast(0.95)`), cursor locked. Tapping a blocked tile triggers a low $196\text{ Hz}$ warning chime.
* **7-Slot Sorting Tray:** Tapping an unblocked tile slides it into a 7-slot tray. The tray automatically clusters identical tiles using alphabetical sort (`localeCompare` on tile ID).
* **Triple Match & Wisdom Revelation:** When 3 identical tiles cluster in the tray, they are removed with a $440\text{ Hz}$ harmonic chime, immediately opening the **Match Reflection Overlay**.
* **Reshuffle Guarantee:** If the tray fills to 7 slots without a triple match, the engine triggers a $196\text{ Hz}$ notification and automatically reshuffles all remaining board tiles, ensuring zero deadlocks.

### 4.2 15 Garden Sanctuaries Across 3 Visual Concepts
The game features 15 physical sanctuaries across Pondicherry and Auroville, categorized into 3 visual rendering concepts:

| Sanctuary Garden | Visual Concept | Tile Set | Dedicated Background Gradient | Difficulty Tier |
| :--- | :--- | :--- | :--- | :--- |
| **1. Samadhi Courtyard** | Concept 2: Circular Mandala | Watercolor Flowers | Soft cream, pale rose & gold | Easy (24 tiles) |
| **2. Ashram Playground** | Concept 2: Circular Mandala | 12 Qualities | Vital orange, gold & white | Medium (36 tiles) |
| **3. Matrimandir Chamber** | Concept 1: Golden Glass Stack | Sanskrit Seeds | Golden ray & white light shafts | Hard (48 tiles) |
| **4. Lake Estate** | Concept 3: Wood & Brass Altar | Indian Instruments | Soft lake reflection teal & bronze | Medium (36 tiles) |
| **5. Service Tree** | Concept 2: Circular Mandala | Watercolor Flowers | Deep leaf green & golden highlights | Easy (24 tiles) |
| **6. Banyan Tree** | Concept 2: Circular Mandala | 12 Qualities | Woodland sage & golden earth | Medium (36 tiles) |
| **7. Promenade Coastline** | Concept 1: Golden Glass Stack | Sanskrit Seeds | Sea-twilight indigo & orange | Hard (48 tiles) |
| **8. SABDA / Library** | Concept 3: Wood & Brass Altar | Watercolor Flowers | Dark mahogany & parchment gold | Medium (36 tiles) |
| **9. Golconde Dormitory** | Concept 3: Wood & Brass Altar | 12 Qualities | Modernist slate gray & bronze | Easy (24 tiles) |
| **10. Ashram Archives** | Concept 3: Wood & Brass Altar | Sanskrit Seeds | Antique papyrus brown & bronze | Hard (48 tiles) |
| **11. Matrimandir Petals** | Concept 1: Golden Glass Stack | Watercolor Flowers | Radiant petal yellow & white | Easy (24 tiles) |
| **12. Auroville Green Belt** | Concept 2: Circular Mandala | 12 Qualities | Forest green & wilderness sage | Medium (36 tiles) |
| **13. Classroom (SAICE)** | Concept 3: Wood & Brass Altar | Watercolor Flowers | Chalk blue & school desk wood | Medium (36 tiles) |
| **14. Botanical Garden** | Concept 2: Circular Mandala | Watercolor Flowers | Tropical jade green & orchid pink | Easy (24 tiles) |
| **15. Dining Hall** | Concept 3: Wood & Brass Altar | 12 Qualities | Copper pot orange & warm wood | Hard (48 tiles) |

### 4.3 Web Audio Generative Soundscape Engine
* **Ashram Meditation Gong:** Dual-fundamental synthesizer using 5 additive sine wave oscillators:
  * Morning / Sunrise ($05:00 - 17:00$): Fundamental $f_0 = 172.08\text{ Hz}$.
  * Evening / Night ($17:00 - 05:00$): Fundamental $f_0 = 110.0\text{ Hz}$.
  * Harmonic Overtones: Factors $[1.0, 1.50, 2.01, 2.65, 3.12]$ with gains $[1.0, 0.50, 0.30, 0.15, 0.08]$.
  * Envelope: Instant attack ($15\text{ms}$) with an exponential decay constant of $5.0\text{s}$.
* **4-Prahar Hindustani Raga Tanpura Drone:** Generates real-time sine wave root, fifth, and octave chord voicings filtered through a low-pass biquad filter ($600\text{ Hz}, Q=1$):
  * *Dawn (04:00 - 08:00):* Raga Bhairav (Root $130.81\text{ Hz}$).
  * *Noon (08:00 - 16:00):* Raga Sarang (Root $130.81\text{ Hz}$).
  * *Evening (16:00 - 20:00):* Raga Yaman (Root $130.81\text{ Hz}$).
  * *Night (20:00 - 04:00):* Raga Darbari (Root $130.81\text{ Hz}$).
* **Dynamic Instrument Layering:** In instrument-themed sanctuaries (e.g. Lake Estate), matching instrument tiles dynamically adds continuous triangle oscillator melodic loops (gain $0.04$) without displacing the Tanpura drone.

### 4.4 Scripture Card & Text-to-Speech Narration
* **Contemplative Pause:** Completing a triple opens a full-screen glassmorphic card displaying the matched flower/virtue, its spiritual significance, and scripture excerpts from Sri Aurobindo and the Mother.
* **Slow Cadence Web Speech (TTS):** Players tap "Listen" to trigger slow, meditative narration (`rate = 0.70`, `pitch = 0.95`).
* **Decoupled Voice & Path Settings:**
  * `voiceTonePreference`: Allows toggling between Indian English (`en-IN` / `en`) and a French-cadence devotee voice (`fr-FR`) modeled after the Mother's reading cadence.
  * `sanctuaryMode`: Supports three distinct onboarding paths:
    1. *Traditional (Sadhana):* Standard yogic vocabulary and Sanskrit seed terms.
    2. *Secular (Mindfulness):* Replaces theological headers with psychological terms (e.g. *Divine Presence* $\rightarrow$ *Internal Awareness*, *Devotion* $\rightarrow$ *Commitment*) while leaving quote bodies verbatim.
    3. *Youth (Starlight):* Simplified level layouts and playful stardust visual tokens.
* **SABDA Links & Glossary:** Direct links to complete works on the Ashram SABDA portal; dotted underlines on words like *Sadhana* and *Consecration* open interactive bottom-sheet definitions.

### 4.5 The Consecration Jar (Surrender Journal)
* **Evening Reflection Canvas:** An incense burner SVG container paired with a self-observation text area.
* **Text-to-Particle Dissolution Physics:** Text is rendered to an offscreen canvas to extract stroke coordinates at $4\times 4\text{px}$ density.
* **Physics Equations:**
  * Gravity: $g = 0.15\text{ px/frame}^2$.
  * Initial upward burst: $v_y = -0.5\text{ to } -2.0\text{ px/frame}$.
  * Horizontal attraction toward jar center: $a_x = (x_{\text{jar}} - x_t) \times 0.005$.
  * Opacity decay: $\alpha_t = \alpha_{t-1} \times (0.95 + \text{random}(0, 0.03))$, particle culled at $\alpha \le 0.01$.
* **Persistence:** Reflections are saved into the encrypted local store and award $+2$ Lotus Petals.

### 4.6 Constellation Star Grid (Star Calendar)
* **Mother's Symbol Geometric Mapping:** A monthly calendar mapping days as nodes forming the sacred geometry of the Mother's 12-petaled symbol (1 central hub, 4 inner petals, 12 outer petals).
* **Pulsing Active Stars:** Days with logged reflections light up as pulsing golden stars.
* **Ashram Milestone Halos:** Historical anniversaries feature glowing yellow `.event-halo` rings:
  * `02-21`: The Mother's Birthday (1878).
  * `04-24`: The Mother's Final Arrival in Pondicherry (1920).
  * `08-15`: Sri Aurobindo's Birthday (1872).
  * `11-24`: Siddhi Day / Victory Day (1926).
  * `12-05`: Sri Aurobindo's Mahasamadhi (1950).

### 4.7 Daily Aspiration (Morning Oracle)
* **Velvet Bag Draw:** A tactile, shaking velvet bag SVG that reveals a daily virtue and sadhanic focus prompt.
* **Daily Lock State:** Locks after one draw per calendar day, anchoring the user's consciousness without compulsive redraws.

### 4.8 Data Security, Backup & Purge Protocol
* **LocalStorage Partitioning:** State is strictly decoupled into dedicated stores:
  * `auro_match_user`: Profile metrics, petals, volume, and path preferences.
  * `auro_match_consecrations`: Private journal reflections array.
  * `auro_match_unlocked_tiles`: History of completed/unlocked tile sets.
  * `auro_match_teachings`: Cached offline thematic database.
  * `auro_match_events`: Offline Darshan milestone database.
* **PBKDF2 + AES-256-GCM Encryption:** Users can export a password-protected JSON backup (`auro_match_backup.json`). Key is derived using PBKDF2 (10,000 iterations, SHA-256, 16-byte random salt) and encrypted using AES-256-GCM with a 12-byte random IV.
* **Verbatim "PURGE" Protocol:** To wipe all personal data, the user must type `"PURGE"` verbatim into a confirmation modal. The action clears all stores and resets the application.

---

## 5. Non-Functional Requirements & Responsive Viewports

* **Mobile PWA Full-Bleed Design:** On screen viewports $\le 480\text{px}$, the application expands edge-to-edge (`100dvh`, zero outer padding, borderless container).
* **Board Scale Transforms:** The 3D tile board automatically scales down using CSS transforms (`transform: scale(min(1, (100vw - 20px) / 380))`) to ensure flawless display on narrow phones (from $360\text{px}$ to $430\text{px}$).
* **PWA Standalone Meta Tags:** Configured with `apple-mobile-web-app-capable`, `apple-mobile-web-app-status-bar-style`, and `theme-color` for fullscreen home-screen launch without browser URL bars.
* **Mobile Audio Unlock:** Features automatic `audioCtx.resume()` bindings on initial user touch to comply with mobile Web Audio policies.
* **Zero External HTTP Asset Dependencies:** Complete independence from remote image/audio CDNs. All visuals are inline SVG and Unicode; all audio is synthesized via Web Audio oscillators.
* **Load Time:** Complete application state initializes in $<500\text{ms}$.
