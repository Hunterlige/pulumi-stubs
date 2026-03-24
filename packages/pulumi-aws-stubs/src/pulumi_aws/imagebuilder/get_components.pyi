import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetComponentsResult",
    "AwaitableGetComponentsResult",
    "get_components",
    "get_components_output",
]

@pulumi.output_type
class GetComponentsResult:
    def __init__(
        __self__, arns=..., filters=..., id=..., names=..., owner=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetComponentsFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetComponentsResult(GetComponentsResult):
    def __await__(self): ...

def get_components(
    filters: Optional[
        Sequence[Union[GetComponentsFilterArgs, GetComponentsFilterArgsDict]]
    ] = ...,
    owner: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetComponentsResult: ...
def get_components_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[Union[GetComponentsFilterArgs, GetComponentsFilterArgsDict]]
            ]
        ]
    ] = ...,
    owner: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetComponentsResult]: ...
