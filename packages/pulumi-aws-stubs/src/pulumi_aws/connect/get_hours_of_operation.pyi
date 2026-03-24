import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetHoursOfOperationResult",
    "AwaitableGetHoursOfOperationResult",
    "get_hours_of_operation",
    "get_hours_of_operation_output",
]

@pulumi.output_type
class GetHoursOfOperationResult:
    def __init__(
        __self__,
        arn=...,
        configs=...,
        description=...,
        hours_of_operation_id=...,
        id=...,
        instance_id=...,
        name=...,
        region=...,
        tags=...,
        time_zone=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def configs(self) -> Sequence[outputs.GetHoursOfOperationConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hoursOfOperationId")
    def hours_of_operation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str: ...

class AwaitableGetHoursOfOperationResult(GetHoursOfOperationResult):
    def __await__(self): ...

def get_hours_of_operation(
    hours_of_operation_id: Optional[_builtins.str] = ...,
    instance_id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetHoursOfOperationResult: ...
def get_hours_of_operation_output(
    hours_of_operation_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetHoursOfOperationResult]: ...
