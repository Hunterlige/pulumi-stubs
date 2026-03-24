

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetManagedRuleGroupResult', 'AwaitableGetManagedRuleGroupResult', 'get_managed_rule_group', 'get_managed_rule_group_output']
@pulumi.output_type
class GetManagedRuleGroupResult:
    
    def __init__(__self__, available_labels=..., capacity=..., consumed_labels=..., id=..., label_namespace=..., name=..., region=..., rules=..., scope=..., sns_topic_arn=..., vendor_name=..., version_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableLabels")
    def available_labels(self) -> Sequence[outputs.GetManagedRuleGroupAvailableLabelResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumedLabels")
    def consumed_labels(self) -> Sequence[outputs.GetManagedRuleGroupConsumedLabelResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelNamespace")
    def label_namespace(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.GetManagedRuleGroupRuleResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vendorName")
    def vendor_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetManagedRuleGroupResult(GetManagedRuleGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetManagedRuleGroupResult]:
        ...
    


def get_managed_rule_group(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., scope: Optional[_builtins.str] = ..., vendor_name: Optional[_builtins.str] = ..., version_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetManagedRuleGroupResult:
    
    ...

def get_managed_rule_group_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., vendor_name: Optional[pulumi.Input[_builtins.str]] = ..., version_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetManagedRuleGroupResult]:
    
    ...

