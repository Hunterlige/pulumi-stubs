import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetFleetResult", "AwaitableGetFleetResult", "get_fleet", "get_fleet_output"]

@pulumi.output_type
class GetFleetResult:
    def __init__(
        __self__,
        additional_locations_profile=...,
        azure_api_version=...,
        compute_profile=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        plan=...,
        provisioning_state=...,
        regular_priority_profile=...,
        spot_priority_profile=...,
        system_data=...,
        tags=...,
        time_created=...,
        type=...,
        unique_id=...,
        vm_attributes=...,
        vm_sizes_profile=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalLocationsProfile")
    def additional_locations_profile(
        self,
    ) -> Optional[outputs.AdditionalLocationsProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="computeProfile")
    def compute_profile(self) -> outputs.ComputeProfileResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[outputs.PlanResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regularPriorityProfile")
    def regular_priority_profile(
        self,
    ) -> Optional[outputs.RegularPriorityProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="spotPriorityProfile")
    def spot_priority_profile(
        self,
    ) -> Optional[outputs.SpotPriorityProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vmAttributes")
    def vm_attributes(self) -> Optional[outputs.VMAttributesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="vmSizesProfile")
    def vm_sizes_profile(self) -> Sequence[outputs.VmSizeProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableGetFleetResult(GetFleetResult):
    def __await__(self): ...

def get_fleet(
    fleet_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFleetResult: ...
def get_fleet_output(
    fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFleetResult]: ...
