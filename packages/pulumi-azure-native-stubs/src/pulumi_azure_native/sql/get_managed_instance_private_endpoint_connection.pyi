

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetManagedInstancePrivateEndpointConnectionResult', ..., 'get_managed_instance_private_endpoint_connection', ...]
@pulumi.output_type
class GetManagedInstancePrivateEndpointConnectionResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., private_endpoint=..., private_link_service_connection_state=..., provisioning_state=..., type=...) -> None:
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
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.ManagedInstancePrivateEndpointPropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.ManagedInstancePrivateLinkServiceConnectionStatePropertyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetManagedInstancePrivateEndpointConnectionResult(GetManagedInstancePrivateEndpointConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetManagedInstancePrivateEndpointConnectionResult]:
        ...
    


def get_managed_instance_private_endpoint_connection(managed_instance_name: Optional[_builtins.str] = ..., private_endpoint_connection_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagedInstancePrivateEndpointConnectionResult:
    
    ...

def get_managed_instance_private_endpoint_connection_output(managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., private_endpoint_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagedInstancePrivateEndpointConnectionResult]:
    
    ...

