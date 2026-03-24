import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetResolverFirewallRuleGroupResult",
    "AwaitableGetResolverFirewallRuleGroupResult",
    "get_resolver_firewall_rule_group",
    "get_resolver_firewall_rule_group_output",
]

@pulumi.output_type
class GetResolverFirewallRuleGroupResult:
    def __init__(
        __self__,
        arn=...,
        creation_time=...,
        creator_request_id=...,
        firewall_rule_group_id=...,
        id=...,
        modification_time=...,
        name=...,
        owner_id=...,
        region=...,
        rule_count=...,
        share_status=...,
        status=...,
        status_message=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creatorRequestId")
    def creator_request_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modificationTime")
    def modification_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleCount")
    def rule_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="shareStatus")
    def share_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str: ...

class AwaitableGetResolverFirewallRuleGroupResult(GetResolverFirewallRuleGroupResult):
    def __await__(self): ...

def get_resolver_firewall_rule_group(
    firewall_rule_group_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetResolverFirewallRuleGroupResult: ...
def get_resolver_firewall_rule_group_output(
    firewall_rule_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetResolverFirewallRuleGroupResult]: ...
