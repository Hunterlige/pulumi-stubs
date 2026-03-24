

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SecurityAdminConfigurationArgs', 'SecurityAdminConfiguration']
@pulumi.input_type
class SecurityAdminConfigurationArgs:
    def __init__(__self__, *, network_manager_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], apply_on_network_intent_policy_based_services: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, NetworkIntentPolicyBasedService]]]]] = ..., configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., network_group_address_space_aggregation_option: Optional[pulumi.Input[Union[_builtins.str, AddressSpaceAggregationOption]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkManagerName")
    def network_manager_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_manager_name.setter
    def network_manager_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyOnNetworkIntentPolicyBasedServices")
    def apply_on_network_intent_policy_based_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, NetworkIntentPolicyBasedService]]]]]:
        
        ...
    
    @apply_on_network_intent_policy_based_services.setter
    def apply_on_network_intent_policy_based_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, NetworkIntentPolicyBasedService]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration_name.setter
    def configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkGroupAddressSpaceAggregationOption")
    def network_group_address_space_aggregation_option(self) -> Optional[pulumi.Input[Union[_builtins.str, AddressSpaceAggregationOption]]]:
        
        ...
    
    @network_group_address_space_aggregation_option.setter
    def network_group_address_space_aggregation_option(self, value: Optional[pulumi.Input[Union[_builtins.str, AddressSpaceAggregationOption]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:SecurityAdminConfiguration")
class SecurityAdminConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., apply_on_network_intent_policy_based_services: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, NetworkIntentPolicyBasedService]]]]] = ..., configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., network_group_address_space_aggregation_option: Optional[pulumi.Input[Union[_builtins.str, AddressSpaceAggregationOption]]] = ..., network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SecurityAdminConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SecurityAdminConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyOnNetworkIntentPolicyBasedServices")
    def apply_on_network_intent_policy_based_services(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
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
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkGroupAddressSpaceAggregationOption")
    def network_group_address_space_aggregation_option(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


