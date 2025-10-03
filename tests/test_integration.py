import sys
from io import StringIO
import pytest

from logger_pkg.factory import LoggerFactory
from logger_pkg.console_logger import ConsoleLogger
from logger_pkg.file_logger import FileLogger
from logger_pkg.kinds import LoggerKind
from logger_pkg.errors import LoggerConfigError


def test_integration_console_logger(monkeypatch):
    factory = LoggerFactory()

    # Captura saída do console
    fake_out = StringIO()
    monkeypatch.setattr(sys, "stdout", fake_out)

    logger = factory.create_logger("console")
    assert isinstance(logger, ConsoleLogger)

    logger.log("hello")
    logger.log(123)

    lines = fake_out.getvalue().splitlines()
    assert lines == ["hello", "123"]

    # Segunda chamada retorna mesma instância
    logger2 = factory.create_logger(LoggerKind.CONSOLE)
    assert logger2 is logger


def test_integration_file_logger(tmp_path):
    factory = LoggerFactory()
    FileLogger._reset_instance()  # limpa instância anterior

    log_path = tmp_path / "integration.log"
    logger = factory.create_logger("file", path=str(log_path))
    assert isinstance(logger, FileLogger)
    assert logger.path == str(log_path)

    logger.log("line one")
    logger.log("line two")

    content = log_path.read_text(encoding="utf-8").splitlines()
    assert content == ["line one", "line two"]

    # Segunda chamada sem path reaproveita instância
    logger2 = factory.create_logger(LoggerKind.FILE)
    assert logger2 is logger

    # Tentar reconfigurar com outro path deve falhar
    with pytest.raises(LoggerConfigError):
        factory.create_logger("file", path=str(tmp_path / "other.log"))
