import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRuntimeVersionResult",
    "AwaitableGetRuntimeVersionResult",
    "get_runtime_version",
    "get_runtime_version_output",
]

@pulumi.output_type
class GetRuntimeVersionResult:
    def __init__(
        __self__,
        deprecation_date=...,
        description=...,
        id=...,
        latest=...,
        prefix=...,
        region=...,
        release_date=...,
        version=...,
        version_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deprecationDate")
    def deprecation_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def latest(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="releaseDate")
    def release_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> _builtins.str: ...

class AwaitableGetRuntimeVersionResult(GetRuntimeVersionResult):
    def __await__(self): ...

def get_runtime_version(
    latest: Optional[_builtins.bool] = ...,
    prefix: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    version: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRuntimeVersionResult: ...
def get_runtime_version_output(
    latest: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRuntimeVersionResult]: ...
