

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResolverRulesResult', 'AwaitableGetResolverRulesResult', 'get_resolver_rules', 'get_resolver_rules_output']
@pulumi.output_type
class GetResolverRulesResult:
    
    def __init__(__self__, id=..., name_regex=..., owner_id=..., region=..., resolver_endpoint_id=..., resolver_rule_ids=..., rule_type=..., share_status=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolverEndpointId")
    def resolver_endpoint_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolverRuleIds")
    def resolver_rule_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleType")
    def rule_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareStatus")
    def share_status(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetResolverRulesResult(GetResolverRulesResult):
    def __await__(self): # -> Generator[Never, Any, GetResolverRulesResult]:
        ...
    


def get_resolver_rules(name_regex: Optional[_builtins.str] = ..., owner_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., resolver_endpoint_id: Optional[_builtins.str] = ..., rule_type: Optional[_builtins.str] = ..., share_status: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResolverRulesResult:
    
    ...

def get_resolver_rules_output(name_regex: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., owner_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resolver_endpoint_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., rule_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., share_status: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResolverRulesResult]:
    
    ...

