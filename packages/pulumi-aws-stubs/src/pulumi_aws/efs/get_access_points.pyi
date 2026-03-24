

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAccessPointsResult', 'AwaitableGetAccessPointsResult', 'get_access_points', 'get_access_points_output']
@pulumi.output_type
class GetAccessPointsResult:
    
    def __init__(__self__, arns=..., file_system_id=..., id=..., ids=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetAccessPointsResult(GetAccessPointsResult):
    def __await__(self): # -> Generator[Never, Any, GetAccessPointsResult]:
        ...
    


def get_access_points(file_system_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAccessPointsResult:
    
    ...

def get_access_points_output(file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAccessPointsResult]:
    
    ...

