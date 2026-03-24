

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResolverFirewallConfigResult', 'AwaitableGetResolverFirewallConfigResult', 'get_resolver_firewall_config', 'get_resolver_firewall_config_output']
@pulumi.output_type
class GetResolverFirewallConfigResult:
    
    def __init__(__self__, firewall_fail_open=..., id=..., owner_id=..., region=..., resource_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallFailOpen")
    def firewall_fail_open(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str:
        ...
    


class AwaitableGetResolverFirewallConfigResult(GetResolverFirewallConfigResult):
    def __await__(self): # -> Generator[Never, Any, GetResolverFirewallConfigResult]:
        ...
    


def get_resolver_firewall_config(region: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResolverFirewallConfigResult:
    
    ...

def get_resolver_firewall_config_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResolverFirewallConfigResult]:
    
    ...

