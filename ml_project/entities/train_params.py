"""
Dataclass for training params
"""

from dataclasses import dataclass, field

@dataclass()
class TrainingParams:
    """
    Training params
    """
    model_type: str = field(default="LogisticRegression")
    random_state: int = field(default=42)
