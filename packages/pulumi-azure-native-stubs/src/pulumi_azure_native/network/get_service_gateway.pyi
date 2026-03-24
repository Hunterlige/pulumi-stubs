

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetServiceGatewayResult', 'AwaitableGetServiceGatewayResult', 'get_service_gateway', 'get_service_gateway_output']
@pulumi.output_type
class GetServiceGatewayResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., location=..., name=..., provisioning_state=..., resource_guid=..., route_target_address=..., route_target_address_v6=..., sku=..., system_data=..., tags=..., type=..., virtual_network=..., zones=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTargetAddress")
    def route_target_address(self) -> Optional[outputs.RouteTargetAddressPropertiesFormatResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeTargetAddressV6")
    def route_target_address_v6(self) -> Optional[outputs.RouteTargetAddressPropertiesFormatResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.ServiceGatewaySkuResponse]:
        
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
    
    @_builtins.property
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> Optional[outputs.VirtualNetworkResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetServiceGatewayResult(GetServiceGatewayResult):
    def __await__(self): # -> Generator[Never, Any, GetServiceGatewayResult]:
        ...
    


def get_service_gateway(resource_group_name: Optional[_builtins.str] = ..., service_gateway_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetServiceGatewayResult:
    
    ...

def get_service_gateway_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetServiceGatewayResult]:
    
    ...

