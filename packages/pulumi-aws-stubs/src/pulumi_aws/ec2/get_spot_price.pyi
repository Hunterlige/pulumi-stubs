import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSpotPriceResult",
    "AwaitableGetSpotPriceResult",
    "get_spot_price",
    "get_spot_price_output",
]

@pulumi.output_type
class GetSpotPriceResult:
    def __init__(
        __self__,
        availability_zone=...,
        filters=...,
        id=...,
        instance_type=...,
        region=...,
        spot_price=...,
        spot_price_timestamp=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetSpotPriceFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="spotPriceTimestamp")
    def spot_price_timestamp(self) -> _builtins.str: ...

class AwaitableGetSpotPriceResult(GetSpotPriceResult):
    def __await__(self): ...

def get_spot_price(
    availability_zone: Optional[_builtins.str] = ...,
    filters: Optional[
        Sequence[Union[GetSpotPriceFilterArgs, GetSpotPriceFilterArgsDict]]
    ] = ...,
    instance_type: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSpotPriceResult: ...
def get_spot_price_output(
    availability_zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[Union[GetSpotPriceFilterArgs, GetSpotPriceFilterArgsDict]]
            ]
        ]
    ] = ...,
    instance_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSpotPriceResult]: ...
