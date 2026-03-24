

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ...]
@pulumi.output_type
class GetOrganizationalUnitDescendantOrganizationalUnitsResult:
    
    def __init__(__self__, childrens=..., id=..., parent_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def childrens(self) -> Sequence[outputs.GetOrganizationalUnitDescendantOrganizationalUnitsChildrenResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> _builtins.str:
        ...
    


class AwaitableGetOrganizationalUnitDescendantOrganizationalUnitsResult(GetOrganizationalUnitDescendantOrganizationalUnitsResult):
    def __await__(self): # -> Generator[Never, Any, GetOrganizationalUnitDescendantOrganizationalUnitsResult]:
        ...
    


def get_organizational_unit_descendant_organizational_units(parent_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOrganizationalUnitDescendantOrganizationalUnitsResult:
    
    ...

def get_organizational_unit_descendant_organizational_units_output(parent_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOrganizationalUnitDescendantOrganizationalUnitsResult]:
    
    ...

