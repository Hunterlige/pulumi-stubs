

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCloudEdgeManagementRoleResult', 'AwaitableGetCloudEdgeManagementRoleResult', 'get_cloud_edge_management_role', 'get_cloud_edge_management_role_output']
@pulumi.output_type
class GetCloudEdgeManagementRoleResult:
    
    def __init__(__self__, azure_api_version=..., edge_profile=..., id=..., kind=..., local_management_status=..., name=..., role_status=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeProfile")
    def edge_profile(self) -> outputs.EdgeProfileResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localManagementStatus")
    def local_management_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleStatus")
    def role_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCloudEdgeManagementRoleResult(GetCloudEdgeManagementRoleResult):
    def __await__(self): # -> Generator[Never, Any, GetCloudEdgeManagementRoleResult]:
        ...
    


def get_cloud_edge_management_role(device_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCloudEdgeManagementRoleResult:
    
    ...

def get_cloud_edge_management_role_output(device_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCloudEdgeManagementRoleResult]:
    
    ...

