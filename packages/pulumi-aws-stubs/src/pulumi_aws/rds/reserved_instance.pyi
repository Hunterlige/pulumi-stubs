import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReservedInstanceArgs", "ReservedInstance"]

@pulumi.input_type
class ReservedInstanceArgs:
    def __init__(
        __self__,
        *,
        offering_id: pulumi.Input[_builtins.str],
        instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="offeringId")
    def offering_id(self) -> pulumi.Input[_builtins.str]: ...
    @offering_id.setter
    def offering_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationId")
    def reservation_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reservation_id.setter
    def reservation_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _ReservedInstanceState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        currency_code: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_class: Optional[pulumi.Input[_builtins.str]] = ...,
        duration: Optional[pulumi.Input[_builtins.int]] = ...,
        fixed_price: Optional[pulumi.Input[_builtins.float]] = ...,
        instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        lease_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az: Optional[pulumi.Input[_builtins.bool]] = ...,
        offering_id: Optional[pulumi.Input[_builtins.str]] = ...,
        offering_type: Optional[pulumi.Input[_builtins.str]] = ...,
        product_description: Optional[pulumi.Input[_builtins.str]] = ...,
        recurring_charges: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReservedInstanceRecurringChargeArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        usage_price: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @currency_code.setter
    def currency_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceClass")
    def db_instance_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_instance_class.setter
    def db_instance_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="fixedPrice")
    def fixed_price(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @fixed_price.setter
    def fixed_price(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="leaseId")
    def lease_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lease_id.setter
    def lease_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_az.setter
    def multi_az(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="offeringId")
    def offering_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offering_id.setter
    def offering_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offering_type.setter
    def offering_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="productDescription")
    def product_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product_description.setter
    def product_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recurringCharges")
    def recurring_charges(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReservedInstanceRecurringChargeArgs]]]
    ]: ...
    @recurring_charges.setter
    def recurring_charges(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReservedInstanceRecurringChargeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationId")
    def reservation_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reservation_id.setter
    def reservation_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="usagePrice")
    def usage_price(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @usage_price.setter
    def usage_price(self, value: Optional[pulumi.Input[_builtins.float]]): ...

@pulumi.type_token("aws:rds/reservedInstance:ReservedInstance")
class ReservedInstance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        offering_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReservedInstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        currency_code: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_class: Optional[pulumi.Input[_builtins.str]] = ...,
        duration: Optional[pulumi.Input[_builtins.int]] = ...,
        fixed_price: Optional[pulumi.Input[_builtins.float]] = ...,
        instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        lease_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az: Optional[pulumi.Input[_builtins.bool]] = ...,
        offering_id: Optional[pulumi.Input[_builtins.str]] = ...,
        offering_type: Optional[pulumi.Input[_builtins.str]] = ...,
        product_description: Optional[pulumi.Input[_builtins.str]] = ...,
        recurring_charges: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReservedInstanceRecurringChargeArgs,
                            ReservedInstanceRecurringChargeArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        usage_price: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> ReservedInstance: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceClass")
    def db_instance_class(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="fixedPrice")
    def fixed_price(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="leaseId")
    def lease_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="offeringId")
    def offering_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productDescription")
    def product_description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recurringCharges")
    def recurring_charges(
        self,
    ) -> pulumi.Output[Sequence[outputs.ReservedInstanceRecurringCharge]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reservationId")
    def reservation_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="usagePrice")
    def usage_price(self) -> pulumi.Output[_builtins.float]: ...
