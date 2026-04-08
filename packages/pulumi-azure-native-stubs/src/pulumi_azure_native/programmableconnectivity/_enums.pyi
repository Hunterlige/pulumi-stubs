import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ["AccountType"]

@pulumi.type_token("azure-native:programmableconnectivity:AccountType")
class AccountType(_builtins.str, Enum):
    AZURE_MANAGED = ...
    USER_MANAGED = ...
