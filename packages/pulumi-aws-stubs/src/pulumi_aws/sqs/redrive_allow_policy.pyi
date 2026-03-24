

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RedriveAllowPolicyArgs', 'RedriveAllowPolicy']
@pulumi.input_type
class RedriveAllowPolicyArgs:
    def __init__(__self__, *, queue_url: pulumi.Input[_builtins.str], redrive_allow_policy: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @queue_url.setter
    def queue_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redriveAllowPolicy")
    def redrive_allow_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @redrive_allow_policy.setter
    def redrive_allow_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RedriveAllowPolicyState:
    def __init__(__self__, *, queue_url: Optional[pulumi.Input[_builtins.str]] = ..., redrive_allow_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @queue_url.setter
    def queue_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redriveAllowPolicy")
    def redrive_allow_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redrive_allow_policy.setter
    def redrive_allow_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:sqs/redriveAllowPolicy:RedriveAllowPolicy")
class RedriveAllowPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., queue_url: Optional[pulumi.Input[_builtins.str]] = ..., redrive_allow_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RedriveAllowPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., queue_url: Optional[pulumi.Input[_builtins.str]] = ..., redrive_allow_policy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> RedriveAllowPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redriveAllowPolicy")
    def redrive_allow_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


