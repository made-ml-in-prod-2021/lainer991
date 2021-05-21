import datetime
import logging
import re
import sys
from typing import List, Tuple

import pandas as pd
import requests

from src.module_functions.make_data import read_data, extract_features
from src.module_functions.feature_transform import full_transform


DEFAULT_FILEPATH = "data/data_wo_target.csv"
PREDICTION_FILEPATH = "predictions"
HOST = "127.0.0.1"
PORT = "8000"


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def get_data(filepath=DEFAULT_FILEPATH) -> Tuple:

    df = read_data(filepath)
    columns = extract_features(df)
    data = full_transform(df)
    return columns, data


def request(
        columns: List[str],
        data: pd.DataFrame
) -> List:

    responses = []
    for _, df_row in data.iterrows():
        logger.info("Getting request: ")
        response = requests.get(
            f"http://{HOST}:{PORT}/predict/",
            json={
                "columns": columns,
                "data": df_row.values.tolist()
            }
        )
        responses.append(response.json()["target"])
        logger.info("Status code %s", response.status_code)
        logger.info("Prediction is %i\n", response.json()["target"])
    return responses


def make_request() -> None:

    columns, data = get_data()
    result = request(columns, data)
    logger.info("Saving to predictions")
    filepath = (
            PREDICTION_FILEPATH +
            "/" +
            re.sub(r"[^0-9]+", "_", str(datetime.datetime.now())) +
            ".csv"
    )
    with open(filepath, "w") as file:
        file.write(str(result))


if __name__ == "__main__":
    make_request()