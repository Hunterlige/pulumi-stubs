import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGatewayRouteResult",
    "AwaitableGetGatewayRouteResult",
    "get_gateway_route",
    "get_gateway_route_output",
]

@pulumi.output_type
class GetGatewayRouteResult:
    def __init__(
        __self__,
        arn=...,
        created_date=...,
        id=...,
        last_updated_date=...,
        mesh_name=...,
        mesh_owner=...,
        name=...,
        region=...,
        resource_owner=...,
        specs=...,
        tags=...,
        virtual_gateway_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="meshName")
    def mesh_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="meshOwner")
    def mesh_owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceOwner")
    def resource_owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def specs(self) -> Sequence[outputs.GetGatewayRouteSpecResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualGatewayName")
    def virtual_gateway_name(self) -> _builtins.str: ...

class AwaitableGetGatewayRouteResult(GetGatewayRouteResult):
    def __await__(self): ...

def get_gateway_route(
    mesh_name: Optional[_builtins.str] = ...,
    mesh_owner: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    virtual_gateway_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGatewayRouteResult: ...
def get_gateway_route_output(
    mesh_name: Optional[pulumi.Input[_builtins.str]] = ...,
    mesh_owner: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    virtual_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGatewayRouteResult]: ...
