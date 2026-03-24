

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NetworkTapArgs', 'NetworkTap']
@pulumi.input_type
class NetworkTapArgs:
    def __init__(__self__, *, destinations: pulumi.Input[Sequence[pulumi.Input[NetworkTapPropertiesDestinationsArgs]]], network_packet_broker_id: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], annotation: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_tap_name: Optional[pulumi.Input[_builtins.str]] = ..., polling_type: Optional[pulumi.Input[Union[_builtins.str, PollingType]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> pulumi.Input[Sequence[pulumi.Input[NetworkTapPropertiesDestinationsArgs]]]:
        
        ...
    
    @destinations.setter
    def destinations(self, value: pulumi.Input[Sequence[pulumi.Input[NetworkTapPropertiesDestinationsArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPacketBrokerId")
    def network_packet_broker_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_packet_broker_id.setter
    def network_packet_broker_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkTapName")
    def network_tap_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_tap_name.setter
    def network_tap_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pollingType")
    def polling_type(self) -> Optional[pulumi.Input[Union[_builtins.str, PollingType]]]:
        
        ...
    
    @polling_type.setter
    def polling_type(self, value: Optional[pulumi.Input[Union[_builtins.str, PollingType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:managednetworkfabric:NetworkTap")
class NetworkTap(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., annotation: Optional[pulumi.Input[_builtins.str]] = ..., destinations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkTapPropertiesDestinationsArgs, NetworkTapPropertiesDestinationsArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_packet_broker_id: Optional[pulumi.Input[_builtins.str]] = ..., network_tap_name: Optional[pulumi.Input[_builtins.str]] = ..., polling_type: Optional[pulumi.Input[Union[_builtins.str, PollingType]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NetworkTapArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> NetworkTap:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> pulumi.Output[Sequence[outputs.NetworkTapPropertiesResponseDestinations]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPacketBrokerId")
    def network_packet_broker_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pollingType")
    def polling_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceTapRuleId")
    def source_tap_rule_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


