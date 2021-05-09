import os
import pandas as pd
import numpy as np

from module_functions.make_data import read_data, extract_target
from module_functions.feature_transform import get_features_labels


DATA_PATH = "heart.csv"
SAVE_PATH = "tests/test_data/noise_data_sample.csv"
TARGET: str = 'target'
RANDOM_PERCENT = 0.8


def dataset_path(path):
    curdir = os.path.dirname(os.getcwd())
    return os.path.join(curdir, path)


def making_data(data_path, target):

    data = read_data(data_path)
    X, y = extract_target(data, target)
    cat_feats, num_feats = get_features_labels(X)

    mu, sigma = 0, 0.1
    noise = np.random.normal(mu, sigma, [X[num_feats].shape[0], X[num_feats].shape[1]])
    num_feats_new = X[num_feats] + noise
    data_fake = pd.concat([num_feats_new, X[cat_feats], y], axis=1)
    return data_fake


def sample_and_save():
    data = making_data(dataset_path(DATA_PATH), TARGET)
    num = data.shape[0]
    data_sample = data.sample(n=int(num * RANDOM_PERCENT))
    data_sample.to_csv(dataset_path(SAVE_PATH), index=False)


if __name__ == "__main__":
    sample_and_save()