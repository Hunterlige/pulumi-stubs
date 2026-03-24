

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSelectionResult', 'AwaitableGetSelectionResult', 'get_selection', 'get_selection_output']
@pulumi.output_type
class GetSelectionResult:
    
    def __init__(__self__, iam_role_arn=..., id=..., name=..., plan_id=..., region=..., resources=..., selection_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectionId")
    def selection_id(self) -> _builtins.str:
        ...
    


class AwaitableGetSelectionResult(GetSelectionResult):
    def __await__(self): # -> Generator[Never, Any, GetSelectionResult]:
        ...
    


def get_selection(plan_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., selection_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSelectionResult:
    
    ...

def get_selection_output(plan_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., selection_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSelectionResult]:
    
    ...

