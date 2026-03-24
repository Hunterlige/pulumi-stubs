

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
__all__ = ['GetVpcIpamsResult', 'AwaitableGetVpcIpamsResult', 'get_vpc_ipams', 'get_vpc_ipams_output']
@pulumi.output_type
class GetVpcIpamsResult:
    
    def __init__(__self__, filters=..., id=..., ipam_ids=..., ipams=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetVpcIpamsFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipamIds")
    def ipam_ids(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ipams(self) -> Sequence[outputs.GetVpcIpamsIpamResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetVpcIpamsResult(GetVpcIpamsResult):
    def __await__(self): # -> Generator[Never, Any, GetVpcIpamsResult]:
        ...
    


def get_vpc_ipams(filters: Optional[Sequence[Union[GetVpcIpamsFilterArgs, GetVpcIpamsFilterArgsDict]]] = ..., ipam_ids: Optional[Sequence[_builtins.str]] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVpcIpamsResult:
    
    ...

def get_vpc_ipams_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetVpcIpamsFilterArgs, GetVpcIpamsFilterArgsDict]]]]] = ..., ipam_ids: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVpcIpamsResult]:
    
    ...

