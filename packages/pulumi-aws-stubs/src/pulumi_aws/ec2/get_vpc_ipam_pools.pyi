

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVpcIpamPoolsResult', 'AwaitableGetVpcIpamPoolsResult', 'get_vpc_ipam_pools', 'get_vpc_ipam_pools_output']
@pulumi.output_type
class GetVpcIpamPoolsResult:
    
    def __init__(__self__, filters=..., id=..., ipam_pools=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetVpcIpamPoolsFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPools")
    def ipam_pools(self) -> Sequence[outputs.GetVpcIpamPoolsIpamPoolResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetVpcIpamPoolsResult(GetVpcIpamPoolsResult):
    def __await__(self): # -> Generator[Never, Any, GetVpcIpamPoolsResult]:
        ...
    


def get_vpc_ipam_pools(filters: Optional[Sequence[Union[GetVpcIpamPoolsFilterArgs, GetVpcIpamPoolsFilterArgsDict]]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVpcIpamPoolsResult:
    
    ...

def get_vpc_ipam_pools_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetVpcIpamPoolsFilterArgs, GetVpcIpamPoolsFilterArgsDict]]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVpcIpamPoolsResult]:
    
    ...

