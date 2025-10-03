# logger_pkg/singleton.py
from __future__ import annotations
from abc import ABCMeta


class Singleton(ABCMeta):
    """
    Metaclass to ensure exactly one instance per concrete class.
    Compatible with ABCs (inherits from ABCMeta).
    """

    _instances: dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def _reset_instance(cls) -> None:
        cls._instances.pop(cls, None)
