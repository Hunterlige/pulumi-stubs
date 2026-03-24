import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetHcVpnGatewayResult",
    "AwaitableGetHcVpnGatewayResult",
    "get_hc_vpn_gateway",
    "get_hc_vpn_gateway_output",
]

@pulumi.output_type
class GetHcVpnGatewayResult:
    def __init__(
        __self__,
        description=...,
        effective_labels=...,
        gateway_ip_version=...,
        id=...,
        label_fingerprint=...,
        labels=...,
        name=...,
        network=...,
        params=...,
        project=...,
        pulumi_labels=...,
        region=...,
        self_link=...,
        stack_type=...,
        vpn_interfaces=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gatewayIpVersion")
    def gateway_ip_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Sequence[outputs.GetHcVpnGatewayParamResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stackType")
    def stack_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpnInterfaces")
    def vpn_interfaces(self) -> Sequence[outputs.GetHcVpnGatewayVpnInterfaceResult]: ...

class AwaitableGetHcVpnGatewayResult(GetHcVpnGatewayResult):
    def __await__(self): ...

def get_hc_vpn_gateway(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetHcVpnGatewayResult: ...
def get_hc_vpn_gateway_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetHcVpnGatewayResult]: ...
