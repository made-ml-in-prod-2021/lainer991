from module_functions.make_data import read_data, extract_target
from module_functions.feature_transform import get_features_labels, full_transform


def test_get_features_labels(dataset_path: str, target_name: str):
    data = read_data(dataset_path)
    X, y = extract_target(data, target_name)
    cat_cols, num_cols = get_features_labels(X)
    assert len(num_cols) > 0


def test_full_transform(dataset_path: str, target_name: str):
    data = read_data(dataset_path)
    X, y = extract_target(data, target_name)
    X_transformed = full_transform(X)
    assert max(X_transformed.describe().T['std']) < 2
    assert max(abs(X_transformed.describe().T['mean'])) < 1
