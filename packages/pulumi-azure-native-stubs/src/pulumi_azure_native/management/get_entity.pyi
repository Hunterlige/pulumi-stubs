

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEntityResult', 'AwaitableGetEntityResult', 'get_entity', 'get_entity_output']
@pulumi.output_type
class GetEntityResult:
    
    def __init__(__self__, count=..., next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.EntityInfoResponse]:
        
        ...
    


class AwaitableGetEntityResult(GetEntityResult):
    def __await__(self): # -> Generator[Never, Any, GetEntityResult]:
        ...
    


def get_entity(filter: Optional[_builtins.str] = ..., group_name: Optional[_builtins.str] = ..., search: Optional[_builtins.str] = ..., select: Optional[_builtins.str] = ..., skip: Optional[_builtins.int] = ..., skiptoken: Optional[_builtins.str] = ..., top: Optional[_builtins.int] = ..., view: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEntityResult:
    
    ...

def get_entity_output(filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., group_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., search: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., select: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., skip: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., skiptoken: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., top: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., view: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEntityResult]:
    
    ...

