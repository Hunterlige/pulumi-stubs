import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetPlanResult", "AwaitableGetPlanResult", "get_plan", "get_plan_output"]

@pulumi.output_type
class GetPlanResult:
    def __init__(__self__, contact_id=..., id=..., region=..., stages=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def stages(self) -> Sequence[outputs.GetPlanStageResult]: ...

class AwaitableGetPlanResult(GetPlanResult):
    def __await__(self): ...

def get_plan(
    contact_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPlanResult: ...
def get_plan_output(
    contact_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPlanResult]: ...
