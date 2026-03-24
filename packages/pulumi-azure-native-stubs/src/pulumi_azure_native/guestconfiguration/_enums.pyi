

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['AssignmentType', 'Kind']
@pulumi.type_token("azure-native:guestconfiguration:AssignmentType")
class AssignmentType(_builtins.str, Enum):
    
    AUDIT = ...
    DEPLOY_AND_AUTO_CORRECT = ...
    APPLY_AND_AUTO_CORRECT = ...
    APPLY_AND_MONITOR = ...


@pulumi.type_token("azure-native:guestconfiguration:Kind")
class Kind(_builtins.str, Enum):
    
    DSC = ...


