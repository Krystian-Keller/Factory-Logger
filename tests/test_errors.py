import pytest
from logger_pkg.errors import LoggerError, LoggerConfigError
from logger_pkg.file_logger import FileLogger


def test_logger_error_is_base_class():
    assert issubclass(LoggerConfigError, LoggerError)


def test_file_logger_raises_config_error(tmp_path):
    FileLogger._reset_instance()
    p1 = tmp_path / "a.log"
    p2 = tmp_path / "b.log"

    FileLogger(str(p1))
    with pytest.raises(LoggerConfigError):
        FileLogger(str(p2))
