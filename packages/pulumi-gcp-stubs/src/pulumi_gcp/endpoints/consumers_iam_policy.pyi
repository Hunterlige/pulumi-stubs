

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConsumersIamPolicyArgs', 'ConsumersIamPolicy']
@pulumi.input_type
class ConsumersIamPolicyArgs:
    def __init__(__self__, *, consumer_project: pulumi.Input[_builtins.str], policy_data: pulumi.Input[_builtins.str], service_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerProject")
    def consumer_project(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @consumer_project.setter
    def consumer_project(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @policy_data.setter
    def policy_data(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _ConsumersIamPolicyState:
    def __init__(__self__, *, consumer_project: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., policy_data: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerProject")
    def consumer_project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @consumer_project.setter
    def consumer_project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_data.setter
    def policy_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ConsumersIamPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., consumer_project: Optional[pulumi.Input[_builtins.str]] = ..., policy_data: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConsumersIamPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., consumer_project: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., policy_data: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ...) -> ConsumersIamPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerProject")
    def consumer_project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


