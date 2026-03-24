import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectionResult",
    "AwaitableGetConnectionResult",
    "get_connection",
    "get_connection_output",
]

@pulumi.output_type
class GetConnectionResult:
    def __init__(
        __self__,
        arn=...,
        athena_properties=...,
        catalog_id=...,
        connection_properties=...,
        connection_type=...,
        description=...,
        id=...,
        match_criterias=...,
        name=...,
        physical_connection_requirements=...,
        region=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="athenaProperties")
    def athena_properties(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionProperties")
    def connection_properties(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchCriterias")
    def match_criterias(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="physicalConnectionRequirements")
    def physical_connection_requirements(
        self,
    ) -> Sequence[outputs.GetConnectionPhysicalConnectionRequirementResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetConnectionResult(GetConnectionResult):
    def __await__(self): ...

def get_connection(
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConnectionResult: ...
def get_connection_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConnectionResult]: ...
