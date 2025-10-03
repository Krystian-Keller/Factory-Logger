import pytest
from logger_pkg.file_logger import FileLogger


def test_file_logger_requires_path_on_first_init(tmp_path):
    # reset para garantir ambiente limpo entre execuções
    FileLogger._reset_instance()
    with pytest.raises(RuntimeError):
        FileLogger()  # sem path na primeira criação não pode


def test_file_logger_singleton_identity(tmp_path):
    FileLogger._reset_instance()
    p = tmp_path / "app.log"
    a = FileLogger(str(p))
    b = FileLogger()
    assert a is b
    assert a.path == str(p)


def test_file_logger_first_path_wins_and_different_path_raises(tmp_path):
    FileLogger._reset_instance()
    p1 = tmp_path / "one.log"
    p2 = tmp_path / "two.log"

    FileLogger(str(p1))  # primeira configuração
    # Mesmo path é ok (reuso):
    FileLogger(str(p1))

    # Path diferente deve falhar:
    with pytest.raises(RuntimeError):
        FileLogger(str(p2))


def test_file_logger_writes_lines_to_file(tmp_path):
    FileLogger._reset_instance()
    p = tmp_path / "events.log"
    logger = FileLogger(str(p))

    logger.log("hello")
    logger.log(123)

    content = p.read_text(encoding="utf-8").splitlines()
    assert content == ["hello", "123"]
