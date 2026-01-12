## Installation

### From PyPI (Recommended) [NOT IMPLEMENTED YET]

Once published, you can install the SDK using pip:

```bash
pip install blendflare
```

### From Source

```bash
# Clone the repository
git clone https://github.com/blendflare/blendflare-python.git
cd blendflare-python

# Install in development mode
pip install -e .

# Or install with dev dependencies
pip install -e ".[dev]"
```

### Requirements

- Python 3.8 or higher
- `requests` library (automatically installed)

## Getting Your API Key

1. **Sign up** at [https://blendflare.com](https://blendflare.com)
2. **Navigate** to your [API Keys settings](https://blendflare.com/dashboard/settings/api-keys)
3. **Create** a new API key
4. **Copy** your key (format: `sk_live_...`)

⚠️ **Important**: Keep your API key secure and never commit it to version control!

## Quick Start

### Basic Usage

```python
from blendflare import BlendflareClient, Category, SortBy

# Initialize the client
client = BlendflareClient(api_key="sk_live_your_api_key")

# Search for assets
results = client.search_projects(
    q="dragon",
    category=Category.CHARACTER,
    sort_by=SortBy.POPULAR,
    limit=10
)

# Display results
for project in results.items:
    print(f"{project.project_info.title} by {project.author.nickname}")
```

### Download an Asset

```python
# Download the first result
if results.items:
    download = client.download_project(
        project_slug=results.items[0].slug,
        nickname=results.items[0].author.nickname
    )
    
    print(f"Download URL: {download.data.download_url}")
    
    # Download the file
    import requests
    response = requests.get(download.data.download_url)
    with open(download.data.file_name, "wb") as f:
        f.write(response.content)
```

## Building from Source

### Build Distribution Package

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# This creates:
# - dist/blendflare-1.0.2-py3-none-any.whl
# - dist/blendflare-1.0.2.tar.gz
```

### Install Built Package

```bash
# Install the wheel
pip install dist/blendflare-1.0.2-py3-none-any.whl

# Or install the source distribution
pip install dist/blendflare-1.0.2.tar.gz
```

### Publish to PyPI (Maintainers Only)

```bash
# Test PyPI first
twine upload --repository testpypi dist/*

# Production PyPI
twine upload dist/*
```