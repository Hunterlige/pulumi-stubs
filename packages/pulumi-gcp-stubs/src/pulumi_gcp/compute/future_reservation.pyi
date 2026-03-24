import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FutureReservationArgs", "FutureReservation"]

@pulumi.input_type
class FutureReservationArgs:
    def __init__(
        __self__,
        *,
        time_window: pulumi.Input[FutureReservationTimeWindowArgs],
        aggregate_reservation: Optional[
            pulumi.Input[FutureReservationAggregateReservationArgs]
        ] = ...,
        auto_created_reservations_delete_time: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        auto_created_reservations_duration: Optional[
            pulumi.Input[FutureReservationAutoCreatedReservationsDurationArgs]
        ] = ...,
        auto_delete_auto_created_reservations: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        commitment_info: Optional[
            pulumi.Input[FutureReservationCommitmentInfoArgs]
        ] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        planning_status: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduling_type: Optional[pulumi.Input[_builtins.str]] = ...,
        share_settings: Optional[
            pulumi.Input[FutureReservationShareSettingsArgs]
        ] = ...,
        specific_reservation_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        specific_sku_properties: Optional[
            pulumi.Input[FutureReservationSpecificSkuPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> pulumi.Input[FutureReservationTimeWindowArgs]: ...
    @time_window.setter
    def time_window(self, value: pulumi.Input[FutureReservationTimeWindowArgs]): ...
    @_builtins.property
    @pulumi.getter(name="aggregateReservation")
    def aggregate_reservation(
        self,
    ) -> Optional[pulumi.Input[FutureReservationAggregateReservationArgs]]: ...
    @aggregate_reservation.setter
    def aggregate_reservation(
        self, value: Optional[pulumi.Input[FutureReservationAggregateReservationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoCreatedReservationsDeleteTime")
    def auto_created_reservations_delete_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_created_reservations_delete_time.setter
    def auto_created_reservations_delete_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoCreatedReservationsDuration")
    def auto_created_reservations_duration(
        self,
    ) -> Optional[
        pulumi.Input[FutureReservationAutoCreatedReservationsDurationArgs]
    ]: ...
    @auto_created_reservations_duration.setter
    def auto_created_reservations_duration(
        self,
        value: Optional[
            pulumi.Input[FutureReservationAutoCreatedReservationsDurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoDeleteAutoCreatedReservations")
    def auto_delete_auto_created_reservations(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_delete_auto_created_reservations.setter
    def auto_delete_auto_created_reservations(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="commitmentInfo")
    def commitment_info(
        self,
    ) -> Optional[pulumi.Input[FutureReservationCommitmentInfoArgs]]: ...
    @commitment_info.setter
    def commitment_info(
        self, value: Optional[pulumi.Input[FutureReservationCommitmentInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="planningStatus")
    def planning_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @planning_status.setter
    def planning_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationMode")
    def reservation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reservation_mode.setter
    def reservation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationName")
    def reservation_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reservation_name.setter
    def reservation_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schedulingType")
    def scheduling_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scheduling_type.setter
    def scheduling_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shareSettings")
    def share_settings(
        self,
    ) -> Optional[pulumi.Input[FutureReservationShareSettingsArgs]]: ...
    @share_settings.setter
    def share_settings(
        self, value: Optional[pulumi.Input[FutureReservationShareSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="specificReservationRequired")
    def specific_reservation_required(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @specific_reservation_required.setter
    def specific_reservation_required(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="specificSkuProperties")
    def specific_sku_properties(
        self,
    ) -> Optional[pulumi.Input[FutureReservationSpecificSkuPropertiesArgs]]: ...
    @specific_sku_properties.setter
    def specific_sku_properties(
        self, value: Optional[pulumi.Input[FutureReservationSpecificSkuPropertiesArgs]]
    ): ...

@pulumi.input_type
class _FutureReservationState:
    def __init__(
        __self__,
        *,
        aggregate_reservation: Optional[
            pulumi.Input[FutureReservationAggregateReservationArgs]
        ] = ...,
        auto_created_reservations_delete_time: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        auto_created_reservations_duration: Optional[
            pulumi.Input[FutureReservationAutoCreatedReservationsDurationArgs]
        ] = ...,
        auto_delete_auto_created_reservations: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        commitment_info: Optional[
            pulumi.Input[FutureReservationCommitmentInfoArgs]
        ] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        planning_status: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduling_type: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link_with_id: Optional[pulumi.Input[_builtins.str]] = ...,
        share_settings: Optional[
            pulumi.Input[FutureReservationShareSettingsArgs]
        ] = ...,
        specific_reservation_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        specific_sku_properties: Optional[
            pulumi.Input[FutureReservationSpecificSkuPropertiesArgs]
        ] = ...,
        statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[FutureReservationStatusArgs]]]
        ] = ...,
        time_window: Optional[pulumi.Input[FutureReservationTimeWindowArgs]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggregateReservation")
    def aggregate_reservation(
        self,
    ) -> Optional[pulumi.Input[FutureReservationAggregateReservationArgs]]: ...
    @aggregate_reservation.setter
    def aggregate_reservation(
        self, value: Optional[pulumi.Input[FutureReservationAggregateReservationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoCreatedReservationsDeleteTime")
    def auto_created_reservations_delete_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_created_reservations_delete_time.setter
    def auto_created_reservations_delete_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoCreatedReservationsDuration")
    def auto_created_reservations_duration(
        self,
    ) -> Optional[
        pulumi.Input[FutureReservationAutoCreatedReservationsDurationArgs]
    ]: ...
    @auto_created_reservations_duration.setter
    def auto_created_reservations_duration(
        self,
        value: Optional[
            pulumi.Input[FutureReservationAutoCreatedReservationsDurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoDeleteAutoCreatedReservations")
    def auto_delete_auto_created_reservations(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_delete_auto_created_reservations.setter
    def auto_delete_auto_created_reservations(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="commitmentInfo")
    def commitment_info(
        self,
    ) -> Optional[pulumi.Input[FutureReservationCommitmentInfoArgs]]: ...
    @commitment_info.setter
    def commitment_info(
        self, value: Optional[pulumi.Input[FutureReservationCommitmentInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="planningStatus")
    def planning_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @planning_status.setter
    def planning_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationMode")
    def reservation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reservation_mode.setter
    def reservation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationName")
    def reservation_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reservation_name.setter
    def reservation_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schedulingType")
    def scheduling_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scheduling_type.setter
    def scheduling_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link_with_id.setter
    def self_link_with_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shareSettings")
    def share_settings(
        self,
    ) -> Optional[pulumi.Input[FutureReservationShareSettingsArgs]]: ...
    @share_settings.setter
    def share_settings(
        self, value: Optional[pulumi.Input[FutureReservationShareSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="specificReservationRequired")
    def specific_reservation_required(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @specific_reservation_required.setter
    def specific_reservation_required(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="specificSkuProperties")
    def specific_sku_properties(
        self,
    ) -> Optional[pulumi.Input[FutureReservationSpecificSkuPropertiesArgs]]: ...
    @specific_sku_properties.setter
    def specific_sku_properties(
        self, value: Optional[pulumi.Input[FutureReservationSpecificSkuPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FutureReservationStatusArgs]]]
    ]: ...
    @statuses.setter
    def statuses(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FutureReservationStatusArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeWindow")
    def time_window(
        self,
    ) -> Optional[pulumi.Input[FutureReservationTimeWindowArgs]]: ...
    @time_window.setter
    def time_window(
        self, value: Optional[pulumi.Input[FutureReservationTimeWindowArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:compute/futureReservation:FutureReservation")
class FutureReservation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aggregate_reservation: Optional[
            pulumi.Input[
                Union[
                    FutureReservationAggregateReservationArgs,
                    FutureReservationAggregateReservationArgsDict,
                ]
            ]
        ] = ...,
        auto_created_reservations_delete_time: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        auto_created_reservations_duration: Optional[
            pulumi.Input[
                Union[
                    FutureReservationAutoCreatedReservationsDurationArgs,
                    FutureReservationAutoCreatedReservationsDurationArgsDict,
                ]
            ]
        ] = ...,
        auto_delete_auto_created_reservations: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        commitment_info: Optional[
            pulumi.Input[
                Union[
                    FutureReservationCommitmentInfoArgs,
                    FutureReservationCommitmentInfoArgsDict,
                ]
            ]
        ] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        planning_status: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduling_type: Optional[pulumi.Input[_builtins.str]] = ...,
        share_settings: Optional[
            pulumi.Input[
                Union[
                    FutureReservationShareSettingsArgs,
                    FutureReservationShareSettingsArgsDict,
                ]
            ]
        ] = ...,
        specific_reservation_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        specific_sku_properties: Optional[
            pulumi.Input[
                Union[
                    FutureReservationSpecificSkuPropertiesArgs,
                    FutureReservationSpecificSkuPropertiesArgsDict,
                ]
            ]
        ] = ...,
        time_window: Optional[
            pulumi.Input[
                Union[
                    FutureReservationTimeWindowArgs, FutureReservationTimeWindowArgsDict
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FutureReservationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        aggregate_reservation: Optional[
            pulumi.Input[
                Union[
                    FutureReservationAggregateReservationArgs,
                    FutureReservationAggregateReservationArgsDict,
                ]
            ]
        ] = ...,
        auto_created_reservations_delete_time: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        auto_created_reservations_duration: Optional[
            pulumi.Input[
                Union[
                    FutureReservationAutoCreatedReservationsDurationArgs,
                    FutureReservationAutoCreatedReservationsDurationArgsDict,
                ]
            ]
        ] = ...,
        auto_delete_auto_created_reservations: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        commitment_info: Optional[
            pulumi.Input[
                Union[
                    FutureReservationCommitmentInfoArgs,
                    FutureReservationCommitmentInfoArgsDict,
                ]
            ]
        ] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_type: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        planning_status: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduling_type: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link_with_id: Optional[pulumi.Input[_builtins.str]] = ...,
        share_settings: Optional[
            pulumi.Input[
                Union[
                    FutureReservationShareSettingsArgs,
                    FutureReservationShareSettingsArgsDict,
                ]
            ]
        ] = ...,
        specific_reservation_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        specific_sku_properties: Optional[
            pulumi.Input[
                Union[
                    FutureReservationSpecificSkuPropertiesArgs,
                    FutureReservationSpecificSkuPropertiesArgsDict,
                ]
            ]
        ] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            FutureReservationStatusArgs, FutureReservationStatusArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        time_window: Optional[
            pulumi.Input[
                Union[
                    FutureReservationTimeWindowArgs, FutureReservationTimeWindowArgsDict
                ]
            ]
        ] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> FutureReservation: ...
    @_builtins.property
    @pulumi.getter(name="aggregateReservation")
    def aggregate_reservation(
        self,
    ) -> pulumi.Output[Optional[outputs.FutureReservationAggregateReservation]]: ...
    @_builtins.property
    @pulumi.getter(name="autoCreatedReservationsDeleteTime")
    def auto_created_reservations_delete_time(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="autoCreatedReservationsDuration")
    def auto_created_reservations_duration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.FutureReservationAutoCreatedReservationsDuration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="autoDeleteAutoCreatedReservations")
    def auto_delete_auto_created_reservations(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="commitmentInfo")
    def commitment_info(
        self,
    ) -> pulumi.Output[Optional[outputs.FutureReservationCommitmentInfo]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="planningStatus")
    def planning_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reservationMode")
    def reservation_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="reservationName")
    def reservation_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="schedulingType")
    def scheduling_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shareSettings")
    def share_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.FutureReservationShareSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="specificReservationRequired")
    def specific_reservation_required(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="specificSkuProperties")
    def specific_sku_properties(
        self,
    ) -> pulumi.Output[Optional[outputs.FutureReservationSpecificSkuProperties]]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.FutureReservationStatus]]: ...
    @_builtins.property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> pulumi.Output[outputs.FutureReservationTimeWindow]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]: ...
