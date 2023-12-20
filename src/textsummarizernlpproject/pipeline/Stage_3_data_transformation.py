from logger import logging
from src.textsummarizernlpproject.config.configuration import ConfigurationManager
from src.textsummarizernlpproject.conponents.data_transformation import DataTransformations

class DataTransformationPipeline:
    def __init__(self):
        pass
    def main(self):
        logging.info(f">>>> Inside {self.__class__.__name__}.{self.__init__.__name__}")
        config=ConfigurationManager()
        datatrasnformationconfig=config.get_data_transformation_config()
        datatransformation=DataTransformations(config=datatrasnformationconfig)
        datatransformation.convert()
        logging.info(f">>>> Data Transformation END")