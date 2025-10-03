from __future__ import annotations
from enum import Enum


class LoggerKind(str, Enum):
    CONSOLE = "console"
    FILE = "file"

    @classmethod
    def from_value(cls, value: str | None) -> "LoggerKind":
        """Normaliza a string (case-insensitive) e retorna o enum; default = CONSOLE."""
        if not value:
            return cls.CONSOLE
        value = value.strip().lower()
        if value in (cls.CONSOLE.value,):
            return cls.CONSOLE
        if value in (cls.FILE.value,):
            return cls.FILE
        # fallback simples para manter robustez (vamos evitar exceptions aqui)
        return cls.CONSOLE
