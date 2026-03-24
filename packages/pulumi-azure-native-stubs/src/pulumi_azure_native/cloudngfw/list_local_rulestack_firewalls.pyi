

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListLocalRulestackFirewallsResult', 'AwaitableListLocalRulestackFirewallsResult', 'list_local_rulestack_firewalls', 'list_local_rulestack_firewalls_output']
@pulumi.output_type
class ListLocalRulestackFirewallsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableListLocalRulestackFirewallsResult(ListLocalRulestackFirewallsResult):
    def __await__(self): # -> Generator[Never, Any, ListLocalRulestackFirewallsResult]:
        ...
    


def list_local_rulestack_firewalls(local_rulestack_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListLocalRulestackFirewallsResult:
    
    ...

def list_local_rulestack_firewalls_output(local_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListLocalRulestackFirewallsResult]:
    
    ...

