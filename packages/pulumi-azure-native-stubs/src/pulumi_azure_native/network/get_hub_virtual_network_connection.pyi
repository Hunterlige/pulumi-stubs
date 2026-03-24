

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetHubVirtualNetworkConnectionResult', 'AwaitableGetHubVirtualNetworkConnectionResult', 'get_hub_virtual_network_connection', 'get_hub_virtual_network_connection_output']
@pulumi.output_type
class GetHubVirtualNetworkConnectionResult:
    
    def __init__(__self__, allow_hub_to_remote_vnet_transit=..., allow_remote_vnet_to_use_hub_vnet_gateways=..., azure_api_version=..., enable_internet_security=..., etag=..., id=..., name=..., provisioning_state=..., remote_virtual_network=..., routing_configuration=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowHubToRemoteVnetTransit")
    def allow_hub_to_remote_vnet_transit(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowRemoteVnetToUseHubVnetGateways")
    def allow_remote_vnet_to_use_hub_vnet_gateways(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteVirtualNetwork")
    def remote_virtual_network(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingConfiguration")
    def routing_configuration(self) -> Optional[outputs.RoutingConfigurationResponse]:
        
        ...
    


class AwaitableGetHubVirtualNetworkConnectionResult(GetHubVirtualNetworkConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetHubVirtualNetworkConnectionResult]:
        ...
    


def get_hub_virtual_network_connection(connection_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., virtual_hub_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetHubVirtualNetworkConnectionResult:
    
    ...

def get_hub_virtual_network_connection_output(connection_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetHubVirtualNetworkConnectionResult]:
    
    ...

