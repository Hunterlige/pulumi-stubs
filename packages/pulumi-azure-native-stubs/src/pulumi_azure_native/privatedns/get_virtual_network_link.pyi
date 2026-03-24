

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualNetworkLinkResult', 'AwaitableGetVirtualNetworkLinkResult', 'get_virtual_network_link', 'get_virtual_network_link_output']
@pulumi.output_type
class GetVirtualNetworkLinkResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., location=..., name=..., provisioning_state=..., registration_enabled=..., resolution_policy=..., system_data=..., tags=..., type=..., virtual_network=..., virtual_network_link_state=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="registrationEnabled")
    def registration_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolutionPolicy")
    def resolution_policy(self) -> Optional[_builtins.str]:
        
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
    def virtual_network(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkLinkState")
    def virtual_network_link_state(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVirtualNetworkLinkResult(GetVirtualNetworkLinkResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualNetworkLinkResult]:
        ...
    


def get_virtual_network_link(private_zone_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., virtual_network_link_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualNetworkLinkResult:
    
    ...

def get_virtual_network_link_output(private_zone_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_link_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualNetworkLinkResult]:
    
    ...

