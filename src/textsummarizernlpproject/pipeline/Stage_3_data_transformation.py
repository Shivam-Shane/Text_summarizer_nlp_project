from logger import logging
from src.textsummarizernlpproject.config.configuration import ConfigurationManager
from src.textsummarizernlpproject.conponents.data_transformation import DataTransformations

class DataTransformationPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        datatrasnformationconfig=config.get_data_transformation_config()
        datatransformation=DataTransformations(config=datatrasnformationconfig)
        datatransformation.convert()
        logging.info(f"Data Transformation END")