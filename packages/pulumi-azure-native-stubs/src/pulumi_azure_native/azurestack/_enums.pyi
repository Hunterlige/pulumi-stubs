import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["Location"]

@pulumi.type_token("azure-native:azurestack:Location")
class Location(_builtins.str, Enum):
    GLOBAL_ = ...
