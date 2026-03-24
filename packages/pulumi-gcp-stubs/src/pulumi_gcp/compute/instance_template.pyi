

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceTemplateArgs', 'InstanceTemplate']
@pulumi.input_type
class InstanceTemplateArgs:
    def __init__(__self__, *, disks: pulumi.Input[Sequence[pulumi.Input[InstanceTemplateDiskArgs]]], machine_type: pulumi.Input[_builtins.str], advanced_machine_features: Optional[pulumi.Input[InstanceTemplateAdvancedMachineFeaturesArgs]] = ..., can_ip_forward: Optional[pulumi.Input[_builtins.bool]] = ..., confidential_instance_config: Optional[pulumi.Input[InstanceTemplateConfidentialInstanceConfigArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_display: Optional[pulumi.Input[_builtins.bool]] = ..., guest_accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateGuestAcceleratorArgs]]]] = ..., instance_description: Optional[pulumi.Input[_builtins.str]] = ..., key_revocation_action_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., metadata_startup_script: Optional[pulumi.Input[_builtins.str]] = ..., min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateNetworkInterfaceArgs]]]] = ..., network_performance_config: Optional[pulumi.Input[InstanceTemplateNetworkPerformanceConfigArgs]] = ..., partner_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reservation_affinity: Optional[pulumi.Input[InstanceTemplateReservationAffinityArgs]] = ..., resource_manager_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_policies: Optional[pulumi.Input[_builtins.str]] = ..., scheduling: Optional[pulumi.Input[InstanceTemplateSchedulingArgs]] = ..., service_account: Optional[pulumi.Input[InstanceTemplateServiceAccountArgs]] = ..., shielded_instance_config: Optional[pulumi.Input[InstanceTemplateShieldedInstanceConfigArgs]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> pulumi.Input[Sequence[pulumi.Input[InstanceTemplateDiskArgs]]]:
        
        ...
    
    @disks.setter
    def disks(self, value: pulumi.Input[Sequence[pulumi.Input[InstanceTemplateDiskArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @machine_type.setter
    def machine_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(self) -> Optional[pulumi.Input[InstanceTemplateAdvancedMachineFeaturesArgs]]:
        
        ...
    
    @advanced_machine_features.setter
    def advanced_machine_features(self, value: Optional[pulumi.Input[InstanceTemplateAdvancedMachineFeaturesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @can_ip_forward.setter
    def can_ip_forward(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(self) -> Optional[pulumi.Input[InstanceTemplateConfidentialInstanceConfigArgs]]:
        
        ...
    
    @confidential_instance_config.setter
    def confidential_instance_config(self, value: Optional[pulumi.Input[InstanceTemplateConfidentialInstanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDisplay")
    def enable_display(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_display.setter
    def enable_display(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateGuestAcceleratorArgs]]]]:
        
        ...
    
    @guest_accelerators.setter
    def guest_accelerators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateGuestAcceleratorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceDescription")
    def instance_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_description.setter
    def instance_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyRevocationActionType")
    def key_revocation_action_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_revocation_action_type.setter
    def key_revocation_action_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataStartupScript")
    def metadata_startup_script(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata_startup_script.setter
    def metadata_startup_script(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateNetworkInterfaceArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(self) -> Optional[pulumi.Input[InstanceTemplateNetworkPerformanceConfigArgs]]:
        
        ...
    
    @network_performance_config.setter
    def network_performance_config(self, value: Optional[pulumi.Input[InstanceTemplateNetworkPerformanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerMetadata")
    def partner_metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @partner_metadata.setter
    def partner_metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(self) -> Optional[pulumi.Input[InstanceTemplateReservationAffinityArgs]]:
        
        ...
    
    @reservation_affinity.setter
    def reservation_affinity(self, value: Optional[pulumi.Input[InstanceTemplateReservationAffinityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_manager_tags.setter
    def resource_manager_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_policies.setter
    def resource_policies(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheduling(self) -> Optional[pulumi.Input[InstanceTemplateSchedulingArgs]]:
        
        ...
    
    @scheduling.setter
    def scheduling(self, value: Optional[pulumi.Input[InstanceTemplateSchedulingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[InstanceTemplateServiceAccountArgs]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[InstanceTemplateServiceAccountArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(self) -> Optional[pulumi.Input[InstanceTemplateShieldedInstanceConfigArgs]]:
        
        ...
    
    @shielded_instance_config.setter
    def shielded_instance_config(self, value: Optional[pulumi.Input[InstanceTemplateShieldedInstanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceTemplateState:
    def __init__(__self__, *, advanced_machine_features: Optional[pulumi.Input[InstanceTemplateAdvancedMachineFeaturesArgs]] = ..., can_ip_forward: Optional[pulumi.Input[_builtins.bool]] = ..., confidential_instance_config: Optional[pulumi.Input[InstanceTemplateConfidentialInstanceConfigArgs]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disks: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateDiskArgs]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_display: Optional[pulumi.Input[_builtins.bool]] = ..., guest_accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateGuestAcceleratorArgs]]]] = ..., instance_description: Optional[pulumi.Input[_builtins.str]] = ..., key_revocation_action_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., metadata_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., metadata_startup_script: Optional[pulumi.Input[_builtins.str]] = ..., min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateNetworkInterfaceArgs]]]] = ..., network_performance_config: Optional[pulumi.Input[InstanceTemplateNetworkPerformanceConfigArgs]] = ..., numeric_id: Optional[pulumi.Input[_builtins.str]] = ..., partner_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reservation_affinity: Optional[pulumi.Input[InstanceTemplateReservationAffinityArgs]] = ..., resource_manager_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_policies: Optional[pulumi.Input[_builtins.str]] = ..., scheduling: Optional[pulumi.Input[InstanceTemplateSchedulingArgs]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., self_link_unique: Optional[pulumi.Input[_builtins.str]] = ..., service_account: Optional[pulumi.Input[InstanceTemplateServiceAccountArgs]] = ..., shielded_instance_config: Optional[pulumi.Input[InstanceTemplateShieldedInstanceConfigArgs]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(self) -> Optional[pulumi.Input[InstanceTemplateAdvancedMachineFeaturesArgs]]:
        
        ...
    
    @advanced_machine_features.setter
    def advanced_machine_features(self, value: Optional[pulumi.Input[InstanceTemplateAdvancedMachineFeaturesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @can_ip_forward.setter
    def can_ip_forward(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(self) -> Optional[pulumi.Input[InstanceTemplateConfidentialInstanceConfigArgs]]:
        
        ...
    
    @confidential_instance_config.setter
    def confidential_instance_config(self, value: Optional[pulumi.Input[InstanceTemplateConfidentialInstanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateDiskArgs]]]]:
        
        ...
    
    @disks.setter
    def disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateDiskArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDisplay")
    def enable_display(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_display.setter
    def enable_display(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateGuestAcceleratorArgs]]]]:
        
        ...
    
    @guest_accelerators.setter
    def guest_accelerators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateGuestAcceleratorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceDescription")
    def instance_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_description.setter
    def instance_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyRevocationActionType")
    def key_revocation_action_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_revocation_action_type.setter
    def key_revocation_action_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataFingerprint")
    def metadata_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata_fingerprint.setter
    def metadata_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataStartupScript")
    def metadata_startup_script(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata_startup_script.setter
    def metadata_startup_script(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateNetworkInterfaceArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceTemplateNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(self) -> Optional[pulumi.Input[InstanceTemplateNetworkPerformanceConfigArgs]]:
        
        ...
    
    @network_performance_config.setter
    def network_performance_config(self, value: Optional[pulumi.Input[InstanceTemplateNetworkPerformanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numericId")
    def numeric_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @numeric_id.setter
    def numeric_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerMetadata")
    def partner_metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @partner_metadata.setter
    def partner_metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(self) -> Optional[pulumi.Input[InstanceTemplateReservationAffinityArgs]]:
        
        ...
    
    @reservation_affinity.setter
    def reservation_affinity(self, value: Optional[pulumi.Input[InstanceTemplateReservationAffinityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_manager_tags.setter
    def resource_manager_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_policies.setter
    def resource_policies(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheduling(self) -> Optional[pulumi.Input[InstanceTemplateSchedulingArgs]]:
        
        ...
    
    @scheduling.setter
    def scheduling(self, value: Optional[pulumi.Input[InstanceTemplateSchedulingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLinkUnique")
    def self_link_unique(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link_unique.setter
    def self_link_unique(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[InstanceTemplateServiceAccountArgs]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[InstanceTemplateServiceAccountArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(self) -> Optional[pulumi.Input[InstanceTemplateShieldedInstanceConfigArgs]]:
        
        ...
    
    @shielded_instance_config.setter
    def shielded_instance_config(self, value: Optional[pulumi.Input[InstanceTemplateShieldedInstanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsFingerprint")
    def tags_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tags_fingerprint.setter
    def tags_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/instanceTemplate:InstanceTemplate")
class InstanceTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., advanced_machine_features: Optional[pulumi.Input[Union[InstanceTemplateAdvancedMachineFeaturesArgs, InstanceTemplateAdvancedMachineFeaturesArgsDict]]] = ..., can_ip_forward: Optional[pulumi.Input[_builtins.bool]] = ..., confidential_instance_config: Optional[pulumi.Input[Union[InstanceTemplateConfidentialInstanceConfigArgs, InstanceTemplateConfidentialInstanceConfigArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceTemplateDiskArgs, InstanceTemplateDiskArgsDict]]]]] = ..., enable_display: Optional[pulumi.Input[_builtins.bool]] = ..., guest_accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceTemplateGuestAcceleratorArgs, InstanceTemplateGuestAcceleratorArgsDict]]]]] = ..., instance_description: Optional[pulumi.Input[_builtins.str]] = ..., key_revocation_action_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., metadata_startup_script: Optional[pulumi.Input[_builtins.str]] = ..., min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceTemplateNetworkInterfaceArgs, InstanceTemplateNetworkInterfaceArgsDict]]]]] = ..., network_performance_config: Optional[pulumi.Input[Union[InstanceTemplateNetworkPerformanceConfigArgs, InstanceTemplateNetworkPerformanceConfigArgsDict]]] = ..., partner_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reservation_affinity: Optional[pulumi.Input[Union[InstanceTemplateReservationAffinityArgs, InstanceTemplateReservationAffinityArgsDict]]] = ..., resource_manager_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_policies: Optional[pulumi.Input[_builtins.str]] = ..., scheduling: Optional[pulumi.Input[Union[InstanceTemplateSchedulingArgs, InstanceTemplateSchedulingArgsDict]]] = ..., service_account: Optional[pulumi.Input[Union[InstanceTemplateServiceAccountArgs, InstanceTemplateServiceAccountArgsDict]]] = ..., shielded_instance_config: Optional[pulumi.Input[Union[InstanceTemplateShieldedInstanceConfigArgs, InstanceTemplateShieldedInstanceConfigArgsDict]]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceTemplateArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., advanced_machine_features: Optional[pulumi.Input[Union[InstanceTemplateAdvancedMachineFeaturesArgs, InstanceTemplateAdvancedMachineFeaturesArgsDict]]] = ..., can_ip_forward: Optional[pulumi.Input[_builtins.bool]] = ..., confidential_instance_config: Optional[pulumi.Input[Union[InstanceTemplateConfidentialInstanceConfigArgs, InstanceTemplateConfidentialInstanceConfigArgsDict]]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceTemplateDiskArgs, InstanceTemplateDiskArgsDict]]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., enable_display: Optional[pulumi.Input[_builtins.bool]] = ..., guest_accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceTemplateGuestAcceleratorArgs, InstanceTemplateGuestAcceleratorArgsDict]]]]] = ..., instance_description: Optional[pulumi.Input[_builtins.str]] = ..., key_revocation_action_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., metadata_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., metadata_startup_script: Optional[pulumi.Input[_builtins.str]] = ..., min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[InstanceTemplateNetworkInterfaceArgs, InstanceTemplateNetworkInterfaceArgsDict]]]]] = ..., network_performance_config: Optional[pulumi.Input[Union[InstanceTemplateNetworkPerformanceConfigArgs, InstanceTemplateNetworkPerformanceConfigArgsDict]]] = ..., numeric_id: Optional[pulumi.Input[_builtins.str]] = ..., partner_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reservation_affinity: Optional[pulumi.Input[Union[InstanceTemplateReservationAffinityArgs, InstanceTemplateReservationAffinityArgsDict]]] = ..., resource_manager_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_policies: Optional[pulumi.Input[_builtins.str]] = ..., scheduling: Optional[pulumi.Input[Union[InstanceTemplateSchedulingArgs, InstanceTemplateSchedulingArgsDict]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., self_link_unique: Optional[pulumi.Input[_builtins.str]] = ..., service_account: Optional[pulumi.Input[Union[InstanceTemplateServiceAccountArgs, InstanceTemplateServiceAccountArgsDict]]] = ..., shielded_instance_config: Optional[pulumi.Input[Union[InstanceTemplateShieldedInstanceConfigArgs, InstanceTemplateShieldedInstanceConfigArgsDict]]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...) -> InstanceTemplate:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(self) -> pulumi.Output[Optional[outputs.InstanceTemplateAdvancedMachineFeatures]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(self) -> pulumi.Output[outputs.InstanceTemplateConfidentialInstanceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> pulumi.Output[Sequence[outputs.InstanceTemplateDisk]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDisplay")
    def enable_display(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(self) -> pulumi.Output[Optional[Sequence[outputs.InstanceTemplateGuestAccelerator]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceDescription")
    def instance_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyRevocationActionType")
    def key_revocation_action_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataFingerprint")
    def metadata_fingerprint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataStartupScript")
    def metadata_startup_script(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Optional[Sequence[outputs.InstanceTemplateNetworkInterface]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(self) -> pulumi.Output[Optional[outputs.InstanceTemplateNetworkPerformanceConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numericId")
    def numeric_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerMetadata")
    def partner_metadata(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(self) -> pulumi.Output[Optional[outputs.InstanceTemplateReservationAffinity]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceManagerTags")
    def resource_manager_tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheduling(self) -> pulumi.Output[outputs.InstanceTemplateScheduling]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLinkUnique")
    def self_link_unique(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[Optional[outputs.InstanceTemplateServiceAccount]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(self) -> pulumi.Output[outputs.InstanceTemplateShieldedInstanceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsFingerprint")
    def tags_fingerprint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


