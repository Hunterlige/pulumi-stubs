import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReservedCacheNodeArgs", "ReservedCacheNode"]

@pulumi.input_type
class ReservedCacheNodeArgs:
    def __init__(
        __self__,
        *,
        reserved_cache_nodes_offering_id: pulumi.Input[_builtins.str],
        cache_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[ReservedCacheNodeTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="reservedCacheNodesOfferingId")
    def reserved_cache_nodes_offering_id(self) -> pulumi.Input[_builtins.str]: ...
    @reserved_cache_nodes_offering_id.setter
    def reserved_cache_nodes_offering_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cacheNodeCount")
    def cache_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cache_node_count.setter
    def cache_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ReservedCacheNodeTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[ReservedCacheNodeTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _ReservedCacheNodeState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        cache_node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
        fixed_price: Optional[pulumi.Input[_builtins.float]] = ...,
        offering_type: Optional[pulumi.Input[_builtins.str]] = ...,
        product_description: Optional[pulumi.Input[_builtins.str]] = ...,
        recurring_charges: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReservedCacheNodeRecurringChargeArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reserved_cache_nodes_offering_id: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[ReservedCacheNodeTimeoutsArgs]] = ...,
        usage_price: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheNodeCount")
    def cache_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cache_node_count.setter
    def cache_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheNodeType")
    def cache_node_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cache_node_type.setter
    def cache_node_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fixedPrice")
    def fixed_price(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @fixed_price.setter
    def fixed_price(self, value: Optional[pulumi.Input[_builtins.float]]): ...
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
        pulumi.Input[Sequence[pulumi.Input[ReservedCacheNodeRecurringChargeArgs]]]
    ]: ...
    @recurring_charges.setter
    def recurring_charges(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReservedCacheNodeRecurringChargeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservedCacheNodesOfferingId")
    def reserved_cache_nodes_offering_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reserved_cache_nodes_offering_id.setter
    def reserved_cache_nodes_offering_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ReservedCacheNodeTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[ReservedCacheNodeTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="usagePrice")
    def usage_price(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @usage_price.setter
    def usage_price(self, value: Optional[pulumi.Input[_builtins.float]]): ...

@pulumi.type_token(...)
class ReservedCacheNode(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cache_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reserved_cache_nodes_offering_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[ReservedCacheNodeTimeoutsArgs, ReservedCacheNodeTimeoutsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReservedCacheNodeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        cache_node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
        fixed_price: Optional[pulumi.Input[_builtins.float]] = ...,
        offering_type: Optional[pulumi.Input[_builtins.str]] = ...,
        product_description: Optional[pulumi.Input[_builtins.str]] = ...,
        recurring_charges: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReservedCacheNodeRecurringChargeArgs,
                            ReservedCacheNodeRecurringChargeArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        reserved_cache_nodes_offering_id: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[ReservedCacheNodeTimeoutsArgs, ReservedCacheNodeTimeoutsArgsDict]
            ]
        ] = ...,
        usage_price: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> ReservedCacheNode: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cacheNodeCount")
    def cache_node_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cacheNodeType")
    def cache_node_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fixedPrice")
    def fixed_price(self) -> pulumi.Output[_builtins.float]: ...
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
    ) -> pulumi.Output[Sequence[outputs.ReservedCacheNodeRecurringCharge]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reservedCacheNodesOfferingId")
    def reserved_cache_nodes_offering_id(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.ReservedCacheNodeTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="usagePrice")
    def usage_price(self) -> pulumi.Output[_builtins.float]: ...
