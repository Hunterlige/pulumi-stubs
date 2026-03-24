

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetActiveReceiptRuleSetResult', 'AwaitableGetActiveReceiptRuleSetResult', 'get_active_receipt_rule_set', 'get_active_receipt_rule_set_output']
@pulumi.output_type
class GetActiveReceiptRuleSetResult:
    
    def __init__(__self__, arn=..., id=..., region=..., rule_set_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleSetName")
    def rule_set_name(self) -> _builtins.str:
        
        ...
    


class AwaitableGetActiveReceiptRuleSetResult(GetActiveReceiptRuleSetResult):
    def __await__(self): # -> Generator[Never, Any, GetActiveReceiptRuleSetResult]:
        ...
    


def get_active_receipt_rule_set(region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetActiveReceiptRuleSetResult:
    
    ...

def get_active_receipt_rule_set_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetActiveReceiptRuleSetResult]:
    
    ...

