# Adventurer Journey Backend

A flask backend built with a layered architecture 
(Controller → Use Case → Service → Model).

## Tech Stack

| Layer         | Technology                          |
| ------------- | ------------------------------------ |
| Language      | Python 3.11+                        |
| Framework     | Flask 3                             |
| Database      | SQLite via SQLAlchemy 2.0 ORM       |
| Dependencies  | Poetry                              |
| Testing       | pytest                              |


## Getting Started

### Prerequisites

- **Python >= 3.11** (verify with `python3 --version`)
- **Poetry** (`pipx install poetry` or see [python-poetry.org](https://python-poetry.org/docs/#installation))

## Demo

```bash
# Install dependencies
poetry install

# Run the API (defaults to sqlite:///moves.db in the project root)
poetry run python -m app.main

# If port 5000 is already in use lsof -i :5000 to find process, then kill

# Run the demo by hitting the API with the provided move string
bash run_demo.sh
```

The database persists between runs, so reset it first if you want a clean setup:

```bash
rm -f moves.db   # then restart the app
```

## Running Tests

```bash
poetry run pytest
```

## Project Structure

```
app/
  main.py             Flask application factory / entrypoint
  db.py               SQLAlchemy engine/session setup
  models/             SQLAlchemy ORM models (Adventurer, Move)
  parsers/            Move parser
    move_parser.py    Main logic for parsing individual moves from stream as defined in project scope
  use_cases/          Orchestrators (MoveAdventurerUseCase)
  controllers/        Flask blueprints - thin, HTTP only
  errors/             Typed ApiError hierarchy
tests/
  unit/               service-level tests
  integration/        Full request/response tests via the Flask test client
```

## Architecture Decisions

- **Strict layering**: Controllers parse requests and call a use case; use cases
  orchestrate services; services are the only thing that touches models.
- **Typed errors**: Services and integrations raise a subclass of `ApiError`
  (`app/errors/errors.py`) rather than a bare `Exception`. `app/errors/handler.py`
  maps errors to an HTTP status code, so controllers never manually build error
  responses.

