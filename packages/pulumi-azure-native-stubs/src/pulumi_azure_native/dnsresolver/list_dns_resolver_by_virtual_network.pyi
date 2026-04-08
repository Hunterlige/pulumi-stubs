import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListDnsResolverByVirtualNetworkResult",
    "AwaitableListDnsResolverByVirtualNetworkResult",
    "list_dns_resolver_by_virtual_network",
    "list_dns_resolver_by_virtual_network_output",
]

@pulumi.output_type
class ListDnsResolverByVirtualNetworkResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.SubResourceResponse]]: ...

class AwaitableListDnsResolverByVirtualNetworkResult(
    ListDnsResolverByVirtualNetworkResult
):
    def __await__(self): ...

def list_dns_resolver_by_virtual_network(
    resource_group_name: Optional[_builtins.str] = ...,
    top: Optional[_builtins.int] = ...,
    virtual_network_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListDnsResolverByVirtualNetworkResult: ...
def list_dns_resolver_by_virtual_network_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    top: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    virtual_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListDnsResolverByVirtualNetworkResult]: ...
