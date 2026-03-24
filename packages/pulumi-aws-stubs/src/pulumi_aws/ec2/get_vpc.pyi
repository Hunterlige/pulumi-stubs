

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVpcResult', 'AwaitableGetVpcResult', 'get_vpc', 'get_vpc_output']
@pulumi.output_type
class GetVpcResult:
    
    def __init__(__self__, arn=..., cidr_block=..., cidr_block_associations=..., default=..., dhcp_options_id=..., enable_dns_hostnames=..., enable_dns_support=..., enable_network_address_usage_metrics=..., filters=..., id=..., instance_tenancy=..., ipv6_association_id=..., ipv6_cidr_block=..., main_route_table_id=..., owner_id=..., region=..., state=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlockAssociations")
    def cidr_block_associations(self) -> Sequence[outputs.GetVpcCidrBlockAssociationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dhcpOptionsId")
    def dhcp_options_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDnsHostnames")
    def enable_dns_hostnames(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDnsSupport")
    def enable_dns_support(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNetworkAddressUsageMetrics")
    def enable_network_address_usage_metrics(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetVpcFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTenancy")
    def instance_tenancy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6AssociationId")
    def ipv6_association_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainRouteTableId")
    def main_route_table_id(self) -> _builtins.str:
        
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
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetVpcResult(GetVpcResult):
    def __await__(self): # -> Generator[Never, Any, GetVpcResult]:
        ...
    


def get_vpc(cidr_block: Optional[_builtins.str] = ..., default: Optional[_builtins.bool] = ..., dhcp_options_id: Optional[_builtins.str] = ..., filters: Optional[Sequence[Union[GetVpcFilterArgs, GetVpcFilterArgsDict]]] = ..., id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVpcResult:
    
    ...

def get_vpc_output(cidr_block: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., default: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., dhcp_options_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., filters: Optional[pulumi.Input[Optional[Sequence[Union[GetVpcFilterArgs, GetVpcFilterArgsDict]]]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., state: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVpcResult]:
    
    ...

