

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DaprComponentResiliencyPolicyArgs', 'DaprComponentResiliencyPolicy']
@pulumi.input_type
class DaprComponentResiliencyPolicyArgs:
    def __init__(__self__, *, component_name: pulumi.Input[_builtins.str], environment_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], inbound_policy: Optional[pulumi.Input[DaprComponentResiliencyPolicyConfigurationArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., outbound_policy: Optional[pulumi.Input[DaprComponentResiliencyPolicyConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentName")
    def component_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @component_name.setter
    def component_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter(name="inboundPolicy")
    def inbound_policy(self) -> Optional[pulumi.Input[DaprComponentResiliencyPolicyConfigurationArgs]]:
        
        ...
    
    @inbound_policy.setter
    def inbound_policy(self, value: Optional[pulumi.Input[DaprComponentResiliencyPolicyConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundPolicy")
    def outbound_policy(self) -> Optional[pulumi.Input[DaprComponentResiliencyPolicyConfigurationArgs]]:
        
        ...
    
    @outbound_policy.setter
    def outbound_policy(self, value: Optional[pulumi.Input[DaprComponentResiliencyPolicyConfigurationArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:app:DaprComponentResiliencyPolicy")
class DaprComponentResiliencyPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., component_name: Optional[pulumi.Input[_builtins.str]] = ..., environment_name: Optional[pulumi.Input[_builtins.str]] = ..., inbound_policy: Optional[pulumi.Input[Union[DaprComponentResiliencyPolicyConfigurationArgs, DaprComponentResiliencyPolicyConfigurationArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., outbound_policy: Optional[pulumi.Input[Union[DaprComponentResiliencyPolicyConfigurationArgs, DaprComponentResiliencyPolicyConfigurationArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DaprComponentResiliencyPolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DaprComponentResiliencyPolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inboundPolicy")
    def inbound_policy(self) -> pulumi.Output[Optional[outputs.DaprComponentResiliencyPolicyConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundPolicy")
    def outbound_policy(self) -> pulumi.Output[Optional[outputs.DaprComponentResiliencyPolicyConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


