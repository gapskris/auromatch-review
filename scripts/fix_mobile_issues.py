#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_mobile_issues.py  --  Implements all 6 mobile root-cause fixes:

RC-A: drawer-toggle/backdrop not hidden on mobile -> 90px stolen from board
RC-B: board-container min-height:480px overestimates containerH on mobile
RC-C: offsetY centering pushes tiles into lower half on mobile
RC-D: Tile Club maxAllowed 70px vs 80px creates visible size difference
RC-E: Realms aspect 1.125 vs 1.294 -> squarer tiles look smaller
RC-F: rawFitW varies by colSpan/rowSpan per mode -> non-uniform fill
"""
import sys, pathlib

ROOT = pathlib.Path(r"c:\DataScience\AuroProject_Annalysis\AuroMatch")
CSS  = ROOT / "styles" / "main.css"
BR   = ROOT / "src" / "ui" / "boardRenderer.js"

def patch(src, old, new, label):
    if old in src:
        print(f"[PATCH]    {label}")
        return src.replace(old, new, 1)
    # normalise CRLF -> LF and retry
    s, o, n = src.replace("\r\n","\n"), old.replace("\r\n","\n"), new.replace("\r\n","\n")
    if o in s:
        print(f"[PATCH-LF] {label}")
        return s.replace(o, n, 1).replace("\n", "\r\n")
    print(f"[FAIL]     {label}")
    print("           TARGET (first 160 chars):", repr(old[:160]))
    sys.exit(1)

# ---------------------------------------------------------------------------
# 1. CSS  -- two changes
# ---------------------------------------------------------------------------
css = CSS.read_text(encoding="utf-8")

# RC-A: hide drawer UI elements on mobile
OLD_MOBILE = """\
/* Mobile Viewport (< 1024px): Standard Single-Column Frame */
@media (max-width: 1023px) {
    #field-guide-col, #status-prahar-col {
        display: none !important;
    }
    .game-desktop-grid {
        display: flex;
        flex-direction: column;
        height: 100%;
        width: 100%;
    }
    #center-stage-col {
        flex: 1;
        display: flex;
        flex-direction: column;
        height: 100%;
    }
}"""

NEW_MOBILE = """\
/* Mobile Viewport (< 1024px): Standard Single-Column Frame */
@media (max-width: 1023px) {
    #field-guide-col, #status-prahar-col {
        display: none !important;
    }

    /* RC-A fix: drawer buttons / backdrop exist in HTML but must be invisible on mobile.
       Without this they render as full-width white blocks stealing ~90px of vertical space. */
    .drawer-toggle-left,
    .drawer-toggle-right,
    .drawer-backdrop,
    .drawer-close-btn {
        display: none !important;
    }

    .game-desktop-grid {
        display: flex;
        flex-direction: column;
        height: 100%;
        width: 100%;
    }
    #center-stage-col {
        flex: 1;
        display: flex;
        flex-direction: column;
        height: 100%;
    }

    /* RC-B fix: remove the min-height:480px floor from the base .board-container rule
       on mobile so JS reads the real rendered height, not the CSS minimum. */
    .board-container {
        min-height: 0 !important;
        padding: 4px 0 6px 0 !important;
    }
}"""

css = patch(css, OLD_MOBILE, NEW_MOBILE, "CSS mobile block: hide drawer elements + remove board-container min-height")
CSS.write_text(css, encoding="utf-8")
print("[OK] CSS written.")

# ---------------------------------------------------------------------------
# 2. boardRenderer.js  -- three changes
# ---------------------------------------------------------------------------
br = BR.read_text(encoding="utf-8")

# RC-C fix: cap offsetY on mobile so tiles don't sink to the lower half.
# After RC-A+B are fixed, containerH will be accurate. But as a safety net,
# cap the top padding to 12% of containerH on mobile so tiles always start near top.
OLD_OFFSET = """\
    // Centering offsets
    let offsetX = 10;
    if (containerW && containerW > boardTotalW) {
      offsetX = Math.max(10, Math.floor((containerW - boardTotalW) / 2));
    }
    let offsetY = 12;
    if (containerH && containerH > boardTotalH) {
      const usableH = isTileClubMode ? Math.max(boardTotalH + 10, containerH - 95) : containerH;
      offsetY = Math.max(8, Math.floor((usableH - boardTotalH) / 2));
    }
    const maxBottom = isTileClubMode ? (containerH - 95) : (containerH - 12);
    if (offsetY + boardTotalH > maxBottom) {
      offsetY = Math.max(6, maxBottom - boardTotalH);
    }"""

NEW_OFFSET = """\
    // Centering offsets
    let offsetX = 10;
    if (containerW && containerW > boardTotalW) {
      offsetX = Math.max(10, Math.floor((containerW - boardTotalW) / 2));
    }
    let offsetY = 12;
    if (containerH && containerH > boardTotalH) {
      const usableH = isTileClubMode ? Math.max(boardTotalH + 10, containerH - 95) : containerH;
      offsetY = Math.max(8, Math.floor((usableH - boardTotalH) / 2));
    }
    const maxBottom = isTileClubMode ? (containerH - 95) : (containerH - 12);
    if (offsetY + boardTotalH > maxBottom) {
      offsetY = Math.max(6, maxBottom - boardTotalH);
    }

    // RC-C fix: on mobile, cap top padding so tiles never sink into the lower half.
    // Centering formula amplifies any containerH overestimation on small screens.
    // Clamp to 12% of containerH (e.g. max ~60px on a 500px board area).
    if (isMobile) {
      offsetY = Math.max(8, Math.min(offsetY, Math.floor(containerH * 0.12)));
    }"""

br = patch(br, OLD_OFFSET, NEW_OFFSET, "boardRenderer offsetY mobile cap (RC-C)")

# RC-D+E fix: unify maxAllowed on mobile across modes.
# - Tile Club: raise cap from 70 -> 76 (tray deduction already handles space)
# - Realms: separate cap of 86px to compensate for squarer aspect (1.125)
#   so the visual tile footprint is more comparable to Pairs/Classic tiles
OLD_CAPS = """\
    if (isMobile) {
      // Mobile Viewport (< 480px): Expand to fill 90%-94% screen width (~64px-74px)
      minAllowed = isSenior ? 50 : 44;
      maxAllowed = isSenior ? 88 : (isTileClubMode ? 70 : 80);
    } else if (isTablet) {"""

NEW_CAPS = """\
    if (isMobile) {
      // Mobile Viewport (< 480px): Expand to fill 90%-94% screen width
      // RC-D fix: raise Tile Club cap 70->76 (tray deduction in availH already limits size)
      // RC-E fix: Realms gets separate cap 86px to offset squarer aspect ratio (1.125 vs 1.294)
      minAllowed = isSenior ? 50 : 44;
      maxAllowed = isSenior ? 92
        : (isTileClubMode ? 76
        : (isRealmsMode  ? 86
        : 80));
    } else if (isTablet) {"""

br = patch(br, OLD_CAPS, NEW_CAPS, "boardRenderer mobile maxAllowed unification (RC-D+E)")

# RC-F fix: on mobile, rawFitW is constrained by colSpan/rowSpan of each level.
# For modes with fewer columns (Tile Club 5-col vs Pairs 7-col), rawFitW naturally
# ends up larger. We can't normalize geometry across modes without changing layouts,
# but we can remove the artificial 0.94 width cap and let rawFitW use 98% of availW
# on mobile so at least the width dimension is maxed out.
OLD_RAW = """\
    // Target 90% - 94% coverage of the container
    const maxWFromWidth = (availW * 0.94) / colDenominator;
    const maxHFromHeight = (availH * 0.91) / rowDenominator;"""

NEW_RAW = """\
    // Target coverage: 98% of width on mobile (tiny screens need every pixel),
    // 94% on tablet/desktop for aesthetic breathing room.
    // RC-F fix: mobile gets 98% so rawFitW from width dimension is maximised.
    const widthCoverage = isMobile ? 0.98 : 0.94;
    const heightCoverage = isMobile ? 0.94 : 0.91;
    const maxWFromWidth = (availW * widthCoverage) / colDenominator;
    const maxHFromHeight = (availH * heightCoverage) / rowDenominator;"""

br = patch(br, OLD_RAW, NEW_RAW, "boardRenderer coverage factors: 98% width on mobile (RC-F)")

BR.write_text(br, encoding="utf-8")
print("[OK] boardRenderer.js written.")
print("")
print("All 6 mobile root-cause fixes applied.")
