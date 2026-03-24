

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSoftwareUpdateConfigurationByNameResult', ..., 'get_software_update_configuration_by_name', 'get_software_update_configuration_by_name_output']
@pulumi.output_type
class GetSoftwareUpdateConfigurationByNameResult:
    
    def __init__(__self__, azure_api_version=..., created_by=..., creation_time=..., error=..., id=..., last_modified_by=..., last_modified_time=..., name=..., provisioning_state=..., schedule_info=..., tasks=..., type=..., update_configuration=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ErrorResponseResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str:
        
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
    @pulumi.getter(name="scheduleInfo")
    def schedule_info(self) -> outputs.SUCSchedulePropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tasks(self) -> Optional[outputs.SoftwareUpdateConfigurationTasksResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateConfiguration")
    def update_configuration(self) -> outputs.UpdateConfigurationResponse:
        
        ...
    


class AwaitableGetSoftwareUpdateConfigurationByNameResult(GetSoftwareUpdateConfigurationByNameResult):
    def __await__(self): # -> Generator[Never, Any, GetSoftwareUpdateConfigurationByNameResult]:
        ...
    


def get_software_update_configuration_by_name(automation_account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., software_update_configuration_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSoftwareUpdateConfigurationByNameResult:
    
    ...

def get_software_update_configuration_by_name_output(automation_account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., software_update_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSoftwareUpdateConfigurationByNameResult]:
    
    ...

