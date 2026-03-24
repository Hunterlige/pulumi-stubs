

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOrganizationalUnitsResult', 'AwaitableGetOrganizationalUnitsResult', 'get_organizational_units', 'get_organizational_units_output']
@pulumi.output_type
class GetOrganizationalUnitsResult:
    
    def __init__(__self__, children=..., id=..., parent_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def children(self) -> Sequence[outputs.GetOrganizationalUnitsChildResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> _builtins.str:
        ...
    


class AwaitableGetOrganizationalUnitsResult(GetOrganizationalUnitsResult):
    def __await__(self): # -> Generator[Never, Any, GetOrganizationalUnitsResult]:
        ...
    


def get_organizational_units(parent_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOrganizationalUnitsResult:
    
    ...

def get_organizational_units_output(parent_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOrganizationalUnitsResult]:
    
    ...

