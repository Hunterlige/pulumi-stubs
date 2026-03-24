

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DataRepositoryAssociationS3Args', 'DataRepositoryAssociationS3ArgsDict', 'DataRepositoryAssociationS3AutoExportPolicyArgs', ..., 'DataRepositoryAssociationS3AutoImportPolicyArgs', ..., 'FileCacheDataRepositoryAssociationArgs', 'FileCacheDataRepositoryAssociationArgsDict', 'FileCacheDataRepositoryAssociationNfArgs', 'FileCacheDataRepositoryAssociationNfArgsDict', 'FileCacheLustreConfigurationArgs', 'FileCacheLustreConfigurationArgsDict', 'FileCacheLustreConfigurationLogConfigurationArgs', ..., ..., ..., 'LustreFileSystemDataReadCacheConfigurationArgs', 'LustreFileSystemDataReadCacheConfigurationArgsDict', 'LustreFileSystemLogConfigurationArgs', 'LustreFileSystemLogConfigurationArgsDict', 'LustreFileSystemMetadataConfigurationArgs', 'LustreFileSystemMetadataConfigurationArgsDict', 'LustreFileSystemRootSquashConfigurationArgs', 'LustreFileSystemRootSquashConfigurationArgsDict', 'OntapFileSystemDiskIopsConfigurationArgs', 'OntapFileSystemDiskIopsConfigurationArgsDict', 'OntapFileSystemEndpointArgs', 'OntapFileSystemEndpointArgsDict', 'OntapFileSystemEndpointInterclusterArgs', 'OntapFileSystemEndpointInterclusterArgsDict', 'OntapFileSystemEndpointManagementArgs', 'OntapFileSystemEndpointManagementArgsDict', ..., ..., ..., ..., 'OntapStorageVirtualMachineEndpointArgs', 'OntapStorageVirtualMachineEndpointArgsDict', 'OntapStorageVirtualMachineEndpointIscsiArgs', 'OntapStorageVirtualMachineEndpointIscsiArgsDict', 'OntapStorageVirtualMachineEndpointManagementArgs', ..., 'OntapStorageVirtualMachineEndpointNfArgs', 'OntapStorageVirtualMachineEndpointNfArgsDict', 'OntapStorageVirtualMachineEndpointSmbArgs', 'OntapStorageVirtualMachineEndpointSmbArgsDict', 'OntapVolumeAggregateConfigurationArgs', 'OntapVolumeAggregateConfigurationArgsDict', 'OntapVolumeSnaplockConfigurationArgs', 'OntapVolumeSnaplockConfigurationArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'OntapVolumeTieringPolicyArgs', 'OntapVolumeTieringPolicyArgsDict', 'OpenZfsFileSystemDiskIopsConfigurationArgs', 'OpenZfsFileSystemDiskIopsConfigurationArgsDict', 'OpenZfsFileSystemReadCacheConfigurationArgs', 'OpenZfsFileSystemReadCacheConfigurationArgsDict', 'OpenZfsFileSystemRootVolumeConfigurationArgs', 'OpenZfsFileSystemRootVolumeConfigurationArgsDict', ..., ..., ..., ..., ..., ..., 'OpenZfsVolumeNfsExportsArgs', 'OpenZfsVolumeNfsExportsArgsDict', 'OpenZfsVolumeNfsExportsClientConfigurationArgs', 'OpenZfsVolumeNfsExportsClientConfigurationArgsDict', 'OpenZfsVolumeOriginSnapshotArgs', 'OpenZfsVolumeOriginSnapshotArgsDict', 'OpenZfsVolumeUserAndGroupQuotaArgs', 'OpenZfsVolumeUserAndGroupQuotaArgsDict', 'S3AccessPointAttachmentOpenzfsConfigurationArgs', ..., ..., ..., ..., ..., 'S3AccessPointAttachmentS3AccessPointArgs', 'S3AccessPointAttachmentS3AccessPointArgsDict', ..., ..., 'S3AccessPointAttachmentTimeoutsArgs', 'S3AccessPointAttachmentTimeoutsArgsDict', 'WindowsFileSystemAuditLogConfigurationArgs', 'WindowsFileSystemAuditLogConfigurationArgsDict', 'WindowsFileSystemDiskIopsConfigurationArgs', 'WindowsFileSystemDiskIopsConfigurationArgsDict', 'WindowsFileSystemSelfManagedActiveDirectoryArgs', ..., 'GetOntapStorageVirtualMachineFilterArgs', 'GetOntapStorageVirtualMachineFilterArgsDict', 'GetOntapStorageVirtualMachinesFilterArgs', 'GetOntapStorageVirtualMachinesFilterArgsDict', 'GetOpenZfsSnapshotFilterArgs', 'GetOpenZfsSnapshotFilterArgsDict']
class DataRepositoryAssociationS3ArgsDict(TypedDict):
    auto_export_policy: NotRequired[pulumi.Input[DataRepositoryAssociationS3AutoExportPolicyArgsDict]]
    auto_import_policy: NotRequired[pulumi.Input[DataRepositoryAssociationS3AutoImportPolicyArgsDict]]


@pulumi.input_type
class DataRepositoryAssociationS3Args:
    def __init__(__self__, *, auto_export_policy: Optional[pulumi.Input[DataRepositoryAssociationS3AutoExportPolicyArgs]] = ..., auto_import_policy: Optional[pulumi.Input[DataRepositoryAssociationS3AutoImportPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoExportPolicy")
    def auto_export_policy(self) -> Optional[pulumi.Input[DataRepositoryAssociationS3AutoExportPolicyArgs]]:
        
        ...
    
    @auto_export_policy.setter
    def auto_export_policy(self, value: Optional[pulumi.Input[DataRepositoryAssociationS3AutoExportPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoImportPolicy")
    def auto_import_policy(self) -> Optional[pulumi.Input[DataRepositoryAssociationS3AutoImportPolicyArgs]]:
        
        ...
    
    @auto_import_policy.setter
    def auto_import_policy(self, value: Optional[pulumi.Input[DataRepositoryAssociationS3AutoImportPolicyArgs]]): # -> None:
        ...
    


class DataRepositoryAssociationS3AutoExportPolicyArgsDict(TypedDict):
    events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DataRepositoryAssociationS3AutoExportPolicyArgs:
    def __init__(__self__, *, events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @events.setter
    def events(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DataRepositoryAssociationS3AutoImportPolicyArgsDict(TypedDict):
    events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DataRepositoryAssociationS3AutoImportPolicyArgs:
    def __init__(__self__, *, events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @events.setter
    def events(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FileCacheDataRepositoryAssociationArgsDict(TypedDict):
    data_repository_path: pulumi.Input[_builtins.str]
    file_cache_path: pulumi.Input[_builtins.str]
    association_id: NotRequired[pulumi.Input[_builtins.str]]
    data_repository_subdirectories: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    file_cache_id: NotRequired[pulumi.Input[_builtins.str]]
    file_system_id: NotRequired[pulumi.Input[_builtins.str]]
    file_system_path: NotRequired[pulumi.Input[_builtins.str]]
    imported_file_chunk_size: NotRequired[pulumi.Input[_builtins.int]]
    nfs: NotRequired[pulumi.Input[Sequence[pulumi.Input[FileCacheDataRepositoryAssociationNfArgsDict]]]]
    resource_arn: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FileCacheDataRepositoryAssociationArgs:
    def __init__(__self__, *, data_repository_path: pulumi.Input[_builtins.str], file_cache_path: pulumi.Input[_builtins.str], association_id: Optional[pulumi.Input[_builtins.str]] = ..., data_repository_subdirectories: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., file_cache_id: Optional[pulumi.Input[_builtins.str]] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., file_system_path: Optional[pulumi.Input[_builtins.str]] = ..., imported_file_chunk_size: Optional[pulumi.Input[_builtins.int]] = ..., nfs: Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheDataRepositoryAssociationNfArgs]]]] = ..., resource_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRepositoryPath")
    def data_repository_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_repository_path.setter
    def data_repository_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileCachePath")
    def file_cache_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_cache_path.setter
    def file_cache_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @association_id.setter
    def association_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataRepositorySubdirectories")
    def data_repository_subdirectories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @data_repository_subdirectories.setter
    def data_repository_subdirectories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileCacheId")
    def file_cache_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_cache_id.setter
    def file_cache_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemPath")
    def file_system_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @file_system_path.setter
    def file_system_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importedFileChunkSize")
    def imported_file_chunk_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @imported_file_chunk_size.setter
    def imported_file_chunk_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheDataRepositoryAssociationNfArgs]]]]:
        
        ...
    
    @nfs.setter
    def nfs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheDataRepositoryAssociationNfArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FileCacheDataRepositoryAssociationNfArgsDict(TypedDict):
    version: pulumi.Input[_builtins.str]
    dns_ips: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FileCacheDataRepositoryAssociationNfArgs:
    def __init__(__self__, *, version: pulumi.Input[_builtins.str], dns_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @dns_ips.setter
    def dns_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FileCacheLustreConfigurationArgsDict(TypedDict):
    deployment_type: pulumi.Input[_builtins.str]
    metadata_configurations: pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationMetadataConfigurationArgsDict]]]
    per_unit_storage_throughput: pulumi.Input[_builtins.int]
    log_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationLogConfigurationArgsDict]]]]
    mount_name: NotRequired[pulumi.Input[_builtins.str]]
    weekly_maintenance_start_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FileCacheLustreConfigurationArgs:
    def __init__(__self__, *, deployment_type: pulumi.Input[_builtins.str], metadata_configurations: pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationMetadataConfigurationArgs]]], per_unit_storage_throughput: pulumi.Input[_builtins.int], log_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationLogConfigurationArgs]]]] = ..., mount_name: Optional[pulumi.Input[_builtins.str]] = ..., weekly_maintenance_start_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @deployment_type.setter
    def deployment_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataConfigurations")
    def metadata_configurations(self) -> pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationMetadataConfigurationArgs]]]:
        
        ...
    
    @metadata_configurations.setter
    def metadata_configurations(self, value: pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationMetadataConfigurationArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="perUnitStorageThroughput")
    def per_unit_storage_throughput(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @per_unit_storage_throughput.setter
    def per_unit_storage_throughput(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfigurations")
    def log_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationLogConfigurationArgs]]]]:
        ...
    
    @log_configurations.setter
    def log_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FileCacheLustreConfigurationLogConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountName")
    def mount_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @mount_name.setter
    def mount_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceStartTime")
    def weekly_maintenance_start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @weekly_maintenance_start_time.setter
    def weekly_maintenance_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FileCacheLustreConfigurationLogConfigurationArgsDict(TypedDict):
    destination: NotRequired[pulumi.Input[_builtins.str]]
    level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FileCacheLustreConfigurationLogConfigurationArgs:
    def __init__(__self__, *, destination: Optional[pulumi.Input[_builtins.str]] = ..., level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @level.setter
    def level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FileCacheLustreConfigurationMetadataConfigurationArgsDict(TypedDict):
    storage_capacity: pulumi.Input[_builtins.int]


@pulumi.input_type
class FileCacheLustreConfigurationMetadataConfigurationArgs:
    def __init__(__self__, *, storage_capacity: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacity")
    def storage_capacity(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @storage_capacity.setter
    def storage_capacity(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class LustreFileSystemDataReadCacheConfigurationArgsDict(TypedDict):
    sizing_mode: pulumi.Input[_builtins.str]
    size: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LustreFileSystemDataReadCacheConfigurationArgs:
    def __init__(__self__, *, sizing_mode: pulumi.Input[_builtins.str], size: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingMode")
    def sizing_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sizing_mode.setter
    def sizing_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class LustreFileSystemLogConfigurationArgsDict(TypedDict):
    destination: NotRequired[pulumi.Input[_builtins.str]]
    level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LustreFileSystemLogConfigurationArgs:
    def __init__(__self__, *, destination: Optional[pulumi.Input[_builtins.str]] = ..., level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @level.setter
    def level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LustreFileSystemMetadataConfigurationArgsDict(TypedDict):
    iops: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LustreFileSystemMetadataConfigurationArgs:
    def __init__(__self__, *, iops: Optional[pulumi.Input[_builtins.int]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LustreFileSystemRootSquashConfigurationArgsDict(TypedDict):
    no_squash_nids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    root_squash: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LustreFileSystemRootSquashConfigurationArgs:
    def __init__(__self__, *, no_squash_nids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., root_squash: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noSquashNids")
    def no_squash_nids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @no_squash_nids.setter
    def no_squash_nids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootSquash")
    def root_squash(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @root_squash.setter
    def root_squash(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OntapFileSystemDiskIopsConfigurationArgsDict(TypedDict):
    iops: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OntapFileSystemDiskIopsConfigurationArgs:
    def __init__(__self__, *, iops: Optional[pulumi.Input[_builtins.int]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OntapFileSystemEndpointArgsDict(TypedDict):
    interclusters: NotRequired[pulumi.Input[Sequence[pulumi.Input[OntapFileSystemEndpointInterclusterArgsDict]]]]
    managements: NotRequired[pulumi.Input[Sequence[pulumi.Input[OntapFileSystemEndpointManagementArgsDict]]]]


@pulumi.input_type
class OntapFileSystemEndpointArgs:
    def __init__(__self__, *, interclusters: Optional[pulumi.Input[Sequence[pulumi.Input[OntapFileSystemEndpointInterclusterArgs]]]] = ..., managements: Optional[pulumi.Input[Sequence[pulumi.Input[OntapFileSystemEndpointManagementArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interclusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OntapFileSystemEndpointInterclusterArgs]]]]:
        
        ...
    
    @interclusters.setter
    def interclusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OntapFileSystemEndpointInterclusterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def managements(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OntapFileSystemEndpointManagementArgs]]]]:
        
        ...
    
    @managements.setter
    def managements(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OntapFileSystemEndpointManagementArgs]]]]): # -> None:
        ...
    


class OntapFileSystemEndpointInterclusterArgsDict(TypedDict):
    dns_name: NotRequired[pulumi.Input[_builtins.str]]
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class OntapFileSystemEndpointInterclusterArgs:
    def __init__(__self__, *, dns_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_addresses.setter
    def ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class OntapFileSystemEndpointManagementArgsDict(TypedDict):
    dns_name: NotRequired[pulumi.Input[_builtins.str]]
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class OntapFileSystemEndpointManagementArgs:
    def __init__(__self__, *, dns_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_addresses.setter
    def ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class OntapStorageVirtualMachineActiveDirectoryConfigurationArgsDict(TypedDict):
    netbios_name: NotRequired[pulumi.Input[_builtins.str]]
    self_managed_active_directory_configuration: NotRequired[pulumi.Input[OntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationArgsDict]]


@pulumi.input_type
class OntapStorageVirtualMachineActiveDirectoryConfigurationArgs:
    def __init__(__self__, *, netbios_name: Optional[pulumi.Input[_builtins.str]] = ..., self_managed_active_directory_configuration: Optional[pulumi.Input[OntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="netbiosName")
    def netbios_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @netbios_name.setter
    def netbios_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfManagedActiveDirectoryConfiguration")
    def self_managed_active_directory_configuration(self) -> Optional[pulumi.Input[OntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationArgs]]:
        ...
    
    @self_managed_active_directory_configuration.setter
    def self_managed_active_directory_configuration(self, value: Optional[pulumi.Input[OntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationArgs]]): # -> None:
        ...
    


class OntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationArgsDict(TypedDict):
    dns_ips: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    domain_name: pulumi.Input[_builtins.str]
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]
    file_system_administrators_group: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit_distinguished_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OntapStorageVirtualMachineActiveDirectoryConfigurationSelfManagedActiveDirectoryConfigurationArgs:
    def __init__(__self__, *, dns_ips: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], domain_name: pulumi.Input[_builtins.str], password: pulumi.Input[_builtins.str], username: pulumi.Input[_builtins.str], file_system_administrators_group: Optional[pulumi.Input[_builtins.str]] = ..., organizational_unit_distinguished_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @dns_ips.setter
    def dns_ips(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemAdministratorsGroup")
    def file_system_administrators_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_system_administrators_group.setter
    def file_system_administrators_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organizational_unit_distinguished_name.setter
    def organizational_unit_distinguished_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OntapStorageVirtualMachineEndpointArgsDict(TypedDict):
    iscsis: NotRequired[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointIscsiArgsDict]]]]
    managements: NotRequired[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointManagementArgsDict]]]]
    nfs: NotRequired[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointNfArgsDict]]]]
    smbs: NotRequired[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointSmbArgsDict]]]]


@pulumi.input_type
class OntapStorageVirtualMachineEndpointArgs:
    def __init__(__self__, *, iscsis: Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointIscsiArgs]]]] = ..., managements: Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointManagementArgs]]]] = ..., nfs: Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointNfArgs]]]] = ..., smbs: Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointSmbArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iscsis(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointIscsiArgs]]]]:
        
        ...
    
    @iscsis.setter
    def iscsis(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointIscsiArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def managements(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointManagementArgs]]]]:
        
        ...
    
    @managements.setter
    def managements(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointManagementArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointNfArgs]]]]:
        
        ...
    
    @nfs.setter
    def nfs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointNfArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def smbs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointSmbArgs]]]]:
        
        ...
    
    @smbs.setter
    def smbs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OntapStorageVirtualMachineEndpointSmbArgs]]]]): # -> None:
        ...
    


class OntapStorageVirtualMachineEndpointIscsiArgsDict(TypedDict):
    dns_name: NotRequired[pulumi.Input[_builtins.str]]
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class OntapStorageVirtualMachineEndpointIscsiArgs:
    def __init__(__self__, *, dns_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_addresses.setter
    def ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class OntapStorageVirtualMachineEndpointManagementArgsDict(TypedDict):
    dns_name: NotRequired[pulumi.Input[_builtins.str]]
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class OntapStorageVirtualMachineEndpointManagementArgs:
    def __init__(__self__, *, dns_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_addresses.setter
    def ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class OntapStorageVirtualMachineEndpointNfArgsDict(TypedDict):
    dns_name: NotRequired[pulumi.Input[_builtins.str]]
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class OntapStorageVirtualMachineEndpointNfArgs:
    def __init__(__self__, *, dns_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_addresses.setter
    def ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class OntapStorageVirtualMachineEndpointSmbArgsDict(TypedDict):
    dns_name: NotRequired[pulumi.Input[_builtins.str]]
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class OntapStorageVirtualMachineEndpointSmbArgs:
    def __init__(__self__, *, dns_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_addresses.setter
    def ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class OntapVolumeAggregateConfigurationArgsDict(TypedDict):
    aggregates: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    constituents_per_aggregate: NotRequired[pulumi.Input[_builtins.int]]
    total_constituents: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class OntapVolumeAggregateConfigurationArgs:
    def __init__(__self__, *, aggregates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., constituents_per_aggregate: Optional[pulumi.Input[_builtins.int]] = ..., total_constituents: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aggregates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @aggregates.setter
    def aggregates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="constituentsPerAggregate")
    def constituents_per_aggregate(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @constituents_per_aggregate.setter
    def constituents_per_aggregate(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalConstituents")
    def total_constituents(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @total_constituents.setter
    def total_constituents(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class OntapVolumeSnaplockConfigurationArgsDict(TypedDict):
    snaplock_type: pulumi.Input[_builtins.str]
    audit_log_volume: NotRequired[pulumi.Input[_builtins.bool]]
    autocommit_period: NotRequired[pulumi.Input[OntapVolumeSnaplockConfigurationAutocommitPeriodArgsDict]]
    privileged_delete: NotRequired[pulumi.Input[_builtins.str]]
    retention_period: NotRequired[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodArgsDict]]
    volume_append_mode_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class OntapVolumeSnaplockConfigurationArgs:
    def __init__(__self__, *, snaplock_type: pulumi.Input[_builtins.str], audit_log_volume: Optional[pulumi.Input[_builtins.bool]] = ..., autocommit_period: Optional[pulumi.Input[OntapVolumeSnaplockConfigurationAutocommitPeriodArgs]] = ..., privileged_delete: Optional[pulumi.Input[_builtins.str]] = ..., retention_period: Optional[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodArgs]] = ..., volume_append_mode_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snaplockType")
    def snaplock_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @snaplock_type.setter
    def snaplock_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditLogVolume")
    def audit_log_volume(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @audit_log_volume.setter
    def audit_log_volume(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autocommitPeriod")
    def autocommit_period(self) -> Optional[pulumi.Input[OntapVolumeSnaplockConfigurationAutocommitPeriodArgs]]:
        
        ...
    
    @autocommit_period.setter
    def autocommit_period(self, value: Optional[pulumi.Input[OntapVolumeSnaplockConfigurationAutocommitPeriodArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privilegedDelete")
    def privileged_delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @privileged_delete.setter
    def privileged_delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodArgs]]:
        
        ...
    
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeAppendModeEnabled")
    def volume_append_mode_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @volume_append_mode_enabled.setter
    def volume_append_mode_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class OntapVolumeSnaplockConfigurationAutocommitPeriodArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class OntapVolumeSnaplockConfigurationAutocommitPeriodArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class OntapVolumeSnaplockConfigurationRetentionPeriodArgsDict(TypedDict):
    default_retention: NotRequired[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodDefaultRetentionArgsDict]]
    maximum_retention: NotRequired[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodMaximumRetentionArgsDict]]
    minimum_retention: NotRequired[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodMinimumRetentionArgsDict]]


@pulumi.input_type
class OntapVolumeSnaplockConfigurationRetentionPeriodArgs:
    def __init__(__self__, *, default_retention: Optional[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodDefaultRetentionArgs]] = ..., maximum_retention: Optional[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodMaximumRetentionArgs]] = ..., minimum_retention: Optional[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodMinimumRetentionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRetention")
    def default_retention(self) -> Optional[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodDefaultRetentionArgs]]:
        
        ...
    
    @default_retention.setter
    def default_retention(self, value: Optional[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodDefaultRetentionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRetention")
    def maximum_retention(self) -> Optional[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodMaximumRetentionArgs]]:
        
        ...
    
    @maximum_retention.setter
    def maximum_retention(self, value: Optional[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodMaximumRetentionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumRetention")
    def minimum_retention(self) -> Optional[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodMinimumRetentionArgs]]:
        
        ...
    
    @minimum_retention.setter
    def minimum_retention(self, value: Optional[pulumi.Input[OntapVolumeSnaplockConfigurationRetentionPeriodMinimumRetentionArgs]]): # -> None:
        ...
    


class OntapVolumeSnaplockConfigurationRetentionPeriodDefaultRetentionArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class OntapVolumeSnaplockConfigurationRetentionPeriodDefaultRetentionArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class OntapVolumeSnaplockConfigurationRetentionPeriodMaximumRetentionArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class OntapVolumeSnaplockConfigurationRetentionPeriodMaximumRetentionArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class OntapVolumeSnaplockConfigurationRetentionPeriodMinimumRetentionArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class OntapVolumeSnaplockConfigurationRetentionPeriodMinimumRetentionArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class OntapVolumeTieringPolicyArgsDict(TypedDict):
    cooling_period: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OntapVolumeTieringPolicyArgs:
    def __init__(__self__, *, cooling_period: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coolingPeriod")
    def cooling_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cooling_period.setter
    def cooling_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OpenZfsFileSystemDiskIopsConfigurationArgsDict(TypedDict):
    iops: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OpenZfsFileSystemDiskIopsConfigurationArgs:
    def __init__(__self__, *, iops: Optional[pulumi.Input[_builtins.int]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OpenZfsFileSystemReadCacheConfigurationArgsDict(TypedDict):
    size: NotRequired[pulumi.Input[_builtins.int]]
    sizing_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OpenZfsFileSystemReadCacheConfigurationArgs:
    def __init__(__self__, *, size: Optional[pulumi.Input[_builtins.int]] = ..., sizing_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizingMode")
    def sizing_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sizing_mode.setter
    def sizing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OpenZfsFileSystemRootVolumeConfigurationArgsDict(TypedDict):
    copy_tags_to_snapshots: NotRequired[pulumi.Input[_builtins.bool]]
    data_compression_type: NotRequired[pulumi.Input[_builtins.str]]
    nfs_exports: NotRequired[pulumi.Input[OpenZfsFileSystemRootVolumeConfigurationNfsExportsArgsDict]]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]
    record_size_kib: NotRequired[pulumi.Input[_builtins.int]]
    user_and_group_quotas: NotRequired[pulumi.Input[Sequence[pulumi.Input[OpenZfsFileSystemRootVolumeConfigurationUserAndGroupQuotaArgsDict]]]]


@pulumi.input_type
class OpenZfsFileSystemRootVolumeConfigurationArgs:
    def __init__(__self__, *, copy_tags_to_snapshots: Optional[pulumi.Input[_builtins.bool]] = ..., data_compression_type: Optional[pulumi.Input[_builtins.str]] = ..., nfs_exports: Optional[pulumi.Input[OpenZfsFileSystemRootVolumeConfigurationNfsExportsArgs]] = ..., read_only: Optional[pulumi.Input[_builtins.bool]] = ..., record_size_kib: Optional[pulumi.Input[_builtins.int]] = ..., user_and_group_quotas: Optional[pulumi.Input[Sequence[pulumi.Input[OpenZfsFileSystemRootVolumeConfigurationUserAndGroupQuotaArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyTagsToSnapshots")
    def copy_tags_to_snapshots(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @copy_tags_to_snapshots.setter
    def copy_tags_to_snapshots(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCompressionType")
    def data_compression_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_compression_type.setter
    def data_compression_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nfsExports")
    def nfs_exports(self) -> Optional[pulumi.Input[OpenZfsFileSystemRootVolumeConfigurationNfsExportsArgs]]:
        
        ...
    
    @nfs_exports.setter
    def nfs_exports(self, value: Optional[pulumi.Input[OpenZfsFileSystemRootVolumeConfigurationNfsExportsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordSizeKib")
    def record_size_kib(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @record_size_kib.setter
    def record_size_kib(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAndGroupQuotas")
    def user_and_group_quotas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OpenZfsFileSystemRootVolumeConfigurationUserAndGroupQuotaArgs]]]]:
        
        ...
    
    @user_and_group_quotas.setter
    def user_and_group_quotas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OpenZfsFileSystemRootVolumeConfigurationUserAndGroupQuotaArgs]]]]): # -> None:
        ...
    


class OpenZfsFileSystemRootVolumeConfigurationNfsExportsArgsDict(TypedDict):
    client_configurations: pulumi.Input[Sequence[pulumi.Input[OpenZfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationArgsDict]]]


@pulumi.input_type
class OpenZfsFileSystemRootVolumeConfigurationNfsExportsArgs:
    def __init__(__self__, *, client_configurations: pulumi.Input[Sequence[pulumi.Input[OpenZfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientConfigurations")
    def client_configurations(self) -> pulumi.Input[Sequence[pulumi.Input[OpenZfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationArgs]]]:
        
        ...
    
    @client_configurations.setter
    def client_configurations(self, value: pulumi.Input[Sequence[pulumi.Input[OpenZfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationArgs]]]): # -> None:
        ...
    


class OpenZfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationArgsDict(TypedDict):
    clients: pulumi.Input[_builtins.str]
    options: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class OpenZfsFileSystemRootVolumeConfigurationNfsExportsClientConfigurationArgs:
    def __init__(__self__, *, clients: pulumi.Input[_builtins.str], options: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clients(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @clients.setter
    def clients(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @options.setter
    def options(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class OpenZfsFileSystemRootVolumeConfigurationUserAndGroupQuotaArgsDict(TypedDict):
    id: pulumi.Input[_builtins.int]
    storage_capacity_quota_gib: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class OpenZfsFileSystemRootVolumeConfigurationUserAndGroupQuotaArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.int], storage_capacity_quota_gib: pulumi.Input[_builtins.int], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacityQuotaGib")
    def storage_capacity_quota_gib(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @storage_capacity_quota_gib.setter
    def storage_capacity_quota_gib(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class OpenZfsVolumeNfsExportsArgsDict(TypedDict):
    client_configurations: pulumi.Input[Sequence[pulumi.Input[OpenZfsVolumeNfsExportsClientConfigurationArgsDict]]]


@pulumi.input_type
class OpenZfsVolumeNfsExportsArgs:
    def __init__(__self__, *, client_configurations: pulumi.Input[Sequence[pulumi.Input[OpenZfsVolumeNfsExportsClientConfigurationArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientConfigurations")
    def client_configurations(self) -> pulumi.Input[Sequence[pulumi.Input[OpenZfsVolumeNfsExportsClientConfigurationArgs]]]:
        
        ...
    
    @client_configurations.setter
    def client_configurations(self, value: pulumi.Input[Sequence[pulumi.Input[OpenZfsVolumeNfsExportsClientConfigurationArgs]]]): # -> None:
        ...
    


class OpenZfsVolumeNfsExportsClientConfigurationArgsDict(TypedDict):
    clients: pulumi.Input[_builtins.str]
    options: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class OpenZfsVolumeNfsExportsClientConfigurationArgs:
    def __init__(__self__, *, clients: pulumi.Input[_builtins.str], options: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clients(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @clients.setter
    def clients(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @options.setter
    def options(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class OpenZfsVolumeOriginSnapshotArgsDict(TypedDict):
    copy_strategy: pulumi.Input[_builtins.str]
    snapshot_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class OpenZfsVolumeOriginSnapshotArgs:
    def __init__(__self__, *, copy_strategy: pulumi.Input[_builtins.str], snapshot_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyStrategy")
    def copy_strategy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @copy_strategy.setter
    def copy_strategy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotArn")
    def snapshot_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @snapshot_arn.setter
    def snapshot_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class OpenZfsVolumeUserAndGroupQuotaArgsDict(TypedDict):
    id: pulumi.Input[_builtins.int]
    storage_capacity_quota_gib: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class OpenZfsVolumeUserAndGroupQuotaArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.int], storage_capacity_quota_gib: pulumi.Input[_builtins.int], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacityQuotaGib")
    def storage_capacity_quota_gib(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @storage_capacity_quota_gib.setter
    def storage_capacity_quota_gib(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class S3AccessPointAttachmentOpenzfsConfigurationArgsDict(TypedDict):
    file_system_identity: pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityArgsDict]
    volume_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class S3AccessPointAttachmentOpenzfsConfigurationArgs:
    def __init__(__self__, *, file_system_identity: pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityArgs], volume_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemIdentity")
    def file_system_identity(self) -> pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityArgs]:
        
        ...
    
    @file_system_identity.setter
    def file_system_identity(self, value: pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @volume_id.setter
    def volume_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    posix_user: NotRequired[pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityPosixUserArgsDict]]


@pulumi.input_type
class S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], posix_user: Optional[pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityPosixUserArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixUser")
    def posix_user(self) -> Optional[pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityPosixUserArgs]]:
        
        ...
    
    @posix_user.setter
    def posix_user(self, value: Optional[pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityPosixUserArgs]]): # -> None:
        ...
    


class S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityPosixUserArgsDict(TypedDict):
    gid: pulumi.Input[_builtins.int]
    uid: pulumi.Input[_builtins.int]
    secondary_gids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]


@pulumi.input_type
class S3AccessPointAttachmentOpenzfsConfigurationFileSystemIdentityPosixUserArgs:
    def __init__(__self__, *, gid: pulumi.Input[_builtins.int], uid: pulumi.Input[_builtins.int], secondary_gids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gid(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @gid.setter
    def gid(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @uid.setter
    def uid(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @secondary_gids.setter
    def secondary_gids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    


class S3AccessPointAttachmentS3AccessPointArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[_builtins.str]]
    vpc_configuration: NotRequired[pulumi.Input[S3AccessPointAttachmentS3AccessPointVpcConfigurationArgsDict]]


@pulumi.input_type
class S3AccessPointAttachmentS3AccessPointArgs:
    def __init__(__self__, *, policy: Optional[pulumi.Input[_builtins.str]] = ..., vpc_configuration: Optional[pulumi.Input[S3AccessPointAttachmentS3AccessPointVpcConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(self) -> Optional[pulumi.Input[S3AccessPointAttachmentS3AccessPointVpcConfigurationArgs]]:
        
        ...
    
    @vpc_configuration.setter
    def vpc_configuration(self, value: Optional[pulumi.Input[S3AccessPointAttachmentS3AccessPointVpcConfigurationArgs]]): # -> None:
        ...
    


class S3AccessPointAttachmentS3AccessPointVpcConfigurationArgsDict(TypedDict):
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class S3AccessPointAttachmentS3AccessPointVpcConfigurationArgs:
    def __init__(__self__, *, vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class S3AccessPointAttachmentTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class S3AccessPointAttachmentTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WindowsFileSystemAuditLogConfigurationArgsDict(TypedDict):
    audit_log_destination: NotRequired[pulumi.Input[_builtins.str]]
    file_access_audit_log_level: NotRequired[pulumi.Input[_builtins.str]]
    file_share_access_audit_log_level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WindowsFileSystemAuditLogConfigurationArgs:
    def __init__(__self__, *, audit_log_destination: Optional[pulumi.Input[_builtins.str]] = ..., file_access_audit_log_level: Optional[pulumi.Input[_builtins.str]] = ..., file_share_access_audit_log_level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditLogDestination")
    def audit_log_destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @audit_log_destination.setter
    def audit_log_destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileAccessAuditLogLevel")
    def file_access_audit_log_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_access_audit_log_level.setter
    def file_access_audit_log_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShareAccessAuditLogLevel")
    def file_share_access_audit_log_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_share_access_audit_log_level.setter
    def file_share_access_audit_log_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WindowsFileSystemDiskIopsConfigurationArgsDict(TypedDict):
    iops: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WindowsFileSystemDiskIopsConfigurationArgs:
    def __init__(__self__, *, iops: Optional[pulumi.Input[_builtins.int]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WindowsFileSystemSelfManagedActiveDirectoryArgsDict(TypedDict):
    dns_ips: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    domain_name: pulumi.Input[_builtins.str]
    domain_join_service_account_secret: NotRequired[pulumi.Input[_builtins.str]]
    file_system_administrators_group: NotRequired[pulumi.Input[_builtins.str]]
    organizational_unit_distinguished_name: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WindowsFileSystemSelfManagedActiveDirectoryArgs:
    def __init__(__self__, *, dns_ips: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], domain_name: pulumi.Input[_builtins.str], domain_join_service_account_secret: Optional[pulumi.Input[_builtins.str]] = ..., file_system_administrators_group: Optional[pulumi.Input[_builtins.str]] = ..., organizational_unit_distinguished_name: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsIps")
    def dns_ips(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @dns_ips.setter
    def dns_ips(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainJoinServiceAccountSecret")
    def domain_join_service_account_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_join_service_account_secret.setter
    def domain_join_service_account_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemAdministratorsGroup")
    def file_system_administrators_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_system_administrators_group.setter
    def file_system_administrators_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationalUnitDistinguishedName")
    def organizational_unit_distinguished_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @organizational_unit_distinguished_name.setter
    def organizational_unit_distinguished_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GetOntapStorageVirtualMachineFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetOntapStorageVirtualMachineFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetOntapStorageVirtualMachinesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetOntapStorageVirtualMachinesFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetOpenZfsSnapshotFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetOpenZfsSnapshotFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


