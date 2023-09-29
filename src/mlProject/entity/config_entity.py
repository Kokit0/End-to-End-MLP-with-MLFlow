#entity dataclass
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True) #<--- esta entidad, mi dataclass para config ingestion ligado al config.yaml. no es una python class si no que una dataclass. como version escrita de esta funcion.
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict