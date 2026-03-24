import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetReservationBlockResult",
    "AwaitableGetReservationBlockResult",
    "get_reservation_block",
    "get_reservation_block_output",
]

@pulumi.output_type
class GetReservationBlockResult:
    def __init__(
        __self__,
        block_count=...,
        creation_timestamp=...,
        health_infos=...,
        id=...,
        in_use_count=...,
        kind=...,
        name=...,
        physical_topologies=...,
        project=...,
        reservation=...,
        reservation_maintenances=...,
        reservation_sub_block_count=...,
        reservation_sub_block_in_use_count=...,
        resource_id=...,
        self_link=...,
        self_link_with_id=...,
        status=...,
        sub_block_names=...,
        zone=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockCount")
    def block_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthInfos")
    def health_infos(self) -> Sequence[outputs.GetReservationBlockHealthInfoResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inUseCount")
    def in_use_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="physicalTopologies")
    def physical_topologies(
        self,
    ) -> Sequence[outputs.GetReservationBlockPhysicalTopologyResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def reservation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reservationMaintenances")
    def reservation_maintenances(
        self,
    ) -> Sequence[outputs.GetReservationBlockReservationMaintenanceResult]: ...
    @_builtins.property
    @pulumi.getter(name="reservationSubBlockCount")
    def reservation_sub_block_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="reservationSubBlockInUseCount")
    def reservation_sub_block_in_use_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subBlockNames")
    def sub_block_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

class AwaitableGetReservationBlockResult(GetReservationBlockResult):
    def __await__(self): ...

def get_reservation_block(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    reservation: Optional[_builtins.str] = ...,
    zone: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetReservationBlockResult: ...
def get_reservation_block_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    reservation: Optional[pulumi.Input[_builtins.str]] = ...,
    zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetReservationBlockResult]: ...
