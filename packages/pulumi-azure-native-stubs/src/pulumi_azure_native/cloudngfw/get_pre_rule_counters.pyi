import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPreRuleCountersResult",
    "AwaitableGetPreRuleCountersResult",
    "get_pre_rule_counters",
    "get_pre_rule_counters_output",
]

@pulumi.output_type
class GetPreRuleCountersResult:
    def __init__(
        __self__,
        app_seen=...,
        firewall_name=...,
        hit_count=...,
        last_updated_timestamp=...,
        priority=...,
        request_timestamp=...,
        rule_list_name=...,
        rule_name=...,
        rule_stack_name=...,
        timestamp=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appSeen")
    def app_seen(self) -> Optional[outputs.AppSeenDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="firewallName")
    def firewall_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hitCount")
    def hit_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requestTimestamp")
    def request_timestamp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleListName")
    def rule_list_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleStackName")
    def rule_stack_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> Optional[_builtins.str]: ...

class AwaitableGetPreRuleCountersResult(GetPreRuleCountersResult):
    def __await__(self): ...

def get_pre_rule_counters(
    firewall_name: Optional[_builtins.str] = ...,
    global_rulestack_name: Optional[_builtins.str] = ...,
    priority: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPreRuleCountersResult: ...
def get_pre_rule_counters_output(
    firewall_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    global_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ...,
    priority: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPreRuleCountersResult]: ...
