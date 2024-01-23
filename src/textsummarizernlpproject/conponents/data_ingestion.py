import os
import urllib.request as request
import zipfile
from pathlib import Path
from src.textsummarizernlpproject.utils.common import get_size
from src.textsummarizernlpproject.entity import DataIngestionConfig
from logger import logging
from tqdm import tqdm

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """Download the dataset from the url specified
        Args:
            source url, download dir location
        Returns:
            None
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
        """Extract data for model building from the given path

        Args:
            zip_file_path (str): path to the zip file containing the dataset
            unzip_file_path (str): path to the directory where the dataset should be extracted

        Returns:
            None
        """
        zip_file_path = self.config.local_data_dir
        logging.info(f"Extracting data from {zip_file_path}")
        unzip_file_path = self.config.unzip_data_dir
        
        with tqdm(total=len(zipfile.ZipFile(zip_file_path).infolist()), unit='file', desc='Extracting') as pbar:
            with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
                for file_info in zip_file.infolist():
                    zip_file.extract(file_info, unzip_file_path)
                    pbar.update(1)
        logging.info(f"File extracted and saved successfully at {unzip_file_path}")                 