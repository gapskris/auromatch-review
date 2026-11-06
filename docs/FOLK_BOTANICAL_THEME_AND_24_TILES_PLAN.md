# AuroMatch: Folk Botanical Theme & 24-Tile Progressive Architecture Plan

> **Status:** Saved for Execution  
> **Target Theme:** `folk_botanical` / `otomi_mandala`  
> **Inspiration Sources:** 3 Folk Art Reference Images (Mexican Otomi, Polish Wycinanki, Slavic/Scandinavian Rosette)  
> **Tile Format:** Native $320 \times 360\text{px}$ RGBA with 3D tactile bevel, zero black borders, and cloisonné enamel floral relief  

---

## 1. Executive Summary & Vision

This plan documents the design, mathematical balancing, and production architecture for introducing the **Folk Botanical** theme to `AuroMatch`.

Unlike static 16-tile themes that repeat identical motifs across large boards, this theme introduces a **24-Tile Dynamic Progression Architecture**:
* **Early Levels (1–8):** Simple 12–24 tile formations utilizing 4–8 introductory floral archetypes.
* **Mid Levels (9–20):** Standard 36–48 tile boards utilizing the complete **Tier 1 (Core 16 tiles)**.
* **Advanced & Master Levels (21–50+):** Monumental 60–108 tile multi-layer stacks introducing **Tier 2 (8 Master expansion tiles)**, bringing the active pool to **24 distinct motifs** and eliminating repetitive board clutter.

---

## 2. Dynamic Progression & Difficulty Mathematics

In `AuroMatch`, the number of distinct flora/tile kinds required on the board scales dynamically:

$$\text{Distinct Tile Kinds} = \max\left(3, \left\lfloor \frac{\text{Total Board Tiles}}{K} \right\rfloor\right)$$

Where $K = 3$ for Match-3 (Tile Club) and $K = 2$ for Mahjong Solitaire (Pairs).

```
                      LEVEL PROGRESSION & TILE POOL
                      
  Lv 1-8 (12-24 Tiles)       Lv 9-20 (36-48 Tiles)       Lv 21-50+ (60-108 Tiles)
 ┌─────────────────────┐   ┌────────────────────────┐   ┌────────────────────────┐
 │   4 to 8 Motifs     │ ─►│     16 Motifs (Core)   │ ─►│   24 Motifs (Master)   │
 │ (Daisies & Tulips)  │   │ (+ Palmettes, Leaves)  │   │ (+ Fins, Plumes, Rays) │
 └─────────────────────┘   └────────────────────────┘   └────────────────────────┘
```

| Level Tier | Formation Size | Unique Kinds ($K=3$) | Unique Kinds ($K=2$) | Active Motifs |
|---|---|---|---|---|
| **Tier 1A (Early)** | 12 – 24 tiles | 4 – 8 kinds | 6 – 12 kinds | Tiles 01 – 08 |
| **Tier 1B (Mid)** | 36 – 48 tiles | 12 – 16 kinds | 16 kinds (max) | Tiles 01 – 16 (Full Core) |
| **Tier 2 (Advanced)**| 60 – 72 tiles | 20 – 24 kinds | 24 kinds | Tiles 01 – 24 (Full Master) |
| **Tier 3 (Master)** | 84 – 108 tiles | 24 kinds (curated) | 24 kinds | Full 24-Tile Diversity |

---

## 3. The 24-Tile Master Roster

Deconstructed from the 27 cataloged elements across the 3 reference images:

| Tile ID | Motif Name | Source Image | Archetype / Silhouette | Dominant Colors | Level Unlock |
|---|---|---|---|---|---|
| `tile_01` | **Top Rosette Daisy** | Pic 1 (`#1`) | 8-Petal Radial Rosette | Magenta (`#EB0F73`), Amber, Cyan | Lv 1 |
| `tile_02` | **Grand Lotus Palmette** | Pic 1 (`#2`) | Scalloped Peacock Fan | Gold, Fuchsia, Deep Teal | Lv 1 |
| `tile_03` | **Folk Tulip** | Pic 1 (`#3`) | 3-Petal Upward Tulip | Fuchsia Crimson, Teal Stamen | Lv 1 |
| `tile_04` | **Marigold Daisy** | Pic 1 (`#4`) | Concentric Sunburst | Warm Orange (`#FF8C00`), Magenta | Lv 1 |
| `tile_05` | **Meadow Cosmos** | Pic 1 (`#5`) | Scalloped Disc Flower | Vivid Lemon Yellow (`#FFEB3B`) | Lv 5 |
| `tile_06` | **Botanical Leaf Sprig** | Pic 1 (`#6`) | S-Curved Leafy Stalk | Bright Cyan, Deep Indigo | Lv 5 |
| `tile_07` | **Symmetric Frond** | Pic 1 (`#8`) | Bilateral Winged Frond | Teal Green, Gold Sprout | Lv 5 |
| `tile_08` | **Core Starburst Rosette** | Pic 2 (`#10`)| 8-Point Geometric Star | Amber Gold, Crimson Heart | Lv 8 |
| `tile_09` | **Full Kaleidoscope Medallion**| Pic 2 (`#11`)| Concentric Mandala Ring | Coral Red, Aqua Cyan, Gold | Lv 10 |
| `tile_10` | **Cardinal Lotus Bloom** | Pic 2 (`#12`)| Outward Scalloped Lotus | Flame Red (`#FF3D00`), Cyan | Lv 10 |
| `tile_11` | **Satellite Mini Rosette** | Pic 2 (`#14`)| Circular Button Rosette | Coral Red, Aqua Teal Core | Lv 12 |
| `tile_12` | **Crown Feather Plume** | Pic 2 (`#16`)| Triple Feather Plume Crest | Aqua Cyan, Cobalt Blue | Lv 12 |
| `tile_13` | **Curved Leaf Bough** | Pic 2 (`#17`)| Arc Perimeter Branch | Cyan, Cobalt, Gold Buds | Lv 15 |
| `tile_14` | **Scalloped Tulip Bell** | Pic 2 (`#18`)| Fluted Hanging Bell | Crimson Coral, Cyan Flutes | Lv 15 |
| `tile_15` | **Slavic Rose Medallion** | Pic 3 (`#19`)| 8-Fold Circular Rosette | Cornflower Blue, Amber, Ruby | Lv 18 |
| `tile_16` | **Cardinal Fleur Finial** | Pic 3 (`#21`)| Outward Fleur-de-lis Crest | Periwinkle Blue, Teal Accents | Lv 18 |
| `tile_17` | **Teardrop Bloom Bud** | Pic 1 (`#7`) | Delicate Turquoise Bud | Turquoise, Fuchsia Tip | **Lv 21+** |
| `tile_18` | **Bicolor Leaf Accent** | Pic 1 (`#9`) | Twin Accent Teardrop Leaves | Cyan, Midnight Violet | **Lv 21+** |
| `tile_19` | **Foliage Sprout Accent** | Pic 2 (`#15`)| Angular Diamond Sprout | Golden Yellow, Teal Wing | **Lv 25+** |
| `tile_20` | **Corner Sun-Daisy Variant** | Pic 2 (`#13`)| 12-Petal Radiant Sunflower | Lemon Yellow, Crimson Eye | **Lv 25+** |
| `tile_21` | **Golden Shield Petal** | Pic 3 (`#23`)| Inward Shield Heart | Amber Gold, Crimson Rib | **Lv 30+** |
| `tile_22` | **Crimson Spear Ray** | Pic 3 (`#24`)| Radiating Spearhead Petal | Vibrant Crimson, Gold Base | **Lv 30+** |
| `tile_23` | **Aqua Scalloped Crest** | Pic 3 (`#25`)| Perimeter Scalloped Fan | Aqua Cyan, Periwinkle Fringe | **Lv 35+** |
| `tile_24` | **Periwinkle Droplet Cluster** | Pic 3 (`#26`)| Multi-Droplet Cluster | Soft Cornflower Blue | **Lv 35+** |

---

## 4. 3D Tile Production Specification

> [!IMPORTANT]
> **Zero Black Borders & Strict Uniform Dimensions:**
> All 24 tiles are rendered on a transparent background ($\alpha = 0$). Only the physical 3D tile slab is rendered.

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

1. **Dimensions:** Exactly **$320 \times 360\text{px}$** (standard AuroMatch 8:9 tile ratio).
2. **Tile Body (Slab):**
   * Rounded corners ($\text{radius} = 32\text{px}$).
   * Dark volcanic slate finish (`#181c2a` to `#262e44`) with subtle satin specular sheen.
   * Extruded lower bevel ($18\text{px}$ depth) providing tangible isometric thickness.
   * Soft ambient occlusion drop shadow beneath the slab.
3. **Embossed 3D Folk Artwork:**
   * Motifs rendered in raised **cloisonné enamel** with gold wire borders.
   * Petals and leaves physically catch light with highlights and cast shadows onto the tile surface.
   * Zero flat scan artifacts, zero compression noise, razor-sharp vector-crisp edges.

---

## 5. Technical Implementation Steps (When Resuming)

1. **Asset Generation:**
   * Generate `tile_01.png` through `tile_24.png` in `AuroMatch/assets/themes/folk_botanical/`.
   * Generate theme wallpaper `background.png` (matching folk tapestry texture).
2. **Engine Registration (`themeManager.js`):**
   * Add `folk_botanical` definition to `THEME_TILE_DEFS` with 24 custom titles and emoji symbols.
   * Ensure `buildCustomTilesForTheme('folk_botanical')` maps all 24 paths.
3. **Solvability & QA Verification:**
   * Run automated reverse-construction solvability verification across Levels 1–50 using `VitaBoardGenerator`.
