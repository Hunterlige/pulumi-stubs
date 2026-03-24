

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConnectedRegistryResult', 'AwaitableGetConnectedRegistryResult', 'get_connected_registry', 'get_connected_registry_output']
@pulumi.output_type
class GetConnectedRegistryResult:
    
    def __init__(__self__, activation=..., azure_api_version=..., client_token_ids=..., connection_state=..., garbage_collection=..., id=..., last_activity_time=..., logging=..., login_server=..., mode=..., name=..., notifications_list=..., parent=..., provisioning_state=..., status_details=..., system_data=..., type=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def activation(self) -> outputs.ActivationPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientTokenIds")
    def client_token_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionState")
    def connection_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="garbageCollection")
    def garbage_collection(self) -> Optional[outputs.GarbageCollectionPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastActivityTime")
    def last_activity_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[outputs.LoggingPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginServer")
    def login_server(self) -> Optional[outputs.LoginServerPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationsList")
    def notifications_list(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> outputs.ParentPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> Sequence[outputs.StatusDetailPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetConnectedRegistryResult(GetConnectedRegistryResult):
    def __await__(self): # -> Generator[Never, Any, GetConnectedRegistryResult]:
        ...
    


def get_connected_registry(connected_registry_name: Optional[_builtins.str] = ..., registry_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConnectedRegistryResult:
    
    ...

def get_connected_registry_output(connected_registry_name: Optional[pulumi.Input[_builtins.str]] = ..., registry_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConnectedRegistryResult]:
    
    ...

