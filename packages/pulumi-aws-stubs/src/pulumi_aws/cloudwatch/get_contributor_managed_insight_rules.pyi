

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetContributorManagedInsightRulesResult', 'AwaitableGetContributorManagedInsightRulesResult', 'get_contributor_managed_insight_rules', 'get_contributor_managed_insight_rules_output']
@pulumi.output_type
class GetContributorManagedInsightRulesResult:
    
    def __init__(__self__, id=..., managed_rules=..., region=..., resource_arn=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> Sequence[outputs.GetContributorManagedInsightRulesManagedRuleResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str:
        
        ...
    


class AwaitableGetContributorManagedInsightRulesResult(GetContributorManagedInsightRulesResult):
    def __await__(self): # -> Generator[Never, Any, GetContributorManagedInsightRulesResult]:
        ...
    


def get_contributor_managed_insight_rules(region: Optional[_builtins.str] = ..., resource_arn: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetContributorManagedInsightRulesResult:
    
    ...

def get_contributor_managed_insight_rules_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetContributorManagedInsightRulesResult]:
    
    ...

