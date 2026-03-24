

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetGuestConfigurationAssignmentsVMSSResult', ..., 'get_guest_configuration_assignments_vmss', 'get_guest_configuration_assignments_vmss_output']
@pulumi.output_type
class GetGuestConfigurationAssignmentsVMSSResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., properties=..., system_data=..., type=...) -> None:
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
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.GuestConfigurationAssignmentPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetGuestConfigurationAssignmentsVMSSResult(GetGuestConfigurationAssignmentsVMSSResult):
    def __await__(self): # -> Generator[Never, Any, GetGuestConfigurationAssignmentsVMSSResult]:
        ...
    


def get_guest_configuration_assignments_vmss(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., vmss_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetGuestConfigurationAssignmentsVMSSResult:
    
    ...

def get_guest_configuration_assignments_vmss_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., vmss_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetGuestConfigurationAssignmentsVMSSResult]:
    
    ...

