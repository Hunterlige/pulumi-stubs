

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNamedQueryResult', 'AwaitableGetNamedQueryResult', 'get_named_query', 'get_named_query_output']
@pulumi.output_type
class GetNamedQueryResult:
    
    def __init__(__self__, database=..., description=..., id=..., name=..., querystring=..., region=..., workgroup=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def querystring(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def workgroup(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetNamedQueryResult(GetNamedQueryResult):
    def __await__(self): # -> Generator[Never, Any, GetNamedQueryResult]:
        ...
    


def get_named_query(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., workgroup: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNamedQueryResult:
    
    ...

def get_named_query_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., workgroup: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNamedQueryResult]:
    
    ...

