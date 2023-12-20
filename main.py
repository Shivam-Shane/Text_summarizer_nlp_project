from src.textsummarizernlpproject.pipeline.Stage_1_data_ingestion import DataIngestionTrainingPipeline
from src.textsummarizernlpproject.pipeline.Stage_2_data_validation import DatavalidationTrainingPipeline
from src.textsummarizernlpproject.pipeline.Stage_3_data_transformation import DataTransformationPipeline
from src.textsummarizernlpproject.pipeline.Stage_4_model_trainer import ModelTrainerPipeline
from src.textsummarizernlpproject.constants import *
from logger import logging
import time
from executionflow import Executionflow


try:
    starttime = time.time()
    executionflow = Executionflow()
    executionflow_data=executionflow.get_data_for_executionflow()
    
    STAGE_NAME="Data Ingestion"
    if executionflow_data.data_ingestion_flow==True:
        logging.info(f">>>>>>>>>>>>>>> Starting {STAGE_NAME} pipeline")
        data_ingetsion=DataIngestionTrainingPipeline()
        data_ingetsion.main()
        logging.info(f"<<<<<<<<<<<<<<< Stage {STAGE_NAME} is completed successfully")
    else:
         logging.info(f"-------------- Stage {STAGE_NAME} is skipped.")
    
    STAGE_NAME="Data Validation"
    if executionflow_data.data_validation_flow==True:
        logging.info(f">>>>>>>>>>>>>>> Starting {STAGE_NAME} pipeline")
        data_validation=DatavalidationTrainingPipeline()
        data_validation.main()
        logging.info(f"<<<<<<<<<<<<<<< Stage {STAGE_NAME} is completed successfully") 
    else:
         logging.info(f"-------------- Stage {STAGE_NAME} is skipped.")
    
    STAGE_NAME="Data Transformation"
    if executionflow_data.data_transformation_flow==True:
        logging.info(f">>>>>>>>>>>>>>> Starting {STAGE_NAME} pipeline")
        data_transformation=DataTransformationPipeline()
        data_transformation.main()
        logging.info(f"<<<<<<<<<<<<<<< Stage {STAGE_NAME} is completed successfully")      
    else:
         logging.info(f"-------------- Stage {STAGE_NAME} is skipped.")   

    STAGE_NAME="Model Trainer"
    if executionflow_data.model_trainer_flow==True:
        logging.info(f">>>>>>>>>>>>>>> Starting {STAGE_NAME} pipeline")
        model_trainer=ModelTrainerPipeline()
        model_trainer.main()
        logging.info(f"<<<<<<<<<<<<<<< Stage {STAGE_NAME} is completed successfully")
    else:
         logging.info(f"-------------- Stage {STAGE_NAME} is skipped.")

    Endtime = time.time()
    logging.info(f"Pipeline execution time: {Endtime-starttime}")

except Exception as e:
        logging.exception(e)
        raise e    