"""
Dataclass for making fake data
"""

from dataclasses import dataclass, field
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class FakeDataParams:
    """
    Making fake data params
    """
    data_path: str
    save_path: str
    target_name: str
    random_percent: int = field(default=13)


FakeDataParamsSchema = class_schema(FakeDataParams)


def read_fake_data_params(path: str) -> FakeDataParams:

    """
    reading params
    """
    with open(path, "r") as input_stream:
        schema = FakeDataParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
