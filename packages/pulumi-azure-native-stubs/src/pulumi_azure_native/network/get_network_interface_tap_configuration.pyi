

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkInterfaceTapConfigurationResult', 'AwaitableGetNetworkInterfaceTapConfigurationResult', 'get_network_interface_tap_configuration', 'get_network_interface_tap_configuration_output']
@pulumi.output_type
class GetNetworkInterfaceTapConfigurationResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., name=..., provisioning_state=..., type=..., virtual_network_tap=...) -> None:
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
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkTap")
    def virtual_network_tap(self) -> Optional[outputs.VirtualNetworkTapResponse]:
        
        ...
    


class AwaitableGetNetworkInterfaceTapConfigurationResult(GetNetworkInterfaceTapConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkInterfaceTapConfigurationResult]:
        ...
    


def get_network_interface_tap_configuration(network_interface_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., tap_configuration_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkInterfaceTapConfigurationResult:
    
    ...

def get_network_interface_tap_configuration_output(network_interface_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tap_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkInterfaceTapConfigurationResult]:
    
    ...

