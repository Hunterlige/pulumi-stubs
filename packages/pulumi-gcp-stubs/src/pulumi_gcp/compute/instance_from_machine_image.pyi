import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InstanceFromMachineImageArgs", "InstanceFromMachineImage"]

@pulumi.input_type
class InstanceFromMachineImageArgs:
    def __init__(
        __self__,
        *,
        source_machine_image: pulumi.Input[_builtins.str],
        advanced_machine_features: Optional[
            pulumi.Input[InstanceFromMachineImageAdvancedMachineFeaturesArgs]
        ] = ...,
        allow_stopping_for_update: Optional[pulumi.Input[_builtins.bool]] = ...,
        can_ip_forward: Optional[pulumi.Input[_builtins.bool]] = ...,
        confidential_instance_config: Optional[
            pulumi.Input[InstanceFromMachineImageConfidentialInstanceConfigArgs]
        ] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_status: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_display: Optional[pulumi.Input[_builtins.bool]] = ...,
        guest_accelerators: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFromMachineImageGuestAcceleratorArgs]]
            ]
        ] = ...,
        hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_encryption_key: Optional[
            pulumi.Input[InstanceFromMachineImageInstanceEncryptionKeyArgs]
        ] = ...,
        key_revocation_action_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        metadata_startup_script: Optional[pulumi.Input[_builtins.str]] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interfaces: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFromMachineImageNetworkInterfaceArgs]]
            ]
        ] = ...,
        network_performance_config: Optional[
            pulumi.Input[InstanceFromMachineImageNetworkPerformanceConfigArgs]
        ] = ...,
        params: Optional[pulumi.Input[InstanceFromMachineImageParamsArgs]] = ...,
        partner_metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_affinity: Optional[
            pulumi.Input[InstanceFromMachineImageReservationAffinityArgs]
        ] = ...,
        resource_policies: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduling: Optional[
            pulumi.Input[InstanceFromMachineImageSchedulingArgs]
        ] = ...,
        service_account: Optional[
            pulumi.Input[InstanceFromMachineImageServiceAccountArgs]
        ] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[InstanceFromMachineImageShieldedInstanceConfigArgs]
        ] = ...,
        source_machine_image_encryption_key: Optional[
            pulumi.Input[InstanceFromMachineImageSourceMachineImageEncryptionKeyArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceMachineImage")
    def source_machine_image(self) -> pulumi.Input[_builtins.str]: ...
    @source_machine_image.setter
    def source_machine_image(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> Optional[
        pulumi.Input[InstanceFromMachineImageAdvancedMachineFeaturesArgs]
    ]: ...
    @advanced_machine_features.setter
    def advanced_machine_features(
        self,
        value: Optional[
            pulumi.Input[InstanceFromMachineImageAdvancedMachineFeaturesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowStoppingForUpdate")
    def allow_stopping_for_update(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_stopping_for_update.setter
    def allow_stopping_for_update(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @can_ip_forward.setter
    def can_ip_forward(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(
        self,
    ) -> Optional[
        pulumi.Input[InstanceFromMachineImageConfidentialInstanceConfigArgs]
    ]: ...
    @confidential_instance_config.setter
    def confidential_instance_config(
        self,
        value: Optional[
            pulumi.Input[InstanceFromMachineImageConfidentialInstanceConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredStatus")
    def desired_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_status.setter
    def desired_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableDisplay")
    def enable_display(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_display.setter
    def enable_display(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceFromMachineImageGuestAcceleratorArgs]]
        ]
    ]: ...
    @guest_accelerators.setter
    def guest_accelerators(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFromMachineImageGuestAcceleratorArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceEncryptionKey")
    def instance_encryption_key(
        self,
    ) -> Optional[pulumi.Input[InstanceFromMachineImageInstanceEncryptionKeyArgs]]: ...
    @instance_encryption_key.setter
    def instance_encryption_key(
        self,
        value: Optional[
            pulumi.Input[InstanceFromMachineImageInstanceEncryptionKeyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyRevocationActionType")
    def key_revocation_action_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_revocation_action_type.setter
    def key_revocation_action_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metadataStartupScript")
    def metadata_startup_script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metadata_startup_script.setter
    def metadata_startup_script(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceFromMachineImageNetworkInterfaceArgs]]
        ]
    ]: ...
    @network_interfaces.setter
    def network_interfaces(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFromMachineImageNetworkInterfaceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(
        self,
    ) -> Optional[
        pulumi.Input[InstanceFromMachineImageNetworkPerformanceConfigArgs]
    ]: ...
    @network_performance_config.setter
    def network_performance_config(
        self,
        value: Optional[
            pulumi.Input[InstanceFromMachineImageNetworkPerformanceConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[InstanceFromMachineImageParamsArgs]]: ...
    @params.setter
    def params(
        self, value: Optional[pulumi.Input[InstanceFromMachineImageParamsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="partnerMetadata")
    def partner_metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @partner_metadata.setter
    def partner_metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[pulumi.Input[InstanceFromMachineImageReservationAffinityArgs]]: ...
    @reservation_affinity.setter
    def reservation_affinity(
        self,
        value: Optional[pulumi.Input[InstanceFromMachineImageReservationAffinityArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_policies.setter
    def resource_policies(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scheduling(
        self,
    ) -> Optional[pulumi.Input[InstanceFromMachineImageSchedulingArgs]]: ...
    @scheduling.setter
    def scheduling(
        self, value: Optional[pulumi.Input[InstanceFromMachineImageSchedulingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(
        self,
    ) -> Optional[pulumi.Input[InstanceFromMachineImageServiceAccountArgs]]: ...
    @service_account.setter
    def service_account(
        self, value: Optional[pulumi.Input[InstanceFromMachineImageServiceAccountArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[pulumi.Input[InstanceFromMachineImageShieldedInstanceConfigArgs]]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self,
        value: Optional[
            pulumi.Input[InstanceFromMachineImageShieldedInstanceConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceMachineImageEncryptionKey")
    def source_machine_image_encryption_key(
        self,
    ) -> Optional[
        pulumi.Input[InstanceFromMachineImageSourceMachineImageEncryptionKeyArgs]
    ]: ...
    @source_machine_image_encryption_key.setter
    def source_machine_image_encryption_key(
        self,
        value: Optional[
            pulumi.Input[InstanceFromMachineImageSourceMachineImageEncryptionKeyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _InstanceFromMachineImageState:
    def __init__(
        __self__,
        *,
        advanced_machine_features: Optional[
            pulumi.Input[InstanceFromMachineImageAdvancedMachineFeaturesArgs]
        ] = ...,
        allow_stopping_for_update: Optional[pulumi.Input[_builtins.bool]] = ...,
        attached_disks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFromMachineImageAttachedDiskArgs]]
            ]
        ] = ...,
        boot_disks: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceFromMachineImageBootDiskArgs]]]
        ] = ...,
        can_ip_forward: Optional[pulumi.Input[_builtins.bool]] = ...,
        confidential_instance_config: Optional[
            pulumi.Input[InstanceFromMachineImageConfidentialInstanceConfigArgs]
        ] = ...,
        cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        current_status: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_status: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_display: Optional[pulumi.Input[_builtins.bool]] = ...,
        guest_accelerators: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFromMachineImageGuestAcceleratorArgs]]
            ]
        ] = ...,
        hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_encryption_key: Optional[
            pulumi.Input[InstanceFromMachineImageInstanceEncryptionKeyArgs]
        ] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_revocation_action_type: Optional[pulumi.Input[_builtins.str]] = ...,
        label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        metadata_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_startup_script: Optional[pulumi.Input[_builtins.str]] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interfaces: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFromMachineImageNetworkInterfaceArgs]]
            ]
        ] = ...,
        network_performance_config: Optional[
            pulumi.Input[InstanceFromMachineImageNetworkPerformanceConfigArgs]
        ] = ...,
        params: Optional[pulumi.Input[InstanceFromMachineImageParamsArgs]] = ...,
        partner_metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reservation_affinity: Optional[
            pulumi.Input[InstanceFromMachineImageReservationAffinityArgs]
        ] = ...,
        resource_policies: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduling: Optional[
            pulumi.Input[InstanceFromMachineImageSchedulingArgs]
        ] = ...,
        scratch_disks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFromMachineImageScratchDiskArgs]]
            ]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[
            pulumi.Input[InstanceFromMachineImageServiceAccountArgs]
        ] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[InstanceFromMachineImageShieldedInstanceConfigArgs]
        ] = ...,
        source_machine_image: Optional[pulumi.Input[_builtins.str]] = ...,
        source_machine_image_encryption_key: Optional[
            pulumi.Input[InstanceFromMachineImageSourceMachineImageEncryptionKeyArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> Optional[
        pulumi.Input[InstanceFromMachineImageAdvancedMachineFeaturesArgs]
    ]: ...
    @advanced_machine_features.setter
    def advanced_machine_features(
        self,
        value: Optional[
            pulumi.Input[InstanceFromMachineImageAdvancedMachineFeaturesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowStoppingForUpdate")
    def allow_stopping_for_update(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_stopping_for_update.setter
    def allow_stopping_for_update(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="attachedDisks")
    def attached_disks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceFromMachineImageAttachedDiskArgs]]]
    ]: ...
    @attached_disks.setter
    def attached_disks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFromMachineImageAttachedDiskArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bootDisks")
    def boot_disks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceFromMachineImageBootDiskArgs]]]
    ]: ...
    @boot_disks.setter
    def boot_disks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceFromMachineImageBootDiskArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @can_ip_forward.setter
    def can_ip_forward(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(
        self,
    ) -> Optional[
        pulumi.Input[InstanceFromMachineImageConfidentialInstanceConfigArgs]
    ]: ...
    @confidential_instance_config.setter
    def confidential_instance_config(
        self,
        value: Optional[
            pulumi.Input[InstanceFromMachineImageConfidentialInstanceConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cpuPlatform")
    def cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu_platform.setter
    def cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="currentStatus")
    def current_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @current_status.setter
    def current_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredStatus")
    def desired_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_status.setter
    def desired_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableDisplay")
    def enable_display(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_display.setter
    def enable_display(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceFromMachineImageGuestAcceleratorArgs]]
        ]
    ]: ...
    @guest_accelerators.setter
    def guest_accelerators(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFromMachineImageGuestAcceleratorArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceEncryptionKey")
    def instance_encryption_key(
        self,
    ) -> Optional[pulumi.Input[InstanceFromMachineImageInstanceEncryptionKeyArgs]]: ...
    @instance_encryption_key.setter
    def instance_encryption_key(
        self,
        value: Optional[
            pulumi.Input[InstanceFromMachineImageInstanceEncryptionKeyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyRevocationActionType")
    def key_revocation_action_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_revocation_action_type.setter
    def key_revocation_action_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label_fingerprint.setter
    def label_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metadataFingerprint")
    def metadata_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metadata_fingerprint.setter
    def metadata_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metadataStartupScript")
    def metadata_startup_script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metadata_startup_script.setter
    def metadata_startup_script(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_cpu_platform.setter
    def min_cpu_platform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceFromMachineImageNetworkInterfaceArgs]]
        ]
    ]: ...
    @network_interfaces.setter
    def network_interfaces(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFromMachineImageNetworkInterfaceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(
        self,
    ) -> Optional[
        pulumi.Input[InstanceFromMachineImageNetworkPerformanceConfigArgs]
    ]: ...
    @network_performance_config.setter
    def network_performance_config(
        self,
        value: Optional[
            pulumi.Input[InstanceFromMachineImageNetworkPerformanceConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[InstanceFromMachineImageParamsArgs]]: ...
    @params.setter
    def params(
        self, value: Optional[pulumi.Input[InstanceFromMachineImageParamsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="partnerMetadata")
    def partner_metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @partner_metadata.setter
    def partner_metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[pulumi.Input[InstanceFromMachineImageReservationAffinityArgs]]: ...
    @reservation_affinity.setter
    def reservation_affinity(
        self,
        value: Optional[pulumi.Input[InstanceFromMachineImageReservationAffinityArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_policies.setter
    def resource_policies(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scheduling(
        self,
    ) -> Optional[pulumi.Input[InstanceFromMachineImageSchedulingArgs]]: ...
    @scheduling.setter
    def scheduling(
        self, value: Optional[pulumi.Input[InstanceFromMachineImageSchedulingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scratchDisks")
    def scratch_disks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceFromMachineImageScratchDiskArgs]]]
    ]: ...
    @scratch_disks.setter
    def scratch_disks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceFromMachineImageScratchDiskArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(
        self,
    ) -> Optional[pulumi.Input[InstanceFromMachineImageServiceAccountArgs]]: ...
    @service_account.setter
    def service_account(
        self, value: Optional[pulumi.Input[InstanceFromMachineImageServiceAccountArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[pulumi.Input[InstanceFromMachineImageShieldedInstanceConfigArgs]]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self,
        value: Optional[
            pulumi.Input[InstanceFromMachineImageShieldedInstanceConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceMachineImage")
    def source_machine_image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_machine_image.setter
    def source_machine_image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceMachineImageEncryptionKey")
    def source_machine_image_encryption_key(
        self,
    ) -> Optional[
        pulumi.Input[InstanceFromMachineImageSourceMachineImageEncryptionKeyArgs]
    ]: ...
    @source_machine_image_encryption_key.setter
    def source_machine_image_encryption_key(
        self,
        value: Optional[
            pulumi.Input[InstanceFromMachineImageSourceMachineImageEncryptionKeyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsFingerprint")
    def tags_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tags_fingerprint.setter
    def tags_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class InstanceFromMachineImage(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        advanced_machine_features: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageAdvancedMachineFeaturesArgs,
                    InstanceFromMachineImageAdvancedMachineFeaturesArgsDict,
                ]
            ]
        ] = ...,
        allow_stopping_for_update: Optional[pulumi.Input[_builtins.bool]] = ...,
        can_ip_forward: Optional[pulumi.Input[_builtins.bool]] = ...,
        confidential_instance_config: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageConfidentialInstanceConfigArgs,
                    InstanceFromMachineImageConfidentialInstanceConfigArgsDict,
                ]
            ]
        ] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_status: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_display: Optional[pulumi.Input[_builtins.bool]] = ...,
        guest_accelerators: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceFromMachineImageGuestAcceleratorArgs,
                            InstanceFromMachineImageGuestAcceleratorArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_encryption_key: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageInstanceEncryptionKeyArgs,
                    InstanceFromMachineImageInstanceEncryptionKeyArgsDict,
                ]
            ]
        ] = ...,
        key_revocation_action_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        metadata_startup_script: Optional[pulumi.Input[_builtins.str]] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interfaces: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceFromMachineImageNetworkInterfaceArgs,
                            InstanceFromMachineImageNetworkInterfaceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        network_performance_config: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageNetworkPerformanceConfigArgs,
                    InstanceFromMachineImageNetworkPerformanceConfigArgsDict,
                ]
            ]
        ] = ...,
        params: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageParamsArgs,
                    InstanceFromMachineImageParamsArgsDict,
                ]
            ]
        ] = ...,
        partner_metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_affinity: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageReservationAffinityArgs,
                    InstanceFromMachineImageReservationAffinityArgsDict,
                ]
            ]
        ] = ...,
        resource_policies: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduling: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageSchedulingArgs,
                    InstanceFromMachineImageSchedulingArgsDict,
                ]
            ]
        ] = ...,
        service_account: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageServiceAccountArgs,
                    InstanceFromMachineImageServiceAccountArgsDict,
                ]
            ]
        ] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageShieldedInstanceConfigArgs,
                    InstanceFromMachineImageShieldedInstanceConfigArgsDict,
                ]
            ]
        ] = ...,
        source_machine_image: Optional[pulumi.Input[_builtins.str]] = ...,
        source_machine_image_encryption_key: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageSourceMachineImageEncryptionKeyArgs,
                    InstanceFromMachineImageSourceMachineImageEncryptionKeyArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InstanceFromMachineImageArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        advanced_machine_features: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageAdvancedMachineFeaturesArgs,
                    InstanceFromMachineImageAdvancedMachineFeaturesArgsDict,
                ]
            ]
        ] = ...,
        allow_stopping_for_update: Optional[pulumi.Input[_builtins.bool]] = ...,
        attached_disks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceFromMachineImageAttachedDiskArgs,
                            InstanceFromMachineImageAttachedDiskArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        boot_disks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceFromMachineImageBootDiskArgs,
                            InstanceFromMachineImageBootDiskArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        can_ip_forward: Optional[pulumi.Input[_builtins.bool]] = ...,
        confidential_instance_config: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageConfidentialInstanceConfigArgs,
                    InstanceFromMachineImageConfidentialInstanceConfigArgsDict,
                ]
            ]
        ] = ...,
        cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        current_status: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_status: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_display: Optional[pulumi.Input[_builtins.bool]] = ...,
        guest_accelerators: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceFromMachineImageGuestAcceleratorArgs,
                            InstanceFromMachineImageGuestAcceleratorArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_encryption_key: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageInstanceEncryptionKeyArgs,
                    InstanceFromMachineImageInstanceEncryptionKeyArgsDict,
                ]
            ]
        ] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_revocation_action_type: Optional[pulumi.Input[_builtins.str]] = ...,
        label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        metadata_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_startup_script: Optional[pulumi.Input[_builtins.str]] = ...,
        min_cpu_platform: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interfaces: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceFromMachineImageNetworkInterfaceArgs,
                            InstanceFromMachineImageNetworkInterfaceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        network_performance_config: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageNetworkPerformanceConfigArgs,
                    InstanceFromMachineImageNetworkPerformanceConfigArgsDict,
                ]
            ]
        ] = ...,
        params: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageParamsArgs,
                    InstanceFromMachineImageParamsArgsDict,
                ]
            ]
        ] = ...,
        partner_metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reservation_affinity: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageReservationAffinityArgs,
                    InstanceFromMachineImageReservationAffinityArgsDict,
                ]
            ]
        ] = ...,
        resource_policies: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduling: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageSchedulingArgs,
                    InstanceFromMachineImageSchedulingArgsDict,
                ]
            ]
        ] = ...,
        scratch_disks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceFromMachineImageScratchDiskArgs,
                            InstanceFromMachineImageScratchDiskArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageServiceAccountArgs,
                    InstanceFromMachineImageServiceAccountArgsDict,
                ]
            ]
        ] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageShieldedInstanceConfigArgs,
                    InstanceFromMachineImageShieldedInstanceConfigArgsDict,
                ]
            ]
        ] = ...,
        source_machine_image: Optional[pulumi.Input[_builtins.str]] = ...,
        source_machine_image_encryption_key: Optional[
            pulumi.Input[
                Union[
                    InstanceFromMachineImageSourceMachineImageEncryptionKeyArgs,
                    InstanceFromMachineImageSourceMachineImageEncryptionKeyArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        tags_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> InstanceFromMachineImage: ...
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(
        self,
    ) -> pulumi.Output[outputs.InstanceFromMachineImageAdvancedMachineFeatures]: ...
    @_builtins.property
    @pulumi.getter(name="allowStoppingForUpdate")
    def allow_stopping_for_update(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="attachedDisks")
    def attached_disks(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceFromMachineImageAttachedDisk]]: ...
    @_builtins.property
    @pulumi.getter(name="bootDisks")
    def boot_disks(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceFromMachineImageBootDisk]]: ...
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(
        self,
    ) -> pulumi.Output[outputs.InstanceFromMachineImageConfidentialInstanceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="cpuPlatform")
    def cpu_platform(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="currentStatus")
    def current_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="desiredStatus")
    def desired_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableDisplay")
    def enable_display(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="guestAccelerators")
    def guest_accelerators(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceFromMachineImageGuestAccelerator]]: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceEncryptionKey")
    def instance_encryption_key(
        self,
    ) -> pulumi.Output[outputs.InstanceFromMachineImageInstanceEncryptionKey]: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyRevocationActionType")
    def key_revocation_action_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="metadataFingerprint")
    def metadata_fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metadataStartupScript")
    def metadata_startup_script(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minCpuPlatform")
    def min_cpu_platform(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceFromMachineImageNetworkInterface]]: ...
    @_builtins.property
    @pulumi.getter(name="networkPerformanceConfig")
    def network_performance_config(
        self,
    ) -> pulumi.Output[outputs.InstanceFromMachineImageNetworkPerformanceConfig]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[outputs.InstanceFromMachineImageParams]: ...
    @_builtins.property
    @pulumi.getter(name="partnerMetadata")
    def partner_metadata(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> pulumi.Output[outputs.InstanceFromMachineImageReservationAffinity]: ...
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scheduling(
        self,
    ) -> pulumi.Output[outputs.InstanceFromMachineImageScheduling]: ...
    @_builtins.property
    @pulumi.getter(name="scratchDisks")
    def scratch_disks(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceFromMachineImageScratchDisk]]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(
        self,
    ) -> pulumi.Output[outputs.InstanceFromMachineImageServiceAccount]: ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> pulumi.Output[outputs.InstanceFromMachineImageShieldedInstanceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="sourceMachineImage")
    def source_machine_image(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceMachineImageEncryptionKey")
    def source_machine_image_encryption_key(
        self,
    ) -> pulumi.Output[
        Optional[outputs.InstanceFromMachineImageSourceMachineImageEncryptionKey]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsFingerprint")
    def tags_fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]: ...
