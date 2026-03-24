

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualHubBgpConnectionResult', 'AwaitableGetVirtualHubBgpConnectionResult', 'get_virtual_hub_bgp_connection', 'get_virtual_hub_bgp_connection_output']
@pulumi.output_type
class GetVirtualHubBgpConnectionResult:
    
    def __init__(__self__, azure_api_version=..., connection_state=..., etag=..., hub_virtual_network_connection=..., id=..., name=..., peer_asn=..., peer_ip=..., provisioning_state=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionState")
    def connection_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubVirtualNetworkConnection")
    def hub_virtual_network_connection(self) -> Optional[outputs.SubResourceResponse]:
        
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
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerIp")
    def peer_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVirtualHubBgpConnectionResult(GetVirtualHubBgpConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualHubBgpConnectionResult]:
        ...
    


def get_virtual_hub_bgp_connection(connection_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., virtual_hub_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualHubBgpConnectionResult:
    
    ...

def get_virtual_hub_bgp_connection_output(connection_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualHubBgpConnectionResult]:
    
    ...

