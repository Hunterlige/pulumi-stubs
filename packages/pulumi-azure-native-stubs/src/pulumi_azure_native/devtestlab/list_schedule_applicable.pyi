import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListScheduleApplicableResult",
    "AwaitableListScheduleApplicableResult",
    "list_schedule_applicable",
    "list_schedule_applicable_output",
]

@pulumi.output_type
class ListScheduleApplicableResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.ScheduleResponse]: ...

class AwaitableListScheduleApplicableResult(ListScheduleApplicableResult):
    def __await__(self): ...

def list_schedule_applicable(
    lab_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListScheduleApplicableResult: ...
def list_schedule_applicable_output(
    lab_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListScheduleApplicableResult]: ...
