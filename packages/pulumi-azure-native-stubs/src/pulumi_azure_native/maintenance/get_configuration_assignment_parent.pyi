

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetConfigurationAssignmentParentResult', 'AwaitableGetConfigurationAssignmentParentResult', 'get_configuration_assignment_parent', 'get_configuration_assignment_parent_output']
@pulumi.output_type
class GetConfigurationAssignmentParentResult:
    
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
    


class AwaitableGetConfigurationAssignmentParentResult(GetConfigurationAssignmentParentResult):
    def __await__(self): # -> Generator[Never, Any, GetConfigurationAssignmentParentResult]:
        ...
    


def get_configuration_assignment_parent(configuration_assignment_name: Optional[_builtins.str] = ..., provider_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., resource_parent_name: Optional[_builtins.str] = ..., resource_parent_type: Optional[_builtins.str] = ..., resource_type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetConfigurationAssignmentParentResult:
    
    ...

def get_configuration_assignment_parent_output(configuration_assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., provider_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_parent_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_parent_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetConfigurationAssignmentParentResult]:
    
    ...

