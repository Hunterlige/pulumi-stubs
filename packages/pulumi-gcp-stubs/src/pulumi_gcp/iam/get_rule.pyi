

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRuleResult', 'AwaitableGetRuleResult', 'get_rule', 'get_rule_output']
@pulumi.output_type
class GetRuleResult:
    
    def __init__(__self__, id=..., included_permissions=..., name=..., stage=..., title=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPermissions")
    def included_permissions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRuleResult(GetRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetRuleResult]:
        ...
    


def get_rule(name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRuleResult:
    
    ...

def get_rule_output(name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRuleResult]:
    
    ...

