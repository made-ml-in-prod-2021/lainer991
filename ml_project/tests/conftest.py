import os
import pytest

DATA_PATH = "ml_project/tests/test_data/noise_data_sample.csv"
CONF_PATH = "ml_project/config/train_conf.yaml"
TARGET: str = 'target'


@pytest.fixture()
def dataset_path():
    curdir = os.path.dirname(os.getcwd())
    return os.path.join(curdir, DATA_PATH)


@pytest.fixture()
def conf_path():
    curdir = os.path.dirname(os.getcwd())
    return os.path.join(curdir, CONF_PATH)


@pytest.fixture()
def target_name():
    return TARGET
