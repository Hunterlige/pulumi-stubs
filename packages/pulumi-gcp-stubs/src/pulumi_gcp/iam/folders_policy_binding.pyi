

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FoldersPolicyBindingArgs', 'FoldersPolicyBinding']
@pulumi.input_type
class FoldersPolicyBindingArgs:
    def __init__(__self__, *, folder: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], policy: pulumi.Input[_builtins.str], policy_binding_id: pulumi.Input[_builtins.str], target: pulumi.Input[FoldersPolicyBindingTargetArgs], annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., condition: Optional[pulumi.Input[FoldersPolicyBindingConditionArgs]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_kind: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @folder.setter
    def folder(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy.setter
    def policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyBindingId")
    def policy_binding_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_binding_id.setter
    def policy_binding_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[FoldersPolicyBindingTargetArgs]:
        
        ...
    
    @target.setter
    def target(self, value: pulumi.Input[FoldersPolicyBindingTargetArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[FoldersPolicyBindingConditionArgs]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[FoldersPolicyBindingConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyKind")
    def policy_kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_kind.setter
    def policy_kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _FoldersPolicyBindingState:
    def __init__(__self__, *, annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., condition: Optional[pulumi.Input[FoldersPolicyBindingConditionArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., policy_binding_id: Optional[pulumi.Input[_builtins.str]] = ..., policy_kind: Optional[pulumi.Input[_builtins.str]] = ..., policy_uid: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[FoldersPolicyBindingTargetArgs]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[FoldersPolicyBindingConditionArgs]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[FoldersPolicyBindingConditionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_annotations.setter
    def effective_annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyBindingId")
    def policy_binding_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_binding_id.setter
    def policy_binding_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyKind")
    def policy_kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_kind.setter
    def policy_kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyUid")
    def policy_uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_uid.setter
    def policy_uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[FoldersPolicyBindingTargetArgs]]:
        
        ...
    
    @target.setter
    def target(self, value: Optional[pulumi.Input[FoldersPolicyBindingTargetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:iam/foldersPolicyBinding:FoldersPolicyBinding")
class FoldersPolicyBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., condition: Optional[pulumi.Input[Union[FoldersPolicyBindingConditionArgs, FoldersPolicyBindingConditionArgsDict]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., policy_binding_id: Optional[pulumi.Input[_builtins.str]] = ..., policy_kind: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[Union[FoldersPolicyBindingTargetArgs, FoldersPolicyBindingTargetArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FoldersPolicyBindingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., condition: Optional[pulumi.Input[Union[FoldersPolicyBindingConditionArgs, FoldersPolicyBindingConditionArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., policy_binding_id: Optional[pulumi.Input[_builtins.str]] = ..., policy_kind: Optional[pulumi.Input[_builtins.str]] = ..., policy_uid: Optional[pulumi.Input[_builtins.str]] = ..., target: Optional[pulumi.Input[Union[FoldersPolicyBindingTargetArgs, FoldersPolicyBindingTargetArgsDict]]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> FoldersPolicyBinding:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional[outputs.FoldersPolicyBindingCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyBindingId")
    def policy_binding_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyKind")
    def policy_kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyUid")
    def policy_uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Output[outputs.FoldersPolicyBindingTarget]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


