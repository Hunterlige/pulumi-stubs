import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetP2sVpnServerConfigurationResult",
    "AwaitableGetP2sVpnServerConfigurationResult",
    "get_p2s_vpn_server_configuration",
    "get_p2s_vpn_server_configuration_output",
]

@pulumi.output_type
class GetP2sVpnServerConfigurationResult:
    def __init__(
        __self__, azure_api_version=..., etag=..., id=..., name=..., properties=...
    ) -> None: ...
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
    @pulumi.getter
    def properties(self) -> outputs.P2SVpnServerConfigurationPropertiesResponse: ...

class AwaitableGetP2sVpnServerConfigurationResult(GetP2sVpnServerConfigurationResult):
    def __await__(self): ...

def get_p2s_vpn_server_configuration(
    p2_s_vpn_server_configuration_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    virtual_wan_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetP2sVpnServerConfigurationResult: ...
def get_p2s_vpn_server_configuration_output(
    p2_s_vpn_server_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_wan_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetP2sVpnServerConfigurationResult]: ...
