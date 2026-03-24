import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIpRangesResult",
    "AwaitableGetIpRangesResult",
    "get_ip_ranges",
    "get_ip_ranges_output",
]

@pulumi.output_type
class GetIpRangesResult:
    def __init__(
        __self__,
        cidr_blocks=...,
        create_date=...,
        id=...,
        ipv6_cidr_blocks=...,
        regions=...,
        services=...,
        sync_token=...,
        url=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlocks")
    def cidr_blocks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createDate")
    def create_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def services(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncToken")
    def sync_token(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...

class AwaitableGetIpRangesResult(GetIpRangesResult):
    def __await__(self): ...

def get_ip_ranges(
    id: Optional[_builtins.str] = ...,
    regions: Optional[Sequence[_builtins.str]] = ...,
    services: Optional[Sequence[_builtins.str]] = ...,
    url: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIpRangesResult: ...
def get_ip_ranges_output(
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    regions: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    services: Optional[pulumi.Input[Sequence[_builtins.str]]] = ...,
    url: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIpRangesResult]: ...
