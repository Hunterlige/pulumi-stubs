

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResolverRuleResult', 'AwaitableGetResolverRuleResult', 'get_resolver_rule', 'get_resolver_rule_output']
@pulumi.output_type
class GetResolverRuleResult:
    
    def __init__(__self__, arn=..., domain_name=..., id=..., name=..., owner_id=..., region=..., resolver_endpoint_id=..., resolver_rule_id=..., rule_type=..., share_status=..., tags=..., target_ips=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolverEndpointId")
    def resolver_endpoint_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolverRuleId")
    def resolver_rule_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareStatus")
    def share_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetIps")
    def target_ips(self) -> Sequence[outputs.GetResolverRuleTargetIpResult]:
        
        ...
    


class AwaitableGetResolverRuleResult(GetResolverRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetResolverRuleResult]:
        ...
    


def get_resolver_rule(domain_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., resolver_endpoint_id: Optional[_builtins.str] = ..., resolver_rule_id: Optional[_builtins.str] = ..., rule_type: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResolverRuleResult:
    
    ...

def get_resolver_rule_output(domain_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resolver_endpoint_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resolver_rule_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., rule_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResolverRuleResult]:
    
    ...

