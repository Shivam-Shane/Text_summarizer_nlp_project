from logger import logging
from src.textsummarizernlpproject.config.configuration import ConfigurationManager
from src.textsummarizernlpproject.conponents.data_ingestion import DataIngestion

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager() ## To access the configuration methods
        dataingestionconfig=config.get_data_ingestion_config() ## To access the data_ingestion config
        dataingestion=DataIngestion(config=dataingestionconfig)
        dataingestion.download_file()
        dataingestion.extract_data()

