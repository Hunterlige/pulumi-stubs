import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "InstanceGceSetupArgs",
    "InstanceGceSetupArgsDict",
    "InstanceGceSetupAcceleratorConfigArgs",
    "InstanceGceSetupAcceleratorConfigArgsDict",
    "InstanceGceSetupBootDiskArgs",
    "InstanceGceSetupBootDiskArgsDict",
    "InstanceGceSetupConfidentialInstanceConfigArgs",
    "InstanceGceSetupConfidentialInstanceConfigArgsDict",
    "InstanceGceSetupContainerImageArgs",
    "InstanceGceSetupContainerImageArgsDict",
    "InstanceGceSetupDataDisksArgs",
    "InstanceGceSetupDataDisksArgsDict",
    "InstanceGceSetupNetworkInterfaceArgs",
    "InstanceGceSetupNetworkInterfaceArgsDict",
    "InstanceGceSetupNetworkInterfaceAccessConfigArgs",
    ...,
    "InstanceGceSetupReservationAffinityArgs",
    "InstanceGceSetupReservationAffinityArgsDict",
    "InstanceGceSetupServiceAccountArgs",
    "InstanceGceSetupServiceAccountArgsDict",
    "InstanceGceSetupShieldedInstanceConfigArgs",
    "InstanceGceSetupShieldedInstanceConfigArgsDict",
    "InstanceGceSetupVmImageArgs",
    "InstanceGceSetupVmImageArgsDict",
    "InstanceHealthInfoArgs",
    "InstanceHealthInfoArgsDict",
    "InstanceIamBindingConditionArgs",
    "InstanceIamBindingConditionArgsDict",
    "InstanceIamMemberConditionArgs",
    "InstanceIamMemberConditionArgsDict",
    "InstanceUpgradeHistoryArgs",
    "InstanceUpgradeHistoryArgsDict",
]

class InstanceGceSetupArgsDict(TypedDict):
    accelerator_configs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InstanceGceSetupAcceleratorConfigArgsDict]]]
    ]
    boot_disk: NotRequired[pulumi.Input[InstanceGceSetupBootDiskArgsDict]]
    confidential_instance_config: NotRequired[
        pulumi.Input[InstanceGceSetupConfidentialInstanceConfigArgsDict]
    ]
    container_image: NotRequired[pulumi.Input[InstanceGceSetupContainerImageArgsDict]]
    data_disks: NotRequired[pulumi.Input[InstanceGceSetupDataDisksArgsDict]]
    disable_public_ip: NotRequired[pulumi.Input[_builtins.bool]]
    enable_ip_forwarding: NotRequired[pulumi.Input[_builtins.bool]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    network_interfaces: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InstanceGceSetupNetworkInterfaceArgsDict]]]
    ]
    reservation_affinity: NotRequired[
        pulumi.Input[InstanceGceSetupReservationAffinityArgsDict]
    ]
    service_accounts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InstanceGceSetupServiceAccountArgsDict]]]
    ]
    shielded_instance_config: NotRequired[
        pulumi.Input[InstanceGceSetupShieldedInstanceConfigArgsDict]
    ]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vm_image: NotRequired[pulumi.Input[InstanceGceSetupVmImageArgsDict]]
    ...

@pulumi.input_type
class InstanceGceSetupArgs:
    def __init__(
        __self__,
        *,
        accelerator_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGceSetupAcceleratorConfigArgs]]]
        ] = ...,
        boot_disk: Optional[pulumi.Input[InstanceGceSetupBootDiskArgs]] = ...,
        confidential_instance_config: Optional[
            pulumi.Input[InstanceGceSetupConfidentialInstanceConfigArgs]
        ] = ...,
        container_image: Optional[
            pulumi.Input[InstanceGceSetupContainerImageArgs]
        ] = ...,
        data_disks: Optional[pulumi.Input[InstanceGceSetupDataDisksArgs]] = ...,
        disable_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_ip_forwarding: Optional[pulumi.Input[_builtins.bool]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        network_interfaces: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGceSetupNetworkInterfaceArgs]]]
        ] = ...,
        reservation_affinity: Optional[
            pulumi.Input[InstanceGceSetupReservationAffinityArgs]
        ] = ...,
        service_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGceSetupServiceAccountArgs]]]
        ] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[InstanceGceSetupShieldedInstanceConfigArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        vm_image: Optional[pulumi.Input[InstanceGceSetupVmImageArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorConfigs")
    def accelerator_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGceSetupAcceleratorConfigArgs]]]
    ]: ...
    @accelerator_configs.setter
    def accelerator_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGceSetupAcceleratorConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> Optional[pulumi.Input[InstanceGceSetupBootDiskArgs]]: ...
    @boot_disk.setter
    def boot_disk(
        self, value: Optional[pulumi.Input[InstanceGceSetupBootDiskArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(
        self,
    ) -> Optional[pulumi.Input[InstanceGceSetupConfidentialInstanceConfigArgs]]: ...
    @confidential_instance_config.setter
    def confidential_instance_config(
        self,
        value: Optional[pulumi.Input[InstanceGceSetupConfidentialInstanceConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(
        self,
    ) -> Optional[pulumi.Input[InstanceGceSetupContainerImageArgs]]: ...
    @container_image.setter
    def container_image(
        self, value: Optional[pulumi.Input[InstanceGceSetupContainerImageArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> Optional[pulumi.Input[InstanceGceSetupDataDisksArgs]]: ...
    @data_disks.setter
    def data_disks(
        self, value: Optional[pulumi.Input[InstanceGceSetupDataDisksArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disablePublicIp")
    def disable_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_public_ip.setter
    def disable_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableIpForwarding")
    def enable_ip_forwarding(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ip_forwarding.setter
    def enable_ip_forwarding(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGceSetupNetworkInterfaceArgs]]]
    ]: ...
    @network_interfaces.setter
    def network_interfaces(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGceSetupNetworkInterfaceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[pulumi.Input[InstanceGceSetupReservationAffinityArgs]]: ...
    @reservation_affinity.setter
    def reservation_affinity(
        self, value: Optional[pulumi.Input[InstanceGceSetupReservationAffinityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccounts")
    def service_accounts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGceSetupServiceAccountArgs]]]
    ]: ...
    @service_accounts.setter
    def service_accounts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGceSetupServiceAccountArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[pulumi.Input[InstanceGceSetupShieldedInstanceConfigArgs]]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self, value: Optional[pulumi.Input[InstanceGceSetupShieldedInstanceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> Optional[pulumi.Input[InstanceGceSetupVmImageArgs]]: ...
    @vm_image.setter
    def vm_image(self, value: Optional[pulumi.Input[InstanceGceSetupVmImageArgs]]): ...

class InstanceGceSetupAcceleratorConfigArgsDict(TypedDict):
    core_count: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceGceSetupAcceleratorConfigArgs:
    def __init__(
        __self__,
        *,
        core_count: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @core_count.setter
    def core_count(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceGceSetupBootDiskArgsDict(TypedDict):
    disk_encryption: NotRequired[pulumi.Input[_builtins.str]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.str]]
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceGceSetupBootDiskArgs:
    def __init__(
        __self__,
        *,
        disk_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryption")
    def disk_encryption(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption.setter
    def disk_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceGceSetupConfidentialInstanceConfigArgsDict(TypedDict):
    confidential_instance_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceGceSetupConfidentialInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        confidential_instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @confidential_instance_type.setter
    def confidential_instance_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class InstanceGceSetupContainerImageArgsDict(TypedDict):
    repository: pulumi.Input[_builtins.str]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceGceSetupContainerImageArgs:
    def __init__(
        __self__,
        *,
        repository: pulumi.Input[_builtins.str],
        tag: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Input[_builtins.str]: ...
    @repository.setter
    def repository(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceGceSetupDataDisksArgsDict(TypedDict):
    disk_encryption: NotRequired[pulumi.Input[_builtins.str]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.str]]
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceGceSetupDataDisksArgs:
    def __init__(
        __self__,
        *,
        disk_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryption")
    def disk_encryption(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption.setter
    def disk_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceGceSetupNetworkInterfaceArgsDict(TypedDict):
    access_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceGceSetupNetworkInterfaceAccessConfigArgsDict]]
        ]
    ]
    network: NotRequired[pulumi.Input[_builtins.str]]
    nic_type: NotRequired[pulumi.Input[_builtins.str]]
    subnet: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceGceSetupNetworkInterfaceArgs:
    def __init__(
        __self__,
        *,
        access_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceGceSetupNetworkInterfaceAccessConfigArgs]]
            ]
        ] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        nic_type: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfigs")
    def access_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceGceSetupNetworkInterfaceAccessConfigArgs]]
        ]
    ]: ...
    @access_configs.setter
    def access_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceGceSetupNetworkInterfaceAccessConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nic_type.setter
    def nic_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceGceSetupNetworkInterfaceAccessConfigArgsDict(TypedDict):
    external_ip: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceGceSetupNetworkInterfaceAccessConfigArgs:
    def __init__(__self__, *, external_ip: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalIp")
    def external_ip(self) -> pulumi.Input[_builtins.str]: ...
    @external_ip.setter
    def external_ip(self, value: pulumi.Input[_builtins.str]): ...

class InstanceGceSetupReservationAffinityArgsDict(TypedDict):
    consume_reservation_type: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class InstanceGceSetupReservationAffinityArgs:
    def __init__(
        __self__,
        *,
        consume_reservation_type: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consume_reservation_type.setter
    def consume_reservation_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class InstanceGceSetupServiceAccountArgsDict(TypedDict):
    email: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class InstanceGceSetupServiceAccountArgs:
    def __init__(
        __self__,
        *,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class InstanceGceSetupShieldedInstanceConfigArgsDict(TypedDict):
    enable_integrity_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    enable_secure_boot: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vtpm: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class InstanceGceSetupShieldedInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_secure_boot: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_vtpm: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_secure_boot.setter
    def enable_secure_boot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableVtpm")
    def enable_vtpm(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_vtpm.setter
    def enable_vtpm(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class InstanceGceSetupVmImageArgsDict(TypedDict):
    family: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    project: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceGceSetupVmImageArgs:
    def __init__(
        __self__,
        *,
        family: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceHealthInfoArgsDict(TypedDict): ...

@pulumi.input_type
class InstanceHealthInfoArgs:
    def __init__(__self__) -> None: ...

class InstanceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceUpgradeHistoryArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[_builtins.str]]
    container_image: NotRequired[pulumi.Input[_builtins.str]]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    framework: NotRequired[pulumi.Input[_builtins.str]]
    snapshot: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    target_version: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]
    vm_image: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceUpgradeHistoryArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        container_image: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        framework: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        target_version: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_image.setter
    def container_image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def framework(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @framework.setter
    def framework(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def snapshot(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot.setter
    def snapshot(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVersion")
    def target_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_version.setter
    def target_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_image.setter
    def vm_image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
