import os
from pathlib import Path
from logger import logging


project_name="textsummarizernlpproject"

list_of_files=(
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "parms.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
)

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory {filedir} for the filename {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath,'w') as f:
            pass ## as nothing to write in the file
            logging.info(f"creating file {filepath}")

    else:
           logging.info(f" file {filepath} already exists")     