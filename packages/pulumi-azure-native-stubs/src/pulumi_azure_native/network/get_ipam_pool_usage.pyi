

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIpamPoolUsageResult', 'AwaitableGetIpamPoolUsageResult', 'get_ipam_pool_usage', 'get_ipam_pool_usage_output']
@pulumi.output_type
class GetIpamPoolUsageResult:
    
    def __init__(__self__, address_prefixes=..., allocated_address_prefixes=..., available_address_prefixes=..., child_pools=..., number_of_allocated_ip_addresses=..., number_of_available_ip_addresses=..., number_of_reserved_ip_addresses=..., reserved_address_prefixes=..., total_number_of_ip_addresses=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefixes")
    def address_prefixes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedAddressPrefixes")
    def allocated_address_prefixes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableAddressPrefixes")
    def available_address_prefixes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="childPools")
    def child_pools(self) -> Sequence[outputs.ResourceBasicsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfAllocatedIPAddresses")
    def number_of_allocated_ip_addresses(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfAvailableIPAddresses")
    def number_of_available_ip_addresses(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfReservedIPAddresses")
    def number_of_reserved_ip_addresses(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedAddressPrefixes")
    def reserved_address_prefixes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalNumberOfIPAddresses")
    def total_number_of_ip_addresses(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIpamPoolUsageResult(GetIpamPoolUsageResult):
    def __await__(self): # -> Generator[Never, Any, GetIpamPoolUsageResult]:
        ...
    


def get_ipam_pool_usage(network_manager_name: Optional[_builtins.str] = ..., pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIpamPoolUsageResult:
    
    ...

def get_ipam_pool_usage_output(network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIpamPoolUsageResult]:
    
    ...

