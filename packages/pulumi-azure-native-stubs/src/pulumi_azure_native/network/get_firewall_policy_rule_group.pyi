import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFirewallPolicyRuleGroupResult",
    "AwaitableGetFirewallPolicyRuleGroupResult",
    "get_firewall_policy_rule_group",
    "get_firewall_policy_rule_group_output",
]

@pulumi.output_type
class GetFirewallPolicyRuleGroupResult:
    def __init__(
        __self__,
        azure_api_version=...,
        etag=...,
        id=...,
        name=...,
        priority=...,
        provisioning_state=...,
        rules=...,
        type=...,
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
    def priority(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetFirewallPolicyRuleGroupResult(GetFirewallPolicyRuleGroupResult):
    def __await__(self): ...

def get_firewall_policy_rule_group(
    firewall_policy_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    rule_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFirewallPolicyRuleGroupResult: ...
def get_firewall_policy_rule_group_output(
    firewall_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    rule_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFirewallPolicyRuleGroupResult]: ...
