

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LogDataProtectionPolicyArgs', 'LogDataProtectionPolicy']
@pulumi.input_type
class LogDataProtectionPolicyArgs:
    def __init__(__self__, *, log_group_name: pulumi.Input[_builtins.str], policy_document: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_document.setter
    def policy_document(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _LogDataProtectionPolicyState:
    def __init__(__self__, *, log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_document: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_group_name.setter
    def log_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class LogDataProtectionPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_document: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LogDataProtectionPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., log_group_name: Optional[pulumi.Input[_builtins.str]] = ..., policy_document: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> LogDataProtectionPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


