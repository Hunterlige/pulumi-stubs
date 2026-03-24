import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGroupsResult",
    "AwaitableGetGroupsResult",
    "get_groups",
    "get_groups_output",
]

@pulumi.output_type
class GetGroupsResult:
    def __init__(__self__, groups=..., id=..., parent=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Sequence[outputs.GetGroupsGroupResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str: ...

class AwaitableGetGroupsResult(GetGroupsResult):
    def __await__(self): ...

def get_groups(
    parent: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetGroupsResult: ...
def get_groups_output(
    parent: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGroupsResult]: ...
