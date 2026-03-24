import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIpSetResult",
    "AwaitableGetIpSetResult",
    "get_ip_set",
    "get_ip_set_output",
]

@pulumi.output_type
class GetIpSetResult:
    def __init__(
        __self__,
        addresses=...,
        arn=...,
        description=...,
        id=...,
        ip_address_version=...,
        name=...,
        region=...,
        scope=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressVersion")
    def ip_address_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...

class AwaitableGetIpSetResult(GetIpSetResult):
    def __await__(self): ...

def get_ip_set(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIpSetResult: ...
def get_ip_set_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIpSetResult]: ...
