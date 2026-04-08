import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualNetworkGatewayAdvertisedRoutesResult",
    ...,
    "get_virtual_network_gateway_advertised_routes",
    ...,
]

@pulumi.output_type
class GetVirtualNetworkGatewayAdvertisedRoutesResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.GatewayRouteResponse]]: ...

class AwaitableGetVirtualNetworkGatewayAdvertisedRoutesResult(
    GetVirtualNetworkGatewayAdvertisedRoutesResult
):
    def __await__(self): ...

def get_virtual_network_gateway_advertised_routes(
    peer: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    virtual_network_gateway_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualNetworkGatewayAdvertisedRoutesResult: ...
def get_virtual_network_gateway_advertised_routes_output(
    peer: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_network_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualNetworkGatewayAdvertisedRoutesResult]: ...
