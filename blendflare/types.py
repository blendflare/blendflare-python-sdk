"""Type definitions and enums for the Blendflare API."""

from enum import Enum
from typing import List, Optional


class Category(str, Enum):
    """Main asset categories."""
    
    ARCHITECTURE = "architecture"
    CHARACTER = "character"
    ACCESSORIES = "accessories"
    DECORATION = "decoration"
    INDUSTRIAL = "industrial"
    INTERIOR = "interior"
    MILITARY = "military"
    NATURE = "nature"
    SCIENCE = "science"
    SPACE = "space"
    SPORT_HOBBY = "sport_hobby"
    TECHNOLOGY = "technology"
    TRANSPORT = "transport"
    NODE_GROUP = "node_group"
    MATERIALS = "materials"
    HDRIS = "hdris"
    BRUSHES = "brushes"
    DECALS = "decals"
    SCENES = "scenes"
    SIMULATIONS_VFX = "simulations_vfx"
    ANIMATION_RIGS = "animation_rigs"
    TEMPLATE_SETUPS = "template_setups"
    EDUCATIONAL = "educational"
    LIGHTING = "lighting"
    RESEARCH = "research"


class Subcategory(str, Enum):
    """Subcategories for assets."""
    
    # Accessories
    BAGS_CARRIERS = "bags_carriers"
    BELTS_STRAPS = "belts_straps"
    EYEWEAR = "eyewear"
    FASHION_ACCESSORIES = "fashion_accessories"
    FOOTWEAR = "footwear"
    GLOVES_HAND_ACCESSORIES = "gloves_hand_accessories"
    HAIR_ACCESSORIES = "hair_accessories"
    HEADWEAR = "headwear"
    JEWELRY = "jewelry"
    OTHER = "other"
    SCARVES_NECKWEAR = "scarves_neckwear"
    TECH_ACCESSORIES = "tech_accessories"
    
    # Animation Rigs
    ANIMAL_RIGS = "animal_rigs"
    ANIMATION_PRESETS = "animation_presets"
    CHARACTER_RIGS = "character_rigs"
    CONTROLLERS_UI = "controllers_ui"
    CREATURE_RIGS = "creature_rigs"
    FACIAL_RIGS = "facial_rigs"
    HAND_RIGS = "hand_rigs"
    IK_FK_SYSTEMS = "ik_fk_systems"
    MECHANICAL_RIGS = "mechanical_rigs"
    MOTION_CAPTURE = "motion_capture"
    TAIL_RIGS = "tail_rigs"
    VEHICLE_RIGS = "vehicle_rigs"
    WING_RIGS = "wing_rigs"
    
    # Architecture
    BALCONY_TERRACE = "balcony_terrace"
    BUILDING = "building"
    DOOR = "door"
    EXTERIOR_ELEMENT = "exterior_element"
    FENCE_RAILING = "fence_railing"
    FLOOR_COVERING = "floor_covering"
    FOUNDATION_STRUCTURAL_BASE = "foundation_structural_base"
    MOLDING_CARVING = "molding_carving"
    ROOF_ROOFING_ELEMENTS = "roof_roofing_elements"
    STAIRS = "stairs"
    STRUCTURE = "structure"
    WALL_PANEL = "wall_panel"
    WINDOW = "window"
    
    # Brushes
    ANIMAL_CREATURE = "animal_creature"
    ART = "art"
    CLOTHING = "clothing"
    DAMAGE = "damage"
    FABRIC_TEXTILE = "fabric_textile"
    GEOMETRIC = "geometric"
    HAIR_FUR = "hair_fur"
    HUMAN = "human"
    INDUSTRIAL = "industrial"
    NATURE = "nature"
    SCI_FI_TECH = "sci_fi_tech"
    
    # Character
    ANATOMY = "anatomy"
    ANIMAL = "animal"
    WOMAN_CLOTHING = "woman_clothing"
    MAN_CLOTHING = "man_clothing"
    FANTASY_RACES = "fantasy_races"
    HAIR_HAIRSTYLES = "hair_hairstyles"
    HUMANOIDS = "humanoids"
    MONSTER_CREATURE = "monster_creature"
    ROBOT = "robot"
    
    # Decals
    BLOOD = "blood"
    BULLET_HOLES = "bullet_holes"
    BURN_MARKS = "burn_marks"
    CRACKS_DAMAGE = "cracks_damage"
    DEBRIS = "debris"
    DECORATION = "decoration"
    DIRT_GRIME = "dirt_grime"
    FLOOR_MARKINGS = "floor_markings"
    FOLIAGE = "foliage"
    FOODS = "foods"
    GRAFFITI = "graffiti"
    IMPERFECTIONS = "imperfections"
    ORGANIC_PATTERNS = "organic_patterns"
    PAINT_CHIPPING = "paint_chipping"
    RUST_CORROSION = "rust_corrosion"
    SCRATCHES_SCUFFS = "scratches_scuffs"
    SIGNAGE = "signage"
    STAINS_SPILLS = "stains_spills"
    SYMBOLS_ICONS = "symbols_icons"
    TEXT_NUMBERS = "text_numbers"
    VEHICLE_MARKINGS = "vehicle_markings"
    WATER_MOISTURE = "water_moisture"
    WEAR_TEAR = "wear_tear"
    
    # Decoration
    BED_SHEET = "bed_sheet"
    BLANKET = "blanket"
    BOOK = "book"
    CANDLES_CANDLE_HOLDERS = "candles_candle_holders"
    CARPETS = "carpets"
    CLOCK_WATCH = "clock_watch"
    CURTAIN = "curtain"
    DECORATION_SET = "decoration_set"
    FABRICS = "fabrics"
    FIREPLACE = "fireplace"
    FOOD_DRINKS = "food_drinks"
    HOLIDAY_DECORATION = "holiday_decoration"
    MIRROR = "mirror"
    MONEY = "money"
    MUSICAL_INSTRUMENTS = "musical_instruments"
    PICTURE = "picture"
    PILLOW = "pillow"
    SCULPTURE = "sculpture"
    TEXTILE = "textile"
    TOYS_GAMES = "toys_games"
    TROPHY_AWARD = "trophy_award"
    VASE = "vase"
    
    # Educational
    BEGINNER_PROJECTS = "beginner_projects"
    CHALLENGE_PROJECTS = "challenge_projects"
    COURSE_MATERIALS = "course_materials"
    DOCUMENTATION = "documentation"
    LEARNING_KITS = "learning_kits"
    PRACTICE_SCENES = "practice_scenes"
    STUDY_REFERENCES = "study_references"
    TECHNIQUE_DEMONSTRATIONS = "technique_demonstrations"
    TUTORIAL_FILES = "tutorial_files"
    WORKFLOW_EXAMPLES = "workflow_examples"
    
    # HDRIs
    ABSTRACT = "abstract"
    ARCHITECTURAL = "architectural"
    CITYSCAPES = "cityscapes"
    FUTURISTIC_ENVIRONMENTS = "futuristic_environments"
    HOLIDAY = "holiday"
    INTERIORS = "interiors"
    LANDSCAPES = "landscapes"
    NIGHTTIME_ENVIRONMENTS = "nighttime_environments"
    PUBLIC = "public"
    RESIDENTIAL = "residential"
    RURAL = "rural"
    SPORTS = "sports"
    STUDIO = "studio"
    URBAN = "urban"
    WATER_ENVIRONMENTS = "water_environments"
    
    # Industrial
    CONTAINER = "container"
    EQUIPMENT = "equipment"
    MACHINERY = "machinery"
    PARTS = "parts"
    SIGN = "sign"
    TOOLS = "tools"
    
    # Lighting
    CINEMATIC_LIGHTING = "cinematic_lighting"
    IES_PROFILES = "ies_profiles"
    LIGHT_RIGS = "light_rigs"
    NATURAL_LIGHTING = "natural_lighting"
    NEON_GLOWING = "neon_glowing"
    NIGHT_LIGHTING = "night_lighting"
    OUTDOOR_LIGHTING = "outdoor_lighting"
    PRODUCT_LIGHTING = "product_lighting"
    STUDIO_LIGHTING = "studio_lighting"
    VOLUMETRIC_LIGHTING = "volumetric_lighting"
    
    # Materials
    ASPHALT = "asphalt"
    BRICKS = "bricks"
    CARBON_FIBER = "carbon_fiber"
    CERAMIC = "ceramic"
    CONCRETE = "concrete"
    DIRT = "dirt"
    FABRIC = "fabric"
    FLOOR = "floor"
    FOAM = "foam"
    FOOD = "food"
    GLASS = "glass"
    GRASS = "grass"
    GROUND = "ground"
    ICE = "ice"
    LEATHER = "leather"
    LIQUID = "liquid"
    MARBLE = "marble"
    METAL = "metal"
    ORGANIC = "organic"
    ORNAMENTS = "ornaments"
    PAINT = "paint"
    PAPER = "paper"
    PAVING = "paving"
    PLASTER = "plaster"
    PLASTIC = "plastic"
    ROCK = "rock"
    ROOFING = "roofing"
    RUBBER = "rubber"
    RUST = "rust"
    SAND = "sand"
    SOIL = "soil"
    STONE = "stone"
    TECH = "tech"
    TERRAZZO = "terrazzo"
    TILES = "tiles"
    WAX = "wax"
    WOOD = "wood"
    
    # Military
    AIRCRAFT = "aircraft"
    VEHICLES = "vehicles"
    WATERCRAFT = "watercraft"
    WEAPONS = "weapons"
    EQUIPMENT_GEAR = "equipment_gear"
    ACCESSORIES_MILITARY = "accessories"
    FORTIFICATIONS = "fortifications"
    CAMPS_BASES = "camps_bases"
    PROPS = "props"
    ARMOR = "armor"
    CLOTHING_UNIFORMS = "clothing_uniforms"
    
    # Nature
    ATMOSPHERE = "atmosphere"
    FLOWERS = "flowers"
    FOLIAGE_BUSH = "foliage_bush"
    FUNGI_MUSHROOMS = "fungi_mushrooms"
    LANDSCAPE = "landscape"
    PLANT = "plant"
    ROCK_STONE_FORMATION = "rock_stone_formation"
    TREE = "tree"
    WATER_FEATURES = "water_features"
    
    # Node Groups
    COMPOSITING_NODES = "compositing_nodes"
    GEOMETRY_NODES = "geometry_nodes"
    PROCEDURAL_GENERATORS = "procedural_generators"
    SHADING_NODES = "shading_nodes"
    SIMULATION_NODES = "simulation_nodes"
    UTILITY_NODES = "utility_nodes"
    
    # Research
    ASTRONOMY_ASTROPHYSICS = "astronomy_astrophysics"
    BIOLOGY_MOLECULAR = "biology_molecular"
    BIOMEDICAL_MEDICAL = "biomedical_medical"
    CHEMISTRY_MATERIALS = "chemistry_materials"
    DATA_VISUALIZATION = "data_visualization"
    EARTH_SCIENCES_GEOLOGY = "earth_sciences_geology"
    MACHINE_LEARNING_AI = "machine_learning_ai"
    NEUROSCIENCE = "neuroscience"
    SCIENTIFIC_ILLUSTRATION = "scientific_illustration"
    SYNTHETIC_DATASETS = "synthetic_datasets"
    
    # Scenes
    ABSTRACT_SCENES = "abstract_scenes"
    ANIMATION_SCENES = "animation_scenes"
    COMPLETE_PROJECTS = "complete_projects"
    ENVIRONMENT_SCENES = "environment_scenes"
    EXTERIOR_SCENES = "exterior_scenes"
    GAME_ENVIRONMENTS = "game_environments"
    INTERIOR_SCENES = "interior_scenes"
    PRODUCT_SHOTS = "product_shots"
    REALISTIC_SCENES = "realistic_scenes"
    STYLIZED_SCENES = "stylized_scenes"
    
    # Simulations & VFX
    ATMOSPHERIC_EFFECTS = "atmospheric_effects"
    CLOTH_SIMULATIONS = "cloth_simulations"
    DESTRUCTION_BREAKING = "destruction_breaking"
    EXPLOSIONS = "explosions"
    FIRE_SMOKE = "fire_smoke"
    FLUID_SIMULATIONS = "fluid_simulations"
    MAGIC_ENERGY_EFFECTS = "magic_energy_effects"
    PARTICLE_SYSTEMS = "particle_systems"
    PHYSICS_SIMULATIONS = "physics_simulations"
    WEATHER_EFFECTS = "weather_effects"
    
    # Space
    PLANET = "planet"
    SATELLITE = "satellite"
    SPACECRAFT = "spacecraft"
    STATION = "station"
    SPACE_SUIT_EQUIPMENT = "space_suit_equipment"
    
    # Sport & Hobby
    FISHING = "fishing"
    GYM = "gym"
    HOBBY_ACCESSORIES = "hobby_accessories"
    MUSIC = "music"
    SPORT = "sport"
    
    # Technology
    AUDIO_DEVICES = "audio_devices"
    CABLES_CONNECTORS = "cables_connectors"
    COMPUTER = "computer"
    DEVICE = "device"
    DRONE = "drone"
    GAMING_HARDWARE = "gaming_hardware"
    HOME_APPLIANCE = "home_appliance"
    PHOTOGRAPHY = "photography"
    ROBOTICS = "robotics"
    SMART_HOME_DEVICES = "smart_home_devices"
    VIDEO_DEVICES = "video_devices"
    
    # Template Setups
    ARCHVIZ_TEMPLATES = "archviz_templates"
    CAMERA_RIGS = "camera_rigs"
    COMPOSITING_TEMPLATES = "compositing_templates"
    LIGHTING_SETUPS = "lighting_setups"
    PRODUCT_VISUALIZATION = "product_visualization"
    RENDER_SETUPS = "render_setups"
    SCENE_TEMPLATES = "scene_templates"
    SHADER_TEMPLATES = "shader_templates"
    STUDIO_SETUPS = "studio_setups"
    WORKFLOW_TEMPLATES = "workflow_templates"
    
    # Transport
    AGRICULTURAL_VEHICLE = "agricultural_vehicle"
    BICYCLE = "bicycle"
    CAR = "car"
    CONSTRUCTION_VEHICLE = "construction_vehicle"
    EMERGENCY = "emergency"
    HEAVY_VEHICLE = "heavy_vehicle"
    MOTOCYCLE = "motocycle"
    PUBLIC_TRANSPORT = "public_transport"
    RAILED_VEHICLE = "railed_vehicle"
    SMALL_ELECTRIC_VEHICLES = "small_electric_vehicles"
    TRAILER_CARAVAN = "trailer_caravan"
    VEHICLE_PARTS = "vehicle_parts"


class Style(str, Enum):
    """Visual style of assets."""
    
    REALISTIC = "realistic"
    STYLIZED = "stylized"
    CARTOON = "cartoon"
    ANIME = "anime"
    PAINTERLY = "painterly"
    LINE_ART = "line_art"
    CLAY = "clay"
    CELL_SHADING = "cell_shading"
    ABSTRACT = "abstract"
    PIXELATED = "pixelated"
    OTHER = "other"


class RenderEngine(str, Enum):
    """Blender render engines."""
    
    CYCLES = "cycles"
    EEVEE = "eevee"
    WORKBENCH = "workbench"
    RENDERMAN = "renderman"
    VRAY = "vray"
    OCTANE = "octane"
    ARNOLD = "arnold"
    LUXCORE = "luxcore"


class MaterialType(str, Enum):
    """Material types."""
    
    PROCEDURAL = "procedural"
    TEXTURE_BASED = "texture_based"
    BOTH = "both"
    NA = "na"


class UVMapping(str, Enum):
    """UV mapping types."""
    
    NO_UV = "no_uv"
    OVERLAPPING = "overlapping"
    NON_OVERLAPPING = "non_overlapping"
    MIXED = "mixed"


class Feature(str, Enum):
    """Asset features."""
    
    PRINTABLE_3D = "3d_printable"
    ANIMATED = "animated"
    RIGGED = "rigged"
    SCANNED_3D = "3d_scanned"
    LOW_POLY = "low_poly"
    HIGH_POLY = "high_poly"
    GAME_READY = "game_ready"
    SCULPTING = "sculpting"
    GREASE_PENCIL = "grease_pencil"
    SYNTHETIC_DATA = "synthetic_data"


class Simulation(str, Enum):
    """Physics simulation types."""
    
    FLUID = "fluid"
    SMOKE = "smoke"
    CLOTH = "cloth"
    SOFT_BODY = "soft_body"
    RIGID_BODY = "rigid_body"
    HAIR = "hair"


class NodeGroupType(str, Enum):
    """Node group types."""
    
    SHADING_NODES = "shading_nodes"
    GEOMETRY_NODES = "geometry_nodes"
    COMPOSITING_NODES = "compositing_nodes"


class Physics(str, Enum):
    """Physics features."""
    
    FORCE_FIELDS = "force_fields"
    RIGID_BODY_CONSTRAINTS = "rigid_body_constraints"
    COLLISION_OBJECTS = "collision_objects"


class GameEngine(str, Enum):
    """Game engine compatibility."""
    
    GODOT = "godot"
    UNITY = "unity"
    UNREAL_ENGINE = "unreal_engine"


class LicenseType(str, Enum):
    """Asset license types."""
    
    CC0 = "cc0"
    CC_BY = "cc_by"
    CC_BY_SA = "cc_by_sa"
    CC_BY_NC = "cc_by_nc"
    CC_BY_NC_SA = "cc_by_nc_sa"
    CUSTOM = "custom"
    ALL_RIGHTS_RESERVED = "all_rights_reserved"


class LegalFlag(str, Enum):
    """Legal flags for assets."""
    
    FAN_ART = "fan_art"
    CONTAINS_NSFW = "contains_nsfw"
    TRADEMARKS = "trademarks"
    NO_AI_LICENSE = "no_ai_license"
    AI_GENERATED = "ai_generated"


class SortBy(str, Enum):
    """Sort fields for search results."""
    
    RELEVANCE = "relevance"
    NEWEST = "newest"
    OLDEST = "oldest"
    POPULAR = "popular"
    DOWNLOADS = "downloads"
    LIKES = "likes"
    VIEWS = "views"
    BOOKMARKS = "bookmarks"


class SortOrder(str, Enum):
    """Sort order for search results."""
    
    ASC = "asc"
    DESC = "desc"


# Helper functions for type conversions
def join_enum_values(values: List[Enum]) -> str:
    """Join multiple enum values with + separator."""
    return "+".join(v.value for v in values)


def parse_tags(tags: List[str]) -> str:
    """Parse list of tags into API format."""
    return "+".join(tags)