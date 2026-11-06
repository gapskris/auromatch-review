# AuroMatch: Master Theme & 24-Tile Progressive Architecture Plan

> **Document Status:** Approved Master Plan for Execution  
> **Synthesizes:**  
> 1. *Folk Botanical Theme & 24-Tile Progressive Architecture Plan*  
> 2. *Targeted UI & Standard Categories Theme Architecture Plan*  
> **Core Decisions:**  
> - 🔒 **Realms Mode:** 100% Preserved. The 20 Secular Realms, custom realm tiles, and background wallpapers remain completely untouched.  
> - ✨ **Global Game UI:** Upgraded to an elevated 3D luxury frame with a 1-tap live theme switcher.  
> - 🌸 **Standard Categories ("Pairs", "Tile Club", "Classic"):** Upgraded from flat cream/wood cards on green felt to the **24-Tile 3D Dual-Theme System** (**☀️ Imperial Gold** vs **🌙 Royal Lapis**).

---

## 1. Architectural Boundaries: What Stays vs. What Changes

```
                           AUROMATCH THEME SCOPE
                                     │
           ┌─────────────────────────┴─────────────────────────┐
           ▼                                                   ▼
   🔒 REALMS MODE (CAMPAIGN)                 ✨ PAIRS • TILE CLUB • CLASSIC
   • 20 Unique Realm Tiles (UNTOUCHED)        • New 3D Elevated Tiles (24 Motifs)
   • 20 Custom Realm Wallpapers (UNTOUCHED)   • New Atmospheric Backgrounds
   • Specific Realm Story Lore (UNTOUCHED)    • Live Dual-Theme Toggle (Gold/Lapis)
           │                                                   │
           └─────────────────────────┬─────────────────────────┘
                                     ▼
                        GLOBAL GAME UI SHELL (UPGRADED)
     • Header HUD: Level Badge, Currency Chips, Settings Gear
     • Mode Selector: [ Pairs ] [ Tile Club ] [ Classic ] [ Realms ]
     • Match-3 Tray: 7 Slots, Counter, Guidance Bar
     • Bottom Action Bar: Shuffle, Undo, Hint, Reset, Lore
     • Modals & Dialogs: Victory Fanfare, Pause, Settings
```

---

## 2. Dynamic Progression & Level Mathematics

In `AuroMatch`, the number of distinct flora/tile kinds required on the board scales dynamically with board size:

$$\text{Distinct Tile Kinds} = \max\left(3, \left\lfloor \frac{\text{Total Board Tiles}}{K} \right\rfloor\right)$$

Where $K = 3$ for Match-3 (Tile Club) and $K = 2$ for Mahjong Solitaire (Pairs / Classic).

```
                      LEVEL PROGRESSION & TILE POOL
                      
  Lv 1-8 (12-24 Tiles)       Lv 9-20 (36-48 Tiles)       Lv 21-50+ (60-108 Tiles)
 ┌─────────────────────┐   ┌────────────────────────┐   ┌────────────────────────┐
 │   4 to 8 Motifs     │ ─►│     16 Motifs (Core)   │ ─►│   24 Motifs (Master)   │
 │ (Daisies & Tulips)  │   │ (+ Palmettes, Leaves)  │   │ (+ Fins, Plumes, Rays) │
 └─────────────────────┘   └────────────────────────┘   └────────────────────────┘
```

* **Early Levels (1–8):** Simple 12–24 tile formations utilizing 4–8 introductory floral archetypes.
* **Mid Levels (9–20):** Standard 36–48 tile boards utilizing the complete **Tier 1 (Core 16 tiles)**.
* **Advanced & Master Levels (21–50+):** Monumental 60–108 tile multi-layer stacks introducing **Tier 2 (8 Master expansion tiles)**, bringing the active pool to **24 distinct motifs** and eliminating repetitive boards.

---

## 3. The 24-Tile Master Roster

Deconstructed from the 27 cataloged elements across the 3 folk art reference images:

| Tile ID | Motif Name | Source Image | Archetype / Silhouette | Dominant Colors | Level Tier Unlock |
|---|---|---|---|---|---|
| `tile_01` | **Top Rosette Daisy** | Pic 1 (`#1`) | 8-Petal Radial Rosette | Magenta (`#EB0F73`), Amber, Cyan | Lv 1 (Core) |
| `tile_02` | **Grand Lotus Palmette** | Pic 1 (`#2`) | Scalloped Peacock Fan | Gold, Fuchsia, Deep Teal | Lv 1 (Core) |
| `tile_03` | **Folk Tulip** | Pic 1 (`#3`) | 3-Petal Upward Tulip | Fuchsia Crimson, Teal Stamen | Lv 1 (Core) |
| `tile_04` | **Marigold Daisy** | Pic 1 (`#4`) | Concentric Sunburst | Warm Orange (`#FF8C00`), Magenta | Lv 1 (Core) |
| `tile_05` | **Meadow Cosmos** | Pic 1 (`#5`) | Scalloped Disc Flower | Vivid Lemon Yellow (`#FFEB3B`) | Lv 5 (Core) |
| `tile_06` | **Botanical Leaf Sprig** | Pic 1 (`#6`) | S-Curved Leafy Stalk | Bright Cyan, Deep Indigo | Lv 5 (Core) |
| `tile_07` | **Symmetric Frond** | Pic 1 (`#8`) | Bilateral Winged Frond | Teal Green, Gold Sprout | Lv 5 (Core) |
| `tile_08` | **Core Starburst Rosette** | Pic 2 (`#10`)| 8-Point Geometric Star | Amber Gold, Crimson Heart | Lv 8 (Core) |
| `tile_09` | **Full Kaleidoscope Medallion**| Pic 2 (`#11`)| Concentric Mandala Ring | Coral Red, Aqua Cyan, Gold | Lv 10 (Core) |
| `tile_10` | **Cardinal Lotus Bloom** | Pic 2 (`#12`)| Outward Scalloped Lotus | Flame Red (`#FF3D00`), Cyan | Lv 10 (Core) |
| `tile_11` | **Satellite Mini Rosette** | Pic 2 (`#14`)| Circular Button Rosette | Coral Red, Aqua Teal Core | Lv 12 (Core) |
| `tile_12` | **Crown Feather Plume** | Pic 2 (`#16`)| Triple Feather Plume Crest | Aqua Cyan, Cobalt Blue | Lv 12 (Core) |
| `tile_13` | **Curved Leaf Bough** | Pic 2 (`#17`)| Arc Perimeter Branch | Cyan, Cobalt, Gold Buds | Lv 15 (Core) |
| `tile_14` | **Scalloped Tulip Bell** | Pic 2 (`#18`)| Fluted Hanging Bell | Crimson Coral, Cyan Flutes | Lv 15 (Core) |
| `tile_15` | **Slavic Rose Medallion** | Pic 3 (`#19`)| 8-Fold Circular Rosette | Cornflower Blue, Amber, Ruby | Lv 18 (Core) |
| `tile_16` | **Cardinal Fleur Finial** | Pic 3 (`#21`)| Outward Fleur-de-lis Crest | Periwinkle Blue, Teal Accents | Lv 18 (Core) |
| `tile_17` | **Teardrop Bloom Bud** | Pic 1 (`#7`) | Delicate Turquoise Bud | Turquoise, Fuchsia Tip | **Lv 21+ (Master)** |
| `tile_18` | **Bicolor Leaf Accent** | Pic 1 (`#9`) | Twin Accent Teardrop Leaves | Cyan, Midnight Violet | **Lv 21+ (Master)** |
| `tile_19` | **Foliage Sprout Accent** | Pic 2 (`#15`)| Angular Diamond Sprout | Golden Yellow, Teal Wing | **Lv 25+ (Master)** |
| `tile_20` | **Corner Sun-Daisy Variant** | Pic 2 (`#13`)| 12-Petal Radiant Sunflower | Lemon Yellow, Crimson Eye | **Lv 25+ (Master)** |
| `tile_21` | **Golden Shield Petal** | Pic 3 (`#23`)| Inward Shield Heart | Amber Gold, Crimson Rib | **Lv 30+ (Master)** |
| `tile_22` | **Crimson Spear Ray** | Pic 3 (`#24`)| Radiating Spearhead Petal | Vibrant Crimson, Gold Base | **Lv 30+ (Master)** |
| `tile_23` | **Aqua Scalloped Crest** | Pic 3 (`#25`)| Perimeter Scalloped Fan | Aqua Cyan, Periwinkle Fringe | **Lv 35+ (Master)** |
| `tile_24` | **Periwinkle Droplet Cluster** | Pic 3 (`#26`)| Multi-Droplet Cluster | Soft Cornflower Blue | **Lv 35+ (Master)** |

---

## 4. Dual-Theme Visual & 3D Material Specifications

The 24 tiles and the app interface are rendered in two contrasting luxury styles:

```
       320px
   ┌───────────┐
   │ ╭───────╮ │ 18px top margin
   │ │  Art  │ │
   │ │ Layer │ │ 360px
   │ ╰───────╯ │
   │  ═══════  │ 18px lower 3D bevel extrusion
   │  ░░░░░░░  │ Ambient occlusion cast shadow
   └───────────┘
```

### Strict 3D Tile Engineering Standards:
* **Dimensions:** Exactly **$320 \times 360\text{px}$ RGBA** (standard AuroMatch 8:9 tile ratio).
* **Zero Black Borders:** $100\%$ transparent outer canvas ($\alpha = 0$). Only the physical 3D tile slab is rendered.
* **Elevated Extrusion:** $18\text{px}$ lower isometric bevel with realistic ambient occlusion drop shadow.
* **Gleaming Specular Sheen:** Diagonal gloss light ribbons and pure white specular glints on bevel rims.

### Theme 1: ☀️ Imperial Gold Reliquary (Day / Solar Luxury)
* **Backdrop:** Deep warm rose-amber vignette (`#24121c` to `#0e080e`) with glowing solar amber light.
* **Tile Slab:** Warm polished ivory ceramic encased in **heavy 24K gold chamfered borders**.
* **Emblem Craft:** Raised gold wire cloisonné holding faceted ruby, emerald, and electric turquoise enamels.
* **UI Elements:** Warm gilded gold borders on buttons, golden tray rims, and amber mode glow.

### Theme 2: 🌙 Royal Lapis & Midnight Cloisonné (Night / Astral Luxury)
* **Backdrop:** Deep royal lapis navy vignette (`#0a1024` to `#040610`) with starlight nebulae.
* **Tile Slab:** Mirror-finish **deep ultramarine lapis ceramic** bound in burnished brass rims.
* **Emblem Craft:** Raised gold wire filigree filled with gleaming vitreous enamels.
* **UI Elements:** Electric cyan and royal sapphire glows, antique brass borders, and midnight slate dialogs.

---

## 5. Global Game UI Shell Transformation

The surrounding game UI shell transforms from the current basic styling into an **elevated luxury frame**:

| UI Component | Current State (Baseline) | Upgraded State (Dual Theme) |
|---|---|---|
| **Header Bar** | Flat translucent dark bar | Polished metallic top trim with gilded currency badges & level badge |
| **Category Pills** | Generic rounded buttons | 3D beveled pills with active theme glow (Amber Gold or Electric Cyan) |
| **Match-3 Tray** | Basic flat container | Beveled metallic 7-slot tray with glowing slot counter (`3 / 7`) |
| **Power-Up Bar** | Simple circular buttons with text | High-relief 3D circular buttons with metallic wire rims & clear hover glows |
| **Modals / Overlays** | Plain modal popups | Luxury parchment/slate dialogs with gold foil borders & celebratory particle accents |
| **Live Theme Switcher** | None | 1-Tap Header Button (`[ ☀️ Imperial Gold ]` / `[ 🌙 Royal Lapis ]`) |

---

## 6. Full App Visual Mockup

![Dual Theme Full App Mockup](C:/Users/gkpan/.gemini/antigravity/brain/ec13e5c0-8407-44b4-9746-5bdf749505cf/theme_dual_app_mockup.png)

---

## 7. Technical Implementation Steps

### Phase 1: 3D Asset Pack Generation
* `AuroMatch/assets/themes/standard_gold/`
  * `tile_01.png` to `tile_24.png` (24K Gold Ingot 3D tiles, 320x360 RGBA)
  * `bg_gold.png` (Rose-Amber Solar Vignette wallpaper)
* `AuroMatch/assets/themes/standard_lapis/`
  * `tile_01.png` to `tile_24.png` (Royal Lapis 3D tiles, 320x360 RGBA)
  * `bg_lapis.png` (Royal Lapis Starlight Vignette wallpaper)

### Phase 2: GameManager Integration (`gameManager.js`)
* In `startLevel()` / tile initialization:
  * If `isRealmsMode`: assign `this.activeRealm.customTiles` and `this.activeRealm.bgImage` (**100% untouched**).
  * If NOT `isRealmsMode` (`Pairs`, `Tile Club`, `Classic`): assign tiles from the active standard theme (`standard_gold` or `standard_lapis`) and apply the matching atmospheric background.

### Phase 3: Global CSS & DOM System
* Add `data-app-theme="imperial_gold"` / `"royal_lapis"` to `<body>`.
* Wire CSS custom properties for header accents, tray frames, power-up buttons, and dialogs.

### Phase 4: Header Live Theme Toggle
* Add interactive toggle button in the header bar.
* Handle live switching with instant visual transition (no reload).
* Persist player preference in `localStorage`.

### Phase 5: QA Solvability & Visual Verification
* Run automated solvability tests across Levels 1–50.
* Verify mobile and desktop layout integrity.
