from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader


class FluentManager:
    """Manages localisation using Project Fluent.

    Loads .ftl resources from a directory structure where each subdirectory
    represents a locale (e.g. locales/en/, locales/pl/).

    Attributes:
        locales: List of preferred locales in priority order.
        default_locale: Fallback locale used when a key is missing in preferred locales.
        locales_path: Path to the directory containing locale subdirectories.
        languages: List of all available locales detected from the filesystem.
        resource_ids: List of .ftl filenames discovered in the default locale directory.
        l10n: Underlying FluentLocalization instance.
    """

    def __init__(
        self, locales: list, locales_path: str, default_locale: str | None = None
    ) -> None:
        """Initialises FluentManager.

        Args:
            locales: Preferred locales in priority order (e.g. ["pl", "uk"]).
            locales_path: Absolute or relative path to the locales directory.
            default_locale: Fallback locale if a key is not found in preferred locales.
                Defaults to "en".
        """

        self.locales = locales
        self.default_locale = default_locale or "en"

        self.locales_path = Path(locales_path)
        self.loader = FluentResourceLoader([str(self.locales_path / "{locale}")])

        self.languages = [d.name for d in self.locales_path.iterdir() if d.is_dir()]

        default_lang_dir = self.locales_path / self.default_locale
        self.resource_ids = [f.name for f in default_lang_dir.glob("*.ftl")]

        self.l10n = FluentLocalization(
            [*self.locales, self.default_locale], self.resource_ids, self.loader
        )

    def get(self, key, **kwargs) -> str:
        """Retrieves a localised string by key.

        Args:
            key: The Fluent message identifier (e.g. "welcome-message").
            **kwargs: Optional variables passed to the Fluent message as arguments.

        Returns:
            Localised string for the first matching locale in the priority list.
            Falls back to default_locale if the key is not found in preferred locales.
        """

        return self.l10n.format_value(key, kwargs or None)
