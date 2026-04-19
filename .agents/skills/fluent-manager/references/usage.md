# `fluent-manager` Usage Guide

## Setup

```python
from fluent_manager import FluentManager

# Initialise with preferred locales, path to locales folder, and a default fallback
lang_manager = FluentManager(
    locales=["uk", "pl"],
    locales_path="locales",
    default_locale="en"
)
```

## Directory Structure Requirement
The library expects a directory per locale:
```
locales/
├── en/
│   └── main.ftl
├── uk/
│   └── main.ftl
└── pl/
    └── main.ftl
```

## Getting Messages

### Simple message
```python
text = lang_manager.get("welcome-message")
```

### With variables
```python
# .ftl: hello = Hello, { $name }!
text = lang_manager.get("hello", name="Andrii")
```

## Available Languages
Check which languages are supported by the current filesystem structure:
```python
print(lang_manager.languages) # e.g. ["en", "uk", "pl"]
```

## Fallback Logic
1. Try each locale in `locales` list.
2. If not found, try `default_locale`.
3. If still not found, return the `key` itself.
