# Blendflare SDK Types Reference

This document provides a complete reference for all enums and types available in the Blendflare Python SDK.

## Table of Contents

- [Blendflare SDK Types Reference](#blendflare-sdk-types-reference)
  - [Table of Contents](#table-of-contents)
  - [Category](#category)
  - [Subcategory](#subcategory)
    - [Accessories Subcategories](#accessories-subcategories)
    - [Animation Rigs Subcategories](#animation-rigs-subcategories)
    - [Architecture Subcategories](#architecture-subcategories)
    - [Character Subcategories](#character-subcategories)
    - [Transport Subcategories](#transport-subcategories)
  - [Style](#style)
  - [Feature](#feature)
  - [RenderEngine](#renderengine)
  - [MaterialType](#materialtype)
  - [UVMapping](#uvmapping)
  - [Simulation](#simulation)
  - [NodeGroupType](#nodegrouptype)
  - [Physics](#physics)
  - [GameEngine](#gameengine)
  - [LicenseType](#licensetype)
  - [LegalFlag](#legalflag)
  - [SortBy](#sortby)
  - [SortOrder](#sortorder)
  - [Helper Functions](#helper-functions)
    - [`join_enum_values(values: List[Enum]) -> str`](#join_enum_valuesvalues-listenum---str)
    - [`parse_tags(tags: List[str]) -> str`](#parse_tagstags-liststr---str)
  - [Complete Example](#complete-example)

---

## Category

Main asset categories for filtering projects.

| Enum Value | String Value | Description |
|------------|--------------|-------------|
| `Category.ARCHITECTURE` | `"architecture"` | Buildings, structures, architectural elements |
| `Category.CHARACTER` | `"character"` | Human and creature characters |
| `Category.ACCESSORIES` | `"accessories"` | Wearable items and accessories |
| `Category.DECORATION` | `"decoration"` | Decorative items and props |
| `Category.INDUSTRIAL` | `"industrial"` | Industrial equipment and machinery |
| `Category.INTERIOR` | `"interior"` | Interior design elements |
| `Category.MILITARY` | `"military"` | Military equipment and vehicles |
| `Category.NATURE` | `"nature"` | Natural elements (trees, plants, rocks) |
| `Category.SCIENCE` | `"science"` | Scientific equipment and models |
| `Category.SPACE` | `"space"` | Space-related assets |
| `Category.SPORT_HOBBY` | `"sport_hobby"` | Sports and hobby equipment |
| `Category.TECHNOLOGY` | `"technology"` | Electronic devices and tech |
| `Category.TRANSPORT` | `"transport"` | Vehicles and transportation |
| `Category.NODE_GROUP` | `"node_group"` | Blender node groups |
| `Category.MATERIALS` | `"materials"` | Material presets |
| `Category.HDRIS` | `"hdris"` | HDRI environments |
| `Category.BRUSHES` | `"brushes"` | Sculpting and painting brushes |
| `Category.DECALS` | `"decals"` | Texture decals |
| `Category.SCENES` | `"scenes"` | Complete scene setups |
| `Category.SIMULATIONS_VFX` | `"simulations_vfx"` | Simulation and VFX setups |
| `Category.ANIMATION_RIGS` | `"animation_rigs"` | Animation and rigging setups |
| `Category.TEMPLATE_SETUPS` | `"template_setups"` | Template and workflow setups |
| `Category.EDUCATIONAL` | `"educational"` | Educational resources |
| `Category.LIGHTING` | `"lighting"` | Lighting setups |
| `Category.RESEARCH` | `"research"` | Research and scientific visualization |

**Example:**
```python
from blendflare import BlendflareClient, Category

client = BlendflareClient(api_key="sk_live_...")
results = client.search_projects(category=Category.NATURE)
```

---

## Subcategory

Subcategories provide more specific filtering within each main category. Due to the large number of subcategories, they are organized by their parent category.

### Accessories Subcategories

| Enum Value | String Value |
|------------|--------------|
| `Subcategory.BAGS_CARRIERS` | `"bags_carriers"` |
| `Subcategory.BELTS_STRAPS` | `"belts_straps"` |
| `Subcategory.EYEWEAR` | `"eyewear"` |
| `Subcategory.FASHION_ACCESSORIES` | `"fashion_accessories"` |
| `Subcategory.FOOTWEAR` | `"footwear"` |
| `Subcategory.GLOVES_HAND_ACCESSORIES` | `"gloves_hand_accessories"` |
| `Subcategory.HAIR_ACCESSORIES` | `"hair_accessories"` |
| `Subcategory.HEADWEAR` | `"headwear"` |
| `Subcategory.JEWELRY` | `"jewelry"` |
| `Subcategory.SCARVES_NECKWEAR` | `"scarves_neckwear"` |
| `Subcategory.TECH_ACCESSORIES` | `"tech_accessories"` |
| `Subcategory.OTHER` | `"other"` |

### Animation Rigs Subcategories

| Enum Value | String Value |
|------------|--------------|
| `Subcategory.ANIMAL_RIGS` | `"animal_rigs"` |
| `Subcategory.ANIMATION_PRESETS` | `"animation_presets"` |
| `Subcategory.CHARACTER_RIGS` | `"character_rigs"` |
| `Subcategory.CONTROLLERS_UI` | `"controllers_ui"` |
| `Subcategory.CREATURE_RIGS` | `"creature_rigs"` |
| `Subcategory.FACIAL_RIGS` | `"facial_rigs"` |
| `Subcategory.HAND_RIGS` | `"hand_rigs"` |
| `Subcategory.IK_FK_SYSTEMS` | `"ik_fk_systems"` |
| `Subcategory.MECHANICAL_RIGS` | `"mechanical_rigs"` |
| `Subcategory.MOTION_CAPTURE` | `"motion_capture"` |
| `Subcategory.TAIL_RIGS` | `"tail_rigs"` |
| `Subcategory.VEHICLE_RIGS` | `"vehicle_rigs"` |
| `Subcategory.WING_RIGS` | `"wing_rigs"` |

### Architecture Subcategories

| Enum Value | String Value |
|------------|--------------|
| `Subcategory.BALCONY_TERRACE` | `"balcony_terrace"` |
| `Subcategory.BUILDING` | `"building"` |
| `Subcategory.DOOR` | `"door"` |
| `Subcategory.EXTERIOR_ELEMENT` | `"exterior_element"` |
| `Subcategory.FENCE_RAILING` | `"fence_railing"` |
| `Subcategory.FLOOR_COVERING` | `"floor_covering"` |
| `Subcategory.FOUNDATION_STRUCTURAL_BASE` | `"foundation_structural_base"` |
| `Subcategory.MOLDING_CARVING` | `"molding_carving"` |
| `Subcategory.ROOF_ROOFING_ELEMENTS` | `"roof_roofing_elements"` |
| `Subcategory.STAIRS` | `"stairs"` |
| `Subcategory.STRUCTURE` | `"structure"` |
| `Subcategory.WALL_PANEL` | `"wall_panel"` |
| `Subcategory.WINDOW` | `"window"` |

### Character Subcategories

| Enum Value | String Value |
|------------|--------------|
| `Subcategory.ANATOMY` | `"anatomy"` |
| `Subcategory.ANIMAL` | `"animal"` |
| `Subcategory.WOMAN_CLOTHING` | `"woman_clothing"` |
| `Subcategory.MAN_CLOTHING` | `"man_clothing"` |
| `Subcategory.FANTASY_RACES` | `"fantasy_races"` |
| `Subcategory.HAIR_HAIRSTYLES` | `"hair_hairstyles"` |
| `Subcategory.HUMANOIDS` | `"humanoids"` |
| `Subcategory.MONSTER_CREATURE` | `"monster_creature"` |
| `Subcategory.ROBOT` | `"robot"` |

### Transport Subcategories

| Enum Value | String Value |
|------------|--------------|
| `Subcategory.AGRICULTURAL_VEHICLE` | `"agricultural_vehicle"` |
| `Subcategory.BICYCLE` | `"bicycle"` |
| `Subcategory.CAR` | `"car"` |
| `Subcategory.CONSTRUCTION_VEHICLE` | `"construction_vehicle"` |
| `Subcategory.EMERGENCY` | `"emergency"` |
| `Subcategory.HEAVY_VEHICLE` | `"heavy_vehicle"` |
| `Subcategory.MOTOCYCLE` | `"motocycle"` |
| `Subcategory.PUBLIC_TRANSPORT` | `"public_transport"` |
| `Subcategory.RAILED_VEHICLE` | `"railed_vehicle"` |
| `Subcategory.SMALL_ELECTRIC_VEHICLES` | `"small_electric_vehicles"` |
| `Subcategory.TRAILER_CARAVAN` | `"trailer_caravan"` |
| `Subcategory.VEHICLE_PARTS` | `"vehicle_parts"` |

> **Note:** For a complete list of all subcategories across all categories, see the full `Subcategory` enum in `blendflare/types.py`

**Example:**
```python
from blendflare import Category, Subcategory

results = client.search_projects(
    category=Category.TRANSPORT,
    subcategory=Subcategory.CAR
)
```

---

## Style

Visual and artistic style of assets.

| Enum Value | String Value | Description |
|------------|--------------|-------------|
| `Style.REALISTIC` | `"realistic"` | Photorealistic or realistic style |
| `Style.STYLIZED` | `"stylized"` | Stylized, artistic interpretation |
| `Style.CARTOON` | `"cartoon"` | Cartoon or comic style |
| `Style.ANIME` | `"anime"` | Anime or manga style |
| `Style.PAINTERLY` | `"painterly"` | Painterly, hand-painted look |
| `Style.LINE_ART` | `"line_art"` | Line art style |
| `Style.CLAY` | `"clay"` | Clay or stop-motion style |
| `Style.CELL_SHADING` | `"cell_shading"` | Cell-shaded, toon-shaded |
| `Style.ABSTRACT` | `"abstract"` | Abstract style |
| `Style.PIXELATED` | `"pixelated"` | Pixel art style |
| `Style.OTHER` | `"other"` | Other or mixed styles |

**Example:**
```python
from blendflare import Style

results = client.search_projects(
    q="character",
    style=Style.REALISTIC
)
```

---

## Feature

Special features and capabilities of assets.

| Enum Value | String Value | Description |
|------------|--------------|-------------|
| `Feature.PRINTABLE_3D` | `"3d_printable"` | Ready for 3D printing |
| `Feature.ANIMATED` | `"animated"` | Includes animations |
| `Feature.RIGGED` | `"rigged"` | Has rigging/armature |
| `Feature.SCANNED_3D` | `"3d_scanned"` | Created from 3D scanning |
| `Feature.LOW_POLY` | `"low_poly"` | Low polygon count |
| `Feature.HIGH_POLY` | `"high_poly"` | High polygon count |
| `Feature.GAME_READY` | `"game_ready"` | Optimized for game engines |
| `Feature.SCULPTING` | `"sculpting"` | Sculpted model |
| `Feature.GREASE_PENCIL` | `"grease_pencil"` | Uses Grease Pencil |
| `Feature.SYNTHETIC_DATA` | `"synthetic_data"` | For synthetic data generation |

**Example:**
```python
from blendflare import Feature

# Search for rigged and animated assets
results = client.search_projects(
    features=[Feature.RIGGED, Feature.ANIMATED]
)
```

---

## RenderEngine

Blender render engine compatibility.

| Enum Value | String Value |
|------------|--------------|
| `RenderEngine.CYCLES` | `"cycles"` |
| `RenderEngine.EEVEE` | `"eevee"` |
| `RenderEngine.WORKBENCH` | `"workbench"` |
| `RenderEngine.RENDERMAN` | `"renderman"` |
| `RenderEngine.VRAY` | `"vray"` |
| `RenderEngine.OCTANE` | `"octane"` |
| `RenderEngine.ARNOLD` | `"arnold"` |
| `RenderEngine.LUXCORE` | `"luxcore"` |

**Example:**
```python
from blendflare import RenderEngine

results = client.search_projects(
    render_engine=RenderEngine.CYCLES
)
```

---

## MaterialType

Type of materials used in the asset.

| Enum Value | String Value | Description |
|------------|--------------|-------------|
| `MaterialType.PROCEDURAL` | `"procedural"` | Procedurally generated materials |
| `MaterialType.TEXTURE_BASED` | `"texture_based"` | Uses texture maps |
| `MaterialType.BOTH` | `"both"` | Mix of procedural and texture-based |
| `MaterialType.NA` | `"na"` | Not applicable |

**Example:**
```python
from blendflare import MaterialType

results = client.search_projects(
    materials=MaterialType.PROCEDURAL
)
```

---

## UVMapping

UV mapping configuration of the asset.

| Enum Value | String Value | Description |
|------------|--------------|-------------|
| `UVMapping.NO_UV` | `"no_uv"` | No UV mapping |
| `UVMapping.OVERLAPPING` | `"overlapping"` | Overlapping UVs |
| `UVMapping.NON_OVERLAPPING` | `"non_overlapping"` | Non-overlapping UVs |
| `UVMapping.MIXED` | `"mixed"` | Mixed UV configuration |

**Example:**
```python
from blendflare import UVMapping

results = client.search_projects(
    uv_mapping=UVMapping.NON_OVERLAPPING
)
```

---

## Simulation

Physics simulation types included in the asset.

| Enum Value | String Value |
|------------|--------------|
| `Simulation.FLUID` | `"fluid"` |
| `Simulation.SMOKE` | `"smoke"` |
| `Simulation.CLOTH` | `"cloth"` |
| `Simulation.SOFT_BODY` | `"soft_body"` |
| `Simulation.RIGID_BODY` | `"rigid_body"` |
| `Simulation.HAIR` | `"hair"` |

**Example:**
```python
from blendflare import Simulation

results = client.search_projects(
    simulations=[Simulation.CLOTH, Simulation.HAIR]
)
```

---

## NodeGroupType

Types of node groups included.

| Enum Value | String Value |
|------------|--------------|
| `NodeGroupType.SHADING_NODES` | `"shading_nodes"` |
| `NodeGroupType.GEOMETRY_NODES` | `"geometry_nodes"` |
| `NodeGroupType.COMPOSITING_NODES` | `"compositing_nodes"` |

**Example:**
```python
from blendflare import NodeGroupType

results = client.search_projects(
    node_groups=[NodeGroupType.GEOMETRY_NODES]
)
```

---

## Physics

Physics features included in the asset.

| Enum Value | String Value |
|------------|--------------|
| `Physics.FORCE_FIELDS` | `"force_fields"` |
| `Physics.RIGID_BODY_CONSTRAINTS` | `"rigid_body_constraints"` |
| `Physics.COLLISION_OBJECTS` | `"collision_objects"` |

**Example:**
```python
from blendflare import Physics

results = client.search_projects(
    physics=[Physics.COLLISION_OBJECTS]
)
```

---

## GameEngine

Game engine compatibility.

| Enum Value | String Value |
|------------|--------------|
| `GameEngine.GODOT` | `"godot"` |
| `GameEngine.UNITY` | `"unity"` |
| `GameEngine.UNREAL_ENGINE` | `"unreal_engine"` |

**Example:**
```python
from blendflare import GameEngine

results = client.search_projects(
    game_engines=[GameEngine.UNITY, GameEngine.UNREAL_ENGINE]
)
```

---

## LicenseType

Asset licensing type.

| Enum Value | String Value | Description |
|------------|--------------|-------------|
| `LicenseType.CC0` | `"cc0"` | Public domain, no restrictions |
| `LicenseType.CC_BY` | `"cc_by"` | Attribution required |
| `LicenseType.CC_BY_SA` | `"cc_by_sa"` | Attribution + ShareAlike |
| `LicenseType.CC_BY_NC` | `"cc_by_nc"` | Attribution + Non-Commercial |
| `LicenseType.CC_BY_NC_SA` | `"cc_by_nc_sa"` | Attribution + Non-Commercial + ShareAlike |
| `LicenseType.CUSTOM` | `"custom"` | Custom license terms |
| `LicenseType.ALL_RIGHTS_RESERVED` | `"all_rights_reserved"` | All rights reserved |

**Example:**
```python
from blendflare import LicenseType

# Find only CC0 (public domain) assets
results = client.search_projects(
    license_type=LicenseType.CC0
)
```

---

## LegalFlag

Legal flags and content warnings for assets.

| Enum Value | String Value | Description |
|------------|--------------|-------------|
| `LegalFlag.FAN_ART` | `"fan_art"` | Fan-created content |
| `LegalFlag.CONTAINS_NSFW` | `"contains_nsfw"` | Contains NSFW content |
| `LegalFlag.TRADEMARKS` | `"trademarks"` | Contains trademarks |
| `LegalFlag.NO_AI_LICENSE` | `"no_ai_license"` | Cannot be used for AI training |
| `LegalFlag.AI_GENERATED` | `"ai_generated"` | AI-generated content |

**Example:**
```python
from blendflare import LegalFlag

# Find assets suitable for AI training (excluding no_ai_license)
results = client.search_projects(
    legal=[LegalFlag.FAN_ART]  # Can combine multiple flags
)
```

---

## SortBy

Fields to sort search results by.

| Enum Value | String Value | Description |
|------------|--------------|-------------|
| `SortBy.RELEVANCE` | `"relevance"` | Sort by search relevance (default) |
| `SortBy.NEWEST` | `"newest"` | Sort by upload date (newest first) |
| `SortBy.OLDEST` | `"oldest"` | Sort by upload date (oldest first) |
| `SortBy.POPULAR` | `"popular"` | Sort by popularity |
| `SortBy.DOWNLOADS` | `"downloads"` | Sort by download count |
| `SortBy.LIKES` | `"likes"` | Sort by likes count |
| `SortBy.VIEWS` | `"views"` | Sort by views count |
| `SortBy.BOOKMARKS` | `"bookmarks"` | Sort by bookmarks count |

**Example:**
```python
from blendflare import SortBy

# Get most popular assets
results = client.search_projects(
    q="car",
    sort_by=SortBy.POPULAR
)
```

---

## SortOrder

Sort direction for results.

| Enum Value | String Value | Description |
|------------|--------------|-------------|
| `SortOrder.ASC` | `"asc"` | Ascending order |
| `SortOrder.DESC` | `"desc"` | Descending order |

**Example:**
```python
from blendflare import SortBy, SortOrder

# Get oldest to newest
results = client.search_projects(
    sort_by=SortBy.NEWEST,
    sort_order=SortOrder.ASC
)
```

---

## Helper Functions

### `join_enum_values(values: List[Enum]) -> str`

Joins multiple enum values with `+` separator for API requests.

**Example:**
```python
from blendflare.types import join_enum_values, Feature

# Manually create filter string
features_str = join_enum_values([Feature.RIGGED, Feature.ANIMATED])
# Returns: "rigged+animated"
```

### `parse_tags(tags: List[str]) -> str`

Converts a list of tag strings into API format.

**Example:**
```python
from blendflare.types import parse_tags

tags_str = parse_tags(["vehicle", "red", "sports"])
# Returns: "vehicle+red+sports"
```

> **Note:** You typically don't need to call these functions directly as the `BlendflareClient` handles the conversion automatically.

---

## Complete Example

Here's a comprehensive example using multiple types:

```python
from blendflare import (
    BlendflareClient,
    Category,
    Subcategory,
    Style,
    Feature,
    RenderEngine,
    LicenseType,
    SortBy,
    SortOrder
)

client = BlendflareClient(api_key="sk_live_your_api_key")

# Complex search with multiple filters
results = client.search_projects(
    # Basic search
    q="sports car",
    category=Category.TRANSPORT,
    subcategory=Subcategory.CAR,
    style=Style.REALISTIC,
    
    # Technical requirements
    render_engine=RenderEngine.CYCLES,
    blender_version="4.4",
    
    # Asset features
    features=[Feature.RIGGED, Feature.ANIMATED, Feature.GAME_READY],
    
    # Polygon count range (1K to 50K)
    min_poly_count=1000,
    max_poly_count=50000,
    
    # License requirements
    license_type=LicenseType.CC0,
    
    # Popularity filters
    min_downloads=100,
    min_likes=50,
    
    # Sorting
    sort_by=SortBy.POPULAR,
    sort_order=SortOrder.DESC,
    
    # Pagination
    page=1,
    limit=20
)

print(f"Found {results.pagination.total} results")
for project in results.items:
    print(f"- {project.project_info.title}")
```