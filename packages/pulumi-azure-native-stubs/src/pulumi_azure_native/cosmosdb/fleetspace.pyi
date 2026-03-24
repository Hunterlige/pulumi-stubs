

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
__all__ = ['FleetspaceArgs', 'Fleetspace']
@pulumi.input_type
class FleetspaceArgs:
    def __init__(__self__, *, fleet_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], data_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., fleetspace_api_kind: Optional[pulumi.Input[Union[_builtins.str, FleetspaceApiKind]]] = ..., fleetspace_name: Optional[pulumi.Input[_builtins.str]] = ..., service_tier: Optional[pulumi.Input[Union[_builtins.str, ServiceTier]]] = ..., throughput_pool_configuration: Optional[pulumi.Input[FleetspacePropertiesThroughputPoolConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetName")
    def fleet_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @fleet_name.setter
    def fleet_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRegions")
    def data_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @data_regions.setter
    def data_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetspaceApiKind")
    def fleetspace_api_kind(self) -> Optional[pulumi.Input[Union[_builtins.str, FleetspaceApiKind]]]:
        
        ...
    
    @fleetspace_api_kind.setter
    def fleetspace_api_kind(self, value: Optional[pulumi.Input[Union[_builtins.str, FleetspaceApiKind]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetspaceName")
    def fleetspace_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fleetspace_name.setter
    def fleetspace_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceTier")
    def service_tier(self) -> Optional[pulumi.Input[Union[_builtins.str, ServiceTier]]]:
        
        ...
    
    @service_tier.setter
    def service_tier(self, value: Optional[pulumi.Input[Union[_builtins.str, ServiceTier]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputPoolConfiguration")
    def throughput_pool_configuration(self) -> Optional[pulumi.Input[FleetspacePropertiesThroughputPoolConfigurationArgs]]:
        
        ...
    
    @throughput_pool_configuration.setter
    def throughput_pool_configuration(self, value: Optional[pulumi.Input[FleetspacePropertiesThroughputPoolConfigurationArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:cosmosdb:Fleetspace")
class Fleetspace(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., fleet_name: Optional[pulumi.Input[_builtins.str]] = ..., fleetspace_api_kind: Optional[pulumi.Input[Union[_builtins.str, FleetspaceApiKind]]] = ..., fleetspace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_tier: Optional[pulumi.Input[Union[_builtins.str, ServiceTier]]] = ..., throughput_pool_configuration: Optional[pulumi.Input[Union[FleetspacePropertiesThroughputPoolConfigurationArgs, FleetspacePropertiesThroughputPoolConfigurationArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FleetspaceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Fleetspace:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRegions")
    def data_regions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetspaceApiKind")
    def fleetspace_api_kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="serviceTier")
    def service_tier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="throughputPoolConfiguration")
    def throughput_pool_configuration(self) -> pulumi.Output[Optional[outputs.FleetspacePropertiesResponseThroughputPoolConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


