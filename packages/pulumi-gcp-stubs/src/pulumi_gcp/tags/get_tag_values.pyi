import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTagValuesResult",
    "AwaitableGetTagValuesResult",
    "get_tag_values",
    "get_tag_values_output",
]

@pulumi.output_type
class GetTagValuesResult:
    def __init__(__self__, id=..., parent=..., values=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[outputs.GetTagValuesValueResult]: ...

class AwaitableGetTagValuesResult(GetTagValuesResult):
    def __await__(self): ...

def get_tag_values(
    parent: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetTagValuesResult: ...
def get_tag_values_output(
    parent: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTagValuesResult]: ...
