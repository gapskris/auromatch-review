# AuroMatch Architecture Plan: Decoupled Rules & Thematic Worlds

> **Status:** Saved & Ready for Implementation  
> **Date:** October 26, 2026  
> **Repositories:** `AuroMatch` & `auromatch-play` (`main` branch)

---

## 1. Executive Summary & Core Discovery

Through our deep architectural audit and layout discussions, we resolved a fundamental game design challenge: **Rules (how tiles match)** and **Themes (what the tiles and environment look like)** were previously mixed together in a single cramped button bar, causing severe mobile clipping and preventing players from experiencing all game modes in different visual worlds.

### The Fundamental Separation
```
+-------------------------------------------------------------------------+
|                         1. THE 2 RULES                                  |
|                         (How you match)                                 |
|   • 🪷 Pairs (Match 2) - Direct dissolve, no tray, relaxing              |
|   • 📥 Tile Club (Match 3) - 7-slot holding tray, tactical triads       |
+-------------------------------------------------------------------------+
                                    |
                          PLAYED FREELY ACROSS
                                    v
+-------------------------------------------------------------------------+
|                      2. THEMES & REALMS                                 |
|                  (Visual Worlds & Dedicated Tile Sets)                  |
|   • Chapter 1: Service Tree Sanctuary                                   |
|   • Chapter 14: Sunlit Lotus Pond                                       |
|   • Chapter 17: Obsidian Observatory (Planet)                           |
|   • Chapter 18: Golden Harvest (Rattan)                                 |
|   • Chapter 19: Iridescent Opal (Ice & Aurora)                          |
|   • Future Themes: Emerald Jungle, Desert of Amber, Volcanic Hearth...  |
+-------------------------------------------------------------------------+
```

- **Pairs, Tile Club, and Classic are not separate content silos** — they are matching mechanics.
- **"Classic" Solitaire** ran the exact same code as Pairs (Match-2); retiring the redundant "Classic" button simplifies the game to the **two true matching rules**.
- **Every Theme** (the 20 built-in chapters, plus future worlds like *Jungle*, *Desert*, *Planet*, and *Ice*) consists of **16 custom carved 3D tiles + environmental wallpaper + ambient raga**.
- **The Interlinking Breakthrough**: By decoupling the engine, **any theme can be played using Pairs OR Tile Club rules**.

---

## 2. The 20 Existing Themes Ready to Interlink

All 20 of these themes are already fully built in `ThemeManager.js` with 16 dedicated 3D tiles each (320 custom tiles total):

| Chapter | Theme Name | Visual Tile Material & Archetype | Background Wallpaper |
| :---: | :--- | :--- | :--- |
| **1** | 🌳 Service Tree Sanctuary | Carved Banyan & Ivory | Ashram Courtyard |
| **2** | 🏛️ Golconde Modernist Slate | Dark Polished Slate & Teakwood | Golconde Architectural |
| **3** | 📜 SABDA Wisdom Library | Embossed Leather & Gold Leaf | Grand Archive Library |
| **4** | 💎 Aquamarine Celestial Glass | Prismatic Translucent Glass | High Celestial Stratosphere |
| **5** | 🌌 Molten Amber Nebula | Glowing Amber & Cosmic Plasma | Deep Space Nebula |
| **6** | 🔥 Brass Altar & Sacred Flame | Cast Temple Brass & Embers | Sacred Agni Hearth |
| **7** | 🪵 Sacred Teak Shrine | Hand-Carved Teakwood Grain | Wooden Altar Pavilion |
| **8** | 🌊 Coromandel Coastline | Seashell, Pearl & Ocean Jade | Bay of Bengal Horizon |
| **9** | 🏺 Ancient Terracotta Banyan | Sun-Baked Terracotta Clay | Sacred Banyan Grove |
| **10** | 🌸 Twelve Sacred Petals | Rose Quartz & Fine Porcelain | Matrimandir Lotus Gardens |
| **11** | 💠 Enameled Porcelain Mandala | Cobalt Enamel & Cloisonné Wire | Temple Fresco Wall |
| **12** | 🌀 Sacred Spiral Mandala | Imperial Jade & Burnished Bronze | Sacred Geometry Mosaic |
| **13** | ⚪ White Marble Master Shrine | Makrana Marble & Gold Inlay | White Samadhi Shrine |
| **14** | 🪷 Sunlit Lotus Pond | River Quartz & Translucent Lilypad | Sunlit Water Garden |
| **15** | 🏔️ Himalayan Granite Monolith | Sparkling Silver Granite & Quartz | Snow-Capped Himalayan Peak |
| **16** | 👑 Royal Sandalwood & Amber | Mysore Sandalwood & Golden Resin | Royal Sandalwood Chamber |
| **17** | 🪐 Obsidian Observatory (Planet) | Jet Black Obsidian & Laser Platinum | Starlit Telescope Observatory |
| **18** | 🌾 Golden Harvest & Woven Rattan | Cane Wicker, Rattan & Ripe Wheat | Sunset Harvest Field |
| **19** | 🌈 Iridescent Opal & Aurora (Ice) | Fire Opal, Ice Crystal & Prism Wave | Polar Aurora Borealis |
| **20** | 🍃 Sacred Bodhi Grove | Sacred Gold Leaf & Verdigris Bronze | Enlightenment Bodhi Tree |

> **Future Expansion:** Whenever you create a new theme (*e.g. #21 Emerald Jungle, #22 Desert of Amber, #23 Volcanic Hearth*), you only supply 16 tiles and a background. It **instantly inherits both Pairs and Tile Club gameplay** with zero extra programming.

---

## 3. Top HUD Bar: The Clean Mobile Architecture

Instead of 5 cluttered buttons that previously clipped on mobile screens, the top bar is streamlined into **two sleek pills**:

```
+------------------------------------------------------------------------+
|  MOBILE TOP HUD BAR (Fits easily in < 320px width)                     |
|                                                                        |
|   [ 🌴 Jungle Sanctuary ▾ ]      [ 🪷 Pairs  |  📥 Tile Club ]    [Aa] |
|   +----------+------------+      +--------------+------------+         |
|              |                                  |                      |
|       THEME SELECTOR                    2-RULE TOGGLE                  |
|    Opens Visual Gallery              Instant 1-Tap Switch              |
+------------------------------------------------------------------------+
```

### 1. Left Pill: The World/Theme Selector (`[ 🌴 Jungle ▾ ]`)
- Displays current theme icon and title.
- Tapping it slides up a **Theme Gallery Sheet** with cards for all 20 chapters plus any future worlds.
- Tapping a card dynamically morphs the background wallpaper and tile textures.

### 2. Right Pill: The Rules Switcher (`[ 🪷 Pairs | 📥 Tile Club ]`)
- A connected 2-state segmented capsule.
- **1-Tap Instant Toggle**:
  - Selecting **Tile Club**: Slides the 7-slot holding tray into view at the bottom and activates triad match-3 logic.
  - Selecting **Pairs**: Hides the tray and lets tiles dissolve directly in pairs of 2.

---

## 4. Implementation Blueprint (Phased Rollout)

### Phase 1: Engine Decoupling (`GameManager.js`)
- Separate single `gameplayMode` into two independent properties:
  ```javascript
  this.gameplayRule = 'tile_club';        // 'vita' (Pairs) | 'tile_club'
  this.activeThemeId = 'whispering_pines'; // 'service_tree', 'obsidian', 'lotus', etc.
  ```
- Retain backward compatibility so existing saves and functions work without disruption.
- Ensure `handleTileClick()` uses `this.gameplayRule` for resolution logic, regardless of which theme's tiles are on the board.

### Phase 2: Theme Asset Skinning Bridging
- Ensure `startNewStage(levelNum)` pulls `customTiles` from `this.activeThemeId`.
- If `gameplayRule === 'tile_club'`, generate $K=3$ triads using that theme's 16 tiles.
- If `gameplayRule === 'vita'`, generate $K=2$ pairs using that theme's 16 tiles.

### Phase 3: UI Dual-Pill & Gallery Sheet Deployment
- Replace the legacy 5-button bar in `index.html` with the **Theme Pill** and **2-Rule Segmented Capsule**.
- Add the slide-up **Theme Gallery Modal** with visual thumbnails for the 20 realms.

### Phase 4: Automated Testing & Visual Verification
- Run all 20 tests in `AuroMatch/tests/qa_suite.test.js`.
- Execute headless Chromium CDP verification:
  - Mobile $390\text{px}$: Verify zero clipping and seamless theme/rule toggles.
  - Desktop $1440\text{px}$: Verify centered layout and zero tray collision.
- Recompile bundle via `scripts/build_prototype.py` and push to GitHub Pages.

---

## 5. Decision Stored for Resumption

When you return, we only need your preference on one simple question:
> **Default Rule on First Boot:** Would you like new players to start in **Tile Club** (Match-3 in tray) or **Pairs** (Match-2 direct)?

*(Everything else is mapped out, audited, and ready to implement).*
