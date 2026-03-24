

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
__all__ = ['CloudVmClusterArgs', 'CloudVmCluster']
@pulumi.input_type
class CloudVmClusterArgs:
    def __init__(__self__, *, cpu_core_count: pulumi.Input[_builtins.int], data_collection_options: pulumi.Input[CloudVmClusterDataCollectionOptionsArgs], data_storage_size_in_tbs: pulumi.Input[_builtins.float], db_servers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], display_name: pulumi.Input[_builtins.str], gi_version: pulumi.Input[_builtins.str], hostname_prefix: pulumi.Input[_builtins.str], ssh_public_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], cloud_exadata_infrastructure_arn: Optional[pulumi.Input[_builtins.str]] = ..., cloud_exadata_infrastructure_id: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., db_node_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., is_local_backup_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., is_sparse_diskgroup_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., license_model: Optional[pulumi.Input[_builtins.str]] = ..., memory_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., odb_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scan_listener_port_tcp: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[CloudVmClusterTimeoutsArgs]] = ..., timezone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @cpu_core_count.setter
    def cpu_core_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionOptions")
    def data_collection_options(self) -> pulumi.Input[CloudVmClusterDataCollectionOptionsArgs]:
        
        ...
    
    @data_collection_options.setter
    def data_collection_options(self, value: pulumi.Input[CloudVmClusterDataCollectionOptionsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInTbs")
    def data_storage_size_in_tbs(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbServers")
    def db_servers(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @db_servers.setter
    def db_servers(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="giVersion")
    def gi_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gi_version.setter
    def gi_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hostname_prefix.setter
    def hostname_prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @ssh_public_keys.setter
    def ssh_public_keys(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureArn")
    def cloud_exadata_infrastructure_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_exadata_infrastructure_arn.setter
    def cloud_exadata_infrastructure_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureId")
    def cloud_exadata_infrastructure_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_exadata_infrastructure_id.setter
    def cloud_exadata_infrastructure_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeInGbs")
    def db_node_storage_size_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @db_node_storage_size_in_gbs.setter
    def db_node_storage_size_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLocalBackupEnabled")
    def is_local_backup_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_local_backup_enabled.setter
    def is_local_backup_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSparseDiskgroupEnabled")
    def is_sparse_diskgroup_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_sparse_diskgroup_enabled.setter
    def is_sparse_diskgroup_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @license_model.setter
    def license_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySizeInGbs")
    def memory_size_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbNetworkArn")
    def odb_network_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @odb_network_arn.setter
    def odb_network_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbNetworkId")
    def odb_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @odb_network_id.setter
    def odb_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcp")
    def scan_listener_port_tcp(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @scan_listener_port_tcp.setter
    def scan_listener_port_tcp(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[CloudVmClusterTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[CloudVmClusterTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CloudVmClusterState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., cloud_exadata_infrastructure_arn: Optional[pulumi.Input[_builtins.str]] = ..., cloud_exadata_infrastructure_id: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., compute_model: Optional[pulumi.Input[_builtins.str]] = ..., cpu_core_count: Optional[pulumi.Input[_builtins.int]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., data_collection_options: Optional[pulumi.Input[CloudVmClusterDataCollectionOptionsArgs]] = ..., data_storage_size_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., db_node_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., db_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., disk_redundancy: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., gi_version: Optional[pulumi.Input[_builtins.str]] = ..., gi_version_computed: Optional[pulumi.Input[_builtins.str]] = ..., hostname_prefix: Optional[pulumi.Input[_builtins.str]] = ..., hostname_prefix_computed: Optional[pulumi.Input[_builtins.str]] = ..., iorm_config_caches: Optional[pulumi.Input[Sequence[pulumi.Input[CloudVmClusterIormConfigCacheArgs]]]] = ..., is_local_backup_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., is_sparse_diskgroup_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., last_update_history_entry_id: Optional[pulumi.Input[_builtins.str]] = ..., license_model: Optional[pulumi.Input[_builtins.str]] = ..., listener_port: Optional[pulumi.Input[_builtins.int]] = ..., memory_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., oci_resource_anchor_name: Optional[pulumi.Input[_builtins.str]] = ..., oci_url: Optional[pulumi.Input[_builtins.str]] = ..., ocid: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_id: Optional[pulumi.Input[_builtins.str]] = ..., percent_progress: Optional[pulumi.Input[_builtins.float]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scan_dns_name: Optional[pulumi.Input[_builtins.str]] = ..., scan_dns_record_id: Optional[pulumi.Input[_builtins.str]] = ..., scan_ip_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., scan_listener_port_tcp: Optional[pulumi.Input[_builtins.int]] = ..., shape: Optional[pulumi.Input[_builtins.str]] = ..., ssh_public_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_reason: Optional[pulumi.Input[_builtins.str]] = ..., storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., system_version: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[CloudVmClusterTimeoutsArgs]] = ..., timezone: Optional[pulumi.Input[_builtins.str]] = ..., vip_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureArn")
    def cloud_exadata_infrastructure_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_exadata_infrastructure_arn.setter
    def cloud_exadata_infrastructure_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureId")
    def cloud_exadata_infrastructure_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloud_exadata_infrastructure_id.setter
    def cloud_exadata_infrastructure_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compute_model.setter
    def compute_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cpu_core_count.setter
    def cpu_core_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionOptions")
    def data_collection_options(self) -> Optional[pulumi.Input[CloudVmClusterDataCollectionOptionsArgs]]:
        
        ...
    
    @data_collection_options.setter
    def data_collection_options(self, value: Optional[pulumi.Input[CloudVmClusterDataCollectionOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInTbs")
    def data_storage_size_in_tbs(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeInGbs")
    def db_node_storage_size_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @db_node_storage_size_in_gbs.setter
    def db_node_storage_size_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbServers")
    def db_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @db_servers.setter
    def db_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskRedundancy")
    def disk_redundancy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_redundancy.setter
    def disk_redundancy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="giVersion")
    def gi_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gi_version.setter
    def gi_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="giVersionComputed")
    def gi_version_computed(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gi_version_computed.setter
    def gi_version_computed(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hostname_prefix.setter
    def hostname_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnamePrefixComputed")
    def hostname_prefix_computed(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hostname_prefix_computed.setter
    def hostname_prefix_computed(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iormConfigCaches")
    def iorm_config_caches(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CloudVmClusterIormConfigCacheArgs]]]]:
        
        ...
    
    @iorm_config_caches.setter
    def iorm_config_caches(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CloudVmClusterIormConfigCacheArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLocalBackupEnabled")
    def is_local_backup_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_local_backup_enabled.setter
    def is_local_backup_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSparseDiskgroupEnabled")
    def is_sparse_diskgroup_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_sparse_diskgroup_enabled.setter
    def is_sparse_diskgroup_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdateHistoryEntryId")
    def last_update_history_entry_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_update_history_entry_id.setter
    def last_update_history_entry_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @license_model.setter
    def license_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerPort")
    def listener_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @listener_port.setter
    def listener_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySizeInGbs")
    def memory_size_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oci_resource_anchor_name.setter
    def oci_resource_anchor_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oci_url.setter
    def oci_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ocid.setter
    def ocid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbNetworkArn")
    def odb_network_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @odb_network_arn.setter
    def odb_network_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbNetworkId")
    def odb_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @odb_network_id.setter
    def odb_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @percent_progress.setter
    def percent_progress(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanDnsName")
    def scan_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scan_dns_name.setter
    def scan_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanDnsRecordId")
    def scan_dns_record_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scan_dns_record_id.setter
    def scan_dns_record_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanIpIds")
    def scan_ip_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scan_ip_ids.setter
    def scan_ip_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcp")
    def scan_listener_port_tcp(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @scan_listener_port_tcp.setter
    def scan_listener_port_tcp(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shape.setter
    def shape(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ssh_public_keys.setter
    def ssh_public_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_reason.setter
    def status_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSizeInGbs")
    def storage_size_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_size_in_gbs.setter
    def storage_size_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemVersion")
    def system_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @system_version.setter
    def system_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[CloudVmClusterTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[CloudVmClusterTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vipIds")
    def vip_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vip_ids.setter
    def vip_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:odb/cloudVmCluster:CloudVmCluster")
class CloudVmCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cloud_exadata_infrastructure_arn: Optional[pulumi.Input[_builtins.str]] = ..., cloud_exadata_infrastructure_id: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., cpu_core_count: Optional[pulumi.Input[_builtins.int]] = ..., data_collection_options: Optional[pulumi.Input[Union[CloudVmClusterDataCollectionOptionsArgs, CloudVmClusterDataCollectionOptionsArgsDict]]] = ..., data_storage_size_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., db_node_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., db_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., gi_version: Optional[pulumi.Input[_builtins.str]] = ..., hostname_prefix: Optional[pulumi.Input[_builtins.str]] = ..., is_local_backup_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., is_sparse_diskgroup_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., license_model: Optional[pulumi.Input[_builtins.str]] = ..., memory_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., odb_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scan_listener_port_tcp: Optional[pulumi.Input[_builtins.int]] = ..., ssh_public_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[CloudVmClusterTimeoutsArgs, CloudVmClusterTimeoutsArgsDict]]] = ..., timezone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CloudVmClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., cloud_exadata_infrastructure_arn: Optional[pulumi.Input[_builtins.str]] = ..., cloud_exadata_infrastructure_id: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., compute_model: Optional[pulumi.Input[_builtins.str]] = ..., cpu_core_count: Optional[pulumi.Input[_builtins.int]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., data_collection_options: Optional[pulumi.Input[Union[CloudVmClusterDataCollectionOptionsArgs, CloudVmClusterDataCollectionOptionsArgsDict]]] = ..., data_storage_size_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., db_node_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., db_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., disk_redundancy: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., gi_version: Optional[pulumi.Input[_builtins.str]] = ..., gi_version_computed: Optional[pulumi.Input[_builtins.str]] = ..., hostname_prefix: Optional[pulumi.Input[_builtins.str]] = ..., hostname_prefix_computed: Optional[pulumi.Input[_builtins.str]] = ..., iorm_config_caches: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CloudVmClusterIormConfigCacheArgs, CloudVmClusterIormConfigCacheArgsDict]]]]] = ..., is_local_backup_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., is_sparse_diskgroup_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., last_update_history_entry_id: Optional[pulumi.Input[_builtins.str]] = ..., license_model: Optional[pulumi.Input[_builtins.str]] = ..., listener_port: Optional[pulumi.Input[_builtins.int]] = ..., memory_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., oci_resource_anchor_name: Optional[pulumi.Input[_builtins.str]] = ..., oci_url: Optional[pulumi.Input[_builtins.str]] = ..., ocid: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_id: Optional[pulumi.Input[_builtins.str]] = ..., percent_progress: Optional[pulumi.Input[_builtins.float]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scan_dns_name: Optional[pulumi.Input[_builtins.str]] = ..., scan_dns_record_id: Optional[pulumi.Input[_builtins.str]] = ..., scan_ip_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., scan_listener_port_tcp: Optional[pulumi.Input[_builtins.int]] = ..., shape: Optional[pulumi.Input[_builtins.str]] = ..., ssh_public_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_reason: Optional[pulumi.Input[_builtins.str]] = ..., storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., system_version: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[CloudVmClusterTimeoutsArgs, CloudVmClusterTimeoutsArgsDict]]] = ..., timezone: Optional[pulumi.Input[_builtins.str]] = ..., vip_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> CloudVmCluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureArn")
    def cloud_exadata_infrastructure_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureId")
    def cloud_exadata_infrastructure_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCollectionOptions")
    def data_collection_options(self) -> pulumi.Output[outputs.CloudVmClusterDataCollectionOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInTbs")
    def data_storage_size_in_tbs(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeInGbs")
    def db_node_storage_size_in_gbs(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbServers")
    def db_servers(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskRedundancy")
    def disk_redundancy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="giVersion")
    def gi_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="giVersionComputed")
    def gi_version_computed(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostnamePrefixComputed")
    def hostname_prefix_computed(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iormConfigCaches")
    def iorm_config_caches(self) -> pulumi.Output[Sequence[outputs.CloudVmClusterIormConfigCache]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLocalBackupEnabled")
    def is_local_backup_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSparseDiskgroupEnabled")
    def is_sparse_diskgroup_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdateHistoryEntryId")
    def last_update_history_entry_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listenerPort")
    def listener_port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorySizeInGbs")
    def memory_size_in_gbs(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociResourceAnchorName")
    def oci_resource_anchor_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbNetworkArn")
    def odb_network_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="odbNetworkId")
    def odb_network_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanDnsName")
    def scan_dns_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanDnsRecordId")
    def scan_dns_record_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanIpIds")
    def scan_ip_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcp")
    def scan_listener_port_tcp(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageSizeInGbs")
    def storage_size_in_gbs(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemVersion")
    def system_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.CloudVmClusterTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vipIds")
    def vip_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


