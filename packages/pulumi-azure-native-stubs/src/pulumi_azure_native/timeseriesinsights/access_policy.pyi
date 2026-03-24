

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccessPolicyArgs', 'AccessPolicy']
@pulumi.input_type
class AccessPolicyArgs:
    def __init__(__self__, *, environment_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], access_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., principal_object_id: Optional[pulumi.Input[_builtins.str]] = ..., roles: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessPolicyRole]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @environment_name.setter
    def environment_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicyName")
    def access_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_policy_name.setter
    def access_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalObjectId")
    def principal_object_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_object_id.setter
    def principal_object_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessPolicyRole]]]]]:
        
        ...
    
    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessPolicyRole]]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:timeseriesinsights:AccessPolicy")
class AccessPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., environment_name: Optional[pulumi.Input[_builtins.str]] = ..., principal_object_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., roles: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessPolicyRole]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AccessPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AccessPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalObjectId")
    def principal_object_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


