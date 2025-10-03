# logger_pkg/logger.py
from __future__ import annotations
from abc import ABC, abstractmethod


class Logger(ABC):
    """Contrato mínimo para loggers."""

    @abstractmethod
    def log(self, message: str) -> None:
        """Registra uma mensagem de log."""
        raise NotImplementedError
