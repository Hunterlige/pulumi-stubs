

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResourceTagsResult', 'AwaitableGetResourceTagsResult', 'get_resource_tags', 'get_resource_tags_output']
@pulumi.output_type
class GetResourceTagsResult:
    
    def __init__(__self__, id=..., resource_id=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetResourceTagsResult(GetResourceTagsResult):
    def __await__(self): # -> Generator[Never, Any, GetResourceTagsResult]:
        ...
    


def get_resource_tags(resource_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResourceTagsResult:
    
    ...

def get_resource_tags_output(resource_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResourceTagsResult]:
    
    ...

