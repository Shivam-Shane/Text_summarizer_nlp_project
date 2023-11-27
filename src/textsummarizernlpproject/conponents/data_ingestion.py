import os
import urllib.request as request
import zipfile
from pathlib import Path
from src.textsummarizernlpproject.utils.common import get_size
from src.textsummarizernlpproject.entity import DataIngestionConfig
from logger import logging


class DataIngetsion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        source url, download location
        Returns None
        """       
        if not os.path.exists(self.config.local_data_dir):
            filename,headers=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_dir
            )    
            logging.info(f"{filename} downloading! with following info:\n{headers}")
        else:
            logging.info(f"file already downloaded at path {self.config.local_data_dir } with size :{get_size(Path(self.config.local_data_dir))}")


    def extract_data(self):
        """
        zip_file_path
        unzip_file_path Extract the file into dir
        Returns None
        """
        zip_file_path = self.config.local_data_dir
        unzip_file_path =self.config.unzip_data_dir
        os.makedirs(unzip_file_path,exist_ok=True)
        with zipfile.ZipFile(zip_file_path,'r') as zip_file:
            zip_file.extractall(unzip_file_path)
                             