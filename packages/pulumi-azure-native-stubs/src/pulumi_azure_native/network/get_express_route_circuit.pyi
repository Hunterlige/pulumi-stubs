

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetExpressRouteCircuitResult', 'AwaitableGetExpressRouteCircuitResult', 'get_express_route_circuit', 'get_express_route_circuit_output']
@pulumi.output_type
class GetExpressRouteCircuitResult:
    
    def __init__(__self__, allow_classic_operations=..., authorization_key=..., authorization_status=..., authorizations=..., azure_api_version=..., bandwidth_in_gbps=..., circuit_provisioning_state=..., enable_direct_port_rate_limit=..., etag=..., express_route_port=..., gateway_manager_etag=..., global_reach_enabled=..., id=..., location=..., name=..., peerings=..., provisioning_state=..., service_key=..., service_provider_notes=..., service_provider_properties=..., service_provider_provisioning_state=..., sku=..., stag=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowClassicOperations")
    def allow_classic_operations(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationStatus")
    def authorization_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorizations(self) -> Optional[Sequence[outputs.ExpressRouteCircuitAuthorizationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bandwidthInGbps")
    def bandwidth_in_gbps(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitProvisioningState")
    def circuit_provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDirectPortRateLimit")
    def enable_direct_port_rate_limit(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRoutePort")
    def express_route_port(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayManagerEtag")
    def gateway_manager_etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalReachEnabled")
    def global_reach_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def peerings(self) -> Optional[Sequence[outputs.ExpressRouteCircuitPeeringResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProviderNotes")
    def service_provider_notes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProviderProperties")
    def service_provider_properties(self) -> Optional[outputs.ExpressRouteCircuitServiceProviderPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProviderProvisioningState")
    def service_provider_provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.ExpressRouteCircuitSkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stag(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetExpressRouteCircuitResult(GetExpressRouteCircuitResult):
    def __await__(self): # -> Generator[Never, Any, GetExpressRouteCircuitResult]:
        ...
    


def get_express_route_circuit(circuit_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetExpressRouteCircuitResult:
    
    ...

def get_express_route_circuit_output(circuit_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetExpressRouteCircuitResult]:
    
    ...

