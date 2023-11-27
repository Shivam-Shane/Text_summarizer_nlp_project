from logger import logging
from src.textsummarizernlpproject.config.configuration import ConfigurationManager
from src.textsummarizernlpproject.conponents.data_ingestion import DataIngetsion

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        dataingestionconfig=config.get_data_ingestion_config()
        dataingestion=DataIngetsion(config=dataingestionconfig)
        dataingestion.download_file()
        dataingestion.extract_data()

