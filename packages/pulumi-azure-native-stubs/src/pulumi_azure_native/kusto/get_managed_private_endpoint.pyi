

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetManagedPrivateEndpointResult', 'AwaitableGetManagedPrivateEndpointResult', 'get_managed_private_endpoint', 'get_managed_private_endpoint_output']
@pulumi.output_type
class GetManagedPrivateEndpointResult:
    
    def __init__(__self__, azure_api_version=..., group_id=..., id=..., name=..., private_link_resource_id=..., private_link_resource_region=..., provisioning_state=..., request_message=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceRegion")
    def private_link_resource_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetManagedPrivateEndpointResult(GetManagedPrivateEndpointResult):
    def __await__(self): # -> Generator[Never, Any, GetManagedPrivateEndpointResult]:
        ...
    


def get_managed_private_endpoint(cluster_name: Optional[_builtins.str] = ..., managed_private_endpoint_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagedPrivateEndpointResult:
    
    ...

def get_managed_private_endpoint_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., managed_private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagedPrivateEndpointResult]:
    
    ...

