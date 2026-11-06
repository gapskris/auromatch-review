# Build ThemeManager for 20 Themes & 1000 Levels
import os
import json

THEMES_DATA = [
    {
        "id": "whispering_pines",
        "chapter": 1,
        "name": "Service Tree Sanctuary",
        "subtitle": "Psychic Aspiration · Service Tree Canopy",
        "bgImage": "./Assets/backgrounds/whispering_pines_clean.png",
        "archetype": "bark_leaf",
        "audioPreset": "forest",
        "icon": "🌲",
        "tiles": [
            ("Rough Bark", "🪵"), ("Growth Rings", "🪵"), ("Burl Grain", "🪵"), ("Walnut Slab", "🪵"),
            ("Service Leaf", "🍃"), ("Birch Leaf", "🌿"), ("Fern Frond", "🌿"), ("Clover Sprout", "☘️"),
            ("Woodland Pinecone", "🌲"), ("Forest Acorn", "🌰"), ("Wild Berries", "🍒"), ("Maple Samara", "🍁"),
            ("Golden Sunlit Leaf", "✨"), ("Golden Tree of Life", "🌟"), ("Mossy Bark Slab", "🍃"), ("Autumn Oak Leaf", "🍂")
        ],
        "base_words": [
            "Aspiration", "Receptivity", "Faith", "Surrender", "Trust", "Sincerity", "Peace", "Joy",
            "Silent Canopy", "Anchor Roots", "Sunlit Foliage", "Inner Bark", "Sap Flow", "Golden Blossom",
            "Psychic Center", "Forest Breeze", "Morning Dew", "Cedar Whispers", "Pines Harmony", "Lichen Stone",
            "Verdant Glade", "Emerald Canopy", "Deep Woodland", "Sunbeam Pathway", "Rooted Strength", "Spring Sprout",
            "Birch Grove", "Ancient Timber", "Serene Arbor", "Green Sanctum", "Mossy Pathway", "Quiet Grove",
            "Pinecone Hearth", "Gentle Rain", "Dappled Shade", "Forest Solitude", "Whispering Frond", "Woodland Trail",
            "Clear Stream", "Golden Dawn", "Canopy Arch", "Pines Symphony", "Spiritual Grove", "Living Wood",
            "Verdant Peace", "Sacred Canopy", "Ancient Sentinel", "Psychic Dawn", "Sanctuary Core", "Service Tree Realization"
        ]
    },
    {
        "id": "temple_of_lines",
        "chapter": 2,
        "name": "Golconde Modernist Slate",
        "subtitle": "Modernist Harmony · Minimalist Slate",
        "bgImage": "./Assets/backgrounds/temple_of_lines_clean.png",
        "archetype": "slate_zen",
        "audioPreset": "zen_stone",
        "icon": "🏛️",
        "tiles": [
            ("Louver Slats", "🏛️"), ("Concentric Squares", "⏹️"), ("Linear Fluting", "🏛️"), ("Modernist Arch", "⛩️"),
            ("Water Ripples", "〰️"), ("Zen River Pebble", "🪨"), ("Bamboo Stalks", "🎋"), ("Slate Water Lily", "🪷"),
            ("Cross-Hair Grid", "➕"), ("Fibonacci Spiral", "🌀"), ("Diamond Tessellation", "💠"), ("Orthogonal Planes", "📐"),
            ("Gilded Inlay Slate", "✨"), ("Amber Sunbeam Slate", "☀️"), ("White Marble Inset", "◽"), ("Moss Patina Slate", "🍃")
        ],
        "base_words": [
            "Symmetry", "Silence", "Light", "Utility", "Cleanliness", "Harmony", "Perfection", "Peace",
            "Monolithic Louvers", "Sun Angles", "Zen Corridors", "Lily Pond", "Polished Stone", "Exposed Slate",
            "Architectural Line", "Geometric Order", "Shadow Grille", "Aero Louver", "Balance Point", "Quiet Portico",
            "Cantilever Beam", "Slate Threshold", "Minimalist Cube", "Linear Axis", "Concrete Matrix", "Zen Terrace",
            "Golden Proportion", "Zen Basin", "Modernist Vault", "Harmonic Ratio", "Pure Plane", "Louvered Dusk",
            "Reflecting Surface", "Structured Stillness", "Modernist Void", "Acoustic Silence", "Zen Garden Walk", "Slate Pillar",
            "Clean Horizon", "Modernist Purity", "Chiseled Balance", "Pure Geometry", "Quiet Rhythm", "Linear Echo",
            "Modernist Sanctuary", "Monolith Wall", "Geometric Dawn", "Slate Mastery", "Architectural Apex", "Perfection of Line"
        ]
    },
    {
        "id": "biblios_wisdom",
        "chapter": 3,
        "name": "SABDA Wisdom Library",
        "subtitle": "Concentration of Wisdom · Antique Tomes & Gilt",
        "bgImage": "./Assets/backgrounds/biblios_wisdom_clean.png",
        "archetype": "leather_tome",
        "audioPreset": "parchment",
        "icon": "📚",
        "tiles": [
            ("Burgundy Tome", "📕"), ("Navy Gilded Spine", "📘"), ("Forest Green Ledger", "📗"), ("Calfskin Book", "📙"),
            ("Golden Quill", "🪶"), ("Crystal Inkwell", "🖋️"), ("Tied Scroll", "📜"), ("Reading Glasses", "👓"),
            ("Glowing Oil Lamp", "🪔"), ("Pendulum Clock", "🕰️"), ("Open Codex", "📖"), ("Tassel Bookmark", "🔖"),
            ("Illuminated Folio", "🌟"), ("Tree of Wisdom", "🌳"), ("Marbled Folio", "📑"), ("Golden Lotus Book", "🪷")
        ],
        "base_words": [
            "Life Divine", "Synthesis", "Illumination", "Inner Knowledge", "Divine Surrender", "Higher Mind", "Words of Light", "Essays of Truth",
            "Gilded Owl", "Feather Quill", "Open Codex", "Celestial Astrolabe", "Hourglass", "Illuminated Verse", "Wisdom Crown",
            "Teak Bookcase", "Sanskrit Stanza", "Leather Tome", "Ancient Folio", "Scriptorium", "Scripture Chamber", "Luminous Scroll",
            "Golden Margins", "Ink of Truth", "Vellum Sheet", "Library Alcove", "Vaulted Teak", "Archival Solitude", "Deep Inquiry",
            "Bound Wisdom", "Eternal Verse", "Philosopher Desk", "Concentration Chamber", "Silent Reader", "Gilded Calligraphy", "Cosmic Dialectic",
            "Mind of Light", "Scholarly Lamp", "Rare Manuscript", "Book of Aspiration", "Wisdom Pillar", "Inscribed Tablet", "Codex of Peace",
            "Archive of Silence", "Teak Gallery", "Luminous Chapter", "Eternal Knowledge", "Crown of Wisdom", "Master Scriptorium", "SABDA Realization"
        ]
    },
    {
        "id": "celestial_starlight",
        "chapter": 4,
        "name": "Aquamarine Celestial Glass",
        "subtitle": "Luminous Glass · Refractive Crystal & Gold",
        "bgImage": "./Assets/backgrounds/celestial_starlight_clean.png",
        "archetype": "cosmic_glass",
        "audioPreset": "crystal_bell",
        "icon": "✨",
        "tiles": [
            ("Cosmic Star", "✨"), ("Aquamarine Tablet", "💎"), ("Crescent Moon", "🌙"), ("Solar Crest", "☀️"),
            ("Polaris Compass", "🧭"), ("Comet Trail", "☄️"), ("Saturn Ring", "🪐"), ("Astral Orbit", "💫"),
            ("Radiant Nova", "🌟"), ("Starlight Crown", "👑"), ("Crystal Prism", "🔮"), ("Eclipse Ring", "⭕"),
            ("Zodiac Rune", "♈"), ("Zenith Spark", "⚡"), ("Cosmic Bell", "🔔"), ("Infinity Spiral", "♾️")
        ],
        "base_words": [
            "Cosmic Star", "Aquamarine Prism", "Crescent Moon", "Solar Corona", "Polaris Compass", "Comet Tail", "Saturn Rings", "Astral Orbit",
            "Radiant Nova", "Starlight Crown", "Crystal Merkaba", "Eclipse Halo", "Zodiac Sign", "Zenith Spark", "Transcendental Light",
            "Refractive Glass", "Cyan Core", "Golden Bevel", "Prismatic Shard", "Astral Beacon", "Starlight Ray", "Cosmic Dust",
            "Deep Orbit", "Celestial Lens", "Astral Meridian", "Stellar Mirror", "Luminous Zenith", "Aquamarine Sphere", "Cosmic Nebula",
            "Starlight Cascade", "Supercluster", "Gleaming Prism", "Solar Flare", "Celestial Compass", "Vibrant Ray", "Astral Sanctuary",
            "Infinite Cosmos", "Stellar Echo", "Planetary Arc", "Glacial Starlight", "Refractive Wave", "Cosmic Halo", "Astral Portal",
            "Golden Constellation", "Celestial Harmony", "Starlight Monolith", "Cosmic Dawn", "Prismatic Apex", "Transcendence", "Eternal Starlight"
        ]
    },
    {
        "id": "golden_nebula",
        "chapter": 5,
        "name": "Molten Amber Nebula",
        "subtitle": "Honey-Amber Resin · Obsidian Stellar Forge",
        "bgImage": "./Assets/backgrounds/golden_nebula_clean.png",
        "archetype": "gold_mantra",
        "audioPreset": "deep_drone",
        "icon": "🌌",
        "tiles": [
            ("Luminous Rune", "💫"), ("Golden Tablet", "🌟"), ("Solar Flare", "☀️"), ("Nebula Spiral", "🌀"),
            ("Gold Constellation", "✨"), ("Supernova", "💥"), ("Galaxy Disc", "🌌"), ("Astral Gateway", "⛩️"),
            ("Golden Lotus", "🪷"), ("Radiant Phoenix", "🦅"), ("Cosmic Eye", "👁️"), ("Golden Sceptre", "🪄"),
            ("Eclipse Sun", "🌕"), ("Astral Hourglass", "⏳"), ("Star Chime", "🔔"), ("Celestial Crown", "👑")
        ],
        "base_words": [
            "Solar Eclipse", "Radiant Sunburst", "Amber Meteorite", "Concentric Orbits", "Sacred Lines", "Metatron Cube", "Torus Field", "Flower of Life",
            "Orion Stars", "Nebula Vortex", "Amber Sphere", "Celestial Phoenix", "Molten Gold Core", "Lotus Heart", "Supreme Radiance",
            "Obsidian Slab", "Amber Resin", "Golden Flare", "Stellar Forge", "Cosmic Fusion", "Honey Corona", "Deep Nebula",
            "Astral Ring", "Golden Dust", "Plasma Stream", "Solar Filament", "Amber Chime", "Celestial Crucible", "Stellar Nursery",
            "Molten Filament", "Nebular Halo", "Golden Core", "Astral Pulse", "Magnetic Wave", "Starlight Crucible", "Amber Horizon",
            "Golden Vortex", "Obsidian Spark", "Radiant Matrix", "Solar Forge", "Celestial Crown", "Golden Filament", "Nebular Dawn",
            "Amber Infinity", "Cosmic Flare", "Golden Genesis", "Stellar Apex", "Supreme Forge", "Molten Zenith", "Nebular Mastery"
        ]
    },
    {
        "id": "spirit_altar",
        "chapter": 6,
        "name": "Brass Altar & Sacred Flame",
        "subtitle": "Hammered Antique Brass · Sacred Offering",
        "bgImage": "./Assets/backgrounds/spirit_altar_clean.png",
        "archetype": "marble_altar",
        "audioPreset": "bronze_bell",
        "icon": "🕯️",
        "tiles": [
            ("Marble Lotus", "🪷"), ("Marble Rosette", "🏵️"), ("Concentric Mandala", "💮"), ("Bodhi Leaf", "🍃"),
            ("Meditation Flame", "🔥"), ("Bronze Chime", "🔔"), ("Incense Censer", "🪔"), ("Offering Bowl", "🥣"),
            ("Sacred Conch", "🐚"), ("Endless Knot", "♾️"), ("White Jasmine", "🌼"), ("Water Lily", "🪷"),
            ("Golden Vessel", "🏺"), ("Spiritual Halo", "⭕"), ("Temple Camellia", "🌺"), ("Serene Pearl", "🤍")
        ],
        "base_words": [
            "White Marble", "Incense Burner", "Flame of Offering", "Brass Censer", "Consecration Smoke", "Aspiration Fire", "Sacred Camphor", "Altar Lamp",
            "Temple Bell", "Brass Platter", "Sandalwood Paste", "Sacred Ash", "Pure Aspiration", "Surrender Hearth", "Eternal Flame",
            "Bronze Diya", "Hammered Urn", "Marble Basin", "Consecrated Petal", "Fragrant Smoke", "Altar Stone", "Sacred Wick",
            "Offering Chalice", "Bronze Halo", "Altar Scriptorium", "Temple Threshold", "Incense Trail", "Sanctuary Bell", "Inner Flame",
            "Consecrated Hearth", "Bronze Petal", "Marble Inlay", "Aspiration Pillar", "Sacred Resonator", "Altar Veil", "Temple Gong",
            "Pure Consecration", "Sacred Embers", "Bronze Lantern", "Offering Table", "Flame of Light", "Incense Bower", "Sanctuary Hearth",
            "Eternal Lamp", "Sacred Platform", "Altar Zenith", "Flame of Peace", "Golden Camphor", "Temple Altar Apex", "Sacred Flame Realization"
        ]
    },
    {
        "id": "sacred_sanctuary",
        "chapter": 7,
        "name": "Sacred Teak Shrine",
        "subtitle": "Dark Teak Wood · Chiseled Brass Lotus Medallions",
        "bgImage": "./Assets/backgrounds/sacred_sanctuary_clean.png",
        "archetype": "brass_lotus",
        "audioPreset": "singing_bowl",
        "icon": "🪷",
        "tiles": [
            ("Chiseled Lotus", "🪷"), ("Brass Rosette", "🏵️"), ("Sanctuary Flame", "🔥"), ("Golden Bell", "🔔"),
            ("Temple Pillar", "🏛️"), ("Incense Mist", "💨"), ("Amber Jewel", "💎"), ("Sacred Garland", "📿"),
            ("Solar Disk", "☀️"), ("Peace Dove", "🕊️"), ("Temple Gateway", "⛩️"), ("Vessel of Light", "🏺"),
            ("Radiant Chime", "🎐"), ("Aura Halo", "⭕"), ("Golden Leaf", "🍂"), ("Eternal Lamp", "🪔")
        ],
        "base_words": [
            "Dark Teak Altar", "Brass Lotus", "Singing Bowl", "Incense Mist", "Sacred Garland", "Diya Glow", "Chiseled Pedestal", "Conch Echo",
            "Meditation Cushion", "Temple Pillar", "Silent Vigil", "Sacred Offering", "Devotional Heart", "Inner Chamber", "Divine Grace",
            "Teak Lattice", "Brass Medallion", "Carved Cornice", "Shrine Door", "Sanctuary Lantern", "Sacred Drapery", "Teak Threshold",
            "Brass Finial", "Sanctuary Bench", "Floral Rosette", "Shrine Bell", "Temple Vault", "Silent Portico", "Carved Teak Column",
            "Shrine Basin", "Golden Garland", "Incense Wisp", "Sacred Aisle", "Devotional Hearth", "Carved Archway", "Teak Balustrade",
            "Brass Diya Stand", "Sanctuary Terrace", "Shrine Solitude", "Quiet Courtyard", "Carved Medallion", "Sacred Teak Arch", "Shrine Light",
            "Inner Sanctum Walk", "Teak Sanctuary Apex", "Shrine Awakening", "Peace of the Teak", "Sacred Chamber", "Shrine Realization", "Eternal Teak Shrine"
        ]
    },
    {
        "id": "ocean_horizon",
        "chapter": 8,
        "name": "Coromandel Coastline",
        "subtitle": "The Infinite Ocean · Seaglass & Pearlescent Shell",
        "bgImage": "./Assets/backgrounds/ocean_horizon_clean.png",
        "archetype": "seaglass",
        "audioPreset": "ocean_tide",
        "icon": "🌊",
        "tiles": [
            ("Azure Bubble", "🫧"), ("Luminous Pearl", "⚪"), ("Nautilus Shell", "🐚"), ("Sea Star", "⭐"),
            ("Ocean Wave", "🌊"), ("Coral Branch", "🪸"), ("Driftwood Tablet", "🪵"), ("Dolphin Crest", "🐬"),
            ("Tide Compass", "🧭"), ("Deep Lagoon", "💧"), ("Sea Anemone", "🌸"), ("Ambergris Gem", "💎"),
            ("Coastal Breeze", "💨"), ("Lighthouse Lamp", "🏮"), ("Seagrass Frond", "🌿"), ("Sunken Coin", "🪙")
        ],
        "base_words": [
            "Vastness", "Quietude", "Depth", "Calm", "Tide", "Wave", "Flow", "Reflection",
            "Frosted Seaglass", "Promenade Rocks", "Pearlescent Shell", "Nautilus Spiral", "Horizon Light", "Ocean Beacon", "Infinite Silence",
            "Seaside Dawn", "Granite Boulders", "Salty Mist", "Foaming Crest", "Aquamarine Tide", "Coastal Twilight", "Coral Garden",
            "Marine Horizon", "Ocean Breeze", "Promenade Walk", "Pastel Dusk", "Deep Swell", "Shell Harbor", "Tidal Solitude",
            "Shoreline Rhythm", "Sea Spray", "Infinite Blue", "Oceanic Stillness", "Granite Pier", "Tidepool Gem", "Azure Calm",
            "Coastal Lighthouse", "Seaglass Pebble", "Dusk Horizon", "Rolling Breaker", "Pacific Calm", "Marine Sanctuary", "Oceanic Peace",
            "Promenade Beacon", "Deep Trench", "Vast Ocean Horizon", "Tide Harmony", "Endless Sea", "Oceanic Apex", "Coromandel Realization"
        ]
    },
    {
        "id": "terracotta_earth",
        "chapter": 9,
        "name": "Ancient Terracotta Banyan",
        "subtitle": "Unified Ground · Baked Terracotta Clay",
        "bgImage": "./Assets/backgrounds/terracotta_earth_clean.png",
        "archetype": "terracotta",
        "audioPreset": "clay_pot",
        "icon": "🏺",
        "tiles": [
            ("Tree of Life", "🌳"), ("Banyan Spray", "🍃"), ("Five-Leaf Fan", "🌿"), ("Celtic Knot", "🏵️"),
            ("Trinity Triquetra", "☘️"), ("Sacred Spiral", "🌀"), ("Ancient Seedling", "🌱"), ("Sanctuary Arch", "⛩️"),
            ("Lotus Fleur", "🪷"), ("Vine Weave", "♾️"), ("Solar Rosette", "☀️"), ("Clay Amphora", "🏺"),
            ("Golden Tree", "✨"), ("Luminous Leaf", "🌟"), ("Radiant Triquetra", "💫"), ("Moss Patina Leaf", "🍃")
        ],
        "base_words": [
            "Harmony", "Peace", "Brotherhood", "Collaboration", "Goodwill", "Sympathy", "Oneness", "Tree of Life",
            "Aerial Roots", "Vast Canopy", "Triquetra Knot", "Ancient Soil", "Sprouting Seedling", "Emerald Patina", "Unified Presence",
            "Sun-Baked Clay", "Red Terracotta", "Potter Wheel", "Earth Basin", "Clay Tablet", "Deep Roots", "Earthy Warmth",
            "Ancient Grove", "Terracotta Pillar", "Root Lattice", "Clay Amphora", "Living Banyan", "Earth Sanctuary", "Soil of Unity",
            "Carved Clay Tile", "Red Ochre Soil", "Banyan Shade", "Terracotta Fleur", "Grounded Peace", "Clay Vessel", "Ancient Trunk",
            "Lichen on Clay", "Terracotta Hearth", "Banyan Courtyard", "Clay Sunburst", "Rooted Harmony", "Porous Clay", "Earthen Sanctum",
            "Terracotta Archway", "Living Soil", "Ancient Wisdom Tree", "Terracotta Apex", "Eternal Roots", "Master Terracotta", "Banyan Realization"
        ]
    },
    {
        "id": "floral_harmony",
        "chapter": 10,
        "name": "Twelve Sacred Petals",
        "subtitle": "Concentric Virtues · Botanical Porcelain & Quartz",
        "bgImage": "./Assets/backgrounds/floral_harmony_clean.png",
        "archetype": "enamel_cameo",
        "audioPreset": "quartz_bowl",
        "icon": "🌸",
        "tiles": [
            ("Lotus Cameo", "🪷"), ("Rose Cameo", "🌹"), ("Magnolia Blossom", "🌸"), ("Orchid Sprig", "🌺"),
            ("Peony Crown", "🏵️"), ("Jasmine Garland", "🌼"), ("Tulip Cup", "🌷"), ("Sunflower Crest", "🌻"),
            ("Lavender Scent", "🪻"), ("Iris Blade", "🌿"), ("Blush Cameo", "💮"), ("Garden Butterfly", "🦋"),
            ("Honey Blossom", "🍯"), ("Morning Dew", "💧"), ("Cameo Brooch", "💎"), ("Pearl Petal", "🤍")
        ],
        "base_words": [
            "Sincerity", "Humility", "Gratitude", "Perseverance", "Aspiration", "Receptivity", "Progress", "Courage",
            "Goodness", "Generosity", "Equality", "Peace", "Harmony", "Perfection", "Supreme Grace",
            "Rose Quartz Cameo", "Blush Petal", "Concentric Walk", "Magnolia Spray", "Orchid Terrace", "Floral Aisle", "Jasmine Bower",
            "Lavender Breeze", "Iris Crest", "Botanical Crown", "Garden Harmony", "Fragrant Bloom", "Cameo Brooch", "Petal Circle",
            "Enamel Blossom", "Dewy Morning", "Porcelain Cameo", "Floral Medallion", "Twelve Virtues Walk", "Petal Sanctuary", "Sacred Blossom",
            "Radiant Cameo", "Garden of Peace", "Rose Petal Path", "Quartz Basin", "Floral Aspiration", "Harmonic Bloom", "Concentric Petals",
            "Virtue of Truth", "Blossom Arch", "Garden Apex", "Petal Realization", "Crown of Flowers", "Twelve Petals Sanctuary", "Eternal Floral Harmony"
        ]
    },
    {
        "id": "blooming_mandala",
        "chapter": 11,
        "name": "Enameled Porcelain Mandala",
        "subtitle": "Concentric Harmony · High-Gloss Porcelain & Gold Wire",
        "bgImage": "./Assets/backgrounds/blooming_mandala_clean.png",
        "archetype": "porcelain_cameo",
        "audioPreset": "birdsong",
        "icon": "🏵️",
        "tiles": [
            ("Porcelain Lotus", "🌸"), ("Gold Cameo", "🏵️"), ("Concentric Ring", "⭕"), ("Radial Star", "✳️"),
            ("Mandala Hub", "💮"), ("Filigree Petal", "🪷"), ("Sacred Wheel", "☸️"), ("Porcelain Rose", "🌹"),
            ("Gold Wire Crest", "⚜️"), ("Sunburst Halo", "☀️"), ("Lace Mandala", "🕸️"), ("Imperial Brocade", "👑"),
            ("Celestial Rosette", "🌟"), ("Ivory Cameo", "🤍"), ("Radiant Bloom", "🌺"), ("Geometric Jewel", "💎")
        ],
        "base_words": [
            "Central Crystal", "Inner Ring", "Twelve Petals", "Concentric Blossom", "Golden Axis", "Watercolor Bloom", "Floral Pathway", "Sacred Orbit",
            "Porcelain Rosette", "Lapis Inlay", "Radiant Aureole", "Petal Symmetry", "Geometric Dance", "Celestial Bloom", "Integral Mandala",
            "Ivory Porcelain", "Gold Wire Clasp", "High-Gloss Glaze", "Ceramic Lotus", "Mandala Core", "Radial Filigree", "Enamel Crest",
            "Porcelain Wheel", "Gilded Rosette", "Circular Solitude", "Ceramic Basin", "Mandala Terrace", "Ivory Cameo Ring", "Concentric Calm",
            "Enamel Petal", "Gold Wire Symmetry", "Porcelain Medallion", "Mandala Center", "Ceramic Mandala Walk", "Radial Harmony", "Enamel Rosette",
            "Gold Wire Lace", "Porcelain Bloom", "Mandala Solitude", "Celestial Porcelain", "Concentric Apex", "Radial Balance", "Ivory Harmony",
            "Enamel Lotus", "Sacred Porcelain Wheel", "Mandala Crown", "Porcelain Mastery", "Concentric Realization", "Mandala Apex", "Eternal Porcelain Mandala"
        ]
    },
    {
        "id": "sacred_spiral",
        "chapter": 12,
        "name": "Sacred Spiral Mandala",
        "subtitle": "Evolutionary Ascent · Imperial Jade & Bronze Filigree",
        "bgImage": "./Assets/backgrounds/sacred_spiral_clean.png",
        "archetype": "spiral_vine",
        "audioPreset": "bansuri_flute",
        "icon": "🌿",
        "tiles": [
            ("Golden Vine", "🌿"), ("Sacred Bloom", "🪷"), ("Fibonacci Spiral", "🌀"), ("Fern Sprout", "🌱"),
            ("Spiral Shell", "🐚"), ("Curled Tendril", "🌾"), ("Helix Crest", "🧬"), ("Emerald Jewel", "💎"),
            ("Sunlit Canopy", "🌳"), ("Verdant Clover", "🍀"), ("Botanical Orbit", "💫"), ("Forest Fern", "🌿"),
            ("Twisting Branch", "🪵"), ("Dewdrop Frond", "💧"), ("Spiral Galaxy", "🌌"), ("Verdant Crown", "👑")
        ],
        "base_words": [
            "Golden Spiral", "Vine of Ascent", "Sacred Vortex", "Evolutionary Curve", "Fibonacci Coil", "Celestial Swirl", "Dynamic Spiral", "Center of Force",
            "Ascending Helix", "Spiral Orbit", "Golden Filigree", "Transformation Gyre", "Cosmic Evolution", "Radiant Core", "Crown of Ascent",
            "Jade Helix", "Bronze Filigree", "Curling Tendril", "Verdant Gyre", "Spiral Path", "Emerald Coil", "Botanical Vortex",
            "Nautilus Curve", "Ascending Vine", "Spiral Sanctuary", "Jade Medallion", "Evolutionary Spiral", "Dynamic Helix", "Bronze Vine",
            "Spiral Chamber", "Jade Sprout", "Coiled Serenity", "Spiral Horizon", "Ascent Wheel", "Jade Rosette", "Botanical Ascent",
            "Spiral Meditation", "Verdant Vortex", "Golden Helix Path", "Ascending Gyre", "Jade Spiral Apex", "Spiral Harmony", "Evolutionary Crest",
            "Verdant Spiral Walk", "Sacred Gyre", "Spiral Ascent Crown", "Jade Transformation", "Evolutionary Mastery", "Spiral Realization", "Eternal Sacred Spiral"
        ]
    },
    {
        "id": "master_sanctuary",
        "chapter": 13,
        "name": "White Marble Master Shrine",
        "subtitle": "Divine Presence · Thassos White Marble & Inlaid 24K Gold",
        "bgImage": "./Assets/backgrounds/master_sanctuary_clean.png",
        "archetype": "ivory_wood",
        "audioPreset": "meditation_gong",
        "icon": "👑",
        "tiles": [
            ("Carved Walnut", "🪵"), ("Marble Inlay", "🪷"), ("Master Crown", "👑"), ("Golden Key", "🗝️"),
            ("Grand Chime", "🔔"), ("Imperial Crest", "⚜️"), ("Sanctuary Sceptre", "🪄"), ("Royal Astrolabe", "🧭"),
            ("Grand Hourglass", "⏳"), ("Polished Cameo", "🏵️"), ("Altar Vessel", "🏺"), ("Diamond Star", "💎"),
            ("Golden Laurel", "🌿"), ("Master Codex", "📖"), ("Shield of Honor", "🛡️"), ("Radiant Sun", "☀️")
        ],
        "base_words": [
            "White Marble Platform", "Floral Garland", "Ancient Canopy", "Golden Ray", "Jasmine Spray", "Divine Blessing", "Supreme Peace", "Inner Silence",
            "Purity of Light", "Gilded Inlay", "Thassos Slab", "Master Pillar", "Sanctuary Threshold", "Sacred Reflection", "White Petal Walk",
            "Marble Courtyard", "Gold Leaf Filigree", "Carved Teak Arch", "Sanctuary Basin", "Offering Platter", "Eternal Presence", "Quiet Portico",
            "Inlaid Lotus", "Sacred Radiance", "Master Gallery", "Chiseled Marble", "Golden Diya Stand", "Peace of the Shrine", "Inner Court",
            "White Rose Inlay", "Pure Marble Arch", "Sanctuary Corridor", "Golden Sunbeam", "Master Hearth", "Marble Scriptorium", "Spiritual Throne",
            "Inlaid Jasmine", "Sanctuary Apex", "Golden Chime", "White Marble Dome", "Master Balustrade", "Courtyard of Peace", "Gilded Petal Walk",
            "Sacred Marble Monolith", "Eternal Blessing", "Master Crown", "Presence of Peace", "Supreme Sanctuary", "Shrine Realization", "Master Shrine Apex"
        ]
    },
    {
        "id": "lotus_pond",
        "chapter": 14,
        "name": "Sunlit Lotus Pond",
        "subtitle": "River Quartz & Bamboo · Serene Water Lily Basin",
        "bgImage": "./Assets/backgrounds/lotus_pond_clean.png",
        "archetype": "slate_zen",
        "audioPreset": "zen_stone",
        "icon": "🪷",
        "tiles": [
            ("Sunlit Lotus", "🪷"), ("Water Lily Petal", "🌸"), ("Floating Lilypad", "🍃"), ("River Pebble", "🪨"),
            ("Koi Fish", "🐟"), ("Bamboo Slat", "🎋"), ("Clear Dewdrop", "💧"), ("Dragonfly Wing", "🪰"),
            ("Reed Frond", "🌾"), ("Spring Water", "🌊"), ("Willow Branch", "🌿"), ("Lotus Seedpod", "🌰"),
            ("Radiant Lotus Core", "✨"), ("Golden Water Lily", "🌟"), ("Jade Lilypad", "🍀"), ("Sunset Reflection", "🌅")
        ],
        "base_words": [
            "Sunlit Lotus", "Water Lily Basin", "Clear Reflection", "Floating Pad", "River Quartz", "Bamboo Terrace", "Quiet Ripples", "Koi Glade",
            "Dewdrop on Leaf", "Reed Bank", "Willow Frond", "Serene Waterway", "Pond Threshold", "Spring Stream", "Lotus Blossom",
            "Bamboo Pier", "Quartz Pebble", "Morning Mist", "Lilypad Mosaic", "Water Reflection", "Dragonfly Flight", "Gentle Ripple",
            "Sunlit Surface", "Emerald Lilypad", "Quartz Basin", "Water Garden", "Lotus Root", "Bamboo Slat Walk", "Quiet Pond",
            "Shimmering Water", "Water Lily Scent", "Bamboo Flute Walk", "Pond Solitude", "Floating Bloom", "Pebble Shore", "Clear Spring",
            "Lily Terrace", "Lotus Stamen", "Sunbeam on Water", "Serene Basin", "Water Lily Dawn", "Reflective Calm", "Emerald Stream",
            "Lotus Harmony", "Bamboo Bridge", "Sunlit Pond Apex", "Water Lily Peace", "Pond Realization", "Lotus Sanctuary", "Sunlit Lotus Pond Realization"
        ]
    },
    {
        "id": "granite_monolith",
        "chapter": 15,
        "name": "Himalayan Granite Monolith",
        "subtitle": "Rough-Hewn Silver Granite · High Mountain Silence",
        "bgImage": "./Assets/backgrounds/granite_monolith_clean.png",
        "archetype": "slate_zen",
        "audioPreset": "zen_stone",
        "icon": "🏔️",
        "tiles": [
            ("Granite Peak", "🏔️"), ("Mountain Ridge", "⛰️"), ("Chiseled Stone", "🪨"), ("Alpine Cloud", "☁️"),
            ("Ice Crystal", "❄️"), ("Glacial Stream", "💧"), ("Pine Needle", "🌲"), ("Falcon Crest", "🦅"),
            ("Stone Cairn", "🗿"), ("Monolith Pillar", "🏛️"), ("High Altitude Sun", "☀️"), ("Mountain Bell", "🔔"),
            ("Gilded Summit", "✨"), ("Radiant Peak", "🌟"), ("Silver Lichen Stone", "◽"), ("Zenith Compass", "🧭")
        ],
        "base_words": [
            "Granite Monolith", "Himalayan Ridge", "Chiseled Stone", "Alpine Cloud", "Glacial Stream", "Mountain Solitude", "High Altitude Sun", "Falcon Crest",
            "Stone Cairn", "Monolith Pillar", "Mountain Bell", "Silver Lichen", "Snowline Quiet", "Granite Threshold", "Highland Wind",
            "Speckled Stone", "Chiseled Ridge", "Alpine Pass", "Glacial Blue", "Monolith Face", "Granite Terrace", "Mountain Dawn",
            "Eternal Granite", "Highland Cairn", "Silver Mist", "Rock Plateau", "Chiseled Steps", "Alpine Stillness", "Granite Pillar",
            "Mountain Aspiration", "Stone Sanctuary", "Granite Slab", "High Altitude Calm", "Monolith Wall", "Alpine Horizon", "Granite Crest",
            "Chiseled Peak", "Rock Scriptorium", "Mountain Echo", "Glacial Crystal", "Granite Spire", "Highland Peace", "Monolith Tower",
            "Summit of Silence", "Granite Strength", "Alpine Monolith Apex", "Mountain Mastery", "Granite Realization", "Himalayan Summit", "Eternal Granite Monolith"
        ]
    },
    {
        "id": "sandalwood_amber",
        "chapter": 16,
        "name": "Royal Sandalwood & Amber",
        "subtitle": "Fragrant Seasoned Sandalwood · Warm Amber Incense",
        "bgImage": "./Assets/backgrounds/sandalwood_amber_clean.png",
        "archetype": "leather_tome",
        "audioPreset": "parchment",
        "icon": "🪵",
        "tiles": [
            ("Sandalwood Fan", "🪭"), ("Amber Resin Drop", "💎"), ("Incense Smoke", "💨"), ("Carved Rosette", "🏵️"),
            ("Honeycomb Cell", "🍯"), ("Aspiration Flame", "🔥"), ("Spiced Clove", "🌰"), ("Carved Elephant", "🐘"),
            ("Teak Box Clasp", "🗝️"), ("Scented Garland", "📿"), ("Amber Sunburst", "☀️"), ("Offering Urn", "🏺"),
            ("Glowing Amber Relic", "✨"), ("Luminous Sandal Seal", "🌟"), ("Golden Grain", "🌾"), ("Royal Diadem", "👑")
        ],
        "base_words": [
            "Sandalwood Fan", "Amber Resin", "Fragrant Smoke", "Carved Rosette", "Honeycomb Cell", "Aspiration Flame", "Spiced Clove", "Carved Elephant",
            "Teak Clasp", "Scented Garland", "Amber Sunburst", "Offering Urn", "Glowing Relic", "Luminous Sandal Seal", "Royal Diadem",
            "Sandalwood Box", "Amber Bead", "Fragrant Hearth", "Seasoned Timber", "Sandal Paste", "Golden Amber Drop", "Carved Lattice",
            "Royal Incense", "Sandalwood Aisle", "Amber Glow", "Fragrant Sanctum", "Warm Honeycomb", "Carved Medallion", "Sandalwood Pillar",
            "Amber Scent", "Golden Resinite", "Sandalwood Screen", "Royal Offering", "Incense Wisp", "Amber Chalice", "Fragrant Solitude",
            "Carved Timber Arch", "Amber Horizon", "Sandalwood Chamber", "Spiced Smoke", "Warm Amber Light", "Sandalwood Terrace", "Royal Hearth",
            "Amber Petal", "Fragrant Aspiration", "Sandalwood Harmony", "Amber Sanctuary Apex", "Sandalwood Realization", "Royal Amber Masterpiece", "Eternal Sandalwood"
        ]
    },
    {
        "id": "obsidian_vault",
        "chapter": 17,
        "name": "Obsidian Observatory",
        "subtitle": "Jet-Black Mirror Obsidian · Platinum Astral Mapping",
        "bgImage": "./Assets/backgrounds/obsidian_vault_clean.png",
        "archetype": "cosmic_glass",
        "audioPreset": "crystal_bell",
        "icon": "🔭",
        "tiles": [
            ("Obsidian Mirror", "🪞"), ("Midnight Star", "⭐"), ("Astrolabe Gear", "⚙️"), ("Celestial Telescope", "🔭"),
            ("Crescent Moon", "🌙"), ("Nebula Core", "🌀"), ("Prismatic Shard", "💎"), ("Eclipse Ring", "⭕"),
            ("Comet Trail", "☄️"), ("Planetary Ring", "🪐"), ("Starlight Ray", "⚡"), ("Cosmic Compass", "🧭"),
            ("Radiant Obsidian Star", "✨"), ("Platinum Nova", "🌟"), ("Deep Sky Void", "🌌"), ("Infinite Knot", "♾️")
        ],
        "base_words": [
            "Obsidian Mirror", "Midnight Star", "Astrolabe Gear", "Celestial Telescope", "Crescent Moon", "Nebula Core", "Prismatic Shard", "Eclipse Ring",
            "Comet Trail", "Planetary Ring", "Starlight Ray", "Cosmic Compass", "Radiant Star", "Platinum Nova", "Deep Sky Void",
            "Jet Obsidian", "Observatory Dome", "Star Chart", "Platinum Armillary", "Cosmic Horizon", "Midnight Glass", "Stellar Transit",
            "Obsidian Slab", "Celestial Axis", "Astral Reticle", "Midnight Solitude", "Deep Sky Lens", "Starlight Reflector", "Obsidian Basin",
            "Platinum Constellation", "Cosmic Vault", "Observatory Pier", "Star Meridian", "Obsidian Core", "Astral Sphere", "Midnight Silence",
            "Celestial Astrolabe", "Obsidian Terrace", "Starlight Calibration", "Platinum Ring", "Deep Space Mirror", "Cosmic Zenith", "Astral Observatory",
            "Obsidian Apex", "Midnight Nova", "Stellar Cartography", "Platinum Starlight", "Obsidian Realization", "Master Observatory", "Eternal Obsidian Vault"
        ]
    },
    {
        "id": "golden_harvest",
        "chapter": 18,
        "name": "Golden Harvest & Woven Rattan",
        "subtitle": "Woven Golden Rattan · Sun-Dried Clay & Wheat Grains",
        "bgImage": "./Assets/backgrounds/golden_harvest_clean.png",
        "archetype": "terracotta",
        "audioPreset": "clay_pot",
        "icon": "🌾",
        "tiles": [
            ("Wheat Sheaf", "🌾"), ("Woven Rattan Knot", "🧺"), ("Harvest Sun", "☀️"), ("Clay Grain Pot", "🏺"),
            ("Golden Corn", "🌽"), ("Earthen Sickle", "🌙"), ("Golden Sprout", "🌱"), ("Honey Comb", "🍯"),
            ("Field Poppy", "🌺"), ("Bountiful Basket", "🧺"), ("Sunlit Millstone", "⚙️"), ("Harvest Bread", "🍞"),
            ("Radiant Golden Ear", "✨"), ("Luminous Grain Wheel", "🌟"), ("Straw Crown", "👑"), ("Autumn Clover", "🍀")
        ],
        "base_words": [
            "Wheat Sheaf", "Woven Rattan", "Harvest Sun", "Grain Pot", "Golden Corn", "Earthen Sickle", "Golden Sprout", "Honey Comb",
            "Field Poppy", "Bountiful Basket", "Sunlit Millstone", "Harvest Bread", "Radiant Ear", "Grain Wheel", "Straw Crown",
            "Rattan Weave", "Sun-Dried Clay", "Golden Stalks", "Threshing Floor", "Autumn Breeze", "Harvest Wagon", "Earthen Granary",
            "Woven Lattice", "Golden Field", "Rattan Basket", "Sunlit Sheaf", "Harvest Hearth", "Barley Grain", "Clay Amphora of Corn",
            "Rattan Canopy", "Golden Chaff", "Autumn Solitude", "Harvest Moon", "Field Meadow", "Woven Straw Mat", "Grain Storage",
            "Golden Stubble", "Harvest Horizon", "Rattan Terrace", "Sunlit Barn", "Golden Ear of Wheat", "Harvest Solstice", "Bountiful Field",
            "Woven Harmony", "Harvest Abundance", "Golden Sheaf Apex", "Rattan Mastery", "Harvest Realization", "Golden Harvest Masterpiece", "Eternal Harvest"
        ]
    },
    {
        "id": "opal_aurora",
        "chapter": 19,
        "name": "Iridescent Opal & Aurora",
        "subtitle": "Fire Opal Gemstone · Northern Lights & Rose-Gold",
        "bgImage": "./Assets/backgrounds/opal_aurora_clean.png",
        "archetype": "enamel_cameo",
        "audioPreset": "quartz_bowl",
        "icon": "💎",
        "tiles": [
            ("Fire Opal", "💎"), ("Aurora Wave", "🌌"), ("Pearlescent Shell", "⚪"), ("Prismatic Prism", "🔮"),
            ("Luminous Butterfly", "🦋"), ("Iridescent Feather", "🪶"), ("Northern Star", "⭐"), ("Violet Crystal", "💜"),
            ("Rainbow Arc", "🌈"), ("Celestial Veil", "✨"), ("Polar Glow", "❄️"), ("Spectral Swan", "🦢"),
            ("Pulsing Opal Core", "🌟"), ("Radiant Aurora Crown", "👑"), ("Iridescent Lotus", "🪷"), ("Astral Halo", "⭕")
        ],
        "base_words": [
            "Fire Opal", "Aurora Wave", "Pearlescent Shell", "Prismatic Shard", "Luminous Butterfly", "Iridescent Feather", "Northern Star", "Violet Crystal",
            "Rainbow Arc", "Celestial Veil", "Polar Glow", "Spectral Swan", "Pulsing Opal", "Aurora Crown", "Iridescent Lotus",
            "Rose-Gold Bezel", "Opal Flashes", "Curtain of Light", "Aurora Borealis", "Prismatic Reflection", "Iridescent Shell", "Northern Radiance",
            "Fire Opal Tablet", "Aurora Horizon", "Rose-Gold Filigree", "Luminous Mist", "Spectral Glow", "Iridescent Shimmer", "Polar Twilight",
            "Opaline Gem", "Aurora Veil", "Celestial Shimmer", "Rainbow Prism", "Rose-Gold Clasp", "Polar Night", "Iridescent Wave",
            "Aurora Cascade", "Opal Fire", "Northern Glow", "Celestial Opal", "Aurora Solitude", "Iridescent Aura", "Rose-Gold Cameo",
            "Polar Aurora Walk", "Spectral Lotus", "Opal Apex", "Aurora Mastery", "Iridescent Realization", "Supreme Opal Crown", "Eternal Opal Aurora"
        ]
    },
    {
        "id": "bodhi_grove",
        "chapter": 20,
        "name": "Sacred Bodhi Grove",
        "subtitle": "Gilded Pipal Wood · White Jade & Universal Light",
        "bgImage": "./Assets/backgrounds/bodhi_grove_clean.png",
        "archetype": "ivory_wood",
        "audioPreset": "meditation_gong",
        "icon": "🌳",
        "tiles": [
            ("Bodhi Leaf", "🍃"), ("Sacred Bodhi Tree", "🌳"), ("White Jade Tablet", "🤍"), ("Enlightenment Flame", "🔥"),
            ("Lotus Seat", "🪷"), ("Wheel of Dharma", "☸️"), ("Golden Bell", "🔔"), ("Meditation Urn", "🏺"),
            ("Sunburst Halo", "☀️"), ("Sacred Thread", "📿"), ("Radiant Deer", "🦌"), ("Peace Crane", "🕊️"),
            ("Golden Bodhi Master", "✨"), ("Supreme Sun Star", "🌟"), ("Jade Lotus Emblem", "🏵️"), ("Universal Crown", "👑")
        ],
        "base_words": [
            "Bodhi Leaf", "Sacred Bodhi Tree", "White Jade Tablet", "Enlightenment Flame", "Lotus Seat", "Wheel of Truth", "Golden Bell", "Meditation Urn",
            "Sunburst Halo", "Sacred Thread", "Radiant Deer", "Peace Crane", "Golden Bodhi Master", "Supreme Sun Star", "Jade Lotus",
            "Gilded Pipal Wood", "Universal Light", "Canopy of Awakening", "White Jade Pillar", "Golden Leaves", "Tree of Enlightenment", "Sacred Grove",
            "Lotus Dais", "Bodhi Terrace", "Ancient Roots", "Spiritual Radiance", "Enlightenment Courtyard", "Universal Peace", "Golden Canopy",
            "White Jade Floor", "Bodhi Whispers", "Sacred Arbor", "Golden Bell Tower", "Sunlit Bodhi Walk", "Seat of Stillness", "Lotus Meditation",
            "Enlightenment Dawn", "Gilded Trunk", "Universal Halo", "Bodhi Sanctuary", "White Jade Rosette", "Tree of Life Core", "Sacred Grove Solitude",
            "Enlightenment Path", "Golden Leaf Rain", "Bodhi Monolith", "Universal Crown", "Supreme Enlightenment", "Grand Finale Awakening", "Bodhi Grove Realization"
        ]
    }
]

print(f"Loaded {len(THEMES_DATA)} themes.")
for t in THEMES_DATA:
    assert len(t["base_words"]) == 50, f"Theme {t['id']} has {len(t['base_words'])} words, must be 50"
    assert len(t["tiles"]) == 16, f"Theme {t['id']} has {len(t['tiles'])} tiles, must be 16"
print("All 20 themes have exactly 50 curated level names and 16 custom tiles!")

# Generate themeManager.js
js_content = """// ThemeManager: Manages the 20 Secular Realms Grand Campaign (1,000 Total Thematic Levels)
// Coordinates clean background wallpapers, authentic 3D tactile tile skins, and audio presets.

export const TOTAL_REALM_LEVELS = 1000; // 20 Themes * 50 Levels per Theme
export const LEVELS_PER_REALM = 50;
export const TOTAL_CLASSIC_LEVELS = 200; // Dedicated Classic Solitaire Campaign

// 16 distinct emblems with symbolic labels for each theme
const THEME_TILE_DEFS = {
"""

for t in THEMES_DATA:
    js_content += f'  "{t["id"]}": [\n'
    for name, sym in t["tiles"]:
        js_content += f'    {{ name: "{name}", symbol: "{sym}" }},\n'
    js_content += '  ],\n'

js_content += """};

function buildCustomTilesForTheme(themeId) {
  const defs = THEME_TILE_DEFS[themeId] || THEME_TILE_DEFS.whispering_pines;
  return defs.map((d, idx) => ({
    name: d.name,
    image: `./Assets/themes/${themeId}/tile_${String(idx + 1).padStart(2, '0')}.png`,
    symbol: d.symbol
  }));
}

export const REALMS = [
"""

for t in THEMES_DATA:
    lvl_start = (t["chapter"] - 1) * 50 + 1
    lvl_end = t["chapter"] * 50
    level_names_json = json.dumps(t["base_words"], indent=6)
    
    js_content += f"""  {{
    id: '{t["id"]}',
    chapter: {t["chapter"]},
    name: '{t["name"]}',
    subtitle: '{t["subtitle"]}',
    mockupImage: '{t["bgImage"].replace("_clean.png", ".png")}',
    bgImage: '{t["bgImage"]}',
    archetype: '{t["archetype"]}',
    audioPreset: '{t["audioPreset"]}',
    levelStart: {lvl_start},
    levelEnd: {lvl_end},
    icon: '{t["icon"]}',
    levelNames: {level_names_json},
    customTiles: buildCustomTilesForTheme('{t["id"]}')
  }},
"""

js_content += """
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
    f.write(js_content)

print("src/controllers/themeManager.js successfully generated with 20 themes and 1,000 levels!")
