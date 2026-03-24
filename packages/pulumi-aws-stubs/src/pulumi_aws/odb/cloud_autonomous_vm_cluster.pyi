

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
__all__ = ['CloudAutonomousVmClusterArgs', 'CloudAutonomousVmCluster']
@pulumi.input_type
class CloudAutonomousVmClusterArgs:
    def __init__(__self__, *, autonomous_data_storage_size_in_tbs: pulumi.Input[_builtins.float], cpu_core_count_per_node: pulumi.Input[_builtins.int], db_servers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], display_name: pulumi.Input[_builtins.str], maintenance_window: pulumi.Input[CloudAutonomousVmClusterMaintenanceWindowArgs], memory_per_oracle_compute_unit_in_gbs: pulumi.Input[_builtins.int], scan_listener_port_non_tls: pulumi.Input[_builtins.int], scan_listener_port_tls: pulumi.Input[_builtins.int], total_container_databases: pulumi.Input[_builtins.int], cloud_exadata_infrastructure_arn: Optional[pulumi.Input[_builtins.str]] = ..., cloud_exadata_infrastructure_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., is_mtls_enabled_vm_cluster: Optional[pulumi.Input[_builtins.bool]] = ..., license_model: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[CloudAutonomousVmClusterTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autonomousDataStorageSizeInTbs")
    def autonomous_data_storage_size_in_tbs(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @autonomous_data_storage_size_in_tbs.setter
    def autonomous_data_storage_size_in_tbs(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCoreCountPerNode")
    def cpu_core_count_per_node(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @cpu_core_count_per_node.setter
    def cpu_core_count_per_node(self, value: pulumi.Input[_builtins.int]): # -> None:
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
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Input[CloudAutonomousVmClusterMaintenanceWindowArgs]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: pulumi.Input[CloudAutonomousVmClusterMaintenanceWindowArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryPerOracleComputeUnitInGbs")
    def memory_per_oracle_compute_unit_in_gbs(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @memory_per_oracle_compute_unit_in_gbs.setter
    def memory_per_oracle_compute_unit_in_gbs(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanListenerPortNonTls")
    def scan_listener_port_non_tls(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @scan_listener_port_non_tls.setter
    def scan_listener_port_non_tls(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTls")
    def scan_listener_port_tls(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @scan_listener_port_tls.setter
    def scan_listener_port_tls(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalContainerDatabases")
    def total_container_databases(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @total_container_databases.setter
    def total_container_databases(self, value: pulumi.Input[_builtins.int]): # -> None:
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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMtlsEnabledVmCluster")
    def is_mtls_enabled_vm_cluster(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_mtls_enabled_vm_cluster.setter
    def is_mtls_enabled_vm_cluster(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @license_model.setter
    def license_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[CloudAutonomousVmClusterTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[CloudAutonomousVmClusterTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _CloudAutonomousVmClusterState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., autonomous_data_storage_percentage: Optional[pulumi.Input[_builtins.float]] = ..., autonomous_data_storage_size_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., available_autonomous_data_storage_size_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., available_container_databases: Optional[pulumi.Input[_builtins.int]] = ..., available_cpus: Optional[pulumi.Input[_builtins.float]] = ..., cloud_exadata_infrastructure_arn: Optional[pulumi.Input[_builtins.str]] = ..., cloud_exadata_infrastructure_id: Optional[pulumi.Input[_builtins.str]] = ..., compute_model: Optional[pulumi.Input[_builtins.str]] = ..., cpu_core_count: Optional[pulumi.Input[_builtins.int]] = ..., cpu_core_count_per_node: Optional[pulumi.Input[_builtins.int]] = ..., cpu_percentage: Optional[pulumi.Input[_builtins.float]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., data_storage_size_in_gbs: Optional[pulumi.Input[_builtins.float]] = ..., data_storage_size_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., db_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., exadata_storage_in_tbs_lowest_scaled_value: Optional[pulumi.Input[_builtins.float]] = ..., hostname: Optional[pulumi.Input[_builtins.str]] = ..., is_mtls_enabled_vm_cluster: Optional[pulumi.Input[_builtins.bool]] = ..., license_model: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[CloudAutonomousVmClusterMaintenanceWindowArgs]] = ..., max_acds_lowest_scaled_value: Optional[pulumi.Input[_builtins.int]] = ..., memory_per_oracle_compute_unit_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., memory_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., non_provisionable_autonomous_container_databases: Optional[pulumi.Input[_builtins.int]] = ..., oci_resource_anchor_name: Optional[pulumi.Input[_builtins.str]] = ..., oci_url: Optional[pulumi.Input[_builtins.str]] = ..., ocid: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_id: Optional[pulumi.Input[_builtins.str]] = ..., odb_node_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., percent_progress: Optional[pulumi.Input[_builtins.float]] = ..., provisionable_autonomous_container_databases: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_autonomous_container_databases: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_cpus: Optional[pulumi.Input[_builtins.float]] = ..., reclaimable_cpus: Optional[pulumi.Input[_builtins.float]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_cpus: Optional[pulumi.Input[_builtins.float]] = ..., scan_listener_port_non_tls: Optional[pulumi.Input[_builtins.int]] = ..., scan_listener_port_tls: Optional[pulumi.Input[_builtins.int]] = ..., shape: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_reason: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., time_database_ssl_certificate_expires: Optional[pulumi.Input[_builtins.str]] = ..., time_ords_certificate_expires: Optional[pulumi.Input[_builtins.str]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[CloudAutonomousVmClusterTimeoutsArgs]] = ..., total_container_databases: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autonomousDataStoragePercentage")
    def autonomous_data_storage_percentage(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @autonomous_data_storage_percentage.setter
    def autonomous_data_storage_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autonomousDataStorageSizeInTbs")
    def autonomous_data_storage_size_in_tbs(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @autonomous_data_storage_size_in_tbs.setter
    def autonomous_data_storage_size_in_tbs(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableAutonomousDataStorageSizeInTbs")
    def available_autonomous_data_storage_size_in_tbs(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @available_autonomous_data_storage_size_in_tbs.setter
    def available_autonomous_data_storage_size_in_tbs(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableContainerDatabases")
    def available_container_databases(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @available_container_databases.setter
    def available_container_databases(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableCpus")
    def available_cpus(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @available_cpus.setter
    def available_cpus(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
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
    @pulumi.getter(name="cpuCoreCountPerNode")
    def cpu_core_count_per_node(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cpu_core_count_per_node.setter
    def cpu_core_count_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuPercentage")
    def cpu_percentage(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @cpu_percentage.setter
    def cpu_percentage(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInGbs")
    def data_storage_size_in_gbs(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInTbs")
    def data_storage_size_in_tbs(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbServers")
    def db_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @db_servers.setter
    def db_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="exadataStorageInTbsLowestScaledValue")
    def exadata_storage_in_tbs_lowest_scaled_value(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @exadata_storage_in_tbs_lowest_scaled_value.setter
    def exadata_storage_in_tbs_lowest_scaled_value(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMtlsEnabledVmCluster")
    def is_mtls_enabled_vm_cluster(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_mtls_enabled_vm_cluster.setter
    def is_mtls_enabled_vm_cluster(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @license_model.setter
    def license_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[CloudAutonomousVmClusterMaintenanceWindowArgs]]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[CloudAutonomousVmClusterMaintenanceWindowArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAcdsLowestScaledValue")
    def max_acds_lowest_scaled_value(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_acds_lowest_scaled_value.setter
    def max_acds_lowest_scaled_value(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryPerOracleComputeUnitInGbs")
    def memory_per_oracle_compute_unit_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @memory_per_oracle_compute_unit_in_gbs.setter
    def memory_per_oracle_compute_unit_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter(name="nonProvisionableAutonomousContainerDatabases")
    def non_provisionable_autonomous_container_databases(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @non_provisionable_autonomous_container_databases.setter
    def non_provisionable_autonomous_container_databases(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter(name="odbNodeStorageSizeInGbs")
    def odb_node_storage_size_in_gbs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @odb_node_storage_size_in_gbs.setter
    def odb_node_storage_size_in_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @percent_progress.setter
    def percent_progress(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionableAutonomousContainerDatabases")
    def provisionable_autonomous_container_databases(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @provisionable_autonomous_container_databases.setter
    def provisionable_autonomous_container_databases(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedAutonomousContainerDatabases")
    def provisioned_autonomous_container_databases(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @provisioned_autonomous_container_databases.setter
    def provisioned_autonomous_container_databases(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedCpus")
    def provisioned_cpus(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @provisioned_cpus.setter
    def provisioned_cpus(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reclaimableCpus")
    def reclaimable_cpus(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @reclaimable_cpus.setter
    def reclaimable_cpus(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedCpus")
    def reserved_cpus(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @reserved_cpus.setter
    def reserved_cpus(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanListenerPortNonTls")
    def scan_listener_port_non_tls(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @scan_listener_port_non_tls.setter
    def scan_listener_port_non_tls(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTls")
    def scan_listener_port_tls(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @scan_listener_port_tls.setter
    def scan_listener_port_tls(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shape.setter
    def shape(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="timeDatabaseSslCertificateExpires")
    def time_database_ssl_certificate_expires(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_database_ssl_certificate_expires.setter
    def time_database_ssl_certificate_expires(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeOrdsCertificateExpires")
    def time_ords_certificate_expires(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_ords_certificate_expires.setter
    def time_ords_certificate_expires(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[CloudAutonomousVmClusterTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[CloudAutonomousVmClusterTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalContainerDatabases")
    def total_container_databases(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @total_container_databases.setter
    def total_container_databases(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CloudAutonomousVmCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., autonomous_data_storage_size_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., cloud_exadata_infrastructure_arn: Optional[pulumi.Input[_builtins.str]] = ..., cloud_exadata_infrastructure_id: Optional[pulumi.Input[_builtins.str]] = ..., cpu_core_count_per_node: Optional[pulumi.Input[_builtins.int]] = ..., db_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., is_mtls_enabled_vm_cluster: Optional[pulumi.Input[_builtins.bool]] = ..., license_model: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[Union[CloudAutonomousVmClusterMaintenanceWindowArgs, CloudAutonomousVmClusterMaintenanceWindowArgsDict]]] = ..., memory_per_oracle_compute_unit_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., odb_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scan_listener_port_non_tls: Optional[pulumi.Input[_builtins.int]] = ..., scan_listener_port_tls: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[CloudAutonomousVmClusterTimeoutsArgs, CloudAutonomousVmClusterTimeoutsArgsDict]]] = ..., total_container_databases: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CloudAutonomousVmClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., autonomous_data_storage_percentage: Optional[pulumi.Input[_builtins.float]] = ..., autonomous_data_storage_size_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., available_autonomous_data_storage_size_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., available_container_databases: Optional[pulumi.Input[_builtins.int]] = ..., available_cpus: Optional[pulumi.Input[_builtins.float]] = ..., cloud_exadata_infrastructure_arn: Optional[pulumi.Input[_builtins.str]] = ..., cloud_exadata_infrastructure_id: Optional[pulumi.Input[_builtins.str]] = ..., compute_model: Optional[pulumi.Input[_builtins.str]] = ..., cpu_core_count: Optional[pulumi.Input[_builtins.int]] = ..., cpu_core_count_per_node: Optional[pulumi.Input[_builtins.int]] = ..., cpu_percentage: Optional[pulumi.Input[_builtins.float]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., data_storage_size_in_gbs: Optional[pulumi.Input[_builtins.float]] = ..., data_storage_size_in_tbs: Optional[pulumi.Input[_builtins.float]] = ..., db_servers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., exadata_storage_in_tbs_lowest_scaled_value: Optional[pulumi.Input[_builtins.float]] = ..., hostname: Optional[pulumi.Input[_builtins.str]] = ..., is_mtls_enabled_vm_cluster: Optional[pulumi.Input[_builtins.bool]] = ..., license_model: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[Union[CloudAutonomousVmClusterMaintenanceWindowArgs, CloudAutonomousVmClusterMaintenanceWindowArgsDict]]] = ..., max_acds_lowest_scaled_value: Optional[pulumi.Input[_builtins.int]] = ..., memory_per_oracle_compute_unit_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., memory_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., non_provisionable_autonomous_container_databases: Optional[pulumi.Input[_builtins.int]] = ..., oci_resource_anchor_name: Optional[pulumi.Input[_builtins.str]] = ..., oci_url: Optional[pulumi.Input[_builtins.str]] = ..., ocid: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_arn: Optional[pulumi.Input[_builtins.str]] = ..., odb_network_id: Optional[pulumi.Input[_builtins.str]] = ..., odb_node_storage_size_in_gbs: Optional[pulumi.Input[_builtins.int]] = ..., percent_progress: Optional[pulumi.Input[_builtins.float]] = ..., provisionable_autonomous_container_databases: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_autonomous_container_databases: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_cpus: Optional[pulumi.Input[_builtins.float]] = ..., reclaimable_cpus: Optional[pulumi.Input[_builtins.float]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., reserved_cpus: Optional[pulumi.Input[_builtins.float]] = ..., scan_listener_port_non_tls: Optional[pulumi.Input[_builtins.int]] = ..., scan_listener_port_tls: Optional[pulumi.Input[_builtins.int]] = ..., shape: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_reason: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., time_database_ssl_certificate_expires: Optional[pulumi.Input[_builtins.str]] = ..., time_ords_certificate_expires: Optional[pulumi.Input[_builtins.str]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[CloudAutonomousVmClusterTimeoutsArgs, CloudAutonomousVmClusterTimeoutsArgsDict]]] = ..., total_container_databases: Optional[pulumi.Input[_builtins.int]] = ...) -> CloudAutonomousVmCluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autonomousDataStoragePercentage")
    def autonomous_data_storage_percentage(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autonomousDataStorageSizeInTbs")
    def autonomous_data_storage_size_in_tbs(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableAutonomousDataStorageSizeInTbs")
    def available_autonomous_data_storage_size_in_tbs(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableContainerDatabases")
    def available_container_databases(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableCpus")
    def available_cpus(self) -> pulumi.Output[_builtins.float]:
        
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
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCoreCountPerNode")
    def cpu_core_count_per_node(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuPercentage")
    def cpu_percentage(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInGbs")
    def data_storage_size_in_gbs(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeInTbs")
    def data_storage_size_in_tbs(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbServers")
    def db_servers(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="exadataStorageInTbsLowestScaledValue")
    def exadata_storage_in_tbs_lowest_scaled_value(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMtlsEnabledVmCluster")
    def is_mtls_enabled_vm_cluster(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[outputs.CloudAutonomousVmClusterMaintenanceWindow]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAcdsLowestScaledValue")
    def max_acds_lowest_scaled_value(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryPerOracleComputeUnitInGbs")
    def memory_per_oracle_compute_unit_in_gbs(self) -> pulumi.Output[_builtins.int]:
        
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
    @pulumi.getter(name="nonProvisionableAutonomousContainerDatabases")
    def non_provisionable_autonomous_container_databases(self) -> pulumi.Output[_builtins.int]:
        
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
    @pulumi.getter(name="odbNodeStorageSizeInGbs")
    def odb_node_storage_size_in_gbs(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionableAutonomousContainerDatabases")
    def provisionable_autonomous_container_databases(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedAutonomousContainerDatabases")
    def provisioned_autonomous_container_databases(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedCpus")
    def provisioned_cpus(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reclaimableCpus")
    def reclaimable_cpus(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedCpus")
    def reserved_cpus(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanListenerPortNonTls")
    def scan_listener_port_non_tls(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTls")
    def scan_listener_port_tls(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeDatabaseSslCertificateExpires")
    def time_database_ssl_certificate_expires(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeOrdsCertificateExpires")
    def time_ords_certificate_expires(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.CloudAutonomousVmClusterTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalContainerDatabases")
    def total_container_databases(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


