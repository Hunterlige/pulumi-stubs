import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstanceProfileResult",
    "AwaitableGetInstanceProfileResult",
    "get_instance_profile",
    "get_instance_profile_output",
]

@pulumi.output_type
class GetInstanceProfileResult:
    def __init__(
        __self__,
        arn=...,
        create_date=...,
        id=...,
        name=...,
        path=...,
        role_arn=...,
        role_id=...,
        role_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createDate")
    def create_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleId")
    def role_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> _builtins.str: ...

class AwaitableGetInstanceProfileResult(GetInstanceProfileResult):
    def __await__(self): ...

def get_instance_profile(
    name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetInstanceProfileResult: ...
def get_instance_profile_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstanceProfileResult]: ...
