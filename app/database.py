from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Default to Postgres unless overridden
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://devuser:devpass@localhost:5432/podb_dev")

# If we're running tests, override with SQLite
if os.getenv("TESTING") == "1":
    DATABASE_URL = "sqlite:///./test.db"

# SQLite needs this extra argument
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    future=True,
    echo=True,        # shows SQL queries in terminal (good for dev, turn off in prod)
    pool_pre_ping=True,
    connect_args=connect_args
)

# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)

# Base class for models
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    future=True,
    echo=True,        # shows SQL queries in terminal (good for dev, turn off in prod)
    pool_pre_ping=True,
    connect_args=connect_args
)

# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)

# Base class for models
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
