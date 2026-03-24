

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualNetworkResult', 'AwaitableGetVirtualNetworkResult', 'get_virtual_network', 'get_virtual_network_output']
@pulumi.output_type
class GetVirtualNetworkResult:
    
    def __init__(__self__, azure_api_version=..., extended_location=..., id=..., inventory_item_id=..., location=..., name=..., network_name=..., provisioning_state=..., system_data=..., tags=..., type=..., uuid=..., vmm_server_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="networkName")
    def network_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
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
    @pulumi.getter
    def uuid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetVirtualNetworkResult(GetVirtualNetworkResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualNetworkResult]:
        ...
    


def get_virtual_network(resource_group_name: Optional[_builtins.str] = ..., virtual_network_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualNetworkResult:
    
    ...

def get_virtual_network_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualNetworkResult]:
    
    ...

