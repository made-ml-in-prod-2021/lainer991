import click
import pandas as pd
import numpy as np

from module_functions.make_data import read_data, extract_target
from module_functions.feature_transform import get_features_labels
from entities.fake_data_params import read_fake_data_params

# DATA_PATH = "data/heart.csv"
# SAVE_PATH = "tests/test_data/noise_data_sample.csv"
# TARGET: str = 'target'
# RANDOM_PERCENT = 0.8


def making_data_launch(config_path: str):
    fake_data_params = read_fake_data_params(config_path)
    return sample_and_save(fake_data_params)


def making_data(data_path, target):
    data = read_data(data_path)
    X, y = extract_target(data, target)
    cat_feats, num_feats = get_features_labels(X)

    mu, sigma = 0, 0.1
    noise = np.random.normal(mu, sigma, [X[num_feats].shape[0], X[num_feats].shape[1]])
    num_feats_new = X[num_feats] + noise
    data_fake = pd.concat([num_feats_new, X[cat_feats], y], axis=1)
    return data_fake


def sample_and_save(fake_data_params):
    data = making_data(fake_data_params.data_path, fake_data_params.target_name)
    num = data.shape[0]
    data_sample = data.sample(n=int(num * fake_data_params.random_percent))
    data_sample.to_csv(fake_data_params.save_path, index=False)


@click.command(name="making_fake_data")
@click.argument("config_path")
def making_data_command(config_path: str):
    making_data_launch(config_path)


if __name__ == "__main__":
    making_data_command()
