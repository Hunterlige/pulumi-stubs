

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from .. import _utilities

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkResult', 'AwaitableGetNetworkResult', 'get_network', 'get_network_output']
@pulumi.output_type
class GetNetworkResult:
    
    def __init__(__self__, description=..., gateway_ipv4=..., id=..., internal_ipv6_range=..., name=..., network_id=..., network_profile=..., numeric_id=..., project=..., self_link=..., subnetworks_self_links=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayIpv4")
    def gateway_ipv4(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIpv6Range")
    def internal_ipv6_range(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkId")
    def network_id(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numericId")
    @_utilities.deprecated(...)
    def numeric_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetworksSelfLinks")
    def subnetworks_self_links(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetNetworkResult(GetNetworkResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkResult]:
        ...
    


def get_network(name: Optional[_builtins.str] = ..., network_profile: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkResult:
    
    ...

def get_network_output(name: Optional[pulumi.Input[_builtins.str]] = ..., network_profile: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkResult]:
    
    ...

