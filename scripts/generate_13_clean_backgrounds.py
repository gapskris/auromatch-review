"""
Generate 13 Clean Thematic Environmental Backgrounds for AuroMatch 13 Realms Campaign.
Zero text prints (no "Score", "Moves", "Goal"), zero pre-rendered tiles.
Provides atmospheric 1600x1000 tactile tabletop/altar environments for each theme.
"""

import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

OUT_DIR = "Assets/backgrounds"
os.makedirs(OUT_DIR, exist_ok=True)
W, H = 1600, 1000

def create_base_gradient(w, h, top_color, bottom_color, radial_center=None, radial_color=None, radial_radius=600):
    """Creates a base atmospheric gradient with optional radial warm spotlight."""
    img = Image.new("RGBA", (w, h))
    
    # Vertical gradient
    base = np.zeros((h, w, 4), dtype=np.float32)
    for y in range(h):
        t = y / (h - 1)
        r = top_color[0] * (1 - t) + bottom_color[0] * t
        g = top_color[1] * (1 - t) + bottom_color[1] * t
        b = top_color[2] * (1 - t) + bottom_color[2] * t
        base[y, :, 0] = r
        base[y, :, 1] = g
        base[y, :, 2] = b
        base[y, :, 3] = 255.0

    if radial_center and radial_color:
        cx, cy = radial_center
        y_coords, x_coords = np.ogrid[:h, :w]
        dist = np.sqrt((x_coords - cx) ** 2 + (y_coords - cy) ** 2)
        factor = np.clip(1.0 - (dist / radial_radius), 0.0, 1.0)
        # Smooth hermite interpolation
        factor = factor * factor * (3.0 - 2.0 * factor)
        
        for c in range(3):
            base[:, :, c] = base[:, :, c] * (1.0 - factor * 0.45) + radial_color[c] * (factor * 0.45)

    base = np.clip(base, 0, 255).astype(np.uint8)
    return Image.fromarray(base, mode="RGBA")

def add_vignette(img, intensity=0.75):
    """Applies a smooth elliptical photographic vignette to focus the center board."""
    w, h = img.size
    y_coords, x_coords = np.ogrid[:h, :w]
    cx, cy = w / 2.0, h / 2.0
    # Normalized radial distance
    nx = (x_coords - cx) / (w * 0.55)
    ny = (y_coords - cy) / (h * 0.55)
    dist = np.sqrt(nx ** 2 + ny ** 2)
    vignette = np.clip(1.0 - (dist - 0.4) * intensity, 0.15, 1.0)
    
    arr = np.array(img).astype(np.float32)
    for c in range(3):
        arr[:, :, c] *= vignette
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), mode="RGBA")

def add_table_frame(img, border_color, fill_color, border_width=4, pad_x=120, pad_y=80, corner_radius=28):
    """Draws an elegant, soft-beveled playing altar surface inside the environment."""
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    box = [pad_x, pad_y, img.size[0] - pad_x, img.size[1] - pad_y]
    
    # Outer soft drop shadow
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([box[0]-12, box[1]-8, box[2]+12, box[3]+16], radius=corner_radius+8, fill=(0, 0, 0, 160))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    
    img = Image.alpha_composite(img, shadow)
    
    # Tabletop slab
    draw.rounded_rectangle(box, radius=corner_radius, fill=fill_color, outline=border_color, width=border_width)
    
    # Inner bevel highlight
    inner_box = [box[0]+border_width, box[1]+border_width, box[2]-border_width, box[3]-border_width]
    draw.rounded_rectangle(inner_box, radius=max(4, corner_radius-border_width), outline=(255, 255, 255, 28), width=1)
    
    return Image.alpha_composite(img, overlay)

def add_surface_noise(img, noise_level=12, grain_scale=1):
    """Adds subtle organic material grain to avoid digital flatness."""
    w, h = img.size
    noise = np.random.normal(0, noise_level, (h, w)).astype(np.float32)
    arr = np.array(img).astype(np.float32)
    for c in range(3):
        arr[:, :, c] = np.clip(arr[:, :, c] + noise, 0, 255)
    return Image.fromarray(arr.astype(np.uint8), mode="RGBA")

# ==============================================================================
# Theme-Specific Background Generators
# ==============================================================================

def make_whispering_pines():
    # Deep mossy pine forest altar: cedarwood, emerald shadows, dappled morning light
    img = create_base_gradient(W, H, (12, 28, 18), (6, 14, 10), radial_center=(800, 480), radial_color=(36, 75, 48), radial_radius=700)
    img = add_surface_noise(img, 14)
    img = add_table_frame(img, border_color=(42, 80, 52, 220), fill_color=(18, 38, 26, 195), border_width=3, pad_x=140, pad_y=90)
    return add_vignette(img, 0.8)

def make_temple_of_lines():
    # Blueprint architectural slate & zen monastery geometry
    img = create_base_gradient(W, H, (20, 26, 34), (10, 14, 20), radial_center=(800, 500), radial_color=(45, 60, 80), radial_radius=750)
    # Subtle blueprint grid overlay
    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(grid)
    for x in range(160, W - 160, 48):
        gdraw.line([(x, 110), (x, H - 110)], fill=(80, 120, 160, 18), width=1)
    for y in range(110, H - 110, 48):
        gdraw.line([(160, y), (W - 160, y)], fill=(80, 120, 160, 18), width=1)
    img = Image.alpha_composite(img, grid)
    img = add_surface_noise(img, 12)
    img = add_table_frame(img, border_color=(70, 95, 125, 230), fill_color=(22, 30, 40, 210), border_width=3, pad_x=140, pad_y=90)
    return add_vignette(img, 0.75)

def make_biblios_wisdom():
    # Warm mahogany scholar's reading table, candle ambient glow, vintage bookbindery
    img = create_base_gradient(W, H, (35, 18, 12), (18, 8, 6), radial_center=(800, 480), radial_color=(115, 65, 30), radial_radius=650)
    img = add_surface_noise(img, 15)
    img = add_table_frame(img, border_color=(180, 125, 65, 210), fill_color=(42, 22, 14, 205), border_width=4, pad_x=140, pad_y=90)
    return add_vignette(img, 0.85)

def make_celestial_starlight():
    # Aquamarine observatory & celestial midnight crystal
    img = create_base_gradient(W, H, (10, 18, 38), (4, 8, 18), radial_center=(800, 480), radial_color=(25, 75, 110), radial_radius=700)
    # Starlight speckles
    stars = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(stars)
    np.random.seed(42)
    for _ in range(180):
        sx, sy = np.random.randint(40, W-40), np.random.randint(30, H-30)
        sr = np.random.uniform(0.8, 2.4)
        alpha = np.random.randint(70, 220)
        sdraw.ellipse([sx-sr, sy-sr, sx+sr, sy+sr], fill=(210, 235, 255, alpha))
    img = Image.alpha_composite(img, stars)
    img = add_table_frame(img, border_color=(100, 190, 235, 210), fill_color=(14, 28, 52, 200), border_width=3, pad_x=140, pad_y=90)
    return add_vignette(img, 0.8)

def make_golden_nebula():
    # Obsidian mirror & radiant gold stardust aurora
    img = create_base_gradient(W, H, (18, 14, 6), (8, 6, 4), radial_center=(800, 480), radial_color=(90, 68, 18), radial_radius=700)
    # Gold cosmic dust
    gold_dust = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(gold_dust)
    np.random.seed(108)
    for _ in range(140):
        gx, gy = np.random.randint(50, W-50), np.random.randint(40, H-40)
        gr = np.random.uniform(1.0, 3.2)
        alpha = np.random.randint(80, 240)
        gdraw.ellipse([gx-gr, gy-gr, gx+gr, gy+gr], fill=(255, 215, 90, alpha))
    gold_dust = gold_dust.filter(ImageFilter.GaussianBlur(1.2))
    img = Image.alpha_composite(img, gold_dust)
    img = add_table_frame(img, border_color=(235, 185, 75, 230), fill_color=(24, 18, 12, 215), border_width=3, pad_x=140, pad_y=90)
    return add_vignette(img, 0.82)

def make_spirit_altar():
    # Teak altar with Carrara marble surface and soft candlelight warmth
    img = create_base_gradient(W, H, (28, 22, 18), (14, 10, 8), radial_center=(800, 480), radial_color=(85, 65, 45), radial_radius=680)
    img = add_surface_noise(img, 12)
    # Carrara marble slab inlay
    img = add_table_frame(img, border_color=(195, 170, 135, 220), fill_color=(36, 30, 26, 215), border_width=4, pad_x=140, pad_y=90)
    return add_vignette(img, 0.82)

def make_sacred_sanctuary():
    # Saffron amber temple altar with antique brass and incense mist
    img = create_base_gradient(W, H, (32, 22, 10), (16, 10, 4), radial_center=(800, 480), radial_color=(105, 75, 25), radial_radius=700)
    img = add_surface_noise(img, 14)
    img = add_table_frame(img, border_color=(220, 165, 55, 220), fill_color=(38, 26, 14, 210), border_width=4, pad_x=140, pad_y=90)
    return add_vignette(img, 0.85)

def make_ocean_horizon():
    # Tumbled sea-glass & sun-bleached coastal driftwood
    img = create_base_gradient(W, H, (14, 32, 42), (8, 18, 24), radial_center=(800, 460), radial_color=(30, 85, 105), radial_radius=720)
    img = add_surface_noise(img, 13)
    img = add_table_frame(img, border_color=(75, 170, 195, 210), fill_color=(18, 38, 48, 205), border_width=3, pad_x=140, pad_y=90)
    return add_vignette(img, 0.78)

def make_terracotta_earth():
    # Sun-baked Mediterranean red earth and pottery clay
    img = create_base_gradient(W, H, (42, 24, 16), (20, 10, 6), radial_center=(800, 480), radial_color=(120, 65, 38), radial_radius=680)
    img = add_surface_noise(img, 16)
    img = add_table_frame(img, border_color=(195, 105, 65, 220), fill_color=(46, 26, 18, 210), border_width=4, pad_x=140, pad_y=90)
    return add_vignette(img, 0.82)

def make_floral_harmony():
    # Rose quartz stone table with soft blush morning ambiance
    img = create_base_gradient(W, H, (36, 20, 26), (18, 8, 12), radial_center=(800, 480), radial_color=(95, 52, 68), radial_radius=700)
    img = add_surface_noise(img, 13)
    img = add_table_frame(img, border_color=(215, 135, 160, 210), fill_color=(40, 22, 28, 205), border_width=3, pad_x=140, pad_y=90)
    return add_vignette(img, 0.8)

def make_blooming_mandala():
    # Porcelain white and gold wire concentric geometry
    img = create_base_gradient(W, H, (30, 26, 22), (14, 12, 10), radial_center=(800, 480), radial_color=(85, 74, 58), radial_radius=700)
    img = add_surface_noise(img, 12)
    # Subtle concentric mandala watermark in center
    manda = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(manda)
    cx, cy = W // 2, H // 2
    for r in [90, 160, 230, 300, 380]:
        mdraw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(235, 195, 120, 22), width=1)
    img = Image.alpha_composite(img, manda)
    img = add_table_frame(img, border_color=(220, 180, 110, 215), fill_color=(32, 28, 24, 210), border_width=3, pad_x=140, pad_y=90)
    return add_vignette(img, 0.82)

def make_sacred_spiral():
    # Deep botanical emerald and golden vine spiral curves
    img = create_base_gradient(W, H, (16, 30, 22), (8, 16, 12), radial_center=(800, 480), radial_color=(42, 82, 58), radial_radius=700)
    img = add_surface_noise(img, 14)
    img = add_table_frame(img, border_color=(165, 195, 95, 215), fill_color=(20, 38, 28, 205), border_width=3, pad_x=140, pad_y=90)
    return add_vignette(img, 0.8)

def make_master_sanctuary():
    # Carved royal walnut and polished brass master table
    img = create_base_gradient(W, H, (26, 20, 16), (12, 8, 6), radial_center=(800, 480), radial_color=(85, 60, 40), radial_radius=700)
    img = add_surface_noise(img, 14)
    img = add_table_frame(img, border_color=(210, 160, 85, 230), fill_color=(34, 24, 18, 215), border_width=4, pad_x=140, pad_y=90)
    return add_vignette(img, 0.85)

def make_lotus_pond():
    # Sunlit Lotus Pond: serene emerald-teal water altar with golden rim
    img = create_base_gradient(W, H, (14, 38, 36), (6, 18, 16), radial_center=(800, 480), radial_color=(32, 92, 84), radial_radius=700)
    img = add_surface_noise(img, 12)
    img = add_table_frame(img, border_color=(74, 222, 128, 210), fill_color=(16, 42, 38, 205), border_width=3, pad_x=140, pad_y=90)
    return add_vignette(img, 0.8)

def make_granite_monolith():
    # Himalayan Granite Monolith: cold chiseled silver-grey granite
    img = create_base_gradient(W, H, (28, 32, 38), (14, 16, 20), radial_center=(800, 480), radial_color=(64, 76, 92), radial_radius=700)
    img = add_surface_noise(img, 16)
    img = add_table_frame(img, border_color=(186, 230, 253, 210), fill_color=(30, 34, 42, 210), border_width=4, pad_x=140, pad_y=90)
    return add_vignette(img, 0.82)

def make_sandalwood_amber():
    # Royal Sandalwood & Amber: rich golden amber and dark teak altar
    img = create_base_gradient(W, H, (38, 24, 12), (18, 10, 4), radial_center=(800, 480), radial_color=(110, 68, 30), radial_radius=700)
    img = add_surface_noise(img, 14)
    img = add_table_frame(img, border_color=(245, 158, 11, 230), fill_color=(46, 28, 14, 215), border_width=4, pad_x=140, pad_y=90)
    return add_vignette(img, 0.84)

def make_obsidian_vault():
    # Obsidian Observatory: mirror-polished midnight obsidian stone
    img = create_base_gradient(W, H, (14, 16, 24), (6, 8, 12), radial_center=(800, 480), radial_color=(36, 42, 68), radial_radius=700)
    img = add_surface_noise(img, 10)
    img = add_table_frame(img, border_color=(129, 140, 248, 215), fill_color=(18, 20, 30, 215), border_width=3, pad_x=140, pad_y=90)
    return add_vignette(img, 0.86)

def make_golden_harvest():
    # Golden Harvest & Woven Rattan: warm straw rattan and terracotta earth
    img = create_base_gradient(W, H, (38, 26, 12), (18, 12, 6), radial_center=(800, 480), radial_color=(105, 72, 30), radial_radius=700)
    img = add_surface_noise(img, 15)
    img = add_table_frame(img, border_color=(234, 179, 8, 220), fill_color=(44, 30, 14, 210), border_width=3, pad_x=140, pad_y=90)
    return add_vignette(img, 0.82)

def make_opal_aurora():
    # Iridescent Opal & Aurora: deep violet cosmic aurora and rose-gold
    img = create_base_gradient(W, H, (24, 16, 38), (10, 6, 18), radial_center=(800, 480), radial_color=(68, 42, 105), radial_radius=700)
    img = add_surface_noise(img, 12)
    img = add_table_frame(img, border_color=(244, 114, 182, 220), fill_color=(28, 18, 44, 210), border_width=3, pad_x=140, pad_y=90)
    return add_vignette(img, 0.83)

def make_bodhi_grove():
    # Sacred Bodhi Grove: gilded pipal wood with divine solar light
    img = create_base_gradient(W, H, (26, 34, 20), (12, 16, 8), radial_center=(800, 480), radial_color=(82, 98, 48), radial_radius=700)
    img = add_surface_noise(img, 13)
    img = add_table_frame(img, border_color=(250, 204, 21, 235), fill_color=(30, 40, 22, 215), border_width=4, pad_x=140, pad_y=90)
    return add_vignette(img, 0.84)

GENERATORS = {
    "whispering_pines_clean.png": make_whispering_pines,
    "temple_of_lines_clean.png": make_temple_of_lines,
    "biblios_wisdom_clean.png": make_biblios_wisdom,
    "celestial_starlight_clean.png": make_celestial_starlight,
    "golden_nebula_clean.png": make_golden_nebula,
    "spirit_altar_clean.png": make_spirit_altar,
    "sacred_sanctuary_clean.png": make_sacred_sanctuary,
    "ocean_horizon_clean.png": make_ocean_horizon,
    "terracotta_earth_clean.png": make_terracotta_earth,
    "floral_harmony_clean.png": make_floral_harmony,
    "blooming_mandala_clean.png": make_blooming_mandala,
    "sacred_spiral_clean.png": make_sacred_spiral,
    "master_sanctuary_clean.png": make_master_sanctuary,
    "lotus_pond_clean.png": make_lotus_pond,
    "granite_monolith_clean.png": make_granite_monolith,
    "sandalwood_amber_clean.png": make_sandalwood_amber,
    "obsidian_vault_clean.png": make_obsidian_vault,
    "golden_harvest_clean.png": make_golden_harvest,
    "opal_aurora_clean.png": make_opal_aurora,
    "bodhi_grove_clean.png": make_bodhi_grove,
}

def main():
    print("Generating 20 clean atmospheric environmental backgrounds...")
    for filename, gen_fn in GENERATORS.items():
        out_path = os.path.join(OUT_DIR, filename)
        img = gen_fn()
        img.save(out_path, format="PNG", optimize=True)
        # Also ensure non-clean copy exists if absent
        base_name = filename.replace("_clean.png", ".png")
        base_path = os.path.join(OUT_DIR, base_name)
        if not os.path.exists(base_path):
            img.save(base_path, format="PNG", optimize=True)
        print(f"  [OK] Saved {out_path} ({img.size[0]}x{img.size[1]})")
    print("All 20 clean backgrounds generated successfully with zero text prints!")

if __name__ == "__main__":
    main()
