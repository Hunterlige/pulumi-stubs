import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [..., ..., ..., ...]

@pulumi.output_type
class GetVirtualNetworkGatewayVpnclientIpsecParametersResult:
    def __init__(
        __self__,
        dh_group=...,
        ike_encryption=...,
        ike_integrity=...,
        ipsec_encryption=...,
        ipsec_integrity=...,
        pfs_group=...,
        sa_data_size_kilobytes=...,
        sa_life_time_seconds=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dhGroup")
    def dh_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ikeEncryption")
    def ike_encryption(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ikeIntegrity")
    def ike_integrity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipsecEncryption")
    def ipsec_encryption(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipsecIntegrity")
    def ipsec_integrity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pfsGroup")
    def pfs_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="saDataSizeKilobytes")
    def sa_data_size_kilobytes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="saLifeTimeSeconds")
    def sa_life_time_seconds(self) -> _builtins.int: ...

class AwaitableGetVirtualNetworkGatewayVpnclientIpsecParametersResult(
    GetVirtualNetworkGatewayVpnclientIpsecParametersResult
):
    def __await__(self): ...

def get_virtual_network_gateway_vpnclient_ipsec_parameters(
    resource_group_name: Optional[_builtins.str] = ...,
    virtual_network_gateway_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualNetworkGatewayVpnclientIpsecParametersResult: ...
def get_virtual_network_gateway_vpnclient_ipsec_parameters_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_network_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualNetworkGatewayVpnclientIpsecParametersResult]: ...
