from module_functions.make_data import read_data, extract_target, split_train_val_data
from module_functions.feature_transform import full_transform
from module_functions.fit_predict_model import train_model, predict_model, evaluate_model
from entities.train_pipeline_params import read_training_pipeline_params


def test_train_pipeline(dataset_path: str, target_name: str, conf_path: str):
    training_pipeline_params = read_training_pipeline_params(conf_path)

    data = read_data(dataset_path)
    X, y = extract_target(data, target_name)
    X_transformed = full_transform(X)
    X_train, X_test, y_train, y_test = split_train_val_data(X_transformed, y, training_pipeline_params.splitting_params)
    model = train_model(X_train, y_train, training_pipeline_params.train_params)
    pred_labels, pred_proba = predict_model(model, X_test)

    res = evaluate_model(y_test, pred_labels, pred_proba)
    assert res['accuracy'] > 0
    assert res['roc_auc_score'] > 0.5
