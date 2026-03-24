

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetL3IsolationDomainResult', 'AwaitableGetL3IsolationDomainResult', 'get_l3_isolation_domain', 'get_l3_isolation_domain_output']
@pulumi.output_type
class GetL3IsolationDomainResult:
    
    def __init__(__self__, administrative_state=..., aggregate_route_configuration=..., annotation=..., azure_api_version=..., configuration_state=..., connected_subnet_route_policy=..., id=..., location=..., name=..., network_fabric_id=..., provisioning_state=..., redistribute_connected_subnets=..., redistribute_static_routes=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregateRouteConfiguration")
    def aggregate_route_configuration(self) -> Optional[outputs.AggregateRouteConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedSubnetRoutePolicy")
    def connected_subnet_route_policy(self) -> Optional[outputs.ConnectedSubnetRoutePolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redistributeConnectedSubnets")
    def redistribute_connected_subnets(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redistributeStaticRoutes")
    def redistribute_static_routes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetL3IsolationDomainResult(GetL3IsolationDomainResult):
    def __await__(self): # -> Generator[Never, Any, GetL3IsolationDomainResult]:
        ...
    


def get_l3_isolation_domain(l3_isolation_domain_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetL3IsolationDomainResult:
    
    ...

def get_l3_isolation_domain_output(l3_isolation_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetL3IsolationDomainResult]:
    
    ...

