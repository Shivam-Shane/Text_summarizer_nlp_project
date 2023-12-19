from dataclasses import dataclass
from os import path
from pathlib import Path



@dataclass(frozen=True)
class ExecutionflowConfig:
    data_ingestion_flow: bool
    data_validation_flow: bool
    data_transformation_flow: bool
    model_trainer_flow: bool

@dataclass(frozen=True)
class DataIngestionConfig:
    #config.yaml
    root_data_dir: Path
    source_url: str
    local_data_dir: Path
    unzip_data_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    #config.yaml
    root_valdata_dir: Path
    Status_file: str
    All_required_files: list[str] 


@dataclass(frozen=True)
class DataTransformationConfig:
    #config.yaml
    root_tradata_dir: Path
    data_path:     Path
    tokenizer_name: Path

@dataclass(frozen=True)
class ModelTraninerConfig:
    #config.yaml
    root_model_dir: Path
    data_path:     Path
    model_name: str
    #parms.yaml
    num_train_epoch:int
    warmup_steps:int
    pre_device_train_batch_size:int
    weight_decay:float
    logging_steps:int
    evaluation_strategy:str
    eval_steps:int
    save_steps:float
    gradient_accumulation_steps:int 
