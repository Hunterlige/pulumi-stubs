

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIpamPreviewNextCidrResult', 'AwaitableGetIpamPreviewNextCidrResult', 'get_ipam_preview_next_cidr', 'get_ipam_preview_next_cidr_output']
@pulumi.output_type
class GetIpamPreviewNextCidrResult:
    
    def __init__(__self__, cidr=..., disallowed_cidrs=..., id=..., ipam_pool_id=..., netmask_length=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disallowedCidrs")
    def disallowed_cidrs(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="netmaskLength")
    def netmask_length(self) -> Optional[_builtins.int]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetIpamPreviewNextCidrResult(GetIpamPreviewNextCidrResult):
    def __await__(self): # -> Generator[Never, Any, GetIpamPreviewNextCidrResult]:
        ...
    


def get_ipam_preview_next_cidr(disallowed_cidrs: Optional[Sequence[_builtins.str]] = ..., ipam_pool_id: Optional[_builtins.str] = ..., netmask_length: Optional[_builtins.int] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIpamPreviewNextCidrResult:
    
    ...

def get_ipam_preview_next_cidr_output(disallowed_cidrs: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ..., netmask_length: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIpamPreviewNextCidrResult]:
    
    ...

