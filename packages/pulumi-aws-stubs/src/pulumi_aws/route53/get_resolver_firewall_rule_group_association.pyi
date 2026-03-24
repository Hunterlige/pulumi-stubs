

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResolverFirewallRuleGroupAssociationResult', ..., 'get_resolver_firewall_rule_group_association', ...]
@pulumi.output_type
class GetResolverFirewallRuleGroupAssociationResult:
    
    def __init__(__self__, arn=..., creation_time=..., creator_request_id=..., firewall_rule_group_association_id=..., firewall_rule_group_id=..., id=..., managed_owner_name=..., modification_time=..., mutation_protection=..., name=..., priority=..., region=..., status=..., status_message=..., vpc_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creatorRequestId")
    def creator_request_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallRuleGroupAssociationId")
    def firewall_rule_group_association_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedOwnerName")
    def managed_owner_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modificationTime")
    def modification_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mutationProtection")
    def mutation_protection(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetResolverFirewallRuleGroupAssociationResult(GetResolverFirewallRuleGroupAssociationResult):
    def __await__(self): # -> Generator[Never, Any, GetResolverFirewallRuleGroupAssociationResult]:
        ...
    


def get_resolver_firewall_rule_group_association(firewall_rule_group_association_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResolverFirewallRuleGroupAssociationResult:
    
    ...

def get_resolver_firewall_rule_group_association_output(firewall_rule_group_association_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResolverFirewallRuleGroupAssociationResult]:
    
    ...

