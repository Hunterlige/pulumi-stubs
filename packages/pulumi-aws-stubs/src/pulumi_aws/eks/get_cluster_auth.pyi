

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetClusterAuthResult', 'AwaitableGetClusterAuthResult', 'get_cluster_auth', 'get_cluster_auth_output']
@pulumi.output_type
class GetClusterAuthResult:
    
    def __init__(__self__, id=..., name=..., region=..., token=...) -> None:
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
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> _builtins.str:
        
        ...
    


class AwaitableGetClusterAuthResult(GetClusterAuthResult):
    def __await__(self): # -> Generator[Never, Any, GetClusterAuthResult]:
        ...
    


def get_cluster_auth(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetClusterAuthResult:
    
    ...

def get_cluster_auth_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetClusterAuthResult]:
    
    ...

