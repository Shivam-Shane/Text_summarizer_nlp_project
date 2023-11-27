import os
import yaml
from logger import logging
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox ## when using dict values without list arguments 
from pathlib import Path 


@ensure_annotations
def read_yaml(path_to_yaml)-> ConfigBox:
    """read yaml file 
    Args: path_to_yaml file to read
    returns: values of yaml file in form of ConfigBox
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {yaml_file} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e: 
        raise e   
                         
def create_directories(path_to_directory:list,verbose=True):
    """create directories
    Args:
    path_to_directory
    """
    for path in path_to_directory:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")



def get_size(path:Path)->str:
    """get size of file.
    Args:
        path
    returns:
        str:size
    """
    file_size=round(os.path.getsize(path))
    return f"~ {file_size} "