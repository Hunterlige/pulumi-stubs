

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkspaceManagerAssignmentResult', 'AwaitableGetWorkspaceManagerAssignmentResult', 'get_workspace_manager_assignment', 'get_workspace_manager_assignment_output']
@pulumi.output_type
class GetWorkspaceManagerAssignmentResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., items=..., last_job_end_time=..., last_job_provisioning_state=..., name=..., system_data=..., target_resource_name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[outputs.AssignmentItemResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastJobEndTime")
    def last_job_end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastJobProvisioningState")
    def last_job_provisioning_state(self) -> _builtins.str:
        
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
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWorkspaceManagerAssignmentResult(GetWorkspaceManagerAssignmentResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkspaceManagerAssignmentResult]:
        ...
    


def get_workspace_manager_assignment(resource_group_name: Optional[_builtins.str] = ..., workspace_manager_assignment_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkspaceManagerAssignmentResult:
    
    ...

def get_workspace_manager_assignment_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_manager_assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkspaceManagerAssignmentResult]:
    
    ...

