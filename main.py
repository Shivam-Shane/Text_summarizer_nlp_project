from src.textsummarizernlpproject.pipeline.Stage_1_data_ingestion import DataIngestionTrainingPipeline
from src.textsummarizernlpproject.pipeline.Stage_2_data_validation import DatavalidationTrainingPipeline
from src.textsummarizernlpproject.pipeline.Stage_3_data_transformation import DataTransformationPipeline

from logger import logging
import time

STAGE_NAME="Data Ingestion"

starttime = time.time()
try:
    logging.info(f"Starting {STAGE_NAME} pipeline")
    data_ingetsion=DataIngestionTrainingPipeline()
    data_ingetsion.main()
    logging.info(f"Stage {STAGE_NAME} is completed successfully")
    ## stage 1 end of pipeline 
    STAGE_NAME="Data Validation"
    logging.info(f"Starting {STAGE_NAME} pipeline")
    data_validation=DatavalidationTrainingPipeline()
    data_validation.main()
    logging.info(f"Stage {STAGE_NAME} is completed successfully")
    ## stage 2 end of pipeline 
    STAGE_NAME="Data Transformation"
    logging.info(f"Starting {STAGE_NAME} pipeline")
    data_transformation=DataTransformationPipeline()
    data_transformation.main()
    logging.info(f"Stage {STAGE_NAME} is completed successfully")
    ## stage 3 end of pipeline 


except Exception as e:
        logging.exception(e)
        raise e    

Endtime = time.time()
logging.info(f"Pipeline execution time: {Endtime-starttime}")