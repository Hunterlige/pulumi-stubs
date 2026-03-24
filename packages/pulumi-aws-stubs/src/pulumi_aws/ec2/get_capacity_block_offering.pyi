import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCapacityBlockOfferingResult",
    "AwaitableGetCapacityBlockOfferingResult",
    "get_capacity_block_offering",
    "get_capacity_block_offering_output",
]

@pulumi.output_type
class GetCapacityBlockOfferingResult:
    def __init__(
        __self__,
        availability_zone=...,
        capacity_block_offering_id=...,
        capacity_duration_hours=...,
        currency_code=...,
        end_date_range=...,
        id=...,
        instance_count=...,
        instance_type=...,
        region=...,
        start_date_range=...,
        tenancy=...,
        upfront_fee=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="capacityBlockOfferingId")
    def capacity_block_offering_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="capacityDurationHours")
    def capacity_duration_hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endDateRange")
    def end_date_range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startDateRange")
    def start_date_range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="upfrontFee")
    def upfront_fee(self) -> _builtins.str: ...

class AwaitableGetCapacityBlockOfferingResult(GetCapacityBlockOfferingResult):
    def __await__(self): ...

def get_capacity_block_offering(
    capacity_duration_hours: Optional[_builtins.int] = ...,
    end_date_range: Optional[_builtins.str] = ...,
    instance_count: Optional[_builtins.int] = ...,
    instance_type: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    start_date_range: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCapacityBlockOfferingResult: ...
def get_capacity_block_offering_output(
    capacity_duration_hours: Optional[pulumi.Input[_builtins.int]] = ...,
    end_date_range: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
    instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    start_date_range: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCapacityBlockOfferingResult]: ...
