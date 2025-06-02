from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os , sys
from sensor.logger import logging
from sensor.utils2 import dump_csv_file_to_mongo_collection
from sensor.entity.config_entity  import TrainingPipelineConfig,DataIngestionConfig

from sensor.pipeline.training_pipeline import TrainPipeline

from fastapi import FastAPI ,UploadFile , Response
from sensor.constant.application import APP_HOST, APP_PORT
from uvicorn import run as app_run
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from sensor.ml.model.estimator import ModelResolver , TargetValueMapping
from sensor.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware
from sensor.constant.training_pipeline import SAVED_MODEL_DIR
import pandas as pd

# https://127.0.0.1:8080/docs

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/" , tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train():

    try:
        training_pipeline = TrainPipeline()
        if training_pipeline.is_pipeline_running:
            return Response(content="Training is already in progress", status_code=200)
        training_pipeline.run_pipeline()
        return Response(content="Training completed successfully", status_code=200)
    except Exception as e:
        return Response(content=str(e), status_code=500)


@app.get("/predict")
async def predict():
    try:
        # Read the CSV file from disk
        df = pd.read_csv("sample_test_data_full.csv")

        # Model resolution and loading
        Model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not Model_resolver.is_model_exists():
            return Response(content="Model is not available", status_code=404)
        
        best_model_path = Model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)

        # Predict
        y_pred = model.predict(df)
        df['predicted_column'] = y_pred
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping, inplace=True)

        # Return predictions as JSON
        return {"predictions": df['predicted_column'].tolist()}

    except Exception as e:
        return Response(content=str(e), status_code=500)

def main():
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        raise SensorException(e, sys)
    


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)