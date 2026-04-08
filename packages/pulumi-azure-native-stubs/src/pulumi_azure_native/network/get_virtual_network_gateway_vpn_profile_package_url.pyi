import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetVirtualNetworkGatewayVpnProfilePackageUrlResult", ..., ..., ...]

@pulumi.output_type
class GetVirtualNetworkGatewayVpnProfilePackageUrlResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

class AwaitableGetVirtualNetworkGatewayVpnProfilePackageUrlResult(
    GetVirtualNetworkGatewayVpnProfilePackageUrlResult
):
    def __await__(self): ...

def get_virtual_network_gateway_vpn_profile_package_url(
    resource_group_name: Optional[_builtins.str] = ...,
    virtual_network_gateway_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualNetworkGatewayVpnProfilePackageUrlResult: ...
def get_virtual_network_gateway_vpn_profile_package_url_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_network_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualNetworkGatewayVpnProfilePackageUrlResult]: ...
