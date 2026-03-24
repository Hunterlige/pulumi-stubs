

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['Category']
@pulumi.type_token("azure-native:aadiam:Category")
class Category(_builtins.str, Enum):
    
    AUDIT_LOGS = ...
    SIGN_IN_LOGS = ...


