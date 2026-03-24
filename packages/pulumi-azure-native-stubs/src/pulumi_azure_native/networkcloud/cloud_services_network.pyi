

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
__all__ = ['CloudServicesNetworkArgs', 'CloudServicesNetwork']
@pulumi.input_type
class CloudServicesNetworkArgs:
    def __init__(__self__, *, extended_location: pulumi.Input[ExtendedLocationArgs], resource_group_name: pulumi.Input[_builtins.str], additional_egress_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[EgressEndpointArgs]]]] = ..., cloud_services_network_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_default_egress_endpoints: Optional[pulumi.Input[Union[_builtins.str, CloudServicesNetworkEnableDefaultEgressEndpoints]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationArgs]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalEgressEndpoints")
    def additional_egress_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EgressEndpointArgs]]]]:
        
        ...
    
    @additional_egress_endpoints.setter
    def additional_egress_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EgressEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudServicesNetworkName")
    def cloud_services_network_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_services_network_name.setter
    def cloud_services_network_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDefaultEgressEndpoints")
    def enable_default_egress_endpoints(self) -> Optional[pulumi.Input[Union[_builtins.str, CloudServicesNetworkEnableDefaultEgressEndpoints]]]:
        
        ...
    
    @enable_default_egress_endpoints.setter
    def enable_default_egress_endpoints(self, value: Optional[pulumi.Input[Union[_builtins.str, CloudServicesNetworkEnableDefaultEgressEndpoints]]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:networkcloud:CloudServicesNetwork")
class CloudServicesNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., additional_egress_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EgressEndpointArgs, EgressEndpointArgsDict]]]]] = ..., cloud_services_network_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_default_egress_endpoints: Optional[pulumi.Input[Union[_builtins.str, CloudServicesNetworkEnableDefaultEgressEndpoints]]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CloudServicesNetworkArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> CloudServicesNetwork:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalEgressEndpoints")
    def additional_egress_endpoints(self) -> pulumi.Output[Optional[Sequence[outputs.EgressEndpointResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedResourceIds")
    def associated_resource_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDefaultEgressEndpoints")
    def enable_default_egress_endpoints(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledEgressEndpoints")
    def enabled_egress_endpoints(self) -> pulumi.Output[Sequence[outputs.EgressEndpointResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridAksClustersAssociatedIds")
    def hybrid_aks_clusters_associated_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interfaceName")
    def interface_name(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
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
    
    @_builtins.property
    @pulumi.getter(name="virtualMachinesAssociatedIds")
    def virtual_machines_associated_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


