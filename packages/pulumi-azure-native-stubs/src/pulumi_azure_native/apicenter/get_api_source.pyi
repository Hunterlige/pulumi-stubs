

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetApiSourceResult', 'AwaitableGetApiSourceResult', 'get_api_source', 'get_api_source_output']
@pulumi.output_type
class GetApiSourceResult:
    
    def __init__(__self__, azure_api_management_source=..., azure_api_version=..., id=..., import_specification=..., link_state=..., name=..., system_data=..., target_environment_id=..., target_lifecycle_stage=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiManagementSource")
    def azure_api_management_source(self) -> Optional[outputs.AzureApiManagementSourceResponse]:
        
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
    @pulumi.getter(name="importSpecification")
    def import_specification(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkState")
    def link_state(self) -> outputs.LinkStateResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetEnvironmentId")
    def target_environment_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLifecycleStage")
    def target_lifecycle_stage(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetApiSourceResult(GetApiSourceResult):
    def __await__(self): # -> Generator[Never, Any, GetApiSourceResult]:
        ...
    


def get_api_source(api_source_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetApiSourceResult:
    
    ...

def get_api_source_output(api_source_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetApiSourceResult]:
    
    ...

