import os 

TARGET_COLUMN = "class"
PIPELINE_NAME = "sensor"
ARTIFACT_DIR = "artifact"
FILE_NAME = "sensor.csv"


TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl" 
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"


"""
 data  ingestion realted constant values 
"""

DATA_INGESTION_COLLECTION_NAME: str = "sensor"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2



"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"


"""
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
"""

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str = "transformed_object"


"""
Model Trainer related constant start with MODEL_TRAINER VAR NAME"
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_FILE_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD: float = 0.05


"""
Model Evaluator related constant start with MODEL_EVALUATOR VAR NAME
"""
MODEL_EVALUATOR_DIR_NAME: str = "model_evaluation"
MODEL_EVALUATOR_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_EVALUATION_REPORT_NAME = "report.yaml"

SAVED_MODEL_DIR: str = os.path.join("saved_models")


MODEL_PUSHER_DIR_NAME= "model_pusher"
MODEL_PUSHER_SAVED_MODEL_DIR = SAVED_MODEL_DIR



