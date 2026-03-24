

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPackageResult', 'AwaitableGetPackageResult', 'get_package', 'get_package_output']
@pulumi.output_type
class GetPackageResult:
    
    def __init__(__self__, annotations=..., create_time=..., display_name=..., id=..., location=..., name=..., project=..., repository_id=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPackageResult(GetPackageResult):
    def __await__(self): # -> Generator[Never, Any, GetPackageResult]:
        ...
    


def get_package(location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., repository_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPackageResult:
    
    ...

def get_package_output(location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., repository_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPackageResult]:
    
    ...

