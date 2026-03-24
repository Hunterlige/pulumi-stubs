

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PolicyAttachmentArgs', 'PolicyAttachment']
@pulumi.input_type
class PolicyAttachmentArgs:
    def __init__(__self__, *, policy_id: pulumi.Input[_builtins.str], target_id: pulumi.Input[_builtins.str], skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_id.setter
    def policy_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_id.setter
    def target_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _PolicyAttachmentState:
    def __init__(__self__, *, policy_id: Optional[pulumi.Input[_builtins.str]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., target_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class PolicyAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., target_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PolicyAttachmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., policy_id: Optional[pulumi.Input[_builtins.str]] = ..., skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., target_id: Optional[pulumi.Input[_builtins.str]] = ...) -> PolicyAttachment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


