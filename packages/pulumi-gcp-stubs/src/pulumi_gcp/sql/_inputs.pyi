

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DatabaseInstanceCloneArgs', 'DatabaseInstanceCloneArgsDict', 'DatabaseInstanceDnsNameArgs', 'DatabaseInstanceDnsNameArgsDict', 'DatabaseInstanceIpAddressArgs', 'DatabaseInstanceIpAddressArgsDict', 'DatabaseInstancePointInTimeRestoreContextArgs', 'DatabaseInstancePointInTimeRestoreContextArgsDict', 'DatabaseInstanceReplicaConfigurationArgs', 'DatabaseInstanceReplicaConfigurationArgsDict', 'DatabaseInstanceReplicationClusterArgs', 'DatabaseInstanceReplicationClusterArgsDict', 'DatabaseInstanceRestoreBackupContextArgs', 'DatabaseInstanceRestoreBackupContextArgsDict', 'DatabaseInstanceServerCaCertArgs', 'DatabaseInstanceServerCaCertArgsDict', 'DatabaseInstanceSettingsArgs', 'DatabaseInstanceSettingsArgsDict', 'DatabaseInstanceSettingsActiveDirectoryConfigArgs', ..., ..., ..., 'DatabaseInstanceSettingsBackupConfigurationArgs', ..., ..., ..., 'DatabaseInstanceSettingsConnectionPoolConfigArgs', ..., ..., ..., 'DatabaseInstanceSettingsDataCacheConfigArgs', 'DatabaseInstanceSettingsDataCacheConfigArgsDict', 'DatabaseInstanceSettingsDatabaseFlagArgs', 'DatabaseInstanceSettingsDatabaseFlagArgsDict', 'DatabaseInstanceSettingsDenyMaintenancePeriodArgs', ..., 'DatabaseInstanceSettingsFinalBackupConfigArgs', 'DatabaseInstanceSettingsFinalBackupConfigArgsDict', 'DatabaseInstanceSettingsInsightsConfigArgs', 'DatabaseInstanceSettingsInsightsConfigArgsDict', 'DatabaseInstanceSettingsIpConfigurationArgs', 'DatabaseInstanceSettingsIpConfigurationArgsDict', ..., ..., ..., ..., ..., ..., 'DatabaseInstanceSettingsLocationPreferenceArgs', 'DatabaseInstanceSettingsLocationPreferenceArgsDict', 'DatabaseInstanceSettingsMaintenanceWindowArgs', 'DatabaseInstanceSettingsMaintenanceWindowArgsDict', ..., ..., ..., ..., ..., ..., 'DatabaseInstanceSettingsSqlServerAuditConfigArgs', ..., 'UserPasswordPolicyArgs', 'UserPasswordPolicyArgsDict', 'UserPasswordPolicyStatusArgs', 'UserPasswordPolicyStatusArgsDict', 'UserSqlServerUserDetailArgs', 'UserSqlServerUserDetailArgsDict']
class DatabaseInstanceCloneArgsDict(TypedDict):
    source_instance_name: pulumi.Input[_builtins.str]
    allocated_ip_range: NotRequired[pulumi.Input[_builtins.str]]
    database_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    point_in_time: NotRequired[pulumi.Input[_builtins.str]]
    preferred_zone: NotRequired[pulumi.Input[_builtins.str]]
    source_instance_deletion_time: NotRequired[pulumi.Input[_builtins.str]]
    source_project: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceCloneArgs:
    def __init__(__self__, *, source_instance_name: pulumi.Input[_builtins.str], allocated_ip_range: Optional[pulumi.Input[_builtins.str]] = ..., database_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., point_in_time: Optional[pulumi.Input[_builtins.str]] = ..., preferred_zone: Optional[pulumi.Input[_builtins.str]] = ..., source_instance_deletion_time: Optional[pulumi.Input[_builtins.str]] = ..., source_project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceInstanceName")
    def source_instance_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_instance_name.setter
    def source_instance_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocated_ip_range.setter
    def allocated_ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseNames")
    def database_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @database_names.setter
    def database_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @point_in_time.setter
    def point_in_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredZone")
    def preferred_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preferred_zone.setter
    def preferred_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceInstanceDeletionTime")
    def source_instance_deletion_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_instance_deletion_time.setter
    def source_instance_deletion_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceProject")
    def source_project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_project.setter
    def source_project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstanceDnsNameArgsDict(TypedDict):
    connection_type: NotRequired[pulumi.Input[_builtins.str]]
    dns_scope: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceDnsNameArgs:
    def __init__(__self__, *, connection_type: Optional[pulumi.Input[_builtins.str]] = ..., dns_scope: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsScope")
    def dns_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_scope.setter
    def dns_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstanceIpAddressArgsDict(TypedDict):
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    time_to_retire: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceIpAddressArgs:
    def __init__(__self__, *, ip_address: Optional[pulumi.Input[_builtins.str]] = ..., time_to_retire: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToRetire")
    def time_to_retire(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_to_retire.setter
    def time_to_retire(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstancePointInTimeRestoreContextArgsDict(TypedDict):
    datasource: pulumi.Input[_builtins.str]
    allocated_ip_range: NotRequired[pulumi.Input[_builtins.str]]
    point_in_time: NotRequired[pulumi.Input[_builtins.str]]
    preferred_zone: NotRequired[pulumi.Input[_builtins.str]]
    target_instance: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstancePointInTimeRestoreContextArgs:
    def __init__(__self__, *, datasource: pulumi.Input[_builtins.str], allocated_ip_range: Optional[pulumi.Input[_builtins.str]] = ..., point_in_time: Optional[pulumi.Input[_builtins.str]] = ..., preferred_zone: Optional[pulumi.Input[_builtins.str]] = ..., target_instance: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datasource(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @datasource.setter
    def datasource(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocated_ip_range.setter
    def allocated_ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @point_in_time.setter
    def point_in_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredZone")
    def preferred_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preferred_zone.setter
    def preferred_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetInstance")
    def target_instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_instance.setter
    def target_instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstanceReplicaConfigurationArgsDict(TypedDict):
    ca_certificate: NotRequired[pulumi.Input[_builtins.str]]
    cascadable_replica: NotRequired[pulumi.Input[_builtins.bool]]
    client_certificate: NotRequired[pulumi.Input[_builtins.str]]
    client_key: NotRequired[pulumi.Input[_builtins.str]]
    connect_retry_interval: NotRequired[pulumi.Input[_builtins.int]]
    dump_file_path: NotRequired[pulumi.Input[_builtins.str]]
    failover_target: NotRequired[pulumi.Input[_builtins.bool]]
    master_heartbeat_period: NotRequired[pulumi.Input[_builtins.int]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    ssl_cipher: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]
    verify_server_certificate: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DatabaseInstanceReplicaConfigurationArgs:
    def __init__(__self__, *, ca_certificate: Optional[pulumi.Input[_builtins.str]] = ..., cascadable_replica: Optional[pulumi.Input[_builtins.bool]] = ..., client_certificate: Optional[pulumi.Input[_builtins.str]] = ..., client_key: Optional[pulumi.Input[_builtins.str]] = ..., connect_retry_interval: Optional[pulumi.Input[_builtins.int]] = ..., dump_file_path: Optional[pulumi.Input[_builtins.str]] = ..., failover_target: Optional[pulumi.Input[_builtins.bool]] = ..., master_heartbeat_period: Optional[pulumi.Input[_builtins.int]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., ssl_cipher: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ..., verify_server_certificate: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ca_certificate.setter
    def ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cascadableReplica")
    def cascadable_replica(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cascadable_replica.setter
    def cascadable_replica(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_certificate.setter
    def client_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_key.setter
    def client_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectRetryInterval")
    def connect_retry_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @connect_retry_interval.setter
    def connect_retry_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpFilePath")
    def dump_file_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dump_file_path.setter
    def dump_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverTarget")
    def failover_target(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @failover_target.setter
    def failover_target(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterHeartbeatPeriod")
    def master_heartbeat_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @master_heartbeat_period.setter
    def master_heartbeat_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCipher")
    def ssl_cipher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssl_cipher.setter
    def ssl_cipher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifyServerCertificate")
    def verify_server_certificate(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @verify_server_certificate.setter
    def verify_server_certificate(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DatabaseInstanceReplicationClusterArgsDict(TypedDict):
    dr_replica: NotRequired[pulumi.Input[_builtins.bool]]
    failover_dr_replica_name: NotRequired[pulumi.Input[_builtins.str]]
    psa_write_endpoint: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceReplicationClusterArgs:
    def __init__(__self__, *, dr_replica: Optional[pulumi.Input[_builtins.bool]] = ..., failover_dr_replica_name: Optional[pulumi.Input[_builtins.str]] = ..., psa_write_endpoint: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="drReplica")
    def dr_replica(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @dr_replica.setter
    def dr_replica(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverDrReplicaName")
    def failover_dr_replica_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @failover_dr_replica_name.setter
    def failover_dr_replica_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="psaWriteEndpoint")
    def psa_write_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @psa_write_endpoint.setter
    def psa_write_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstanceRestoreBackupContextArgsDict(TypedDict):
    backup_run_id: pulumi.Input[_builtins.int]
    instance_id: NotRequired[pulumi.Input[_builtins.str]]
    project: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceRestoreBackupContextArgs:
    def __init__(__self__, *, backup_run_id: pulumi.Input[_builtins.int], instance_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRunId")
    def backup_run_id(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @backup_run_id.setter
    def backup_run_id(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstanceServerCaCertArgsDict(TypedDict):
    cert: NotRequired[pulumi.Input[_builtins.str]]
    common_name: NotRequired[pulumi.Input[_builtins.str]]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    expiration_time: NotRequired[pulumi.Input[_builtins.str]]
    sha1_fingerprint: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceServerCaCertArgs:
    def __init__(__self__, *, cert: Optional[pulumi.Input[_builtins.str]] = ..., common_name: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., expiration_time: Optional[pulumi.Input[_builtins.str]] = ..., sha1_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cert.setter
    def cert(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @common_name.setter
    def common_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiration_time.setter
    def expiration_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sha1_fingerprint.setter
    def sha1_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstanceSettingsArgsDict(TypedDict):
    tier: pulumi.Input[_builtins.str]
    activation_policy: NotRequired[pulumi.Input[_builtins.str]]
    active_directory_config: NotRequired[pulumi.Input[DatabaseInstanceSettingsActiveDirectoryConfigArgsDict]]
    advanced_machine_features: NotRequired[pulumi.Input[DatabaseInstanceSettingsAdvancedMachineFeaturesArgsDict]]
    auto_upgrade_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    availability_type: NotRequired[pulumi.Input[_builtins.str]]
    backup_configuration: NotRequired[pulumi.Input[DatabaseInstanceSettingsBackupConfigurationArgsDict]]
    collation: NotRequired[pulumi.Input[_builtins.str]]
    connection_pool_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsConnectionPoolConfigArgsDict]]]]
    connector_enforcement: NotRequired[pulumi.Input[_builtins.str]]
    data_api_access: NotRequired[pulumi.Input[_builtins.str]]
    data_cache_config: NotRequired[pulumi.Input[DatabaseInstanceSettingsDataCacheConfigArgsDict]]
    data_disk_provisioned_iops: NotRequired[pulumi.Input[_builtins.int]]
    data_disk_provisioned_throughput: NotRequired[pulumi.Input[_builtins.int]]
    database_flags: NotRequired[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsDatabaseFlagArgsDict]]]]
    deletion_protection_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    deny_maintenance_period: NotRequired[pulumi.Input[DatabaseInstanceSettingsDenyMaintenancePeriodArgsDict]]
    disk_autoresize: NotRequired[pulumi.Input[_builtins.bool]]
    disk_autoresize_limit: NotRequired[pulumi.Input[_builtins.int]]
    disk_size: NotRequired[pulumi.Input[_builtins.int]]
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    edition: NotRequired[pulumi.Input[_builtins.str]]
    effective_availability_type: NotRequired[pulumi.Input[_builtins.str]]
    enable_dataplex_integration: NotRequired[pulumi.Input[_builtins.bool]]
    enable_google_ml_integration: NotRequired[pulumi.Input[_builtins.bool]]
    final_backup_config: NotRequired[pulumi.Input[DatabaseInstanceSettingsFinalBackupConfigArgsDict]]
    insights_config: NotRequired[pulumi.Input[DatabaseInstanceSettingsInsightsConfigArgsDict]]
    ip_configuration: NotRequired[pulumi.Input[DatabaseInstanceSettingsIpConfigurationArgsDict]]
    location_preference: NotRequired[pulumi.Input[DatabaseInstanceSettingsLocationPreferenceArgsDict]]
    maintenance_window: NotRequired[pulumi.Input[DatabaseInstanceSettingsMaintenanceWindowArgsDict]]
    password_validation_policy: NotRequired[pulumi.Input[DatabaseInstanceSettingsPasswordValidationPolicyArgsDict]]
    pricing_plan: NotRequired[pulumi.Input[_builtins.str]]
    read_pool_auto_scale_config: NotRequired[pulumi.Input[DatabaseInstanceSettingsReadPoolAutoScaleConfigArgsDict]]
    retain_backups_on_delete: NotRequired[pulumi.Input[_builtins.bool]]
    sql_server_audit_config: NotRequired[pulumi.Input[DatabaseInstanceSettingsSqlServerAuditConfigArgsDict]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]
    user_labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    version: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DatabaseInstanceSettingsArgs:
    def __init__(__self__, *, tier: pulumi.Input[_builtins.str], activation_policy: Optional[pulumi.Input[_builtins.str]] = ..., active_directory_config: Optional[pulumi.Input[DatabaseInstanceSettingsActiveDirectoryConfigArgs]] = ..., advanced_machine_features: Optional[pulumi.Input[DatabaseInstanceSettingsAdvancedMachineFeaturesArgs]] = ..., auto_upgrade_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., availability_type: Optional[pulumi.Input[_builtins.str]] = ..., backup_configuration: Optional[pulumi.Input[DatabaseInstanceSettingsBackupConfigurationArgs]] = ..., collation: Optional[pulumi.Input[_builtins.str]] = ..., connection_pool_configs: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsConnectionPoolConfigArgs]]]] = ..., connector_enforcement: Optional[pulumi.Input[_builtins.str]] = ..., data_api_access: Optional[pulumi.Input[_builtins.str]] = ..., data_cache_config: Optional[pulumi.Input[DatabaseInstanceSettingsDataCacheConfigArgs]] = ..., data_disk_provisioned_iops: Optional[pulumi.Input[_builtins.int]] = ..., data_disk_provisioned_throughput: Optional[pulumi.Input[_builtins.int]] = ..., database_flags: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsDatabaseFlagArgs]]]] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., deny_maintenance_period: Optional[pulumi.Input[DatabaseInstanceSettingsDenyMaintenancePeriodArgs]] = ..., disk_autoresize: Optional[pulumi.Input[_builtins.bool]] = ..., disk_autoresize_limit: Optional[pulumi.Input[_builtins.int]] = ..., disk_size: Optional[pulumi.Input[_builtins.int]] = ..., disk_type: Optional[pulumi.Input[_builtins.str]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., effective_availability_type: Optional[pulumi.Input[_builtins.str]] = ..., enable_dataplex_integration: Optional[pulumi.Input[_builtins.bool]] = ..., enable_google_ml_integration: Optional[pulumi.Input[_builtins.bool]] = ..., final_backup_config: Optional[pulumi.Input[DatabaseInstanceSettingsFinalBackupConfigArgs]] = ..., insights_config: Optional[pulumi.Input[DatabaseInstanceSettingsInsightsConfigArgs]] = ..., ip_configuration: Optional[pulumi.Input[DatabaseInstanceSettingsIpConfigurationArgs]] = ..., location_preference: Optional[pulumi.Input[DatabaseInstanceSettingsLocationPreferenceArgs]] = ..., maintenance_window: Optional[pulumi.Input[DatabaseInstanceSettingsMaintenanceWindowArgs]] = ..., password_validation_policy: Optional[pulumi.Input[DatabaseInstanceSettingsPasswordValidationPolicyArgs]] = ..., pricing_plan: Optional[pulumi.Input[_builtins.str]] = ..., read_pool_auto_scale_config: Optional[pulumi.Input[DatabaseInstanceSettingsReadPoolAutoScaleConfigArgs]] = ..., retain_backups_on_delete: Optional[pulumi.Input[_builtins.bool]] = ..., sql_server_audit_config: Optional[pulumi.Input[DatabaseInstanceSettingsSqlServerAuditConfigArgs]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., user_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tier.setter
    def tier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationPolicy")
    def activation_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @activation_policy.setter
    def activation_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfig")
    def active_directory_config(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsActiveDirectoryConfigArgs]]:
        ...
    
    @active_directory_config.setter
    def active_directory_config(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsActiveDirectoryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsAdvancedMachineFeaturesArgs]]:
        ...
    
    @advanced_machine_features.setter
    def advanced_machine_features(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsAdvancedMachineFeaturesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpgradeEnabled")
    def auto_upgrade_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_upgrade_enabled.setter
    def auto_upgrade_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityType")
    def availability_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_type.setter
    def availability_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfiguration")
    def backup_configuration(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsBackupConfigurationArgs]]:
        ...
    
    @backup_configuration.setter
    def backup_configuration(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsBackupConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collation.setter
    def collation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolConfigs")
    def connection_pool_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsConnectionPoolConfigArgs]]]]:
        
        ...
    
    @connection_pool_configs.setter
    def connection_pool_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsConnectionPoolConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorEnforcement")
    def connector_enforcement(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connector_enforcement.setter
    def connector_enforcement(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataApiAccess")
    def data_api_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_api_access.setter
    def data_api_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCacheConfig")
    def data_cache_config(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsDataCacheConfigArgs]]:
        
        ...
    
    @data_cache_config.setter
    def data_cache_config(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsDataCacheConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskProvisionedIops")
    def data_disk_provisioned_iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @data_disk_provisioned_iops.setter
    def data_disk_provisioned_iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskProvisionedThroughput")
    def data_disk_provisioned_throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @data_disk_provisioned_throughput.setter
    def data_disk_provisioned_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFlags")
    def database_flags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsDatabaseFlagArgs]]]]:
        ...
    
    @database_flags.setter
    def database_flags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsDatabaseFlagArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="denyMaintenancePeriod")
    def deny_maintenance_period(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsDenyMaintenancePeriodArgs]]:
        ...
    
    @deny_maintenance_period.setter
    def deny_maintenance_period(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsDenyMaintenancePeriodArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskAutoresize")
    def disk_autoresize(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disk_autoresize.setter
    def disk_autoresize(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskAutoresizeLimit")
    def disk_autoresize_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_autoresize_limit.setter
    def disk_autoresize_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_size.setter
    def disk_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAvailabilityType")
    def effective_availability_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effective_availability_type.setter
    def effective_availability_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDataplexIntegration")
    def enable_dataplex_integration(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_dataplex_integration.setter
    def enable_dataplex_integration(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGoogleMlIntegration")
    def enable_google_ml_integration(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_google_ml_integration.setter
    def enable_google_ml_integration(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalBackupConfig")
    def final_backup_config(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsFinalBackupConfigArgs]]:
        
        ...
    
    @final_backup_config.setter
    def final_backup_config(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsFinalBackupConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightsConfig")
    def insights_config(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsInsightsConfigArgs]]:
        
        ...
    
    @insights_config.setter
    def insights_config(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsInsightsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfiguration")
    def ip_configuration(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsIpConfigurationArgs]]:
        ...
    
    @ip_configuration.setter
    def ip_configuration(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsIpConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationPreference")
    def location_preference(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsLocationPreferenceArgs]]:
        ...
    
    @location_preference.setter
    def location_preference(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsLocationPreferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsMaintenanceWindowArgs]]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsMaintenanceWindowArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordValidationPolicy")
    def password_validation_policy(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsPasswordValidationPolicyArgs]]:
        ...
    
    @password_validation_policy.setter
    def password_validation_policy(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsPasswordValidationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingPlan")
    def pricing_plan(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pricing_plan.setter
    def pricing_plan(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readPoolAutoScaleConfig")
    def read_pool_auto_scale_config(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsReadPoolAutoScaleConfigArgs]]:
        
        ...
    
    @read_pool_auto_scale_config.setter
    def read_pool_auto_scale_config(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsReadPoolAutoScaleConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainBackupsOnDelete")
    def retain_backups_on_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @retain_backups_on_delete.setter
    def retain_backups_on_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerAuditConfig")
    def sql_server_audit_config(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsSqlServerAuditConfigArgs]]:
        ...
    
    @sql_server_audit_config.setter
    def sql_server_audit_config(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsSqlServerAuditConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_labels.setter
    def user_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DatabaseInstanceSettingsActiveDirectoryConfigArgsDict(TypedDict):
    domain: pulumi.Input[_builtins.str]


@pulumi.input_type
class DatabaseInstanceSettingsActiveDirectoryConfigArgs:
    def __init__(__self__, *, domain: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DatabaseInstanceSettingsAdvancedMachineFeaturesArgsDict(TypedDict):
    threads_per_core: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DatabaseInstanceSettingsAdvancedMachineFeaturesArgs:
    def __init__(__self__, *, threads_per_core: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @threads_per_core.setter
    def threads_per_core(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DatabaseInstanceSettingsBackupConfigurationArgsDict(TypedDict):
    backup_retention_settings: NotRequired[pulumi.Input[DatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsArgsDict]]
    backup_tier: NotRequired[pulumi.Input[_builtins.str]]
    binary_log_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    point_in_time_recovery_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    transaction_log_retention_days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DatabaseInstanceSettingsBackupConfigurationArgs:
    def __init__(__self__, *, backup_retention_settings: Optional[pulumi.Input[DatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsArgs]] = ..., backup_tier: Optional[pulumi.Input[_builtins.str]] = ..., binary_log_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., point_in_time_recovery_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., transaction_log_retention_days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionSettings")
    def backup_retention_settings(self) -> Optional[pulumi.Input[DatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsArgs]]:
        
        ...
    
    @backup_retention_settings.setter
    def backup_retention_settings(self, value: Optional[pulumi.Input[DatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupTier")
    def backup_tier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_tier.setter
    def backup_tier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryLogEnabled")
    def binary_log_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @binary_log_enabled.setter
    def binary_log_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecoveryEnabled")
    def point_in_time_recovery_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @point_in_time_recovery_enabled.setter
    def point_in_time_recovery_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionLogRetentionDays")
    def transaction_log_retention_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @transaction_log_retention_days.setter
    def transaction_log_retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsArgsDict(TypedDict):
    retained_backups: pulumi.Input[_builtins.int]
    retention_unit: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceSettingsBackupConfigurationBackupRetentionSettingsArgs:
    def __init__(__self__, *, retained_backups: pulumi.Input[_builtins.int], retention_unit: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainedBackups")
    def retained_backups(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @retained_backups.setter
    def retained_backups(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionUnit")
    def retention_unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @retention_unit.setter
    def retention_unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstanceSettingsConnectionPoolConfigArgsDict(TypedDict):
    connection_pooling_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    flags: NotRequired[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsConnectionPoolConfigFlagArgsDict]]]]


@pulumi.input_type
class DatabaseInstanceSettingsConnectionPoolConfigArgs:
    def __init__(__self__, *, connection_pooling_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., flags: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsConnectionPoolConfigFlagArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolingEnabled")
    def connection_pooling_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @connection_pooling_enabled.setter
    def connection_pooling_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsConnectionPoolConfigFlagArgs]]]]:
        
        ...
    
    @flags.setter
    def flags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsConnectionPoolConfigFlagArgs]]]]): # -> None:
        ...
    


class DatabaseInstanceSettingsConnectionPoolConfigFlagArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class DatabaseInstanceSettingsConnectionPoolConfigFlagArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DatabaseInstanceSettingsDataCacheConfigArgsDict(TypedDict):
    data_cache_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DatabaseInstanceSettingsDataCacheConfigArgs:
    def __init__(__self__, *, data_cache_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCacheEnabled")
    def data_cache_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @data_cache_enabled.setter
    def data_cache_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DatabaseInstanceSettingsDatabaseFlagArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class DatabaseInstanceSettingsDatabaseFlagArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DatabaseInstanceSettingsDenyMaintenancePeriodArgsDict(TypedDict):
    end_date: pulumi.Input[_builtins.str]
    start_date: pulumi.Input[_builtins.str]
    time: pulumi.Input[_builtins.str]


@pulumi.input_type
class DatabaseInstanceSettingsDenyMaintenancePeriodArgs:
    def __init__(__self__, *, end_date: pulumi.Input[_builtins.str], start_date: pulumi.Input[_builtins.str], time: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @end_date.setter
    def end_date(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @start_date.setter
    def start_date(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @time.setter
    def time(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DatabaseInstanceSettingsFinalBackupConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    retention_days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DatabaseInstanceSettingsFinalBackupConfigArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., retention_days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DatabaseInstanceSettingsInsightsConfigArgsDict(TypedDict):
    enhanced_query_insights_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    query_insights_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    query_plans_per_minute: NotRequired[pulumi.Input[_builtins.int]]
    query_string_length: NotRequired[pulumi.Input[_builtins.int]]
    record_application_tags: NotRequired[pulumi.Input[_builtins.bool]]
    record_client_address: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DatabaseInstanceSettingsInsightsConfigArgs:
    def __init__(__self__, *, enhanced_query_insights_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., query_insights_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., query_plans_per_minute: Optional[pulumi.Input[_builtins.int]] = ..., query_string_length: Optional[pulumi.Input[_builtins.int]] = ..., record_application_tags: Optional[pulumi.Input[_builtins.bool]] = ..., record_client_address: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedQueryInsightsEnabled")
    def enhanced_query_insights_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enhanced_query_insights_enabled.setter
    def enhanced_query_insights_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryInsightsEnabled")
    def query_insights_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @query_insights_enabled.setter
    def query_insights_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryPlansPerMinute")
    def query_plans_per_minute(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @query_plans_per_minute.setter
    def query_plans_per_minute(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringLength")
    def query_string_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @query_string_length.setter
    def query_string_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordApplicationTags")
    def record_application_tags(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @record_application_tags.setter
    def record_application_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordClientAddress")
    def record_client_address(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @record_client_address.setter
    def record_client_address(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DatabaseInstanceSettingsIpConfigurationArgsDict(TypedDict):
    allocated_ip_range: NotRequired[pulumi.Input[_builtins.str]]
    authorized_networks: NotRequired[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsIpConfigurationAuthorizedNetworkArgsDict]]]]
    custom_subject_alternative_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    enable_private_path_for_google_cloud_services: NotRequired[pulumi.Input[_builtins.bool]]
    ipv4_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    private_network: NotRequired[pulumi.Input[_builtins.str]]
    psc_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsIpConfigurationPscConfigArgsDict]]]]
    server_ca_mode: NotRequired[pulumi.Input[_builtins.str]]
    server_ca_pool: NotRequired[pulumi.Input[_builtins.str]]
    ssl_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceSettingsIpConfigurationArgs:
    def __init__(__self__, *, allocated_ip_range: Optional[pulumi.Input[_builtins.str]] = ..., authorized_networks: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsIpConfigurationAuthorizedNetworkArgs]]]] = ..., custom_subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enable_private_path_for_google_cloud_services: Optional[pulumi.Input[_builtins.bool]] = ..., ipv4_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., private_network: Optional[pulumi.Input[_builtins.str]] = ..., psc_configs: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsIpConfigurationPscConfigArgs]]]] = ..., server_ca_mode: Optional[pulumi.Input[_builtins.str]] = ..., server_ca_pool: Optional[pulumi.Input[_builtins.str]] = ..., ssl_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocated_ip_range.setter
    def allocated_ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedNetworks")
    def authorized_networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsIpConfigurationAuthorizedNetworkArgs]]]]:
        ...
    
    @authorized_networks.setter
    def authorized_networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsIpConfigurationAuthorizedNetworkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customSubjectAlternativeNames")
    def custom_subject_alternative_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @custom_subject_alternative_names.setter
    def custom_subject_alternative_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivatePathForGoogleCloudServices")
    def enable_private_path_for_google_cloud_services(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_private_path_for_google_cloud_services.setter
    def enable_private_path_for_google_cloud_services(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Enabled")
    def ipv4_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ipv4_enabled.setter
    def ipv4_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateNetwork")
    def private_network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_network.setter
    def private_network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsIpConfigurationPscConfigArgs]]]]:
        
        ...
    
    @psc_configs.setter
    def psc_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsIpConfigurationPscConfigArgs]]]]): # -> None:
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
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssl_mode.setter
    def ssl_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstanceSettingsIpConfigurationAuthorizedNetworkArgsDict(TypedDict):
    value: pulumi.Input[_builtins.str]
    expiration_time: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceSettingsIpConfigurationAuthorizedNetworkArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str], expiration_time: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiration_time.setter
    def expiration_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstanceSettingsIpConfigurationPscConfigArgsDict(TypedDict):
    allowed_consumer_projects: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    network_attachment_uri: NotRequired[pulumi.Input[_builtins.str]]
    psc_auto_connections: NotRequired[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsIpConfigurationPscConfigPscAutoConnectionArgsDict]]]]
    psc_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DatabaseInstanceSettingsIpConfigurationPscConfigArgs:
    def __init__(__self__, *, allowed_consumer_projects: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., network_attachment_uri: Optional[pulumi.Input[_builtins.str]] = ..., psc_auto_connections: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsIpConfigurationPscConfigPscAutoConnectionArgs]]]] = ..., psc_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedConsumerProjects")
    def allowed_consumer_projects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_consumer_projects.setter
    def allowed_consumer_projects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAttachmentUri")
    def network_attachment_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_attachment_uri.setter
    def network_attachment_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscAutoConnections")
    def psc_auto_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsIpConfigurationPscConfigPscAutoConnectionArgs]]]]:
        
        ...
    
    @psc_auto_connections.setter
    def psc_auto_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsIpConfigurationPscConfigPscAutoConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscEnabled")
    def psc_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @psc_enabled.setter
    def psc_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DatabaseInstanceSettingsIpConfigurationPscConfigPscAutoConnectionArgsDict(TypedDict):
    consumer_network: pulumi.Input[_builtins.str]
    consumer_network_status: NotRequired[pulumi.Input[_builtins.str]]
    consumer_service_project_id: NotRequired[pulumi.Input[_builtins.str]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceSettingsIpConfigurationPscConfigPscAutoConnectionArgs:
    def __init__(__self__, *, consumer_network: pulumi.Input[_builtins.str], consumer_network_status: Optional[pulumi.Input[_builtins.str]] = ..., consumer_service_project_id: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerNetwork")
    def consumer_network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @consumer_network.setter
    def consumer_network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerNetworkStatus")
    def consumer_network_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @consumer_network_status.setter
    def consumer_network_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerServiceProjectId")
    def consumer_service_project_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @consumer_service_project_id.setter
    def consumer_service_project_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstanceSettingsLocationPreferenceArgsDict(TypedDict):
    follow_gae_application: NotRequired[pulumi.Input[_builtins.str]]
    secondary_zone: NotRequired[pulumi.Input[_builtins.str]]
    zone: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceSettingsLocationPreferenceArgs:
    def __init__(__self__, *, follow_gae_application: Optional[pulumi.Input[_builtins.str]] = ..., secondary_zone: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="followGaeApplication")
    def follow_gae_application(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @follow_gae_application.setter
    def follow_gae_application(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryZone")
    def secondary_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secondary_zone.setter
    def secondary_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstanceSettingsMaintenanceWindowArgsDict(TypedDict):
    day: NotRequired[pulumi.Input[_builtins.int]]
    hour: NotRequired[pulumi.Input[_builtins.int]]
    update_track: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceSettingsMaintenanceWindowArgs:
    def __init__(__self__, *, day: Optional[pulumi.Input[_builtins.int]] = ..., hour: Optional[pulumi.Input[_builtins.int]] = ..., update_track: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hour.setter
    def hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTrack")
    def update_track(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_track.setter
    def update_track(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DatabaseInstanceSettingsPasswordValidationPolicyArgsDict(TypedDict):
    enable_password_policy: pulumi.Input[_builtins.bool]
    complexity: NotRequired[pulumi.Input[_builtins.str]]
    disallow_username_substring: NotRequired[pulumi.Input[_builtins.bool]]
    min_length: NotRequired[pulumi.Input[_builtins.int]]
    password_change_interval: NotRequired[pulumi.Input[_builtins.str]]
    reuse_interval: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DatabaseInstanceSettingsPasswordValidationPolicyArgs:
    def __init__(__self__, *, enable_password_policy: pulumi.Input[_builtins.bool], complexity: Optional[pulumi.Input[_builtins.str]] = ..., disallow_username_substring: Optional[pulumi.Input[_builtins.bool]] = ..., min_length: Optional[pulumi.Input[_builtins.int]] = ..., password_change_interval: Optional[pulumi.Input[_builtins.str]] = ..., reuse_interval: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePasswordPolicy")
    def enable_password_policy(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_password_policy.setter
    def enable_password_policy(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def complexity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @complexity.setter
    def complexity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disallowUsernameSubstring")
    def disallow_username_substring(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disallow_username_substring.setter
    def disallow_username_substring(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minLength")
    def min_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_length.setter
    def min_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordChangeInterval")
    def password_change_interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_change_interval.setter
    def password_change_interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reuseInterval")
    def reuse_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @reuse_interval.setter
    def reuse_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DatabaseInstanceSettingsReadPoolAutoScaleConfigArgsDict(TypedDict):
    disable_scale_in: NotRequired[pulumi.Input[_builtins.bool]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    max_node_count: NotRequired[pulumi.Input[_builtins.int]]
    min_node_count: NotRequired[pulumi.Input[_builtins.int]]
    scale_in_cooldown_seconds: NotRequired[pulumi.Input[_builtins.int]]
    scale_out_cooldown_seconds: NotRequired[pulumi.Input[_builtins.int]]
    target_metrics: NotRequired[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsReadPoolAutoScaleConfigTargetMetricArgsDict]]]]


@pulumi.input_type
class DatabaseInstanceSettingsReadPoolAutoScaleConfigArgs:
    def __init__(__self__, *, disable_scale_in: Optional[pulumi.Input[_builtins.bool]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., max_node_count: Optional[pulumi.Input[_builtins.int]] = ..., min_node_count: Optional[pulumi.Input[_builtins.int]] = ..., scale_in_cooldown_seconds: Optional[pulumi.Input[_builtins.int]] = ..., scale_out_cooldown_seconds: Optional[pulumi.Input[_builtins.int]] = ..., target_metrics: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsReadPoolAutoScaleConfigTargetMetricArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_scale_in.setter
    def disable_scale_in(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_node_count.setter
    def max_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_node_count.setter
    def min_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleInCooldownSeconds")
    def scale_in_cooldown_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @scale_in_cooldown_seconds.setter
    def scale_in_cooldown_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOutCooldownSeconds")
    def scale_out_cooldown_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @scale_out_cooldown_seconds.setter
    def scale_out_cooldown_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetMetrics")
    def target_metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsReadPoolAutoScaleConfigTargetMetricArgs]]]]:
        
        ...
    
    @target_metrics.setter
    def target_metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInstanceSettingsReadPoolAutoScaleConfigTargetMetricArgs]]]]): # -> None:
        ...
    


class DatabaseInstanceSettingsReadPoolAutoScaleConfigTargetMetricArgsDict(TypedDict):
    metric: NotRequired[pulumi.Input[_builtins.str]]
    target_value: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class DatabaseInstanceSettingsReadPoolAutoScaleConfigTargetMetricArgs:
    def __init__(__self__, *, metric: Optional[pulumi.Input[_builtins.str]] = ..., target_value: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metric(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metric.setter
    def metric(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @target_value.setter
    def target_value(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class DatabaseInstanceSettingsSqlServerAuditConfigArgsDict(TypedDict):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    retention_interval: NotRequired[pulumi.Input[_builtins.str]]
    upload_interval: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatabaseInstanceSettingsSqlServerAuditConfigArgs:
    def __init__(__self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ..., retention_interval: Optional[pulumi.Input[_builtins.str]] = ..., upload_interval: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionInterval")
    def retention_interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @retention_interval.setter
    def retention_interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadInterval")
    def upload_interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @upload_interval.setter
    def upload_interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserPasswordPolicyArgsDict(TypedDict):
    allowed_failed_attempts: NotRequired[pulumi.Input[_builtins.int]]
    enable_failed_attempts_check: NotRequired[pulumi.Input[_builtins.bool]]
    enable_password_verification: NotRequired[pulumi.Input[_builtins.bool]]
    password_expiration_duration: NotRequired[pulumi.Input[_builtins.str]]
    statuses: NotRequired[pulumi.Input[Sequence[pulumi.Input[UserPasswordPolicyStatusArgsDict]]]]


@pulumi.input_type
class UserPasswordPolicyArgs:
    def __init__(__self__, *, allowed_failed_attempts: Optional[pulumi.Input[_builtins.int]] = ..., enable_failed_attempts_check: Optional[pulumi.Input[_builtins.bool]] = ..., enable_password_verification: Optional[pulumi.Input[_builtins.bool]] = ..., password_expiration_duration: Optional[pulumi.Input[_builtins.str]] = ..., statuses: Optional[pulumi.Input[Sequence[pulumi.Input[UserPasswordPolicyStatusArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedFailedAttempts")
    def allowed_failed_attempts(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @allowed_failed_attempts.setter
    def allowed_failed_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFailedAttemptsCheck")
    def enable_failed_attempts_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_failed_attempts_check.setter
    def enable_failed_attempts_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePasswordVerification")
    def enable_password_verification(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_password_verification.setter
    def enable_password_verification(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordExpirationDuration")
    def password_expiration_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_expiration_duration.setter
    def password_expiration_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserPasswordPolicyStatusArgs]]]]:
        ...
    
    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserPasswordPolicyStatusArgs]]]]): # -> None:
        ...
    


class UserPasswordPolicyStatusArgsDict(TypedDict):
    locked: NotRequired[pulumi.Input[_builtins.bool]]
    password_expiration_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class UserPasswordPolicyStatusArgs:
    def __init__(__self__, *, locked: Optional[pulumi.Input[_builtins.bool]] = ..., password_expiration_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locked(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @locked.setter
    def locked(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordExpirationTime")
    def password_expiration_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_expiration_time.setter
    def password_expiration_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserSqlServerUserDetailArgsDict(TypedDict):
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    server_roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class UserSqlServerUserDetailArgs:
    def __init__(__self__, *, disabled: Optional[pulumi.Input[_builtins.bool]] = ..., server_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverRoles")
    def server_roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @server_roles.setter
    def server_roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


