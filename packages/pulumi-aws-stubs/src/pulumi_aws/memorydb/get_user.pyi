import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetUserResult", "AwaitableGetUserResult", "get_user", "get_user_output"]

@pulumi.output_type
class GetUserResult:
    def __init__(
        __self__,
        access_string=...,
        arn=...,
        authentication_modes=...,
        id=...,
        minimum_engine_version=...,
        region=...,
        tags=...,
        user_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessString")
    def access_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationModes")
    def authentication_modes(
        self,
    ) -> Sequence[outputs.GetUserAuthenticationModeResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimumEngineVersion")
    def minimum_engine_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str: ...

class AwaitableGetUserResult(GetUserResult):
    def __await__(self): ...

def get_user(
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    user_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetUserResult: ...
def get_user_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    user_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetUserResult]: ...
