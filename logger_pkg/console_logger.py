# logger_pkg/console_logger.py

from __future__ import annotations
from .logger import Logger
from .singleton import Singleton


class ConsoleLogger(Logger, metaclass=Singleton):
    """Escreve logs no terminal (stdout)."""

    def log(self, message: str) -> None:
        # Conversão defensiva para string e flush imediato no console.
        print(str(message), flush=True)
