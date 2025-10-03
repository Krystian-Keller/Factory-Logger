import pytest
from logger_pkg.logger import Logger

def test_logger_nao_pode_ser_instanciado():
    # ABC não deve permitir instanciar diretamente
    with pytest.raises(TypeError):
        Logger()  # type: ignore[abstract]

def test_subclasse_minima_funciona():
    # cria uma subclasse “fake” só para validar o contrato
    class DummyLogger(Logger):
        def __init__(self):
            self.buffer = []

        def log(self, message: str) -> None:
            self.buffer.append(message)

    dl = DummyLogger()
    dl.log("hello")
    dl.log("world")

    assert dl.buffer == ["hello", "world"]
