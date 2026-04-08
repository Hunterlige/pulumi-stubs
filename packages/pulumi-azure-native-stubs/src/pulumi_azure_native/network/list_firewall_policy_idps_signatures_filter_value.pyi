import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListFirewallPolicyIdpsSignaturesFilterValueResult",
    ...,
    "list_firewall_policy_idps_signatures_filter_value",
    ...,
]

@pulumi.output_type
class ListFirewallPolicyIdpsSignaturesFilterValueResult:
    def __init__(__self__, filter_values=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterValues")
    def filter_values(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableListFirewallPolicyIdpsSignaturesFilterValueResult(
    ListFirewallPolicyIdpsSignaturesFilterValueResult
):
    def __await__(self): ...

def list_firewall_policy_idps_signatures_filter_value(
    filter_name: Optional[_builtins.str] = ...,
    firewall_policy_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListFirewallPolicyIdpsSignaturesFilterValueResult: ...
def list_firewall_policy_idps_signatures_filter_value_output(
    filter_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    firewall_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListFirewallPolicyIdpsSignaturesFilterValueResult]: ...
