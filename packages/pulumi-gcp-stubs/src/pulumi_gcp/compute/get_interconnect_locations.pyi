

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInterconnectLocationsResult', 'AwaitableGetInterconnectLocationsResult', 'get_interconnect_locations', 'get_interconnect_locations_output']
@pulumi.output_type
class GetInterconnectLocationsResult:
    
    def __init__(__self__, id=..., locations=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[outputs.GetInterconnectLocationsLocationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetInterconnectLocationsResult(GetInterconnectLocationsResult):
    def __await__(self): # -> Generator[Never, Any, GetInterconnectLocationsResult]:
        ...
    


def get_interconnect_locations(project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInterconnectLocationsResult:
    
    ...

def get_interconnect_locations_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInterconnectLocationsResult]:
    
    ...

