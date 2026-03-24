import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "RouterStatusResult",
    "AwaitableRouterStatusResult",
    "router_status",
    "router_status_output",
]

@pulumi.output_type
class RouterStatusResult:
    def __init__(
        __self__,
        best_routes=...,
        best_routes_for_routers=...,
        id=...,
        name=...,
        network=...,
        project=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bestRoutes")
    def best_routes(self) -> Sequence[outputs.RouterStatusBestRouteResult]: ...
    @_builtins.property
    @pulumi.getter(name="bestRoutesForRouters")
    def best_routes_for_routers(
        self,
    ) -> Sequence[outputs.RouterStatusBestRoutesForRouterResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableRouterStatusResult(RouterStatusResult):
    def __await__(self): ...

def router_status(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableRouterStatusResult: ...
def router_status_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[RouterStatusResult]: ...
