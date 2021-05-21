from typing import List
import pandas as pd
import pytest

from src.module_functions.make_data import read_data

DATA_FILEPATH = "data/data_wo_target.csv"


@pytest.fixture(scope="session")
def test_df() -> pd.DataFrame:
    return read_data(DATA_FILEPATH)


@pytest.fixture(scope="session")
def column_names() -> List[str]:
    return [
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "ca",
        "thal"
    ]


@pytest.fixture(scope="session")
def target_col() -> str:
    return "target"