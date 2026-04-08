import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [..., ..., ..., ...]

@pulumi.output_type
class GetVirtualNetworkGatewayVpnclientConnectionHealthResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[Sequence[outputs.VpnClientConnectionHealthDetailResponse]]: ...

class AwaitableGetVirtualNetworkGatewayVpnclientConnectionHealthResult(
    GetVirtualNetworkGatewayVpnclientConnectionHealthResult
):
    def __await__(self): ...

def get_virtual_network_gateway_vpnclient_connection_health(
    resource_group_name: Optional[_builtins.str] = ...,
    virtual_network_gateway_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualNetworkGatewayVpnclientConnectionHealthResult: ...
def get_virtual_network_gateway_vpnclient_connection_health_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_network_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualNetworkGatewayVpnclientConnectionHealthResult]: ...
