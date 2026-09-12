"""main.py

Flask application factory. Run with:

    poetry run flask --app app.main run --debug

or:

    poetry run python -m app.main
"""

import os
from flask import Flask

from app.controllers.move_controller import adventurer_bp
from app.db import init_engine, close_session
from app.errors.handler import register_error_handler


def create_app(database_uri: str | None = None) -> Flask:
    app = Flask(__name__)

    database_uri = database_uri or os.environ.get(
        "DATABASE_URL", "sqlite:///moves.db"
    )
    init_engine(database_uri)

    app.register_blueprint(adventurer_bp, url_prefix="/adventurers")
    register_error_handler(app)
    app.teardown_appcontext(close_session)
    
    return app


if __name__ == "__main__":
    create_app().run(debug=True)

