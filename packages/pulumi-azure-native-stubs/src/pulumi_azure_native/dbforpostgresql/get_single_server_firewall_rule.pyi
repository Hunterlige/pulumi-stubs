import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSingleServerFirewallRuleResult",
    "AwaitableGetSingleServerFirewallRuleResult",
    "get_single_server_firewall_rule",
    "get_single_server_firewall_rule_output",
]

@pulumi.output_type
class GetSingleServerFirewallRuleResult:
    def __init__(
        __self__,
        azure_api_version=...,
        end_ip_address=...,
        id=...,
        name=...,
        start_ip_address=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSingleServerFirewallRuleResult(GetSingleServerFirewallRuleResult):
    def __await__(self): ...

def get_single_server_firewall_rule(
    firewall_rule_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSingleServerFirewallRuleResult: ...
def get_single_server_firewall_rule_output(
    firewall_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSingleServerFirewallRuleResult]: ...
