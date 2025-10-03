from logger_pkg.kinds import LoggerKind


def test_logger_kind_values():
    assert LoggerKind.CONSOLE.value == "console"
    assert LoggerKind.FILE.value == "file"


def test_from_value_normalizes_and_defaults():
    assert LoggerKind.from_value("console") is LoggerKind.CONSOLE
    assert LoggerKind.from_value("CONSOLE") is LoggerKind.CONSOLE
    assert LoggerKind.from_value("  CoNsOlE  ") is LoggerKind.CONSOLE

    assert LoggerKind.from_value("file") is LoggerKind.FILE
    assert LoggerKind.from_value("FILE") is LoggerKind.FILE
    assert LoggerKind.from_value("  fIlE  ") is LoggerKind.FILE

    # default/fallback
    assert LoggerKind.from_value(None) is LoggerKind.CONSOLE
    assert LoggerKind.from_value("") is LoggerKind.CONSOLE
    assert LoggerKind.from_value("unknown-kind") is LoggerKind.CONSOLE
