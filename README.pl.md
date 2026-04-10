# fluent-manager

[![DOI](https://zenodo.org/badge/1186346418.svg)](https://doi.org/10.5281/zenodo.19492979)

🌐 Tłumaczenia: [🇬🇧 English](https://github.com/BogdanovychA/fluent-manager/blob/main/README.md) · [🇺🇦 Українська](https://github.com/BogdanovychA/fluent-manager/blob/main/README.uk.md)

Lekki menedżer lokalizacji oparty na [Project Fluent](https://projectfluent.org/) z automatycznym fallback między lokalizacjami.

## Instalacja

```bash
pip install fluent-manager
```

## Funkcje

- Proste API do pobierania zlokalizowanych ciągów znaków
- Automatyczny łańcuch fallback: preferowane lokalizacje → domyślna lokalizacja → sam klucz
- Automatyczne wykrywanie dostępnych lokalizacji i plików `.ftl` z systemu plików
- Obsługa wielu preferowanych lokalizacji w kolejności priorytetu

## Struktura katalogów

```
locales/
├── en/
│   └── messages.ftl
├── uk/
│   └── messages.ftl
└── pl/
    └── messages.ftl
```

## Użycie

```python
from fluent_manager import FluentManager

lang_manager = FluentManager(
    locales=["pl", "uk"],
    locales_path="/ścieżka/do/locales",
    default_locale="en",
)

# Zwraca zlokalizowany ciąg w pierwszej pasującej lokalizacji
message = lang_manager.get("welcome-message", user_name="Andrzej")
```

## Zachowanie fallback

| Sytuacja | Wynik |
|---|---|
| Klucz istnieje w pierwszej preferowanej lokalizacji | Zwracany jest ciąg pierwszej lokalizacji |
| Klucz brakuje w pierwszej, istnieje w następnej | Zwracany jest ciąg następnej lokalizacji |
| Klucz istnieje tylko w domyślnej lokalizacji | Zwracany jest ciąg domyślnej lokalizacji |
| Klucz nie istnieje w żadnej lokalizacji | Zwracany jest sam klucz |

## API

### `FluentManager(locales, locales_path, default_locale=None)`

| Parametr | Typ | Opis |
|---|---|---|
| `locales` | `list` | Preferowane lokalizacje w kolejności priorytetu, np. `["pl", "uk"]` |
| `locales_path` | `str` | Ścieżka do katalogu zawierającego podkatalogi lokalizacji |
| `default_locale` | `str \| None` | Zapasowa lokalizacja. Domyślnie `"en"` |

### `FluentManager.get(key, **kwargs) -> str`

Zwraca zlokalizowany ciąg znaków według klucza z opcjonalnymi zmiennymi.

### `FluentManager.languages -> list`

Lista wszystkich dostępnych lokalizacji wykrytych z systemu plików.

## Linki

- [Project Fluent](https://projectfluent.org/)
- [Repozytorium](https://github.com/BogdanovychA/fluent-manager)
