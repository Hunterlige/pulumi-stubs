

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['RefillPolicy', 'VirtualMachineState']
@pulumi.type_token("azure-native:standbypool:RefillPolicy")
class RefillPolicy(_builtins.str, Enum):
    
    ALWAYS = ...


@pulumi.type_token("azure-native:standbypool:VirtualMachineState")
class VirtualMachineState(_builtins.str, Enum):
    
    RUNNING = ...
    DEALLOCATED = ...


