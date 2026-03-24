

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetManagedZonesResult', 'AwaitableGetManagedZonesResult', 'get_managed_zones', 'get_managed_zones_output']
@pulumi.output_type
class GetManagedZonesResult:
    
    def __init__(__self__, id=..., managed_zones=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedZones")
    def managed_zones(self) -> Sequence[outputs.GetManagedZonesManagedZoneResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetManagedZonesResult(GetManagedZonesResult):
    def __await__(self): # -> Generator[Never, Any, GetManagedZonesResult]:
        ...
    


def get_managed_zones(project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagedZonesResult:
    
    ...

def get_managed_zones_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagedZonesResult]:
    
    ...

