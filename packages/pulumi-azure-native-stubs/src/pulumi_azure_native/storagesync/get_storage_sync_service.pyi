

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStorageSyncServiceResult', 'AwaitableGetStorageSyncServiceResult', 'get_storage_sync_service', 'get_storage_sync_service_output']
@pulumi.output_type
class GetStorageSyncServiceResult:
    
    def __init__(__self__, azure_api_version=..., id=..., identity=..., incoming_traffic_policy=..., last_operation_name=..., last_workflow_id=..., location=..., name=..., private_endpoint_connections=..., provisioning_state=..., storage_sync_service_status=..., storage_sync_service_uid=..., system_data=..., tags=..., type=..., use_identity=...) -> None:
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
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incomingTrafficPolicy")
    def incoming_traffic_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastOperationName")
    def last_operation_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastWorkflowId")
    def last_workflow_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSyncServiceStatus")
    def storage_sync_service_status(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSyncServiceUid")
    def storage_sync_service_uid(self) -> _builtins.str:
        
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
    
    @_builtins.property
    @pulumi.getter(name="useIdentity")
    def use_identity(self) -> _builtins.bool:
        
        ...
    


class AwaitableGetStorageSyncServiceResult(GetStorageSyncServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetStorageSyncServiceResult]:
        ...
    


def get_storage_sync_service(resource_group_name: Optional[_builtins.str] = ..., storage_sync_service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStorageSyncServiceResult:
    
    ...

def get_storage_sync_service_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_sync_service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStorageSyncServiceResult]:
    
    ...

