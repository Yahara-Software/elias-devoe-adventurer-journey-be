"""errors.py

Typed exception heirarchy for the adventurer backend API.
"""

from typing import Any


class ApiError(Exception):
    """Base class for typed API errors
    
        Attributes:
            message: Human-readable description of the problem.
            status_code: HTTP status code to return for this error.
            payload: optional extra context to return with the message.
    """
    
    status_code = 500
    
    def __init__(self, message: str, payload: dict[str, Any] | None = None):
        super().__init__(message)
        self.message = message
        self.payload = payload or {}
        
    def to_dict(self):
        body = {"error": self.__class__.__name__, "message": self.message}
        body.update(self.payload)
        return body


class MalformedDirectionError(ApiError):
    """Raised when a direction string does not contain the expected alternating n_steps/FBRL format"""
    
    status_code = 422