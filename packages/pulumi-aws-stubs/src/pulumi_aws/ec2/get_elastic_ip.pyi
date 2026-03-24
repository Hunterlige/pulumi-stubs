

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
__all__ = ['GetElasticIpResult', 'AwaitableGetElasticIpResult', 'get_elastic_ip', 'get_elastic_ip_output']
@pulumi.output_type
class GetElasticIpResult:
    
    def __init__(__self__, arn=..., association_id=..., carrier_ip=..., customer_owned_ip=..., customer_owned_ipv4_pool=..., domain=..., filters=..., id=..., instance_id=..., ipam_pool_id=..., network_interface_id=..., network_interface_owner_id=..., private_dns=..., private_ip=..., ptr_record=..., public_dns=..., public_ip=..., public_ipv4_pool=..., region=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="carrierIp")
    def carrier_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIp")
    def customer_owned_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetElasticIpFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceOwnerId")
    def network_interface_owner_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDns")
    def private_dns(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ptrRecord")
    def ptr_record(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicDns")
    def public_dns(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpv4Pool")
    def public_ipv4_pool(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetElasticIpResult(GetElasticIpResult):
    def __await__(self): # -> Generator[Never, Any, GetElasticIpResult]:
        ...
    


def get_elastic_ip(filters: Optional[Sequence[Union[GetElasticIpFilterArgs, GetElasticIpFilterArgsDict]]] = ..., id: Optional[_builtins.str] = ..., public_ip: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetElasticIpResult:
    
    ...

def get_elastic_ip_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetElasticIpFilterArgs, GetElasticIpFilterArgsDict]]]]] = ..., id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., public_ip: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetElasticIpResult]:
    
    ...

