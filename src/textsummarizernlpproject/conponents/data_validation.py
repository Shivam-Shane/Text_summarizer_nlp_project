import os
from src.textsummarizernlpproject.entity import DataValidationConfig
from logger import logging

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config

    def validatedata(self)->bool:
        """Validate: data
        Args: files[List] to be validated, file where to wrtie validation result
        return True if data is valid, False otherwise in file.
        """
        try:
            logging.info(f"Starting data validation")
            validation_status = None
            all_files=os.listdir(os.path.join("artifacts","data_ingestion","Newsdataset"))
            for file in all_files:
               if file not in self.config.All_required_files:
                  validation_status=False
                  with open(self.config.Status_file,"w") as f:
                       f.write(f"validation_status: {validation_status}")
                       logging.info(f"Stored data validation result {validation_status} {file}")
               else:
                  validation_status=True
                  with open(self.config.Status_file,"w") as f:
                       f.write(f"validation_status: {validation_status}")   
            logging.info(f"Stored data validation result {validation_status}")
            return bool(validation_status)
        except Exception as e: 
         raise e   
        