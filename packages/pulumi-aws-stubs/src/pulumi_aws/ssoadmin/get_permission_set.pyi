import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPermissionSetResult",
    "AwaitableGetPermissionSetResult",
    "get_permission_set",
    "get_permission_set_output",
]

@pulumi.output_type
class GetPermissionSetResult:
    def __init__(
        __self__,
        arn=...,
        created_date=...,
        description=...,
        id=...,
        instance_arn=...,
        name=...,
        region=...,
        relay_state=...,
        session_duration=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="relayState")
    def relay_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionDuration")
    def session_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetPermissionSetResult(GetPermissionSetResult):
    def __await__(self): ...

def get_permission_set(
    arn: Optional[_builtins.str] = ...,
    instance_arn: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPermissionSetResult: ...
def get_permission_set_output(
    arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPermissionSetResult]: ...
