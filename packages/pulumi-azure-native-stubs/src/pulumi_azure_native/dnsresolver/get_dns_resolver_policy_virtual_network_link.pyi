

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDnsResolverPolicyVirtualNetworkLinkResult', ..., 'get_dns_resolver_policy_virtual_network_link', ...]
@pulumi.output_type
class GetDnsResolverPolicyVirtualNetworkLinkResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., location=..., name=..., provisioning_state=..., system_data=..., tags=..., type=..., virtual_network=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> outputs.SubResourceResponse:
        
        ...
    


class AwaitableGetDnsResolverPolicyVirtualNetworkLinkResult(GetDnsResolverPolicyVirtualNetworkLinkResult):
    def __await__(self): # -> Generator[Never, Any, GetDnsResolverPolicyVirtualNetworkLinkResult]:
        ...
    


def get_dns_resolver_policy_virtual_network_link(dns_resolver_policy_name: Optional[_builtins.str] = ..., dns_resolver_policy_virtual_network_link_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDnsResolverPolicyVirtualNetworkLinkResult:
    
    ...

def get_dns_resolver_policy_virtual_network_link_output(dns_resolver_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., dns_resolver_policy_virtual_network_link_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDnsResolverPolicyVirtualNetworkLinkResult]:
    
    ...

