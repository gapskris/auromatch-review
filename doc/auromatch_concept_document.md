# AuroMatch: Mindful General Knowledge & Concentration Sanctuary — Master Concept Note

AuroMatch is a cozy, mindful, 2.5D Mahjong concentration game designed for student learning, intellectual curiosity, and cognitive engagement. It combines the tactile pattern-matching mechanics of classic Mahjong with a massive 3,840-item multi-disciplinary General Knowledge (GK) educational curriculum across 520 progressive levels.

> **[IMPORTANT] Strategic Architecture Note (V1 vs. V2 Scope):**  
> * **Version 1 (Current Live Engine):** Focuses exclusively on **General Knowledge, Student Learning, and Cognitive Skill Development** (Fauna & Wildlife, Botany & Ecology, Astronomy & Cosmos, Earth Sciences, Physical & Life Sciences, World Arts, and Character Building).  
> * **Version 2 (Planned Future Expansion):** All earlier implemented features related specifically to Sri Aurobindo Ashram, the Mother's Spiritual Significances of Flowers, and Darshan rituals are **safely preserved and hidden in the codebase** for dedicated future V2 release.

---

## 1. Core Philosophy & Educational Guardrails

Most commercial matching games are designed to trigger high-stress excitement (ticking countdown timers, flashing screen explosions, ranking scoreboards, and aggressive push notifications). AuroMatch reverses these patterns to create a calm, focused digital learning sanctuary:
* **Anti-Addiction (No Timers or Pressure):** There are no countdown timers, lives, or penalty countdowns. Students play at their own natural learning rhythm.
* **100% Free Senior & Student Undo:** Players can undo moves freely without penalty, encouraging experimentation and spatial problem-solving.
* **Dual-Mode Gameplay:** Default Mode A (Vita Mahjong Match-2 pair dissolution directly on board) for calm play; optional Mode B (Tile Club 7-slot tray triad matching) for advanced pattern sorting.
* **Pictorial Educational Recognition:** Every tile features a large, colorful illustration and a clear subject name, fostering instant visual recognition across science, nature, and world knowledge.
* **Guaranteed Solvability (Deadlock-Free):** Reverse-construction mathematical generation ensures that every single level from 1 to 520 is 100% solvable without unwinnable dead-ends.
* **Local-First Privacy:** Zero cloud trackers, zero student profiling, zero telemetry. All player profiles and progress remain entirely on the local device.

---

## 2. Conceptual Curriculum Blueprint (V1 Live Engine)

### Part 1: The 3,840-Item General Knowledge Curriculum
Instead of repetitive generic symbols, students encounter an expansive encyclopedia spanning 5 core knowledge domains:

#### Domain 1: Nature & Biodiversity (Wildlife & Marine Biology)
* **The Tiles:** Mammals, birds, aquatic life, insects, and flora (🐿️ Squirrel, 🦫 Beaver, 🐬 Dolphin, 🦅 Eagle, 🦁 Lion, 🦉 Owl, 🦚 Peacock, 🦋 Monarch, 🌺 Lotus, 🌿 Bamboo).
* **Educational Lore:** Taxonomic classification, habitat, ecological roles, and biodiversity preservation.

#### Domain 2: Cosmos, Astronomy & Earth Sciences
* **The Tiles:** Planetary bodies, celestial phenomena, geological formations (🪐 Saturn, 🚀 Rocket, 🔭 Telescope, 🌋 Volcano, 🏔️ Mountain, 🌊 Ocean Wave, ⚡ Energy, 🧭 Compass).
* **Educational Lore:** Planetary orbits, stellar lifecycles, tectonic plates, and atmospheric dynamics.

#### Domain 3: Mind, Physics & Life Sciences
* **The Tiles:** Atomic structures, genetic code, mathematical wonders (⚛️ Atom, 🧬 DNA Double Helix, 🔬 Microscope, 🧪 Chemistry, 📐 Geometry).
* **Educational Lore:** Fundamental laws of physics, cellular biology, scientific discoveries, and logic.

#### Domain 4: World Arts, Heritage & Cultural Wonders
* **The Tiles:** Classical instruments, architectural monuments, artistic expressions (🎨 Palette, 🎻 Violin, 🏛️ Temple, 🌈 Rainbow, 🌅 Sunrise, 🗿 Heritage).
* **Educational Lore:** Historical architecture, world music traditions, fine arts, and cultural heritage.

#### Domain 5: Character, Mind & Philosophical Thought
* **The Tiles:** Inner focus, mindfulness, determination, ethical discernment (💡 Insight, 🔥 Will, 📖 Study, 🕊️ Peace, ⚖️ Justice).
* **Educational Lore:** Cognitive habits, emotional balance, perseverance, and intellectual clarity.

---

---

### Part 2: Core App Ecosystem (V1 Live Architecture & V2 Reserved Modules)

#### 🎮 The 520-Level Progressive Learning Engine (V1 Live Core)
* **Zero-Gate Direct Progression:** When a student opens the app, they immediately jump into their saved level via **"Continue Level X ➔"** without navigational friction.
* **S-Curve Cognitive Complexity:** Tile count and vertical depth scale smoothly from Level 1 (24 tiles, 2 layers) up to Level 520 (108 tiles, 6 layers).
* **Vak Progression Ladder & 7 Ranks:** Students earn Sparks and advance through 7 secular intellectual ranks:
  $$\text{Aspirant (1–25)} \to \text{Learner (26–60)} \to \text{Thinker (61–110)} \to \text{Discerner (111–175)} \to \text{Sage (176–240)} \to \text{Explorer (241–300)} \to \text{Luminous (301–520)}$$
* **Sanctuary Milestones:** Every 10th level (10, 20, 30...) awards a +30 Sparks celebration bonus.
* **Tactile Mahjong Controls:** Ergonomic circular action buttons: Shuffle (S), 100% Free Senior Undo (U), Hint (H), and Reset (R).
* **Multi-Player Profile Isolation:** Multiple students can share a single classroom device or household tablet with independent progress, levels, and sparks saved per name.

#### 🏛️ Reserved V2 Ashram & Sacred Sanctuary Modules (Archived for Future Phase)
The following modules were successfully developed during initial prototyping and are **safely preserved in code for future V2 activation**:
* **15 Thematic Ashram & Auroville Gardens:** Dedicated garden level selector featuring Ashram Samadhi Courtyard, Matrimandir Chamber, Ashram Playground, Golconde, and Lake Estate.
* **Sacred Mother's Flower Significances:** In-depth floral and virtue cards derived from *Flowers and Their Messages*.
* **The Daily Morning Oracle & Consecration Jar:** Morning aspiration lottery and evening text-dissolution reflection journal.
* **Darshan Milestone Greetings:** Annual calendar recognitions for Feb 21, Apr 24, Aug 15, and Nov 24.

---

## 3. Product Vision & Stakeholder Framing

When demonstrating AuroMatch:

> *"AuroMatch takes the universally loved, highly calming Mahjong matching genre and transforms it into an empowering, mindful General Knowledge learning game for students and lifelong learners. Across 520 solvable levels, students explore 3,840 illustrated encyclopedia concepts spanning wildlife, astronomy, earth sciences, physics, and world culture. There are zero timers, zero paywalls, zero ads, and 100% private offline progress. The Ashram-specific spiritual garden sanctuaries and Mother's flower significances have been preserved and safely archived for a dedicated V2 sacred expansion in the future."*

---

## 4. Technical Architecture Specifications
* **3D Coordinate Stacking & Bounding Math:** Layered coordinates with mathematical occlusion detection ($W_{\text{threshold}} = 42\text{px}, H_{\text{threshold}} = 56\text{px}$). Multi-layer depth dispersion ensures partner tiles are separated across vertical tiers and perimeter wings.
* **Dual-Mode Engine:** Default Mode A (Vita Pairs direct dissolution); optional Mode B (Tile Club 7-slot tray).
* **Offline-First Multi-Profile Storage:** LocalStorage partitioning (`auromatch_player_state`, `auromatch_player_profiles`). PBKDF2 + AES-GCM encrypted backup exports/imports. Verbatim `"PURGE"` factory reset.
* **Universal Ergonomics & Senior View:** Fluid 3-column desktop layout, touch/pointer parity, keyboard shortcuts, and `[Aa] Senior View` (+25% tile scaling).
