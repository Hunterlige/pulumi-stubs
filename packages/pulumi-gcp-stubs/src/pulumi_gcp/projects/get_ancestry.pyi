

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAncestryResult', 'AwaitableGetAncestryResult', 'get_ancestry', 'get_ancestry_output']
@pulumi.output_type
class GetAncestryResult:
    
    def __init__(__self__, ancestors=..., id=..., org_id=..., parent_id=..., parent_type=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ancestors(self) -> Sequence[outputs.GetAncestryAncestorResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentType")
    def parent_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetAncestryResult(GetAncestryResult):
    def __await__(self): # -> Generator[Never, Any, GetAncestryResult]:
        ...
    


def get_ancestry(project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAncestryResult:
    
    ...

def get_ancestry_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAncestryResult]:
    
    ...

