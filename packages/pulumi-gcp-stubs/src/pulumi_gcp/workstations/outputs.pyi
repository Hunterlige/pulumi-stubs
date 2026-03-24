

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkstationClusterCondition', 'WorkstationClusterDomainConfig', 'WorkstationClusterPrivateClusterConfig', 'WorkstationConfigAllowedPort', 'WorkstationConfigCondition', 'WorkstationConfigContainer', 'WorkstationConfigEncryptionKey', 'WorkstationConfigEphemeralDirectory', 'WorkstationConfigEphemeralDirectoryGcePd', 'WorkstationConfigHost', 'WorkstationConfigHostGceInstance', 'WorkstationConfigHostGceInstanceAccelerator', 'WorkstationConfigHostGceInstanceBoostConfig', ..., ..., ..., 'WorkstationConfigIamBindingCondition', 'WorkstationConfigIamMemberCondition', 'WorkstationConfigPersistentDirectory', 'WorkstationConfigPersistentDirectoryGcePd', 'WorkstationConfigReadinessCheck', 'WorkstationIamBindingCondition', 'WorkstationIamMemberCondition']
@pulumi.output_type
class WorkstationClusterCondition(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., details: Optional[Sequence[Mapping[str, _builtins.str]]] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkstationClusterDomainConfig(dict):
    def __init__(__self__, *, domain: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkstationClusterPrivateClusterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_private_endpoint: _builtins.bool, allowed_projects: Optional[Sequence[_builtins.str]] = ..., cluster_hostname: Optional[_builtins.str] = ..., service_attachment_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateEndpoint")
    def enable_private_endpoint(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedProjects")
    def allowed_projects(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterHostname")
    def cluster_hostname(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachmentUri")
    def service_attachment_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkstationConfigAllowedPort(dict):
    def __init__(__self__, *, first: Optional[_builtins.int] = ..., last: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def first(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def last(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkstationConfigCondition(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., details: Optional[Sequence[Mapping[str, _builtins.str]]] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkstationConfigContainer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, args: Optional[Sequence[_builtins.str]] = ..., commands: Optional[Sequence[_builtins.str]] = ..., env: Optional[Mapping[str, _builtins.str]] = ..., image: Optional[_builtins.str] = ..., run_as_user: Optional[_builtins.int] = ..., working_dir: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def env(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkstationConfigEncryptionKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key: _builtins.str, kms_key_service_account: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyServiceAccount")
    def kms_key_service_account(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkstationConfigEphemeralDirectory(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gce_pd: Optional[outputs.WorkstationConfigEphemeralDirectoryGcePd] = ..., mount_path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcePd")
    def gce_pd(self) -> Optional[outputs.WorkstationConfigEphemeralDirectoryGcePd]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkstationConfigEphemeralDirectoryGcePd(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_type: Optional[_builtins.str] = ..., read_only: Optional[_builtins.bool] = ..., source_image: Optional[_builtins.str] = ..., source_snapshot: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceImage")
    def source_image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshot")
    def source_snapshot(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkstationConfigHost(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gce_instance: Optional[outputs.WorkstationConfigHostGceInstance] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gceInstance")
    def gce_instance(self) -> Optional[outputs.WorkstationConfigHostGceInstance]:
        
        ...
    


@pulumi.output_type
class WorkstationConfigHostGceInstance(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, accelerators: Optional[Sequence[outputs.WorkstationConfigHostGceInstanceAccelerator]] = ..., boost_configs: Optional[Sequence[outputs.WorkstationConfigHostGceInstanceBoostConfig]] = ..., boot_disk_size_gb: Optional[_builtins.int] = ..., confidential_instance_config: Optional[outputs.WorkstationConfigHostGceInstanceConfidentialInstanceConfig] = ..., disable_public_ip_addresses: Optional[_builtins.bool] = ..., disable_ssh: Optional[_builtins.bool] = ..., enable_nested_virtualization: Optional[_builtins.bool] = ..., machine_type: Optional[_builtins.str] = ..., pool_size: Optional[_builtins.int] = ..., service_account: Optional[_builtins.str] = ..., service_account_scopes: Optional[Sequence[_builtins.str]] = ..., shielded_instance_config: Optional[outputs.WorkstationConfigHostGceInstanceShieldedInstanceConfig] = ..., tags: Optional[Sequence[_builtins.str]] = ..., vm_tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[Sequence[outputs.WorkstationConfigHostGceInstanceAccelerator]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boostConfigs")
    def boost_configs(self) -> Optional[Sequence[outputs.WorkstationConfigHostGceInstanceBoostConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(self) -> Optional[outputs.WorkstationConfigHostGceInstanceConfidentialInstanceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disablePublicIpAddresses")
    def disable_public_ip_addresses(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableSsh")
    def disable_ssh(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolSize")
    def pool_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountScopes")
    def service_account_scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(self) -> Optional[outputs.WorkstationConfigHostGceInstanceShieldedInstanceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmTags")
    def vm_tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class WorkstationConfigHostGceInstanceAccelerator(dict):
    def __init__(__self__, *, count: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkstationConfigHostGceInstanceBoostConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, accelerators: Optional[Sequence[outputs.WorkstationConfigHostGceInstanceBoostConfigAccelerator]] = ..., boot_disk_size_gb: Optional[_builtins.int] = ..., enable_nested_virtualization: Optional[_builtins.bool] = ..., machine_type: Optional[_builtins.str] = ..., pool_size: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[Sequence[outputs.WorkstationConfigHostGceInstanceBoostConfigAccelerator]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolSize")
    def pool_size(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkstationConfigHostGceInstanceBoostConfigAccelerator(dict):
    def __init__(__self__, *, count: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkstationConfigHostGceInstanceConfidentialInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_confidential_compute: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableConfidentialCompute")
    def enable_confidential_compute(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class WorkstationConfigHostGceInstanceShieldedInstanceConfig(dict):
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
class WorkstationConfigIamBindingCondition(dict):
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
class WorkstationConfigIamMemberCondition(dict):
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
class WorkstationConfigPersistentDirectory(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gce_pd: Optional[outputs.WorkstationConfigPersistentDirectoryGcePd] = ..., mount_path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcePd")
    def gce_pd(self) -> Optional[outputs.WorkstationConfigPersistentDirectoryGcePd]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkstationConfigPersistentDirectoryGcePd(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_type: Optional[_builtins.str] = ..., fs_type: Optional[_builtins.str] = ..., reclaim_policy: Optional[_builtins.str] = ..., size_gb: Optional[_builtins.int] = ..., source_snapshot: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fsType")
    def fs_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reclaimPolicy")
    def reclaim_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshot")
    def source_snapshot(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkstationConfigReadinessCheck(dict):
    def __init__(__self__, *, path: _builtins.str, port: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class WorkstationIamBindingCondition(dict):
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
class WorkstationIamMemberCondition(dict):
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
    


