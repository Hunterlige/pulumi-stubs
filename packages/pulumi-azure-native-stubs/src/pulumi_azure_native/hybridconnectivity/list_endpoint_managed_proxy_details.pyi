

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListEndpointManagedProxyDetailsResult', 'AwaitableListEndpointManagedProxyDetailsResult', 'list_endpoint_managed_proxy_details', 'list_endpoint_managed_proxy_details_output']
@pulumi.output_type
class ListEndpointManagedProxyDetailsResult:
    
    def __init__(__self__, expires_on=..., proxy=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def proxy(self) -> _builtins.str:
        
        ...
    


class AwaitableListEndpointManagedProxyDetailsResult(ListEndpointManagedProxyDetailsResult):
    def __await__(self): # -> Generator[Never, Any, ListEndpointManagedProxyDetailsResult]:
        ...
    


def list_endpoint_managed_proxy_details(endpoint_name: Optional[_builtins.str] = ..., hostname: Optional[_builtins.str] = ..., resource_uri: Optional[_builtins.str] = ..., service: Optional[_builtins.str] = ..., service_name: Optional[Union[_builtins.str, ServiceName]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListEndpointManagedProxyDetailsResult:
    
    ...

def list_endpoint_managed_proxy_details_output(endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., hostname: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[Optional[Union[_builtins.str, ServiceName]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListEndpointManagedProxyDetailsResult]:
    
    ...

