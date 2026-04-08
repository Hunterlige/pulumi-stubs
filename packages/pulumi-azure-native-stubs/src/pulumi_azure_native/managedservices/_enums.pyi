import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["MultiFactorAuthProvider"]

@pulumi.type_token(...)
class MultiFactorAuthProvider(_builtins.str, Enum):
    AZURE = ...
    NONE = ...
