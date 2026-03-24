

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualNetworkRetrieveResult', 'AwaitableGetVirtualNetworkRetrieveResult', 'get_virtual_network_retrieve', 'get_virtual_network_retrieve_output']
@pulumi.output_type
class GetVirtualNetworkRetrieveResult:
    
    def __init__(__self__, azure_api_version=..., extended_location=..., id=..., location=..., name=..., properties=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.VirtualNetworksResponseExtendedLocation]:
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
    @pulumi.getter
    def properties(self) -> outputs.VirtualNetworksPropertiesResponse:
        
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
    


class AwaitableGetVirtualNetworkRetrieveResult(GetVirtualNetworkRetrieveResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualNetworkRetrieveResult]:
        ...
    


def get_virtual_network_retrieve(resource_group_name: Optional[_builtins.str] = ..., virtual_networks_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualNetworkRetrieveResult:
    
    ...

def get_virtual_network_retrieve_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_networks_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualNetworkRetrieveResult]:
    
    ...

