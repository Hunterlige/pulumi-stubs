import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstancesResult",
    "AwaitableGetInstancesResult",
    "get_instances",
    "get_instances_output",
]

@pulumi.output_type
class GetInstancesResult:
    def __init__(
        __self__,
        filters=...,
        id=...,
        instance_arns=...,
        instance_identifiers=...,
        region=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetInstancesFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceArns")
    def instance_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceIdentifiers")
    def instance_identifiers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetInstancesResult(GetInstancesResult):
    def __await__(self): ...

def get_instances(
    filters: Optional[
        Sequence[Union[GetInstancesFilterArgs, GetInstancesFilterArgsDict]]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstancesResult: ...
def get_instances_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[Union[GetInstancesFilterArgs, GetInstancesFilterArgsDict]]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstancesResult]: ...
