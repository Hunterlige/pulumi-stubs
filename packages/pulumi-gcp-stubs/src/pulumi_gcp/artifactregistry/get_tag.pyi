

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTagResult', 'AwaitableGetTagResult', 'get_tag', 'get_tag_output']
@pulumi.output_type
class GetTagResult:
    
    def __init__(__self__, id=..., location=..., name=..., package_name=..., project=..., repository_id=..., tag_name=..., version=...) -> None:
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
    @pulumi.getter(name="packageName")
    def package_name(self) -> _builtins.str:
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
    @pulumi.getter(name="tagName")
    def tag_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTagResult(GetTagResult):
    def __await__(self): # -> Generator[Never, Any, GetTagResult]:
        ...
    


def get_tag(location: Optional[_builtins.str] = ..., package_name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., repository_id: Optional[_builtins.str] = ..., tag_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTagResult:
    
    ...

def get_tag_output(location: Optional[pulumi.Input[_builtins.str]] = ..., package_name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., repository_id: Optional[pulumi.Input[_builtins.str]] = ..., tag_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTagResult]:
    
    ...

