import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListGlobalRulestackFirewallsResult",
    "AwaitableListGlobalRulestackFirewallsResult",
    "list_global_rulestack_firewalls",
    "list_global_rulestack_firewalls_output",
]

@pulumi.output_type
class ListGlobalRulestackFirewallsResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[_builtins.str]: ...

class AwaitableListGlobalRulestackFirewallsResult(ListGlobalRulestackFirewallsResult):
    def __await__(self): ...

def list_global_rulestack_firewalls(
    global_rulestack_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListGlobalRulestackFirewallsResult: ...
def list_global_rulestack_firewalls_output(
    global_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListGlobalRulestackFirewallsResult]: ...
