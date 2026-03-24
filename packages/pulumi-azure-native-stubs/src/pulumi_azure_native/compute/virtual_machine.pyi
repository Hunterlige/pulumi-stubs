

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VirtualMachineArgs', 'VirtualMachine']
@pulumi.input_type
class VirtualMachineArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], additional_capabilities: Optional[pulumi.Input[AdditionalCapabilitiesArgs]] = ..., application_profile: Optional[pulumi.Input[ApplicationProfileArgs]] = ..., availability_set: Optional[pulumi.Input[SubResourceArgs]] = ..., billing_profile: Optional[pulumi.Input[BillingProfileArgs]] = ..., capacity_reservation: Optional[pulumi.Input[CapacityReservationProfileArgs]] = ..., diagnostics_profile: Optional[pulumi.Input[DiagnosticsProfileArgs]] = ..., eviction_policy: Optional[pulumi.Input[Union[_builtins.str, VirtualMachineEvictionPolicyTypes]]] = ..., extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ..., extensions_time_budget: Optional[pulumi.Input[_builtins.str]] = ..., hardware_profile: Optional[pulumi.Input[HardwareProfileArgs]] = ..., host: Optional[pulumi.Input[SubResourceArgs]] = ..., host_group: Optional[pulumi.Input[SubResourceArgs]] = ..., identity: Optional[pulumi.Input[VirtualMachineIdentityArgs]] = ..., license_type: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_profile: Optional[pulumi.Input[NetworkProfileArgs]] = ..., os_profile: Optional[pulumi.Input[OSProfileArgs]] = ..., placement: Optional[pulumi.Input[PlacementArgs]] = ..., plan: Optional[pulumi.Input[PlanArgs]] = ..., platform_fault_domain: Optional[pulumi.Input[_builtins.int]] = ..., priority: Optional[pulumi.Input[Union[_builtins.str, VirtualMachinePriorityTypes]]] = ..., proximity_placement_group: Optional[pulumi.Input[SubResourceArgs]] = ..., scheduled_events_policy: Optional[pulumi.Input[ScheduledEventsPolicyArgs]] = ..., scheduled_events_profile: Optional[pulumi.Input[ScheduledEventsProfileArgs]] = ..., security_profile: Optional[pulumi.Input[SecurityProfileArgs]] = ..., storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., virtual_machine_scale_set: Optional[pulumi.Input[SubResourceArgs]] = ..., vm_name: Optional[pulumi.Input[_builtins.str]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> Optional[pulumi.Input[AdditionalCapabilitiesArgs]]:
        
        ...
    
    @additional_capabilities.setter
    def additional_capabilities(self, value: Optional[pulumi.Input[AdditionalCapabilitiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationProfile")
    def application_profile(self) -> Optional[pulumi.Input[ApplicationProfileArgs]]:
        
        ...
    
    @application_profile.setter
    def application_profile(self, value: Optional[pulumi.Input[ApplicationProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilitySet")
    def availability_set(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @availability_set.setter
    def availability_set(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingProfile")
    def billing_profile(self) -> Optional[pulumi.Input[BillingProfileArgs]]:
        
        ...
    
    @billing_profile.setter
    def billing_profile(self, value: Optional[pulumi.Input[BillingProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservation")
    def capacity_reservation(self) -> Optional[pulumi.Input[CapacityReservationProfileArgs]]:
        
        ...
    
    @capacity_reservation.setter
    def capacity_reservation(self, value: Optional[pulumi.Input[CapacityReservationProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diagnosticsProfile")
    def diagnostics_profile(self) -> Optional[pulumi.Input[DiagnosticsProfileArgs]]:
        
        ...
    
    @diagnostics_profile.setter
    def diagnostics_profile(self, value: Optional[pulumi.Input[DiagnosticsProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, VirtualMachineEvictionPolicyTypes]]]:
        
        ...
    
    @eviction_policy.setter
    def eviction_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, VirtualMachineEvictionPolicyTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input[ExtendedLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionsTimeBudget")
    def extensions_time_budget(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @extensions_time_budget.setter
    def extensions_time_budget(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> Optional[pulumi.Input[HardwareProfileArgs]]:
        
        ...
    
    @hardware_profile.setter
    def hardware_profile(self, value: Optional[pulumi.Input[HardwareProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostGroup")
    def host_group(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @host_group.setter
    def host_group(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[VirtualMachineIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[VirtualMachineIdentityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @license_type.setter
    def license_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[NetworkProfileArgs]]:
        
        ...
    
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[NetworkProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input[OSProfileArgs]]:
        
        ...
    
    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input[OSProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> Optional[pulumi.Input[PlacementArgs]]:
        
        ...
    
    @placement.setter
    def placement(self, value: Optional[pulumi.Input[PlacementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[PlanArgs]]:
        
        ...
    
    @plan.setter
    def plan(self, value: Optional[pulumi.Input[PlanArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformFaultDomain")
    def platform_fault_domain(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @platform_fault_domain.setter
    def platform_fault_domain(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[Union[_builtins.str, VirtualMachinePriorityTypes]]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[Union[_builtins.str, VirtualMachinePriorityTypes]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @proximity_placement_group.setter
    def proximity_placement_group(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEventsPolicy")
    def scheduled_events_policy(self) -> Optional[pulumi.Input[ScheduledEventsPolicyArgs]]:
        
        ...
    
    @scheduled_events_policy.setter
    def scheduled_events_policy(self, value: Optional[pulumi.Input[ScheduledEventsPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEventsProfile")
    def scheduled_events_profile(self) -> Optional[pulumi.Input[ScheduledEventsProfileArgs]]:
        
        ...
    
    @scheduled_events_profile.setter
    def scheduled_events_profile(self, value: Optional[pulumi.Input[ScheduledEventsProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional[pulumi.Input[SecurityProfileArgs]]:
        
        ...
    
    @security_profile.setter
    def security_profile(self, value: Optional[pulumi.Input[SecurityProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]:
        
        ...
    
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineScaleSet")
    def virtual_machine_scale_set(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @virtual_machine_scale_set.setter
    def virtual_machine_scale_set(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmName")
    def vm_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vm_name.setter
    def vm_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:compute:VirtualMachine")
class VirtualMachine(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., additional_capabilities: Optional[pulumi.Input[Union[AdditionalCapabilitiesArgs, AdditionalCapabilitiesArgsDict]]] = ..., application_profile: Optional[pulumi.Input[Union[ApplicationProfileArgs, ApplicationProfileArgsDict]]] = ..., availability_set: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., billing_profile: Optional[pulumi.Input[Union[BillingProfileArgs, BillingProfileArgsDict]]] = ..., capacity_reservation: Optional[pulumi.Input[Union[CapacityReservationProfileArgs, CapacityReservationProfileArgsDict]]] = ..., diagnostics_profile: Optional[pulumi.Input[Union[DiagnosticsProfileArgs, DiagnosticsProfileArgsDict]]] = ..., eviction_policy: Optional[pulumi.Input[Union[_builtins.str, VirtualMachineEvictionPolicyTypes]]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]] = ..., extensions_time_budget: Optional[pulumi.Input[_builtins.str]] = ..., hardware_profile: Optional[pulumi.Input[Union[HardwareProfileArgs, HardwareProfileArgsDict]]] = ..., host: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., host_group: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., identity: Optional[pulumi.Input[Union[VirtualMachineIdentityArgs, VirtualMachineIdentityArgsDict]]] = ..., license_type: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_profile: Optional[pulumi.Input[Union[NetworkProfileArgs, NetworkProfileArgsDict]]] = ..., os_profile: Optional[pulumi.Input[Union[OSProfileArgs, OSProfileArgsDict]]] = ..., placement: Optional[pulumi.Input[Union[PlacementArgs, PlacementArgsDict]]] = ..., plan: Optional[pulumi.Input[Union[PlanArgs, PlanArgsDict]]] = ..., platform_fault_domain: Optional[pulumi.Input[_builtins.int]] = ..., priority: Optional[pulumi.Input[Union[_builtins.str, VirtualMachinePriorityTypes]]] = ..., proximity_placement_group: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scheduled_events_policy: Optional[pulumi.Input[Union[ScheduledEventsPolicyArgs, ScheduledEventsPolicyArgsDict]]] = ..., scheduled_events_profile: Optional[pulumi.Input[Union[ScheduledEventsProfileArgs, ScheduledEventsProfileArgsDict]]] = ..., security_profile: Optional[pulumi.Input[Union[SecurityProfileArgs, SecurityProfileArgsDict]]] = ..., storage_profile: Optional[pulumi.Input[Union[StorageProfileArgs, StorageProfileArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., virtual_machine_scale_set: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., vm_name: Optional[pulumi.Input[_builtins.str]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VirtualMachineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> VirtualMachine:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(self) -> pulumi.Output[Optional[outputs.AdditionalCapabilitiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationProfile")
    def application_profile(self) -> pulumi.Output[Optional[outputs.ApplicationProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilitySet")
    def availability_set(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingProfile")
    def billing_profile(self) -> pulumi.Output[Optional[outputs.BillingProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityReservation")
    def capacity_reservation(self) -> pulumi.Output[Optional[outputs.CapacityReservationProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diagnosticsProfile")
    def diagnostics_profile(self) -> pulumi.Output[Optional[outputs.DiagnosticsProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionsTimeBudget")
    def extensions_time_budget(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> pulumi.Output[Optional[outputs.HardwareProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostGroup")
    def host_group(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.VirtualMachineIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> pulumi.Output[outputs.VirtualMachineInstanceViewResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional[outputs.NetworkProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> pulumi.Output[Optional[outputs.OSProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def placement(self) -> pulumi.Output[Optional[outputs.PlacementResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional[outputs.PlanResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformFaultDomain")
    def platform_fault_domain(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence[outputs.VirtualMachineExtensionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEventsPolicy")
    def scheduled_events_policy(self) -> pulumi.Output[Optional[outputs.ScheduledEventsPolicyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEventsProfile")
    def scheduled_events_profile(self) -> pulumi.Output[Optional[outputs.ScheduledEventsProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> pulumi.Output[Optional[outputs.SecurityProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Output[Optional[outputs.StorageProfileResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineScaleSet")
    def virtual_machine_scale_set(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    


