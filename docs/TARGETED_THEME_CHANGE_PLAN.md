# AuroMatch: Targeted UI & Standard Categories Theme Architecture Plan

> **Scope & Boundary Protection:**  
> 🔒 **Realms Mode:** 100% Preserved. The 20 Secular Realms, custom realm tiles, and dedicated background wallpapers remain completely untouched.  
> ✨ **Targeted Upgrades:**  
> 1. **Global Game UI:** Header HUD, Mode pills, Match-3 Tray, Action power-up bar, and Dialogs.  
> 2. **Standard Categories ("Pairs", "Tile Club", "Classic"):** Full upgrade of playable 3D tiles and atmospheric backdrops to the new shining elevated dual-theme system (**Imperial Gold** vs **Royal Lapis**).

---

## 1. Architectural Boundaries: What Changes vs. What Stays

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

## 2. Global Game UI Upgrade Specification

The surrounding game UI shell transforms from the current basic styling into an **elevated luxury frame**:

| UI Component | Current State (Baseline) | Upgraded State (Dual Theme) |
|---|---|---|
| **Header Bar** | Flat translucent dark bar | Polished metallic top trim with gilded currency badges & level badge |
| **Category Pills** | Generic rounded buttons | 3D beveled pills with active theme glow (Amber Gold or Electric Cyan) |
| **Match-3 Tray** | Basic flat container | Beveled metallic 7-slot tray with glowing slot counter (`3/7`) |
| **Power-Up Bar** | Simple circular buttons with text | High-relief 3D circular buttons with metallic wire rims & clear hover glows |
| **Modals / Overlays** | Plain modal popups | Luxury parchment/slate dialogs with gold foil borders & celebratory particle accents |
| **Theme Switcher** | None | 1-Tap Header Button (`[ ☀️ Imperial Gold ]` / `[ 🌙 Royal Lapis ]`) |

---

## 3. Categories "Pairs", "Tile Club", & "Classic" Upgrade

In the current code ([`gameManager.js` lines 384–402](file:///C:/DataScience/AuroProject_Annalysis/AuroMatch/src/controllers/gameManager.js#L384-L402)), standard modes fall back to an untextured "cream ivory / walnut wood" mixed deck on an empty background (flat green felt).

### New Implementation for Pairs, Tile Club, & Classic:
1. **Atmospheric Backdrops (Replacing Flat Green):**
   * **Imperial Gold Active:** Deep warm rose-amber vignette (`#24121c` to `#0e080e`) with radiant sunrise glow.
   * **Royal Lapis Active:** Deep royal navy lapis lazuli vignette (`#0a1024` to `#040610`) with starlight nebula dust.
2. **Playable 3D Tile Assets:**
   * Instead of plain cards, the board loads the **24-tile elevated shining set**:
     * **Imperial Gold:** 24K gold chamfered borders with warm ivory face and faceted cloisonné jewel enamels.
     * **Royal Lapis:** Mirror-finish ultramarine lapis ceramic with burnished brass rims and raised gold wire filigree.
   * Both themes use our strictly calibrated **$320 \times 360\text{px}$ RGBA** format with **zero black borders** ($\alpha = 0$) and $18\text{px}$ isometric 3D bevels.
3. **Dynamic Scaling (Levels 1–50+):**
   * Levels 1–20 automatically draw from the **Core 16 tiles**.
   * Large multi-tier formations (Levels 21–50+) expand to utilize all **24 tiles**, eliminating repetitive boards.

---

## 4. Preservation Protocol for Realms Mode

To ensure zero interference with the 20 Realms:
1. In [`gameManager.js`](file:///C:/DataScience/AuroProject_Annalysis/AuroMatch/src/controllers/gameManager.js), if `isRealmsMode` is true:
   * `this.tiles` strictly uses `this.activeRealm.customTiles` (e.g. Whispering Pines bark/leaves, Temple of Lines slates, etc.).
   * Background strictly loads `this.activeRealm.bgImage`.
2. The Global UI (Header, Tray, Bottom Bar) remains harmoniously styled without overriding the realm's internal tile textures or wallpaper.

---

## 5. Technical Implementation Roadmap

```
Step 1: Generate Standard 3D Asset Sets
├── assets/themes/standard_gold/ (tile_01.png to tile_24.png + bg_gold.png)
└── assets/themes/standard_lapis/ (tile_01.png to tile_24.png + bg_lapis.png)

Step 2: Update GameManager Tile Assignment
└── In gameManager.js: When !isRealmsMode, assign tiles from standard_gold or standard_lapis
    based on active user theme preference.

Step 3: Global CSS Custom Properties System
└── Add data-theme="imperial_gold" / "royal_lapis" to <body>.
    Update header, mode pills, tray container, and power-up buttons with theme variables.

Step 4: Header Live Theme Toggle
└── Insert sleek 1-tap toggle button in header to switch between ☀️ Gold and 🌙 Lapis.
    Persist choice in localStorage.

Step 5: QA Verification
└── Verify Pairs, Tile Club, and Classic display new 3D tiles & backdrops.
└── Verify Realms mode remains 100% authentic with its existing custom tiles and wallpapers.
```
