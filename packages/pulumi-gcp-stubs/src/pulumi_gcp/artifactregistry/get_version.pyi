

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVersionResult', 'AwaitableGetVersionResult', 'get_version', 'get_version_output']
@pulumi.output_type
class GetVersionResult:
    
    def __init__(__self__, annotations=..., create_time=..., description=..., id=..., location=..., name=..., package_name=..., project=..., related_tags=..., repository_id=..., update_time=..., version_name=..., view=...) -> None:
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
    @pulumi.getter
    def description(self) -> _builtins.str:
        
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
    @pulumi.getter(name="relatedTags")
    def related_tags(self) -> Sequence[outputs.GetVersionRelatedTagResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def view(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetVersionResult(GetVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetVersionResult]:
        ...
    


def get_version(location: Optional[_builtins.str] = ..., package_name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., repository_id: Optional[_builtins.str] = ..., version_name: Optional[_builtins.str] = ..., view: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVersionResult:
    
    ...

def get_version_output(location: Optional[pulumi.Input[_builtins.str]] = ..., package_name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., repository_id: Optional[pulumi.Input[_builtins.str]] = ..., version_name: Optional[pulumi.Input[_builtins.str]] = ..., view: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVersionResult]:
    
    ...

