---
category: Tutorials
tags: ["build", "packaging"]
---

# Building and Packaging Projects

There are two separate concerns in this repository: building the engine for development, and packaging the Hub for distribution.

## Development build

```bash
conda activate infengine
pip install -r requirements.txt
cmake --preset release
cmake --build --preset release
```

## Packaging

- `cmake --build --preset packaging` builds the standalone Hub bundle.
- `cmake --build --preset packaging-installer` builds the graphical Windows installer.

## Documentation build

```bash
conda activate infengine
python docs/wiki/generate_api_docs.py
python -m mkdocs build --clean -f docs/wiki/mkdocs.yml
```
