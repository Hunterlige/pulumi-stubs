

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConfigurationAssignmentResult', 'AwaitableGetConfigurationAssignmentResult', 'get_configuration_assignment', 'get_configuration_assignment_output']
@pulumi.output_type
class GetConfigurationAssignmentResult:
    
    def __init__(__self__, azure_api_version=..., filter=..., id=..., location=..., maintenance_configuration_id=..., name=..., resource_id=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[outputs.ConfigurationAssignmentFilterPropertiesResponse]:
        
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
    @pulumi.getter(name="maintenanceConfigurationId")
    def maintenance_configuration_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetConfigurationAssignmentResult(GetConfigurationAssignmentResult):
    def __await__(self): # -> Generator[Never, Any, GetConfigurationAssignmentResult]:
        ...
    


def get_configuration_assignment(configuration_assignment_name: Optional[_builtins.str] = ..., provider_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., resource_type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConfigurationAssignmentResult:
    
    ...

def get_configuration_assignment_output(configuration_assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., provider_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConfigurationAssignmentResult]:
    
    ...

