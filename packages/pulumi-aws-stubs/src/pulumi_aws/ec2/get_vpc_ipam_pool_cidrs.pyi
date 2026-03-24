import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVpcIpamPoolCidrsResult",
    "AwaitableGetVpcIpamPoolCidrsResult",
    "get_vpc_ipam_pool_cidrs",
    "get_vpc_ipam_pool_cidrs_output",
]

@pulumi.output_type
class GetVpcIpamPoolCidrsResult:
    def __init__(
        __self__, filters=..., id=..., ipam_pool_cidrs=..., ipam_pool_id=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetVpcIpamPoolCidrsFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipamPoolCidrs")
    def ipam_pool_cidrs(
        self,
    ) -> Sequence[outputs.GetVpcIpamPoolCidrsIpamPoolCidrResult]: ...
    @_builtins.property
    @pulumi.getter(name="ipamPoolId")
    def ipam_pool_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetVpcIpamPoolCidrsResult(GetVpcIpamPoolCidrsResult):
    def __await__(self): ...

def get_vpc_ipam_pool_cidrs(
    filters: Optional[
        Sequence[
            Union[GetVpcIpamPoolCidrsFilterArgs, GetVpcIpamPoolCidrsFilterArgsDict]
        ]
    ] = ...,
    ipam_pool_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVpcIpamPoolCidrsResult: ...
def get_vpc_ipam_pool_cidrs_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetVpcIpamPoolCidrsFilterArgs, GetVpcIpamPoolCidrsFilterArgsDict
                    ]
                ]
            ]
        ]
    ] = ...,
    ipam_pool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVpcIpamPoolCidrsResult]: ...
