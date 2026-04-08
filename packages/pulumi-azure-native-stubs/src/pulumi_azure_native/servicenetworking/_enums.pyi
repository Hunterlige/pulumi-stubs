import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["AssociationType"]

@pulumi.type_token("azure-native:servicenetworking:AssociationType")
class AssociationType(_builtins.str, Enum):
    SUBNETS = ...
