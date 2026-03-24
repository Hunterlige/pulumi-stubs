

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['UserRuleArgs', 'UserRule']
@pulumi.input_type
class UserRuleArgs:
    def __init__(__self__, *, configuration_name: pulumi.Input[_builtins.str], direction: pulumi.Input[Union[_builtins.str, SecurityConfigurationRuleDirection]], kind: pulumi.Input[_builtins.str], network_manager_name: pulumi.Input[_builtins.str], protocol: pulumi.Input[Union[_builtins.str, SecurityConfigurationRuleProtocol]], resource_group_name: pulumi.Input[_builtins.str], rule_collection_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., destinations: Optional[pulumi.Input[Sequence[pulumi.Input[AddressPrefixItemArgs]]]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sources: Optional[pulumi.Input[Sequence[pulumi.Input[AddressPrefixItemArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @configuration_name.setter
    def configuration_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Input[Union[_builtins.str, SecurityConfigurationRuleDirection]]:
        
        ...
    
    @direction.setter
    def direction(self, value: pulumi.Input[Union[_builtins.str, SecurityConfigurationRuleDirection]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkManagerName")
    def network_manager_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_manager_name.setter
    def network_manager_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[Union[_builtins.str, SecurityConfigurationRuleProtocol]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[Union[_builtins.str, SecurityConfigurationRuleProtocol]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleCollectionName")
    def rule_collection_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_collection_name.setter
    def rule_collection_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @destination_port_ranges.setter
    def destination_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AddressPrefixItemArgs]]]]:
        
        ...
    
    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AddressPrefixItemArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_port_ranges.setter
    def source_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AddressPrefixItemArgs]]]]:
        
        ...
    
    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AddressPrefixItemArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:UserRule")
class UserRule(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., destinations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AddressPrefixItemArgs, AddressPrefixItemArgsDict]]]]] = ..., direction: Optional[pulumi.Input[Union[_builtins.str, SecurityConfigurationRuleDirection]]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[Union[_builtins.str, SecurityConfigurationRuleProtocol]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_collection_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AddressPrefixItemArgs, AddressPrefixItemArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UserRuleArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> UserRule:
        
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
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> pulumi.Output[Optional[Sequence[outputs.AddressPrefixItemResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Optional[Sequence[outputs.AddressPrefixItemResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


