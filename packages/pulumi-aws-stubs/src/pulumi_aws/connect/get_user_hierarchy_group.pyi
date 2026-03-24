

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetUserHierarchyGroupResult', 'AwaitableGetUserHierarchyGroupResult', 'get_user_hierarchy_group', 'get_user_hierarchy_group_output']
@pulumi.output_type
class GetUserHierarchyGroupResult:
    
    def __init__(__self__, arn=..., hierarchy_group_id=..., hierarchy_paths=..., id=..., instance_id=..., level_id=..., name=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hierarchyGroupId")
    def hierarchy_group_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hierarchyPaths")
    def hierarchy_paths(self) -> Sequence[outputs.GetUserHierarchyGroupHierarchyPathResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="levelId")
    def level_id(self) -> _builtins.str:
        
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
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetUserHierarchyGroupResult(GetUserHierarchyGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetUserHierarchyGroupResult]:
        ...
    


def get_user_hierarchy_group(hierarchy_group_id: Optional[_builtins.str] = ..., instance_id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetUserHierarchyGroupResult:
    
    ...

def get_user_hierarchy_group_output(hierarchy_group_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetUserHierarchyGroupResult]:
    
    ...

