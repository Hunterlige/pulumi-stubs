

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ReservationArgs', 'Reservation']
@pulumi.input_type
class ReservationArgs:
    def __init__(__self__, *, specific_reservation: pulumi.Input[ReservationSpecificReservationArgs], zone: pulumi.Input[_builtins.str], delete_after_duration: Optional[pulumi.Input[ReservationDeleteAfterDurationArgs]] = ..., delete_at_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_emergent_maintenance: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reservation_sharing_policy: Optional[pulumi.Input[ReservationReservationSharingPolicyArgs]] = ..., share_settings: Optional[pulumi.Input[ReservationShareSettingsArgs]] = ..., specific_reservation_required: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="specificReservation")
    def specific_reservation(self) -> pulumi.Input[ReservationSpecificReservationArgs]:
        
        ...
    
    @specific_reservation.setter
    def specific_reservation(self, value: pulumi.Input[ReservationSpecificReservationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @zone.setter
    def zone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAfterDuration")
    def delete_after_duration(self) -> Optional[pulumi.Input[ReservationDeleteAfterDurationArgs]]:
        
        ...
    
    @delete_after_duration.setter
    def delete_after_duration(self, value: Optional[pulumi.Input[ReservationDeleteAfterDurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAtTime")
    def delete_at_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_at_time.setter
    def delete_at_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEmergentMaintenance")
    def enable_emergent_maintenance(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_emergent_maintenance.setter
    def enable_emergent_maintenance(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationSharingPolicy")
    def reservation_sharing_policy(self) -> Optional[pulumi.Input[ReservationReservationSharingPolicyArgs]]:
        
        ...
    
    @reservation_sharing_policy.setter
    def reservation_sharing_policy(self, value: Optional[pulumi.Input[ReservationReservationSharingPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareSettings")
    def share_settings(self) -> Optional[pulumi.Input[ReservationShareSettingsArgs]]:
        
        ...
    
    @share_settings.setter
    def share_settings(self, value: Optional[pulumi.Input[ReservationShareSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="specificReservationRequired")
    def specific_reservation_required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @specific_reservation_required.setter
    def specific_reservation_required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _ReservationState:
    def __init__(__self__, *, block_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., commitment: Optional[pulumi.Input[_builtins.str]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., delete_after_duration: Optional[pulumi.Input[ReservationDeleteAfterDurationArgs]] = ..., delete_at_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_emergent_maintenance: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., linked_commitments: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reservation_block_count: Optional[pulumi.Input[_builtins.int]] = ..., reservation_sharing_policy: Optional[pulumi.Input[ReservationReservationSharingPolicyArgs]] = ..., resource_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[ReservationResourceStatusArgs]]]] = ..., satisfies_pzs: Optional[pulumi.Input[_builtins.bool]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., share_settings: Optional[pulumi.Input[ReservationShareSettingsArgs]] = ..., specific_reservation: Optional[pulumi.Input[ReservationSpecificReservationArgs]] = ..., specific_reservation_required: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockNames")
    def block_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @block_names.setter
    def block_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def commitment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @commitment.setter
    def commitment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAfterDuration")
    def delete_after_duration(self) -> Optional[pulumi.Input[ReservationDeleteAfterDurationArgs]]:
        
        ...
    
    @delete_after_duration.setter
    def delete_after_duration(self, value: Optional[pulumi.Input[ReservationDeleteAfterDurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAtTime")
    def delete_at_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_at_time.setter
    def delete_at_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEmergentMaintenance")
    def enable_emergent_maintenance(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_emergent_maintenance.setter
    def enable_emergent_maintenance(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedCommitments")
    def linked_commitments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @linked_commitments.setter
    def linked_commitments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationBlockCount")
    def reservation_block_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @reservation_block_count.setter
    def reservation_block_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationSharingPolicy")
    def reservation_sharing_policy(self) -> Optional[pulumi.Input[ReservationReservationSharingPolicyArgs]]:
        
        ...
    
    @reservation_sharing_policy.setter
    def reservation_sharing_policy(self, value: Optional[pulumi.Input[ReservationReservationSharingPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceStatuses")
    def resource_statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReservationResourceStatusArgs]]]]:
        
        ...
    
    @resource_statuses.setter
    def resource_statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ReservationResourceStatusArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @satisfies_pzs.setter
    def satisfies_pzs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareSettings")
    def share_settings(self) -> Optional[pulumi.Input[ReservationShareSettingsArgs]]:
        
        ...
    
    @share_settings.setter
    def share_settings(self, value: Optional[pulumi.Input[ReservationShareSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="specificReservation")
    def specific_reservation(self) -> Optional[pulumi.Input[ReservationSpecificReservationArgs]]:
        
        ...
    
    @specific_reservation.setter
    def specific_reservation(self, value: Optional[pulumi.Input[ReservationSpecificReservationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="specificReservationRequired")
    def specific_reservation_required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @specific_reservation_required.setter
    def specific_reservation_required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/reservation:Reservation")
class Reservation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., delete_after_duration: Optional[pulumi.Input[Union[ReservationDeleteAfterDurationArgs, ReservationDeleteAfterDurationArgsDict]]] = ..., delete_at_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_emergent_maintenance: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reservation_sharing_policy: Optional[pulumi.Input[Union[ReservationReservationSharingPolicyArgs, ReservationReservationSharingPolicyArgsDict]]] = ..., share_settings: Optional[pulumi.Input[Union[ReservationShareSettingsArgs, ReservationShareSettingsArgsDict]]] = ..., specific_reservation: Optional[pulumi.Input[Union[ReservationSpecificReservationArgs, ReservationSpecificReservationArgsDict]]] = ..., specific_reservation_required: Optional[pulumi.Input[_builtins.bool]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ReservationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., block_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., commitment: Optional[pulumi.Input[_builtins.str]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., delete_after_duration: Optional[pulumi.Input[Union[ReservationDeleteAfterDurationArgs, ReservationDeleteAfterDurationArgsDict]]] = ..., delete_at_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_emergent_maintenance: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., linked_commitments: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reservation_block_count: Optional[pulumi.Input[_builtins.int]] = ..., reservation_sharing_policy: Optional[pulumi.Input[Union[ReservationReservationSharingPolicyArgs, ReservationReservationSharingPolicyArgsDict]]] = ..., resource_statuses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ReservationResourceStatusArgs, ReservationResourceStatusArgsDict]]]]] = ..., satisfies_pzs: Optional[pulumi.Input[_builtins.bool]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., share_settings: Optional[pulumi.Input[Union[ReservationShareSettingsArgs, ReservationShareSettingsArgsDict]]] = ..., specific_reservation: Optional[pulumi.Input[Union[ReservationSpecificReservationArgs, ReservationSpecificReservationArgsDict]]] = ..., specific_reservation_required: Optional[pulumi.Input[_builtins.bool]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> Reservation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockNames")
    def block_names(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commitment(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAfterDuration")
    def delete_after_duration(self) -> pulumi.Output[Optional[outputs.ReservationDeleteAfterDuration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAtTime")
    def delete_at_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEmergentMaintenance")
    def enable_emergent_maintenance(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedCommitments")
    def linked_commitments(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationBlockCount")
    def reservation_block_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationSharingPolicy")
    def reservation_sharing_policy(self) -> pulumi.Output[outputs.ReservationReservationSharingPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceStatuses")
    def resource_statuses(self) -> pulumi.Output[Sequence[outputs.ReservationResourceStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareSettings")
    def share_settings(self) -> pulumi.Output[outputs.ReservationShareSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="specificReservation")
    def specific_reservation(self) -> pulumi.Output[outputs.ReservationSpecificReservation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="specificReservationRequired")
    def specific_reservation_required(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


