class LoggerError(Exception):
    """Erro genérico relacionado ao sistema de log."""
    pass


class LoggerConfigError(LoggerError):
    """Erro para problemas de configuração (ex.: FileLogger reconfigurado)."""
    pass
