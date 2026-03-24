import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRouteTablePropagationsResult",
    "AwaitableGetRouteTablePropagationsResult",
    "get_route_table_propagations",
    "get_route_table_propagations_output",
]

@pulumi.output_type
class GetRouteTablePropagationsResult:
    def __init__(
        __self__,
        filters=...,
        id=...,
        ids=...,
        region=...,
        transit_gateway_route_table_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetRouteTablePropagationsFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> _builtins.str: ...

class AwaitableGetRouteTablePropagationsResult(GetRouteTablePropagationsResult):
    def __await__(self): ...

def get_route_table_propagations(
    filters: Optional[
        Sequence[
            Union[
                GetRouteTablePropagationsFilterArgs,
                GetRouteTablePropagationsFilterArgsDict,
            ]
        ]
    ] = ...,
    region: Optional[_builtins.str] = ...,
    transit_gateway_route_table_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRouteTablePropagationsResult: ...
def get_route_table_propagations_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetRouteTablePropagationsFilterArgs,
                        GetRouteTablePropagationsFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    transit_gateway_route_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRouteTablePropagationsResult]: ...
