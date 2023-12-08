from src.textsummarizernlpproject.constants import *
from src.textsummarizernlpproject.utils.common import read_yaml, create_directories
from src.textsummarizernlpproject.entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from logger import logging


class ConfigurationManager:
    def __init__(self,
        config_filepath=CONFIG_FILE_PATH, ## from constants
        parms_filepath=PARMS_FILE_PATH): ## from constants
        logging.info(f"Entering {self.__class__.__name__}.{self.__init__.__name__}")
        self.config=read_yaml(config_filepath), # Reading config yaml file
        self.parms=read_yaml(parms_filepath)  # Reading parms yaml file
        create_directories([self.config[0].artifacts_root]) 

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        logging.info(f"Entering {self.__class__.__name__}.{self.get_data_ingestion_config.__name__}")
        config=self.config[0].data_ingestion

        create_directories([config.root_data_dir])#function to create directory

        data_ingestion_config=DataIngestionConfig(
            root_data_dir=config.root_data_dir,
            source_url=config.source_url,
            local_data_dir=config.local_data_dir,
            unzip_data_dir=config.unzip_data_dir
        )
        logging.info(f"End of {self.get_data_ingestion_config.__name__}")
        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        logging.info(f"Entering {self.__class__.__name__}.{self.get_data_validation_config.__name__}")
        config=self.config[0].data_validation

        create_directories([config.root_valdata_dir])#function to create directory
        
        data_validation_config=DataValidationConfig(
            root_valdata_dir=config.root_valdata_dir,
            Status_file=config.Status_file,
            All_required_files=config.All_required_files
        )
        logging.info(f"End of {self.get_data_validation_config.__name__}")
        return data_validation_config
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        logging.info(f"Entering {self.__class__.__name__}.{self.get_data_transformation_config.__name__}")

        config=self.config[0].data_transformation

        create_directories([config.root_tradata_dir]) #function to create directory

        data_transformation_config=DataTransformationConfig(
        root_tradata_dir= config.root_tradata_dir,
        data_path   =config.data_path,
        tokenizer_name=config.tokenizer_name
        )
        logging.info(f"End of {self.get_data_transformation_config.__name__}")
        return data_transformation_config