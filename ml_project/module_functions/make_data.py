# -*- coding: utf-8 -*-
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

from entities.split_params import SplittingParams


def read_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data


def extract_target(df, target_name):
    X = df.drop(target_name, axis=1)
    y = df[target_name]
    return X, y


def split_train_val_data(
        X: pd.DataFrame, y: pd.DataFrame, params: SplittingParams
        ) -> Tuple:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=params.val_size, random_state=params.random_state
    )
    return X_train, X_test, y_train, y_test
