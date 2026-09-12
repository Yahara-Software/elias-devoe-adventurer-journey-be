"""db.py

Engine/session setup for the SQLite database. Call `init_engine(uri)` once
at app startup, then use `get_session()` anywhere a service or use case
needs to talk to the database.
"""

from flask import g
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.models.base import Base

_engine: Engine | None = None
_SessionFactory: sessionmaker | None = None


def init_engine(database_uri: str) -> None:
    global _engine, _SessionFactory
    _engine = create_engine(database_uri)
    Base.metadata.create_all(_engine)
    _SessionFactory = sessionmaker(bind=_engine)


def get_session() -> Session:
    if _SessionFactory is None:
        raise RuntimeError("init_engine() must be called before get_session()")
    
    if "db_session" not in g:
        g.db_session = _SessionFactory()
    
    return g.db_session


def close_session(exception: BaseException | None = None) -> None:
    """Roll back on errors and close the session at the end of the request."""
    session: Session | None = g.pop("db_session", None)
    
    if session is not None:
        if exception is not None:
            session.rollback()
        session.close()
