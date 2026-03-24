

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResolverFirewallRulesResult', 'AwaitableGetResolverFirewallRulesResult', 'get_resolver_firewall_rules', 'get_resolver_firewall_rules_output']
@pulumi.output_type
class GetResolverFirewallRulesResult:
    
    def __init__(__self__, action=..., firewall_rule_group_id=..., firewall_rules=..., id=..., priority=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> Sequence[outputs.GetResolverFirewallRulesFirewallRuleResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetResolverFirewallRulesResult(GetResolverFirewallRulesResult):
    def __await__(self): # -> Generator[Never, Any, GetResolverFirewallRulesResult]:
        ...
    


def get_resolver_firewall_rules(action: Optional[_builtins.str] = ..., firewall_rule_group_id: Optional[_builtins.str] = ..., priority: Optional[_builtins.int] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResolverFirewallRulesResult:
    
    ...

def get_resolver_firewall_rules_output(action: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., firewall_rule_group_id: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResolverFirewallRulesResult]:
    
    ...

