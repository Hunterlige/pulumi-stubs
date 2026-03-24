

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['ParameterType']
@pulumi.type_token("aws:ssm/ParameterType:ParameterType")
class ParameterType(_builtins.str, Enum):
    STRING = ...
    STRING_LIST = ...
    SECURE_STRING = ...


