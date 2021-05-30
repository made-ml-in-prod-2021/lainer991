import os
import numpy as np

import uvicorn
from fastapi import FastAPI

from src.entities.inference_parameters import Request, Response
from src.module_functions.fit_predict_model import predict_model
from src.module_functions.load_dump import load_model


PATH_TO_MODEL: str = "models/model_dump.pkl"
app = FastAPI()


@app.get("/")
def main():
    return {"Starting app: now"}


@app.get("/predict/", response_model=Response)
def predict(request: Request):

    model_path = PATH_TO_MODEL
    model = load_model(model_path)
    return {"target": predict_model(model, np.array(request.data).reshape(1, -1))[0]}


if __name__ == "__main__":
    uvicorn.run(
        app, host="0.0.0.0", port=os.getenv("PORT", 8000)
    )