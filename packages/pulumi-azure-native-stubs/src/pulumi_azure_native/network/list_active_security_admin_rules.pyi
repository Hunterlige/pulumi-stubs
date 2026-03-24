

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListActiveSecurityAdminRulesResult', 'AwaitableListActiveSecurityAdminRulesResult', 'list_active_security_admin_rules', 'list_active_security_admin_rules_output']
@pulumi.output_type
class ListActiveSecurityAdminRulesResult:
    
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
    


class AwaitableListActiveSecurityAdminRulesResult(ListActiveSecurityAdminRulesResult):
    def __await__(self): # -> Generator[Never, Any, ListActiveSecurityAdminRulesResult]:
        ...
    


def list_active_security_admin_rules(network_manager_name: Optional[_builtins.str] = ..., regions: Optional[Sequence[_builtins.str]] = ..., resource_group_name: Optional[_builtins.str] = ..., skip_token: Optional[_builtins.str] = ..., top: Optional[_builtins.int] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListActiveSecurityAdminRulesResult:
    
    ...

def list_active_security_admin_rules_output(network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., regions: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., top: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListActiveSecurityAdminRulesResult]:
    
    ...

