

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPublicIpv4PoolResult', 'AwaitableGetPublicIpv4PoolResult', 'get_public_ipv4_pool', 'get_public_ipv4_pool_output']
@pulumi.output_type
class GetPublicIpv4PoolResult:
    
    def __init__(__self__, description=..., id=..., network_border_group=..., pool_address_ranges=..., pool_id=..., region=..., tags=..., total_address_count=..., total_available_address_count=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkBorderGroup")
    def network_border_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolAddressRanges")
    def pool_address_ranges(self) -> Sequence[outputs.GetPublicIpv4PoolPoolAddressRangeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> _builtins.str:
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
    @pulumi.getter(name="totalAddressCount")
    def total_address_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalAvailableAddressCount")
    def total_available_address_count(self) -> _builtins.int:
        
        ...
    


class AwaitableGetPublicIpv4PoolResult(GetPublicIpv4PoolResult):
    def __await__(self): # -> Generator[Never, Any, GetPublicIpv4PoolResult]:
        ...
    


def get_public_ipv4_pool(pool_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPublicIpv4PoolResult:
    
    ...

def get_public_ipv4_pool_output(pool_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPublicIpv4PoolResult]:
    
    ...

