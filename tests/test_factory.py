import pytest
from logger_pkg.factory import LoggerFactory
from logger_pkg.console_logger import ConsoleLogger
from logger_pkg.file_logger import FileLogger
from logger_pkg.kinds import LoggerKind


def test_factory_is_singleton():
    f1 = LoggerFactory()
    f2 = LoggerFactory()
    assert f1 is f2


def test_factory_creates_console_logger_by_string_and_enum():
    # String (case-insensitive)
    lf = LoggerFactory()
    c1 = lf.create_logger("console")
    assert isinstance(c1, ConsoleLogger)

    c2 = lf.create_logger("CONSOLE")  # mesma instância (produto é singleton)
    assert c1 is c2

    # Enum
    c3 = lf.create_logger(LoggerKind.CONSOLE)
    assert c3 is c1


def test_factory_creates_file_logger_and_passes_path(tmp_path):
    # resetar o singleton do FileLogger para evitar sujeira entre testes
    FileLogger._reset_instance()

    lf = LoggerFactory()
    p = tmp_path / "factory.log"
    fl = lf.create_logger("file", path=str(p))
    assert isinstance(fl, FileLogger)
    assert fl.path == str(p)

    # Chamadas subsequentes sem path reaproveitam a instância
    fl2 = lf.create_logger(LoggerKind.FILE)
    assert fl2 is fl


def test_factory_unknown_kind_falls_back_to_console():
    lf = LoggerFactory()
    logger = lf.create_logger("unknown-kind")
    assert isinstance(logger, ConsoleLogger)
