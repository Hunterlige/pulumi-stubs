import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetParametersByPathResult",
    "AwaitableGetParametersByPathResult",
    "get_parameters_by_path",
    "get_parameters_by_path_output",
]

@pulumi.output_type
class GetParametersByPathResult:
    def __init__(
        __self__,
        arns=...,
        id=...,
        names=...,
        path=...,
        recursive=...,
        region=...,
        types=...,
        values=...,
        with_decryption=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def recursive(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="withDecryption")
    def with_decryption(self) -> Optional[_builtins.bool]: ...

class AwaitableGetParametersByPathResult(GetParametersByPathResult):
    def __await__(self): ...

def get_parameters_by_path(
    path: Optional[_builtins.str] = ...,
    recursive: Optional[_builtins.bool] = ...,
    region: Optional[_builtins.str] = ...,
    with_decryption: Optional[_builtins.bool] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetParametersByPathResult: ...
def get_parameters_by_path_output(
    path: Optional[pulumi.Input[_builtins.str]] = ...,
    recursive: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    with_decryption: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetParametersByPathResult]: ...
