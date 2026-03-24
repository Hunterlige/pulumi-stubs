import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRouteTableResult",
    "AwaitableGetRouteTableResult",
    "get_route_table",
    "get_route_table_output",
]

@pulumi.output_type
class GetRouteTableResult:
    def __init__(
        __self__,
        arn=...,
        default_association_route_table=...,
        default_propagation_route_table=...,
        filters=...,
        id=...,
        region=...,
        tags=...,
        transit_gateway_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultAssociationRouteTable")
    def default_association_route_table(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="defaultPropagationRouteTable")
    def default_propagation_route_table(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetRouteTableFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> _builtins.str: ...

class AwaitableGetRouteTableResult(GetRouteTableResult):
    def __await__(self): ...

def get_route_table(
    filters: Optional[
        Sequence[Union[GetRouteTableFilterArgs, GetRouteTableFilterArgsDict]]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRouteTableResult: ...
def get_route_table_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[Union[GetRouteTableFilterArgs, GetRouteTableFilterArgsDict]]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRouteTableResult]: ...
