

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ...]
@pulumi.output_type
class GetPrivateLinkServicePrivateEndpointConnectionResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., link_identifier=..., name=..., private_endpoint=..., private_endpoint_location=..., private_link_service_connection_state=..., provisioning_state=..., type=...) -> None:
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
    @pulumi.getter(name="linkIdentifier")
    def link_identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> outputs.PrivateEndpointResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointLocation")
    def private_endpoint_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPrivateLinkServicePrivateEndpointConnectionResult(GetPrivateLinkServicePrivateEndpointConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetPrivateLinkServicePrivateEndpointConnectionResult]:
        ...
    


def get_private_link_service_private_endpoint_connection(expand: Optional[_builtins.str] = ..., pe_connection_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrivateLinkServicePrivateEndpointConnectionResult:
    
    ...

def get_private_link_service_private_endpoint_connection_output(expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., pe_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrivateLinkServicePrivateEndpointConnectionResult]:
    
    ...

