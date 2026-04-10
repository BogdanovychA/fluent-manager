# fluent-manager

[![DOI](https://zenodo.org/badge/1186346418.svg)](https://doi.org/10.5281/zenodo.19492979)

🌐 Переклади: [🇬🇧 English](https://github.com/BogdanovychA/fluent-manager/blob/main/README.md) · [🇵🇱 Polski](https://github.com/BogdanovychA/fluent-manager/blob/main/README.pl.md)

Легковісний менеджер локалізації на основі [Project Fluent](https://projectfluent.org/) з автоматичним fallback між локалями.

## Встановлення

```bash
pip install fluent-manager
```

## Можливості

- Простий API для отримання локалізованих рядків
- Автоматичний ланцюг fallback: пріоритетні локалі → локаль за замовчуванням → сам ключ
- Автовизначення доступних локалей і `.ftl` файлів з файлової системи
- Підтримка кількох пріоритетних локалей

## Структура директорій

```
locales/
├── en/
│   └── messages.ftl
├── uk/
│   └── messages.ftl
└── pl/
    └── messages.ftl
```

## Використання

```python
from fluent_manager import FluentManager

lang_manager = FluentManager(
    locales=["uk", "pl"],
    locales_path="/шлях/до/locales",
    default_locale="en",
)

# Повертає локалізований рядок у першій доступній локалі
message = lang_manager.get("welcome-message", user_name="Андрій")
```

## Поведінка fallback

| Ситуація | Результат |
|---|---|
| Ключ є у першій пріоритетній локалі | Повертається рядок першої локалі |
| Ключ відсутній у першій, є у наступній | Повертається рядок наступної локалі |
| Ключ є лише у локалі за замовчуванням | Повертається рядок локалі за замовчуванням |
| Ключ відсутній у всіх локалях | Повертається сам ключ |

## API

### `FluentManager(locales, locales_path, default_locale=None)`

| Параметр | Тип | Опис                                                  |
|---|---|-------------------------------------------------------|
| `locales` | `list` | Локалі у порядку пріоритету, наприклад `["uk", "pl"]` |
| `locales_path` | `str` | Шлях до директорії з піддиректоріями локалей          |
| `default_locale` | `str \| None` | Резервна локаль. За замовчуванням `"en"`              |

### `FluentManager.get(key, **kwargs) -> str`

Повертає локалізований рядок за ключем з опціональними змінними.

### `FluentManager.languages -> list`

Список усіх доступних локалей, визначених з файлової системи.

## Посилання

- [Project Fluent](https://projectfluent.org/)
- [Репозиторій](https://github.com/BogdanovychA/fluent-manager)
