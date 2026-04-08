import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualHubRouteTableV2Result",
    "AwaitableGetVirtualHubRouteTableV2Result",
    "get_virtual_hub_route_table_v2",
    "get_virtual_hub_route_table_v2_output",
]

@pulumi.output_type
class GetVirtualHubRouteTableV2Result:
    def __init__(
        __self__,
        attached_connections=...,
        azure_api_version=...,
        etag=...,
        id=...,
        name=...,
        provisioning_state=...,
        routes=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachedConnections")
    def attached_connections(self) -> Optional[Sequence[_builtins.str]]: ...
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
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[Sequence[outputs.VirtualHubRouteV2Response]]: ...

class AwaitableGetVirtualHubRouteTableV2Result(GetVirtualHubRouteTableV2Result):
    def __await__(self): ...

def get_virtual_hub_route_table_v2(
    resource_group_name: Optional[_builtins.str] = ...,
    route_table_name: Optional[_builtins.str] = ...,
    virtual_hub_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualHubRouteTableV2Result: ...
def get_virtual_hub_route_table_v2_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    route_table_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualHubRouteTableV2Result]: ...
