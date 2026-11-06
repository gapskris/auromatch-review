import os
import sys
import math
from PIL import Image, ImageDraw, ImageFilter

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def draw_auromatch_icon(size=1024, maskable=False):
    # Render at high resolution (1024x1024) for supersampled downscaling
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    margin = int(size * 0.1) if maskable else int(size * 0.025)
    w = size - 2 * margin
    radius = int(w * 0.22) # Squircle radius ~22%
    
    # Gradient simulation for background: Deep sanctuary emerald
    # Top-left to bottom-right emerald gradient
    top_color = (2, 26, 18, 255)
    mid_color = (7, 56, 42, 255)
    bot_color = (13, 74, 55, 255)
    
    # Base rounded rectangle background
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=radius,
        fill=mid_color
    )
    
    # Outer golden rim
    rim_width = max(3, int(size * 0.015))
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=radius,
        outline=(217, 119, 6, 255),
        width=rim_width
    )
    
    # Inner gold border with dash/inset
    inset = margin + int(size * 0.028)
    draw.rounded_rectangle(
        [inset, inset, size - inset, size - inset],
        radius=radius - int(size * 0.02),
        outline=(251, 191, 36, 120),
        width=max(1, int(size * 0.003))
    )

    cx, cy = size // 2, size // 2
    
    # Central radiant glow
    glow_r = int(w * 0.38)
    for r in range(glow_r, 0, -int(size * 0.02)):
        alpha = int(45 * (1.0 - (r / glow_r)))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(253, 224, 71, alpha))

    # Outer celestial geometry circles
    r_geom = int(w * 0.32)
    draw.ellipse([cx - r_geom, cy - r_geom, cx + r_geom, cy + r_geom], outline=(251, 191, 36, 80), width=max(1, int(size * 0.003)))
    
    r_inner_ring = int(w * 0.27)
    draw.ellipse([cx - r_inner_ring, cy - r_inner_ring, cx + r_inner_ring, cy + r_inner_ring], outline=(251, 191, 36, 110), width=max(1, int(size * 0.002)))

    # 12 Starlight orbit nodes
    for i in range(12):
        angle = math.radians(i * 30)
        node_x = cx + int(r_geom * math.sin(angle))
        node_y = cy - int(r_geom * math.cos(angle))
        nr = max(2, int(size * 0.007))
        draw.ellipse([node_x - nr, node_y - nr, node_x + nr, node_y + nr], fill=(254, 240, 138, 230))

    # 12 Golden Lotus Petals (Concentric sacred geometry)
    petal_len = int(w * 0.24)
    petal_w = int(w * 0.045)
    for i in range(12):
        angle = math.radians(i * 30)
        tip_x = cx + int(petal_len * math.sin(angle))
        tip_y = cy - int(petal_len * math.cos(angle))
        
        base_x = cx + int((petal_len * 0.25) * math.sin(angle))
        base_y = cy - int((petal_len * 0.25) * math.cos(angle))
        
        # Perpendicular vector for petal width
        px = -math.cos(angle) * petal_w
        py = -math.sin(angle) * petal_w
        
        mid_x = cx + int((petal_len * 0.6) * math.sin(angle))
        mid_y = cy - int((petal_len * 0.6) * math.cos(angle))
        
        points = [
            (base_x, base_y),
            (mid_x + px, mid_y + py),
            (tip_x, tip_y),
            (mid_x - px, mid_y - py)
        ]
        draw.polygon(points, fill=(250, 204, 21, 230), outline=(180, 83, 9, 255))

    # Inner Triad Trinity Arcs (3-Match Mechanic, at 0, 120, 240 deg)
    triad_len = int(w * 0.17)
    triad_w = int(w * 0.055)
    for i in [0, 120, 240]:
        angle = math.radians(i)
        tip_x = cx + int(triad_len * math.sin(angle))
        tip_y = cy - int(triad_len * math.cos(angle))
        
        base_x = cx + int((triad_len * 0.2) * math.sin(angle))
        base_y = cy - int((triad_len * 0.2) * math.cos(angle))
        
        px = -math.cos(angle) * triad_w
        py = -math.sin(angle) * triad_w
        
        mid_x = cx + int((triad_len * 0.55) * math.sin(angle))
        mid_y = cy - int((triad_len * 0.55) * math.cos(angle))
        
        points = [
            (base_x, base_y),
            (mid_x + px, mid_y + py),
            (tip_x, tip_y),
            (mid_x - px, mid_y - py)
        ]
        draw.polygon(points, fill=(255, 255, 255, 240), outline=(245, 158, 11, 255))

    # Central Core Shield
    core_r = int(w * 0.08)
    draw.ellipse([cx - core_r, cy - core_r, cx + core_r, cy + core_r], fill=(4, 34, 25, 255), outline=(245, 158, 11, 255), width=max(2, int(size * 0.008)))
    
    # 4-Pointed Morning Star Diamond (✨ Spark)
    star_len = int(w * 0.09)
    star_waist = int(w * 0.02)
    diamond = [
        (cx, cy - star_len),
        (cx + star_waist, cy - star_waist),
        (cx + star_len, cy),
        (cx + star_waist, cy + star_waist),
        (cx, cy + star_len),
        (cx - star_waist, cy + star_waist),
        (cx - star_len, cy),
        (cx - star_waist, cy - star_waist)
    ]
    draw.polygon(diamond, fill=(255, 251, 235, 255), outline=(245, 158, 11, 255))
    
    # Central white nucleus
    nuc_r = max(2, int(size * 0.012))
    draw.ellipse([cx - nuc_r, cy - nuc_r, cx + nuc_r, cy + nuc_r], fill=(255, 255, 255, 255))

    return img

def generate_all_icons():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    icons_dir = os.path.join(base_dir, 'Assets', 'icons')
    os.makedirs(icons_dir, exist_ok=True)

    print("--> Generating Master 2048x2048 icon model...")
    master_img = draw_auromatch_icon(size=2048, maskable=False)
    maskable_img = draw_auromatch_icon(size=2048, maskable=True)

    targets = [
        ('icon-512.png', master_img, 512),
        ('icon-maskable-512.png', maskable_img, 512),
        ('icon-192.png', master_img, 192),
        ('apple-touch-icon.png', master_img, 180),
        ('favicon.png', master_img, 64),
        ('favicon-32.png', master_img, 32),
    ]

    for fname, src, dim in targets:
        out_path = os.path.join(icons_dir, fname)
        resized = src.resize((dim, dim), Image.Resampling.LANCZOS)
        resized.save(out_path, format='PNG', optimize=True)
        print(f"    ✓ Generated {fname} ({dim}x{dim})")

    # Generate multi-res favicon.ico in base directory and icons directory
    ico_img = master_img.resize((64, 64), Image.Resampling.LANCZOS)
    ico_path1 = os.path.join(base_dir, 'favicon.ico')
    ico_path2 = os.path.join(icons_dir, 'favicon.ico')
    ico_img.save(ico_path1, format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    ico_img.save(ico_path2, format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print("    ✓ Generated favicon.ico (16, 32, 48, 64px)")

if __name__ == '__main__':
    generate_all_icons()
