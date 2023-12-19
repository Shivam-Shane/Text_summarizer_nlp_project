from logger import logging
from src.textsummarizernlpproject.config.configuration import ConfigurationManager
from src.textsummarizernlpproject.conponents.model_trainer import ModelTrainer

class ModelTrainerPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager() ## To access the configuration methods
        modelconfig=config.get_model_trainer_config()## To access the data_ingestion config
        model_trainer=ModelTrainer(config=modelconfig)
        model_trainer.train()

