# fluent-manager

[![DOI](https://zenodo.org/badge/1186346418.svg)](https://doi.org/10.5281/zenodo.19492979) [![PyPI Downloads](https://static.pepy.tech/personalized-badge/fluent-manager?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/fluent-manager) ![PyPI - License](https://img.shields.io/pypi/l/fluent-manager?logoColor=grey&color=blue) ![PyPI - Version](https://img.shields.io/pypi/v/fluent-manager?logoColor=grey&color=blue)

Translations: [🇺🇦 Українська](https://github.com/BogdanovychA/fluent-manager/blob/main/README.uk.md) · [🇵🇱 Polski](https://github.com/BogdanovychA/fluent-manager/blob/main/README.pl.md)

Lightweight [Project Fluent](https://projectfluent.org/) localisation manager with automatic locale fallback.

## Installation

```bash
pip install fluent-manager
```

## Features

- Simple API for retrieving localised strings
- Automatic fallback chain: preferred locales → default locale → key itself
- Auto-discovery of available locales and `.ftl` resource files from the filesystem
- Supports multiple preferred locales in priority order

## Directory structure

```
locales/
├── en/
│   └── messages.ftl
├── uk/
│   └── messages.ftl
└── pl/
    └── messages.ftl
```

## Usage

```python
from fluent_manager import FluentManager

lang_manager = FluentManager(
    locales=["uk", "pl"],
    locales_path="/path/to/locales",
    default_locale="en",
)

# Returns localised string in the first matching locale
message = lang_manager.get("welcome-message", user_name="Andrii")
```

## Fallback behaviour

| Situation | Result |
|---|---|
| Key exists in first preferred locale | Renders in first preferred locale |
| Key missing in first locale, exists in next | Renders in next preferred locale |
| Key exists only in default locale | Renders in default locale |
| Key missing in all locales | Returns the key itself |

## API

### `FluentManager(locales, locales_path, default_locale=None)`

| Parameter | Type | Description |
|---|---|---|
| `locales` | `list` | Preferred locales in priority order, e.g. `["uk", "pl"]` |
| `locales_path` | `str` | Path to the directory containing locale subdirectories |
| `default_locale` | `str \| None` | Fallback locale. Defaults to `"en"` |

### `FluentManager.get(key, **kwargs) -> str`

Retrieves a localised string by key with optional variables.

### `FluentManager.languages -> list`

List of all available locales detected from the filesystem.

## AI Agent Skill

This repository contains a specialised skill for AI agents (such as Gemini CLI). It helps the agent provide expert assistance in writing Python code and integrating this library into your projects.

To install the skill, run:
```bash
npx skills add BogdanovychA/fluent-manager --skill fluent-manager
```

## Links

- [Project Fluent](https://projectfluent.org/)
- [Repository](https://github.com/BogdanovychA/fluent-manager)
