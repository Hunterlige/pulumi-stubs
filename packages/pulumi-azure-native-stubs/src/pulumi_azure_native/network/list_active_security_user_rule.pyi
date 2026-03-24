

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListActiveSecurityUserRuleResult', 'AwaitableListActiveSecurityUserRuleResult', 'list_active_security_user_rule', 'list_active_security_user_rule_output']
@pulumi.output_type
class ListActiveSecurityUserRuleResult:
    
    def __init__(__self__, skip_token=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipToken")
    def skip_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[Any]]:
        
        ...
    


class AwaitableListActiveSecurityUserRuleResult(ListActiveSecurityUserRuleResult):
    def __await__(self): # -> Generator[Never, Any, ListActiveSecurityUserRuleResult]:
        ...
    


def list_active_security_user_rule(network_manager_name: Optional[_builtins.str] = ..., regions: Optional[Sequence[_builtins.str]] = ..., resource_group_name: Optional[_builtins.str] = ..., skip_token: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListActiveSecurityUserRuleResult:
    
    ...

def list_active_security_user_rule_output(network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., regions: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListActiveSecurityUserRuleResult]:
    
    ...

