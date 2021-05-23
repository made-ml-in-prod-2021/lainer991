import sys
import logging
import click
import pandas as pd

from module_functions.make_data import read_data, extract_target
from module_functions.feature_transform import full_transform
from module_functions.load_dump import load_model

from module_functions.fit_predict_model import predict_model

from entities.predict_pipeline_params import read_predict_pipeline_params

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def predict_pipeline(config_path: str):
    predict_pipeline_params = read_predict_pipeline_params(config_path)
    return predict_pipeline_run(predict_pipeline_params)


def predict_pipeline_run(predict_pipeline_params):
    logger.info(f"Start predict pipeline")

    data = read_data(predict_pipeline_params.input_data_path)

    # testing predict function on data without target
    data, y = extract_target(data,'target')

    data_transformed = full_transform(data)
    logger.info(f"Transformed data shape is {data_transformed.shape}")

    model = load_model(predict_pipeline_params.dump_model)
    pred_labels, pred_proba = predict_model(model, data_transformed)

    pd.Series(pred_labels, index=data_transformed.index, name="prediction") \
        .to_csv(predict_pipeline_params.result_path)
    logger.info(f"Results written to directory")


@click.command(name="predict_pipeline")
@click.argument("config_path")
def predict_pipeline_command(config_path: str):
    predict_pipeline(config_path)


if __name__ == "__main__":
    predict_pipeline_command()
