

import builtins as _builtins
import sys
import pulumi
from typing import Any

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['QueueReservationPlanSettings']
@pulumi.output_type
class QueueReservationPlanSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commitment: _builtins.str, renewal_type: _builtins.str, reserved_slots: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commitment(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalType")
    def renewal_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedSlots")
    def reserved_slots(self) -> _builtins.int:
        
        ...
    


