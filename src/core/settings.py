import os
from pathlib import Path
from pydantic import BaseSettings
from dotenv import load_dotenv, dotenv_values


base_dir = Path(__file__).parent.parent.parent.absolute()
load_dotenv()

class Settings(BaseSettings):
    max_file_size: int = os.getenv("MAX_FILE_SIZE")
    min_io: str = os.getenv("MIN_IO")

    @property
    def max_file_size_dsn(self) -> int:
        return self.max_file_size

    @property
    def minio_dsn(self) -> str:
        return self.min_io