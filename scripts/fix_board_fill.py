#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_board_fill.py  --  Implements all 5 root-cause fixes for tile fill issue.

RC1/RC2: .tile-layout max-width:980px not overridden in desktop media query
RC3:     board-container height calc wrong / min-height:400px floor too high
RC4:     containerW/H JS fallbacks too conservative in boardRenderer.js render()
RC5:     maxWFromHeight traps rawFitW because containerH underreported
rAF:     setTiles() defers render so CSS paints before JS measures clientWidth
"""

import sys
import pathlib

ROOT = pathlib.Path(r"c:\DataScience\AuroProject_Annalysis\AuroMatch")
CSS  = ROOT / "styles" / "main.css"
BR   = ROOT / "src" / "ui" / "boardRenderer.js"

def apply(src, old, new, label, lf_ok=True):
    if old in src:
        print(f"[PATCH] {label}")
        return src.replace(old, new, 1)
    if lf_ok:
        src_lf  = src.replace("\r\n", "\n")
        old_lf  = old.replace("\r\n", "\n")
        new_lf  = new.replace("\r\n", "\n")
        if old_lf in src_lf:
            print(f"[PATCH-LF] {label}")
            return src_lf.replace(old_lf, new_lf, 1).replace("\n", "\r\n")
    print(f"[FAIL] Could not locate target for: {label}")
    print("       First 120 chars of OLD:")
    print("      ", repr(old[:120]))
    sys.exit(1)

# ===========================================================================
# 1. CSS FIXES
# ===========================================================================
css = CSS.read_text(encoding="utf-8")

# RC2+RC3: Replace .board-container block and append .tile-layout override
OLD_BC = """\
    /* Board fills the full stage \u2014 no width cap, no height cap */
    .board-container {
        width: 100% !important;
        max-width: 100% !important;
        flex: 1 !important;
        height: calc(100vh - 116px) !important;
        min-height: 400px !important;
        max-height: none !important;
        position: relative !important;
        overflow: visible !important;
        border-radius: 0 !important;
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
    }"""

NEW_BC = """\
    /* Board fills the full stage \u2014 no width cap, no height cap */
    .board-container {
        width: 100% !important;
        max-width: 100% !important;
        flex: 1 1 0 !important;
        /* RC3: use --app-height set by JS viewport updater; subtract header+modebar */
        height: calc(var(--app-height, 100vh) - 104px) !important;
        min-height: 0 !important;
        max-height: none !important;
        position: relative !important;
        overflow: visible !important;
        border-radius: 0 !important;
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
        padding: 0 !important;
    }

    /* RC2: #board (.tile-layout) must inherit full parent size.
       The global rule has max-width:980px and min-height:520px -- kill them on desktop. */
    .game-desktop-grid .tile-layout {
        width: 100% !important;
        max-width: none !important;
        height: 100% !important;
        min-height: 0 !important;
        position: relative !important;
        display: block !important;
    }"""

css = apply(css, OLD_BC, NEW_BC, "CSS board-container + tile-layout override")
CSS.write_text(css, encoding="utf-8")
print("[OK] CSS written.")

# ===========================================================================
# 2. boardRenderer.js FIXES
# ===========================================================================
br = BR.read_text(encoding="utf-8")

# RC1+RC4: fix containerW / containerH measurement
OLD_WH = """\
    const containerW = (this.container && this.container.clientWidth > 100)
      ? this.container.clientWidth
      : (typeof window !== 'undefined' && window.innerWidth < 768 ? window.innerWidth - 24 : null);

    const containerH = (this.container && this.container.clientHeight > 100)
      ? this.container.clientHeight
      : (typeof window !== 'undefined' && window.innerHeight ? Math.floor(window.innerHeight * 0.65) : 560);"""

NEW_WH = """\
    // RC1+RC4 fix: measure the PARENT .board-container (not #board which has max-width:980px).
    // Fall back to window dimensions so desktop never returns null/tiny values.
    const _boardParent = this.container ? this.container.parentElement : null;
    const _rawW = (_boardParent && _boardParent.clientWidth > 120)
      ? _boardParent.clientWidth
      : (this.container && this.container.clientWidth > 120 ? this.container.clientWidth : 0);
    const containerW = _rawW > 120
      ? _rawW
      : (typeof window !== 'undefined' ? window.innerWidth : 1280);

    // RC3 fix: measure parent height (board-container has the correct calc height).
    // Fall back to 82% of viewport so height aspect never crushes rawFitW.
    const _rawH = (_boardParent && _boardParent.clientHeight > 200)
      ? _boardParent.clientHeight
      : (this.container && this.container.clientHeight > 200 ? this.container.clientHeight : 0);
    const containerH = _rawH > 200
      ? _rawH
      : (typeof window !== 'undefined' ? Math.floor(window.innerHeight * 0.82) : 700);"""

br = apply(br, OLD_WH, NEW_WH, "boardRenderer containerW/H measurement")

# rAF defer fix: setTiles() defers render so CSS has painted before JS measures
OLD_SET = """\
  setTiles(tiles) {
    this.tiles = tiles || [];
    this.stageLayoutMetrics = null;
    this.render();
  }"""

NEW_SET = """\
  setTiles(tiles) {
    this.tiles = tiles || [];
    this.stageLayoutMetrics = null;
    // rAF defer: let CSS finish painting so clientWidth/clientHeight are real values
    if (typeof requestAnimationFrame !== 'undefined') {
      requestAnimationFrame(() => { this.render(); });
    } else {
      this.render();
    }
  }"""

br = apply(br, OLD_SET, NEW_SET, "boardRenderer setTiles() rAF defer")

BR.write_text(br, encoding="utf-8")
print("[OK] boardRenderer.js written.")
print("")
print("All 5 root-cause fixes applied successfully.")
print("Run: npm test  &&  python scripts/build_prototype.py  &&  python scripts/deploy_live.py")
