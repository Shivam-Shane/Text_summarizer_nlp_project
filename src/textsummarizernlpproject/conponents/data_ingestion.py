import os
import urllib.request as request
import zipfile
from pathlib import Path
from src.textsummarizernlpproject.utils.common import get_size
from src.textsummarizernlpproject.entity import DataIngestionConfig
from logger import logging


class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        source url, download location
        Returns None
        """  
        logging.info("Dataset download started")    
        if not os.path.exists(self.config.local_data_dir):
            filename,headers=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_dir
            )    
            logging.info(f"Downloading! dataset from {self.config.source_url} at path {self.config.local_data_dir }with following info:\n{headers}")
        else:
            logging.info(f"file already downloaded at path {self.config.local_data_dir} with size :{get_size(Path(self.config.local_data_dir))}")

    def extract_data(self):
            """
            zip_file_path
            unzip_file_path Extract the file into dir
            Returns None
            """
            zip_file_path = self.config.local_data_dir
            logging.info(f"Extracting data from {zip_file_path}")
            unzip_file_path = self.config.unzip_data_dir

            # Check if the target directory is not empty
            if os.listdir(unzip_file_path):
                logging.info(f"Data already extracted at {unzip_file_path}")
                return  # No need to extract again if the directory is not empty

            with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
                zip_file.extractall(unzip_file_path)
            
            logging.info(f"File extracted and saved successfully at {unzip_file_path}")
                                