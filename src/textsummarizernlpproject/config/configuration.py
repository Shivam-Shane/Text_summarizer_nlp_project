from src.textsummarizernlpproject.constants import *
from src.textsummarizernlpproject.utils.common import read_yaml, create_directories
from src.textsummarizernlpproject.entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTraninerConfig
from logger import logging

class ConfigurationManager:
    def __init__(self,
        config_filepath=CONFIG_FILE_PATH, ## from constants
        parms_filepath=PARMS_FILE_PATH): ## from constants
        self.config=read_yaml(config_filepath), # Reading config yaml file
        self.parms=read_yaml(parms_filepath)  # Reading parms yaml file for model parameters
        create_directories([self.config[0].artifacts_root]) 

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        logging.info(f">>>> Inside {self.__class__.__name__}.{self.get_data_ingestion_config.__name__}")
        config=self.config[0].data_ingestion

        create_directories([config.root_data_dir])#function to create directory

        data_ingestion_config=DataIngestionConfig(
            root_data_dir=config.root_data_dir,
            source_url=config.source_url,
            local_data_dir=config.local_data_dir,
            unzip_data_dir=config.unzip_data_dir
        )
        logging.info(f">>>> End of {self.get_data_ingestion_config.__name__} function")
        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        logging.info(f">>>> Inside {self.__class__.__name__}.{self.get_data_validation_config.__name__}")
        config=self.config[0].data_validation

        create_directories([config.root_valdata_dir])#function to create directory
        
        data_validation_config=DataValidationConfig(
            root_valdata_dir=config.root_valdata_dir,
            Status_file=config.Status_file,
            All_required_files=config.All_required_files
        )
        logging.info(f">>>> End of {self.get_data_validation_config.__name__}")
        return data_validation_config
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        logging.info(f">>>> Inside {self.__class__.__name__}.{self.get_data_transformation_config.__name__}")

        config=self.config[0].data_transformation

        create_directories([config.root_tradata_dir]) #function to create directory

        data_transformation_config=DataTransformationConfig(
        root_tradata_dir= config.root_tradata_dir,
        data_path   =config.data_path,
        tokenizer_name=config.tokenizer_name
        )
        logging.info(f">>>> End of {self.get_data_transformation_config.__name__}")
        return data_transformation_config
    
    def get_model_trainer_config(self)->ModelTraninerConfig:
        logging.info(f">>>> Inside {self.__class__.__name__}.{self.get_model_trainer_config.__name__}")

        config = self.config[0].model_trainer
        parms=self.parms.TrainingArguments
        create_directories([config.root_model_dir])

        model_trainer_config = ModelTraninerConfig(
                #config.yaml 
                root_model_dir= config.root_model_dir,
                data_path  =config.data_path,
                model_name=config.model_name,
                #parms.yaml model parameters
                num_train_epoch=parms.num_train_epoch,
                warmup_steps=parms.warmup_steps,
                pre_device_train_batch_size=parms.pre_device_train_batch_size,
                weight_decay=parms.weight_decay,
                logging_steps=parms.logging_steps,
                evaluation_strategy=parms.evaluation_strategy,
                eval_steps=parms.eval_steps,
                save_steps=parms.save_steps,
                gradient_accumulation_steps=parms.gradient_accumulation_steps
        )
        return model_trainer_config