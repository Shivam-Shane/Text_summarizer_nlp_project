from logger import logging
from src.textsummarizernlpproject.config.configuration import ConfigurationManager
from src.textsummarizernlpproject.conponents.model_evaluation import Model_Evaluation

class DataEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        logging.info(f">>>> Inside {self.__class__.__name__}.{self.__init__.__name__}")
        config=ConfigurationManager() ## To access the configuration methods
        dataEvaluationconfig=config.get_model_evaluation_config()## To access the data_Evaluation config
        dataEvaluationconfig=Model_Evaluation(config=dataEvaluationconfig)
        dataEvaluationconfig.evaluate()
        logging.info(f">>>> Data Evaluation END")