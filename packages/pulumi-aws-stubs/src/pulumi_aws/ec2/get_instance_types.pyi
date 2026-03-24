import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstanceTypesResult",
    "AwaitableGetInstanceTypesResult",
    "get_instance_types",
    "get_instance_types_output",
]

@pulumi.output_type
class GetInstanceTypesResult:
    def __init__(
        __self__, filters=..., id=..., instance_types=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetInstanceTypesFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetInstanceTypesResult(GetInstanceTypesResult):
    def __await__(self): ...

def get_instance_types(
    filters: Optional[
        Sequence[Union[GetInstanceTypesFilterArgs, GetInstanceTypesFilterArgsDict]]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstanceTypesResult: ...
def get_instance_types_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[GetInstanceTypesFilterArgs, GetInstanceTypesFilterArgsDict]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstanceTypesResult]: ...
