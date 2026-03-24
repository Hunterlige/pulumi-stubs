import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DataRepositoryAssociationS3",
    "DataRepositoryAssociationS3AutoExportPolicy",
    "DataRepositoryAssociationS3AutoImportPolicy",
    "FileCacheDataRepositoryAssociation",
    "FileCacheDataRepositoryAssociationNf",
    "FileCacheLustreConfiguration",
    "FileCacheLustreConfigurationLogConfiguration",
    "FileCacheLustreConfigurationMetadataConfiguration",
    "LustreFileSystemDataReadCacheConfiguration",
    "LustreFileSystemLogConfiguration",
    "LustreFileSystemMetadataConfiguration",
    "LustreFileSystemRootSquashConfiguration",
    "OntapFileSystemDiskIopsConfiguration",
    "OntapFileSystemEndpoint",
    "OntapFileSystemEndpointIntercluster",
    "OntapFileSystemEndpointManagement",
    ...,
    ...,
    "OntapStorageVirtualMachineEndpoint",
    "OntapStorageVirtualMachineEndpointIscsi",
    "OntapStorageVirtualMachineEndpointManagement",
    "OntapStorageVirtualMachineEndpointNf",
    "OntapStorageVirtualMachineEndpointSmb",
    "OntapVolumeAggregateConfiguration",
    "OntapVolumeSnaplockConfiguration",
    "OntapVolumeSnaplockConfigurationAutocommitPeriod",
    "OntapVolumeSnaplockConfigurationRetentionPeriod",
    ...,
    ...,
    ...,
    "OntapVolumeTieringPolicy",
    "OpenZfsFileSystemDiskIopsConfiguration",
    "OpenZfsFileSystemReadCacheConfiguration",
    "OpenZfsFileSystemRootVolumeConfiguration",
    "OpenZfsFileSystemRootVolumeConfigurationNfsExports",
    ...,
    ...,
    "OpenZfsVolumeNfsExports",
    "OpenZfsVolumeNfsExportsClientConfiguration",
    "OpenZfsVolumeOriginSnapshot",
    "OpenZfsVolumeUserAndGroupQuota",
    "S3AccessPointAttachmentOpenzfsConfiguration",
    ...,
    ...,
    "S3AccessPointAttachmentS3AccessPoint",
    ...,
    "S3AccessPointAttachmentTimeouts",
    "WindowsFileSystemAuditLogConfiguration",
    "WindowsFileSystemDiskIopsConfiguration",
    "WindowsFileSystemSelfManagedActiveDirectory",
    "GetOntapFileSystemDiskIopsConfigurationResult",
    "GetOntapFileSystemEndpointResult",
    "GetOntapFileSystemEndpointInterclusterResult",
    "GetOntapFileSystemEndpointManagementResult",
    ...,
    ...,
    "GetOntapStorageVirtualMachineEndpointResult",
    "GetOntapStorageVirtualMachineEndpointIscsiResult",
    ...,
    "GetOntapStorageVirtualMachineEndpointNfResult",
    "GetOntapStorageVirtualMachineEndpointSmbResult",
    "GetOntapStorageVirtualMachineFilterResult",
    ...,
    "GetOntapStorageVirtualMachinesFilterResult",
    "GetOpenZfsSnapshotFilterResult",
    "GetWindowsFileSystemAuditLogConfigurationResult",
    "GetWindowsFileSystemDiskIopsConfigurationResult",
]

@pulumi.output_type
class DataRepositoryAssociationS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_export_policy: Optional[
            outputs.DataRepositoryAssociationS3AutoExportPolicy
        ] = ...,
        auto_import_policy: Optional[
            outputs.DataRepositoryAssociationS3AutoImportPolicy
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoExportPolicy")
    def auto_export_policy(
        self,
    ) -> Optional[outputs.DataRepositoryAssociationS3AutoExportPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="autoImportPolicy")
    def auto_import_policy(
        self,
    ) -> Optional[outputs.DataRepositoryAssociationS3AutoImportPolicy]: ...

@pulumi.output_type
class DataRepositoryAssociationS3AutoExportPolicy(dict):
    def __init__(
        __self__, *, events: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DataRepositoryAssociationS3AutoImportPolicy(dict):
    def __init__(
        __self__, *, events: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FileCacheDataRepositoryAssociation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_repository_path: _builtins.str,
        file_cache_path: _builtins.str,
        association_id: Optional[_builtins.str] = ...,
        data_repository_subdirectories: Optional[Sequence[_builtins.str]] = ...,
        file_cache_id: Optional[_builtins.str] = ...,
        file_system_id: Optional[_builtins.str] = ...,
        file_system_path: Optional[_builtins.str] = ...,
        imported_file_chunk_size: Optional[_builtins.int] = ...,
        nfs: Optional[Sequence[outputs.FileCacheDataRepositoryAssociationNf]] = ...,
        resource_arn: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataRepositoryPath")
    def data_repository_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileCachePath")
    def file_cache_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataRepositorySubdirectories")
    def data_repository_subdirectories(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fileCacheId")
    def file_cache_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemPath")
    def file_system_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="importedFileChunkSize")
    def imported_file_chunk_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nfs(
        self,
    ) -> Optional[Sequence[outputs.FileCacheDataRepositoryAssociationNf]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class FileCacheDataRepositoryAssociationNf(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        version: _builtins.str,
        dns_ips: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FileCacheLustreConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deployment_type: _builtins.str,
        metadata_configurations: Sequence[
            outputs.FileCacheLustreConfigurationMetadataConfiguration
        ],
        per_unit_storage_throughput: _builtins.int,
        log_configurations: Optional[
            Sequence[outputs.FileCacheLustreConfigurationLogConfiguration]
        ] = ...,
        mount_name: Optional[_builtins.str] = ...,
        weekly_maintenance_start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metadataConfigurations")
    def metadata_configurations(
        self,
    ) -> Sequence[outputs.FileCacheLustreConfigurationMetadataConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="perUnitStorageThroughput")
    def per_unit_storage_throughput(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="logConfigurations")
    def log_configurations(
        self,
    ) -> Optional[Sequence[outputs.FileCacheLustreConfigurationLogConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="mountName")
    def mount_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FileCacheLustreConfigurationLogConfiguration(dict):
    def __init__(
        __self__,
        *,
        destination: Optional[_builtins.str] = ...,
        level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FileCacheLustreConfigurationMetadataConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, storage_capacity: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> _builtins.int: ...

@pulumi.output_type
class LustreFileSystemDataReadCacheConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, sizing_mode: _builtins.str, size: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizingMode")
    def sizing_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class LustreFileSystemLogConfiguration(dict):
    def __init__(
        __self__,
        *,
        destination: Optional[_builtins.str] = ...,
        level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LustreFileSystemMetadataConfiguration(dict):
    def __init__(
        __self__,
        *,
        iops: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LustreFileSystemRootSquashConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        no_squash_nids: Optional[Sequence[_builtins.str]] = ...,
        root_squash: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="noSquashNids")
    def no_squash_nids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="rootSquash")
    def root_squash(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OntapFileSystemDiskIopsConfiguration(dict):
    def __init__(
        __self__,
        *,
        iops: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OntapFileSystemEndpoint(dict):
    def __init__(
        __self__,
        *,
        interclusters: Optional[
            Sequence[outputs.OntapFileSystemEndpointIntercluster]
        ] = ...,
        managements: Optional[
            Sequence[outputs.OntapFileSystemEndpointManagement]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interclusters(
        self,
    ) -> Optional[Sequence[outputs.OntapFileSystemEndpointIntercluster]]: ...
    @_builtins.property
    @pulumi.getter
    def managements(
        self,
    ) -> Optional[Sequence[outputs.OntapFileSystemEndpointManagement]]: ...

@pulumi.output_type
class OntapFileSystemEndpointIntercluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_name: Optional[_builtins.str] = ...,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OntapFileSystemEndpointManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_name: Optional[_builtins.str] = ...,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OntapStorageVirtualMachineActiveDirectoryConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        netbios_name: Optional[_builtins.str] = ...,
        self_managed_active_directory_configuration: Optional[
            outputs.OntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="netbiosName")
    def netbios_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfManagedActiveDirectoryConfiguration")
    def self_managed_active_directory_configuration(
        self,
    ) -> Optional[
        outputs.OntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration
    ]: ...

@pulumi.output_type
class OntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_ips: Sequence[_builtins.str],
        domain_name: _builtins.str,
        password: _builtins.str,
        username: _builtins.str,
        file_system_administrators_group: Optional[_builtins.str] = ...,
        organizational_unit_distinguished_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemAdministratorsGroup")
    def file_system_administrators_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OntapStorageVirtualMachineEndpoint(dict):
    def __init__(
        __self__,
        *,
        iscsis: Optional[
            Sequence[outputs.OntapStorageVirtualMachineEndpointIscsi]
        ] = ...,
        managements: Optional[
            Sequence[outputs.OntapStorageVirtualMachineEndpointManagement]
        ] = ...,
        nfs: Optional[Sequence[outputs.OntapStorageVirtualMachineEndpointNf]] = ...,
        smbs: Optional[Sequence[outputs.OntapStorageVirtualMachineEndpointSmb]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iscsis(
        self,
    ) -> Optional[Sequence[outputs.OntapStorageVirtualMachineEndpointIscsi]]: ...
    @_builtins.property
    @pulumi.getter
    def managements(
        self,
    ) -> Optional[Sequence[outputs.OntapStorageVirtualMachineEndpointManagement]]: ...
    @_builtins.property
    @pulumi.getter
    def nfs(
        self,
    ) -> Optional[Sequence[outputs.OntapStorageVirtualMachineEndpointNf]]: ...
    @_builtins.property
    @pulumi.getter
    def smbs(
        self,
    ) -> Optional[Sequence[outputs.OntapStorageVirtualMachineEndpointSmb]]: ...

@pulumi.output_type
class OntapStorageVirtualMachineEndpointIscsi(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_name: Optional[_builtins.str] = ...,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OntapStorageVirtualMachineEndpointManagement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_name: Optional[_builtins.str] = ...,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OntapStorageVirtualMachineEndpointNf(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_name: Optional[_builtins.str] = ...,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OntapStorageVirtualMachineEndpointSmb(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_name: Optional[_builtins.str] = ...,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OntapVolumeAggregateConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aggregates: Optional[Sequence[_builtins.str]] = ...,
        constituents_per_aggregate: Optional[_builtins.int] = ...,
        total_constituents: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def aggregates(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="constituentsPerAggregate")
    def constituents_per_aggregate(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="totalConstituents")
    def total_constituents(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class OntapVolumeSnaplockConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        snaplock_type: _builtins.str,
        audit_log_volume: Optional[_builtins.bool] = ...,
        autocommit_period: Optional[
            outputs.OntapVolumeSnaplockConfigurationAutocommitPeriod
        ] = ...,
        privileged_delete: Optional[_builtins.str] = ...,
        retention_period: Optional[
            outputs.OntapVolumeSnaplockConfigurationRetentionPeriod
        ] = ...,
        volume_append_mode_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="snaplockType")
    def snaplock_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="auditLogVolume")
    def audit_log_volume(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="autocommitPeriod")
    def autocommit_period(
        self,
    ) -> Optional[outputs.OntapVolumeSnaplockConfigurationAutocommitPeriod]: ...
    @_builtins.property
    @pulumi.getter(name="privilegedDelete")
    def privileged_delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(
        self,
    ) -> Optional[outputs.OntapVolumeSnaplockConfigurationRetentionPeriod]: ...
    @_builtins.property
    @pulumi.getter(name="volumeAppendModeEnabled")
    def volume_append_mode_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class OntapVolumeSnaplockConfigurationAutocommitPeriod(dict):
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        value: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class OntapVolumeSnaplockConfigurationRetentionPeriod(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_retention: Optional[
            outputs.OntapVolumeSnaplockConfigurationRetentionPeriodDefaultRetention
        ] = ...,
        maximum_retention: Optional[
            outputs.OntapVolumeSnaplockConfigurationRetentionPeriodMaximumRetention
        ] = ...,
        minimum_retention: Optional[
            outputs.OntapVolumeSnaplockConfigurationRetentionPeriodMinimumRetention
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultRetention")
    def default_retention(
        self,
    ) -> Optional[
        outputs.OntapVolumeSnaplockConfigurationRetentionPeriodDefaultRetention
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maximumRetention")
    def maximum_retention(
        self,
    ) -> Optional[
        outputs.OntapVolumeSnaplockConfigurationRetentionPeriodMaximumRetention
    ]: ...
    @_builtins.property
    @pulumi.getter(name="minimumRetention")
    def minimum_retention(
        self,
    ) -> Optional[
        outputs.OntapVolumeSnaplockConfigurationRetentionPeriodMinimumRetention
    ]: ...

@pulumi.output_type
class OntapVolumeSnaplockConfigurationRetentionPeriodDefaultRetention(dict):
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        value: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class OntapVolumeSnaplockConfigurationRetentionPeriodMaximumRetention(dict):
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        value: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class OntapVolumeSnaplockConfigurationRetentionPeriodMinimumRetention(dict):
    def __init__(
        __self__,
        *,
        type: Optional[_builtins.str] = ...,
        value: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class OntapVolumeTieringPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cooling_period: Optional[_builtins.int] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="coolingPeriod")
    def cooling_period(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OpenZfsFileSystemDiskIopsConfiguration(dict):
    def __init__(
        __self__,
        *,
        iops: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OpenZfsFileSystemReadCacheConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        size: Optional[_builtins.int] = ...,
        sizing_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sizingMode")
    def sizing_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OpenZfsFileSystemRootVolumeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        copy_tags_to_snapshots: Optional[_builtins.bool] = ...,
        data_compression_type: Optional[_builtins.str] = ...,
        nfs_exports: Optional[
            outputs.OpenZfsFileSystemRootVolumeConfigurationNfsExports
        ] = ...,
        read_only: Optional[_builtins.bool] = ...,
        record_size_kib: Optional[_builtins.int] = ...,
        user_and_group_quotas: Optional[
            Sequence[outputs.OpenZfsFileSystemRootVolumeConfigurationUserAndGroupQuota]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="copyTagsToSnapshots")
    def copy_tags_to_snapshots(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dataCompressionType")
    def data_compression_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nfsExports")
    def nfs_exports(
        self,
    ) -> Optional[outputs.OpenZfsFileSystemRootVolumeConfigurationNfsExports]: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="recordSizeKib")
    def record_size_kib(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="userAndGroupQuotas")
    def user_and_group_quotas(
        self,
    ) -> Optional[
        Sequence[outputs.OpenZfsFileSystemRootVolumeConfigurationUserAndGroupQuota]
    ]: ...

@pulumi.output_type
class OpenZfsFileSystemRootVolumeConfigurationNfsExports(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_configurations: Sequence[
            outputs.OpenZfsFileSystemRootVolumeConfigurationNfsExportsClientConfiguration
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientConfigurations")
    def client_configurations(
        self,
    ) -> Sequence[
        outputs.OpenZfsFileSystemRootVolumeConfigurationNfsExportsClientConfiguration
    ]: ...

@pulumi.output_type
class OpenZfsFileSystemRootVolumeConfigurationNfsExportsClientConfiguration(dict):
    def __init__(
        __self__, *, clients: _builtins.str, options: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def clients(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class OpenZfsFileSystemRootVolumeConfigurationUserAndGroupQuota(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.int,
        storage_capacity_quota_gib: _builtins.int,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageCapacityQuotaGib")
    def storage_capacity_quota_gib(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class OpenZfsVolumeNfsExports(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_configurations: Sequence[
            outputs.OpenZfsVolumeNfsExportsClientConfiguration
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientConfigurations")
    def client_configurations(
        self,
    ) -> Sequence[outputs.OpenZfsVolumeNfsExportsClientConfiguration]: ...

@pulumi.output_type
class OpenZfsVolumeNfsExportsClientConfiguration(dict):
    def __init__(
        __self__, *, clients: _builtins.str, options: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def clients(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class OpenZfsVolumeOriginSnapshot(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, copy_strategy: _builtins.str, snapshot_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="copyStrategy")
    def copy_strategy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="snapshotArn")
    def snapshot_arn(self) -> _builtins.str: ...

@pulumi.output_type
class OpenZfsVolumeUserAndGroupQuota(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.int,
        storage_capacity_quota_gib: _builtins.int,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageCapacityQuotaGib")
    def storage_capacity_quota_gib(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class S3AccessPointAttachmentOpenzfsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        file_system_identity: outputs.S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentity,
        volume_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemIdentity")
    def file_system_identity(
        self,
    ) -> outputs.S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentity: ...
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> _builtins.str: ...

@pulumi.output_type
class S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        posix_user: Optional[
            outputs.S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityPosixUser
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="posixUser")
    def posix_user(
        self,
    ) -> Optional[
        outputs.S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityPosixUser
    ]: ...

@pulumi.output_type
class S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityPosixUser(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        gid: _builtins.int,
        uid: _builtins.int,
        secondary_gids: Optional[Sequence[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class S3AccessPointAttachmentS3AccessPoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        policy: Optional[_builtins.str] = ...,
        vpc_configuration: Optional[
            outputs.S3AccessPointAttachmentS3AccessPointVpcConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> Optional[outputs.S3AccessPointAttachmentS3AccessPointVpcConfiguration]: ...

@pulumi.output_type
class S3AccessPointAttachmentS3AccessPointVpcConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, vpc_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class S3AccessPointAttachmentTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WindowsFileSystemAuditLogConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audit_log_destination: Optional[_builtins.str] = ...,
        file_access_audit_log_level: Optional[_builtins.str] = ...,
        file_share_access_audit_log_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogDestination")
    def audit_log_destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileAccessAuditLogLevel")
    def file_access_audit_log_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileShareAccessAuditLogLevel")
    def file_share_access_audit_log_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WindowsFileSystemDiskIopsConfiguration(dict):
    def __init__(
        __self__,
        *,
        iops: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WindowsFileSystemSelfManagedActiveDirectory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_ips: Sequence[_builtins.str],
        domain_name: _builtins.str,
        domain_join_service_account_secret: Optional[_builtins.str] = ...,
        file_system_administrators_group: Optional[_builtins.str] = ...,
        organizational_unit_distinguished_name: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainJoinServiceAccountSecret")
    def domain_join_service_account_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemAdministratorsGroup")
    def file_system_administrators_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetOntapFileSystemDiskIopsConfigurationResult(dict):
    def __init__(__self__, *, iops: _builtins.int, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...

@pulumi.output_type
class GetOntapFileSystemEndpointResult(dict):
    def __init__(
        __self__,
        *,
        interclusters: Sequence[outputs.GetOntapFileSystemEndpointInterclusterResult],
        managements: Sequence[outputs.GetOntapFileSystemEndpointManagementResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interclusters(
        self,
    ) -> Sequence[outputs.GetOntapFileSystemEndpointInterclusterResult]: ...
    @_builtins.property
    @pulumi.getter
    def managements(
        self,
    ) -> Sequence[outputs.GetOntapFileSystemEndpointManagementResult]: ...

@pulumi.output_type
class GetOntapFileSystemEndpointInterclusterResult(dict):
    def __init__(
        __self__, *, dns_name: _builtins.str, ip_addresses: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetOntapFileSystemEndpointManagementResult(dict):
    def __init__(
        __self__, *, dns_name: _builtins.str, ip_addresses: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetOntapStorageVirtualMachineActiveDirectoryConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        netbios_name: _builtins.str,
        self_managed_active_directory_configurations: Sequence[
            outputs.GetOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="netbiosName")
    def netbios_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfManagedActiveDirectoryConfigurations")
    def self_managed_active_directory_configurations(
        self,
    ) -> Sequence[
        outputs.GetOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationResult
    ]: ...

@pulumi.output_type
class GetOntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationResult(
    dict
):
    def __init__(
        __self__,
        *,
        dns_ips: Sequence[_builtins.str],
        domain_name: _builtins.str,
        file_system_administrators_group: _builtins.str,
        organizational_unit_distinguished_name: _builtins.str,
        username: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemAdministratorsGroup")
    def file_system_administrators_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class GetOntapStorageVirtualMachineEndpointResult(dict):
    def __init__(
        __self__,
        *,
        iscsis: Sequence[outputs.GetOntapStorageVirtualMachineEndpointIscsiResult],
        managements: Sequence[
            outputs.GetOntapStorageVirtualMachineEndpointManagementResult
        ],
        nfs: Sequence[outputs.GetOntapStorageVirtualMachineEndpointNfResult],
        smbs: Sequence[outputs.GetOntapStorageVirtualMachineEndpointSmbResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iscsis(
        self,
    ) -> Sequence[outputs.GetOntapStorageVirtualMachineEndpointIscsiResult]: ...
    @_builtins.property
    @pulumi.getter
    def managements(
        self,
    ) -> Sequence[outputs.GetOntapStorageVirtualMachineEndpointManagementResult]: ...
    @_builtins.property
    @pulumi.getter
    def nfs(
        self,
    ) -> Sequence[outputs.GetOntapStorageVirtualMachineEndpointNfResult]: ...
    @_builtins.property
    @pulumi.getter
    def smbs(
        self,
    ) -> Sequence[outputs.GetOntapStorageVirtualMachineEndpointSmbResult]: ...

@pulumi.output_type
class GetOntapStorageVirtualMachineEndpointIscsiResult(dict):
    def __init__(
        __self__, *, dns_name: _builtins.str, ip_addresses: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetOntapStorageVirtualMachineEndpointManagementResult(dict):
    def __init__(
        __self__, *, dns_name: _builtins.str, ip_addresses: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetOntapStorageVirtualMachineEndpointNfResult(dict):
    def __init__(
        __self__, *, dns_name: _builtins.str, ip_addresses: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetOntapStorageVirtualMachineEndpointSmbResult(dict):
    def __init__(
        __self__, *, dns_name: _builtins.str, ip_addresses: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetOntapStorageVirtualMachineFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetOntapStorageVirtualMachineLifecycleTransitionReasonResult(dict):
    def __init__(__self__, *, message: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...

@pulumi.output_type
class GetOntapStorageVirtualMachinesFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetOpenZfsSnapshotFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetWindowsFileSystemAuditLogConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        audit_log_destination: _builtins.str,
        file_access_audit_log_level: _builtins.str,
        file_share_access_audit_log_level: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogDestination")
    def audit_log_destination(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileAccessAuditLogLevel")
    def file_access_audit_log_level(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileShareAccessAuditLogLevel")
    def file_share_access_audit_log_level(self) -> _builtins.str: ...

@pulumi.output_type
class GetWindowsFileSystemDiskIopsConfigurationResult(dict):
    def __init__(__self__, *, iops: _builtins.int, mode: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
