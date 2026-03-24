import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLocalGatewayRouteTableResult",
    "AwaitableGetLocalGatewayRouteTableResult",
    "get_local_gateway_route_table",
    "get_local_gateway_route_table_output",
]

@pulumi.output_type
class GetLocalGatewayRouteTableResult:
    def __init__(
        __self__,
        filters=...,
        id=...,
        local_gateway_id=...,
        local_gateway_route_table_id=...,
        outpost_arn=...,
        region=...,
        state=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetLocalGatewayRouteTableFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localGatewayId")
    def local_gateway_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localGatewayRouteTableId")
    def local_gateway_route_table_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetLocalGatewayRouteTableResult(GetLocalGatewayRouteTableResult):
    def __await__(self): ...

def get_local_gateway_route_table(
    filters: Optional[
        Sequence[
            Union[
                GetLocalGatewayRouteTableFilterArgs,
                GetLocalGatewayRouteTableFilterArgsDict,
            ]
        ]
    ] = ...,
    local_gateway_id: Optional[_builtins.str] = ...,
    local_gateway_route_table_id: Optional[_builtins.str] = ...,
    outpost_arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    state: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLocalGatewayRouteTableResult: ...
def get_local_gateway_route_table_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetLocalGatewayRouteTableFilterArgs,
                        GetLocalGatewayRouteTableFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    local_gateway_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    local_gateway_route_table_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    outpost_arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    state: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLocalGatewayRouteTableResult]: ...
