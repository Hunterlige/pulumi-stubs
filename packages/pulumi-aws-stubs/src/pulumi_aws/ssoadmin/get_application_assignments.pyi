

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetApplicationAssignmentsResult', 'AwaitableGetApplicationAssignmentsResult', 'get_application_assignments', 'get_application_assignments_output']
@pulumi.output_type
class GetApplicationAssignmentsResult:
    
    def __init__(__self__, application_arn=..., application_assignments=..., id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationAssignments")
    def application_assignments(self) -> Sequence[outputs.GetApplicationAssignmentsApplicationAssignmentResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetApplicationAssignmentsResult(GetApplicationAssignmentsResult):
    def __await__(self): # -> Generator[Never, Any, GetApplicationAssignmentsResult]:
        ...
    


def get_application_assignments(application_arn: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetApplicationAssignmentsResult:
    
    ...

def get_application_assignments_output(application_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetApplicationAssignmentsResult]:
    
    ...

