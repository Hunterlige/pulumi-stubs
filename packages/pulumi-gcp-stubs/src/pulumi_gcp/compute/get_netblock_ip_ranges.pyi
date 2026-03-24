import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNetblockIPRangesResult",
    "AwaitableGetNetblockIPRangesResult",
    "get_netblock_ip_ranges",
    "get_netblock_ip_ranges_output",
]

@pulumi.output_type
class GetNetblockIPRangesResult:
    def __init__(
        __self__,
        cidr_blocks=...,
        cidr_blocks_ipv4s=...,
        cidr_blocks_ipv6s=...,
        id=...,
        range_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocksIpv4s")
    def cidr_blocks_ipv4s(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocksIpv6s")
    def cidr_blocks_ipv6s(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rangeType")
    def range_type(self) -> Optional[_builtins.str]: ...

class AwaitableGetNetblockIPRangesResult(GetNetblockIPRangesResult):
    def __await__(self): ...

def get_netblock_ip_ranges(
    range_type: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNetblockIPRangesResult: ...
def get_netblock_ip_ranges_output(
    range_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNetblockIPRangesResult]: ...
