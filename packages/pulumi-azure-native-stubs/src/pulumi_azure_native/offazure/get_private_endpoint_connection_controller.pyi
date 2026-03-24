

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPrivateEndpointConnectionControllerResult', ..., 'get_private_endpoint_connection_controller', 'get_private_endpoint_connection_controller_output']
@pulumi.output_type
class GetPrivateEndpointConnectionControllerResult:
    
    def __init__(__self__, azure_api_version=..., group_ids=..., id=..., name=..., private_endpoint=..., private_link_service_connection_state=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]:
        
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
    def private_endpoint(self) -> outputs.ResourceIdResponse:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPrivateEndpointConnectionControllerResult(GetPrivateEndpointConnectionControllerResult):
    def __await__(self): # -> Generator[Never, Any, GetPrivateEndpointConnectionControllerResult]:
        ...
    


def get_private_endpoint_connection_controller(pe_connection_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., site_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrivateEndpointConnectionControllerResult:
    
    ...

def get_private_endpoint_connection_controller_output(pe_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., site_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrivateEndpointConnectionControllerResult]:
    
    ...

