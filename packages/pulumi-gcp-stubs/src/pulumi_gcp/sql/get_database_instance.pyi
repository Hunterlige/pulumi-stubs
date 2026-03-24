

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDatabaseInstanceResult', 'AwaitableGetDatabaseInstanceResult', 'get_database_instance', 'get_database_instance_output']
@pulumi.output_type
class GetDatabaseInstanceResult:
    
    def __init__(__self__, available_maintenance_versions=..., backupdr_backup=..., clones=..., connection_name=..., database_version=..., deletion_protection=..., dns_name=..., dns_names=..., encryption_key_name=..., final_backup_description=..., first_ip_address=..., id=..., instance_type=..., ip_addresses=..., maintenance_version=..., master_instance_name=..., name=..., node_count=..., point_in_time_restore_contexts=..., private_ip_address=..., project=..., psc_service_attachment_link=..., public_ip_address=..., region=..., replica_configurations=..., replica_names=..., replication_clusters=..., restore_backup_contexts=..., root_password=..., root_password_wo=..., root_password_wo_version=..., self_link=..., server_ca_certs=..., service_account_email_address=..., settings=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMaintenanceVersions")
    def available_maintenance_versions(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupdrBackup")
    def backupdr_backup(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def clones(self) -> Sequence[outputs.GetDatabaseInstanceCloneResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsNames")
    def dns_names(self) -> Sequence[outputs.GetDatabaseInstanceDnsNameResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeyName")
    def encryption_key_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalBackupDescription")
    def final_backup_description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstIpAddress")
    def first_ip_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[outputs.GetDatabaseInstanceIpAddressResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterInstanceName")
    def master_instance_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRestoreContexts")
    def point_in_time_restore_contexts(self) -> Sequence[outputs.GetDatabaseInstancePointInTimeRestoreContextResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscServiceAttachmentLink")
    def psc_service_attachment_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaConfigurations")
    def replica_configurations(self) -> Sequence[outputs.GetDatabaseInstanceReplicaConfigurationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaNames")
    def replica_names(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationClusters")
    def replication_clusters(self) -> Sequence[outputs.GetDatabaseInstanceReplicationClusterResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreBackupContexts")
    def restore_backup_contexts(self) -> Sequence[outputs.GetDatabaseInstanceRestoreBackupContextResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPassword")
    def root_password(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPasswordWo")
    def root_password_wo(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPasswordWoVersion")
    def root_password_wo_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaCerts")
    def server_ca_certs(self) -> Sequence[outputs.GetDatabaseInstanceServerCaCertResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Sequence[outputs.GetDatabaseInstanceSettingResult]:
        ...
    


class AwaitableGetDatabaseInstanceResult(GetDatabaseInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetDatabaseInstanceResult]:
        ...
    


def get_database_instance(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDatabaseInstanceResult:
    
    ...

def get_database_instance_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDatabaseInstanceResult]:
    
    ...

