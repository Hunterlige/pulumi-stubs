

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ManagedPolicyAttachmentsExclusiveArgs', 'ManagedPolicyAttachmentsExclusive']
@pulumi.input_type
class ManagedPolicyAttachmentsExclusiveArgs:
    def __init__(__self__, *, instance_arn: pulumi.Input[_builtins.str], managed_policy_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], permission_set_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[ManagedPolicyAttachmentsExclusiveTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @managed_policy_arns.setter
    def managed_policy_arns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @permission_set_arn.setter
    def permission_set_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ManagedPolicyAttachmentsExclusiveTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ManagedPolicyAttachmentsExclusiveTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ManagedPolicyAttachmentsExclusiveState:
    def __init__(__self__, *, instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[ManagedPolicyAttachmentsExclusiveTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_arn.setter
    def instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @managed_policy_arns.setter
    def managed_policy_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @permission_set_arn.setter
    def permission_set_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ManagedPolicyAttachmentsExclusiveTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ManagedPolicyAttachmentsExclusiveTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ManagedPolicyAttachmentsExclusive(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[ManagedPolicyAttachmentsExclusiveTimeoutsArgs, ManagedPolicyAttachmentsExclusiveTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ManagedPolicyAttachmentsExclusiveArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., managed_policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[ManagedPolicyAttachmentsExclusiveTimeoutsArgs, ManagedPolicyAttachmentsExclusiveTimeoutsArgsDict]]] = ...) -> ManagedPolicyAttachmentsExclusive:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPolicyArns")
    def managed_policy_arns(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ManagedPolicyAttachmentsExclusiveTimeouts]]:
        ...
    


