"""
Dataclass for split params
"""


from dataclasses import dataclass, field


@dataclass()
class SplittingParams:
    """
    Slpit size and rand seed
    """

    val_size: float = field(default=0.3)
    random_state: int = field(default=13)
