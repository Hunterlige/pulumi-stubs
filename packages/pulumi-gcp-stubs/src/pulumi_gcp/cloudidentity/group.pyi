

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GroupArgs', 'Group']
@pulumi.input_type
class GroupArgs:
    def __init__(__self__, *, group_key: pulumi.Input[GroupGroupKeyArgs], labels: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]], parent: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., initial_group_config: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> pulumi.Input[GroupGroupKeyArgs]:
        
        ...
    
    @group_key.setter
    def group_key(self, value: pulumi.Input[GroupGroupKeyArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialGroupConfig")
    def initial_group_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @initial_group_config.setter
    def initial_group_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _GroupState:
    def __init__(__self__, *, additional_group_keys: Optional[pulumi.Input[Sequence[pulumi.Input[GroupAdditionalGroupKeyArgs]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., group_key: Optional[pulumi.Input[GroupGroupKeyArgs]] = ..., initial_group_config: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalGroupKeys")
    def additional_group_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GroupAdditionalGroupKeyArgs]]]]:
        
        ...
    
    @additional_group_keys.setter
    def additional_group_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GroupAdditionalGroupKeyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> Optional[pulumi.Input[GroupGroupKeyArgs]]:
        
        ...
    
    @group_key.setter
    def group_key(self, value: Optional[pulumi.Input[GroupGroupKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialGroupConfig")
    def initial_group_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @initial_group_config.setter
    def initial_group_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:cloudidentity/group:Group")
class Group(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., group_key: Optional[pulumi.Input[Union[GroupGroupKeyArgs, GroupGroupKeyArgsDict]]] = ..., initial_group_config: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., additional_group_keys: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GroupAdditionalGroupKeyArgs, GroupAdditionalGroupKeyArgsDict]]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., group_key: Optional[pulumi.Input[Union[GroupGroupKeyArgs, GroupGroupKeyArgsDict]]] = ..., initial_group_config: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Group:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalGroupKeys")
    def additional_group_keys(self) -> pulumi.Output[Sequence[outputs.GroupAdditionalGroupKey]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> pulumi.Output[outputs.GroupGroupKey]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialGroupConfig")
    def initial_group_config(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


