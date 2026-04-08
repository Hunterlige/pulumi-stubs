import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIPv6FirewallRuleResult",
    "AwaitableGetIPv6FirewallRuleResult",
    "get_i_pv6_firewall_rule",
    "get_i_pv6_firewall_rule_output",
]

@pulumi.output_type
class GetIPv6FirewallRuleResult:
    def __init__(
        __self__,
        azure_api_version=...,
        end_i_pv6_address=...,
        id=...,
        name=...,
        start_i_pv6_address=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endIPv6Address")
    def end_i_pv6_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startIPv6Address")
    def start_i_pv6_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetIPv6FirewallRuleResult(GetIPv6FirewallRuleResult):
    def __await__(self): ...

def get_i_pv6_firewall_rule(
    firewall_rule_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIPv6FirewallRuleResult: ...
def get_i_pv6_firewall_rule_output(
    firewall_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIPv6FirewallRuleResult]: ...
