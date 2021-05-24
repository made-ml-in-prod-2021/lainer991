"""
Training params dataclass
"""

from dataclasses import dataclass, field
import yaml
from marshmallow_dataclass import class_schema

from .split_params import SplittingParams
from .train_params import TrainingParams


@dataclass()
class TrainingPipelineParams:
    """
    Training params
    """

    input_data_path: str
    target_name: str
    splitting_params: SplittingParams
    train_params: TrainingParams
    dump_model: str
    estimators_n: int = field(default=300)

TrainingPipelineParamsSchema = class_schema(TrainingPipelineParams)


def read_training_pipeline_params(path: str) -> TrainingPipelineParams:
    """
    Reading traing params
    :param path:
    :return:
    """

    with open(path, "r") as input_stream:
        schema = TrainingPipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
