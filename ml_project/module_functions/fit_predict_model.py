from typing import Union

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

from entities.train_params import TrainingParams

ClassificationModel = Union[LogisticRegression, RandomForestClassifier]


def train_model(
        X: pd.DataFrame, y: pd.DataFrame, train_params: TrainingParams
) -> ClassificationModel:
    if train_params.model_type == "LogisticRegression":
        model = LogisticRegression()
    elif train_params.model_type == "RandomForestClassifier":
        model = RandomForestClassifier(n_estimators=train_params.estimators_n)
    else:
        raise NotImplementedError()
    model.fit(X, y)
    return model


def predict_model(model, X):
    pred_labels = model.predict(X)
    pred_proba = model.predict_proba(X)[:, 1]
    return pred_labels, pred_proba


def evaluate_model(true_labels, pred_labels, pred_proba):
    return {
        "accuracy": metrics.accuracy_score(true_labels, pred_labels),
        "precision_score": metrics.precision_score(true_labels, pred_labels),
        "recall": metrics.recall_score(true_labels, pred_labels),
        "f1_score": metrics.f1_score(true_labels, pred_labels),
        "roc_auc_score": metrics.roc_auc_score(true_labels, pred_proba),
    }
