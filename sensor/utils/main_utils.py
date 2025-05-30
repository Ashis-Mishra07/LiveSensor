import yaml
import pandas as pd
import os
import numpy as np
import dill
import sys
from sensor.exception import SensorException


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