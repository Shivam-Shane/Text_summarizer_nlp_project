from src.textsummarizernlpproject.pipeline.Stage_1_data_ingestion import DataIngestionTrainingPipeline
from logger import logging

STAGE_NAME="Data Ingestion Stage"

try:
    logging.info(f"Starting {STAGE_NAME} pipeline")
    data_ingetsion=DataIngestionTrainingPipeline()
    data_ingetsion.main()
    logging.info(f"Stage {STAGE_NAME}  is completed successfully")
except Exception as e:
        logging.exception(e)
        raise e    
