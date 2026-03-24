

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFirewallPolicyResult', 'AwaitableGetFirewallPolicyResult', 'get_firewall_policy', 'get_firewall_policy_output']
@pulumi.output_type
class GetFirewallPolicyResult:
    
    def __init__(__self__, arn=..., description=..., firewall_policies=..., id=..., name=..., region=..., tags=..., update_token=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallPolicies")
    def firewall_policies(self) -> Sequence[outputs.GetFirewallPolicyFirewallPolicyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> _builtins.str:
        
        ...
    


class AwaitableGetFirewallPolicyResult(GetFirewallPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetFirewallPolicyResult]:
        ...
    


def get_firewall_policy(arn: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFirewallPolicyResult:
    
    ...

def get_firewall_policy_output(arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFirewallPolicyResult]:
    
    ...

