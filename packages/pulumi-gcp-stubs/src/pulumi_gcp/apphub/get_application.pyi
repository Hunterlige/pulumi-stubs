import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApplicationResult",
    "AwaitableGetApplicationResult",
    "get_application",
    "get_application_output",
]

@pulumi.output_type
class GetApplicationResult:
    def __init__(
        __self__,
        application_id=...,
        attributes=...,
        create_time=...,
        description=...,
        display_name=...,
        id=...,
        location=...,
        name=...,
        project=...,
        scopes=...,
        state=...,
        uid=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Sequence[outputs.GetApplicationAttributeResult]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Sequence[outputs.GetApplicationScopeResult]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetApplicationResult(GetApplicationResult):
    def __await__(self): ...

def get_application(
    application_id: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApplicationResult: ...
def get_application_output(
    application_id: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApplicationResult]: ...
