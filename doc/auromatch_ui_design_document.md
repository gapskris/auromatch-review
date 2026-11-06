# AuroMatch: The Triple Garden of Significances — Wireframes Document

---

## 1. Primary Screen Wireframes (ASCII Layouts)

### 1.1 Screen A: Stacking Match Board (Remembrance Sanctuary)
```text
==================================================
|  [AUROMATCH: CONCENTRATION SANCTUARY]          |
|                                                |
|  [  Tray:  [💮] [💮] [🪷] [ ] [ ] [ ] [ ] ]   |
|  +------------------------------------------+  |
|  |                  [🪷]*                   |  |
|  |             [💮]      [🌹]               |  |
|  |                  [🌺]                    |  |
|  |             [🌻]      [🌼]*              |  |
|  |                  [🪻]                    |  |
|  +------------------------------------------+  |
|  *Note: Darkened tiles (e.g. [🌼]*) are blocked |
|                                                |
|  [ Reshuffle Board ]              [ Tiles: 24 ]|
==================================================
```

### 1.2 Screen B: Wisdom Card (Match Reflection Overlay)
```text
==================================================
|  [AUROMATCH: CONCENTRATION SANCTUARY]          |
|                                                |
|  +------------------------------------------+  |
|  |  (🪷) LOTUS                               |  |
|  |  Botanical: Nelumbo nucifera             |  |
|  |  Quality: DIVINE PRESENCE                |  |
|  |                                          |  |
|  |  "To feel the Divine presence constantly  |  |
|  |   in all things and all movements."      |  |
|  |                               — The Mother |  |
|  +------------------------------------------+  |
|                                                |
|     [ Listen ]    [ Pause ]    [ Stop ]        |
|                                                |
|                 [ Continue ]                   |
==================================================
```

### 1.3 Screen C: Consecration Jar (Release Journal)
```text
==================================================
|  [THE CONSECRATION JAR]                        |
|                                                |
|                     .---.                      |
|                    /     \                     |
|                   |  (*)  | <--- Brass Jar     |
|                    \_____/                     |
|                                                |
|  "What vital storm, worry or friction would    |
|   you like to consecrate today?"               |
|                                                |
|  Self-Observation Journal Notes:               |
|  +------------------------------------------+  |
|  | Feeling anxious about the meeting..      |  |
|  +------------------------------------------+  |
|                                                |
|               [ Consecrate Worry ]             |
==================================================
```

### 1.4 Screen D: Constellation Grid (Star Calendar)
```text
==================================================
|  [CONSTELLATION OF LIGHT]                      |
|                                                |
|       *--------.--------*--------.--------*    |
|    (Day 1)  (Day 2)  (Day 3)  (Day 4)  (Day 5) |
|       |                                        |
|       .        *--------.--------*        .    |
|    (Day 6)  (Day 7)  (Day 8)  (Day 9)  (Day 10)|
|                                                |
|  [ Completed month connects stars to draw ]    |
|  [ a sacred symbol (e.g. Lotus / Mother's) ]   |
|                                                |
|                 [ Back Home ]                  |
==================================================
```

### 1.5 Screen E: Onboarding Path Selection Overlay
```text
==================================================
|  [WELCOME TO AUROMATCH SANCTUARY]              |
|                                                |
|  Please select your path to begin the practice:|
|                                                |
|  +------------------------------------------+  |
|  | [ TRADITIONAL PATH ]                     |  |
|  | Sadhana-focused terminology and quotes.  |  |
|  +------------------------------------------+  |
|  +------------------------------------------+  |
|  | [ SECULAR PATH ]                         |  |
|  | Universal psychological & mindful tags.  |  |
|  +------------------------------------------+  |
|  +------------------------------------------+  |
|  | [ YOUTH PATH ]                           |  |
|  | Simple word lists, stars, & blooming.    |  |
|  +------------------------------------------+  |
|                                                |
==================================================
```

---

## 2. Mockup & Reference Details

* **Design Elements:** Soft pastel colors, watercolor aesthetics, gold-rimmed tiles, and glassmorphic card overlays to ensure a premium, soothing experience.
* **Mockup Image Path:** [auromatch_ui_mockup.png](file:///c:/DataScience/AuroProject_Annalysis/AuroMatch/doc/auromatch_ui_mockup.png)
* **Design Specs File:** [auromatch_ui_design_document.md](file:///c:/DataScience/AuroProject_Annalysis/AuroMatch/doc/auromatch_ui_design_document.md)

---

## 3. Screen Dimensions & Bounding Coordinates

* **App Bounding Box:** Centered PC web client is set to portrait layout width `360px` to `412px` and height `640px` to `820px`.
* **3D coordinate range:** Board coordinate system maps tiles inside a `320px x 420px` region. Tile sizes are standard `50px` width by `66px` height. Bounding box coordinates calculate occlusion and selection triggers based on coordinates.
* **7-Slot Tray dimensions:** Located at the top of the board, bounded at `340px x 74px`. Tray slots are `44px x 60px` with `6px` spacing.
