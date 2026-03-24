

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProjectEnvironmentTypeResult', 'AwaitableGetProjectEnvironmentTypeResult', 'get_project_environment_type', 'get_project_environment_type_output']
@pulumi.output_type
class GetProjectEnvironmentTypeResult:
    
    def __init__(__self__, azure_api_version=..., creator_role_assignment=..., deployment_target_id=..., display_name=..., environment_count=..., id=..., identity=..., location=..., name=..., provisioning_state=..., status=..., system_data=..., tags=..., type=..., user_role_assignments=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creatorRoleAssignment")
    def creator_role_assignment(self) -> Optional[outputs.ProjectEnvironmentTypeUpdatePropertiesResponseCreatorRoleAssignment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentTargetId")
    def deployment_target_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentCount")
    def environment_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
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
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="userRoleAssignments")
    def user_role_assignments(self) -> Optional[Mapping[str, outputs.UserRoleAssignmentResponse]]:
        
        ...
    


class AwaitableGetProjectEnvironmentTypeResult(GetProjectEnvironmentTypeResult):
    def __await__(self): # -> Generator[Never, Any, GetProjectEnvironmentTypeResult]:
        ...
    


def get_project_environment_type(environment_type_name: Optional[_builtins.str] = ..., project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProjectEnvironmentTypeResult:
    
    ...

def get_project_environment_type_output(environment_type_name: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProjectEnvironmentTypeResult]:
    
    ...

