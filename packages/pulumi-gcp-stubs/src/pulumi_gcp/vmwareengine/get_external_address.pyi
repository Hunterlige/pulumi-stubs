import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetExternalAddressResult",
    "AwaitableGetExternalAddressResult",
    "get_external_address",
    "get_external_address_output",
]

@pulumi.output_type
class GetExternalAddressResult:
    def __init__(
        __self__,
        create_time=...,
        description=...,
        external_ip=...,
        id=...,
        internal_ip=...,
        name=...,
        parent=...,
        state=...,
        uid=...,
        update_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="externalIp")
    def external_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...

class AwaitableGetExternalAddressResult(GetExternalAddressResult):
    def __await__(self): ...

def get_external_address(
    name: Optional[_builtins.str] = ...,
    parent: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetExternalAddressResult: ...
def get_external_address_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    parent: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetExternalAddressResult]: ...
