# Tile Match & Mahjong Specific Analysis: Deconstructing Vita Mahjong & Tile Club

---

## 1. Comparative Analysis Matrix

| Feature / Dimension | *Vita Mahjong* (Vita Studio) | *Tile Club* (Gameduell) | *AuroMatch* (AuroProject) |
| :--- | :--- | :--- | :--- |
| **Match Mode** | Pair Matching (Match-2) | Triad Tray Matching (Match-3) | **Dual Mode (Match-2 & Match-3)** |
| **Board View** | 2D/2.5D Classic Mahjong | 3D Isometric Stack | **2.5D Isometric Canvas** |
| **Tile Size** | Oversized ($60 \times 80\text{px}$) | Standard ($48 \times 64\text{px}$) | **Massive ($68 \times 88\text{px}$, +25% Senior)** |
| **Solvability Algorithm**| Random shuffle with reshuffles | Random distribution | **Reverse Construction Guaranteed** |
| **Occlusion Feedback** | Edge-border highlight | Subtle drop shadow | **50% Dimming on Blocked Tiles** |
| **Tray Overflow Sound**| Sharp buzzer | Warning chime + ad | **Warm 196Hz Non-Startle Hum** |
| **Audio Tuning** | Standard 440Hz samples | Commercial pop synths | **432Hz Prahar Ragas & Bronze** |
| **Monetization** | Ad-supported + coin shop | Aggressive booster shop | **0% Ads / Voluntary Dakshina** |

---

## 2. In-Depth Mechanical Breakdown

### 2.1 Why Did Vita Mahjong Reach 126M Downloads?
* Traditional mobile games treat seniors as an afterthought, with tiny buttons, low contrast, and frantic timers.
* *Vita Mahjong* proved that the senior market ($\ge 60$) is vast, loyal, and hungers for:
  1. **Massive touch targets** that accommodate reduced fingertip sensitivity.
  2. **High-contrast visual legibility** without confusing background clutter.
  3. **Zero timer anxiety.**

### 2.2 The Trap of Random Tile Placement
* Many commercial tile matchers randomly place tiles on a 3D layout. If the 3rd tile of a set is buried beneath its two siblings, the player can be mathematically trapped with an empty tray or board deadlock.
* **Our Solution: Reverse Construction Solvability.** By generating the puzzle backwards from an empty solved state, we guarantee that every level has a natural, beautiful path to completion without ever needing paid reshuffles.
