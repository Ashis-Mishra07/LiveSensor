import yaml
import pandas as pd
import os
import numpy as np
import dill
import sys
from sensor.exception import SensorException
import logging


def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its content as a dictionary.
    
    :param file_path: Path to the YAML file.
    :return: Dictionary containing the YAML file content.
    :raises SensorException: If the file cannot be read or parsed.
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise SensorException(e, sys) from e
    


def write_yaml_file(file_path:str , content:object , replace:bool = False) -> None:
    """
    Writes content to a YAML file.
    
    :param file_path: Path to the YAML file.
    :param content: Content to write to the file.
    :param replace: If True, replaces the file if it exists; otherwise, appends.
    :raises SensorException: If the file cannot be written.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise SensorException(e, sys) from e
    


def save_numpy_array_data(file_path: str, array: np.ndarray):
    """
    Saves a NumPy array to a file.
    
    :param file_path: Path to the file where the array will be saved.
    :param array: NumPy array to save.
    :raises SensorException: If the file cannot be written.
    """
    try:
       dir_path = os.path.dirname(file_path)
       os.makedirs(dir_path, exist_ok=True)
       with open(file_path, 'wb') as file:
           np.save(file, array)
    except Exception as e:
        raise SensorException(e, sys) from e    
    


def load_numpy_array_data(file_path: str) -> np.ndarray:
    """
    Loads a NumPy array from a file.
    
    :param file_path: Path to the file from which the array will be loaded.
    :return: Loaded NumPy array.
    :raises SensorException: If the file cannot be read.
    """
    try:
        with open(file_path, 'rb') as file:
            return np.load(file)
    except Exception as e:
        raise SensorException(e, sys) from e
    

def save_object(file_path: str, obj: object)-> None:
    """
    Saves an object to a file using dill.
    
    :param file_path: Path to the file where the object will be saved.
    :param obj: Object to save.
    :raises SensorException: If the file cannot be written.
    """
    try:
        logging.info("Entering the save_object method")
        os.makedirs(os.path.dirname(file_path) , exist_ok=True)
        with open(file_path, 'wb') as file:
            dill.dump(obj, file)
        logging.info(f"Object saved to {file_path}")
    except Exception as e:
        raise SensorException(e, sys) from e