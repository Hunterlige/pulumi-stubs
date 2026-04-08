import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetHubRouteTableResult",
    "AwaitableGetHubRouteTableResult",
    "get_hub_route_table",
    "get_hub_route_table_output",
]

@pulumi.output_type
class GetHubRouteTableResult:
    def __init__(
        __self__,
        associated_connections=...,
        azure_api_version=...,
        etag=...,
        id=...,
        labels=...,
        name=...,
        propagating_connections=...,
        provisioning_state=...,
        routes=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="associatedConnections")
    def associated_connections(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propagatingConnections")
    def propagating_connections(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[Sequence[outputs.HubRouteResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetHubRouteTableResult(GetHubRouteTableResult):
    def __await__(self): ...

def get_hub_route_table(
    resource_group_name: Optional[_builtins.str] = ...,
    route_table_name: Optional[_builtins.str] = ...,
    virtual_hub_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetHubRouteTableResult: ...
def get_hub_route_table_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    route_table_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetHubRouteTableResult]: ...
