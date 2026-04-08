import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFirewallPolicyRuleCollectionGroupDraftResult",
    ...,
    "get_firewall_policy_rule_collection_group_draft",
    ...,
]

@pulumi.output_type
class GetFirewallPolicyRuleCollectionGroupDraftResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        priority=...,
        rule_collections=...,
        size=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
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
    @pulumi.getter(name="ruleCollections")
    def rule_collections(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetFirewallPolicyRuleCollectionGroupDraftResult(
    GetFirewallPolicyRuleCollectionGroupDraftResult
):
    def __await__(self): ...

def get_firewall_policy_rule_collection_group_draft(
    firewall_policy_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    rule_collection_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFirewallPolicyRuleCollectionGroupDraftResult: ...
def get_firewall_policy_rule_collection_group_draft_output(
    firewall_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    rule_collection_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFirewallPolicyRuleCollectionGroupDraftResult]: ...
