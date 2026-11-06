import os
import json
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BG_DIR = "Assets/backgrounds"
THEME_DIR = "Assets/themes"
os.makedirs(BG_DIR, exist_ok=True)
os.makedirs(THEME_DIR, exist_ok=True)

# 20 Brand New Themes with Distinct Physical Materials (Zero references to doc/ mockups)
NEW_20_THEMES = [
    {
        "id": "kyoto_bamboo",
        "chapter": 1,
        "name": "Kyoto Bamboo Grove",
        "subtitle": "Polished Moso Bamboo · Serene Water Basin",
        "archetype": "bark_leaf",
        "audioPreset": "forest",
        "icon": "🎋",
        "bg_top": (16, 48, 24), "bg_bot": (8, 24, 12),
        "radial": (42, 120, 64),
        "rim_type": "warm_gold",
        "caustic": (74, 222, 128),
        "emblem_color": (240, 255, 215), "emblem_gleam": (255, 255, 240), "emblem_shadow": (6, 22, 10), "aura_color": (34, 197, 94),
        "tiles": [
            ("Bamboo Slat", "🎋"), ("Fresh Sprout", "🌱"), ("River Pebble", "🪨"), ("Water Lily", "🪷"),
            ("Green Tea Leaf", "🍃"), ("Cranes Nest", "🪺"), ("Stone Basin", "🥣"), ("Willow Wisp", "🌿"),
            ("Zen Bell", "🔔"), ("Koi Ripple", "🐟"), ("Paper Lantern", "🏮"), ("Bamboo Raft", "🪵"),
            ("Radiant Bamboo", "✨"), ("Golden Sprout", "🌟"), ("Jade Lilypad", "🍀"), ("Zen Crest", "🏵️")
        ]
    },
    {
        "id": "nordic_pine",
        "chapter": 2,
        "name": "Nordic Pine & Amber",
        "subtitle": "Scandinavian Pine Timber · Raw Golden Amber",
        "archetype": "bark_leaf",
        "audioPreset": "forest",
        "icon": "🌲",
        "bg_top": (22, 42, 28), "bg_bot": (10, 22, 14),
        "radial": (68, 110, 55),
        "rim_type": "copper_gold",
        "caustic": (245, 158, 11),
        "emblem_color": (255, 235, 160), "emblem_gleam": (255, 255, 230), "emblem_shadow": (14, 20, 8), "aura_color": (217, 119, 6),
        "tiles": [
            ("Pinecone", "🌲"), ("Cedar Bark", "🪵"), ("Forest Acorn", "🌰"), ("Amber Resin", "💎"),
            ("Birch Leaf", "🍂"), ("Wild Blueberry", "🫐"), ("Forest Fern", "🌿"), ("Clover Leaf", "☘️"),
            ("Woodland Owl", "🦉"), ("Stag Antler", "🦌"), ("Winter Chime", "🔔"), ("Campfire Embers", "🔥"),
            ("Gilded Pinecone", "✨"), ("Radiant Amber", "🌟"), ("Lichen Bark", "🍃"), ("Nordic Crown", "👑")
        ]
    },
    {
        "id": "celadon_jade",
        "chapter": 3,
        "name": "Imperial Celadon Jade",
        "subtitle": "Carved Translucent Pale Jade · Aged Bronze",
        "archetype": "slate_zen",
        "audioPreset": "zen_stone",
        "icon": "🪨",
        "bg_top": (20, 48, 38), "bg_bot": (10, 26, 20),
        "radial": (52, 130, 95),
        "rim_type": "champagne_brass",
        "caustic": (110, 231, 183),
        "emblem_color": (230, 255, 235), "emblem_gleam": (255, 255, 250), "emblem_shadow": (8, 24, 16), "aura_color": (52, 211, 153),
        "tiles": [
            ("Jade Tablet", "🪨"), ("Carved Lotus", "🪷"), ("Bronze Bell", "🔔"), ("Water Ripple", "〰️"),
            ("Zen Pebble", "⚪"), ("Bamboo Shoot", "🎍"), ("Temple Gate", "⛩️"), ("Dragon Crest", "🐉"),
            ("Jade Disk", "⭕"), ("Incense Mist", "💨"), ("Ceramic Bowl", "🥣"), ("Willow Frond", "🌿"),
            ("Luminous Jade", "✨"), ("Golden Lotus Cameo", "🌟"), ("Imperial Seal", "🏵️"), ("Jade Crown", "👑")
        ]
    },
    {
        "id": "aegean_seaglass",
        "chapter": 4,
        "name": "Aegean Sea Glass",
        "subtitle": "Frosted Aquamarine Sea-Glass · Salted Driftwood",
        "archetype": "seaglass",
        "audioPreset": "ocean_tide",
        "icon": "🌊",
        "bg_top": (14, 56, 76), "bg_bot": (6, 28, 42),
        "radial": (38, 135, 175),
        "rim_type": "platinum",
        "caustic": (56, 189, 248),
        "emblem_color": (235, 250, 255), "emblem_gleam": (255, 255, 255), "emblem_shadow": (4, 20, 28), "aura_color": (56, 189, 248),
        "tiles": [
            ("Frosted Seaglass", "🫧"), ("Nautilus Shell", "🐚"), ("Sea Star", "⭐"), ("Tidal Wave", "🌊"),
            ("Driftwood Slat", "🪵"), ("Coral Branch", "🪸"), ("Pearlescent Shell", "⚪"), ("Sea Anemone", "🌸"),
            ("Coastal Compass", "🧭"), ("Azure Pebble", "🪨"), ("Lighthouse Lamp", "🏮"), ("Dolphin Crest", "🐬"),
            ("Radiant Seaglass", "✨"), ("Golden Starfish", "🌟"), ("Tidal Core", "💫"), ("Aegean Crown", "👑")
        ]
    },
    {
        "id": "murano_crystal",
        "chapter": 5,
        "name": "Venetian Murano Crystal",
        "subtitle": "Cobalt Blown Glass · 24K Suspended Gold Leaf",
        "archetype": "cosmic_glass",
        "audioPreset": "crystal_bell",
        "icon": "💎",
        "tiles": [
            ("Murano Glass", "💎"), ("Gold Leaf Drop", "✨"), ("Azure Spiral", "🌀"), ("Cobalt Prism", "🔮"),
            ("Venetian Mask", "🎭"), ("Palazzo Lantern", "🏮"), ("Chandelier Shard", "⭐"), ("Gilded Scroll", "📜"),
            ("Canal Ripple", "🌊"), ("Glass Goblet", "🍷"), ("Filigree Wire", "⚜️"), ("Hourglass", "⏳"),
            ("Luminous Crystal", "🌟"), ("Golden Nebula Core", "💫"), ("Radiant Chime", "🔔"), ("Murano Crown", "👑")
        ],
        "bg_top": (18, 32, 68), "bg_bot": (8, 14, 38), "radial": (44, 82, 170),
        "rim_type": "gold_24k", "caustic": (96, 165, 250),
        "emblem_color": (255, 235, 145), "emblem_gleam": (255, 255, 230), "emblem_shadow": (8, 12, 34), "aura_color": (251, 191, 36)
    },
    {
        "id": "moroccan_zellige",
        "chapter": 6,
        "name": "Moroccan Zellige Ceramic",
        "subtitle": "Hand-Cut Glazed Terracotta · Cobalt Inlays",
        "archetype": "porcelain_cameo",
        "audioPreset": "clay_pot",
        "icon": "🏺",
        "tiles": [
            ("Zellige Star", "✳️"), ("Cobalt Tile", "🔷"), ("Terracotta Rosette", "🏵️"), ("Courtyard Arch", "⛩️"),
            ("Fountain Ripple", "💧"), ("Orange Blossom", "🌼"), ("Brass Lantern", "🏮"), ("Mosaic Square", "⏹️"),
            ("Geometric Knot", "♾️"), ("Glazed amphora", "🏺"), ("Ochre Tile", "🔶"), ("Palm Frond", "🌴"),
            ("Golden Zellige", "✨"), ("Radiant Rosette", "🌟"), ("Mosaic Wheel", "☸️"), ("Royal Riad Crown", "👑")
        ],
        "bg_top": (44, 26, 18), "bg_bot": (22, 12, 8), "radial": (130, 68, 38),
        "rim_type": "copper_gold", "caustic": (249, 115, 22),
        "emblem_color": (255, 230, 160), "emblem_gleam": (255, 255, 225), "emblem_shadow": (20, 10, 6), "aura_color": (245, 158, 11)
    },
    {
        "id": "silver_granite",
        "chapter": 7,
        "name": "Himalayan Silver Granite",
        "subtitle": "Rough-Hewn Silver Granite · High Mountain Mist",
        "archetype": "slate_zen",
        "audioPreset": "zen_stone",
        "icon": "🏔️",
        "tiles": [
            ("Granite Peak", "🏔️"), ("Mountain Ridge", "⛰️"), ("Chiseled Slab", "🪨"), ("Alpine Cloud", "☁️"),
            ("Glacial Ice", "❄️"), ("Pine Spig", "🌲"), ("Falcon Crest", "🦅"), ("Mountain Cairn", "🗿"),
            ("Glacial Stream", "💧"), ("Stone Pillar", "🏛️"), ("Highland Bell", "🔔"), ("Compass Rose", "🧭"),
            ("Gilded Summit", "✨"), ("Silver Lichen Tile", "◽"), ("Radiant Monolith", "🌟"), ("Alpine Crown", "👑")
        ],
        "bg_top": (32, 38, 46), "bg_bot": (16, 20, 26), "radial": (78, 96, 118),
        "rim_type": "platinum", "caustic": (186, 230, 253),
        "emblem_color": (245, 248, 255), "emblem_gleam": (255, 255, 255), "emblem_shadow": (12, 14, 18), "aura_color": (147, 197, 253)
    },
    {
        "id": "sandalwood_teak",
        "chapter": 8,
        "name": "Royal Sandalwood & Teak",
        "subtitle": "Aromatic Carved Sandalwood · Polished Brass",
        "archetype": "leather_tome",
        "audioPreset": "parchment",
        "icon": "🪵",
        "tiles": [
            ("Sandalwood Fan", "🪭"), ("Teak Rosette", "🏵️"), ("Incense Smoke", "💨"), ("Honey Resin", "🍯"),
            ("Carved Elephant", "🐘"), ("Brass Clasp", "🗝️"), ("Aspiration Flame", "🔥"), ("Scented Garland", "📿"),
            ("Teak Pillar", "🏛️"), ("Offering Urn", "🏺"), ("Carved Book", "📖"), ("Warm Diya", "🪔"),
            ("Luminous Sandalwood", "✨"), ("Golden Amber Seal", "🌟"), ("Teak Sunburst", "☀️"), ("Royal Sceptre", "🪄")
        ],
        "bg_top": (46, 26, 14), "bg_bot": (22, 12, 6), "radial": (125, 72, 32),
        "rim_type": "gold_24k", "caustic": (245, 158, 11),
        "emblem_color": (255, 230, 140), "emblem_gleam": (255, 255, 220), "emblem_shadow": (20, 10, 4), "aura_color": (251, 191, 36)
    },
    {
        "id": "midnight_obsidian",
        "chapter": 9,
        "name": "Midnight Obsidian Star",
        "subtitle": "Mirror Jet Obsidian · Laser-Etched Platinum",
        "archetype": "cosmic_glass",
        "audioPreset": "crystal_bell",
        "icon": "🔭",
        "tiles": [
            ("Obsidian Mirror", "🪞"), ("Midnight Star", "⭐"), ("Astrolabe Gear", "⚙️"), ("Telescope Lens", "🔭"),
            ("Crescent Moon", "🌙"), ("Nebula Vortex", "🌀"), ("Cosmic Ray", "⚡"), ("Eclipse Halo", "⭕"),
            ("Starlight Compass", "🧭"), ("Comet Tail", "☄️"), ("Planetary Sphere", "🪐"), ("Diamond Shard", "💎"),
            ("Radiant Obsidian", "✨"), ("Platinum Nova", "🌟"), ("Deep Cosmos", "🌌"), ("Infinity Loop", "♾️")
        ],
        "bg_top": (16, 18, 28), "bg_bot": (6, 8, 14), "radial": (42, 52, 88),
        "rim_type": "platinum", "caustic": (129, 140, 248),
        "emblem_color": (235, 245, 255), "emblem_gleam": (255, 255, 255), "emblem_shadow": (4, 6, 12), "aura_color": (99, 102, 241)
    },
    {
        "id": "tuscan_terracotta",
        "chapter": 10,
        "name": "Tuscan Sunlit Terracotta",
        "subtitle": "Sun-Baked Sienna Clay · Olive Wood Trim",
        "archetype": "terracotta",
        "audioPreset": "clay_pot",
        "icon": "🏺",
        "tiles": [
            ("Tree of Life", "🌳"), ("Clay Amphora", "🏺"), ("Olive Branch", "🫒"), ("Sun-Baked Tile", "🧱"),
            ("Vine Cluster", "🍇"), ("Terracotta Leaf", "🍂"), ("Earthen Basin", "🥣"), ("Hearth Fire", "🔥"),
            ("Wheat Ear", "🌾"), ("Pebble Slab", "🪨"), ("Clay Rosette", "🏵️"), ("Cypress Spire", "🌲"),
            ("Golden Terracotta", "✨"), ("Sunlit Clay Leaf", "🌟"), ("Terra Cameo", "🏵️"), ("Tuscan Crown", "👑")
        ],
        "bg_top": (56, 28, 16), "bg_bot": (28, 12, 6), "radial": (148, 76, 36),
        "rim_type": "copper_gold", "caustic": (249, 115, 22),
        "emblem_color": (255, 225, 170), "emblem_gleam": (255, 250, 220), "emblem_shadow": (26, 10, 4), "aura_color": (245, 158, 11)
    },
    {
        "id": "kyoto_porcelain",
        "chapter": 11,
        "name": "Kyoto White Porcelain",
        "subtitle": "Fine Bone China · Kintsugi Gold Line Repair",
        "archetype": "porcelain_cameo",
        "audioPreset": "birdsong",
        "icon": "🏵️",
        "tiles": [
            ("Porcelain Lotus", "🌸"), ("Kintsugi Golden Vein", "⚡"), ("Cherry Blossom", "🌸"), ("Tea Whisk", "🍵"),
            ("Paper Fan", "🪭"), ("Ceramic Basin", "🥣"), ("Porcelain Bird", "🕊️"), ("Gold Wire Knot", "⚜️"),
            ("Origami Crane", "🦢"), ("Zen Circle", "⭕"), ("Porcelain Pebble", "🤍"), ("Camellia Flower", "🌺"),
            ("Luminous Kintsugi", "✨"), ("Golden Porcelain Cameo", "🌟"), ("Imperial Blossom", "💮"), ("Porcelain Crown", "👑")
        ],
        "bg_top": (28, 30, 36), "bg_bot": (14, 16, 20), "radial": (75, 82, 98),
        "rim_type": "gold_24k", "caustic": (234, 179, 8),
        "emblem_color": (255, 240, 165), "emblem_gleam": (255, 255, 240), "emblem_shadow": (12, 14, 18), "aura_color": (250, 204, 21)
    },
    {
        "id": "rose_alabaster",
        "chapter": 12,
        "name": "Rose Alabaster Colonnade",
        "subtitle": "Translucent Veined Alabaster · Champagne Gold",
        "archetype": "enamel_cameo",
        "audioPreset": "quartz_bowl",
        "icon": "🌸",
        "tiles": [
            ("Alabaster Cameo", "💮"), ("Rose Quartz Gem", "💎"), ("Classical Column", "🏛️"), ("Jasmine Spray", "🌼"),
            ("Champagne Bell", "🔔"), ("Petal Garland", "📿"), ("Fountain Basin", "🥣"), ("Morning Ray", "☀️"),
            ("Garden Rose", "🌹"), ("Blush Petal", "🌸"), ("Carved Arch", "⛩️"), ("Dove of Dawn", "🕊️"),
            ("Radiant Alabaster", "✨"), ("Golden Rose Cameo", "🌟"), ("Sacred Virtues Bloom", "🪷"), ("Alabaster Crown", "👑")
        ],
        "bg_top": (48, 24, 34), "bg_bot": (24, 10, 16), "radial": (128, 62, 92),
        "rim_type": "rose_gold", "caustic": (244, 114, 182),
        "emblem_color": (255, 235, 245), "emblem_gleam": (255, 255, 255), "emblem_shadow": (22, 8, 14), "aura_color": (244, 114, 182)
    },
    {
        "id": "nacre_pearl",
        "chapter": 13,
        "name": "Coromandel Pearlescent Nacre",
        "subtitle": "Iridescent Seashell Nacre · Smoked Walnut Chassis",
        "archetype": "seaglass",
        "audioPreset": "ocean_tide",
        "icon": "🦪",
        "tiles": [
            ("Nacre Cameo", "⚪"), ("Spiral Conch", "🐚"), ("Pearl Drop", "🦪"), ("Tidal Breeze", "💨"),
            ("Smoked Walnut", "🪵"), ("Coral Spray", "🪸"), ("Sea Star Cameo", "⭐"), ("Lagoon Wave", "🌊"),
            ("Glistening Pebble", "🪨"), ("Seagrass Frond", "🌿"), ("Promenade Lamp", "🏮"), ("Deep Shell", "🐚"),
            ("Luminous Pearl", "✨"), ("Golden Nacre Core", "🌟"), ("Iridescent Amulet", "💎"), ("Oceanic Crown", "👑")
        ],
        "bg_top": (18, 44, 52), "bg_bot": (8, 22, 28), "radial": (45, 110, 130),
        "rim_type": "champagne_brass", "caustic": (45, 212, 191),
        "emblem_color": (240, 255, 255), "emblem_gleam": (255, 255, 255), "emblem_shadow": (6, 18, 24), "aura_color": (94, 234, 212)
    },
    {
        "id": "amethyst_geode",
        "chapter": 14,
        "name": "Amethyst Geode Cavern",
        "subtitle": "Raw Purple Amethyst Crystal · Silver Matrix",
        "archetype": "enamel_cameo",
        "audioPreset": "quartz_bowl",
        "icon": "🔮",
        "tiles": [
            ("Amethyst Crystal", "🔮"), ("Violet Geode", "💎"), ("Quartz Point", "✨"), ("Basalt Shard", "🪨"),
            ("Prismatic Ray", "⚡"), ("Crystal Merkaba", "🔯"), ("Chime Bell", "🔔"), ("Cave Lotus", "🪷"),
            ("Deep Vein", "🧬"), ("Luminous Cluster", "🌟"), ("Starlight Drop", "💧"), ("Silver Ribbon", "🎗️"),
            ("Radiant Amethyst", "💫"), ("Violet Nova", "🟣"), ("Geode Rosette", "💮"), ("Amethyst Crown", "👑")
        ],
        "bg_top": (36, 18, 54), "bg_bot": (16, 8, 26), "radial": (105, 48, 155),
        "rim_type": "platinum", "caustic": (192, 132, 252),
        "emblem_color": (250, 235, 255), "emblem_gleam": (255, 255, 255), "emblem_shadow": (18, 6, 28), "aura_color": (168, 85, 247)
    },
    {
        "id": "desert_sandstone",
        "chapter": 15,
        "name": "Sedona Red Sandstone",
        "subtitle": "Wind-Carved Red Sandstone · Sleeping Beauty Turquoise",
        "archetype": "terracotta",
        "audioPreset": "clay_pot",
        "icon": "🏜️",
        "tiles": [
            ("Sandstone Butte", "🏜️"), ("Turquoise Inlay", "💠"), ("Canyon Arch", "⛩️"), ("Sunburst Medallion", "☀️"),
            ("Desert Cactus", "🌵"), ("Wind Ripple", "〰️"), ("Eagle Feather", "🪶"), ("Agave Bloom", "🪴"),
            ("Red Rock Pillar", "🏛️"), ("Pottery Shard", "🏺"), ("Evening Star", "⭐"), ("Desert Campfire", "🔥"),
            ("Golden Sandstone", "✨"), ("Turquoise Solar Seal", "🌟"), ("Canyon Petroglyph", "📜"), ("Sedona Crown", "👑")
        ],
        "bg_top": (62, 24, 18), "bg_bot": (30, 10, 8), "radial": (155, 68, 42),
        "rim_type": "copper_gold", "caustic": (245, 158, 11),
        "emblem_color": (255, 220, 155), "emblem_gleam": (255, 250, 220), "emblem_shadow": (28, 8, 6), "aura_color": (6, 182, 212)
    },
    {
        "id": "river_basalt",
        "chapter": 16,
        "name": "Zen River Basalt",
        "subtitle": "Water-Smoothed Dark Basalt · White Marble Inlays",
        "archetype": "slate_zen",
        "audioPreset": "zen_stone",
        "icon": "🪨",
        "tiles": [
            ("Basalt Pebble", "🪨"), ("White Marble Ring", "⚪"), ("Flowing Water", "🌊"), ("River Moss", "🍃"),
            ("Zen Balance Rock", "🗿"), ("Bamboo Slat", "🎋"), ("Clear Brook", "💧"), ("Iris Flower", "🌺"),
            ("Water Ripple", "〰️"), ("Stone Chime", "🔔"), ("Smooth Slate", "⏹️"), ("Spring Fern", "🌿"),
            ("Radiant River Stone", "✨"), ("Marble Lotus Cameo", "🌟"), ("Zen Stream Seal", "🏵️"), ("Basalt Crown", "👑")
        ],
        "bg_top": (22, 24, 28), "bg_bot": (10, 12, 14), "radial": (58, 64, 76),
        "rim_type": "platinum", "caustic": (148, 163, 184),
        "emblem_color": (240, 245, 250), "emblem_gleam": (255, 255, 255), "emblem_shadow": (8, 10, 12), "aura_color": (203, 213, 225)
    },
    {
        "id": "golden_honeycomb",
        "chapter": 17,
        "name": "Golden Honeycomb & Resin",
        "subtitle": "Warm Beeswax Amber · Meadow Lavender Scent",
        "archetype": "gold_mantra",
        "audioPreset": "deep_drone",
        "icon": "🍯",
        "tiles": [
            ("Honeycomb Hexagon", "🍯"), ("Amber Drop", "💎"), ("Honeybee Wing", "🐝"), ("Wildflower Lavender", "🪻"),
            ("Sunlit Pollen", "☀️"), ("Clover Sprout", "🍀"), ("Beeswax Candle", "🕯️"), ("Clay Honey Pot", "🏺"),
            ("Meadow Grass", "🌾"), ("Sunburst Rosette", "🏵️"), ("Wooden Dipper", "🪵"), ("Pollen Halo", "⭕"),
            ("Luminous Honeycomb", "✨"), ("Golden Bee Sovereign", "🌟"), ("Amber Bloom", "🌺"), ("Honey Crown", "👑")
        ],
        "bg_top": (54, 34, 12), "bg_bot": (26, 16, 6), "radial": (150, 95, 28),
        "rim_type": "gold_24k", "caustic": (245, 158, 11),
        "emblem_color": (255, 235, 140), "emblem_gleam": (255, 255, 220), "emblem_shadow": (24, 14, 4), "aura_color": (234, 179, 8)
    },
    {
        "id": "lapis_lazuli",
        "chapter": 18,
        "name": "Lapis Lazuli Treasury",
        "subtitle": "Royal Ultramarine Lapis Stone · Pyrite Gold Specks",
        "archetype": "cosmic_glass",
        "audioPreset": "crystal_bell",
        "icon": "💠",
        "tiles": [
            ("Lapis Tablet", "🔷"), ("Pyrite Gold Vein", "✨"), ("Starry Vault", "🌌"), ("Vaulted Arch", "🏛️"),
            ("Persian Rosette", "🏵️"), ("Lapis Seal", "💠"), ("Golden Astrolabe", "🧭"), ("Azure Lotus", "🪷"),
            ("Library Scroll", "📜"), ("Midnight Lantern", "🏮"), ("Pyrite Star", "⭐"), ("Sapphire Gem", "💎"),
            ("Radiant Lapis", "🌟"), ("Ultramarine Sunburst", "☀️"), ("Treasury Emblem", "⚜️"), ("Lapis Crown", "👑")
        ],
        "bg_top": (14, 28, 64), "bg_bot": (6, 12, 34), "radial": (36, 75, 170),
        "rim_type": "gold_24k", "caustic": (59, 130, 246),
        "emblem_color": (255, 235, 150), "emblem_gleam": (255, 255, 230), "emblem_shadow": (6, 12, 32), "aura_color": (251, 191, 36)
    },
    {
        "id": "smoked_topaz",
        "chapter": 19,
        "name": "Smoked Topaz & Cognac",
        "subtitle": "Faceted Smoked Topaz Gemstone · Polished Rosewood",
        "archetype": "leather_tome",
        "audioPreset": "parchment",
        "icon": "💎",
        "tiles": [
            ("Smoked Topaz", "💎"), ("Polished Rosewood", "🪵"), ("Hearth Flame", "🔥"), ("Cognac Droplet", "💧"),
            ("Leather Volume", "📕"), ("Brass Clockwork", "🕰️"), ("Vintage Hourglass", "⏳"), ("Faceted Prism", "🔮"),
            ("Topaz Cameo", "🏵️"), ("Aromatic Pipe Wisp", "💨"), ("Reading Spectacles", "👓"), ("Warm Diya", "🪔"),
            ("Luminous Topaz", "✨"), ("Rosewood Sunburst", "🌟"), ("Salon Crest", "⚜️"), ("Topaz Crown", "👑")
        ],
        "bg_top": (44, 22, 14), "bg_bot": (20, 8, 4), "radial": (120, 58, 26),
        "rim_type": "copper_gold", "caustic": (217, 119, 6),
        "emblem_color": (255, 225, 160), "emblem_gleam": (255, 250, 225), "emblem_shadow": (20, 8, 4), "aura_color": (245, 158, 11)
    },
    {
        "id": "celestial_opal",
        "chapter": 20,
        "name": "Celestial Opal Grand Finale",
        "subtitle": "Rainbow Fire Opal · Radiant White Gold Universal Light",
        "archetype": "ivory_wood",
        "audioPreset": "meditation_gong",
        "icon": "🌟",
        "tiles": [
            ("Fire Opal Core", "💎"), ("Rainbow Aurora", "🌈"), ("Universal Light", "☀️"), ("White Jade Tablet", "🤍"),
            ("Lotus Seat", "🪷"), ("Golden Dharma Wheel", "☸️"), ("Temple Bell", "🔔"), ("Peace Dove", "🕊️"),
            ("Radiant Deer", "🦌"), ("Starry Corona", "✨"), ("Prismatic Halo", "⭕"), ("Ascending Helix", "🧬"),
            ("Grand Opal Masterpiece", "🌟"), ("Supreme Sun Star", "☀️"), ("Universal Enlightenment", "✨"), ("Crown of All Realms", "👑")
        ],
        "bg_top": (28, 22, 48), "bg_bot": (12, 8, 24), "radial": (95, 65, 150),
        "rim_type": "gold_24k", "caustic": (236, 72, 153),
        "emblem_color": (255, 245, 180), "emblem_gleam": (255, 255, 240), "emblem_shadow": (14, 8, 22), "aura_color": (244, 114, 182)
    }
]

# Generate 50 Level Names for each theme
def generate_50_levels(theme):
    base = [t[0] for t in theme["tiles"]] # 16 names
    # Add 34 meditative, architectural and serene variants
    prefixes = ["Silent", "Inner", "Deep", "Morning", "Golden", "Ascending", "Pure", "Eternal", "Sacred", "Zenith"]
    suffixes = ["Path", "Gate", "Alcove", "Bower", "Threshold", "Sanctum", "Reflection", "Harmony", "Stillness", "Realization", "Mastery", "Apex"]
    
    levels = list(base)
    idx = 0
    while len(levels) < 50:
        p = prefixes[idx % len(prefixes)]
        s = suffixes[(idx // len(prefixes)) % len(suffixes)]
        stem = base[idx % len(base)]
        candidate = f"{p} {stem} {s}" if len(levels) > 35 else f"{p} {stem}"
        if candidate not in levels:
            levels.append(candidate)
        idx += 1
    # Ensure Level 50 is the Chapter Masterpiece
    levels[49] = f"{theme['name']} Masterpiece"
    return levels[:50]

for t in NEW_20_THEMES:
    t["levelNames"] = generate_50_levels(t)
    assert len(t["levelNames"]) == 50

# 1. Generate Clean Backgrounds and Thumbnails
W, H = 1600, 1000
def make_clean_bg(t):
    img = Image.new("RGBA", (W, H))
    base = np.zeros((H, W, 4), dtype=np.float32)
    tc, bc = t["bg_top"], t["bg_bot"]
    for y in range(H):
        f = y / (H - 1)
        base[y, :, 0] = tc[0] * (1 - f) + bc[0] * f
        base[y, :, 1] = tc[1] * (1 - f) + bc[1] * f
        base[y, :, 2] = tc[2] * (1 - f) + bc[2] * f
        base[y, :, 3] = 255.0
    
    # Radial spotlight
    cx, cy = 800, 480
    y_coords, x_coords = np.ogrid[:H, :W]
    dist = np.sqrt((x_coords - cx) ** 2 + (y_coords - cy) ** 2)
    factor = np.clip(1.0 - (dist / 700.0), 0.0, 1.0)
    factor = factor * factor * (3.0 - 2.0 * factor)
    rc = t["radial"]
    for c in range(3):
        base[:, :, c] = base[:, :, c] * (1.0 - factor * 0.45) + rc[c] * (factor * 0.45)
    
    # Noise
    noise = np.random.normal(0, 12, (H, W)).astype(np.float32)
    for c in range(3):
        base[:, :, c] = np.clip(base[:, :, c] + noise, 0, 255)

    # Vignette
    nx = (x_coords - cx) / (W * 0.55)
    ny = (y_coords - cy) / (H * 0.55)
    vignette = np.clip(1.0 - (np.sqrt(nx ** 2 + ny ** 2) - 0.4) * 0.8, 0.15, 1.0)
    for c in range(3):
        base[:, :, c] *= vignette
    
    arr = np.clip(base, 0, 255).astype(np.uint8)
    img = Image.fromarray(arr, mode="RGBA")
    
    # Add subtle central playing tabletop slab
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    pad_x, pad_y = 140, 90
    box = [pad_x, pad_y, W - pad_x, H - pad_y]
    
    # Drop shadow
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle([box[0]-10, box[1]-6, box[2]+10, box[3]+14], radius=32, fill=(0, 0, 0, 160))
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    img = Image.alpha_composite(img, shadow)
    
    # Table border and fill
    odraw.rounded_rectangle(box, radius=24, fill=(tc[0], tc[1], tc[2], 210), outline=(rc[0], rc[1], rc[2], 220), width=3)
    img = Image.alpha_composite(img, overlay)
    return img

print("Rendering 20 pristine environmental wallpapers & clean thumbnails...")
for t in NEW_20_THEMES:
    bg_img = make_clean_bg(t)
    clean_path = os.path.join(BG_DIR, f"{t['id']}_clean.png")
    bg_path = os.path.join(BG_DIR, f"{t['id']}.png")
    bg_img.save(clean_path, format="PNG", optimize=True)
    bg_img.save(bg_path, format="PNG", optimize=True)
    print(f"  [OK] Saved {clean_path}")

# 2. Render 16 Custom 3D Tiles for Each Theme (20 x 16 = 320 tiles)
TILE_W, TILE_H = 320, 360
font_emoji = None
for fpath in ["C:/Windows/Fonts/seguiemj.ttf", "C:/Windows/Fonts/seguisym.ttf"]:
    if os.path.exists(fpath):
        font_emoji = ImageFont.truetype(fpath, 120)
        break
if font_emoji is None:
    font_emoji = ImageFont.load_default()

def render_3d_tile(t, idx, name, sym):
    img = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Drop shadow
    draw.rounded_rectangle([18, 24, TILE_W - 14, TILE_H - 10], radius=44, fill=(0, 0, 0, 140))
    img = img.filter(ImageFilter.GaussianBlur(10))
    
    # Chassis depth along right and bottom
    chassis = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(chassis)
    cdraw.rounded_rectangle([20, 18, TILE_W - 18, TILE_H - 18], radius=42, fill=(t["bg_bot"][0]//2, t["bg_bot"][1]//2, t["bg_bot"][2]//2, 255))
    img = Image.alpha_composite(img, chassis)
    
    # Metallic beveled rim
    rim_box = [20, 18, TILE_W - 20, TILE_H - 26]
    rim_mask = Image.new("L", (TILE_W, TILE_H), 0)
    rm_draw = ImageDraw.Draw(rim_mask)
    rm_draw.rounded_rectangle(rim_box, radius=42, fill=255)
    
    gold_grad = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(gold_grad)
    for y in range(rim_box[1], rim_box[3]):
        frac = (y - rim_box[1]) / (rim_box[3] - rim_box[1])
        c = t["emblem_gleam"] if frac < 0.2 else (t["radial"] if frac < 0.6 else t["bg_bot"])
        g_draw.line([(0, y), (TILE_W, y)], fill=c + (255,))
    
    rim_layer = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    rim_layer.paste(gold_grad, (0, 0), rim_mask)
    img = Image.alpha_composite(img, rim_layer)
    
    # Inner Jewel / Material Glass Slab
    glass_box = [26, 24, TILE_W - 26, TILE_H - 32]
    glass_mask = Image.new("L", (TILE_W, TILE_H), 0)
    gm_draw = ImageDraw.Draw(glass_mask)
    gm_draw.rounded_rectangle(glass_box, radius=36, fill=255)
    
    glass_grad = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    gg_draw = ImageDraw.Draw(glass_grad)
    for y in range(glass_box[1], glass_box[3]):
        frac = (y - glass_box[1]) / (glass_box[3] - glass_box[1])
        r = int(t["bg_top"][0] * (1 - frac) + t["bg_bot"][0] * frac)
        g = int(t["bg_top"][1] * (1 - frac) + t["bg_bot"][1] * frac)
        b = int(t["bg_top"][2] * (1 - frac) + t["bg_bot"][2] * frac)
        gg_draw.line([(0, y), (TILE_W, y)], fill=(r, g, b, 255))
    
    # Caustic radial spotlight
    caustic = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(caustic)
    cx, cy = TILE_W // 2, int(glass_box[1] + (glass_box[3] - glass_box[1]) * 0.45)
    for r in range(100, 0, -8):
        alpha = int(60 * (1 - r / 100))
        cdraw.ellipse([cx - r * 1.15, cy - r * 0.85, cx + r * 1.15, cy + r * 0.85], fill=t["caustic"] + (alpha,))
    glass_grad = Image.alpha_composite(glass_grad, caustic)
    
    glass_layer = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    glass_layer.paste(glass_grad, (0, 0), glass_mask)
    img = Image.alpha_composite(img, glass_layer)
    
    # Gloss reflection top bubble
    gloss = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    gldraw = ImageDraw.Draw(gloss)
    gldraw.rounded_rectangle([32, 28, int(TILE_W * 0.68), int(TILE_H * 0.28)], radius=24, fill=(255, 255, 255, 55))
    gloss = gloss.filter(ImageFilter.GaussianBlur(8))
    gloss_layer = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    gloss_layer.paste(gloss, (0, 0), glass_mask)
    img = Image.alpha_composite(img, gloss_layer)
    
    # 3D Embossed Emblem
    draw = ImageDraw.Draw(img)
    bbox = draw.textbbox((0, 0), sym, font=font_emoji)
    sym_x = (TILE_W - (bbox[2] + bbox[0])) // 2
    sym_y = (TILE_H - (bbox[3] + bbox[1])) // 2 - 4
    
    # Shadow
    draw.text((sym_x + 3, sym_y + 4), sym, font=font_emoji, fill=t["emblem_shadow"] + (230,))
    # Aura
    aura = Image.new("RGBA", (TILE_W, TILE_H), (0, 0, 0, 0))
    adraw = ImageDraw.Draw(aura)
    adraw.text((sym_x, sym_y), sym, font=font_emoji, fill=t["aura_color"] + (180,))
    aura = aura.filter(ImageFilter.GaussianBlur(10))
    img = Image.alpha_composite(img, aura)
    
    # Main symbol body
    draw = ImageDraw.Draw(img)
    draw.text((sym_x, sym_y), sym, font=font_emoji, fill=t["emblem_color"] + (255,))
    draw.text((sym_x - 1, sym_y - 2), sym, font=font_emoji, fill=t["emblem_gleam"] + (160,))
    return img

print("Rendering 320 custom 3D tiles for all 20 themes...")
for t in NEW_20_THEMES:
    t_dir = os.path.join(THEME_DIR, t["id"])
    os.makedirs(t_dir, exist_ok=True)
    for idx, (tname, tsym) in enumerate(t["tiles"], start=1):
        tile_img = render_3d_tile(t, idx, tname, tsym)
        out_f = os.path.join(t_dir, f"tile_{idx:02d}.png")
        tile_img.save(out_f, format="PNG", optimize=True)
    print(f"  [OK] Generated 16 tiles for {t['name']} ({t['id']})")

# 3. Generate themeManager.js
js_code = """// ThemeManager: Manages the 20 Secular Realms Grand Campaign (1,000 Total Thematic Levels)
// Coordinates clean background wallpapers, authentic 3D tactile tile skins, and audio presets.

export const TOTAL_REALM_LEVELS = 1000; // 20 Themes * 50 Levels per Theme
export const LEVELS_PER_REALM = 50;
export const TOTAL_CLASSIC_LEVELS = 200; // Dedicated Classic Solitaire Campaign

// 16 distinct emblems with symbolic labels for each of the 20 themes
const THEME_TILE_DEFS = {
"""

for t in NEW_20_THEMES:
    js_code += f'  "{t["id"]}": [\n'
    for name, sym in t["tiles"]:
        js_code += f'    {{ name: "{name}", symbol: "{sym}" }},\n'
    js_code += '  ],\n'

js_code += """};

function buildCustomTilesForTheme(themeId) {
  const defs = THEME_TILE_DEFS[themeId] || THEME_TILE_DEFS.kyoto_bamboo;
  return defs.map((d, idx) => ({
    name: d.name,
    image: `./Assets/themes/${themeId}/tile_${String(idx + 1).padStart(2, '0')}.png`,
    symbol: d.symbol
  }));
}

export const REALMS = [
"""

for t in NEW_20_THEMES:
    lvl_start = (t["chapter"] - 1) * 50 + 1
    lvl_end = t["chapter"] * 50
    level_names_json = json.dumps(t["levelNames"], indent=6)
    
    js_code += f"""  {{
    id: '{t["id"]}',
    chapter: {t["chapter"]},
    name: '{t["name"]}',
    subtitle: '{t["subtitle"]}',
    mockupImage: './Assets/backgrounds/{t["id"]}_clean.png',
    bgImage: './Assets/backgrounds/{t["id"]}_clean.png',
    archetype: '{t["archetype"]}',
    audioPreset: '{t["audioPreset"]}',
    levelStart: {lvl_start},
    levelEnd: {lvl_end},
    icon: '{t["icon"]}',
    levelNames: {level_names_json},
    customTiles: buildCustomTilesForTheme('{t["id"]}')
  }},
"""

js_code += """
];

export class ThemeManager {
  /**
   * Retrieves the active Realm definition for any level (1 - 1000)
   */
  static getRealmForLevel(levelNum = 1) {
    const safeLevel = Math.max(1, Math.min(TOTAL_REALM_LEVELS, levelNum));
    const realmIdx = Math.floor((safeLevel - 1) / LEVELS_PER_REALM) % REALMS.length;
    const realm = REALMS[realmIdx];
    const levelInRealm = ((safeLevel - 1) % LEVELS_PER_REALM) + 1;
    const levelName = (realm.levelNames && realm.levelNames[levelInRealm - 1]) 
      ? realm.levelNames[levelInRealm - 1] 
      : `Level ${levelInRealm}`;

    return {
      ...realm,
      currentLevel: safeLevel,
      levelInRealm,
      levelName,
      isMasterArtLevel: true, // In Realms mode, all 50 levels feature authentic dedicated art tiles
      masterLevelIndex: levelInRealm,
      classicLevelIndex: null,
      isFirstInRealm: levelInRealm === 1,
      isLastInRealm: levelInRealm === LEVELS_PER_REALM
    };
  }

  /**
   * Returns list of all 20 secular realms for the visual Realm Browser carousel
   */
  static getAllRealms() {
    return REALMS;
  }

  /**
   * Check if a specific realm is unlocked based on player's highest completed/current level
   * Chapter 1 is always unlocked. Chapter N is unlocked if player has reached or passed levelStart.
   */
  static isRealmUnlocked(realmId, playerCurrentLevel = 1) {
    const realm = REALMS.find(r => r.id === realmId);
    if (!realm) return false;
    if (realm.chapter === 1) return true;
    return playerCurrentLevel >= realm.levelStart;
  }

  /**
   * Returns progression statistics for a realm:
   * { completedLevels, totalLevels: 50, percent, isCompleted }
   */
  static getRealmProgress(realmId, playerCurrentLevel = 1) {
    const realm = REALMS.find(r => r.id === realmId);
    if (!realm) return { completedLevels: 0, totalLevels: 50, percent: 0, isCompleted: false };
    
    if (playerCurrentLevel <= realm.levelStart) {
      return { completedLevels: 0, totalLevels: 50, percent: 0, isCompleted: false };
    }
    if (playerCurrentLevel > realm.levelEnd) {
      return { completedLevels: 50, totalLevels: 50, percent: 100, isCompleted: true };
    }
    const completed = playerCurrentLevel - realm.levelStart;
    return {
      completedLevels: completed,
      totalLevels: 50,
      percent: Math.round((completed / 50) * 100),
      isCompleted: false
    };
  }
}
"""

with open("src/controllers/themeManager.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("src/controllers/themeManager.js generated with 20 BRAND NEW THEMES!")
