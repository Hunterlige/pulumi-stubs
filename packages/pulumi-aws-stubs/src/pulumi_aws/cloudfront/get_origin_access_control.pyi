import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOriginAccessControlResult",
    "AwaitableGetOriginAccessControlResult",
    "get_origin_access_control",
    "get_origin_access_control_output",
]

@pulumi.output_type
class GetOriginAccessControlResult:
    def __init__(
        __self__,
        arn=...,
        description=...,
        etag=...,
        id=...,
        name=...,
        origin_access_control_origin_type=...,
        signing_behavior=...,
        signing_protocol=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="originAccessControlOriginType")
    def origin_access_control_origin_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signingBehavior")
    def signing_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signingProtocol")
    def signing_protocol(self) -> _builtins.str: ...

class AwaitableGetOriginAccessControlResult(GetOriginAccessControlResult):
    def __await__(self): ...

def get_origin_access_control(
    id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetOriginAccessControlResult: ...
def get_origin_access_control_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOriginAccessControlResult]: ...
