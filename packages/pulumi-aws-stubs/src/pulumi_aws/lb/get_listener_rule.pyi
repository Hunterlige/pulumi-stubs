

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetListenerRuleResult', 'AwaitableGetListenerRuleResult', 'get_listener_rule', 'get_listener_rule_output']
@pulumi.output_type
class GetListenerRuleResult:
    
    def __init__(__self__, actions=..., arn=..., conditions=..., id=..., listener_arn=..., priority=..., region=..., tags=..., transforms=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[outputs.GetListenerRuleActionResult]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.GetListenerRuleConditionResult]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> _builtins.str:
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
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[outputs.GetListenerRuleTransformResult]]:
        
        ...
    


class AwaitableGetListenerRuleResult(GetListenerRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetListenerRuleResult]:
        ...
    


def get_listener_rule(actions: Optional[Sequence[Union[GetListenerRuleActionArgs, GetListenerRuleActionArgsDict]]] = ..., arn: Optional[_builtins.str] = ..., conditions: Optional[Sequence[Union[GetListenerRuleConditionArgs, GetListenerRuleConditionArgsDict]]] = ..., listener_arn: Optional[_builtins.str] = ..., priority: Optional[_builtins.int] = ..., region: Optional[_builtins.str] = ..., transforms: Optional[Sequence[Union[GetListenerRuleTransformArgs, GetListenerRuleTransformArgsDict]]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetListenerRuleResult:
    
    ...

def get_listener_rule_output(actions: Optional[pulumi.Input[Optional[Sequence[Union[GetListenerRuleActionArgs, GetListenerRuleActionArgsDict]]]]] = ..., arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., conditions: Optional[pulumi.Input[Optional[Sequence[Union[GetListenerRuleConditionArgs, GetListenerRuleConditionArgsDict]]]]] = ..., listener_arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., priority: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., transforms: Optional[pulumi.Input[Optional[Sequence[Union[GetListenerRuleTransformArgs, GetListenerRuleTransformArgsDict]]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetListenerRuleResult]:
    
    ...

