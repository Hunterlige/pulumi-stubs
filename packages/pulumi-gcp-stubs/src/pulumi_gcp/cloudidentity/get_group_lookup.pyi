import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGroupLookupResult",
    "AwaitableGetGroupLookupResult",
    "get_group_lookup",
    "get_group_lookup_output",
]

@pulumi.output_type
class GetGroupLookupResult:
    def __init__(__self__, group_key=..., id=..., name=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> outputs.GetGroupLookupGroupKeyResult: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

class AwaitableGetGroupLookupResult(GetGroupLookupResult):
    def __await__(self): ...

def get_group_lookup(
    group_key: Optional[
        Union[GetGroupLookupGroupKeyArgs, GetGroupLookupGroupKeyArgsDict]
    ] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGroupLookupResult: ...
def get_group_lookup_output(
    group_key: Optional[
        pulumi.Input[Union[GetGroupLookupGroupKeyArgs, GetGroupLookupGroupKeyArgsDict]]
    ] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGroupLookupResult]: ...
