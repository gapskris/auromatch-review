# Visual Design Proposal — 3D Colorful Tiles & Spiritual Aura Glows

To align with Sri Maa's love for vibrant colors and the spiritual significances associated with them, the production version of AuroMatch will feature a premium, tactile, and highly attractive visual design.

![AuroMatch 3D Board Mockup](/C:/Users/gkpan/.gemini/antigravity/brain/ec13e5c0-8407-44b4-9746-5bdf749505cf/auromatch_board_mockup_1785929901083.jpg)

---

## 1. 3D Glassmorphic Tile Design

Instead of flat, plain tile blocks, the tiles will be styled as **3D glassmorphic medallions**. We will achieve this using native CSS:

```css
/* Core 3D Tile Medallion Style */
.tile-3d {
    position: absolute;
    width: 50px;
    height: 66px;
    border-radius: 12px;
    background: linear-gradient(135deg, rgba(255,255,255,0.9) 0%, rgba(245,240,230,0.8) 100%);
    
    /* Layered 3D shadows for tactile beveled edges */
    box-shadow: 
        inset 0 2px 0 rgba(255, 255, 255, 0.6),           /* Top highlight */
        inset 0 -2px 0 rgba(0, 0, 0, 0.1),                /* Bottom inset shadow */
        0 4px 6px rgba(0, 0, 0, 0.15),                     /* Soft drop shadow */
        0 8px 0 var(--tile-depth-color),                   /* 3D block depth */
        0 12px 24px rgba(0, 0, 0, 0.3);                    /* Deep ambient shadow */
        
    transition: transform 0.2s cubic-bezier(0.25, 1, 0.5, 1), box-shadow 0.2s ease;
}

/* Hover & Active Tactile States */
.tile-3d:not(.blocked):hover {
    transform: translateY(-4px);
    box-shadow: 
        inset 0 2px 0 rgba(255, 255, 255, 0.7),
        inset 0 -2px 0 rgba(0, 0, 0, 0.1),
        0 6px 10px rgba(0, 0, 0, 0.2),
        0 12px 0 var(--tile-depth-color),
        0 16px 32px rgba(0, 0, 0, 0.4);
}

.tile-3d:active {
    transform: translateY(4px); /* Pushes down into the depth */
    box-shadow: 
        inset 0 1px 0 rgba(255, 255, 255, 0.4),
        0 1px 2px rgba(0, 0, 0, 0.15),
        0 4px 0 var(--tile-depth-color),
        0 6px 12px rgba(0, 0, 0, 0.25);
}
```

---

## 2. Vibrant Spiritual Color Gradients

Each quality and flower will be assigned a **vibrant spiritual color gradient** that defines its medallion background and its corresponding 3D depth border:

| Theme / Quality | Color Hex | CSS Gradient (`--tile-bg`) | 3D Depth (`--tile-depth-color`) |
| :--- | :--- | :--- | :--- |
| **Sincerity** (Vibrant Blue) | `#00b0ff` | `linear-gradient(135deg, #e1f5fe 0%, #80d8ff 100%)` | `#00b0ff` |
| **Aspiration** (Deep Orange) | `#ff6d00` | `linear-gradient(135deg, #ffe0b2 0%, #ffb74d 100%)` | `#ff6d00` |
| **Gratitude** (Spiritual Green) | `#00e676` | `linear-gradient(135deg, #e8f5e9 0%, #a7ffeb 100%)` | `#00e676` |
| **Perseverance** (Gold/Yellow) | `#ffd600` | `linear-gradient(135deg, #fffde7 0%, #ffe082 100%)` | `#ffd600` |
| **Courage** (Spiritual Red) | `#ff1744` | `linear-gradient(135deg, #ffebee 0%, #ff8a80 100%)` | `#ff1744` |
| **Peace** (Pure White/Teal) | `#00e5ff` | `linear-gradient(135deg, #ffffff 0%, #e0f7fa 100%)` | `#00e5ff` |

---

## 3. Glowing Spiritual Aura Effect

To visualize the "vibration" or "consciousness level" of unblocked tiles, we will add a **glowing background aura** using CSS drop-filters:

```css
/* Glowing background aura representing the tile's quality energy */
.tile-3d.glowing-aura {
    filter: drop-shadow(0 0 8px var(--tile-glow-color));
    animation: gentleGlow 3s infinite ease-in-out;
}

@keyframes gentleGlow {
    0%, 100% { filter: drop-shadow(0 0 6px var(--tile-glow-color)); }
    50% { filter: drop-shadow(0 0 14px var(--tile-glow-color)); }
}

/* Blocked tiles turn gray, silent, and have their aura turned off */
.tile-3d.blocked {
    filter: grayscale(100%) brightness(0.65) contrast(0.95);
    box-shadow: 
        0 2px 3px rgba(0, 0, 0, 0.1),
        0 4px 0 #5a5a5a;
}
```

---

## 4. Visual Layout Shifts (Prahar Clock)

The background of the application changes dynamically matching the time-of-day:
* **Dawn (04:00 - 08:00):** Soft rose pink and golden rays.
* **Noon (08:00 - 16:00):** Deep forest green and golden sunlight.
* **Evening (16:00 - 20:00):** Rich sand saffron and dusty copper twilight.
* **Night (20:00 - 04:00):** Dark jade greens and deep midnight teals.

---

## 5. Unique Visual Mappings for the 15 Gardens

Each of the 15 thematic sanctuaries features its own dedicated visual assets, color gradients, tile sets, and audio alignments:

| Sanctuary Garden | Visual Style Concept | Active Tile Set | Dedicated Background Color Gradient | Music / Ambient Drone Mode |
| :--- | :--- | :--- | :--- | :--- |
| **1. Samadhi Courtyard** | Circular Mandala | Watercolor Flowers | Soft cream, pale rose, and gold | Meditative, low flute chords |
| **2. Ashram Playground** | Circular Mandala | 12 Virtues/Qualities | Vital orange, gold, and white | Uplifting, rhythmic sitar drone |
| **3. Matrimandir Chamber** | Golden Glass Stack | Sanskrit Seed Words | Golden ray, white light shafts | Deep, resonant C3 fundamental gong |
| **4. Lake Estate** | Wood & Brass Altar | Indian Instruments | Soft lake reflection teal and bronze | Active layering of sitar/veena loops |
| **5. Service Tree** | Circular Mandala | Watercolor Flowers | Deep leaf green and golden highlights | Soft, continuous backing Tanpura |
| **6. Banyan Tree** | Circular Mandala | 12 Virtues/Qualities | Organic woodland sage and gold | Natural wind-rustle ambient chime |
| **7. Promenade Coastline** | Golden Glass Stack | Sanskrit Seed Words | Sea-twilight indigo and orange | Deep ocean-wash bass drone |
| **8. SABDA / Library** | Wood & Brass Altar | Watercolor Flowers | Dark mahogany and parchment gold | Steady, calming harmonium drone |
| **9. Golconde Dormitory** | Wood & Brass Altar | 12 Virtues/Qualities | Modernist gray, concrete, and bronze | Pure silence with periodic gong bells |
| **10. Ashram Archives** | Wood & Brass Altar | Sanskrit Seed Words | Antique papyrus brown and bronze | Solemn, deep quietude chants |
| **11. Matrimandir Petals** | Golden Glass Stack | Watercolor Flowers | Radiant petal yellow and white | Multi-frequency acoustic gongs |
| **12. Auroville Green Belt** | Circular Mandala | 12 Virtues/Qualities | Forest green and wilderness sage | Active bird-chirp atmospheric chimes |
| **13. Classroom (SAICE/SAS)** | Wood & Brass Altar | Watercolor Flowers | Bright chalk blue and school desk wood | Joyful, light, pentatonic bells |
| **14. Botanical Garden** | Circular Mandala | Watercolor Flowers | Tropical jade green and orchid pink | Floral breeze wind-harp resonance |
| **15. Dining Hall** | Wood & Brass Altar | 12 Virtues/Qualities | Copper pot orange and warm wood | Grounded, steady hand-drum table base |

