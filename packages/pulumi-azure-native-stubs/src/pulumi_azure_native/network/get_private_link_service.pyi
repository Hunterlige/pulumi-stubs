

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPrivateLinkServiceResult', 'AwaitableGetPrivateLinkServiceResult', 'get_private_link_service', 'get_private_link_service_output']
@pulumi.output_type
class GetPrivateLinkServiceResult:
    
    def __init__(__self__, alias=..., auto_approval=..., azure_api_version=..., destination_ip_address=..., enable_proxy_protocol=..., etag=..., extended_location=..., fqdns=..., id=..., ip_configurations=..., load_balancer_frontend_ip_configurations=..., location=..., name=..., network_interfaces=..., private_endpoint_connections=..., provisioning_state=..., tags=..., type=..., visibility=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoApproval")
    def auto_approval(self) -> Optional[outputs.PrivateLinkServicePropertiesResponseAutoApproval]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationIPAddress")
    def destination_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableProxyProtocol")
    def enable_proxy_protocol(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdns(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Optional[Sequence[outputs.PrivateLinkServiceIpConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerFrontendIpConfigurations")
    def load_balancer_frontend_ip_configurations(self) -> Optional[Sequence[outputs.FrontendIPConfigurationResponse]]:
        
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
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Sequence[outputs.NetworkInterfaceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
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
    @pulumi.getter
    def visibility(self) -> Optional[outputs.PrivateLinkServicePropertiesResponseVisibility]:
        
        ...
    


class AwaitableGetPrivateLinkServiceResult(GetPrivateLinkServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetPrivateLinkServiceResult]:
        ...
    


def get_private_link_service(expand: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrivateLinkServiceResult:
    
    ...

def get_private_link_service_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrivateLinkServiceResult]:
    
    ...

