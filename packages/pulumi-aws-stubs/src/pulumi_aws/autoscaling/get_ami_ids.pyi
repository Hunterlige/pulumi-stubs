import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAmiIdsResult",
    "AwaitableGetAmiIdsResult",
    "get_ami_ids",
    "get_ami_ids_output",
]

@pulumi.output_type
class GetAmiIdsResult:
    def __init__(
        __self__, arns=..., filters=..., id=..., names=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetAmiIdsFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetAmiIdsResult(GetAmiIdsResult):
    def __await__(self): ...

def get_ami_ids(
    filters: Optional[
        Sequence[Union[GetAmiIdsFilterArgs, GetAmiIdsFilterArgsDict]]
    ] = ...,
    names: Optional[Sequence[_builtins.str]] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAmiIdsResult: ...
def get_ami_ids_output(
    filters: Optional[
        pulumi.Input[
            Optional[Sequence[Union[GetAmiIdsFilterArgs, GetAmiIdsFilterArgsDict]]]
        ]
    ] = ...,
    names: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAmiIdsResult]: ...
