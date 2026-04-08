import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListCapacityPoolCachePeeringPassphrasesResult",
    ...,
    "list_capacity_pool_cache_peering_passphrases",
    ...,
]

@pulumi.output_type
class ListCapacityPoolCachePeeringPassphrasesResult:
    def __init__(
        __self__,
        cluster_peering_command=...,
        cluster_peering_passphrase=...,
        vserver_peering_command=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterPeeringCommand")
    def cluster_peering_command(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterPeeringPassphrase")
    def cluster_peering_passphrase(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vserverPeeringCommand")
    def vserver_peering_command(self) -> _builtins.str: ...

class AwaitableListCapacityPoolCachePeeringPassphrasesResult(
    ListCapacityPoolCachePeeringPassphrasesResult
):
    def __await__(self): ...

def list_capacity_pool_cache_peering_passphrases(
    account_name: Optional[_builtins.str] = ...,
    cache_name: Optional[_builtins.str] = ...,
    pool_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListCapacityPoolCachePeeringPassphrasesResult: ...
def list_capacity_pool_cache_peering_passphrases_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    cache_name: Optional[pulumi.Input[_builtins.str]] = ...,
    pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListCapacityPoolCachePeeringPassphrasesResult]: ...
