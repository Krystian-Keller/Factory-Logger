# Logger Tool (Factory Method + Singleton)

Pequena ferramenta de logs para demonstrar **Factory Method** e **Singleton** em Python.

## Estrutura

```
logger_tool/
├─ logger_pkg/
│  ├─ __init__.py
│  ├─ logger.py            # contrato (ABC)
│  ├─ singleton.py         # metaclasse Singleton (compatível com ABCMeta)
│  ├─ console_logger.py    # logger de console (Singleton)
│  ├─ file_logger.py       # logger de arquivo (Singleton, "first path wins")
│  ├─ kinds.py             # enum LoggerKind (console/file)
│  ├─ factory.py           # LoggerFactory (Singleton, registry + fallback)
│  ├─ errors.py            # LoggerError / LoggerConfigError
├─ tests/
│  ├─ test_*.py            # unitários + integração (pytest)
└─ main.py                 # ponto de entrada do programa (CLI/demo)
```

## Requisitos

- Python 3.10+
- pip / venv
- (dev) pytest

## Setup rápido

```bash
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# Windows (CMD)
.\.venv\Scripts\activate.bat
# Linux/Mac
source .venv/bin/activate

python -m pip install --upgrade pip
pip install pytest
```

## Rodando os testes

```bash
pytest -q
```

## Uso (CLI)

### Console
```bash
python main.py --kind console
```

### Arquivo
```bash
python main.py --kind file --path app.log
```

Se você não passar argumentos, a CLI pergunta interativamente.

## Comportamento importante

- **Singleton**: `ConsoleLogger`, `FileLogger` e `LoggerFactory` produzem sempre **uma única instância** por classe.
- **FileLogger — “first path wins”**:
  - A **primeira** inicialização deve informar `path`.
  - Chamadas futuras **reutilizam** a instância existente.
  - Tentar reconfigurar com outro `path` gera `LoggerConfigError`.
- **Factory Method**:
  - `LoggerFactory.create_logger(kind, **opts)` escolhe o produto concreto (`ConsoleLogger` ou `FileLogger`), com **fallback para console** quando `kind` é inválido/nulo.
- **Saída**:
  - Console: prints diretos (usa `str(...)`).
  - Arquivo: `append` em UTF-8, uma linha por mensagem.

## Exemplos

```bash
# Console
python main.py --kind console
# file
python main.py --kind file --path logs/app.log
# sem args (interativo)
python main.py
```

## Extensão (opcional)

- Registrar novos tipos na `LoggerFactory.register(kind, cls)`.
- Trocar a formatação do console (ex.: JSON) alterando `ConsoleLogger.log`.
- Tornar Singleton thread-safe adicionando locks em `singleton.py`.

## Licença

MIT (ou a que você preferir).
