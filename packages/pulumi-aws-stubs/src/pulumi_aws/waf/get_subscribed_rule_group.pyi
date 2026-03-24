

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSubscribedRuleGroupResult', 'AwaitableGetSubscribedRuleGroupResult', 'get_subscribed_rule_group', 'get_subscribed_rule_group_output']
@pulumi.output_type
class GetSubscribedRuleGroupResult:
    
    def __init__(__self__, id=..., metric_name=..., name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetSubscribedRuleGroupResult(GetSubscribedRuleGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetSubscribedRuleGroupResult]:
        ...
    


def get_subscribed_rule_group(metric_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSubscribedRuleGroupResult:
    
    ...

def get_subscribed_rule_group_output(metric_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSubscribedRuleGroupResult]:
    
    ...

