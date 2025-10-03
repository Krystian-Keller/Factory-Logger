# main.py
from __future__ import annotations

import argparse
import sys

from logger_pkg.factory import LoggerFactory
from logger_pkg.kinds import LoggerKind
from logger_pkg.errors import LoggerError, LoggerConfigError


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="logger_tool",
        description="Demo simples de Logger com Factory Method + Singleton.",
    )
    parser.add_argument(
        "--kind",
        choices=[LoggerKind.CONSOLE.value, LoggerKind.FILE.value],
        help="Tipo de logger: console ou file.",
    )
    parser.add_argument(
        "--path",
        help="Caminho do arquivo de log (obrigatório se --kind file).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    # Entrada interativa se nada for passado
    kind_value = args.kind
    if not kind_value:
        kind_value = input("Escolha o tipo de logger [console/file]: ").strip().lower() or "console"

    # Se for file e não tem path, perguntar
    path = args.path
    if kind_value == LoggerKind.FILE.value and not path:
        path = input("Informe o caminho do arquivo de log: ").strip()

    factory = LoggerFactory()

    try:
        if kind_value == LoggerKind.FILE.value:
            logger = factory.create_logger(kind_value, path=path)
        else:
            logger = factory.create_logger(kind_value)
    except LoggerConfigError as e:
        print(f"[config error] {e}", file=sys.stderr)
        return 2
    except LoggerError as e:
        print(f"[logger error] {e}", file=sys.stderr)
        return 1

    # Demonstração simples
    print(f"-> Logger escolhido: {kind_value!r}")
    if kind_value == LoggerKind.FILE.value:
        # type: ignore[attr-defined]  # FileLogger tem .path
        print(f"-> Escrevendo no arquivo: {logger.path}")

    logger.log("Primeira linha de log")
    logger.log("Segunda linha de log")
    logger.log({"payload": 123, "ok": True})

    print("-> Feito. Veja a saída acima (console) ou o arquivo de log.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
