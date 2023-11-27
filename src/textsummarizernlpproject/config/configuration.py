from src.textsummarizernlpproject.constants import *
from src.textsummarizernlpproject.utils.common import read_yaml, create_directories
from src.textsummarizernlpproject.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self,
        config_filepath=CONFIG_FILE_PATH, ## from constants
        parms_filepath=PARMS_FILE_PATH): ## from constants

        self.config=read_yaml(config_filepath), # 4 ingestion config values
        self.parms=read_yaml(parms_filepath)  # no value
        create_directories([self.config[0].artifacts_root]) 

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config[0].data_ingestion

        create_directories([config.root_data_dir])

        data_ingestion_config=DataIngestionConfig(
            root_data_dir=config.root_data_dir,
            source_url=config.source_url,
            local_data_dir=config.local_data_dir,
            unzip_data_dir=config.unzip_data_dir

        )
        return data_ingestion_config
    
