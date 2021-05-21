from typing import List, Union
from pydantic import BaseModel, conlist


class Request(BaseModel):
    """
    Parameters
    """
    columns: List[str]
    data: conlist(Union[float, int, None], min_items=30, max_items=30)


class Response(BaseModel):
    """
    Parameters
    """
    target: int