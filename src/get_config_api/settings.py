# from pydantic import BaseSettings
from pathlib import Path


class Settings:
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR / "data"


def get_settings() -> Settings:
    """Return settings object"""

    return Settings()
