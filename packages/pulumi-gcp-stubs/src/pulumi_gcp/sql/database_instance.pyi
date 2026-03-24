

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DatabaseInstanceArgs', 'DatabaseInstance']
@pulumi.input_type
class DatabaseInstanceArgs:
    def __init__(__self__, *, database_version: pulumi.Input[_builtins.str], backupdr_backup: Optional[pulumi.Input[_builtins.str]] = ..., clone: Optional[pulumi.Input[DatabaseInstanceCloneArgs]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., final_backup_description: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_version: Optional[pulumi.Input[_builtins.str]] = ..., master_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., point_in_time_restore_context: Optional[pulumi.Input[DatabaseInstancePointInTimeRestoreContextArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replica_configuration: Optional[pulumi.Input[DatabaseInstanceReplicaConfigurationArgs]] = ..., replica_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., replication_cluster: Optional[pulumi.Input[DatabaseInstanceReplicationClusterArgs]] = ..., restore_backup_context: Optional[pulumi.Input[DatabaseInstanceRestoreBackupContextArgs]] = ..., root_password: Optional[pulumi.Input[_builtins.str]] = ..., root_password_wo: Optional[pulumi.Input[_builtins.str]] = ..., root_password_wo_version: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[DatabaseInstanceSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_version.setter
    def database_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupdrBackup")
    def backupdr_backup(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backupdr_backup.setter
    def backupdr_backup(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def clone(self) -> Optional[pulumi.Input[DatabaseInstanceCloneArgs]]:
        
        ...
    
    @clone.setter
    def clone(self, value: Optional[pulumi.Input[DatabaseInstanceCloneArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeyName")
    def encryption_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_key_name.setter
    def encryption_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalBackupDescription")
    def final_backup_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @final_backup_description.setter
    def final_backup_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maintenance_version.setter
    def maintenance_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterInstanceName")
    def master_instance_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_instance_name.setter
    def master_instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRestoreContext")
    def point_in_time_restore_context(self) -> Optional[pulumi.Input[DatabaseInstancePointInTimeRestoreContextArgs]]:
        
        ...
    
    @point_in_time_restore_context.setter
    def point_in_time_restore_context(self, value: Optional[pulumi.Input[DatabaseInstancePointInTimeRestoreContextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaConfiguration")
    def replica_configuration(self) -> Optional[pulumi.Input[DatabaseInstanceReplicaConfigurationArgs]]:
        
        ...
    
    @replica_configuration.setter
    def replica_configuration(self, value: Optional[pulumi.Input[DatabaseInstanceReplicaConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaNames")
    def replica_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @replica_names.setter
    def replica_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationCluster")
    def replication_cluster(self) -> Optional[pulumi.Input[DatabaseInstanceReplicationClusterArgs]]:
        
        ...
    
    @replication_cluster.setter
    def replication_cluster(self, value: Optional[pulumi.Input[DatabaseInstanceReplicationClusterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreBackupContext")
    def restore_backup_context(self) -> Optional[pulumi.Input[DatabaseInstanceRestoreBackupContextArgs]]:
        
        ...
    
    @restore_backup_context.setter
    def restore_backup_context(self, value: Optional[pulumi.Input[DatabaseInstanceRestoreBackupContextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPassword")
    def root_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @root_password.setter
    def root_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPasswordWo")
    def root_password_wo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @root_password_wo.setter
    def root_password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPasswordWoVersion")
    def root_password_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @root_password_wo_version.setter
    def root_password_wo_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsArgs]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DatabaseInstanceState:
    def __init__(__self__, *, available_maintenance_versions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backupdr_backup: Optional[pulumi.Input[_builtins.str]] = ..., clone: Optional[pulumi.Input[DatabaseInstanceCloneArgs]] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ..., database_version: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., dns_name: Optional[pulumi.Input[_builtins.str]] = ..., dns_names: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceDnsNameArgs]]]] = ..., encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., final_backup_description: Optional[pulumi.Input[_builtins.str]] = ..., first_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceIpAddressArgs]]]] = ..., maintenance_version: Optional[pulumi.Input[_builtins.str]] = ..., master_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., point_in_time_restore_context: Optional[pulumi.Input[DatabaseInstancePointInTimeRestoreContextArgs]] = ..., private_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., psc_service_attachment_link: Optional[pulumi.Input[_builtins.str]] = ..., public_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replica_configuration: Optional[pulumi.Input[DatabaseInstanceReplicaConfigurationArgs]] = ..., replica_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., replication_cluster: Optional[pulumi.Input[DatabaseInstanceReplicationClusterArgs]] = ..., restore_backup_context: Optional[pulumi.Input[DatabaseInstanceRestoreBackupContextArgs]] = ..., root_password: Optional[pulumi.Input[_builtins.str]] = ..., root_password_wo: Optional[pulumi.Input[_builtins.str]] = ..., root_password_wo_version: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., server_ca_certs: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceServerCaCertArgs]]]] = ..., service_account_email_address: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[DatabaseInstanceSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMaintenanceVersions")
    def available_maintenance_versions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @available_maintenance_versions.setter
    def available_maintenance_versions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupdrBackup")
    def backupdr_backup(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backupdr_backup.setter
    def backupdr_backup(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def clone(self) -> Optional[pulumi.Input[DatabaseInstanceCloneArgs]]:
        
        ...
    
    @clone.setter
    def clone(self, value: Optional[pulumi.Input[DatabaseInstanceCloneArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_version.setter
    def database_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsNames")
    def dns_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceDnsNameArgs]]]]:
        
        ...
    
    @dns_names.setter
    def dns_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceDnsNameArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeyName")
    def encryption_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_key_name.setter
    def encryption_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalBackupDescription")
    def final_backup_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @final_backup_description.setter
    def final_backup_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstIpAddress")
    def first_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_ip_address.setter
    def first_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceIpAddressArgs]]]]:
        ...
    
    @ip_addresses.setter
    def ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceIpAddressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maintenance_version.setter
    def maintenance_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterInstanceName")
    def master_instance_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @master_instance_name.setter
    def master_instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRestoreContext")
    def point_in_time_restore_context(self) -> Optional[pulumi.Input[DatabaseInstancePointInTimeRestoreContextArgs]]:
        
        ...
    
    @point_in_time_restore_context.setter
    def point_in_time_restore_context(self, value: Optional[pulumi.Input[DatabaseInstancePointInTimeRestoreContextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscServiceAttachmentLink")
    def psc_service_attachment_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @psc_service_attachment_link.setter
    def psc_service_attachment_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ip_address.setter
    def public_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaConfiguration")
    def replica_configuration(self) -> Optional[pulumi.Input[DatabaseInstanceReplicaConfigurationArgs]]:
        
        ...
    
    @replica_configuration.setter
    def replica_configuration(self, value: Optional[pulumi.Input[DatabaseInstanceReplicaConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaNames")
    def replica_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @replica_names.setter
    def replica_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationCluster")
    def replication_cluster(self) -> Optional[pulumi.Input[DatabaseInstanceReplicationClusterArgs]]:
        
        ...
    
    @replication_cluster.setter
    def replication_cluster(self, value: Optional[pulumi.Input[DatabaseInstanceReplicationClusterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreBackupContext")
    def restore_backup_context(self) -> Optional[pulumi.Input[DatabaseInstanceRestoreBackupContextArgs]]:
        
        ...
    
    @restore_backup_context.setter
    def restore_backup_context(self, value: Optional[pulumi.Input[DatabaseInstanceRestoreBackupContextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPassword")
    def root_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @root_password.setter
    def root_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPasswordWo")
    def root_password_wo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @root_password_wo.setter
    def root_password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPasswordWoVersion")
    def root_password_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @root_password_wo_version.setter
    def root_password_wo_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaCerts")
    def server_ca_certs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceServerCaCertArgs]]]]:
        ...
    
    @server_ca_certs.setter
    def server_ca_certs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceServerCaCertArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_email_address.setter
    def service_account_email_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsArgs]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:sql/databaseInstance:DatabaseInstance")
class DatabaseInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backupdr_backup: Optional[pulumi.Input[_builtins.str]] = ..., clone: Optional[pulumi.Input[Union[DatabaseInstanceCloneArgs, DatabaseInstanceCloneArgsDict]]] = ..., database_version: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., final_backup_description: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_version: Optional[pulumi.Input[_builtins.str]] = ..., master_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., point_in_time_restore_context: Optional[pulumi.Input[Union[DatabaseInstancePointInTimeRestoreContextArgs, DatabaseInstancePointInTimeRestoreContextArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replica_configuration: Optional[pulumi.Input[Union[DatabaseInstanceReplicaConfigurationArgs, DatabaseInstanceReplicaConfigurationArgsDict]]] = ..., replica_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., replication_cluster: Optional[pulumi.Input[Union[DatabaseInstanceReplicationClusterArgs, DatabaseInstanceReplicationClusterArgsDict]]] = ..., restore_backup_context: Optional[pulumi.Input[Union[DatabaseInstanceRestoreBackupContextArgs, DatabaseInstanceRestoreBackupContextArgsDict]]] = ..., root_password: Optional[pulumi.Input[_builtins.str]] = ..., root_password_wo: Optional[pulumi.Input[_builtins.str]] = ..., root_password_wo_version: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[Union[DatabaseInstanceSettingsArgs, DatabaseInstanceSettingsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DatabaseInstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., available_maintenance_versions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., backupdr_backup: Optional[pulumi.Input[_builtins.str]] = ..., clone: Optional[pulumi.Input[Union[DatabaseInstanceCloneArgs, DatabaseInstanceCloneArgsDict]]] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ..., database_version: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., dns_name: Optional[pulumi.Input[_builtins.str]] = ..., dns_names: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DatabaseInstanceDnsNameArgs, DatabaseInstanceDnsNameArgsDict]]]]] = ..., encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., final_backup_description: Optional[pulumi.Input[_builtins.str]] = ..., first_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DatabaseInstanceIpAddressArgs, DatabaseInstanceIpAddressArgsDict]]]]] = ..., maintenance_version: Optional[pulumi.Input[_builtins.str]] = ..., master_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., point_in_time_restore_context: Optional[pulumi.Input[Union[DatabaseInstancePointInTimeRestoreContextArgs, DatabaseInstancePointInTimeRestoreContextArgsDict]]] = ..., private_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., psc_service_attachment_link: Optional[pulumi.Input[_builtins.str]] = ..., public_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replica_configuration: Optional[pulumi.Input[Union[DatabaseInstanceReplicaConfigurationArgs, DatabaseInstanceReplicaConfigurationArgsDict]]] = ..., replica_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., replication_cluster: Optional[pulumi.Input[Union[DatabaseInstanceReplicationClusterArgs, DatabaseInstanceReplicationClusterArgsDict]]] = ..., restore_backup_context: Optional[pulumi.Input[Union[DatabaseInstanceRestoreBackupContextArgs, DatabaseInstanceRestoreBackupContextArgsDict]]] = ..., root_password: Optional[pulumi.Input[_builtins.str]] = ..., root_password_wo: Optional[pulumi.Input[_builtins.str]] = ..., root_password_wo_version: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., server_ca_certs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DatabaseInstanceServerCaCertArgs, DatabaseInstanceServerCaCertArgsDict]]]]] = ..., service_account_email_address: Optional[pulumi.Input[_builtins.str]] = ..., settings: Optional[pulumi.Input[Union[DatabaseInstanceSettingsArgs, DatabaseInstanceSettingsArgsDict]]] = ...) -> DatabaseInstance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableMaintenanceVersions")
    def available_maintenance_versions(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupdrBackup")
    def backupdr_backup(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clone(self) -> pulumi.Output[Optional[outputs.DatabaseInstanceClone]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsNames")
    def dns_names(self) -> pulumi.Output[Sequence[outputs.DatabaseInstanceDnsName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeyName")
    def encryption_key_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalBackupDescription")
    def final_backup_description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstIpAddress")
    def first_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> pulumi.Output[Sequence[outputs.DatabaseInstanceIpAddress]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterInstanceName")
    def master_instance_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRestoreContext")
    def point_in_time_restore_context(self) -> pulumi.Output[Optional[outputs.DatabaseInstancePointInTimeRestoreContext]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscServiceAttachmentLink")
    def psc_service_attachment_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaConfiguration")
    def replica_configuration(self) -> pulumi.Output[outputs.DatabaseInstanceReplicaConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaNames")
    def replica_names(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationCluster")
    def replication_cluster(self) -> pulumi.Output[outputs.DatabaseInstanceReplicationCluster]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreBackupContext")
    def restore_backup_context(self) -> pulumi.Output[Optional[outputs.DatabaseInstanceRestoreBackupContext]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPassword")
    def root_password(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPasswordWo")
    def root_password_wo(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootPasswordWoVersion")
    def root_password_wo_version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaCerts")
    def server_ca_certs(self) -> pulumi.Output[Sequence[outputs.DatabaseInstanceServerCaCert]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Output[outputs.DatabaseInstanceSettings]:
        
        ...
    


