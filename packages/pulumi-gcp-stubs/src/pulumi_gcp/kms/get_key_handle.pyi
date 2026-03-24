import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKeyHandleResult",
    "AwaitableGetKeyHandleResult",
    "get_key_handle",
    "get_key_handle_output",
]

@pulumi.output_type
class GetKeyHandleResult:
    def __init__(
        __self__,
        id=...,
        kms_key=...,
        location=...,
        name=...,
        project=...,
        resource_type_selector=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeSelector")
    def resource_type_selector(self) -> _builtins.str: ...

class AwaitableGetKeyHandleResult(GetKeyHandleResult):
    def __await__(self): ...

def get_key_handle(
    location: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKeyHandleResult: ...
def get_key_handle_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKeyHandleResult]: ...
