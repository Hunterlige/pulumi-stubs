

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetClusterResult', 'AwaitableGetClusterResult', 'get_cluster', 'get_cluster_output']
@pulumi.output_type
class GetClusterResult:
    
    def __init__(__self__, authorization_mode=..., automated_backup_configs=..., available_maintenance_versions=..., backup_collection=..., create_time=..., cross_cluster_replication_configs=..., deletion_protection_enabled=..., discovery_endpoints=..., effective_labels=..., effective_maintenance_version=..., gcs_sources=..., id=..., kms_key=..., labels=..., maintenance_policies=..., maintenance_schedules=..., maintenance_version=..., managed_backup_sources=..., managed_server_cas=..., name=..., node_type=..., persistence_configs=..., precise_size_gb=..., project=..., psc_configs=..., psc_connections=..., psc_service_attachments=..., pulumi_labels=..., redis_configs=..., region=..., replica_count=..., server_ca_mode=..., server_ca_pool=..., shard_count=..., size_gb=..., state=..., state_infos=..., transit_encryption_mode=..., uid=..., zone_distribution_configs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationMode")
    def authorization_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automatedBackupConfigs")
    def automated_backup_configs(self) -> Sequence[outputs.GetClusterAutomatedBackupConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMaintenanceVersions")
    def available_maintenance_versions(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupCollection")
    def backup_collection(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossClusterReplicationConfigs")
    def cross_cluster_replication_configs(self) -> Sequence[outputs.GetClusterCrossClusterReplicationConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryEndpoints")
    def discovery_endpoints(self) -> Sequence[outputs.GetClusterDiscoveryEndpointResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveMaintenanceVersion")
    def effective_maintenance_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsSources")
    def gcs_sources(self) -> Sequence[outputs.GetClusterGcsSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicies")
    def maintenance_policies(self) -> Sequence[outputs.GetClusterMaintenancePolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(self) -> Sequence[outputs.GetClusterMaintenanceScheduleResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBackupSources")
    def managed_backup_sources(self) -> Sequence[outputs.GetClusterManagedBackupSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedServerCas")
    def managed_server_cas(self) -> Sequence[outputs.GetClusterManagedServerCaResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistenceConfigs")
    def persistence_configs(self) -> Sequence[outputs.GetClusterPersistenceConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preciseSizeGb")
    def precise_size_gb(self) -> _builtins.float:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(self) -> Sequence[outputs.GetClusterPscConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConnections")
    def psc_connections(self) -> Sequence[outputs.GetClusterPscConnectionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscServiceAttachments")
    def psc_service_attachments(self) -> Sequence[outputs.GetClusterPscServiceAttachmentResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redisConfigs")
    def redis_configs(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaMode")
    def server_ca_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaPool")
    def server_ca_pool(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateInfos")
    def state_infos(self) -> Sequence[outputs.GetClusterStateInfoResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneDistributionConfigs")
    def zone_distribution_configs(self) -> Sequence[outputs.GetClusterZoneDistributionConfigResult]:
        ...
    


class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetClusterResult]:
        ...
    


def get_cluster(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetClusterResult:
    
    ...

def get_cluster_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetClusterResult]:
    
    ...

