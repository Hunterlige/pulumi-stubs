

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetControlResult', 'AwaitableGetControlResult', 'get_control', 'get_control_output']
@pulumi.output_type
class GetControlResult:
    
    def __init__(__self__, action_plan_instructions=..., action_plan_title=..., arn=..., control_mapping_sources=..., description=..., id=..., name=..., region=..., tags=..., testing_information=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionPlanInstructions")
    def action_plan_instructions(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionPlanTitle")
    def action_plan_title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlMappingSources")
    def control_mapping_sources(self) -> Sequence[outputs.GetControlControlMappingSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
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
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testingInformation")
    def testing_information(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    


class AwaitableGetControlResult(GetControlResult):
    def __await__(self): # -> Generator[Never, Any, GetControlResult]:
        ...
    


def get_control(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetControlResult:
    
    ...

def get_control_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetControlResult]:
    
    ...

