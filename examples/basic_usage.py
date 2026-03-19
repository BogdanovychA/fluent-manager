from pathlib import Path

from fluent_manager import FluentManager

if __name__ == "__main__":
    current_dir = Path(__file__).parent
    lang_manager = FluentManager(
        ["uk", "pl"], str(current_dir / "locales"), default_locale="en"
    )

    print(f"All locales: {lang_manager.languages}", end="\n\n")

    # Key exists in all locales — renders in first preferred locale (uk)
    print(
        lang_manager.get(
            "test-message",
            user_name="Andrii",
            tasks_count=3,
        ),
        end="\n\n",
    )

    # Key exists only in default locale (en) — fallback renders in English
    print(lang_manager.get("test-message-1"), end="\n\n")

    # Key missing in uk, exists in pl and en — next preferred locale (pl) is used
    print(lang_manager.get("test-message-2"), end="\n\n")

    # Key does not exist in any locale — Fluent returns the key itself as a fallback
    print(lang_manager.get("test-message-3"))
