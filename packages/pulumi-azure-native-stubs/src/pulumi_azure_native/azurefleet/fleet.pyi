import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FleetArgs", "Fleet"]

@pulumi.input_type
class FleetArgs:
    def __init__(
        __self__,
        *,
        compute_profile: pulumi.Input[ComputeProfileArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        vm_sizes_profile: pulumi.Input[Sequence[pulumi.Input[VmSizeProfileArgs]]],
        additional_locations_profile: Optional[
            pulumi.Input[AdditionalLocationsProfileArgs]
        ] = ...,
        fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        plan: Optional[pulumi.Input[PlanArgs]] = ...,
        regular_priority_profile: Optional[
            pulumi.Input[RegularPriorityProfileArgs]
        ] = ...,
        spot_priority_profile: Optional[pulumi.Input[SpotPriorityProfileArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vm_attributes: Optional[pulumi.Input[VMAttributesArgs]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeProfile")
    def compute_profile(self) -> pulumi.Input[ComputeProfileArgs]: ...
    @compute_profile.setter
    def compute_profile(self, value: pulumi.Input[ComputeProfileArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vmSizesProfile")
    def vm_sizes_profile(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[VmSizeProfileArgs]]]: ...
    @vm_sizes_profile.setter
    def vm_sizes_profile(
        self, value: pulumi.Input[Sequence[pulumi.Input[VmSizeProfileArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalLocationsProfile")
    def additional_locations_profile(
        self,
    ) -> Optional[pulumi.Input[AdditionalLocationsProfileArgs]]: ...
    @additional_locations_profile.setter
    def additional_locations_profile(
        self, value: Optional[pulumi.Input[AdditionalLocationsProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fleetName")
    def fleet_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fleet_name.setter
    def fleet_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[PlanArgs]]: ...
    @plan.setter
    def plan(self, value: Optional[pulumi.Input[PlanArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="regularPriorityProfile")
    def regular_priority_profile(
        self,
    ) -> Optional[pulumi.Input[RegularPriorityProfileArgs]]: ...
    @regular_priority_profile.setter
    def regular_priority_profile(
        self, value: Optional[pulumi.Input[RegularPriorityProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="spotPriorityProfile")
    def spot_priority_profile(
        self,
    ) -> Optional[pulumi.Input[SpotPriorityProfileArgs]]: ...
    @spot_priority_profile.setter
    def spot_priority_profile(
        self, value: Optional[pulumi.Input[SpotPriorityProfileArgs]]
    ): ...
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
    @pulumi.getter(name="vmAttributes")
    def vm_attributes(self) -> Optional[pulumi.Input[VMAttributesArgs]]: ...
    @vm_attributes.setter
    def vm_attributes(self, value: Optional[pulumi.Input[VMAttributesArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:azurefleet:Fleet")
class Fleet(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_locations_profile: Optional[
            pulumi.Input[
                Union[
                    AdditionalLocationsProfileArgs, AdditionalLocationsProfileArgsDict
                ]
            ]
        ] = ...,
        compute_profile: Optional[
            pulumi.Input[Union[ComputeProfileArgs, ComputeProfileArgsDict]]
        ] = ...,
        fleet_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        plan: Optional[pulumi.Input[Union[PlanArgs, PlanArgsDict]]] = ...,
        regular_priority_profile: Optional[
            pulumi.Input[
                Union[RegularPriorityProfileArgs, RegularPriorityProfileArgsDict]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        spot_priority_profile: Optional[
            pulumi.Input[Union[SpotPriorityProfileArgs, SpotPriorityProfileArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vm_attributes: Optional[
            pulumi.Input[Union[VMAttributesArgs, VMAttributesArgsDict]]
        ] = ...,
        vm_sizes_profile: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[VmSizeProfileArgs, VmSizeProfileArgsDict]]]
            ]
        ] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FleetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Fleet: ...
    @_builtins.property
    @pulumi.getter(name="additionalLocationsProfile")
    def additional_locations_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.AdditionalLocationsProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeProfile")
    def compute_profile(self) -> pulumi.Output[outputs.ComputeProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional[outputs.PlanResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regularPriorityProfile")
    def regular_priority_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.RegularPriorityProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="spotPriorityProfile")
    def spot_priority_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.SpotPriorityProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmAttributes")
    def vm_attributes(
        self,
    ) -> pulumi.Output[Optional[outputs.VMAttributesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="vmSizesProfile")
    def vm_sizes_profile(
        self,
    ) -> pulumi.Output[Sequence[outputs.VmSizeProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
