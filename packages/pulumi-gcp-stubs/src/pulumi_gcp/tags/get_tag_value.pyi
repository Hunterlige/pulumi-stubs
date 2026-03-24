

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTagValueResult', 'AwaitableGetTagValueResult', 'get_tag_value', 'get_tag_value_output']
@pulumi.output_type
class GetTagValueResult:
    
    def __init__(__self__, create_time=..., description=..., id=..., name=..., namespaced_name=..., parent=..., short_name=..., update_time=...) -> None:
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
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespacedName")
    def namespaced_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTagValueResult(GetTagValueResult):
    def __await__(self): # -> Generator[Never, Any, GetTagValueResult]:
        ...
    


def get_tag_value(parent: Optional[_builtins.str] = ..., short_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTagValueResult:
    
    ...

def get_tag_value_output(parent: Optional[pulumi.Input[_builtins.str]] = ..., short_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTagValueResult]:
    
    ...

