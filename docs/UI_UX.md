# UI/UX & Senior Accessibility Specification: AuroMatch

---

## 1. Ergonomic Viewport & Screen Hierarchy

```
+-------------------------------------------------------------------------+
| [AuroMatch]          Sanctuary 3: Golconde Slate          [Aa Senior]   | <- Top Navigation Bar (54px)
| Mode: [ Vita Mahjong | Tile Club v ]         Time: Sandhya (Evening)    |
+-------------------------------------------------------------------------+
|                                                                         |
|                                                                         |
|                     [■] [■] [■]                                         |
|                 [■] [■] [■] [■] [■]                                     |
|             [■] [■] [■] [■] [■] [■] [■]                                 |
|                 [■] [■] [■] [■] [■]         3D Isometric Tile Stack     |
|                     [■] [■] [■]             (Height: 500px)             |
|                                                                         |
|                                                                         |
+-------------------------------------------------------------------------+
|                                                                         |
|   +-----------------------------------------------------------------+   |
|   | [Rose] [Rose] [Lotus] [  ] [  ] [  ] [  ]                       |   | <- 7-Slot Sacred Tray
|   +-----------------------------------------------------------------+   |    (Height: 96px)
|                                                                         |
+-------------------------------------------------------------------------+
|   [Prana Undo]            "Gratitude brings peace"        [Auto-Sort]   | <- Footer Control Bar (64px)
+-------------------------------------------------------------------------+
```

---

## 2. Senior-First Accessibility Innovations

Following the global success of *Vita Mahjong* (126M senior downloads), AuroMatch implements dedicated aging-adult accessibility features:

### 2.1 The `[Aa]` Senior View Mode Toggle
* **Scale Enhancement:** Expands active tile dimensions by $+25\%$ ($68 \times 88\text{px} \rightarrow 85 \times 110\text{px}$).
* **Occlusion Dimming:** Blocked/covered tiles have their brightness reduced by $50\%$ and saturation reduced by $60\%$, instantly clarifying which tiles are available to tap.
* **Selection Halo:** Tapped tiles receive a pulsating $4\text{px}$ golden halo (`#D4AF37`) with high visual contrast.

### 2.2 Motor & Auditory Comfort
* **Zero Startle Audio:** Commercial puzzle games trigger sudden buzzer noises when trays fill up. AuroBlocks plays a soft, warm $196\text{ Hz}$ harmonic hum that invites a calm undo without alarming sensitive nervous systems.
* **Large Touch Tolerances:** Minimum clickable tile area exceeds $68 \times 88\text{px}$, preventing missed taps from minor finger tremors.

---

## 3. The Botanical Virtue Card (Match Dialog)

When a flower triad or pair clears, a subtle floating card reveals the flower's botanical and spiritual quality:

```
+-------------------------------------------------------+
|                                                       |
|                  [ HIBISCUS ROSA ]                    |
|                                                       |
|                        Power                          |
|                                                       |
|      "The quiet strength that acts without violence   |
|           and remains steady in all storms."          |
|                                                       |
+-------------------------------------------------------+
```

* **Zero Gameplay Interruption:** The card floats in the upper corner for $2.4$ seconds without halting tile interactions or freezing the game loop.
