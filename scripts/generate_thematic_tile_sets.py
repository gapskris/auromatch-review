"""
Generate High-Definition Luxury 3D Squircle Thematic Tile Sets (16 distinct tiles per theme for 13 themes = 208 tiles).
Matches the original isometric jewel art:
- 320x360 px (aspect ratio 1 : 1.125 squircle)
- Deep ambient drop shadow
- 3D extruded metallic chassis along bottom & right edges (physical depth)
- Multi-stop metallic beveled rim (24K Gold / Platinum / Rose Gold / Bronze)
- Volumetric translucent jewel glass core with radial caustic lighting
- Inner recessed metallic hairline ring
- Curved glass gloss bubble highlight across top-left quadrant
- Bold, large, 3D embossed metallic emblems with cast shadow, aura glow, and specular gleam
- No bottom text plaque cutting off the tile face
"""

import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

TILE_W, TILE_H = 320, 360
BASE_DIR = "Assets/themes"
os.makedirs(BASE_DIR, exist_ok=True)

# 13 Thematic Realms Configuration
THEME_CONFIGS = {
    "celestial_starlight": {
        "name": "Celestial Starlight",
        "bg_top": (14, 68, 88),
        "bg_bot": (8, 38, 55),
        "caustic": (34, 211, 238),
        "rim_type": "gold_24k",
        "emblem_color": (255, 235, 135),
        "emblem_gleam": (255, 255, 230),
        "emblem_shadow": (5, 20, 25),
        "aura_color": (251, 191, 36),
        "tiles": [
            ("Cosmic Star", "✨"), ("Aquamarine Gem", "💎"), ("Crescent Moon", "🌙"), ("Solar Crest", "☀️"),
            ("Polaris Compass", "🧭"), ("Comet Trail", "☄️"), ("Saturn Ring", "🪐"), ("Astral Orbit", "💫"),
            ("Radiant Nova", "🌟"), ("Starlight Crown", "👑"), ("Crystal Prism", "🔮"), ("Eclipse Ring", "⭕"),
            ("Zodiac Rune", "♈"), ("Zenith Spark", "⚡"), ("Cosmic Bell", "🔔"), ("Infinity Spiral", "♾️")
        ]
    },
    "whispering_pines": {
        "name": "Whispering Pines",
        "bg_top": (20, 62, 38),
        "bg_bot": (10, 34, 20),
        "caustic": (52, 211, 153),
        "rim_type": "warm_gold",
        "emblem_color": (255, 230, 145),
        "emblem_gleam": (255, 255, 220),
        "emblem_shadow": (8, 25, 12),
        "aura_color": (245, 158, 11),
        "tiles": [
            ("Emerald Leaf", "🍃"), ("Pinecone", "🌲"), ("Acorn", "🌰"), ("Oak Leaf", "🍂"),
            ("Fern Frond", "🌿"), ("Forest Mushroom", "🍄"), ("Cedar Bark", "🪵"), ("Maple Wing", "🍁"),
            ("Clover Sprout", "☘️"), ("Wild Berry", "🫐"), ("Woodland Owl", "🦉"), ("Forest Deer", "🦌"),
            ("Pine Needle", "🎋"), ("Sunlit Sprout", "🌱"), ("Tree of Life", "🌳"), ("Forest Blossom", "🌸")
        ]
    },
    "temple_of_lines": {
        "name": "Temple of Lines",
        "bg_top": (26, 52, 84),
        "bg_bot": (14, 28, 48),
        "caustic": (56, 189, 248),
        "rim_type": "platinum",
        "emblem_color": (235, 248, 255),
        "emblem_gleam": (255, 255, 255),
        "emblem_shadow": (8, 18, 32),
        "aura_color": (125, 211, 252),
        "tiles": [
            ("Blueprint Arch", "⛩️"), ("Slate Dome", "🏛️"), ("Torana Gate", "🛕"), ("Zen Tower", "🗼"),
            ("Sacred Triangle", "📐"), ("Compass Rose", "🧭"), ("Keystone", "🧱"), ("Spiral Column", "🌀"),
            ("Stepped Terrace", "🪜"), ("Temple Bell", "🔔"), ("Golden Caliper", "📏"), ("Sanctuary Obelisk", "🗿"),
            ("Lattice Grid", "🕸️"), ("Zen Stone", "🪨"), ("Balance Scale", "⚖️"), ("Horizon Portal", "🪟")
        ]
    },
    "biblios_wisdom": {
        "name": "Biblios Wisdom",
        "bg_top": (72, 26, 20),
        "bg_bot": (40, 12, 10),
        "caustic": (245, 158, 11),
        "rim_type": "gold_24k",
        "emblem_color": (255, 230, 140),
        "emblem_gleam": (255, 255, 225),
        "emblem_shadow": (25, 8, 6),
        "aura_color": (251, 191, 36),
        "tiles": [
            ("Gilded Owl", "🦉"), ("Sunburst Tome", "☀️"), ("Feather Quill", "🪶"), ("Open Codex", "📖"),
            ("Astrolabe", "🧭"), ("Vintage Hourglass", "⏳"), ("Laurel Wreath", "🌿"), ("Celestial Globe", "🌐"),
            ("Inkpot Scroll", "📜"), ("Library Lamp", "🏮"), ("Sealing Wax", "🏷️"), ("Scholar Key", "🗝️"),
            ("Radiant Star", "🌟"), ("Illuminated Folio", "📑"), ("Wisdom Crown", "👑"), ("Looking Glass", "🔍")
        ]
    },
    "golden_nebula": {
        "name": "Golden Nebula",
        "bg_top": (42, 28, 14),
        "bg_bot": (20, 12, 6),
        "caustic": (251, 191, 36),
        "rim_type": "gold_24k",
        "emblem_color": (255, 235, 145),
        "emblem_gleam": (255, 255, 230),
        "emblem_shadow": (20, 10, 4),
        "aura_color": (245, 158, 11),
        "tiles": [
            ("Luminous Rune", "💫"), ("Golden Tablet", "🌟"), ("Solar Flare", "☀️"), ("Nebula Spiral", "🌀"),
            ("Gold Constellation", "✨"), ("Supernova", "💥"), ("Galaxy Disc", "🌌"), ("Astral Gateway", "⛩️"),
            ("Golden Lotus", "🪷"), ("Radiant Phoenix", "🦅"), ("Cosmic Eye", "👁️"), ("Golden Sceptre", "🪄"),
            ("Eclipse Sun", "🌕"), ("Astral Hourglass", "⏳"), ("Star Chime", "🔔"), ("Celestial Crown", "👑")
        ]
    },
    "spirit_altar": {
        "name": "Spirit Altar",
        "bg_top": (240, 238, 232),
        "bg_bot": (198, 194, 186),
        "caustic": (255, 252, 240),
        "rim_type": "champagne_brass",
        "emblem_color": (155, 110, 45),
        "emblem_gleam": (245, 205, 115),
        "emblem_shadow": (60, 45, 20),
        "aura_color": (217, 165, 80),
        "tiles": [
            ("Marble Lotus", "🪷"), ("Marble Rosette", "🏵️"), ("Concentric Mandala", "💮"), ("Bodhi Leaf", "🍃"),
            ("Meditation Flame", "🔥"), ("Bronze Chime", "🔔"), ("Incense Censer", "🪔"), ("Offering Bowl", "🥣"),
            ("Sacred Conch", "🐚"), ("Endless Knot", "♾️"), ("White Jasmine", "🌼"), ("Water Lily", "🌸"),
            ("Golden Vessel", "🏺"), ("Spiritual Halo", "⭕"), ("Temple Camellia", "🌺"), ("Serene Pearl", "🤍")
        ]
    },
    "sacred_sanctuary": {
        "name": "Sacred Sanctuary",
        "bg_top": (66, 42, 16),
        "bg_bot": (36, 20, 8),
        "caustic": (245, 158, 11),
        "rim_type": "gold_24k",
        "emblem_color": (255, 230, 140),
        "emblem_gleam": (255, 255, 225),
        "emblem_shadow": (22, 12, 4),
        "aura_color": (251, 191, 36),
        "tiles": [
            ("Chiseled Lotus", "🪷"), ("Brass Rosette", "🏵️"), ("Sanctuary Flame", "🔥"), ("Golden Bell", "🔔"),
            ("Temple Pillar", "🏛️"), ("Incense Mist", "💨"), ("Amber Jewel", "💎"), ("Sacred Garland", "📿"),
            ("Solar Disk", "☀️"), ("Peace Dove", "🕊️"), ("Temple Gateway", "⛩️"), ("Vessel of Light", "🏺"),
            ("Radiant Chime", "🎐"), ("Aura Halo", "⭕"), ("Golden Leaf", "🍂"), ("Eternal Lamp", "🪔")
        ]
    },
    "ocean_horizon": {
        "name": "Ocean Horizon",
        "bg_top": (16, 70, 94),
        "bg_bot": (8, 38, 54),
        "caustic": (45, 212, 191),
        "rim_type": "gold_24k",
        "emblem_color": (240, 250, 255),
        "emblem_gleam": (255, 255, 255),
        "emblem_shadow": (4, 20, 28),
        "aura_color": (56, 189, 248),
        "tiles": [
            ("Azure Bubble", "🫧"), ("Luminous Pearl", "⚪"), ("Nautilus Shell", "🐚"), ("Sea Star", "⭐"),
            ("Ocean Wave", "🌊"), ("Coral Branch", "🪸"), ("Driftwood Tablet", "🪵"), ("Dolphin Crest", "🐬"),
            ("Tide Compass", "🧭"), ("Deep Lagoon", "💧"), ("Sea Anemone", "🌸"), ("Ambergris Gem", "💎"),
            ("Coastal Breeze", "💨"), ("Lighthouse Lamp", "🏮"), ("Seagrass Frond", "🌿"), ("Sunken Coin", "🪙")
        ]
    },
    "terracotta_earth": {
        "name": "Terracotta Earth",
        "bg_top": (96, 48, 28),
        "bg_bot": (52, 22, 12),
        "caustic": (249, 115, 22),
        "rim_type": "copper_gold",
        "emblem_color": (255, 225, 175),
        "emblem_gleam": (255, 250, 225),
        "emblem_shadow": (30, 10, 6),
        "aura_color": (245, 158, 11),
        "tiles": [
            ("Tree of Life", "🌳"), ("Terracotta Leaf", "🍂"), ("Clay Amphora", "🏺"), ("Deep Root", "🌱"),
            ("Sun-Baked Brick", "🧱"), ("Potter Wheel", "⚙️"), ("River Pebble", "🪨"), ("Earthy Wheat", "🌾"),
            ("Hearth Flame", "🔥"), ("Clay Basin", "🥣"), ("Ancient Fossil", "🐚"), ("Desert Bloom", "🌵"),
            ("Sienna Sun", "☀️"), ("Clay Tablet", "📜"), ("Terra Cameo", "🏵️"), ("Harvest Basket", "🧺")
        ]
    },
    "floral_harmony": {
        "name": "Floral Harmony",
        "bg_top": (86, 36, 56),
        "bg_bot": (48, 18, 30),
        "caustic": (244, 114, 182),
        "rim_type": "rose_gold",
        "emblem_color": (255, 235, 245),
        "emblem_gleam": (255, 255, 255),
        "emblem_shadow": (28, 8, 18),
        "aura_color": (244, 114, 182),
        "tiles": [
            ("Lotus Cameo", "🪷"), ("Rose Cameo", "🌹"), ("Magnolia Blossom", "🌸"), ("Orchid Sprig", "🌺"),
            ("Peony Crown", "🏵️"), ("Jasmine Garland", "🌼"), ("Tulip Cup", "🌷"), ("Sunflower Crest", "🌻"),
            ("Lavender Scent", "🪻"), ("Iris Blade", "🌿"), ("Blush Cameo", "💮"), ("Garden Butterfly", "🦋"),
            ("Honey Blossom", "🍯"), ("Morning Dew", "💧"), ("Cameo Brooch", "💎"), ("Pearl Petal", "🤍")
        ]
    },
    "blooming_mandala": {
        "name": "Blooming Mandala",
        "bg_top": (62, 32, 74),
        "bg_bot": (32, 14, 40),
        "caustic": (192, 132, 252),
        "rim_type": "gold_24k",
        "emblem_color": (255, 235, 150),
        "emblem_gleam": (255, 255, 230),
        "emblem_shadow": (22, 8, 28),
        "aura_color": (251, 191, 36),
        "tiles": [
            ("Porcelain Lotus", "🌸"), ("Gold Cameo", "🏵️"), ("Concentric Ring", "⭕"), ("Radial Star", "✳️"),
            ("Mandala Hub", "💮"), ("Filigree Petal", "🪷"), ("Sacred Wheel", "☸️"), ("Porcelain Rose", "🌹"),
            ("Gold Wire Crest", "⚜️"), ("Sunburst Halo", "☀️"), ("Lace Mandala", "🕸️"), ("Imperial Brocade", "👑"),
            ("Celestial Rosette", "🌟"), ("Ivory Cameo", "🤍"), ("Radiant Bloom", "🌺"), ("Geometric Jewel", "💎")
        ]
    },
    "sacred_spiral": {
        "name": "Sacred Spiral",
        "bg_top": (24, 70, 44),
        "bg_bot": (10, 36, 22),
        "caustic": (74, 222, 128),
        "rim_type": "warm_gold",
        "emblem_color": (245, 255, 185),
        "emblem_gleam": (255, 255, 235),
        "emblem_shadow": (8, 24, 14),
        "aura_color": (163, 230, 53),
        "tiles": [
            ("Golden Vine", "🌿"), ("Sacred Bloom", "🪷"), ("Fibonacci Spiral", "🌀"), ("Fern Sprout", "🌱"),
            ("Spiral Shell", "🐚"), ("Curled Tendril", "🌾"), ("Helix Crest", "🧬"), ("Emerald Jewel", "💎"),
            ("Sunlit Canopy", "🌳"), ("Verdant Clover", "🍀"), ("Botanical Orbit", "💫"), ("Forest Fern", "🌿"),
            ("Twisting Branch", "🪵"), ("Dewdrop Frond", "💧"), ("Spiral Galaxy", "🌌"), ("Verdant Crown", "👑")
        ]
    },
    "master_sanctuary": {
        "name": "Master Sanctuary",
        "bg_top": (48, 32, 22),
        "bg_bot": (22, 14, 8),
        "caustic": (251, 191, 36),
        "rim_type": "gold_24k",
        "emblem_color": (255, 235, 145),
        "emblem_gleam": (255, 255, 230),
        "emblem_shadow": (20, 10, 4),
        "aura_color": (245, 158, 11),
        "tiles": [
            ("Carved Walnut", "🪵"), ("Marble Inlay", "🪷"), ("Master Crown", "👑"), ("Golden Key", "🗝️"),
            ("Grand Chime", "🔔"), ("Imperial Crest", "⚜️"), ("Sanctuary Sceptre", "🪄"), ("Royal Astrolabe", "🧭"),
            ("Grand Hourglass", "⏳"), ("Polished Cameo", "🏵️"), ("Altar Vessel", "🏺"), ("Diamond Star", "💎"),
            ("Golden Laurel", "🌿"), ("Master Codex", "📖"), ("Shield of Honor", "🛡️"), ("Radiant Sun", "☀️")
        ]
    },
    "lotus_pond": {
        "name": "Sunlit Lotus Pond",
        "bg_top": (20, 68, 64),
        "bg_bot": (10, 38, 36),
        "caustic": (45, 212, 191),
        "rim_type": "warm_gold",
        "emblem_color": (240, 255, 220),
        "emblem_gleam": (255, 255, 240),
        "emblem_shadow": (8, 28, 24),
        "aura_color": (52, 211, 153),
        "tiles": [
            ("Sunlit Lotus", "🪷"), ("Water Lily Petal", "🌸"), ("Floating Lilypad", "🍃"), ("River Pebble", "🪨"),
            ("Koi Fish", "🐟"), ("Bamboo Slat", "🎋"), ("Clear Dewdrop", "💧"), ("Dragonfly Wing", "🪰"),
            ("Reed Frond", "🌾"), ("Spring Water", "🌊"), ("Willow Branch", "🌿"), ("Lotus Seedpod", "🌰"),
            ("Radiant Lotus Core", "✨"), ("Golden Water Lily", "🌟"), ("Jade Lilypad", "🍀"), ("Sunset Reflection", "🌅")
        ]
    },
    "granite_monolith": {
        "name": "Himalayan Granite Monolith",
        "bg_top": (46, 52, 60),
        "bg_bot": (24, 28, 34),
        "caustic": (186, 230, 253),
        "rim_type": "platinum",
        "emblem_color": (245, 248, 255),
        "emblem_gleam": (255, 255, 255),
        "emblem_shadow": (12, 16, 20),
        "aura_color": (147, 197, 253),
        "tiles": [
            ("Granite Peak", "🏔️"), ("Mountain Ridge", "⛰️"), ("Chiseled Stone", "🪨"), ("Alpine Cloud", "☁️"),
            ("Ice Crystal", "❄️"), ("Glacial Stream", "💧"), ("Pine Needle", "🌲"), ("Falcon Crest", "🦅"),
            ("Stone Cairn", "🗿"), ("Monolith Pillar", "🏛️"), ("High Altitude Sun", "☀️"), ("Mountain Bell", "🔔"),
            ("Gilded Summit", "✨"), ("Radiant Peak", "🌟"), ("Silver Lichen Stone", "◽"), ("Zenith Compass", "🧭")
        ]
    },
    "sandalwood_amber": {
        "name": "Royal Sandalwood & Amber",
        "bg_top": (78, 48, 22),
        "bg_bot": (42, 24, 10),
        "caustic": (245, 158, 11),
        "rim_type": "gold_24k",
        "emblem_color": (255, 230, 140),
        "emblem_gleam": (255, 255, 220),
        "emblem_shadow": (24, 12, 4),
        "aura_color": (251, 191, 36),
        "tiles": [
            ("Sandalwood Fan", "🪭"), ("Amber Resin Drop", "💎"), ("Incense Smoke", "💨"), ("Carved Rosette", "🏵️"),
            ("Honeycomb Cell", "🍯"), ("Aspiration Flame", "🔥"), ("Spiced Clove", "🌰"), ("Carved Elephant", "🐘"),
            ("Teak Box Clasp", "🗝️"), ("Scented Garland", "📿"), ("Amber Sunburst", "☀️"), ("Offering Urn", "🏺"),
            ("Glowing Amber Relic", "✨"), ("Luminous Sandal Seal", "🌟"), ("Golden Grain", "🌾"), ("Royal Diadem", "👑")
        ]
    },
    "obsidian_vault": {
        "name": "Obsidian Observatory",
        "bg_top": (18, 20, 28),
        "bg_bot": (8, 10, 16),
        "caustic": (147, 197, 253),
        "rim_type": "platinum",
        "emblem_color": (230, 245, 255),
        "emblem_gleam": (255, 255, 255),
        "emblem_shadow": (4, 6, 10),
        "aura_color": (99, 102, 241),
        "tiles": [
            ("Obsidian Mirror", "🪞"), ("Midnight Star", "⭐"), ("Astrolabe Gear", "⚙️"), ("Celestial Telescope", "🔭"),
            ("Crescent Moon", "🌙"), ("Nebula Core", "🌀"), ("Prismatic Shard", "💎"), ("Eclipse Ring", "⭕"),
            ("Comet Trail", "☄️"), ("Planetary Ring", "🪐"), ("Starlight Ray", "⚡"), ("Cosmic Compass", "🧭"),
            ("Radiant Obsidian Star", "✨"), ("Platinum Nova", "🌟"), ("Deep Sky Void", "🌌"), ("Infinite Knot", "♾️")
        ]
    },
    "golden_harvest": {
        "name": "Golden Harvest & Woven Rattan",
        "bg_top": (84, 56, 20),
        "bg_bot": (46, 28, 8),
        "caustic": (245, 158, 11),
        "rim_type": "warm_gold",
        "emblem_color": (255, 235, 150),
        "emblem_gleam": (255, 255, 230),
        "emblem_shadow": (26, 14, 4),
        "aura_color": (234, 179, 8),
        "tiles": [
            ("Wheat Sheaf", "🌾"), ("Woven Rattan Knot", "🧺"), ("Harvest Sun", "☀️"), ("Clay Grain Pot", "🏺"),
            ("Golden Corn", "🌽"), ("Earthen Sickle", "🌙"), ("Golden Sprout", "🌱"), ("Honey Comb", "🍯"),
            ("Field Poppy", "🌺"), ("Bountiful Basket", "🧺"), ("Sunlit Millstone", "⚙️"), ("Harvest Bread", "🍞"),
            ("Radiant Golden Ear", "✨"), ("Luminous Grain Wheel", "🌟"), ("Straw Crown", "👑"), ("Autumn Clover", "🍀")
        ]
    },
    "opal_aurora": {
        "name": "Iridescent Opal & Aurora",
        "bg_top": (32, 24, 58),
        "bg_bot": (14, 10, 30),
        "caustic": (168, 85, 247),
        "rim_type": "rose_gold",
        "emblem_color": (245, 235, 255),
        "emblem_gleam": (255, 255, 255),
        "emblem_shadow": (14, 8, 26),
        "aura_color": (192, 132, 252),
        "tiles": [
            ("Fire Opal", "💎"), ("Aurora Wave", "🌌"), ("Mother of Pearl", "⚪"), ("Prismatic Prism", "🔮"),
            ("Luminous Butterfly", "🦋"), ("Iridescent Feather", "🪶"), ("Northern Star", "⭐"), ("Violet Crystal", "💜"),
            ("Rainbow Arc", "🌈"), ("Celestial Veil", "✨"), ("Polar Glow", "❄️"), ("Spectral Swan", "🦢"),
            ("Pulsing Opal Core", "🌟"), ("Radiant Aurora Crown", "👑"), ("Iridescent Lotus", "🪷"), ("Astral Halo", "⭕")
        ]
    },
    "bodhi_grove": {
        "name": "Sacred Bodhi Grove",
        "bg_top": (38, 56, 32),
        "bg_bot": (18, 30, 16),
        "caustic": (234, 179, 8),
        "rim_type": "gold_24k",
        "emblem_color": (255, 240, 160),
        "emblem_gleam": (255, 255, 230),
        "emblem_shadow": (12, 22, 10),
        "aura_color": (250, 204, 21),
        "tiles": [
            ("Bodhi Leaf", "🍃"), ("Sacred Bodhi Tree", "🌳"), ("White Jade Tablet", "🤍"), ("Enlightenment Flame", "🔥"),
            ("Lotus Seat", "🪷"), ("Wheel of Dharma", "☸️"), ("Golden Bell", "🔔"), ("Meditation Urn", "🏺"),
            ("Sunburst Halo", "☀️"), ("Sacred Thread", "📿"), ("Radiant Deer", "🦌"), ("Peace Crane", "🕊️"),
            ("Golden Bodhi Master", "✨"), ("Supreme Sun Star", "🌟"), ("Jade Lotus Emblem", "🏵️"), ("Universal Crown", "👑")
        ]
    }
}

def get_rim_colors(rim_type):
    """Returns color stops for metallic rim and chassis."""
    if rim_type == "platinum":
        return {
            "chassis_dark": (110, 130, 155),
            "chassis_light": (190, 210, 230),
            "rim_gleam": (255, 255, 255),
            "rim_mid": (210, 225, 240),
            "rim_dark": (130, 150, 175),
            "rim_accent": (225, 240, 255),
            "hairline": (200, 225, 245, 180)
        }
    elif rim_type == "rose_gold":
        return {
            "chassis_dark": (140, 75, 90),
            "chassis_light": (220, 150, 165),
            "rim_gleam": (255, 240, 245),
            "rim_mid": (235, 165, 180),
            "rim_dark": (160, 90, 105),
            "rim_accent": (245, 185, 200),
            "hairline": (245, 190, 205, 180)
        }
    elif rim_type == "copper_gold":
        return {
            "chassis_dark": (130, 65, 25),
            "chassis_light": (215, 135, 75),
            "rim_gleam": (255, 240, 215),
            "rim_mid": (225, 145, 80),
            "rim_dark": (155, 80, 30),
            "rim_accent": (240, 165, 105),
            "hairline": (240, 175, 120, 180)
        }
    elif rim_type == "champagne_brass":
        return {
            "chassis_dark": (120, 90, 45),
            "chassis_light": (195, 155, 95),
            "rim_gleam": (255, 250, 230),
            "rim_mid": (210, 170, 105),
            "rim_dark": (145, 105, 45),
            "rim_accent": (225, 185, 125),
            "hairline": (210, 170, 105, 180)
        }
    elif rim_type == "warm_gold":
        return {
            "chassis_dark": (125, 80, 25),
            "chassis_light": (210, 160, 60),
            "rim_gleam": (255, 248, 205),
            "rim_mid": (225, 175, 65),
            "rim_dark": (160, 105, 25),
            "rim_accent": (235, 195, 85),
            "hairline": (235, 195, 95, 180)
        }
    else:  # gold_24k (Pic 1 benchmark)
        return {
            "chassis_dark": (130, 85, 20),
            "chassis_light": (220, 170, 65),
            "rim_gleam": (255, 250, 210),
            "rim_mid": (235, 185, 70),
            "rim_dark": (175, 115, 25),
            "rim_accent": (245, 205, 95),
            "hairline": (245, 210, 110, 180)
        }

def render_luxury_tile(theme_id, cfg, tile_idx, tile_name, symbol_char, font_emoji):
    """Renders a single 320x360 luxury squircle 3D jewel tile replicating the original mockups."""
    W, H = TILE_W, TILE_H
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    rim = get_rim_colors(cfg["rim_type"])

    # 1. Deep Ambient Drop Shadow
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([20, 24, W - 14, H - 10], radius=52, fill=(0, 0, 0, 160))
    shadow = shadow.filter(ImageFilter.GaussianBlur(12))
    img = Image.alpha_composite(img, shadow)

    # 2. 3D Extruded Metallic Base / Chassis (bottom and right bevel depth)
    base_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(base_img)
    cd, cl = rim["chassis_dark"], rim["chassis_light"]
    for offset in range(14, 0, -2):
        t = offset / 14.0
        r = int(cd[0] * (1 - t) + cl[0] * t)
        g = int(cd[1] * (1 - t) + cl[1] * t)
        b = int(cd[2] * (1 - t) + cl[2] * t)
        b_draw.rounded_rectangle(
            [18 + offset // 3, 20 + offset, W - 18 + offset // 3, H - 18 + offset],
            radius=48, fill=(r, g, b, 255)
        )
    img = Image.alpha_composite(img, base_img)

    # 3. Outer Polished Metallic Rim (Main Bezel)
    rim_box = [20, 18, W - 20, H - 26]
    rim_mask = Image.new("L", (W, H), 0)
    rm_draw = ImageDraw.Draw(rim_mask)
    rm_draw.rounded_rectangle(rim_box, radius=46, fill=255)

    gold_grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(gold_grad)
    for y in range(rim_box[1], rim_box[3]):
        frac = (y - rim_box[1]) / (rim_box[3] - rim_box[1])
        if frac < 0.12:
            color = rim["rim_gleam"] + (255,)
        elif frac < 0.45:
            color = rim["rim_mid"] + (255,)
        elif frac < 0.85:
            color = rim["rim_dark"] + (255,)
        else:
            color = rim["rim_accent"] + (255,)
        g_draw.line([(0, y), (W, y)], fill=color)

    rim_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    rim_layer.paste(gold_grad, (0, 0), rim_mask)
    img = Image.alpha_composite(img, rim_layer)

    # 4. Volumetric Translucent Jewel Glass / Core
    glass_box = [26, 24, W - 26, H - 32]
    glass_mask = Image.new("L", (W, H), 0)
    gm_draw = ImageDraw.Draw(glass_mask)
    gm_draw.rounded_rectangle(glass_box, radius=40, fill=255)

    glass_grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gg_draw = ImageDraw.Draw(glass_grad)
    top_c, bot_c = cfg["bg_top"], cfg["bg_bot"]
    for y in range(glass_box[1], glass_box[3]):
        frac = (y - glass_box[1]) / (glass_box[3] - glass_box[1])
        # Smooth cubic interpolation for depth
        smooth_frac = frac * frac * (3 - 2 * frac)
        r = int(top_c[0] * (1 - smooth_frac) + bot_c[0] * smooth_frac)
        g = int(top_c[1] * (1 - smooth_frac) + bot_c[1] * smooth_frac)
        b = int(top_c[2] * (1 - smooth_frac) + bot_c[2] * smooth_frac)
        gg_draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    # Radial Caustic Spotlight in upper-center of glass
    caustic = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    c_draw = ImageDraw.Draw(caustic)
    cx, cy = W // 2, int(glass_box[1] + (glass_box[3] - glass_box[1]) * 0.48)
    cc = cfg["caustic"]
    for radius in range(120, 0, -6):
        alpha = int(55 * (1 - radius / 120))
        c_draw.ellipse(
            [cx - radius * 1.15, cy - radius * 0.85, cx + radius * 1.15, cy + radius * 0.85],
            fill=cc + (alpha,)
        )
    glass_grad = Image.alpha_composite(glass_grad, caustic)

    glass_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glass_layer.paste(glass_grad, (0, 0), glass_mask)
    img = Image.alpha_composite(img, glass_layer)

    # 5. Inner Recessed Metallic Hairline Ring
    inner_box = [34, 32, W - 34, H - 40]
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle(inner_box, radius=32, outline=rim["hairline"], width=2)

    # 6. Curved Glass Gloss Reflection (Top-Left Bubble Highlight)
    gloss = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gl_draw = ImageDraw.Draw(gloss)
    gl_draw.rounded_rectangle([32, 28, int(W * 0.68), int(H * 0.28)], radius=26, fill=(255, 255, 255, 55))
    gloss = gloss.filter(ImageFilter.GaussianBlur(8))
    gloss_clipped = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gloss_clipped.paste(gloss, (0, 0), glass_mask)
    img = Image.alpha_composite(img, gloss_clipped)

    # 7. Bold Gleaming 3D Embossed Metallic Emblem
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), symbol_char, font=font_emoji)
    sym_x = (W - (bbox[2] + bbox[0])) // 2
    sym_y = (H - (bbox[3] + bbox[1])) // 2 - 4

    # Cast shadow behind symbol
    sh_color = cfg["emblem_shadow"] + (230,)
    draw.text((sym_x + 3, sym_y + 4), symbol_char, font=font_emoji, fill=sh_color)

    # Radiant glow aura around symbol
    aura = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    a_draw = ImageDraw.Draw(aura)
    a_draw.text((sym_x, sym_y), symbol_char, font=font_emoji, fill=cfg["aura_color"] + (180,))
    aura = aura.filter(ImageFilter.GaussianBlur(10))
    img = Image.alpha_composite(img, aura)

    # Main metallic symbol body
    draw = ImageDraw.Draw(img)
    draw.text((sym_x, sym_y), symbol_char, font=font_emoji, fill=cfg["emblem_color"] + (255,))
    # Top-left specular gleam highlight
    draw.text((sym_x - 1, sym_y - 2), symbol_char, font=font_emoji, fill=cfg["emblem_gleam"] + (170,))

    return img

def main():
    print("Generating 208 Ultra-HD Luxury 3D Squircle Thematic Tiles (320x360)...")
    
    # Load Segoe UI Emoji font at 120px
    font_emoji = None
    for fpath in ["C:/Windows/Fonts/seguiemj.ttf", "C:/Windows/Fonts/seguisym.ttf"]:
        if os.path.exists(fpath):
            font_emoji = ImageFont.truetype(fpath, 120)
            break
    if font_emoji is None:
        font_emoji = ImageFont.load_default()

    total_generated = 0
    for theme_id, cfg in THEME_CONFIGS.items():
        theme_dir = os.path.join(BASE_DIR, theme_id)
        os.makedirs(theme_dir, exist_ok=True)
        for idx, (t_name, t_symbol) in enumerate(cfg["tiles"], start=1):
            tile_img = render_luxury_tile(theme_id, cfg, idx, t_name, t_symbol, font_emoji)
            fname = f"tile_{idx:02d}.png"
            tile_path = os.path.join(theme_dir, fname)
            tile_img.save(tile_path, format="PNG", optimize=True)
            total_generated += 1
        print(f"  [OK] Generated 16 luxury squircle tiles for: {cfg['name']} ({theme_id})")

    print(f"\nSUCCESS: Generated {total_generated} ultra-luxury tiles across all 13 themes!")

if __name__ == "__main__":
    main()
