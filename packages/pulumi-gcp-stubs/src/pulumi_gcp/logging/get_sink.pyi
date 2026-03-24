import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetSinkResult", "AwaitableGetSinkResult", "get_sink", "get_sink_output"]

@pulumi.output_type
class GetSinkResult:
    def __init__(
        __self__,
        bigquery_options=...,
        description=...,
        destination=...,
        disabled=...,
        exclusions=...,
        filter=...,
        id=...,
        name=...,
        writer_identity=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(self) -> Sequence[outputs.GetSinkBigqueryOptionResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Sequence[outputs.GetSinkExclusionResult]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> _builtins.str: ...

class AwaitableGetSinkResult(GetSinkResult):
    def __await__(self): ...

def get_sink(
    id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetSinkResult: ...
def get_sink_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSinkResult]: ...
