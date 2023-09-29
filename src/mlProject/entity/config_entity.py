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



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig: #<--- rutas para entrenar con los test.csv y train.csv segun lo definido en el config.yaml 
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float # <--- parametro alpha predefinido en params.yaml
    l1_ratio: float # <--- parametro l1 predefinido en mi params.yaml
    target_column: str # <---columna objetivo segun lo definamos en schema.yaml ( Quality of wine)



'''
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str
    '''