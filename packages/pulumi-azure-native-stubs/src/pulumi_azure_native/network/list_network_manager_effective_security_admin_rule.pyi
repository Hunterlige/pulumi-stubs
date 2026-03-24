

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListNetworkManagerEffectiveSecurityAdminRuleResult', ..., 'list_network_manager_effective_security_admin_rule', ...]
@pulumi.output_type
class ListNetworkManagerEffectiveSecurityAdminRuleResult:
    
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
    


class AwaitableListNetworkManagerEffectiveSecurityAdminRuleResult(ListNetworkManagerEffectiveSecurityAdminRuleResult):
    def __await__(self): # -> Generator[Never, Any, ListNetworkManagerEffectiveSecurityAdminRuleResult]:
        ...
    


def list_network_manager_effective_security_admin_rule(resource_group_name: Optional[_builtins.str] = ..., skip_token: Optional[_builtins.str] = ..., virtual_network_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListNetworkManagerEffectiveSecurityAdminRuleResult:
    
    ...

def list_network_manager_effective_security_admin_rule_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., virtual_network_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListNetworkManagerEffectiveSecurityAdminRuleResult]:
    
    ...

