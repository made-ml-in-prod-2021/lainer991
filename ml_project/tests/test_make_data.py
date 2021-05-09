from module_functions.make_data import read_data, extract_target, split_train_val_data
from entities.train_pipeline_params import read_training_pipeline_params



def test_read_data(dataset_path: str):
    data = read_data(dataset_path)
    assert len(data) > 0


def test_extract_target(dataset_path: str, target_name: str):
    data = read_data(dataset_path)
    X, y = extract_target(data, target_name)
    assert len(X) > 0
    assert len(y) > 0


def test_split_train_val_data(dataset_path: str, target_name: str, conf_path: str):
    training_pipeline_params = read_training_pipeline_params(conf_path)

    data = read_data(dataset_path)
    X, y = extract_target(data, target_name)
    X_train, X_test, y_train, y_test = split_train_val_data(X, y, training_pipeline_params.splitting_params)
    assert len(X_train) > 0
    assert len(X_test) > 0
    assert len(y_train) > 0
    assert len(y_test) > 0

