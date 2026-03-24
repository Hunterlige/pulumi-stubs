

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListFirewallPolicyIdpsSignatureResult', 'AwaitableListFirewallPolicyIdpsSignatureResult', 'list_firewall_policy_idps_signature', 'list_firewall_policy_idps_signature_output']
@pulumi.output_type
class ListFirewallPolicyIdpsSignatureResult:
    
    def __init__(__self__, matching_records_count=..., signatures=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchingRecordsCount")
    def matching_records_count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def signatures(self) -> Optional[Sequence[outputs.SingleQueryResultResponse]]:
        
        ...
    


class AwaitableListFirewallPolicyIdpsSignatureResult(ListFirewallPolicyIdpsSignatureResult):
    def __await__(self): # -> Generator[Never, Any, ListFirewallPolicyIdpsSignatureResult]:
        ...
    


def list_firewall_policy_idps_signature(filters: Optional[Sequence[Union[FilterItems, FilterItemsDict]]] = ..., firewall_policy_name: Optional[_builtins.str] = ..., order_by: Optional[Union[OrderBy, OrderByDict]] = ..., resource_group_name: Optional[_builtins.str] = ..., results_per_page: Optional[_builtins.int] = ..., search: Optional[_builtins.str] = ..., skip: Optional[_builtins.int] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListFirewallPolicyIdpsSignatureResult:
    
    ...

def list_firewall_policy_idps_signature_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[FilterItems, FilterItemsDict]]]]] = ..., firewall_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., order_by: Optional[pulumi.Input[Optional[Union[OrderBy, OrderByDict]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., results_per_page: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., search: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., skip: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListFirewallPolicyIdpsSignatureResult]:
    
    ...

