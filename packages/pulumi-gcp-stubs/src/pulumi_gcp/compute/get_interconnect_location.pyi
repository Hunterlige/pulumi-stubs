import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInterconnectLocationResult",
    "AwaitableGetInterconnectLocationResult",
    "get_interconnect_location",
    "get_interconnect_location_output",
]

@pulumi.output_type
class GetInterconnectLocationResult:
    def __init__(
        __self__,
        address=...,
        availability_zone=...,
        city=...,
        continent=...,
        description=...,
        facility_provider=...,
        facility_provider_facility_id=...,
        id=...,
        name=...,
        peeringdb_facility_id=...,
        project=...,
        self_link=...,
        status=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def continent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="facilityProvider")
    def facility_provider(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="facilityProviderFacilityId")
    def facility_provider_facility_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peeringdbFacilityId")
    def peeringdb_facility_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

class AwaitableGetInterconnectLocationResult(GetInterconnectLocationResult):
    def __await__(self): ...

def get_interconnect_location(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInterconnectLocationResult: ...
def get_interconnect_location_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInterconnectLocationResult]: ...
