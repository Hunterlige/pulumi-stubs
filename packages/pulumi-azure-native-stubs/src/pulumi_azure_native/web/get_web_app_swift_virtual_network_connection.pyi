

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebAppSwiftVirtualNetworkConnectionResult', ..., 'get_web_app_swift_virtual_network_connection', ...]
@pulumi.output_type
class GetWebAppSwiftVirtualNetworkConnectionResult:
    
    def __init__(__self__, azure_api_version=..., id=..., kind=..., name=..., subnet_resource_id=..., swift_supported=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetResourceId")
    def subnet_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="swiftSupported")
    def swift_supported(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWebAppSwiftVirtualNetworkConnectionResult(GetWebAppSwiftVirtualNetworkConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetWebAppSwiftVirtualNetworkConnectionResult]:
        ...
    


def get_web_app_swift_virtual_network_connection(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebAppSwiftVirtualNetworkConnectionResult:
    
    ...

def get_web_app_swift_virtual_network_connection_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebAppSwiftVirtualNetworkConnectionResult]:
    
    ...

