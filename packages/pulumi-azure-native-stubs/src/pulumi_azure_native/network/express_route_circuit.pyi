

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
__all__ = ['ExpressRouteCircuitArgs', 'ExpressRouteCircuit']
@pulumi.input_type
class ExpressRouteCircuitArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], allow_classic_operations: Optional[pulumi.Input[_builtins.bool]] = ..., authorization_key: Optional[pulumi.Input[_builtins.str]] = ..., authorizations: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressRouteCircuitAuthorizationArgs]]]] = ..., bandwidth_in_gbps: Optional[pulumi.Input[_builtins.float]] = ..., circuit_name: Optional[pulumi.Input[_builtins.str]] = ..., circuit_provisioning_state: Optional[pulumi.Input[_builtins.str]] = ..., enable_direct_port_rate_limit: Optional[pulumi.Input[_builtins.bool]] = ..., express_route_port: Optional[pulumi.Input[SubResourceArgs]] = ..., gateway_manager_etag: Optional[pulumi.Input[_builtins.str]] = ..., global_reach_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., peerings: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressRouteCircuitPeeringArgs]]]] = ..., service_key: Optional[pulumi.Input[_builtins.str]] = ..., service_provider_notes: Optional[pulumi.Input[_builtins.str]] = ..., service_provider_properties: Optional[pulumi.Input[ExpressRouteCircuitServiceProviderPropertiesArgs]] = ..., service_provider_provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ServiceProviderProvisioningState]]] = ..., sku: Optional[pulumi.Input[ExpressRouteCircuitSkuArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowClassicOperations")
    def allow_classic_operations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_classic_operations.setter
    def allow_classic_operations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_key.setter
    def authorization_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorizations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExpressRouteCircuitAuthorizationArgs]]]]:
        
        ...
    
    @authorizations.setter
    def authorizations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressRouteCircuitAuthorizationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bandwidthInGbps")
    def bandwidth_in_gbps(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @bandwidth_in_gbps.setter
    def bandwidth_in_gbps(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitName")
    def circuit_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @circuit_name.setter
    def circuit_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitProvisioningState")
    def circuit_provisioning_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @circuit_provisioning_state.setter
    def circuit_provisioning_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDirectPortRateLimit")
    def enable_direct_port_rate_limit(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_direct_port_rate_limit.setter
    def enable_direct_port_rate_limit(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRoutePort")
    def express_route_port(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @express_route_port.setter
    def express_route_port(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayManagerEtag")
    def gateway_manager_etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_manager_etag.setter
    def gateway_manager_etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalReachEnabled")
    def global_reach_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @global_reach_enabled.setter
    def global_reach_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def peerings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExpressRouteCircuitPeeringArgs]]]]:
        
        ...
    
    @peerings.setter
    def peerings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ExpressRouteCircuitPeeringArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_key.setter
    def service_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProviderNotes")
    def service_provider_notes(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_provider_notes.setter
    def service_provider_notes(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProviderProperties")
    def service_provider_properties(self) -> Optional[pulumi.Input[ExpressRouteCircuitServiceProviderPropertiesArgs]]:
        
        ...
    
    @service_provider_properties.setter
    def service_provider_properties(self, value: Optional[pulumi.Input[ExpressRouteCircuitServiceProviderPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProviderProvisioningState")
    def service_provider_provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ServiceProviderProvisioningState]]]:
        
        ...
    
    @service_provider_provisioning_state.setter
    def service_provider_provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ServiceProviderProvisioningState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[ExpressRouteCircuitSkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[ExpressRouteCircuitSkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:ExpressRouteCircuit")
class ExpressRouteCircuit(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_classic_operations: Optional[pulumi.Input[_builtins.bool]] = ..., authorization_key: Optional[pulumi.Input[_builtins.str]] = ..., authorizations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ExpressRouteCircuitAuthorizationArgs, ExpressRouteCircuitAuthorizationArgsDict]]]]] = ..., bandwidth_in_gbps: Optional[pulumi.Input[_builtins.float]] = ..., circuit_name: Optional[pulumi.Input[_builtins.str]] = ..., circuit_provisioning_state: Optional[pulumi.Input[_builtins.str]] = ..., enable_direct_port_rate_limit: Optional[pulumi.Input[_builtins.bool]] = ..., express_route_port: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., gateway_manager_etag: Optional[pulumi.Input[_builtins.str]] = ..., global_reach_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., peerings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ExpressRouteCircuitPeeringArgs, ExpressRouteCircuitPeeringArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_key: Optional[pulumi.Input[_builtins.str]] = ..., service_provider_notes: Optional[pulumi.Input[_builtins.str]] = ..., service_provider_properties: Optional[pulumi.Input[Union[ExpressRouteCircuitServiceProviderPropertiesArgs, ExpressRouteCircuitServiceProviderPropertiesArgsDict]]] = ..., service_provider_provisioning_state: Optional[pulumi.Input[Union[_builtins.str, ServiceProviderProvisioningState]]] = ..., sku: Optional[pulumi.Input[Union[ExpressRouteCircuitSkuArgs, ExpressRouteCircuitSkuArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ExpressRouteCircuitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ExpressRouteCircuit:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowClassicOperations")
    def allow_classic_operations(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationStatus")
    def authorization_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorizations(self) -> pulumi.Output[Optional[Sequence[outputs.ExpressRouteCircuitAuthorizationResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bandwidthInGbps")
    def bandwidth_in_gbps(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitProvisioningState")
    def circuit_provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDirectPortRateLimit")
    def enable_direct_port_rate_limit(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRoutePort")
    def express_route_port(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayManagerEtag")
    def gateway_manager_etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalReachEnabled")
    def global_reach_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def peerings(self) -> pulumi.Output[Optional[Sequence[outputs.ExpressRouteCircuitPeeringResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProviderNotes")
    def service_provider_notes(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProviderProperties")
    def service_provider_properties(self) -> pulumi.Output[Optional[outputs.ExpressRouteCircuitServiceProviderPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProviderProvisioningState")
    def service_provider_provisioning_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.ExpressRouteCircuitSkuResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stag(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


