

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['UserPolicyAttachmentArgs', 'UserPolicyAttachment']
@pulumi.input_type
class UserPolicyAttachmentArgs:
    def __init__(__self__, *, policy_arn: pulumi.Input[_builtins.str], user: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_arn.setter
    def policy_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user.setter
    def user(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _UserPolicyAttachmentState:
    def __init__(__self__, *, policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., user: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_arn.setter
    def policy_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:iam/userPolicyAttachment:UserPolicyAttachment")
class UserPolicyAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., user: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UserPolicyAttachmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., policy_arn: Optional[pulumi.Input[_builtins.str]] = ..., user: Optional[pulumi.Input[_builtins.str]] = ...) -> UserPolicyAttachment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyArn")
    def policy_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


