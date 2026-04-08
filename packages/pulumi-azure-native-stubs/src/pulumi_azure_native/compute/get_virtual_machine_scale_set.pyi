import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualMachineScaleSetResult",
    "AwaitableGetVirtualMachineScaleSetResult",
    "get_virtual_machine_scale_set",
    "get_virtual_machine_scale_set_output",
]

@pulumi.output_type
class GetVirtualMachineScaleSetResult:
    def __init__(
        __self__,
        additional_capabilities=...,
        automatic_repairs_policy=...,
        azure_api_version=...,
        constrained_maximum_capacity=...,
        do_not_run_extensions_on_overprovisioned_vms=...,
        etag=...,
        extended_location=...,
        host_group=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        orchestration_mode=...,
        overprovision=...,
        plan=...,
        platform_fault_domain_count=...,
        priority_mix_policy=...,
        provisioning_state=...,
        proximity_placement_group=...,
        resiliency_policy=...,
        scale_in_policy=...,
        scheduled_events_policy=...,
        single_placement_group=...,
        sku=...,
        sku_profile=...,
        spot_restore_policy=...,
        system_data=...,
        tags=...,
        time_created=...,
        type=...,
        unique_id=...,
        upgrade_policy=...,
        virtual_machine_profile=...,
        zonal_platform_fault_domain_align_mode=...,
        zone_balance=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(
        self,
    ) -> Optional[outputs.AdditionalCapabilitiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="automaticRepairsPolicy")
    def automatic_repairs_policy(
        self,
    ) -> Optional[outputs.AutomaticRepairsPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="constrainedMaximumCapacity")
    def constrained_maximum_capacity(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="doNotRunExtensionsOnOverprovisionedVMs")
    def do_not_run_extensions_on_overprovisioned_vms(
        self,
    ) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hostGroup")
    def host_group(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.VirtualMachineScaleSetIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="orchestrationMode")
    def orchestration_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def overprovision(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[outputs.PlanResponse]: ...
    @_builtins.property
    @pulumi.getter(name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="priorityMixPolicy")
    def priority_mix_policy(self) -> Optional[outputs.PriorityMixPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resiliencyPolicy")
    def resiliency_policy(self) -> Optional[outputs.ResiliencyPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="scaleInPolicy")
    def scale_in_policy(self) -> Optional[outputs.ScaleInPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="scheduledEventsPolicy")
    def scheduled_events_policy(
        self,
    ) -> Optional[outputs.ScheduledEventsPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="singlePlacementGroup")
    def single_placement_group(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="skuProfile")
    def sku_profile(self) -> Optional[outputs.SkuProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="spotRestorePolicy")
    def spot_restore_policy(self) -> Optional[outputs.SpotRestorePolicyResponse]: ...
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
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional[outputs.UpgradePolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineProfile")
    def virtual_machine_profile(
        self,
    ) -> Optional[outputs.VirtualMachineScaleSetVMProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="zonalPlatformFaultDomainAlignMode")
    def zonal_platform_fault_domain_align_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zoneBalance")
    def zone_balance(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableGetVirtualMachineScaleSetResult(GetVirtualMachineScaleSetResult):
    def __await__(self): ...

def get_virtual_machine_scale_set(
    expand: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    vm_scale_set_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualMachineScaleSetResult: ...
def get_virtual_machine_scale_set_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    vm_scale_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualMachineScaleSetResult]: ...
