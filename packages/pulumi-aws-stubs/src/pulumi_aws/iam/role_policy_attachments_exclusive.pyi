

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RolePolicyAttachmentsExclusiveArgs', 'RolePolicyAttachmentsExclusive']
@pulumi.input_type
class RolePolicyAttachmentsExclusiveArgs:
    def __init__(__self__, *, policy_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], role_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArns")
    def policy_arns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @policy_arns.setter
    def policy_arns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_name.setter
    def role_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _RolePolicyAttachmentsExclusiveState:
    def __init__(__self__, *, policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., role_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArns")
    def policy_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @policy_arns.setter
    def policy_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RolePolicyAttachmentsExclusive(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., role_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RolePolicyAttachmentsExclusiveArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., policy_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., role_name: Optional[pulumi.Input[_builtins.str]] = ...) -> RolePolicyAttachmentsExclusive:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArns")
    def policy_arns(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


