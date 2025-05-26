from sensor.exception import SensorException
import os
import sys

from sensor.logger import logging


def test_exception():
    try:
        # Simulating an error
        logging.info("Testing exception handling")
        1 / 0
    except Exception as e:
        raise SensorException(e, sys)

if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        sensor_exception = SensorException(e, sys)
        print(sensor_exception)  # This will print the custom error message with file name and line number