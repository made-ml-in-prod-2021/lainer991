# -*- coding: utf-8 -*-
from typing import Tuple, List

import pandas as pd
from sklearn.model_selection import train_test_split


def read_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data


def extract_target(df, target_name):
    X = df.drop(target_name, axis=1)
    y = df[target_name]
    return X, y


def extract_features(df: pd.DataFrame) -> List:

    if "target" in df.columns.to_list():
        return df.drop(["target"], axis=1).columns.tolist()
    return df.columns.tolist()
