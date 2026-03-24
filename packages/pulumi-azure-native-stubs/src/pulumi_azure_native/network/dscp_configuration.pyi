

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
__all__ = ['DscpConfigurationArgs', 'DscpConfiguration']
@pulumi.input_type
class DscpConfigurationArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], destination_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[QosIpRangeArgs]]]] = ..., destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[QosPortRangeArgs]]]] = ..., dscp_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., markings: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., protocol: Optional[pulumi.Input[Union[_builtins.str, ProtocolType]]] = ..., qos_definition_collection: Optional[pulumi.Input[Sequence[pulumi.Input[QosDefinitionArgs]]]] = ..., source_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[QosIpRangeArgs]]]] = ..., source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[QosPortRangeArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[QosIpRangeArgs]]]]:
        
        ...
    
    @destination_ip_ranges.setter
    def destination_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[QosIpRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[QosPortRangeArgs]]]]:
        
        ...
    
    @destination_port_ranges.setter
    def destination_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[QosPortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dscpConfigurationName")
    def dscp_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dscp_configuration_name.setter
    def dscp_configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def markings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @markings.setter
    def markings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[Union[_builtins.str, ProtocolType]]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[Union[_builtins.str, ProtocolType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="qosDefinitionCollection")
    def qos_definition_collection(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[QosDefinitionArgs]]]]:
        
        ...
    
    @qos_definition_collection.setter
    def qos_definition_collection(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[QosDefinitionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[QosIpRangeArgs]]]]:
        
        ...
    
    @source_ip_ranges.setter
    def source_ip_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[QosIpRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[QosPortRangeArgs]]]]:
        
        ...
    
    @source_port_ranges.setter
    def source_port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[QosPortRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:DscpConfiguration")
class DscpConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., destination_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[QosIpRangeArgs, QosIpRangeArgsDict]]]]] = ..., destination_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[QosPortRangeArgs, QosPortRangeArgsDict]]]]] = ..., dscp_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., markings: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., protocol: Optional[pulumi.Input[Union[_builtins.str, ProtocolType]]] = ..., qos_definition_collection: Optional[pulumi.Input[Sequence[pulumi.Input[Union[QosDefinitionArgs, QosDefinitionArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source_ip_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[QosIpRangeArgs, QosIpRangeArgsDict]]]]] = ..., source_port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[Union[QosPortRangeArgs, QosPortRangeArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DscpConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DscpConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedNetworkInterfaces")
    def associated_network_interfaces(self) -> pulumi.Output[Sequence[outputs.NetworkInterfaceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationIpRanges")
    def destination_ip_ranges(self) -> pulumi.Output[Optional[Sequence[outputs.QosIpRangeResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> pulumi.Output[Optional[Sequence[outputs.QosPortRangeResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def markings(self) -> pulumi.Output[Optional[Sequence[_builtins.int]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qosCollectionId")
    def qos_collection_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qosDefinitionCollection")
    def qos_definition_collection(self) -> pulumi.Output[Optional[Sequence[outputs.QosDefinitionResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIpRanges")
    def source_ip_ranges(self) -> pulumi.Output[Optional[Sequence[outputs.QosIpRangeResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> pulumi.Output[Optional[Sequence[outputs.QosPortRangeResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


