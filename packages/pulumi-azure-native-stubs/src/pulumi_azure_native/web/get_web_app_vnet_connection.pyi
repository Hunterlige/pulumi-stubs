

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebAppVnetConnectionResult', 'AwaitableGetWebAppVnetConnectionResult', 'get_web_app_vnet_connection', 'get_web_app_vnet_connection_output']
@pulumi.output_type
class GetWebAppVnetConnectionResult:
    
    def __init__(__self__, azure_api_version=..., cert_blob=..., cert_thumbprint=..., dns_servers=..., id=..., is_swift=..., kind=..., name=..., resync_required=..., routes=..., type=..., vnet_resource_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certBlob")
    def cert_blob(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certThumbprint")
    def cert_thumbprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSwift")
    def is_swift(self) -> Optional[_builtins.bool]:
        
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
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Sequence[outputs.VnetRouteResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vnetResourceId")
    def vnet_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetWebAppVnetConnectionResult(GetWebAppVnetConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetWebAppVnetConnectionResult]:
        ...
    


def get_web_app_vnet_connection(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., vnet_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebAppVnetConnectionResult:
    
    ...

def get_web_app_vnet_connection_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., vnet_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebAppVnetConnectionResult]:
    
    ...

