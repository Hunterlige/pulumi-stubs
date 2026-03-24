

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLocalNetworkGatewayResult', 'AwaitableGetLocalNetworkGatewayResult', 'get_local_network_gateway', 'get_local_network_gateway_output']
@pulumi.output_type
class GetLocalNetworkGatewayResult:
    
    def __init__(__self__, azure_api_version=..., bgp_settings=..., etag=..., fqdn=..., gateway_ip_address=..., id=..., local_network_address_space=..., location=..., name=..., provisioning_state=..., resource_guid=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpSettings")
    def bgp_settings(self) -> Optional[outputs.BgpSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayIpAddress")
    def gateway_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localNetworkAddressSpace")
    def local_network_address_space(self) -> Optional[outputs.AddressSpaceResponse]:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetLocalNetworkGatewayResult(GetLocalNetworkGatewayResult):
    def __await__(self): # -> Generator[Never, Any, GetLocalNetworkGatewayResult]:
        ...
    


def get_local_network_gateway(local_network_gateway_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLocalNetworkGatewayResult:
    
    ...

def get_local_network_gateway_output(local_network_gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLocalNetworkGatewayResult]:
    
    ...

