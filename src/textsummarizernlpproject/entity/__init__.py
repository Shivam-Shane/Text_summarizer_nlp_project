from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_data_dir: Path
    source_url: str
    local_data_dir: Path
    unzip_data_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_valdata_dir: Path
    Status_file: str
    All_required_files: list[str] 


@dataclass(frozen=True)
class DataTransformationConfig:
    root_tradata_dir: Path
    data_path:     Path
    tokenizer_name: Path
