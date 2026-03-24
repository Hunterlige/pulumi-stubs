

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PermissionSetInlinePolicyArgs', 'PermissionSetInlinePolicy']
@pulumi.input_type
class PermissionSetInlinePolicyArgs:
    def __init__(__self__, *, inline_policy: pulumi.Input[_builtins.str], instance_arn: pulumi.Input[_builtins.str], permission_set_arn: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inlinePolicy")
    def inline_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @inline_policy.setter
    def inline_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
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
class _PermissionSetInlinePolicyState:
    def __init__(__self__, *, inline_policy: Optional[pulumi.Input[_builtins.str]] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inlinePolicy")
    def inline_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inline_policy.setter
    def inline_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_arn.setter
    def instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
class PermissionSetInlinePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., inline_policy: Optional[pulumi.Input[_builtins.str]] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PermissionSetInlinePolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., inline_policy: Optional[pulumi.Input[_builtins.str]] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> PermissionSetInlinePolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inlinePolicy")
    def inline_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


