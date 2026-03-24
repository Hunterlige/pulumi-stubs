

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
__all__ = ['ClusterArgs', 'Cluster']
@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *, shard_count: pulumi.Input[_builtins.int], authorization_mode: Optional[pulumi.Input[_builtins.str]] = ..., automated_backup_config: Optional[pulumi.Input[ClusterAutomatedBackupConfigArgs]] = ..., cross_cluster_replication_config: Optional[pulumi.Input[ClusterCrossClusterReplicationConfigArgs]] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., gcs_source: Optional[pulumi.Input[ClusterGcsSourceArgs]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., maintenance_policy: Optional[pulumi.Input[ClusterMaintenancePolicyArgs]] = ..., maintenance_version: Optional[pulumi.Input[_builtins.str]] = ..., managed_backup_source: Optional[pulumi.Input[ClusterManagedBackupSourceArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., persistence_config: Optional[pulumi.Input[ClusterPersistenceConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., psc_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterPscConfigArgs]]]] = ..., redis_configs: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replica_count: Optional[pulumi.Input[_builtins.int]] = ..., server_ca_mode: Optional[pulumi.Input[_builtins.str]] = ..., server_ca_pool: Optional[pulumi.Input[_builtins.str]] = ..., transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ..., zone_distribution_config: Optional[pulumi.Input[ClusterZoneDistributionConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @shard_count.setter
    def shard_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationMode")
    def authorization_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_mode.setter
    def authorization_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automatedBackupConfig")
    def automated_backup_config(self) -> Optional[pulumi.Input[ClusterAutomatedBackupConfigArgs]]:
        
        ...
    
    @automated_backup_config.setter
    def automated_backup_config(self, value: Optional[pulumi.Input[ClusterAutomatedBackupConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossClusterReplicationConfig")
    def cross_cluster_replication_config(self) -> Optional[pulumi.Input[ClusterCrossClusterReplicationConfigArgs]]:
        
        ...
    
    @cross_cluster_replication_config.setter
    def cross_cluster_replication_config(self, value: Optional[pulumi.Input[ClusterCrossClusterReplicationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsSource")
    def gcs_source(self) -> Optional[pulumi.Input[ClusterGcsSourceArgs]]:
        
        ...
    
    @gcs_source.setter
    def gcs_source(self, value: Optional[pulumi.Input[ClusterGcsSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> Optional[pulumi.Input[ClusterMaintenancePolicyArgs]]:
        
        ...
    
    @maintenance_policy.setter
    def maintenance_policy(self, value: Optional[pulumi.Input[ClusterMaintenancePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maintenance_version.setter
    def maintenance_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBackupSource")
    def managed_backup_source(self) -> Optional[pulumi.Input[ClusterManagedBackupSourceArgs]]:
        
        ...
    
    @managed_backup_source.setter
    def managed_backup_source(self, value: Optional[pulumi.Input[ClusterManagedBackupSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistenceConfig")
    def persistence_config(self) -> Optional[pulumi.Input[ClusterPersistenceConfigArgs]]:
        
        ...
    
    @persistence_config.setter
    def persistence_config(self, value: Optional[pulumi.Input[ClusterPersistenceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterPscConfigArgs]]]]:
        
        ...
    
    @psc_configs.setter
    def psc_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterPscConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redisConfigs")
    def redis_configs(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @redis_configs.setter
    def redis_configs(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaMode")
    def server_ca_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_ca_mode.setter
    def server_ca_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaPool")
    def server_ca_pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_ca_pool.setter
    def server_ca_pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_encryption_mode.setter
    def transit_encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneDistributionConfig")
    def zone_distribution_config(self) -> Optional[pulumi.Input[ClusterZoneDistributionConfigArgs]]:
        
        ...
    
    @zone_distribution_config.setter
    def zone_distribution_config(self, value: Optional[pulumi.Input[ClusterZoneDistributionConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *, authorization_mode: Optional[pulumi.Input[_builtins.str]] = ..., automated_backup_config: Optional[pulumi.Input[ClusterAutomatedBackupConfigArgs]] = ..., available_maintenance_versions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backup_collection: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., cross_cluster_replication_config: Optional[pulumi.Input[ClusterCrossClusterReplicationConfigArgs]] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., discovery_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterDiscoveryEndpointArgs]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_maintenance_version: Optional[pulumi.Input[_builtins.str]] = ..., gcs_source: Optional[pulumi.Input[ClusterGcsSourceArgs]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., maintenance_policy: Optional[pulumi.Input[ClusterMaintenancePolicyArgs]] = ..., maintenance_schedules: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMaintenanceScheduleArgs]]]] = ..., maintenance_version: Optional[pulumi.Input[_builtins.str]] = ..., managed_backup_source: Optional[pulumi.Input[ClusterManagedBackupSourceArgs]] = ..., managed_server_cas: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterManagedServerCaArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., persistence_config: Optional[pulumi.Input[ClusterPersistenceConfigArgs]] = ..., precise_size_gb: Optional[pulumi.Input[_builtins.float]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., psc_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterPscConfigArgs]]]] = ..., psc_connections: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterPscConnectionArgs]]]] = ..., psc_service_attachments: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterPscServiceAttachmentArgs]]]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., redis_configs: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replica_count: Optional[pulumi.Input[_builtins.int]] = ..., server_ca_mode: Optional[pulumi.Input[_builtins.str]] = ..., server_ca_pool: Optional[pulumi.Input[_builtins.str]] = ..., shard_count: Optional[pulumi.Input[_builtins.int]] = ..., size_gb: Optional[pulumi.Input[_builtins.int]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_infos: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStateInfoArgs]]]] = ..., transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., zone_distribution_config: Optional[pulumi.Input[ClusterZoneDistributionConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationMode")
    def authorization_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_mode.setter
    def authorization_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automatedBackupConfig")
    def automated_backup_config(self) -> Optional[pulumi.Input[ClusterAutomatedBackupConfigArgs]]:
        
        ...
    
    @automated_backup_config.setter
    def automated_backup_config(self, value: Optional[pulumi.Input[ClusterAutomatedBackupConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMaintenanceVersions")
    def available_maintenance_versions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @available_maintenance_versions.setter
    def available_maintenance_versions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupCollection")
    def backup_collection(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_collection.setter
    def backup_collection(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossClusterReplicationConfig")
    def cross_cluster_replication_config(self) -> Optional[pulumi.Input[ClusterCrossClusterReplicationConfigArgs]]:
        
        ...
    
    @cross_cluster_replication_config.setter
    def cross_cluster_replication_config(self, value: Optional[pulumi.Input[ClusterCrossClusterReplicationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryEndpoints")
    def discovery_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterDiscoveryEndpointArgs]]]]:
        
        ...
    
    @discovery_endpoints.setter
    def discovery_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterDiscoveryEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveMaintenanceVersion")
    def effective_maintenance_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effective_maintenance_version.setter
    def effective_maintenance_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsSource")
    def gcs_source(self) -> Optional[pulumi.Input[ClusterGcsSourceArgs]]:
        
        ...
    
    @gcs_source.setter
    def gcs_source(self, value: Optional[pulumi.Input[ClusterGcsSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> Optional[pulumi.Input[ClusterMaintenancePolicyArgs]]:
        
        ...
    
    @maintenance_policy.setter
    def maintenance_policy(self, value: Optional[pulumi.Input[ClusterMaintenancePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMaintenanceScheduleArgs]]]]:
        
        ...
    
    @maintenance_schedules.setter
    def maintenance_schedules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterMaintenanceScheduleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maintenance_version.setter
    def maintenance_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBackupSource")
    def managed_backup_source(self) -> Optional[pulumi.Input[ClusterManagedBackupSourceArgs]]:
        
        ...
    
    @managed_backup_source.setter
    def managed_backup_source(self, value: Optional[pulumi.Input[ClusterManagedBackupSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedServerCas")
    def managed_server_cas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterManagedServerCaArgs]]]]:
        
        ...
    
    @managed_server_cas.setter
    def managed_server_cas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterManagedServerCaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistenceConfig")
    def persistence_config(self) -> Optional[pulumi.Input[ClusterPersistenceConfigArgs]]:
        
        ...
    
    @persistence_config.setter
    def persistence_config(self, value: Optional[pulumi.Input[ClusterPersistenceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preciseSizeGb")
    def precise_size_gb(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @precise_size_gb.setter
    def precise_size_gb(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterPscConfigArgs]]]]:
        
        ...
    
    @psc_configs.setter
    def psc_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterPscConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnections")
    def psc_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterPscConnectionArgs]]]]:
        
        ...
    
    @psc_connections.setter
    def psc_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterPscConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscServiceAttachments")
    def psc_service_attachments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterPscServiceAttachmentArgs]]]]:
        
        ...
    
    @psc_service_attachments.setter
    def psc_service_attachments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterPscServiceAttachmentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redisConfigs")
    def redis_configs(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @redis_configs.setter
    def redis_configs(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaMode")
    def server_ca_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_ca_mode.setter
    def server_ca_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaPool")
    def server_ca_pool(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_ca_pool.setter
    def server_ca_pool(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @shard_count.setter
    def shard_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @size_gb.setter
    def size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateInfos")
    def state_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStateInfoArgs]]]]:
        
        ...
    
    @state_infos.setter
    def state_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStateInfoArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transit_encryption_mode.setter
    def transit_encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneDistributionConfig")
    def zone_distribution_config(self) -> Optional[pulumi.Input[ClusterZoneDistributionConfigArgs]]:
        
        ...
    
    @zone_distribution_config.setter
    def zone_distribution_config(self, value: Optional[pulumi.Input[ClusterZoneDistributionConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:redis/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., authorization_mode: Optional[pulumi.Input[_builtins.str]] = ..., automated_backup_config: Optional[pulumi.Input[Union[ClusterAutomatedBackupConfigArgs, ClusterAutomatedBackupConfigArgsDict]]] = ..., cross_cluster_replication_config: Optional[pulumi.Input[Union[ClusterCrossClusterReplicationConfigArgs, ClusterCrossClusterReplicationConfigArgsDict]]] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., gcs_source: Optional[pulumi.Input[Union[ClusterGcsSourceArgs, ClusterGcsSourceArgsDict]]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., maintenance_policy: Optional[pulumi.Input[Union[ClusterMaintenancePolicyArgs, ClusterMaintenancePolicyArgsDict]]] = ..., maintenance_version: Optional[pulumi.Input[_builtins.str]] = ..., managed_backup_source: Optional[pulumi.Input[Union[ClusterManagedBackupSourceArgs, ClusterManagedBackupSourceArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., persistence_config: Optional[pulumi.Input[Union[ClusterPersistenceConfigArgs, ClusterPersistenceConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., psc_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterPscConfigArgs, ClusterPscConfigArgsDict]]]]] = ..., redis_configs: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replica_count: Optional[pulumi.Input[_builtins.int]] = ..., server_ca_mode: Optional[pulumi.Input[_builtins.str]] = ..., server_ca_pool: Optional[pulumi.Input[_builtins.str]] = ..., shard_count: Optional[pulumi.Input[_builtins.int]] = ..., transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ..., zone_distribution_config: Optional[pulumi.Input[Union[ClusterZoneDistributionConfigArgs, ClusterZoneDistributionConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., authorization_mode: Optional[pulumi.Input[_builtins.str]] = ..., automated_backup_config: Optional[pulumi.Input[Union[ClusterAutomatedBackupConfigArgs, ClusterAutomatedBackupConfigArgsDict]]] = ..., available_maintenance_versions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backup_collection: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., cross_cluster_replication_config: Optional[pulumi.Input[Union[ClusterCrossClusterReplicationConfigArgs, ClusterCrossClusterReplicationConfigArgsDict]]] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., discovery_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterDiscoveryEndpointArgs, ClusterDiscoveryEndpointArgsDict]]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_maintenance_version: Optional[pulumi.Input[_builtins.str]] = ..., gcs_source: Optional[pulumi.Input[Union[ClusterGcsSourceArgs, ClusterGcsSourceArgsDict]]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., maintenance_policy: Optional[pulumi.Input[Union[ClusterMaintenancePolicyArgs, ClusterMaintenancePolicyArgsDict]]] = ..., maintenance_schedules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterMaintenanceScheduleArgs, ClusterMaintenanceScheduleArgsDict]]]]] = ..., maintenance_version: Optional[pulumi.Input[_builtins.str]] = ..., managed_backup_source: Optional[pulumi.Input[Union[ClusterManagedBackupSourceArgs, ClusterManagedBackupSourceArgsDict]]] = ..., managed_server_cas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterManagedServerCaArgs, ClusterManagedServerCaArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., persistence_config: Optional[pulumi.Input[Union[ClusterPersistenceConfigArgs, ClusterPersistenceConfigArgsDict]]] = ..., precise_size_gb: Optional[pulumi.Input[_builtins.float]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., psc_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterPscConfigArgs, ClusterPscConfigArgsDict]]]]] = ..., psc_connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterPscConnectionArgs, ClusterPscConnectionArgsDict]]]]] = ..., psc_service_attachments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterPscServiceAttachmentArgs, ClusterPscServiceAttachmentArgsDict]]]]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., redis_configs: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replica_count: Optional[pulumi.Input[_builtins.int]] = ..., server_ca_mode: Optional[pulumi.Input[_builtins.str]] = ..., server_ca_pool: Optional[pulumi.Input[_builtins.str]] = ..., shard_count: Optional[pulumi.Input[_builtins.int]] = ..., size_gb: Optional[pulumi.Input[_builtins.int]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., state_infos: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterStateInfoArgs, ClusterStateInfoArgsDict]]]]] = ..., transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., zone_distribution_config: Optional[pulumi.Input[Union[ClusterZoneDistributionConfigArgs, ClusterZoneDistributionConfigArgsDict]]] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationMode")
    def authorization_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automatedBackupConfig")
    def automated_backup_config(self) -> pulumi.Output[Optional[outputs.ClusterAutomatedBackupConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMaintenanceVersions")
    def available_maintenance_versions(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupCollection")
    def backup_collection(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossClusterReplicationConfig")
    def cross_cluster_replication_config(self) -> pulumi.Output[outputs.ClusterCrossClusterReplicationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryEndpoints")
    def discovery_endpoints(self) -> pulumi.Output[Sequence[outputs.ClusterDiscoveryEndpoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveMaintenanceVersion")
    def effective_maintenance_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsSource")
    def gcs_source(self) -> pulumi.Output[Optional[outputs.ClusterGcsSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(self) -> pulumi.Output[Optional[outputs.ClusterMaintenancePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(self) -> pulumi.Output[Sequence[outputs.ClusterMaintenanceSchedule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBackupSource")
    def managed_backup_source(self) -> pulumi.Output[Optional[outputs.ClusterManagedBackupSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedServerCas")
    def managed_server_cas(self) -> pulumi.Output[Sequence[outputs.ClusterManagedServerCa]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistenceConfig")
    def persistence_config(self) -> pulumi.Output[outputs.ClusterPersistenceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preciseSizeGb")
    def precise_size_gb(self) -> pulumi.Output[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(self) -> pulumi.Output[Optional[Sequence[outputs.ClusterPscConfig]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnections")
    def psc_connections(self) -> pulumi.Output[Sequence[outputs.ClusterPscConnection]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscServiceAttachments")
    def psc_service_attachments(self) -> pulumi.Output[Sequence[outputs.ClusterPscServiceAttachment]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redisConfigs")
    def redis_configs(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaMode")
    def server_ca_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaPool")
    def server_ca_pool(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateInfos")
    def state_infos(self) -> pulumi.Output[Sequence[outputs.ClusterStateInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneDistributionConfig")
    def zone_distribution_config(self) -> pulumi.Output[outputs.ClusterZoneDistributionConfig]:
        
        ...
    


