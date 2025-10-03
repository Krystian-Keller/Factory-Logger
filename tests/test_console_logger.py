import pytest
from logger_pkg.console_logger import ConsoleLogger
from io import StringIO
import sys


def test_console_logger_singleton_identity():
    c1 = ConsoleLogger()
    c2 = ConsoleLogger()
    assert c1 is c2


def test_console_logger_prints_to_stdout(monkeypatch):
    logger = ConsoleLogger()

    # Captura a saída do print
    fake_out = StringIO()
    monkeypatch.setattr(sys, "stdout", fake_out)

    logger.log("hello world")
    logger.log(123)

    output = fake_out.getvalue().strip().splitlines()
    assert output == ["hello world", "123"]
