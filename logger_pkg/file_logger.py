# logger_pkg/file_logger.py
from __future__ import annotations
from .logger import Logger
from .singleton import Singleton
from .errors import LoggerConfigError

class FileLogger(Logger, metaclass=Singleton):
    def __init__(self, path: str | None = None) -> None:
        if not hasattr(self, "_path"):
            if not path:
                raise LoggerConfigError("FileLogger requires a path on first initialization.")
            self._path = str(path)

   
    def _validate_reinit_args(self, path: str | None = None, **_):
        if path and str(path) != getattr(self, "_path", None):
            raise LoggerConfigError(
        f"FileLogger already configured for '{self._path}', "
        f"received different path '{path}'."
    )

    @property
    def path(self) -> str:
        return self._path

    def log(self, message: str) -> None:
        if not hasattr(self, "_path"):
            raise RuntimeError("FileLogger not configured with a path.")
        with open(self._path, mode="a", encoding="utf-8") as f:
            f.write(f"{str(message)}\n")
            f.flush()
