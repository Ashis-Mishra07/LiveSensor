from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os , sys
from sensor.logger import logging
from  sensor.utils import dump_csv_file_to_mongo_collection
from sensor.entity.config_entity  import TrainingPipelineConfig,DataIngestionConfig

from sensor.pipeline.training_pipeline import TrainPipeline


if __name__ == "__main__":

    # file_path=r"F:\Complete ML\All_Projects\MLProject2\dataset.csv"
    # database_name="ineuron"
    # collection_name ="sensor"
    # dump_csv_file_to_mongo_collection(file_path,database_name,collection_name)

    training_pipeline = TrainPipeline()
    # training_pipeline.start_data_ingestion()
    training_pipeline.run_pipeline()