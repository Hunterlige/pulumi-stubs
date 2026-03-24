import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetSResult", "AwaitableGetSResult", "get_s", "get_s_output"]

@pulumi.output_type
class GetSResult:
    def __init__(
        __self__, accounts=..., id=..., prefix=..., project=..., regex=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accounts(self) -> Sequence[outputs.GetSAccountResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]: ...

class AwaitableGetSResult(GetSResult):
    def __await__(self): ...

def get_s(
    prefix: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    regex: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSResult: ...
def get_s_output(
    prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    regex: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSResult]: ...
