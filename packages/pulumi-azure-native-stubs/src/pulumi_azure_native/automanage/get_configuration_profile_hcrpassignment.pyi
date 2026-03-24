

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConfigurationProfileHCRPAssignmentResult', ..., 'get_configuration_profile_hcrpassignment', 'get_configuration_profile_hcrpassignment_output']
@pulumi.output_type
class GetConfigurationProfileHCRPAssignmentResult:
    
    def __init__(__self__, azure_api_version=..., id=..., managed_by=..., name=..., properties=..., system_data=..., type=...) -> None:
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
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ConfigurationProfileAssignmentPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetConfigurationProfileHCRPAssignmentResult(GetConfigurationProfileHCRPAssignmentResult):
    def __await__(self): # -> Generator[Never, Any, GetConfigurationProfileHCRPAssignmentResult]:
        ...
    


def get_configuration_profile_hcrpassignment(configuration_profile_assignment_name: Optional[_builtins.str] = ..., machine_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConfigurationProfileHCRPAssignmentResult:
    
    ...

def get_configuration_profile_hcrpassignment_output(configuration_profile_assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., machine_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConfigurationProfileHCRPAssignmentResult]:
    
    ...

