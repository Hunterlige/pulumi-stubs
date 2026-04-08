import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVirtualMachineResult",
    "AwaitableGetVirtualMachineResult",
    "get_virtual_machine",
    "get_virtual_machine_output",
]

@pulumi.output_type
class GetVirtualMachineResult:
    def __init__(
        __self__,
        additional_capabilities=...,
        application_profile=...,
        availability_set=...,
        azure_api_version=...,
        billing_profile=...,
        capacity_reservation=...,
        diagnostics_profile=...,
        etag=...,
        eviction_policy=...,
        extended_location=...,
        extensions_time_budget=...,
        hardware_profile=...,
        host=...,
        host_group=...,
        id=...,
        identity=...,
        instance_view=...,
        license_type=...,
        location=...,
        managed_by=...,
        name=...,
        network_profile=...,
        os_profile=...,
        placement=...,
        plan=...,
        platform_fault_domain=...,
        priority=...,
        provisioning_state=...,
        proximity_placement_group=...,
        resources=...,
        scheduled_events_policy=...,
        scheduled_events_profile=...,
        security_profile=...,
        storage_profile=...,
        system_data=...,
        tags=...,
        time_created=...,
        type=...,
        user_data=...,
        virtual_machine_scale_set=...,
        vm_id=...,
        zones=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(
        self,
    ) -> Optional[outputs.AdditionalCapabilitiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="applicationProfile")
    def application_profile(self) -> Optional[outputs.ApplicationProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="availabilitySet")
    def availability_set(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingProfile")
    def billing_profile(self) -> Optional[outputs.BillingProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="capacityReservation")
    def capacity_reservation(
        self,
    ) -> Optional[outputs.CapacityReservationProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsProfile")
    def diagnostics_profile(self) -> Optional[outputs.DiagnosticsProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="extensionsTimeBudget")
    def extensions_time_budget(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[outputs.HardwareProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hostGroup")
    def host_group(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.VirtualMachineIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> outputs.VirtualMachineInstanceViewResponse: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[outputs.NetworkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[outputs.OSProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def placement(self) -> Optional[outputs.PlacementResponse]: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[outputs.PlanResponse]: ...
    @_builtins.property
    @pulumi.getter(name="platformFaultDomain")
    def platform_fault_domain(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[outputs.VirtualMachineExtensionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="scheduledEventsPolicy")
    def scheduled_events_policy(
        self,
    ) -> Optional[outputs.ScheduledEventsPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="scheduledEventsProfile")
    def scheduled_events_profile(
        self,
    ) -> Optional[outputs.ScheduledEventsProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[outputs.SecurityProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[outputs.StorageProfileResponse]: ...
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
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineScaleSet")
    def virtual_machine_scale_set(self) -> Optional[outputs.SubResourceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableGetVirtualMachineResult(GetVirtualMachineResult):
    def __await__(self): ...

def get_virtual_machine(
    expand: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    vm_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVirtualMachineResult: ...
def get_virtual_machine_output(
    expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    vm_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVirtualMachineResult]: ...
