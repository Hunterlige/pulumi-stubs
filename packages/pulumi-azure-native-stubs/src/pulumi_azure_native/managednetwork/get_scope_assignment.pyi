

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetScopeAssignmentResult', 'AwaitableGetScopeAssignmentResult', 'get_scope_assignment', 'get_scope_assignment_output']
@pulumi.output_type
class GetScopeAssignmentResult:
    
    def __init__(__self__, assigned_managed_network=..., azure_api_version=..., etag=..., id=..., location=..., name=..., provisioning_state=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedManagedNetwork")
    def assigned_managed_network(self) -> Optional[_builtins.str]:
        
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
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetScopeAssignmentResult(GetScopeAssignmentResult):
    def __await__(self): # -> Generator[Never, Any, GetScopeAssignmentResult]:
        ...
    


def get_scope_assignment(scope: Optional[_builtins.str] = ..., scope_assignment_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetScopeAssignmentResult:
    
    ...

def get_scope_assignment_output(scope: Optional[pulumi.Input[_builtins.str]] = ..., scope_assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetScopeAssignmentResult]:
    
    ...

