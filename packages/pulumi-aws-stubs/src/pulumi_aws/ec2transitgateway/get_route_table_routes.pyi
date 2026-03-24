import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRouteTableRoutesResult",
    "AwaitableGetRouteTableRoutesResult",
    "get_route_table_routes",
    "get_route_table_routes_output",
]

@pulumi.output_type
class GetRouteTableRoutesResult:
    def __init__(
        __self__,
        filters=...,
        id=...,
        region=...,
        routes=...,
        transit_gateway_route_table_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Sequence[outputs.GetRouteTableRoutesFilterResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Sequence[outputs.GetRouteTableRoutesRouteResult]: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> _builtins.str: ...

class AwaitableGetRouteTableRoutesResult(GetRouteTableRoutesResult):
    def __await__(self): ...

def get_route_table_routes(
    filters: Optional[
        Sequence[
            Union[GetRouteTableRoutesFilterArgs, GetRouteTableRoutesFilterArgsDict]
        ]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    transit_gateway_route_table_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRouteTableRoutesResult: ...
def get_route_table_routes_output(
    filters: Optional[
        pulumi.Input[
            Sequence[
                Union[GetRouteTableRoutesFilterArgs, GetRouteTableRoutesFilterArgsDict]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    transit_gateway_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRouteTableRoutesResult]: ...
