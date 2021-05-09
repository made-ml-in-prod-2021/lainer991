import sys
import logging
import click

from module_functions.make_data import read_data, extract_target, split_train_val_data
from module_functions.feature_transform import full_transform
from module_functions.load_dump import dump_model

from entities.train_pipeline_params import read_training_pipeline_params
from module_functions.fit_predict_model import train_model, evaluate_model, predict_model

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def train_pipeline(config_path: str):
    training_pipeline_params = read_training_pipeline_params(config_path)
    return train_pipeline_run(training_pipeline_params)


def train_pipeline_run(training_pipeline_params):
    logger.info(f"Start training pipeline")
    data = read_data(training_pipeline_params.input_data_path)
    X, y = extract_target(data, training_pipeline_params.target_name)
    logger.info(f"X and y shape is {X.shape, y.shape}")

    X_transformed = full_transform(X)
    X_train, X_test, y_train, y_test = split_train_val_data(X_transformed, y, training_pipeline_params.splitting_params)

    model = train_model(X_train, y_train, training_pipeline_params.train_params)
    dump_model(training_pipeline_params.dump_model, model)
    logger.info(f"model fitted and dumped")

    pred_labels, pred_proba = predict_model(model, X_test)
    res = evaluate_model(y_test, pred_labels, pred_proba)

    logger.info(f"metrics is {res}")


@click.command(name="train_pipeline")
@click.argument("config_path")
def train_pipeline_command(config_path: str):
    train_pipeline(config_path)


if __name__ == "__main__":
    train_pipeline_command()
