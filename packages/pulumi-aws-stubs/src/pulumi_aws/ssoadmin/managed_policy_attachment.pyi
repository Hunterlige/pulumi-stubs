

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ManagedPolicyAttachmentArgs', 'ManagedPolicyAttachment']
@pulumi.input_type
class ManagedPolicyAttachmentArgs:
    def __init__(__self__, *, instance_arn: pulumi.Input[_builtins.str], managed_policy_arn: pulumi.Input[_builtins.str], permission_set_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPolicyArn")
    def managed_policy_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @managed_policy_arn.setter
    def managed_policy_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    


@pulumi.input_type
class _ManagedPolicyAttachmentState:
    def __init__(__self__, *, instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., managed_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., managed_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_arn.setter
    def instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPolicyArn")
    def managed_policy_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_policy_arn.setter
    def managed_policy_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPolicyName")
    def managed_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_policy_name.setter
    def managed_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token(...)
class ManagedPolicyAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., managed_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ManagedPolicyAttachmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., managed_policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., managed_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> ManagedPolicyAttachment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPolicyArn")
    def managed_policy_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPolicyName")
    def managed_policy_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


