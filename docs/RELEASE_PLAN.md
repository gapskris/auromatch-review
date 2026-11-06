# Release & Distribution Plan: AuroMatch

---

## 1. App Store & Market Metadata

* **App Title:** AuroMatch: Floral Sanctuary
* **Subtitle (iOS):** Zen Mahjong & Tile Match
* **Short Description (Google Play - 80 chars max):**
  * *"Relax with sacred flowers. Ad-free Mahjong and 3D tile matching for all ages."*
* **Full Description:**
  > Welcome to **AuroMatch**, a serene botanical sanctuary uniting the classic clarity of Mahjong solitaire with modern 3D tile matching.
  >
  > Immerse yourself in 15 tranquil botanical gardens, discovering the quiet wisdom of sacred flowers through stress-free, ad-free play.
  >
  > **Key Features:**
  > • **Two Meditative Modes:** Choose between classic Vita Mahjong (pair matching) and Tile Club (3-tile holding tray).
  > • **Senior-First Accessibility:** Massive high-contrast tiles, special [Aa] Senior View mode, and zero startle noises.
  > • **Prahar Solar Harmonics:** Experience soothing procedural Indian raga drones and bronze temple chimes calibrated to the time of day.
  > • **Guaranteed Solvable:** Reverse-constructed boards ensure every puzzle has a clean, natural solution path.
  > • **100% Free & Ad-Free:** Zero video ads, zero energy limits, zero data tracking.
* **Keywords (iOS - 100 chars):**
  `mahjong,tile match,zen,botany,flowers,senior puzzle,vita mahjong,tile club,relax,ad-free`

---

## 2. PWA Manifest (`manifest.json`)

```json
{
  "name": "AuroMatch: Floral Sanctuary",
  "short_name": "AuroMatch",
  "start_url": "./index.html",
  "display": "standalone",
  "background_color": "#12181B",
  "theme_color": "#D4AF37",
  "orientation": "portrait",
  "icons": [
    {
      "src": "./assets/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "./assets/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```
