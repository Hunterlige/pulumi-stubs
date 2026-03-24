import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetParameterResult",
    "AwaitableGetParameterResult",
    "get_parameter",
    "get_parameter_output",
]

@pulumi.output_type
class GetParameterResult:
    def __init__(
        __self__,
        arn=...,
        id=...,
        insecure_value=...,
        name=...,
        region=...,
        type=...,
        value=...,
        version=...,
        with_decryption=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="insecureValue")
    def insecure_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="withDecryption")
    def with_decryption(self) -> Optional[_builtins.bool]: ...

class AwaitableGetParameterResult(GetParameterResult):
    def __await__(self): ...

def get_parameter(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    with_decryption: Optional[_builtins.bool] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetParameterResult: ...
def get_parameter_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    with_decryption: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetParameterResult]: ...
