import yaml # type: ignore
import os,sys
# import dillr
import numpy as np
import pickle
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

def read_yaml_file(file_path) -> dict:
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        logging.error("Error in read_yaml_file method")
        raise NetworkSecurityException(e,sys)
    

def write_yaml_file(file_path:str,content: object, replace: bool = False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(content,file)

    except Exception as e:
        logging.error("Error in write_yaml_file method")
        raise NetworkSecurityException(e,sys)