import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetRoleResult", "AwaitableGetRoleResult", "get_role", "get_role_output"]

@pulumi.output_type
class GetRoleResult:
    def __init__(
        __self__,
        arn=...,
        assume_role_policy=...,
        create_date=...,
        description=...,
        id=...,
        max_session_duration=...,
        name=...,
        path=...,
        permissions_boundary=...,
        role_last_useds=...,
        tags=...,
        unique_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="assumeRolePolicy")
    def assume_role_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createDate")
    def create_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxSessionDuration")
    def max_session_duration(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleLastUseds")
    def role_last_useds(self) -> Sequence[outputs.GetRoleRoleLastUsedResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> _builtins.str: ...

class AwaitableGetRoleResult(GetRoleResult):
    def __await__(self): ...

def get_role(
    name: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRoleResult: ...
def get_role_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRoleResult]: ...
