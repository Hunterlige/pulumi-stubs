import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AvailabilitySetArgs", "AvailabilitySet"]

@pulumi.input_type
class AvailabilitySetArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        availability_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_fault_domain_count: Optional[pulumi.Input[_builtins.int]] = ...,
        platform_update_domain_count: Optional[pulumi.Input[_builtins.int]] = ...,
        proximity_placement_group: Optional[pulumi.Input[SubResourceArgs]] = ...,
        scheduled_events_policy: Optional[
            pulumi.Input[ScheduledEventsPolicyArgs]
        ] = ...,
        sku: Optional[pulumi.Input[SkuArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_machines: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="availabilitySetName")
    def availability_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_set_name.setter
    def availability_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @platform_fault_domain_count.setter
    def platform_fault_domain_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="platformUpdateDomainCount")
    def platform_update_domain_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @platform_update_domain_count.setter
    def platform_update_domain_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> Optional[pulumi.Input[SubResourceArgs]]: ...
    @proximity_placement_group.setter
    def proximity_placement_group(
        self, value: Optional[pulumi.Input[SubResourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scheduledEventsPolicy")
    def scheduled_events_policy(
        self,
    ) -> Optional[pulumi.Input[ScheduledEventsPolicyArgs]]: ...
    @scheduled_events_policy.setter
    def scheduled_events_policy(
        self, value: Optional[pulumi.Input[ScheduledEventsPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): ...
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
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]: ...
    @virtual_machines.setter
    def virtual_machines(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SubResourceArgs]]]]
    ): ...

@pulumi.type_token("azure-native:compute:AvailabilitySet")
class AvailabilitySet(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        availability_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_fault_domain_count: Optional[pulumi.Input[_builtins.int]] = ...,
        platform_update_domain_count: Optional[pulumi.Input[_builtins.int]] = ...,
        proximity_placement_group: Optional[
            pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduled_events_policy: Optional[
            pulumi.Input[
                Union[ScheduledEventsPolicyArgs, ScheduledEventsPolicyArgsDict]
            ]
        ] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_machines: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AvailabilitySetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AvailabilitySet: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="platformUpdateDomainCount")
    def platform_update_domain_count(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(
        self,
    ) -> pulumi.Output[Optional[outputs.SubResourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="scheduledEventsPolicy")
    def scheduled_events_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.ScheduledEventsPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceViewStatusResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineScaleSetMigrationInfo")
    def virtual_machine_scale_set_migration_info(
        self,
    ) -> pulumi.Output[outputs.VirtualMachineScaleSetMigrationInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.SubResourceResponse]]]: ...
