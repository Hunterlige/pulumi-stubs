import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualNetworkGatewayNatRuleResult",
    "AwaitableGetVirtualNetworkGatewayNatRuleResult",
    "get_virtual_network_gateway_nat_rule",
    "get_virtual_network_gateway_nat_rule_output",
]

@pulumi.output_type
class GetVirtualNetworkGatewayNatRuleResult:
    def __init__(
        __self__,
        azure_api_version=...,
        etag=...,
        external_mappings=...,
        id=...,
        internal_mappings=...,
        ip_configuration_id=...,
        mode=...,
        name=...,
        provisioning_state=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="externalMappings")
    def external_mappings(
        self,
    ) -> Optional[Sequence[outputs.VpnNatRuleMappingResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="internalMappings")
    def internal_mappings(
        self,
    ) -> Optional[Sequence[outputs.VpnNatRuleMappingResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="ipConfigurationId")
    def ip_configuration_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetVirtualNetworkGatewayNatRuleResult(
    GetVirtualNetworkGatewayNatRuleResult
):
    def __await__(self): ...

def get_virtual_network_gateway_nat_rule(
    nat_rule_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    virtual_network_gateway_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualNetworkGatewayNatRuleResult: ...
def get_virtual_network_gateway_nat_rule_output(
    nat_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    virtual_network_gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualNetworkGatewayNatRuleResult]: ...
