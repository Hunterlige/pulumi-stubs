

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMHSMPrivateEndpointConnectionResult', 'AwaitableGetMHSMPrivateEndpointConnectionResult', 'get_mhsm_private_endpoint_connection', 'get_mhsm_private_endpoint_connection_output']
@pulumi.output_type
class GetMHSMPrivateEndpointConnectionResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., identity=..., location=..., name=..., private_endpoint=..., private_link_service_connection_state=..., provisioning_state=..., sku=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
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
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.MHSMPrivateEndpointResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.MHSMPrivateLinkServiceConnectionStateResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.ManagedHsmSkuResponse]:
        
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
    


class AwaitableGetMHSMPrivateEndpointConnectionResult(GetMHSMPrivateEndpointConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetMHSMPrivateEndpointConnectionResult]:
        ...
    


def get_mhsm_private_endpoint_connection(name: Optional[_builtins.str] = ..., private_endpoint_connection_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMHSMPrivateEndpointConnectionResult:
    
    ...

def get_mhsm_private_endpoint_connection_output(name: Optional[pulumi.Input[_builtins.str]] = ..., private_endpoint_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMHSMPrivateEndpointConnectionResult]:
    
    ...

