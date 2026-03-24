import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetReservedCacheNodeOfferingResult",
    "AwaitableGetReservedCacheNodeOfferingResult",
    "get_reserved_cache_node_offering",
    "get_reserved_cache_node_offering_output",
]

@pulumi.output_type
class GetReservedCacheNodeOfferingResult:
    def __init__(
        __self__,
        cache_node_type=...,
        duration=...,
        fixed_price=...,
        id=...,
        offering_id=...,
        offering_type=...,
        product_description=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheNodeType")
    def cache_node_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fixedPrice")
    def fixed_price(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringId")
    def offering_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="productDescription")
    def product_description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetReservedCacheNodeOfferingResult(GetReservedCacheNodeOfferingResult):
    def __await__(self): ...

def get_reserved_cache_node_offering(
    cache_node_type: Optional[_builtins.str] = ...,
    duration: Optional[_builtins.str] = ...,
    offering_type: Optional[_builtins.str] = ...,
    product_description: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetReservedCacheNodeOfferingResult: ...
def get_reserved_cache_node_offering_output(
    cache_node_type: Optional[pulumi.Input[_builtins.str]] = ...,
    duration: Optional[pulumi.Input[_builtins.str]] = ...,
    offering_type: Optional[pulumi.Input[_builtins.str]] = ...,
    product_description: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetReservedCacheNodeOfferingResult]: ...
