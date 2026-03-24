

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EnvironmentContainerImage', 'EnvironmentVmImage', 'InstanceAcceleratorConfig', 'InstanceContainerImage', 'InstanceIamBindingCondition', 'InstanceIamMemberCondition', 'InstanceReservationAffinity', 'InstanceShieldedInstanceConfig', 'InstanceVmImage', 'RuntimeAccessConfig', 'RuntimeIamBindingCondition', 'RuntimeIamMemberCondition', 'RuntimeMetric', 'RuntimeSoftwareConfig', 'RuntimeSoftwareConfigKernel', 'RuntimeVirtualMachine', 'RuntimeVirtualMachineVirtualMachineConfig', ..., ..., 'RuntimeVirtualMachineVirtualMachineConfigDataDisk', ..., ..., ...]
@pulumi.output_type
class EnvironmentContainerImage(dict):
    def __init__(__self__, *, repository: _builtins.str, tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentVmImage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, project: _builtins.str, image_family: Optional[_builtins.str] = ..., image_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageFamily")
    def image_family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceAcceleratorConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, core_count: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InstanceContainerImage(dict):
    def __init__(__self__, *, repository: _builtins.str, tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class InstanceIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class InstanceReservationAffinity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, consume_reservation_type: _builtins.str, key: Optional[_builtins.str] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumeReservationType")
    def consume_reservation_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class InstanceShieldedInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_integrity_monitoring: Optional[_builtins.bool] = ..., enable_secure_boot: Optional[_builtins.bool] = ..., enable_vtpm: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableVtpm")
    def enable_vtpm(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class InstanceVmImage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, project: _builtins.str, image_family: Optional[_builtins.str] = ..., image_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageFamily")
    def image_family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeAccessConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_type: Optional[_builtins.str] = ..., proxy_uri: Optional[_builtins.str] = ..., runtime_owner: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessType")
    def access_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyUri")
    def proxy_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeOwner")
    def runtime_owner(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuntimeIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuntimeMetric(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, system_metrics: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemMetrics")
    def system_metrics(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuntimeSoftwareConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_gpu_driver_path: Optional[_builtins.str] = ..., enable_health_monitoring: Optional[_builtins.bool] = ..., idle_shutdown: Optional[_builtins.bool] = ..., idle_shutdown_timeout: Optional[_builtins.int] = ..., install_gpu_driver: Optional[_builtins.bool] = ..., kernels: Optional[Sequence[outputs.RuntimeSoftwareConfigKernel]] = ..., notebook_upgrade_schedule: Optional[_builtins.str] = ..., post_startup_script: Optional[_builtins.str] = ..., post_startup_script_behavior: Optional[_builtins.str] = ..., upgradeable: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customGpuDriverPath")
    def custom_gpu_driver_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableHealthMonitoring")
    def enable_health_monitoring(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleShutdown")
    def idle_shutdown(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleShutdownTimeout")
    def idle_shutdown_timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installGpuDriver")
    def install_gpu_driver(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kernels(self) -> Optional[Sequence[outputs.RuntimeSoftwareConfigKernel]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notebookUpgradeSchedule")
    def notebook_upgrade_schedule(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postStartupScript")
    def post_startup_script(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postStartupScriptBehavior")
    def post_startup_script_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def upgradeable(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RuntimeSoftwareConfigKernel(dict):
    def __init__(__self__, *, repository: _builtins.str, tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeVirtualMachine(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_id: Optional[_builtins.str] = ..., instance_name: Optional[_builtins.str] = ..., virtual_machine_config: Optional[outputs.RuntimeVirtualMachineVirtualMachineConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineConfig")
    def virtual_machine_config(self) -> Optional[outputs.RuntimeVirtualMachineVirtualMachineConfig]:
        
        ...
    


@pulumi.output_type
class RuntimeVirtualMachineVirtualMachineConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_disk: outputs.RuntimeVirtualMachineVirtualMachineConfigDataDisk, machine_type: _builtins.str, accelerator_config: Optional[outputs.RuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig] = ..., container_images: Optional[Sequence[outputs.RuntimeVirtualMachineVirtualMachineConfigContainerImage]] = ..., encryption_config: Optional[outputs.RuntimeVirtualMachineVirtualMachineConfigEncryptionConfig] = ..., guest_attributes: Optional[Mapping[str, _builtins.str]] = ..., internal_ip_only: Optional[_builtins.bool] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., network: Optional[_builtins.str] = ..., nic_type: Optional[_builtins.str] = ..., reserved_ip_range: Optional[_builtins.str] = ..., shielded_instance_config: Optional[outputs.RuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig] = ..., subnet: Optional[_builtins.str] = ..., tags: Optional[Sequence[_builtins.str]] = ..., zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDisk")
    def data_disk(self) -> outputs.RuntimeVirtualMachineVirtualMachineConfigDataDisk:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorConfig")
    def accelerator_config(self) -> Optional[outputs.RuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerImages")
    def container_images(self) -> Optional[Sequence[outputs.RuntimeVirtualMachineVirtualMachineConfigContainerImage]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[outputs.RuntimeVirtualMachineVirtualMachineConfigEncryptionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestAttributes")
    def guest_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalIpOnly")
    def internal_ip_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedIpRange")
    def reserved_ip_range(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(self) -> Optional[outputs.RuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeVirtualMachineVirtualMachineConfigAcceleratorConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, core_count: Optional[_builtins.int] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreCount")
    def core_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeVirtualMachineVirtualMachineConfigContainerImage(dict):
    def __init__(__self__, *, repository: _builtins.str, tag: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeVirtualMachineVirtualMachineConfigDataDisk(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_delete: Optional[_builtins.bool] = ..., boot: Optional[_builtins.bool] = ..., device_name: Optional[_builtins.str] = ..., guest_os_features: Optional[Sequence[_builtins.str]] = ..., index: Optional[_builtins.int] = ..., initialize_params: Optional[outputs.RuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams] = ..., interface: Optional[_builtins.str] = ..., kind: Optional[_builtins.str] = ..., licenses: Optional[Sequence[_builtins.str]] = ..., mode: Optional[_builtins.str] = ..., source: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoDelete")
    def auto_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def boot(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def index(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initializeParams")
    def initialize_params(self) -> Optional[outputs.RuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interface(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def licenses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeVirtualMachineVirtualMachineConfigDataDiskInitializeParams(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., disk_name: Optional[_builtins.str] = ..., disk_size_gb: Optional[_builtins.int] = ..., disk_type: Optional[_builtins.str] = ..., labels: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuntimeVirtualMachineVirtualMachineConfigEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeVirtualMachineVirtualMachineConfigShieldedInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_integrity_monitoring: Optional[_builtins.bool] = ..., enable_secure_boot: Optional[_builtins.bool] = ..., enable_vtpm: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableVtpm")
    def enable_vtpm(self) -> Optional[_builtins.bool]:
        
        ...
    


