

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPrincipalApplicationAssignmentsResult', 'AwaitableGetPrincipalApplicationAssignmentsResult', 'get_principal_application_assignments', 'get_principal_application_assignments_output']
@pulumi.output_type
class GetPrincipalApplicationAssignmentsResult:
    
    def __init__(__self__, application_assignments=..., id=..., instance_arn=..., principal_id=..., principal_type=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationAssignments")
    def application_assignments(self) -> Optional[Sequence[outputs.GetPrincipalApplicationAssignmentsApplicationAssignmentResult]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetPrincipalApplicationAssignmentsResult(GetPrincipalApplicationAssignmentsResult):
    def __await__(self): # -> Generator[Never, Any, GetPrincipalApplicationAssignmentsResult]:
        ...
    


def get_principal_application_assignments(application_assignments: Optional[Sequence[Union[GetPrincipalApplicationAssignmentsApplicationAssignmentArgs, GetPrincipalApplicationAssignmentsApplicationAssignmentArgsDict]]] = ..., instance_arn: Optional[_builtins.str] = ..., principal_id: Optional[_builtins.str] = ..., principal_type: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPrincipalApplicationAssignmentsResult:
    
    ...

def get_principal_application_assignments_output(application_assignments: Optional[pulumi.Input[Optional[Sequence[Union[GetPrincipalApplicationAssignmentsApplicationAssignmentArgs, GetPrincipalApplicationAssignmentsApplicationAssignmentArgsDict]]]]] = ..., instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., principal_id: Optional[pulumi.Input[_builtins.str]] = ..., principal_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPrincipalApplicationAssignmentsResult]:
    
    ...

