import os,sys
import certifi # type: ignore

ca = certifi.where()

from dotenv import load_dotenv # type: ignore
load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")
print(mongo_db_url)

import pymongo # type: ignore
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline

from networksecurity.utils.main_utils.utils import load_object
from networksecurity.utils.ml_utils.model.estimator import NetworkModel

from fastapi.middleware.cors import CORSMiddleware # type: ignore
from fastapi import FastAPI, File, UploadFile, Request # type: ignore
from uvicorn import run as app_run # type: ignore
from fastapi.responses import Response # type: ignore
from starlette.responses import RedirectResponse # type: ignore
import pandas as pd

client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME, DATA_INGESTION_COLLECTION_NAME

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.templating import Jinja2Templates # type: ignore
templates = Jinja2Templates(directory="./templates")

@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training completed successfully.")
    except Exception as e:
        logging.error(f"Error occurred while training: {e}")
        raise NetworkSecurityException(e, sys)

@app.post("/predict")
async def predict_route(request: Request,file:UploadFile=File(...)):
    try:
        df=pd.read_csv(file.file)
        preprocessor = load_object(file_path="final_model/preprocessor.pkl")
        final_model = load_object(file_path="final_model/model.pkl")
        network_model = NetworkModel(preprocessor=preprocessor, model=final_model)
        print(df.iloc[0])
        y_pred = network_model.predict(df)
        print(y_pred)
        df['predicted_column'] = y_pred
        print(df["predicted_column"])
        df.to_csv('prediction_output/output.csv')
        table_html = df.to_html(classes='table table-striped')
        return templates.TemplateResponse("table.html",{"request":request,"table":table_html})

    except Exception as e:
        logging.error(f"Error occurred while loading model: {e}")
        raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    app_run(app,host="0.0.0.0",port=8000)