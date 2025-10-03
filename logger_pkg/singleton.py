# logger_pkg/singleton.py
from __future__ import annotations


class Singleton(type):
    """
    Metaclass to ensure exactly one instance per concrete class.

    Usage:
        class MyClass(metaclass=Singleton):
            pass

        a = MyClass()
        b = MyClass()
        assert a is b
    """

    _instances: dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        # Create the instance once; subsequent calls return the cached one.
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    # Helper for tests: allows resetting the cached instance of a given class.
    def _reset_instance(cls) -> None:
        """
        Reset the singleton instance for this class.
        Useful in tests to force re-creation with different constructor args.
        """
        cls._instances.pop(cls, None)
