

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAccessPointResult', 'AwaitableGetAccessPointResult', 'get_access_point', 'get_access_point_output']
@pulumi.output_type
class GetAccessPointResult:
    
    def __init__(__self__, access_point_id=..., arn=..., file_system_arn=..., file_system_id=..., id=..., owner_id=..., posix_users=..., region=..., root_directories=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPointId")
    def access_point_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemArn")
    def file_system_arn(self) -> _builtins.str:
        
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
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixUsers")
    def posix_users(self) -> Sequence[outputs.GetAccessPointPosixUserResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectories")
    def root_directories(self) -> Sequence[outputs.GetAccessPointRootDirectoryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetAccessPointResult(GetAccessPointResult):
    def __await__(self): # -> Generator[Never, Any, GetAccessPointResult]:
        ...
    


def get_access_point(access_point_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAccessPointResult:
    
    ...

def get_access_point_output(access_point_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAccessPointResult]:
    
    ...

