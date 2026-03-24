

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProjectCatalogImageDefinitionBuildDetailsResult', ..., 'get_project_catalog_image_definition_build_details', ...]
@pulumi.output_type
class GetProjectCatalogImageDefinitionBuildDetailsResult:
    
    def __init__(__self__, end_time=..., error_details=..., id=..., image_reference=..., name=..., start_time=..., status=..., system_data=..., task_groups=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorDetails")
    def error_details(self) -> outputs.ImageCreationErrorDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> outputs.ImageReferenceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskGroups")
    def task_groups(self) -> Sequence[outputs.ImageDefinitionBuildTaskGroupResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetProjectCatalogImageDefinitionBuildDetailsResult(GetProjectCatalogImageDefinitionBuildDetailsResult):
    def __await__(self): # -> Generator[Never, Any, GetProjectCatalogImageDefinitionBuildDetailsResult]:
        ...
    


def get_project_catalog_image_definition_build_details(build_name: Optional[_builtins.str] = ..., catalog_name: Optional[_builtins.str] = ..., image_definition_name: Optional[_builtins.str] = ..., project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProjectCatalogImageDefinitionBuildDetailsResult:
    
    ...

def get_project_catalog_image_definition_build_details_output(build_name: Optional[pulumi.Input[_builtins.str]] = ..., catalog_name: Optional[pulumi.Input[_builtins.str]] = ..., image_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProjectCatalogImageDefinitionBuildDetailsResult]:
    
    ...

