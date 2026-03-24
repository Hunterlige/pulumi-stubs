import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFunctionResult",
    "AwaitableGetFunctionResult",
    "get_function",
    "get_function_output",
]

@pulumi.output_type
class GetFunctionResult:
    def __init__(
        __self__,
        arn=...,
        code=...,
        comment=...,
        etag=...,
        id=...,
        key_value_store_associations=...,
        last_modified_time=...,
        name=...,
        runtime=...,
        stage=...,
        status=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyValueStoreAssociations")
    def key_value_store_associations(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

class AwaitableGetFunctionResult(GetFunctionResult):
    def __await__(self): ...

def get_function(
    name: Optional[_builtins.str] = ...,
    stage: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFunctionResult: ...
def get_function_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    stage: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFunctionResult]: ...
