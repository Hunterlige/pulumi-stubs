import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "InstanceGceSetup",
    "InstanceGceSetupAcceleratorConfig",
    "InstanceGceSetupBootDisk",
    "InstanceGceSetupConfidentialInstanceConfig",
    "InstanceGceSetupContainerImage",
    "InstanceGceSetupDataDisks",
    "InstanceGceSetupNetworkInterface",
    "InstanceGceSetupNetworkInterfaceAccessConfig",
    "InstanceGceSetupReservationAffinity",
    "InstanceGceSetupServiceAccount",
    "InstanceGceSetupShieldedInstanceConfig",
    "InstanceGceSetupVmImage",
    "InstanceHealthInfo",
    "InstanceIamBindingCondition",
    "InstanceIamMemberCondition",
    "InstanceUpgradeHistory",
]

@pulumi.output_type
class InstanceGceSetup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        accelerator_configs: Optional[
            Sequence[outputs.InstanceGceSetupAcceleratorConfig]
        ] = ...,
        boot_disk: Optional[outputs.InstanceGceSetupBootDisk] = ...,
        confidential_instance_config: Optional[
            outputs.InstanceGceSetupConfidentialInstanceConfig
        ] = ...,
        container_image: Optional[outputs.InstanceGceSetupContainerImage] = ...,
        data_disks: Optional[outputs.InstanceGceSetupDataDisks] = ...,
        disable_public_ip: Optional[_builtins.bool] = ...,
        enable_ip_forwarding: Optional[_builtins.bool] = ...,
        machine_type: Optional[_builtins.str] = ...,
        metadata: Optional[Mapping[str, _builtins.str]] = ...,
        network_interfaces: Optional[
            Sequence[outputs.InstanceGceSetupNetworkInterface]
        ] = ...,
        reservation_affinity: Optional[
            outputs.InstanceGceSetupReservationAffinity
        ] = ...,
        service_accounts: Optional[
            Sequence[outputs.InstanceGceSetupServiceAccount]
        ] = ...,
        shielded_instance_config: Optional[
            outputs.InstanceGceSetupShieldedInstanceConfig
        ] = ...,
        tags: Optional[Sequence[_builtins.str]] = ...,
        vm_image: Optional[outputs.InstanceGceSetupVmImage] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorConfigs")
    def accelerator_configs(
        self,
    ) -> Optional[Sequence[outputs.InstanceGceSetupAcceleratorConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="bootDisk")
    def boot_disk(self) -> Optional[outputs.InstanceGceSetupBootDisk]: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(
        self,
    ) -> Optional[outputs.InstanceGceSetupConfidentialInstanceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[outputs.InstanceGceSetupContainerImage]: ...
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> Optional[outputs.InstanceGceSetupDataDisks]: ...
    @_builtins.property
    @pulumi.getter(name="disablePublicIp")
    def disable_public_ip(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableIpForwarding")
    def enable_ip_forwarding(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Optional[Sequence[outputs.InstanceGceSetupNetworkInterface]]: ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[outputs.InstanceGceSetupReservationAffinity]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccounts")
    def service_accounts(
        self,
    ) -> Optional[Sequence[outputs.InstanceGceSetupServiceAccount]]: ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[outputs.InstanceGceSetupShieldedInstanceConfig]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> Optional[outputs.InstanceGceSetupVmImage]: ...

@pulumi.output_type
class InstanceGceSetupAcceleratorConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        core_count: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceGceSetupBootDisk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_encryption: Optional[_builtins.str] = ...,
        disk_size_gb: Optional[_builtins.str] = ...,
        disk_type: Optional[_builtins.str] = ...,
        kms_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryption")
    def disk_encryption(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceGceSetupConfidentialInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, confidential_instance_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceType")
    def confidential_instance_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceGceSetupContainerImage(dict):
    def __init__(
        __self__, *, repository: _builtins.str, tag: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceGceSetupDataDisks(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_encryption: Optional[_builtins.str] = ...,
        disk_size_gb: Optional[_builtins.str] = ...,
        disk_type: Optional[_builtins.str] = ...,
        kms_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryption")
    def disk_encryption(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceGceSetupNetworkInterface(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_configs: Optional[
            Sequence[outputs.InstanceGceSetupNetworkInterfaceAccessConfig]
        ] = ...,
        network: Optional[_builtins.str] = ...,
        nic_type: Optional[_builtins.str] = ...,
        subnet: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfigs")
    def access_configs(
        self,
    ) -> Optional[Sequence[outputs.InstanceGceSetupNetworkInterfaceAccessConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceGceSetupNetworkInterfaceAccessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, external_ip: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalIp")
    def external_ip(self) -> _builtins.str: ...

@pulumi.output_type
class InstanceGceSetupReservationAffinity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consume_reservation_type: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class InstanceGceSetupServiceAccount(dict):
    def __init__(
        __self__,
        *,
        email: Optional[_builtins.str] = ...,
        scopes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class InstanceGceSetupShieldedInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_integrity_monitoring: Optional[_builtins.bool] = ...,
        enable_secure_boot: Optional[_builtins.bool] = ...,
        enable_vtpm: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableVtpm")
    def enable_vtpm(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class InstanceGceSetupVmImage(dict):
    def __init__(
        __self__,
        *,
        family: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        project: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceHealthInfo(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class InstanceIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceUpgradeHistory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: Optional[_builtins.str] = ...,
        container_image: Optional[_builtins.str] = ...,
        create_time: Optional[_builtins.str] = ...,
        framework: Optional[_builtins.str] = ...,
        snapshot: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        target_version: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
        vm_image: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def framework(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def snapshot(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetVersion")
    def target_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> Optional[_builtins.str]: ...
