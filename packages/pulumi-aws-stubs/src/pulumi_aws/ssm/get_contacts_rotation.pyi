import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetContactsRotationResult",
    "AwaitableGetContactsRotationResult",
    "get_contacts_rotation",
    "get_contacts_rotation_output",
]

@pulumi.output_type
class GetContactsRotationResult:
    def __init__(
        __self__,
        arn=...,
        contact_ids=...,
        id=...,
        name=...,
        recurrences=...,
        region=...,
        start_time=...,
        tags=...,
        time_zone_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contactIds")
    def contact_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def recurrences(self) -> Sequence[outputs.GetContactsRotationRecurrenceResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> _builtins.str: ...

class AwaitableGetContactsRotationResult(GetContactsRotationResult):
    def __await__(self): ...

def get_contacts_rotation(
    arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetContactsRotationResult: ...
def get_contacts_rotation_output(
    arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetContactsRotationResult]: ...
