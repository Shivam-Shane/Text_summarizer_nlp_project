from logger import logging
from src.textsummarizernlpproject.config.configuration import ConfigurationManager
from src.textsummarizernlpproject.conponents.data_validation import DataValidation

class DatavalidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        logging.info(f"Inside {self.__class__.__name__}.{self.__init__.__name__}")
        config=ConfigurationManager()
        datavalidationconfig=config.get_data_validation_config()
        datavalidation=DataValidation(config=datavalidationconfig)
        datavalidation.validatedata()
        logging.info(f"Data validation END")