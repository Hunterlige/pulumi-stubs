import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EnvironmentContainerImageArgs",
    "EnvironmentContainerImageArgsDict",
    "EnvironmentVmImageArgs",
    "EnvironmentVmImageArgsDict",
    "InstanceAcceleratorConfigArgs",
    "InstanceAcceleratorConfigArgsDict",
    "InstanceContainerImageArgs",
    "InstanceContainerImageArgsDict",
    "InstanceIamBindingConditionArgs",
    "InstanceIamBindingConditionArgsDict",
    "InstanceIamMemberConditionArgs",
    "InstanceIamMemberConditionArgsDict",
    "InstanceReservationAffinityArgs",
    "InstanceReservationAffinityArgsDict",
    "InstanceShieldedInstanceConfigArgs",
    "InstanceShieldedInstanceConfigArgsDict",
    "InstanceVmImageArgs",
    "InstanceVmImageArgsDict",
    "RuntimeAccessConfigArgs",
    "RuntimeAccessConfigArgsDict",
    "RuntimeIamBindingConditionArgs",
    "RuntimeIamBindingConditionArgsDict",
    "RuntimeIamMemberConditionArgs",
    "RuntimeIamMemberConditionArgsDict",
    "RuntimeMetricArgs",
    "RuntimeMetricArgsDict",
    "RuntimeSoftwareConfigArgs",
    "RuntimeSoftwareConfigArgsDict",
    "RuntimeSoftwareConfigKernelArgs",
    "RuntimeSoftwareConfigKernelArgsDict",
    "RuntimeVirtualMachineArgs",
    "RuntimeVirtualMachineArgsDict",
    "RuntimeVirtualMachineVirtualMachineConfigArgs",
    "RuntimeVirtualMachineVirtualMachineConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

class EnvironmentContainerImageArgsDict(TypedDict):
    repository: pulumi.Input[_builtins.str]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EnvironmentContainerImageArgs:
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

class EnvironmentVmImageArgsDict(TypedDict):
    project: pulumi.Input[_builtins.str]
    image_family: NotRequired[pulumi.Input[_builtins.str]]
    image_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EnvironmentVmImageArgs:
    def __init__(
        __self__,
        *,
        project: pulumi.Input[_builtins.str],
        image_family: Optional[pulumi.Input[_builtins.str]] = ...,
        image_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]: ...
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="imageFamily")
    def image_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_family.setter
    def image_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceAcceleratorConfigArgsDict(TypedDict):
    core_count: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceAcceleratorConfigArgs:
    def __init__(
        __self__,
        *,
        core_count: pulumi.Input[_builtins.int],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> pulumi.Input[_builtins.int]: ...
    @core_count.setter
    def core_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class InstanceContainerImageArgsDict(TypedDict):
    repository: pulumi.Input[_builtins.str]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceContainerImageArgs:
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

class InstanceReservationAffinityArgsDict(TypedDict):
    consume_reservation_type: pulumi.Input[_builtins.str]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class InstanceReservationAffinityArgs:
    def __init__(
        __self__,
        *,
        consume_reservation_type: pulumi.Input[_builtins.str],
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> pulumi.Input[_builtins.str]: ...
    @consume_reservation_type.setter
    def consume_reservation_type(self, value: pulumi.Input[_builtins.str]): ...
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

class InstanceShieldedInstanceConfigArgsDict(TypedDict):
    enable_integrity_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    enable_secure_boot: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vtpm: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class InstanceShieldedInstanceConfigArgs:
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

class InstanceVmImageArgsDict(TypedDict):
    project: pulumi.Input[_builtins.str]
    image_family: NotRequired[pulumi.Input[_builtins.str]]
    image_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceVmImageArgs:
    def __init__(
        __self__,
        *,
        project: pulumi.Input[_builtins.str],
        image_family: Optional[pulumi.Input[_builtins.str]] = ...,
        image_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]: ...
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="imageFamily")
    def image_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_family.setter
    def image_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RuntimeAccessConfigArgsDict(TypedDict):
    access_type: NotRequired[pulumi.Input[_builtins.str]]
    proxy_uri: NotRequired[pulumi.Input[_builtins.str]]
    runtime_owner: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RuntimeAccessConfigArgs:
    def __init__(
        __self__,
        *,
        access_type: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_owner: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_type.setter
    def access_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="proxyUri")
    def proxy_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @proxy_uri.setter
    def proxy_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeOwner")
    def runtime_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_owner.setter
    def runtime_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RuntimeIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RuntimeIamBindingConditionArgs:
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

class RuntimeIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RuntimeIamMemberConditionArgs:
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

class RuntimeMetricArgsDict(TypedDict):
    system_metrics: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class RuntimeMetricArgs:
    def __init__(
        __self__,
        *,
        system_metrics: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="systemMetrics")
    def system_metrics(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @system_metrics.setter
    def system_metrics(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class RuntimeSoftwareConfigArgsDict(TypedDict):
    custom_gpu_driver_path: NotRequired[pulumi.Input[_builtins.str]]
    enable_health_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    idle_shutdown: NotRequired[pulumi.Input[_builtins.bool]]
    idle_shutdown_timeout: NotRequired[pulumi.Input[_builtins.int]]
    install_gpu_driver: NotRequired[pulumi.Input[_builtins.bool]]
    kernels: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RuntimeSoftwareConfigKernelArgsDict]]]
    ]
    notebook_upgrade_schedule: NotRequired[pulumi.Input[_builtins.str]]
    post_startup_script: NotRequired[pulumi.Input[_builtins.str]]
    post_startup_script_behavior: NotRequired[pulumi.Input[_builtins.str]]
    upgradeable: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class RuntimeSoftwareConfigArgs:
    def __init__(
        __self__,
        *,
        custom_gpu_driver_path: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_health_monitoring: Optional[pulumi.Input[_builtins.bool]] = ...,
        idle_shutdown: Optional[pulumi.Input[_builtins.bool]] = ...,
        idle_shutdown_timeout: Optional[pulumi.Input[_builtins.int]] = ...,
        install_gpu_driver: Optional[pulumi.Input[_builtins.bool]] = ...,
        kernels: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuntimeSoftwareConfigKernelArgs]]]
        ] = ...,
        notebook_upgrade_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        post_startup_script: Optional[pulumi.Input[_builtins.str]] = ...,
        post_startup_script_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        upgradeable: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customGpuDriverPath")
    def custom_gpu_driver_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_gpu_driver_path.setter
    def custom_gpu_driver_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableHealthMonitoring")
    def enable_health_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_health_monitoring.setter
    def enable_health_monitoring(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="idleShutdown")
    def idle_shutdown(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @idle_shutdown.setter
    def idle_shutdown(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="idleShutdownTimeout")
    def idle_shutdown_timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_shutdown_timeout.setter
    def idle_shutdown_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="installGpuDriver")
    def install_gpu_driver(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @install_gpu_driver.setter
    def install_gpu_driver(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def kernels(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RuntimeSoftwareConfigKernelArgs]]]
    ]: ...
    @kernels.setter
    def kernels(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuntimeSoftwareConfigKernelArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="notebookUpgradeSchedule")
    def notebook_upgrade_schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notebook_upgrade_schedule.setter
    def notebook_upgrade_schedule(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="postStartupScript")
    def post_startup_script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @post_startup_script.setter
    def post_startup_script(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postStartupScriptBehavior")
    def post_startup_script_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @post_startup_script_behavior.setter
    def post_startup_script_behavior(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def upgradeable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @upgradeable.setter
    def upgradeable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class RuntimeSoftwareConfigKernelArgsDict(TypedDict):
    repository: pulumi.Input[_builtins.str]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RuntimeSoftwareConfigKernelArgs:
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

class RuntimeVirtualMachineArgsDict(TypedDict):
    instance_id: NotRequired[pulumi.Input[_builtins.str]]
    instance_name: NotRequired[pulumi.Input[_builtins.str]]
    virtual_machine_config: NotRequired[
        pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigArgsDict]
    ]
    ...

@pulumi.input_type
class RuntimeVirtualMachineArgs:
    def __init__(
        __self__,
        *,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine_config: Optional[
            pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachineConfig")
    def virtual_machine_config(
        self,
    ) -> Optional[pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigArgs]]: ...
    @virtual_machine_config.setter
    def virtual_machine_config(
        self,
        value: Optional[pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigArgs]],
    ): ...

class RuntimeVirtualMachineVirtualMachineConfigArgsDict(TypedDict):
    data_disk: pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigDataDiskArgsDict]
    machine_type: pulumi.Input[_builtins.str]
    accelerator_config: NotRequired[
        pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigArgsDict]
    ]
    container_images: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuntimeVirtualMachineVirtualMachineConfigContainerImageArgsDict
                ]
            ]
        ]
    ]
    encryption_config: NotRequired[
        pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigEncryptionConfigArgsDict]
    ]
    guest_attributes: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    internal_ip_only: NotRequired[pulumi.Input[_builtins.bool]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    nic_type: NotRequired[pulumi.Input[_builtins.str]]
    reserved_ip_range: NotRequired[pulumi.Input[_builtins.str]]
    shielded_instance_config: NotRequired[
        pulumi.Input[
            RuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigArgsDict
        ]
    ]
    subnet: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RuntimeVirtualMachineVirtualMachineConfigArgs:
    def __init__(
        __self__,
        *,
        data_disk: pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigDataDiskArgs],
        machine_type: pulumi.Input[_builtins.str],
        accelerator_config: Optional[
            pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigArgs]
        ] = ...,
        container_images: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuntimeVirtualMachineVirtualMachineConfigContainerImageArgs
                    ]
                ]
            ]
        ] = ...,
        encryption_config: Optional[
            pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigEncryptionConfigArgs]
        ] = ...,
        guest_attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        internal_ip_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        nic_type: Optional[pulumi.Input[_builtins.str]] = ...,
        reserved_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        shielded_instance_config: Optional[
            pulumi.Input[
                RuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigArgs
            ]
        ] = ...,
        subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataDisk")
    def data_disk(
        self,
    ) -> pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigDataDiskArgs]: ...
    @data_disk.setter
    def data_disk(
        self, value: pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigDataDiskArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Input[_builtins.str]: ...
    @machine_type.setter
    def machine_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="acceleratorConfig")
    def accelerator_config(
        self,
    ) -> Optional[
        pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigArgs]
    ]: ...
    @accelerator_config.setter
    def accelerator_config(
        self,
        value: Optional[
            pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="containerImages")
    def container_images(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RuntimeVirtualMachineVirtualMachineConfigContainerImageArgs
                ]
            ]
        ]
    ]: ...
    @container_images.setter
    def container_images(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RuntimeVirtualMachineVirtualMachineConfigContainerImageArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(
        self,
    ) -> Optional[
        pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigEncryptionConfigArgs]
    ]: ...
    @encryption_config.setter
    def encryption_config(
        self,
        value: Optional[
            pulumi.Input[RuntimeVirtualMachineVirtualMachineConfigEncryptionConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="guestAttributes")
    def guest_attributes(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @guest_attributes.setter
    def guest_attributes(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="internalIpOnly")
    def internal_ip_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @internal_ip_only.setter
    def internal_ip_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @nic_type.setter
    def nic_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reservedIpRange")
    def reserved_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reserved_ip_range.setter
    def reserved_ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(
        self,
    ) -> Optional[
        pulumi.Input[
            RuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigArgs
        ]
    ]: ...
    @shielded_instance_config.setter
    def shielded_instance_config(
        self,
        value: Optional[
            pulumi.Input[
                RuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigArgs
            ]
        ],
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
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigArgsDict(TypedDict):
    core_count: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RuntimeVirtualMachineVirtualMachineConfigAcceleratorConfigArgs:
    def __init__(
        __self__,
        *,
        core_count: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @core_count.setter
    def core_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RuntimeVirtualMachineVirtualMachineConfigContainerImageArgsDict(TypedDict):
    repository: pulumi.Input[_builtins.str]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RuntimeVirtualMachineVirtualMachineConfigContainerImageArgs:
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

class RuntimeVirtualMachineVirtualMachineConfigDataDiskArgsDict(TypedDict):
    auto_delete: NotRequired[pulumi.Input[_builtins.bool]]
    boot: NotRequired[pulumi.Input[_builtins.bool]]
    device_name: NotRequired[pulumi.Input[_builtins.str]]
    guest_os_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    index: NotRequired[pulumi.Input[_builtins.int]]
    initialize_params: NotRequired[
        pulumi.Input[
            RuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsArgsDict
        ]
    ]
    interface: NotRequired[pulumi.Input[_builtins.str]]
    kind: NotRequired[pulumi.Input[_builtins.str]]
    licenses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    source: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RuntimeVirtualMachineVirtualMachineConfigDataDiskArgs:
    def __init__(
        __self__,
        *,
        auto_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        boot: Optional[pulumi.Input[_builtins.bool]] = ...,
        device_name: Optional[pulumi.Input[_builtins.str]] = ...,
        guest_os_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        index: Optional[pulumi.Input[_builtins.int]] = ...,
        initialize_params: Optional[
            pulumi.Input[
                RuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsArgs
            ]
        ] = ...,
        interface: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoDelete")
    def auto_delete(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_delete.setter
    def auto_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def boot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boot.setter
    def boot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @guest_os_features.setter
    def guest_os_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def index(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @index.setter
    def index(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="initializeParams")
    def initialize_params(
        self,
    ) -> Optional[
        pulumi.Input[
            RuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsArgs
        ]
    ]: ...
    @initialize_params.setter
    def initialize_params(
        self,
        value: Optional[
            pulumi.Input[
                RuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def interface(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interface.setter
    def interface(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def licenses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @licenses.setter
    def licenses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsArgsDict(
    TypedDict
):
    description: NotRequired[pulumi.Input[_builtins.str]]
    disk_name: NotRequired[pulumi.Input[_builtins.str]]
    disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class RuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParamsArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        disk_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_name.setter
    def disk_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class RuntimeVirtualMachineVirtualMachineConfigEncryptionConfigArgsDict(TypedDict):
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RuntimeVirtualMachineVirtualMachineConfigEncryptionConfigArgs:
    def __init__(
        __self__, *, kms_key: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigArgsDict(
    TypedDict
):
    enable_integrity_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    enable_secure_boot: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vtpm: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class RuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfigArgs:
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
