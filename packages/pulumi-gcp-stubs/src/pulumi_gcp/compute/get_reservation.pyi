

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReservationResult', 'AwaitableGetReservationResult', 'get_reservation', 'get_reservation_output']
@pulumi.output_type
class GetReservationResult:
    
    def __init__(__self__, block_names=..., commitment=..., creation_timestamp=..., delete_after_durations=..., delete_at_time=..., description=..., enable_emergent_maintenance=..., id=..., kind=..., linked_commitments=..., name=..., project=..., reservation_block_count=..., reservation_sharing_policies=..., resource_statuses=..., satisfies_pzs=..., self_link=..., share_settings=..., specific_reservation_required=..., specific_reservations=..., status=..., zone=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockNames")
    def block_names(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def commitment(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAfterDurations")
    def delete_after_durations(self) -> Sequence[outputs.GetReservationDeleteAfterDurationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAtTime")
    def delete_at_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEmergentMaintenance")
    def enable_emergent_maintenance(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedCommitments")
    def linked_commitments(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationBlockCount")
    def reservation_block_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationSharingPolicies")
    def reservation_sharing_policies(self) -> Sequence[outputs.GetReservationReservationSharingPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceStatuses")
    def resource_statuses(self) -> Sequence[outputs.GetReservationResourceStatusResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareSettings")
    def share_settings(self) -> Sequence[outputs.GetReservationShareSettingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="specificReservationRequired")
    def specific_reservation_required(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="specificReservations")
    def specific_reservations(self) -> Sequence[outputs.GetReservationSpecificReservationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        ...
    


class AwaitableGetReservationResult(GetReservationResult):
    def __await__(self): # -> Generator[Never, Any, GetReservationResult]:
        ...
    


def get_reservation(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., zone: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReservationResult:
    
    ...

def get_reservation_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReservationResult]:
    
    ...

