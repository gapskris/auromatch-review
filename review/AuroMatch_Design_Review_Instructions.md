# AuroMatch — Design Review Instructions
### Companion to the Implementation Review — run in Claude Code

**This is a different kind of review from the implementation one.** That review verifies logic by executing code. This one verifies experience by looking at what actually renders — the garden map, the tile stack, the wisdom card, the jar, the sky of stars — the screens a seeker or a child actually sees. A component that reads correctly in the source can still look, feel, or land wrong on screen. Don't infer the visual outcome from the CSS; observe it.

**How to observe it:** run the app (dev server or deployed build) and walk through it — screenshot every screen/state named below, either via browser automation if the session has it, or by asking Gopal ji to supply screenshots if it doesn't. Describe what's genuinely on screen, not what the component *should* produce. Where you can't observe a state directly, say so.

Paste findings back screen by screen, in plain text, in the message body.

---

## 1. First Impression & Onboarding (Welcome Screen)
- What does a first-time user see in the first 30–60 seconds?
- Screenshot the Onboarding Path Selector — three cards (Traditional/Sadhana, Secular/Mindfulness, Youth/Starlight). Are all three legible, and does the framing feel inviting rather than clinical?
- Does the app feel like a sanctuary from the first screen, or could the same shell hold any generic matching game?
- Does the drifting stardust particle background actually render, and at a restful pace (not distracting)?

## 2. Garden Selection Screen — critical, check this first
The specs disagree on whether there are 4 gardens or 15 (see Implementation Review Section 1 for the full contradiction). **Screenshot the actual selection screen and count what's rendered.** Report the exact number and names shown, regardless of what any document claims. This single screenshot resolves an open question that affects the rest of this review.

## 3. The Matching Board (Core Interaction)
- Touch target size and tile legibility on a small viewport (320px).
- Is the 3D stacking / occlusion effect visually legible — can a player tell which tiles are blocked without being told?
- Screenshot a blocked tile next to an unblocked one; confirm the `brightness(0.65) contrast(0.95)` desaturation is visually distinct, not subtle to the point of confusion.
- Watch the tile-selection slide into the tray — does it match the spec's 0.25s `cubic-bezier(0.25, 1, 0.5, 1)` easing, i.e. does it feel quick and settled, not floaty or abrupt?
- Play the same garden level twice — does difficulty feel consistent?

## 4. Wisdom Card / Match Reflection Overlay
- Screenshot the exact moment a triple match completes and the card appears. Is there a beat to actually read the quote, or does the UI rush toward "continue"?
- Confirm *Playfair Display* is actually rendering for the quote text (not a fallback serif) — check computed font-family in devtools if visual inspection is ambiguous.
- Test the "Listen" control. Does slow narration (rate 0.70) actually sound meditative, or does it read as broken/robotic at that speed?
- Try to reach the French-accented / "devotee" voice option through the actual UI. Given the naming bug flagged in the Implementation Review, confirm whether this setting is reachable at all, and if so, through which control.

## 5. Content Accuracy Spot-Check — ties directly to the highest-priority finding
Pick 5 of the 12 Qualities and 5 flowers as they actually render in-app (color, hex, and significance text shown on screen). Compare against **both** `auromatch_15_themes_and_visual_designs.md` and `AuroMatch_Detailed_Concepts_and_Specs.md`, which disagree with each other on several of these (e.g. Humility's color, Progress's color, Marigold's and Periwinkle's significance). Report which source — if either — the shipped content matches. Do not treat either document as ground truth; the point of this check is to find out what's actually live, so it can be verified against the real SABDA source afterward.

## 6. Consecration Jar (Evening Journal)
- Screenshot the jar screen. Does the placeholder text read as intended: *"What vital storm, worry, or friction would you like to consecrate today?"*
- Type a short entry and submit. Watch the dissolution animation — does it feel like a gentle surrender (per spec: gold particles, ~1.2s decay, drifting toward the jar), or does it read as a generic particle effect disconnected from the text?
- Confirm no visual or console evidence of the entry leaving the device (no network calls fired on submit).

## 7. Constellation Grid (Star Calendar)
- Screenshot the monthly grid with at least one logged day. Confirm the pulse animation (`scale 1.0 → 1.15` every 2.5s) is visible and calm, not jittery.
- Screenshot an Ashram-event day (mock one of the 5 milestone dates) — confirm the golden `.event-halo` ring renders and the detail bottom-sheet opens correctly.
- If a full month of entries can be simulated, confirm the symbol-constellation path-drawing actually traces a recognizable shape rather than a random scatter of lines.

## 8. Daily Aspiration (Morning Oracle)
- Screenshot the velvet bag draw interaction. Does the single-draw-per-day restriction feel respected in the UI, or does it look drawable multiple times?

## 9. Settings & Onboarding Path Behavior
- Switch between Traditional / Secular / Youth in Settings. Confirm each actually changes what the spec says it should: text headers (spiritual vs. psychological terms), and for Youth, the SVG lotus/spark visuals.
- Confirm the Secular toggle changes headers but leaves quote bodies verbatim, per spec — this is a content-integrity requirement, not just a cosmetic one.

## 10. Design Tokens vs. Shipped Reality
Check the rendered app against the UI Design Document's exact tokens, not impressionistically:
- **Evening palette:** board gradient `#0e4e37 → #041812`, Spiritual Gold `#c5a880`, Creamy Tile `#fcf9f2`, Glass Overlay `rgba(4,24,18,0.75)`, Glass Border `rgba(255,255,255,0.12)`.
- **Morning palette** (from the technical Bible, not in the original UI doc — confirm it's actually implemented): background `linear-gradient(135deg, #fdfcf7, #f7f3e3)`, text `#27272a`, accent `#d97706`.
- **Typography:** Playfair Display for headers/reflections, Outfit for UI controls — confirm both load, not fallback fonts.
- **Z-index layering:** base canvas (1) → tiles layers 0–3 (10/20/30/40) → tray (50) → reflection overlays (100). Confirm overlays never render beneath tiles or the tray.
- **Theme transition:** 2s ease on background/color/border-color when morning/evening shifts — confirm it's a smooth cross-fade, not an abrupt cut.

## 11. Darshan Day Greetings
Mock the system date to each of the 5 milestone dates (Feb-21, Apr-24, Aug-15, Nov-24, Dec-05) and confirm the gold-bordered greeting card and quote actually appear on launch for each one.
