import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["ResolutionPolicy"]

@pulumi.type_token("azure-native:privatedns:ResolutionPolicy")
class ResolutionPolicy(_builtins.str, Enum):
    DEFAULT = ...
    NX_DOMAIN_REDIRECT = ...
