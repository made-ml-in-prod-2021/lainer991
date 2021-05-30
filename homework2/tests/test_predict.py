from typing import List
import logging
import sys
import pandas as pd

from fastapi.testclient import TestClient
from app import app

from src.module_functions.feature_transform import full_transform
from src.module_functions.load_dump import load_model
from src.module_functions.fit_predict_model import predict_model


MODEL_FILEPATH = "models/model_dump.pkl"

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.ERROR)
logger.addHandler(handler)


client = TestClient(app)


def test_predict():
    response = client.get("/")
    assert (
            response.status_code == 200
    ), logging.info("The response 200 is not gotten")
    assert (
            response.json() == ["Starting app: now"]
    ), logging.info("The starting message differs from the planned")


def test_output(test_df: pd.DataFrame) -> None:
    model = load_model(MODEL_FILEPATH)
    df = full_transform(test_df)
    predictions = predict_model(model, df)
    assert (
            predictions.shape[0] ==
            df.shape[0]
    ), logger.error("Shape problem, pal")
    assert (
            len(predictions.shape) == 1
    ), logger.error("Prediction shape is 1, pal")


def test_column_correctness(test_df: pd.DataFrame, column_names: List) -> None:
    extracted_col_names = test_df.columns.to_list()
    assert (
            len(extracted_col_names) ==
            len(column_names)
    ), logging.error("Shape problem, bub")
    assert (
            sorted(extracted_col_names) ==
            sorted(column_names)
    ), logging.error("The columns' names are not as expected")
    assert (
            extracted_col_names ==
            column_names
    ), logging.error("Wrong Column names")