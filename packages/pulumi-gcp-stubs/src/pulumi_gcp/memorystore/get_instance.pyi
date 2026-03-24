

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInstanceResult', 'AwaitableGetInstanceResult', 'get_instance', 'get_instance_output']
@pulumi.output_type
class GetInstanceResult:
    
    def __init__(__self__, authorization_mode=..., automated_backup_configs=..., available_maintenance_versions=..., backup_collection=..., create_time=..., cross_instance_replication_configs=..., deletion_protection_enabled=..., desired_auto_created_endpoints=..., desired_psc_auto_connections=..., discovery_endpoints=..., effective_labels=..., effective_maintenance_version=..., endpoints=..., engine_configs=..., engine_version=..., gcs_sources=..., id=..., instance_id=..., kms_key=..., labels=..., location=..., maintenance_policies=..., maintenance_schedules=..., maintenance_version=..., managed_backup_sources=..., managed_server_cas=..., mode=..., name=..., node_configs=..., node_type=..., persistence_configs=..., project=..., psc_attachment_details=..., psc_auto_connections=..., pulumi_labels=..., replica_count=..., server_ca_mode=..., server_ca_pool=..., shard_count=..., state=..., state_infos=..., transit_encryption_mode=..., uid=..., update_time=..., zone_distribution_configs=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationMode")
    def authorization_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="automatedBackupConfigs")
    def automated_backup_configs(self) -> Sequence[outputs.GetInstanceAutomatedBackupConfigResult]:
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
    @pulumi.getter(name="crossInstanceReplicationConfigs")
    def cross_instance_replication_configs(self) -> Sequence[outputs.GetInstanceCrossInstanceReplicationConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredAutoCreatedEndpoints")
    def desired_auto_created_endpoints(self) -> Sequence[outputs.GetInstanceDesiredAutoCreatedEndpointResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredPscAutoConnections")
    def desired_psc_auto_connections(self) -> Sequence[outputs.GetInstanceDesiredPscAutoConnectionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryEndpoints")
    def discovery_endpoints(self) -> Sequence[outputs.GetInstanceDiscoveryEndpointResult]:
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
    @pulumi.getter
    def endpoints(self) -> Sequence[outputs.GetInstanceEndpointResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineConfigs")
    def engine_configs(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsSources")
    def gcs_sources(self) -> Sequence[outputs.GetInstanceGcsSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
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
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenancePolicies")
    def maintenance_policies(self) -> Sequence[outputs.GetInstanceMaintenancePolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(self) -> Sequence[outputs.GetInstanceMaintenanceScheduleResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBackupSources")
    def managed_backup_sources(self) -> Sequence[outputs.GetInstanceManagedBackupSourceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedServerCas")
    def managed_server_cas(self) -> Sequence[outputs.GetInstanceManagedServerCaResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> Sequence[outputs.GetInstanceNodeConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistenceConfigs")
    def persistence_configs(self) -> Sequence[outputs.GetInstancePersistenceConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscAttachmentDetails")
    def psc_attachment_details(self) -> Sequence[outputs.GetInstancePscAttachmentDetailResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscAutoConnections")
    def psc_auto_connections(self) -> Sequence[outputs.GetInstancePscAutoConnectionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
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
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateInfos")
    def state_infos(self) -> Sequence[outputs.GetInstanceStateInfoResult]:
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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneDistributionConfigs")
    def zone_distribution_configs(self) -> Sequence[outputs.GetInstanceZoneDistributionConfigResult]:
        ...
    


class AwaitableGetInstanceResult(GetInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetInstanceResult]:
        ...
    


def get_instance(instance_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInstanceResult:
    
    ...

def get_instance_output(instance_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInstanceResult]:
    
    ...

