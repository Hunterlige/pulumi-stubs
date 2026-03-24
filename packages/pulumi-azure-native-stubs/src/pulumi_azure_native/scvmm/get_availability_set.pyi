

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAvailabilitySetResult', 'AwaitableGetAvailabilitySetResult', 'get_availability_set', 'get_availability_set_output']
@pulumi.output_type
class GetAvailabilitySetResult:
    
    def __init__(__self__, availability_set_name=..., azure_api_version=..., extended_location=..., id=..., location=..., name=..., provisioning_state=..., system_data=..., tags=..., type=..., vmm_server_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilitySetName")
    def availability_set_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetAvailabilitySetResult(GetAvailabilitySetResult):
    def __await__(self): # -> Generator[Never, Any, GetAvailabilitySetResult]:
        ...
    


def get_availability_set(availability_set_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAvailabilitySetResult:
    
    ...

def get_availability_set_output(availability_set_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAvailabilitySetResult]:
    
    ...

