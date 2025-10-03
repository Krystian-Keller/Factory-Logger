from __future__ import annotations
from typing import Any, Dict, Type

from .singleton import Singleton
from .logger import Logger
from .console_logger import ConsoleLogger
from .file_logger import FileLogger
from .kinds import LoggerKind


class LoggerFactory(metaclass=Singleton):
    """Ponto único de criação de loggers (Factory Method)."""

    # Registry simples: kind.value -> classe concreta
    _registry: Dict[str, Type[Logger]] = {
        LoggerKind.CONSOLE.value: ConsoleLogger,
        LoggerKind.FILE.value: FileLogger,
    }

    def create_logger(self, kind: str | LoggerKind | None, **options: Any) -> Logger:
        """
        Decide qual logger criar e retorna a instância (produtos são Singletons).
        - kind pode ser string, enum ou None (fallback = console).
        - **options repassado ao construtor (ex.: path= para FileLogger).
        """
        # Normaliza o tipo
        if isinstance(kind, LoggerKind):
            lk = kind
        else:
            lk = LoggerKind.from_value(kind)

        # Seleciona classe concreta com fallback para Console
        logger_cls = self._registry.get(lk.value, ConsoleLogger)

        # Instancia (ou reaproveita) — produtos são Singletons
        return logger_cls(**options)

    # (Opcional) permitir extensão externa do registry
    def register(self, kind: str | LoggerKind, cls: Type[Logger]) -> None:
        key = kind.value if isinstance(kind, LoggerKind) else LoggerKind.from_value(str(kind)).value
        self._registry[key] = cls
