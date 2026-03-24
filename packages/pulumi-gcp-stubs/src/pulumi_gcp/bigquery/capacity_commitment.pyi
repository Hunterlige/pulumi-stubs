import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CapacityCommitmentArgs", "CapacityCommitment"]

@pulumi.input_type
class CapacityCommitmentArgs:
    def __init__(
        __self__,
        *,
        plan: pulumi.Input[_builtins.str],
        slot_count: pulumi.Input[_builtins.int],
        capacity_commitment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        edition: Optional[pulumi.Input[_builtins.str]] = ...,
        enforce_single_admin_project_per_org: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        renewal_plan: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> pulumi.Input[_builtins.str]: ...
    @plan.setter
    def plan(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="slotCount")
    def slot_count(self) -> pulumi.Input[_builtins.int]: ...
    @slot_count.setter
    def slot_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="capacityCommitmentId")
    def capacity_commitment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capacity_commitment_id.setter
    def capacity_commitment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enforceSingleAdminProjectPerOrg")
    def enforce_single_admin_project_per_org(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enforce_single_admin_project_per_org.setter
    def enforce_single_admin_project_per_org(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="renewalPlan")
    def renewal_plan(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @renewal_plan.setter
    def renewal_plan(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _CapacityCommitmentState:
    def __init__(
        __self__,
        *,
        capacity_commitment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        commitment_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        commitment_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        edition: Optional[pulumi.Input[_builtins.str]] = ...,
        enforce_single_admin_project_per_org: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        plan: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        renewal_plan: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_count: Optional[pulumi.Input[_builtins.int]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityCommitmentId")
    def capacity_commitment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capacity_commitment_id.setter
    def capacity_commitment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commitmentEndTime")
    def commitment_end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commitment_end_time.setter
    def commitment_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commitmentStartTime")
    def commitment_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commitment_start_time.setter
    def commitment_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enforceSingleAdminProjectPerOrg")
    def enforce_single_admin_project_per_org(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enforce_single_admin_project_per_org.setter
    def enforce_single_admin_project_per_org(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plan.setter
    def plan(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="renewalPlan")
    def renewal_plan(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @renewal_plan.setter
    def renewal_plan(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="slotCount")
    def slot_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @slot_count.setter
    def slot_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:bigquery/capacityCommitment:CapacityCommitment")
class CapacityCommitment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        capacity_commitment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        edition: Optional[pulumi.Input[_builtins.str]] = ...,
        enforce_single_admin_project_per_org: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        plan: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        renewal_plan: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_count: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CapacityCommitmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        capacity_commitment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        commitment_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        commitment_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        edition: Optional[pulumi.Input[_builtins.str]] = ...,
        enforce_single_admin_project_per_org: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        plan: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        renewal_plan: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_count: Optional[pulumi.Input[_builtins.int]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> CapacityCommitment: ...
    @_builtins.property
    @pulumi.getter(name="capacityCommitmentId")
    def capacity_commitment_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="commitmentEndTime")
    def commitment_end_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="commitmentStartTime")
    def commitment_start_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def edition(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enforceSingleAdminProjectPerOrg")
    def enforce_single_admin_project_per_org(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="renewalPlan")
    def renewal_plan(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="slotCount")
    def slot_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
