# Why use `fluent-manager` instead of `fluent.runtime`?

While `fluent.runtime` provides the core Project Fluent functionality, `fluent-manager` is a high-level wrapper designed for developer convenience and real-world application needs.

## 1. Automatic Resource Discovery
- **`fluent.runtime`**: Requires manually loading each `.ftl` file and creating a `FluentResourceLoader`.
- **`fluent-manager`**: Automatically scans the `locales_path` and finds all `.ftl` files for all available languages. You only provide the directory path.

## 2. Simplified Locale Fallback
- **`fluent.runtime`**: Requires managing the fallback list yourself.
- **`fluent-manager`**: Automatically constructs a robust fallback chain: `Preferred Locales` -> `Default Locale` -> `Key ID`.

## 3. Cleaner API
- **`fluent.runtime`**: Use `FluentLocalization.format_value(key, args)`.
- **`fluent-manager`**: Use `FluentManager.get(key, **kwargs)`. It feels more idiomatic and less verbose.

## 4. Automatic Locale Detection
- **`fluent-manager`**: Exposes `languages` attribute which lists all locales found on disk, making it easy to validate user-requested languages against available ones.

## Conclusion
Use `fluent-manager` if you want to avoid boilerplate code for file loading and manual fallback management. It's "Fluent for Humans."
