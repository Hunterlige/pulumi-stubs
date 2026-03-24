

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVpnServerConfigurationResult', 'AwaitableGetVpnServerConfigurationResult', 'get_vpn_server_configuration', 'get_vpn_server_configuration_output']
@pulumi.output_type
class GetVpnServerConfigurationResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., location=..., name=..., properties=..., tags=..., type=...) -> None:
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
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.VpnServerConfigurationPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVpnServerConfigurationResult(GetVpnServerConfigurationResult):
    def __await__(self): # -> Generator[Never, Any, GetVpnServerConfigurationResult]:
        ...
    


def get_vpn_server_configuration(resource_group_name: Optional[_builtins.str] = ..., vpn_server_configuration_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVpnServerConfigurationResult:
    
    ...

def get_vpn_server_configuration_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., vpn_server_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVpnServerConfigurationResult]:
    
    ...

