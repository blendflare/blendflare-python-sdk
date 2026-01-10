# Blendflare Python SDK

[![PyPI version](https://badge.fury.io/py/blendflare.svg)](https://badge.fury.io/py/blendflare)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official Python SDK for the [Blendflare API](https://blendflare.com) - Search and download Blender projects with powerful filtering options.


>[!IMPORTANT]
API keys are intended for personal use only. Do not expose your API key in public apps, client-side code, or any environment where it could be accessed by others. Keep your key secure and private.

## Features

- 🔍 **Advanced Search** - Filter by category, style, features, and technical specs
- 📦 **Easy Downloads** - Generate download URLs for any asset
- 🎯 **Type Safety** - Full type hints and enum support for all parameters
- 🔧 **Blender Integration** - Perfect for building Blender add-ons

## Installation [NOT IMPLEMENTED YET]

```bash
pip install blendflare
```


## Quick Start

```python
from blendflare import BlendflareClient, Category, Feature, SortBy

# Initialize the client with your API key
client = BlendflareClient(api_key="sk_live_your_api_key")

# Search for rigged and animated sports cars
results = client.search_projects(
    q="sports car",
    category=Category.TRANSPORT,
    features=[Feature.RIGGED, Feature.ANIMATED],
    sort_by=SortBy.POPULAR,
    limit=20
)

# Display results
for project in results.items:
    # Project info
    print(f"Title: {project.project_info.title}")
    print(f"Tags: {', '.join(project.project_info.tags)}")
    
    # Slug
    print(f"Slug: {project.slug}")

    # Category and subcategory
    print(f"Category: {project.category}")
    print(f"Subcategory: {project.subcategory}")
    
    # Author
    print(f"Author: {project.author.nickname}")
    print(f"Avatar: {project.author.avatar_url}")
    
    # Stats
    print(f"Downloads: {project.stats.downloads_count}")
    print(f"Likes: {project.stats.likes_count}")
    print(f"Views: {project.stats.views_count}")
    
    # Technical specs
    print(f"Blender: {project.technical_specs.blender_version.full_version}")
    print(f"Render engine: {project.technical_specs.render_engine}")
    
    # File info
    print(f"File size: {project.file_info.file_size_mb:.2f} MB")
    print(f"Polygons: {project.file_info.poly_count}")
    
    # Legal
    print(f"License: {project.legal.license_type}")

# Download the first result
if results.items:
    download = client.download_project(
        project_slug=results.items[0].slug,
        nickname=results.items[0].author.nickname
    )
    print(f"Download URL: {download.data.download_url}")
    print(f"File size: {download.data.file_size_mb:.2f} MB")
```

## Getting Your API Key

1. Sign up at [Blendflare](https://blendflare.com)
2. Go to your [API Keys settings](https://blendflare.com/dashboard/settings/api-keys)
3. Create a new API key
4. Copy your key (format: `sk_live_...`)

## Usage Guide

### Basic Search

```python
from blendflare import BlendflareClient, Category

client = BlendflareClient(api_key="sk_live_your_api_key")

# Simple keyword search
results = client.search_projects(q="dragon")

# Search with category
results = client.search_projects(
    q="chair",
    category=Category.DECORATION
)

# Search by tags
results = client.search_projects(
    tags=["vehicle", "red", "sports"]
)
```

### Advanced Filtering

```python
from blendflare import (
    BlendflareClient,
    Category,
    Subcategory,
    Style,
    Feature,
    RenderEngine,
    LicenseType,
    SortBy
)

client = BlendflareClient(api_key="sk_live_your_api_key")

results = client.search_projects(
    # Basic filters
    q="character",
    category=Category.CHARACTER,
    subcategory=Subcategory.ROBOT,
    style=Style.REALISTIC,
    
    # Technical specs
    render_engine=RenderEngine.CYCLES,
    blender_version="4.4",
    
    # Features
    features=[Feature.RIGGED, Feature.ANIMATED, Feature.GAME_READY],
    
    # Polygon count range
    min_poly_count=1000,
    max_poly_count=50000,
    
    # License
    license_type=LicenseType.CC0,
    
    # Popularity filters
    min_downloads=100,
    min_likes=50,
    
    # Sorting
    sort_by=SortBy.POPULAR,
    
    # Pagination
    page=1,
    limit=20
)
```

### Working with Results

```python
results = client.search_projects(q="tree", category=Category.NATURE)

# Access metadata
print(f"Total results: {results.pagination.total}")
print(f"Search time: {results.metadata.search_time_ms}ms")

# Iterate through projects
for project in results.items:
    # Project info
    print(f"Title: {project.project_info.title}")
    print(f"Tags: {', '.join(project.project_info.tags)}")
    
    # Author
    print(f"Author: {project.author.nickname}")
    print(f"Avatar: {project.author.avatar_url}")
    
    # Stats
    print(f"Downloads: {project.stats.downloads_count}")
    print(f"Likes: {project.stats.likes_count}")
    print(f"Views: {project.stats.views_count}")
    
    # Technical specs
    print(f"Blender: {project.technical_specs.blender_version.full_version}")
    print(f"Render engine: {project.technical_specs.render_engine}")
    
    # File info
    print(f"File size: {project.file_info.file_size_mb:.2f} MB")
    print(f"Polygons: {project.file_info.poly_count}")
    
    # Legal
    print(f"License: {project.legal.license_type}")

# Pagination
if results.pagination.has_next_page:
    next_page = client.search_projects(
        q="tree",
        category=Category.NATURE,
        page=results.pagination.page + 1
    )
```

### Downloading Projects

```python
# Download a specific project
download = client.download_project(
    project_slug="sign-decal-pack",
    nickname="example_nickname"
)

# Access download information
print(f"Download URL: {download.data.download_url}")
print(f"File name: {download.data.file_name}")
print(f"File size: {download.data.file_size_mb:.2f} MB")
print(f"Expires in: {download.data.expires_in} seconds")
print(f"Is owner: {download.data.is_owner}")

# Download the file
import requests

response = requests.get(download.data.download_url)
with open(download.data.file_name, "wb") as f:
    f.write(response.content)
```

### Error Handling

```python
from blendflare import (
    BlendflareClient,
    AuthenticationError,
    ValidationError,
    RateLimitError,
    NotFoundError
)

client = BlendflareClient(api_key="sk_live_your_api_key")

try:
    results = client.search_projects(q="car", category="invalid_category")
except AuthenticationError:
    print("Invalid API key")
except ValidationError as e:
    print(f"Validation error: {e}")
    print(f"Details: {e.details}")
except RateLimitError as e:
    print(f"Rate limit exceeded")
except NotFoundError:
    print("Resource not found")
except Exception as e:
    print(f"Unexpected error: {e}")
```

See the [Types Reference](docs/TYPES_REFERENCE.md) for all available enums and their values.

## API Reference

### BlendflareClient

#### `__init__(api_key, base_url=None, timeout=30)`

Initialize the client.

**Parameters:**
- `api_key` (str): Your Blendflare API key (format: `sk_live_...`)
- `base_url` (str, optional): Custom API base URL
- `timeout` (int, optional): Request timeout in seconds

#### `search_projects(**kwargs) -> SearchResponse`

Search for projects with advanced filters.

**Parameters:** See [Usage Guide](#advanced-filtering) for all available parameters.

**Returns:** `SearchResponse` object containing:
- `message`: Response message
- `metadata`: Search metadata and statistics
- `items`: List of `Project` objects
- `pagination`: Pagination information

#### `download_project(project_slug, nickname) -> DownloadResponse`

Generate a download URL for a project.

**Parameters:**
- `project_slug` (str): Project slug identifier
- `nickname` (str): Author's nickname

**Returns:** `DownloadResponse` object containing:
- `message`: Response message
- `data`: `DownloadData` object with URL and file info

## Rate Limits

API requests are rate-limited per API key. If you exceed the limit, you'll receive a `RateLimitError`.


## Support

- 📖 [Documentation](https://docs.blendflare.com)
- 📧 Email: support@blendflare.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.