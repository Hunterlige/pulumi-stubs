

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBareMetalMachineKeySetResult', 'AwaitableGetBareMetalMachineKeySetResult', 'get_bare_metal_machine_key_set', 'get_bare_metal_machine_key_set_output']
@pulumi.output_type
class GetBareMetalMachineKeySetResult:
    def __init__(__self__, azure_api_version=..., azure_group_id=..., detailed_status=..., detailed_status_message=..., etag=..., expiration=..., extended_location=..., id=..., jump_hosts_allowed=..., last_validation=..., location=..., name=..., os_group_name=..., privilege_level=..., provisioning_state=..., system_data=..., tags=..., type=..., user_list=..., user_list_status=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureGroupId")
    def azure_group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jumpHostsAllowed")
    def jump_hosts_allowed(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastValidation")
    def last_validation(self) -> _builtins.str:
        
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
    @pulumi.getter(name="osGroupName")
    def os_group_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privilegeLevel")
    def privilege_level(self) -> _builtins.str:
        
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
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userList")
    def user_list(self) -> Sequence[outputs.KeySetUserResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userListStatus")
    def user_list_status(self) -> Sequence[outputs.KeySetUserStatusResponse]:
        
        ...
    


class AwaitableGetBareMetalMachineKeySetResult(GetBareMetalMachineKeySetResult):
    def __await__(self): # -> Generator[Never, Any, GetBareMetalMachineKeySetResult]:
        ...
    


def get_bare_metal_machine_key_set(bare_metal_machine_key_set_name: Optional[_builtins.str] = ..., cluster_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBareMetalMachineKeySetResult:
    
    ...

def get_bare_metal_machine_key_set_output(bare_metal_machine_key_set_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBareMetalMachineKeySetResult]:
    
    ...

