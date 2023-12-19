from src.textsummarizernlpproject.constants import *
from src.textsummarizernlpproject.utils.common import read_yaml
from logger import logging
from src.textsummarizernlpproject.entity import ExecutionflowConfig


class Executionflow():
    def __init__(self,
        config_filepath=CONFIG_FILE_PATH):
        logging.info(f"Entering {self.__class__.__name__}.{self.__init__.__name__}")
        self.config=read_yaml(config_filepath), # Reading config yaml file for execution flow
    def get_data_for_executionflow(self)->ExecutionflowConfig: #type: ignore
        config=self.config[0].execution_flow
        execution_flow_config=ExecutionflowConfig(
                                data_ingestion_flow=config.data_ingestion_flow,
                                data_validation_flow=config.data_validation_flow,
                                data_transformation_flow=config.model_trainer_flow,
                                model_trainer_flow=config.model_trainer_flow
        )
        return execution_flow_config
        
        
        
    
    