import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReservationArgs", "Reservation"]

@pulumi.input_type
class ReservationArgs:
    def __init__(
        __self__,
        *,
        slot_capacity: pulumi.Input[_builtins.int],
        autoscale: Optional[pulumi.Input[ReservationAutoscaleArgs]] = ...,
        concurrency: Optional[pulumi.Input[_builtins.int]] = ...,
        edition: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_idle_slots: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_slots: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="slotCapacity")
    def slot_capacity(self) -> pulumi.Input[_builtins.int]: ...
    @slot_capacity.setter
    def slot_capacity(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def autoscale(self) -> Optional[pulumi.Input[ReservationAutoscaleArgs]]: ...
    @autoscale.setter
    def autoscale(self, value: Optional[pulumi.Input[ReservationAutoscaleArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def concurrency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @concurrency.setter
    def concurrency(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreIdleSlots")
    def ignore_idle_slots(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_idle_slots.setter
    def ignore_idle_slots(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxSlots")
    def max_slots(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_slots.setter
    def max_slots(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scaling_mode.setter
    def scaling_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryLocation")
    def secondary_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_location.setter
    def secondary_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ReservationState:
    def __init__(
        __self__,
        *,
        autoscale: Optional[pulumi.Input[ReservationAutoscaleArgs]] = ...,
        concurrency: Optional[pulumi.Input[_builtins.int]] = ...,
        edition: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_idle_slots: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_slots: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        original_primary_location: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReservationReplicationStatusArgs]]]
        ] = ...,
        scaling_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_location: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def autoscale(self) -> Optional[pulumi.Input[ReservationAutoscaleArgs]]: ...
    @autoscale.setter
    def autoscale(self, value: Optional[pulumi.Input[ReservationAutoscaleArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def concurrency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @concurrency.setter
    def concurrency(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreIdleSlots")
    def ignore_idle_slots(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_idle_slots.setter
    def ignore_idle_slots(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxSlots")
    def max_slots(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_slots.setter
    def max_slots(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="originalPrimaryLocation")
    def original_primary_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @original_primary_location.setter
    def original_primary_location(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryLocation")
    def primary_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_location.setter
    def primary_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationStatuses")
    def replication_statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReservationReplicationStatusArgs]]]
    ]: ...
    @replication_statuses.setter
    def replication_statuses(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReservationReplicationStatusArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scaling_mode.setter
    def scaling_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryLocation")
    def secondary_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_location.setter
    def secondary_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="slotCapacity")
    def slot_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @slot_capacity.setter
    def slot_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token("gcp:bigquery/reservation:Reservation")
class Reservation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        autoscale: Optional[
            pulumi.Input[Union[ReservationAutoscaleArgs, ReservationAutoscaleArgsDict]]
        ] = ...,
        concurrency: Optional[pulumi.Input[_builtins.int]] = ...,
        edition: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_idle_slots: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_slots: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_location: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReservationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        autoscale: Optional[
            pulumi.Input[Union[ReservationAutoscaleArgs, ReservationAutoscaleArgsDict]]
        ] = ...,
        concurrency: Optional[pulumi.Input[_builtins.int]] = ...,
        edition: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_idle_slots: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_slots: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        original_primary_location: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_statuses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReservationReplicationStatusArgs,
                            ReservationReplicationStatusArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        scaling_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_location: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> Reservation: ...
    @_builtins.property
    @pulumi.getter
    def autoscale(self) -> pulumi.Output[Optional[outputs.ReservationAutoscale]]: ...
    @_builtins.property
    @pulumi.getter
    def concurrency(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def edition(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreIdleSlots")
    def ignore_idle_slots(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxSlots")
    def max_slots(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originalPrimaryLocation")
    def original_primary_location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryLocation")
    def primary_location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationStatuses")
    def replication_statuses(
        self,
    ) -> pulumi.Output[Sequence[outputs.ReservationReplicationStatus]]: ...
    @_builtins.property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryLocation")
    def secondary_location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="slotCapacity")
    def slot_capacity(self) -> pulumi.Output[_builtins.int]: ...
