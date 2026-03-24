

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['OutboundRuleArgs', 'OutboundRule']
@pulumi.input_type
class OutboundRuleArgs:
    def __init__(__self__, *, managed_network_name: pulumi.Input[_builtins.str], properties: pulumi.Input[Union[FqdnOutboundRuleArgs, PrivateEndpointOutboundRuleArgs, ServiceTagOutboundRuleArgs]], resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], rule_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedNetworkName")
    def managed_network_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @managed_network_name.setter
    def managed_network_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Union[FqdnOutboundRuleArgs, PrivateEndpointOutboundRuleArgs, ServiceTagOutboundRuleArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[Union[FqdnOutboundRuleArgs, PrivateEndpointOutboundRuleArgs, ServiceTagOutboundRuleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:machinelearningservices:OutboundRule")
class OutboundRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., managed_network_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[Union[FqdnOutboundRuleArgs, FqdnOutboundRuleArgsDict], Union[PrivateEndpointOutboundRuleArgs, PrivateEndpointOutboundRuleArgsDict], Union[ServiceTagOutboundRuleArgs, ServiceTagOutboundRuleArgsDict]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OutboundRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> OutboundRule:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


