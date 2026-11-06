# AuroMatch: The Triple Garden of Significances — User Stories Document

---

## 1. Target Personas

### Persona A: Anuradha (The Ashram Devotee)
* **Background:** A regular practitioner of Integral Yoga living in Pondicherry.
* **Goal:** Wants a gentle daily ritual to contemplate flower significances and remember the Mother's teachings without being distracted by addictive, high-arousal gamification loops.
* **Pain Point:** Finds standard matching games stressful, saturated, and filled with ads, which disturb her inner quietude.

### Persona B: Vikram (The Meditative Professional)
* **Background:** A busy designer who uses his phone to decompress but wants to reduce mindless screen time and vital restlessness.
* **Goal:** Wants to replace his nervous gaming habits with a mindful matching sanctuary, using a private journal to release work anxieties.
* **Pain Point:** Regular journals feel like a chore; game-based journals feel shallow.

### Persona C: Devika (The Devoted Parent)
* **Background:** A mother raising her child in a spiritual atmosphere.
* **Goal:** Wants to teach her child the 12 qualities of the Mother's Symbol, the names of local flowers, and simple Sanskrit seed terms in an engaging, beautiful, and non-commercial format.
* **Pain Point:** Most educational games are commercialized and overstimulating for children.

---

## 2. Feature-Specific User Stories & Acceptance Criteria

### 2.1 Overlapping 3D Tile Matching
* **Story:** As Anuradha, I want to tap on unblocked watercolor tiles to move them to a tray and match them in sets of three, so that I can practice patient concentration and visually contemplate the symbols.
* **Acceptance Criteria:**
  * Must support smooth tapping on desktop and touchscreens.
  * Overlapping layers must be calculated mathematically; covered tiles must be visually dimmed and unselectable.
  * Selecting an unblocked tile must slide it into the tray and sort it immediately, clustering identical tiles.
  * Matching a triple removes it from the tray and opens the Match Reflection card.

### 2.2 Unlocking Teachings & French-Accented Narrator
* **Story:** As Devika, I want to read the flower's significance and listen to the Mother's teachings read with a soft French-accented voice, so that my child can learn the exact quotes and hear them read in the Mother's reading tone.
* **Acceptance Criteria:**
  * Displays the common name, botanical name, and significance quote on a glassmorphic card.
  * The "Listen" button triggers the Web Speech engine with slow speed parameters (rate `0.70`).
  * The voice settings allow selecting a soft French-accented speaker to mimic the Mother's cadence.

### 2.3 The Consecration Jar (Private Journal)
* **Story:** As Vikram, I want to write down my work anxiety in a private journal and watch the text dissolve into a jar, so that I can practice the movement of surrender (*pranam*) and let go of vital friction.
* **Acceptance Criteria:**
  * A text entry box must accept qualitative reflections.
  * Clicking "Consecrate" must trigger a canvas particle animation where letters break apart and slide into a brass jar.
  * Entries must be stored locally in an encrypted format, inaccessible from external files or other applications.

### 2.4 Daily Aspiration Oracle & Launcher Widget
* **Story:** As Anuradha, I want to draw a morning attitude card and pin it to my phone launcher screen, so that I can keep that quality in mind throughout my busy day.
* **Acceptance Criteria:**
  * Pulling a card from the bag displays a quality medallion.
  * Offers a widget shortcut to pin the medallion image directly to the device home screen.
  * Only one card can be drawn per day, resetting at midnight local time.

### 2.5 Onboarding Path Selection & Terminology Toggles
* **Story:** As Devika, I want to choose the "Youth" mode for my child upon first launch, so that the vocabulary remains simple and they get visual progress indicators (such as the blooming lotus).
* **Acceptance Criteria:**
  * Displays a Path Selection modal on first boot containing three choices: Traditional (Sadhana), Secular (Mindfulness), and Youth (Starlight).
  * Selecting "Secular" translates spiritual titles (e.g., "Sanskrit Seed Words" to "Mindful Sounds") while keeping quotes verbatim.
  * Selecting "Youth" bounds levels to the easy tier (conversational quotes) and activates the vector SVG lotus profile panel.
