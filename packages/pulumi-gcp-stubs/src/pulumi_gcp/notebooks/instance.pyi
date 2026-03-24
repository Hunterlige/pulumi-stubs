import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InstanceArgs", "Instance"]

@pulumi.input_type
class InstanceArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        machine_type: pulumi.Input[_builtins.str],
        accelerator_config: Optional[pulumi.Input[InstanceAcceleratorConfigArgs]] = ...,
        boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        boot_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        container_image: Optional[pulumi.Input[InstanceContainerImageArgs]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_gpu_driver_path: Optional[pulumi.Input[_builtins.str]] = ...,
        data_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        data_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        install_gpu_driver: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        nic_type: Optional[pulumi.Input[_builtins.str]] = ...,
        no_proxy_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        no_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        no_remove_data_disk: Optional[pulumi.Input[_builtins.bool]] = ...,
        post_startup_script: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_affinity: Optional[
            pulumi.Input[InstanceReservationAffinityArgs]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[InstanceShieldedInstanceConfigArgs]
        ] = ...,
        subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image: Optional[pulumi.Input[InstanceVmImageArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Input[_builtins.str]: ...
    @machine_type.setter
    def machine_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorConfig")
    def accelerator_config(
        self,
    ) -> Optional[pulumi.Input[InstanceAcceleratorConfigArgs]]: ...
    @accelerator_config.setter
    def accelerator_config(
        self, value: Optional[pulumi.Input[InstanceAcceleratorConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_type.setter
    def boot_disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[pulumi.Input[InstanceContainerImageArgs]]: ...
    @container_image.setter
    def container_image(
        self, value: Optional[pulumi.Input[InstanceContainerImageArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customGpuDriverPath")
    def custom_gpu_driver_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_gpu_driver_path.setter
    def custom_gpu_driver_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataDiskSizeGb")
    def data_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_disk_size_gb.setter
    def data_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="dataDiskType")
    def data_disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_disk_type.setter
    def data_disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryption")
    def disk_encryption(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption.setter
    def disk_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="installGpuDriver")
    def install_gpu_driver(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @install_gpu_driver.setter
    def install_gpu_driver(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceOwners")
    def instance_owners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_owners.setter
    def instance_owners(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="noProxyAccess")
    def no_proxy_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_proxy_access.setter
    def no_proxy_access(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="noPublicIp")
    def no_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_public_ip.setter
    def no_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="noRemoveDataDisk")
    def no_remove_data_disk(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_remove_data_disk.setter
    def no_remove_data_disk(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="postStartupScript")
    def post_startup_script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @post_startup_script.setter
    def post_startup_script(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> Optional[pulumi.Input[InstanceReservationAffinityArgs]]: ...
    @reservation_affinity.setter
    def reservation_affinity(
        self, value: Optional[pulumi.Input[InstanceReservationAffinityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountScopes")
    def service_account_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @service_account_scopes.setter
    def service_account_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[pulumi.Input[InstanceShieldedInstanceConfigArgs]]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self, value: Optional[pulumi.Input[InstanceShieldedInstanceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> Optional[pulumi.Input[InstanceVmImageArgs]]: ...
    @vm_image.setter
    def vm_image(self, value: Optional[pulumi.Input[InstanceVmImageArgs]]): ...

@pulumi.input_type
class _InstanceState:
    def __init__(
        __self__,
        *,
        accelerator_config: Optional[pulumi.Input[InstanceAcceleratorConfigArgs]] = ...,
        boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        boot_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        container_image: Optional[pulumi.Input[InstanceContainerImageArgs]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_gpu_driver_path: Optional[pulumi.Input[_builtins.str]] = ...,
        data_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        data_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        install_gpu_driver: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        nic_type: Optional[pulumi.Input[_builtins.str]] = ...,
        no_proxy_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        no_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        no_remove_data_disk: Optional[pulumi.Input[_builtins.bool]] = ...,
        post_startup_script: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reservation_affinity: Optional[
            pulumi.Input[InstanceReservationAffinityArgs]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[InstanceShieldedInstanceConfigArgs]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image: Optional[pulumi.Input[InstanceVmImageArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorConfig")
    def accelerator_config(
        self,
    ) -> Optional[pulumi.Input[InstanceAcceleratorConfigArgs]]: ...
    @accelerator_config.setter
    def accelerator_config(
        self, value: Optional[pulumi.Input[InstanceAcceleratorConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @boot_disk_type.setter
    def boot_disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[pulumi.Input[InstanceContainerImageArgs]]: ...
    @container_image.setter
    def container_image(
        self, value: Optional[pulumi.Input[InstanceContainerImageArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customGpuDriverPath")
    def custom_gpu_driver_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_gpu_driver_path.setter
    def custom_gpu_driver_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataDiskSizeGb")
    def data_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_disk_size_gb.setter
    def data_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="dataDiskType")
    def data_disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_disk_type.setter
    def data_disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryption")
    def disk_encryption(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_encryption.setter
    def disk_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="installGpuDriver")
    def install_gpu_driver(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @install_gpu_driver.setter
    def install_gpu_driver(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceOwners")
    def instance_owners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instance_owners.setter
    def instance_owners(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="noProxyAccess")
    def no_proxy_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_proxy_access.setter
    def no_proxy_access(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="noPublicIp")
    def no_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_public_ip.setter
    def no_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="noRemoveDataDisk")
    def no_remove_data_disk(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @no_remove_data_disk.setter
    def no_remove_data_disk(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="postStartupScript")
    def post_startup_script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @post_startup_script.setter
    def post_startup_script(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="proxyUri")
    def proxy_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @proxy_uri.setter
    def proxy_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    ) -> Optional[pulumi.Input[InstanceReservationAffinityArgs]]: ...
    @reservation_affinity.setter
    def reservation_affinity(
        self, value: Optional[pulumi.Input[InstanceReservationAffinityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountScopes")
    def service_account_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @service_account_scopes.setter
    def service_account_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[pulumi.Input[InstanceShieldedInstanceConfigArgs]]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self, value: Optional[pulumi.Input[InstanceShieldedInstanceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> Optional[pulumi.Input[InstanceVmImageArgs]]: ...
    @vm_image.setter
    def vm_image(self, value: Optional[pulumi.Input[InstanceVmImageArgs]]): ...

@pulumi.type_token("gcp:notebooks/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        accelerator_config: Optional[
            pulumi.Input[
                Union[InstanceAcceleratorConfigArgs, InstanceAcceleratorConfigArgsDict]
            ]
        ] = ...,
        boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        boot_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        container_image: Optional[
            pulumi.Input[
                Union[InstanceContainerImageArgs, InstanceContainerImageArgsDict]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_gpu_driver_path: Optional[pulumi.Input[_builtins.str]] = ...,
        data_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        data_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        install_gpu_driver: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        nic_type: Optional[pulumi.Input[_builtins.str]] = ...,
        no_proxy_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        no_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        no_remove_data_disk: Optional[pulumi.Input[_builtins.bool]] = ...,
        post_startup_script: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reservation_affinity: Optional[
            pulumi.Input[
                Union[
                    InstanceReservationAffinityArgs, InstanceReservationAffinityArgsDict
                ]
            ]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[
                Union[
                    InstanceShieldedInstanceConfigArgs,
                    InstanceShieldedInstanceConfigArgsDict,
                ]
            ]
        ] = ...,
        subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image: Optional[
            pulumi.Input[Union[InstanceVmImageArgs, InstanceVmImageArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        accelerator_config: Optional[
            pulumi.Input[
                Union[InstanceAcceleratorConfigArgs, InstanceAcceleratorConfigArgsDict]
            ]
        ] = ...,
        boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        boot_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        container_image: Optional[
            pulumi.Input[
                Union[InstanceContainerImageArgs, InstanceContainerImageArgsDict]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_gpu_driver_path: Optional[pulumi.Input[_builtins.str]] = ...,
        data_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        data_disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        install_gpu_driver: Optional[pulumi.Input[_builtins.bool]] = ...,
        instance_owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        nic_type: Optional[pulumi.Input[_builtins.str]] = ...,
        no_proxy_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        no_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        no_remove_data_disk: Optional[pulumi.Input[_builtins.bool]] = ...,
        post_startup_script: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reservation_affinity: Optional[
            pulumi.Input[
                Union[
                    InstanceReservationAffinityArgs, InstanceReservationAffinityArgsDict
                ]
            ]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[
                Union[
                    InstanceShieldedInstanceConfigArgs,
                    InstanceShieldedInstanceConfigArgsDict,
                ]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        vm_image: Optional[
            pulumi.Input[Union[InstanceVmImageArgs, InstanceVmImageArgsDict]]
        ] = ...,
    ) -> Instance: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorConfig")
    def accelerator_config(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceAcceleratorConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="bootDiskType")
    def boot_disk_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceContainerImage]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customGpuDriverPath")
    def custom_gpu_driver_path(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskSizeGb")
    def data_disk_size_gb(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="dataDiskType")
    def data_disk_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryption")
    def disk_encryption(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="installGpuDriver")
    def install_gpu_driver(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceOwners")
    def instance_owners(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="noProxyAccess")
    def no_proxy_access(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="noPublicIp")
    def no_public_ip(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="noRemoveDataDisk")
    def no_remove_data_disk(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="postStartupScript")
    def post_startup_script(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="proxyUri")
    def proxy_uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="reservationAffinity")
    def reservation_affinity(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceReservationAffinity]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountScopes")
    def service_account_scopes(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> pulumi.Output[outputs.InstanceShieldedInstanceConfig]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> pulumi.Output[Optional[outputs.InstanceVmImage]]: ...
