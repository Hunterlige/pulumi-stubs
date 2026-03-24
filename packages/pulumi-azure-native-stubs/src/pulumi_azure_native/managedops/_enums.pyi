

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['DesiredEnablementState']
@pulumi.type_token("azure-native:managedops:DesiredEnablementState")
class DesiredEnablementState(_builtins.str, Enum):
    
    ENABLE = ...
    DISABLE = ...


