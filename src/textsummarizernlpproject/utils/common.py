import os
import yaml
from logger import logging
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox ## when using dict values 
from pathlib import Path 


@ensure_annotations
def read_yaml(path_to_yaml)-> ConfigBox:
    """read yaml file 
    Args: path_to_yaml file to read
    returns: values of yaml file in form of ConfigBox
    """
    logging.info(f"Starting reading yaml file {path_to_yaml}")
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {yaml_file} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e: 
        raise e   
                         
def create_directories(path_to_directory: list[str], verbose=True):
    """Create directories if they don't exist.

    Args:
        path_to_directory (list): List of paths to be created.
        verbose (bool, optional): Whether to log the creation of directories. Defaults to True.
    """
    for path in path_to_directory:
        if not os.path.isdir(path):
            os.makedirs(path, exist_ok=True)
            if verbose:
                action = "Created" if not os.path.exists(path) else "Already exists"
                logging.info(f"{action} directory at: {path}")
        elif verbose:
            logging.info(f"Directory already exists at: {path}")
            
def get_size(path: Path) -> str:
    """Get the size of a file.
    Args:
        path (Path): The path to the file.

    Returns:
        str: A string representation of the file size.
    """
    file_size_bytes = os.path.getsize(path)   # Get the size of the file in bytes using os.path.getsize   
    rounded_file_size = round(file_size_bytes) # Round the file size to the nearest integer
    formatted_size = format_size(rounded_file_size)# For example, "~ 1.23 MB" or "~ 567 KB"

    return formatted_size

def format_size(size_in_bytes: int) -> str:
    """Format the size in bytes to a human-readable string.
    Args:
        size_in_bytes (int): Size in bytes.

    Returns:
        str: Formatted size string.
    """
    units = ['Bytes', 'KB', 'MB', 'GB', 'TB']  # Define the units and their corresponding labels    
    unit_index = 0 # Determine the appropriate unit for the file size
    size = size_in_bytes

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1

    # Format the size with the unit and return
    formatted_size = f"~ {round(size, 2)} {units[unit_index]}"
    return formatted_size