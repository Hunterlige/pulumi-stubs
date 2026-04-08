import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServerKeyResult",
    "AwaitableGetServerKeyResult",
    "get_server_key",
    "get_server_key_output",
]

@pulumi.output_type
class GetServerKeyResult:
    def __init__(
        __self__,
        auto_rotation_enabled=...,
        azure_api_version=...,
        creation_date=...,
        id=...,
        kind=...,
        location=...,
        name=...,
        subregion=...,
        thumbprint=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoRotationEnabled")
    def auto_rotation_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subregion(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetServerKeyResult(GetServerKeyResult):
    def __await__(self): ...

def get_server_key(
    key_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServerKeyResult: ...
def get_server_key_output(
    key_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServerKeyResult]: ...
