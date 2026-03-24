import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetReservationSubBlockResult",
    "AwaitableGetReservationSubBlockResult",
    "get_reservation_sub_block",
    "get_reservation_sub_block_output",
]

@pulumi.output_type
class GetReservationSubBlockResult:
    def __init__(
        __self__,
        creation_timestamp=...,
        health_infos=...,
        id=...,
        in_use_count=...,
        kind=...,
        name=...,
        physical_topologies=...,
        project=...,
        reservation=...,
        reservation_block=...,
        reservation_sub_block_maintenances=...,
        resource_id=...,
        self_link=...,
        self_link_with_id=...,
        status=...,
        sub_block_count=...,
        zone=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthInfos")
    def health_infos(
        self,
    ) -> Sequence[outputs.GetReservationSubBlockHealthInfoResult]: ...
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
    ) -> Sequence[outputs.GetReservationSubBlockPhysicalTopologyResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def reservation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reservationBlock")
    def reservation_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="reservationSubBlockMaintenances")
    def reservation_sub_block_maintenances(
        self,
    ) -> Sequence[
        outputs.GetReservationSubBlockReservationSubBlockMaintenanceResult
    ]: ...
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
    @pulumi.getter(name="subBlockCount")
    def sub_block_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

class AwaitableGetReservationSubBlockResult(GetReservationSubBlockResult):
    def __await__(self): ...

def get_reservation_sub_block(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    reservation: Optional[_builtins.str] = ...,
    reservation_block: Optional[_builtins.str] = ...,
    zone: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetReservationSubBlockResult: ...
def get_reservation_sub_block_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    reservation: Optional[pulumi.Input[_builtins.str]] = ...,
    reservation_block: Optional[pulumi.Input[_builtins.str]] = ...,
    zone: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetReservationSubBlockResult]: ...
