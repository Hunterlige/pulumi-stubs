

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVirtualHubIpConfigurationResult', 'AwaitableGetVirtualHubIpConfigurationResult', 'get_virtual_hub_ip_configuration', 'get_virtual_hub_ip_configuration_output']
@pulumi.output_type
class GetVirtualHubIpConfigurationResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., name=..., private_ip_address=..., private_ip_allocation_method=..., provisioning_state=..., public_ip_address=..., subnet=..., type=...) -> None:
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
    @pulumi.getter(name="privateIPAddress")
    def private_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIPAllocationMethod")
    def private_ip_allocation_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIPAddress")
    def public_ip_address(self) -> Optional[outputs.PublicIPAddressResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[outputs.SubnetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVirtualHubIpConfigurationResult(GetVirtualHubIpConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualHubIpConfigurationResult]:
        ...
    


def get_virtual_hub_ip_configuration(ip_config_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., virtual_hub_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualHubIpConfigurationResult:
    
    ...

def get_virtual_hub_ip_configuration_output(ip_config_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualHubIpConfigurationResult]:
    
    ...

