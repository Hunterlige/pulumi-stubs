import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIpFirewallRuleResult",
    "AwaitableGetIpFirewallRuleResult",
    "get_ip_firewall_rule",
    "get_ip_firewall_rule_output",
]

@pulumi.output_type
class GetIpFirewallRuleResult:
    def __init__(
        __self__,
        azure_api_version=...,
        end_ip_address=...,
        id=...,
        name=...,
        provisioning_state=...,
        start_ip_address=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetIpFirewallRuleResult(GetIpFirewallRuleResult):
    def __await__(self): ...

def get_ip_firewall_rule(
    resource_group_name: Optional[_builtins.str] = ...,
    rule_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIpFirewallRuleResult: ...
def get_ip_firewall_rule_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIpFirewallRuleResult]: ...
