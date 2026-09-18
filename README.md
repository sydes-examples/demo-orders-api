# Demo Orders API

A tiny FastAPI application for creating orders against a fixed in-memory product inventory.

## Setup

Requires Python 3.11 or newer.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
pip install ".[dev]"
```

## Run

```bash
uvicorn app.main:app --reload
```

## Test

```bash
pytest
```

## Examples

```bash
curl http://127.0.0.1:8000/health
```

```bash
curl http://127.0.0.1:8000/inventory/BOOK-001
```

```bash
curl -X POST http://127.0.0.1:8000/orders \
  -H "Content-Type: application/json" \
  -d '{"sku":"BOOK-001","quantity":3}'
```
