"""handler.py

Registers Flask error handler so controllers never build error messages.
Just raise a typed ApiError, and this module transforms it into the right
shape (JSON) with HTTP status code.
"""

from flask import Flask, jsonify

from app.errors.errors import ApiError

def register_error_handler(app: Flask) -> None:
    @app.errorhandler(ApiError)
    def handle_api_error(err: ApiError):
        res = jsonify(err.to_dict())
        res.status_code = err.status_code
        return res