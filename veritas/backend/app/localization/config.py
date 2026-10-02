"""Global-first localization configuration for VERITAS.

This module defines locale metadata only. Translation content and localized
product behaviour are introduced in the dedicated localization stage.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LocaleConfig:
    code: str
    name: str
    default: bool = False


DEFAULT_LOCALE = "en"


SUPPORTED_LOCALES: tuple[LocaleConfig, ...] = (
    LocaleConfig(
        code="en",
        name="English",
        default=True,
    ),
    LocaleConfig(
        code="ur-PK",
        name="Urdu",
    ),
)


def normalise_locale(locale: str | None) -> str:
    """Return a canonical supported locale or the global default."""

    if not locale:
        return DEFAULT_LOCALE

    candidate = locale.strip().replace("_", "-").lower()

    aliases = {
        "en": "en",
        "en-us": "en",
        "en-gb": "en",
        "ur": "ur-PK",
        "ur-pk": "ur-PK",
    }

    return aliases.get(candidate, DEFAULT_LOCALE)


def is_supported_locale(locale: str | None) -> bool:
    """Return whether the supplied locale is explicitly supported."""

    if not locale:
        return False

    candidate = locale.strip().replace("_", "-").lower()

    aliases = {
        "en": "en",
        "en-us": "en",
        "en-gb": "en",
        "ur": "ur-PK",
        "ur-pk": "ur-PK",
    }

    canonical = aliases.get(candidate)

    return canonical in {
        item.code
        for item in SUPPORTED_LOCALES
    }
