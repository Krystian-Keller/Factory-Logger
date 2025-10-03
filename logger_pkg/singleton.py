from __future__ import annotations
from abc import ABCMeta

class Singleton(ABCMeta):
    _instances: dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            # Gancho para validar re-chamadas (reconfiguração)
            validator = getattr(cls, "_validate_reinit_args", None)
            if callable(validator):
                validator(cls._instances[cls], *args, **kwargs)
        return cls._instances[cls]

    def _reset_instance(cls) -> None:
        cls._instances.pop(cls, None)
