

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResourceResult', 'AwaitableGetResourceResult', 'get_resource', 'get_resource_output']
@pulumi.output_type
class GetResourceResult:
    
    def __init__(__self__, id=..., parent_id=..., path=..., path_part=..., region=..., rest_api_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathPart")
    def path_part(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restApiId")
    def rest_api_id(self) -> _builtins.str:
        ...
    


class AwaitableGetResourceResult(GetResourceResult):
    def __await__(self): # -> Generator[Never, Any, GetResourceResult]:
        ...
    


def get_resource(path: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., rest_api_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResourceResult:
    
    ...

def get_resource_output(path: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., rest_api_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResourceResult]:
    
    ...

