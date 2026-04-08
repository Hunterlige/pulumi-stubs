import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["EnablementStatus"]

@pulumi.type_token(...)
class EnablementStatus(_builtins.str, Enum):
    ENABLED = ...
    DISABLED = ...
