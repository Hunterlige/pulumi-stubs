

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DatabaseInstanceClone', 'DatabaseInstanceDnsName', 'DatabaseInstanceIpAddress', 'DatabaseInstancePointInTimeRestoreContext', 'DatabaseInstanceReplicaConfiguration', 'DatabaseInstanceReplicationCluster', 'DatabaseInstanceRestoreBackupContext', 'DatabaseInstanceServerCaCert', 'DatabaseInstanceSettings', 'DatabaseInstanceSettingsActiveDirectoryConfig', 'DatabaseInstanceSettingsAdvancedMachineFeatures', 'DatabaseInstanceSettingsBackupConfiguration', ..., 'DatabaseInstanceSettingsConnectionPoolConfig', 'DatabaseInstanceSettingsConnectionPoolConfigFlag', 'DatabaseInstanceSettingsDataCacheConfig', 'DatabaseInstanceSettingsDatabaseFlag', 'DatabaseInstanceSettingsDenyMaintenancePeriod', 'DatabaseInstanceSettingsFinalBackupConfig', 'DatabaseInstanceSettingsInsightsConfig', 'DatabaseInstanceSettingsIpConfiguration', ..., 'DatabaseInstanceSettingsIpConfigurationPscConfig', ..., 'DatabaseInstanceSettingsLocationPreference', 'DatabaseInstanceSettingsMaintenanceWindow', 'DatabaseInstanceSettingsPasswordValidationPolicy', 'DatabaseInstanceSettingsReadPoolAutoScaleConfig', ..., 'DatabaseInstanceSettingsSqlServerAuditConfig', 'UserPasswordPolicy', 'UserPasswordPolicyStatus', 'UserSqlServerUserDetail', 'GetCaCertsCertResult', 'GetDatabaseInstanceCloneResult', 'GetDatabaseInstanceDnsNameResult', 'GetDatabaseInstanceIpAddressResult', 'GetDatabaseInstancePointInTimeRestoreContextResult', 'GetDatabaseInstanceReplicaConfigurationResult', 'GetDatabaseInstanceReplicationClusterResult', 'GetDatabaseInstanceRestoreBackupContextResult', 'GetDatabaseInstanceServerCaCertResult', 'GetDatabaseInstanceSettingResult', ..., ..., ..., ..., ..., ..., 'GetDatabaseInstanceSettingDataCacheConfigResult', 'GetDatabaseInstanceSettingDatabaseFlagResult', ..., 'GetDatabaseInstanceSettingFinalBackupConfigResult', 'GetDatabaseInstanceSettingInsightsConfigResult', 'GetDatabaseInstanceSettingIpConfigurationResult', ..., ..., ..., 'GetDatabaseInstanceSettingLocationPreferenceResult', 'GetDatabaseInstanceSettingMaintenanceWindowResult', ..., ..., ..., ..., 'GetDatabaseInstancesInstanceResult', 'GetDatabaseInstancesInstanceCloneResult', 'GetDatabaseInstancesInstanceDnsNameResult', 'GetDatabaseInstancesInstanceIpAddressResult', ..., ..., ..., ..., 'GetDatabaseInstancesInstanceServerCaCertResult', 'GetDatabaseInstancesInstanceSettingResult', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'GetDatabasesDatabaseResult', 'GetTiersTierResult']
@pulumi.output_type
class DatabaseInstanceClone(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_instance_name: _builtins.str, allocated_ip_range: Optional[_builtins.str] = ..., database_names: Optional[Sequence[_builtins.str]] = ..., point_in_time: Optional[_builtins.str] = ..., preferred_zone: Optional[_builtins.str] = ..., source_instance_deletion_time: Optional[_builtins.str] = ..., source_project: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceInstanceName")
    def source_instance_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseNames")
    def database_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredZone")
    def preferred_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceInstanceDeletionTime")
    def source_instance_deletion_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceProject")
    def source_project(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceDnsName(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_type: Optional[_builtins.str] = ..., dns_scope: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsScope")
    def dns_scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceIpAddress(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address: Optional[_builtins.str] = ..., time_to_retire: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToRetire")
    def time_to_retire(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstancePointInTimeRestoreContext(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, datasource: _builtins.str, allocated_ip_range: Optional[_builtins.str] = ..., point_in_time: Optional[_builtins.str] = ..., preferred_zone: Optional[_builtins.str] = ..., target_instance: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datasource(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredZone")
    def preferred_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetInstance")
    def target_instance(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceReplicaConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ca_certificate: Optional[_builtins.str] = ..., cascadable_replica: Optional[_builtins.bool] = ..., client_certificate: Optional[_builtins.str] = ..., client_key: Optional[_builtins.str] = ..., connect_retry_interval: Optional[_builtins.int] = ..., dump_file_path: Optional[_builtins.str] = ..., failover_target: Optional[_builtins.bool] = ..., master_heartbeat_period: Optional[_builtins.int] = ..., password: Optional[_builtins.str] = ..., ssl_cipher: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ..., verify_server_certificate: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cascadableReplica")
    def cascadable_replica(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectRetryInterval")
    def connect_retry_interval(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpFilePath")
    def dump_file_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverTarget")
    def failover_target(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterHeartbeatPeriod")
    def master_heartbeat_period(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCipher")
    def ssl_cipher(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifyServerCertificate")
    def verify_server_certificate(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceReplicationCluster(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dr_replica: Optional[_builtins.bool] = ..., failover_dr_replica_name: Optional[_builtins.str] = ..., psa_write_endpoint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="drReplica")
    def dr_replica(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverDrReplicaName")
    def failover_dr_replica_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="psaWriteEndpoint")
    def psa_write_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceRestoreBackupContext(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_run_id: _builtins.int, instance_id: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRunId")
    def backup_run_id(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceServerCaCert(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cert: Optional[_builtins.str] = ..., common_name: Optional[_builtins.str] = ..., create_time: Optional[_builtins.str] = ..., expiration_time: Optional[_builtins.str] = ..., sha1_fingerprint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tier: _builtins.str, activation_policy: Optional[_builtins.str] = ..., active_directory_config: Optional[outputs.DatabaseInstanceSettingsActiveDirectoryConfig] = ..., advanced_machine_features: Optional[outputs.DatabaseInstanceSettingsAdvancedMachineFeatures] = ..., auto_upgrade_enabled: Optional[_builtins.bool] = ..., availability_type: Optional[_builtins.str] = ..., backup_configuration: Optional[outputs.DatabaseInstanceSettingsBackupConfiguration] = ..., collation: Optional[_builtins.str] = ..., connection_pool_configs: Optional[Sequence[outputs.DatabaseInstanceSettingsConnectionPoolConfig]] = ..., connector_enforcement: Optional[_builtins.str] = ..., data_api_access: Optional[_builtins.str] = ..., data_cache_config: Optional[outputs.DatabaseInstanceSettingsDataCacheConfig] = ..., data_disk_provisioned_iops: Optional[_builtins.int] = ..., data_disk_provisioned_throughput: Optional[_builtins.int] = ..., database_flags: Optional[Sequence[outputs.DatabaseInstanceSettingsDatabaseFlag]] = ..., deletion_protection_enabled: Optional[_builtins.bool] = ..., deny_maintenance_period: Optional[outputs.DatabaseInstanceSettingsDenyMaintenancePeriod] = ..., disk_autoresize: Optional[_builtins.bool] = ..., disk_autoresize_limit: Optional[_builtins.int] = ..., disk_size: Optional[_builtins.int] = ..., disk_type: Optional[_builtins.str] = ..., edition: Optional[_builtins.str] = ..., effective_availability_type: Optional[_builtins.str] = ..., enable_dataplex_integration: Optional[_builtins.bool] = ..., enable_google_ml_integration: Optional[_builtins.bool] = ..., final_backup_config: Optional[outputs.DatabaseInstanceSettingsFinalBackupConfig] = ..., insights_config: Optional[outputs.DatabaseInstanceSettingsInsightsConfig] = ..., ip_configuration: Optional[outputs.DatabaseInstanceSettingsIpConfiguration] = ..., location_preference: Optional[outputs.DatabaseInstanceSettingsLocationPreference] = ..., maintenance_window: Optional[outputs.DatabaseInstanceSettingsMaintenanceWindow] = ..., password_validation_policy: Optional[outputs.DatabaseInstanceSettingsPasswordValidationPolicy] = ..., pricing_plan: Optional[_builtins.str] = ..., read_pool_auto_scale_config: Optional[outputs.DatabaseInstanceSettingsReadPoolAutoScaleConfig] = ..., retain_backups_on_delete: Optional[_builtins.bool] = ..., sql_server_audit_config: Optional[outputs.DatabaseInstanceSettingsSqlServerAuditConfig] = ..., time_zone: Optional[_builtins.str] = ..., user_labels: Optional[Mapping[str, _builtins.str]] = ..., version: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationPolicy")
    def activation_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfig")
    def active_directory_config(self) -> Optional[outputs.DatabaseInstanceSettingsActiveDirectoryConfig]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(self) -> Optional[outputs.DatabaseInstanceSettingsAdvancedMachineFeatures]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpgradeEnabled")
    def auto_upgrade_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityType")
    def availability_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfiguration")
    def backup_configuration(self) -> Optional[outputs.DatabaseInstanceSettingsBackupConfiguration]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolConfigs")
    def connection_pool_configs(self) -> Optional[Sequence[outputs.DatabaseInstanceSettingsConnectionPoolConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorEnforcement")
    def connector_enforcement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataApiAccess")
    def data_api_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCacheConfig")
    def data_cache_config(self) -> Optional[outputs.DatabaseInstanceSettingsDataCacheConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskProvisionedIops")
    def data_disk_provisioned_iops(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskProvisionedThroughput")
    def data_disk_provisioned_throughput(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFlags")
    def database_flags(self) -> Optional[Sequence[outputs.DatabaseInstanceSettingsDatabaseFlag]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denyMaintenancePeriod")
    def deny_maintenance_period(self) -> Optional[outputs.DatabaseInstanceSettingsDenyMaintenancePeriod]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskAutoresize")
    def disk_autoresize(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskAutoresizeLimit")
    def disk_autoresize_limit(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAvailabilityType")
    def effective_availability_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDataplexIntegration")
    def enable_dataplex_integration(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGoogleMlIntegration")
    def enable_google_ml_integration(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalBackupConfig")
    def final_backup_config(self) -> Optional[outputs.DatabaseInstanceSettingsFinalBackupConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightsConfig")
    def insights_config(self) -> Optional[outputs.DatabaseInstanceSettingsInsightsConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfiguration")
    def ip_configuration(self) -> Optional[outputs.DatabaseInstanceSettingsIpConfiguration]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationPreference")
    def location_preference(self) -> Optional[outputs.DatabaseInstanceSettingsLocationPreference]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[outputs.DatabaseInstanceSettingsMaintenanceWindow]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordValidationPolicy")
    def password_validation_policy(self) -> Optional[outputs.DatabaseInstanceSettingsPasswordValidationPolicy]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingPlan")
    def pricing_plan(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readPoolAutoScaleConfig")
    def read_pool_auto_scale_config(self) -> Optional[outputs.DatabaseInstanceSettingsReadPoolAutoScaleConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainBackupsOnDelete")
    def retain_backups_on_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerAuditConfig")
    def sql_server_audit_config(self) -> Optional[outputs.DatabaseInstanceSettingsSqlServerAuditConfig]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsActiveDirectoryConfig(dict):
    def __init__(__self__, *, domain: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsAdvancedMachineFeatures(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, threads_per_core: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsBackupConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_retention_settings: Optional[outputs.DatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings] = ..., backup_tier: Optional[_builtins.str] = ..., binary_log_enabled: Optional[_builtins.bool] = ..., enabled: Optional[_builtins.bool] = ..., location: Optional[_builtins.str] = ..., point_in_time_recovery_enabled: Optional[_builtins.bool] = ..., start_time: Optional[_builtins.str] = ..., transaction_log_retention_days: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionSettings")
    def backup_retention_settings(self) -> Optional[outputs.DatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupTier")
    def backup_tier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryLogEnabled")
    def binary_log_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecoveryEnabled")
    def point_in_time_recovery_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionLogRetentionDays")
    def transaction_log_retention_days(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsBackupConfigurationBackupRetentionSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, retained_backups: _builtins.int, retention_unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainedBackups")
    def retained_backups(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionUnit")
    def retention_unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsConnectionPoolConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_pooling_enabled: Optional[_builtins.bool] = ..., flags: Optional[Sequence[outputs.DatabaseInstanceSettingsConnectionPoolConfigFlag]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolingEnabled")
    def connection_pooling_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Optional[Sequence[outputs.DatabaseInstanceSettingsConnectionPoolConfigFlag]]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsConnectionPoolConfigFlag(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsDataCacheConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_cache_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCacheEnabled")
    def data_cache_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsDatabaseFlag(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsDenyMaintenancePeriod(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_date: _builtins.str, start_date: _builtins.str, time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsFinalBackupConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., retention_days: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsInsightsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enhanced_query_insights_enabled: Optional[_builtins.bool] = ..., query_insights_enabled: Optional[_builtins.bool] = ..., query_plans_per_minute: Optional[_builtins.int] = ..., query_string_length: Optional[_builtins.int] = ..., record_application_tags: Optional[_builtins.bool] = ..., record_client_address: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedQueryInsightsEnabled")
    def enhanced_query_insights_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryInsightsEnabled")
    def query_insights_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryPlansPerMinute")
    def query_plans_per_minute(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringLength")
    def query_string_length(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordApplicationTags")
    def record_application_tags(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordClientAddress")
    def record_client_address(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsIpConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allocated_ip_range: Optional[_builtins.str] = ..., authorized_networks: Optional[Sequence[outputs.DatabaseInstanceSettingsIpConfigurationAuthorizedNetwork]] = ..., custom_subject_alternative_names: Optional[Sequence[_builtins.str]] = ..., enable_private_path_for_google_cloud_services: Optional[_builtins.bool] = ..., ipv4_enabled: Optional[_builtins.bool] = ..., private_network: Optional[_builtins.str] = ..., psc_configs: Optional[Sequence[outputs.DatabaseInstanceSettingsIpConfigurationPscConfig]] = ..., server_ca_mode: Optional[_builtins.str] = ..., server_ca_pool: Optional[_builtins.str] = ..., ssl_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedNetworks")
    def authorized_networks(self) -> Optional[Sequence[outputs.DatabaseInstanceSettingsIpConfigurationAuthorizedNetwork]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customSubjectAlternativeNames")
    def custom_subject_alternative_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivatePathForGoogleCloudServices")
    def enable_private_path_for_google_cloud_services(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Enabled")
    def ipv4_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateNetwork")
    def private_network(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(self) -> Optional[Sequence[outputs.DatabaseInstanceSettingsIpConfigurationPscConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaMode")
    def server_ca_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCaPool")
    def server_ca_pool(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsIpConfigurationAuthorizedNetwork(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, value: _builtins.str, expiration_time: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsIpConfigurationPscConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_consumer_projects: Optional[Sequence[_builtins.str]] = ..., network_attachment_uri: Optional[_builtins.str] = ..., psc_auto_connections: Optional[Sequence[outputs.DatabaseInstanceSettingsIpConfigurationPscConfigPscAutoConnection]] = ..., psc_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedConsumerProjects")
    def allowed_consumer_projects(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAttachmentUri")
    def network_attachment_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscAutoConnections")
    def psc_auto_connections(self) -> Optional[Sequence[outputs.DatabaseInstanceSettingsIpConfigurationPscConfigPscAutoConnection]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscEnabled")
    def psc_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsIpConfigurationPscConfigPscAutoConnection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, consumer_network: _builtins.str, consumer_network_status: Optional[_builtins.str] = ..., consumer_service_project_id: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerNetwork")
    def consumer_network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerNetworkStatus")
    def consumer_network_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerServiceProjectId")
    def consumer_service_project_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsLocationPreference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, follow_gae_application: Optional[_builtins.str] = ..., secondary_zone: Optional[_builtins.str] = ..., zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="followGaeApplication")
    def follow_gae_application(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryZone")
    def secondary_zone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., hour: Optional[_builtins.int] = ..., update_track: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTrack")
    def update_track(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsPasswordValidationPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_password_policy: _builtins.bool, complexity: Optional[_builtins.str] = ..., disallow_username_substring: Optional[_builtins.bool] = ..., min_length: Optional[_builtins.int] = ..., password_change_interval: Optional[_builtins.str] = ..., reuse_interval: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePasswordPolicy")
    def enable_password_policy(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def complexity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disallowUsernameSubstring")
    def disallow_username_substring(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minLength")
    def min_length(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordChangeInterval")
    def password_change_interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reuseInterval")
    def reuse_interval(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsReadPoolAutoScaleConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disable_scale_in: Optional[_builtins.bool] = ..., enabled: Optional[_builtins.bool] = ..., max_node_count: Optional[_builtins.int] = ..., min_node_count: Optional[_builtins.int] = ..., scale_in_cooldown_seconds: Optional[_builtins.int] = ..., scale_out_cooldown_seconds: Optional[_builtins.int] = ..., target_metrics: Optional[Sequence[outputs.DatabaseInstanceSettingsReadPoolAutoScaleConfigTargetMetric]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleInCooldownSeconds")
    def scale_in_cooldown_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOutCooldownSeconds")
    def scale_out_cooldown_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetMetrics")
    def target_metrics(self) -> Optional[Sequence[outputs.DatabaseInstanceSettingsReadPoolAutoScaleConfigTargetMetric]]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsReadPoolAutoScaleConfigTargetMetric(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metric: Optional[_builtins.str] = ..., target_value: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metric(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class DatabaseInstanceSettingsSqlServerAuditConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket: Optional[_builtins.str] = ..., retention_interval: Optional[_builtins.str] = ..., upload_interval: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionInterval")
    def retention_interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadInterval")
    def upload_interval(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserPasswordPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_failed_attempts: Optional[_builtins.int] = ..., enable_failed_attempts_check: Optional[_builtins.bool] = ..., enable_password_verification: Optional[_builtins.bool] = ..., password_expiration_duration: Optional[_builtins.str] = ..., statuses: Optional[Sequence[outputs.UserPasswordPolicyStatus]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedFailedAttempts")
    def allowed_failed_attempts(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFailedAttemptsCheck")
    def enable_failed_attempts_check(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePasswordVerification")
    def enable_password_verification(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordExpirationDuration")
    def password_expiration_duration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Optional[Sequence[outputs.UserPasswordPolicyStatus]]:
        ...
    


@pulumi.output_type
class UserPasswordPolicyStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, locked: Optional[_builtins.bool] = ..., password_expiration_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locked(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordExpirationTime")
    def password_expiration_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserSqlServerUserDetail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disabled: Optional[_builtins.bool] = ..., server_roles: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverRoles")
    def server_roles(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class GetCaCertsCertResult(dict):
    def __init__(__self__, *, cert: _builtins.str, common_name: _builtins.str, create_time: _builtins.str, expiration_time: _builtins.str, sha1_fingerprint: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceCloneResult(dict):
    def __init__(__self__, *, allocated_ip_range: _builtins.str, database_names: Sequence[_builtins.str], point_in_time: _builtins.str, preferred_zone: _builtins.str, source_instance_deletion_time: _builtins.str, source_instance_name: _builtins.str, source_project: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseNames")
    def database_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredZone")
    def preferred_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceInstanceDeletionTime")
    def source_instance_deletion_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceInstanceName")
    def source_instance_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceProject")
    def source_project(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceDnsNameResult(dict):
    def __init__(__self__, *, connection_type: _builtins.str, dns_scope: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsScope")
    def dns_scope(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceIpAddressResult(dict):
    def __init__(__self__, *, ip_address: _builtins.str, time_to_retire: _builtins.str, type: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToRetire")
    def time_to_retire(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetDatabaseInstancePointInTimeRestoreContextResult(dict):
    def __init__(__self__, *, allocated_ip_range: _builtins.str, datasource: _builtins.str, point_in_time: _builtins.str, preferred_zone: _builtins.str, target_instance: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datasource(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredZone")
    def preferred_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetInstance")
    def target_instance(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceReplicaConfigurationResult(dict):
    def __init__(__self__, *, ca_certificate: _builtins.str, cascadable_replica: _builtins.bool, client_certificate: _builtins.str, client_key: _builtins.str, connect_retry_interval: _builtins.int, dump_file_path: _builtins.str, failover_target: _builtins.bool, master_heartbeat_period: _builtins.int, password: _builtins.str, ssl_cipher: _builtins.str, username: _builtins.str, verify_server_certificate: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cascadableReplica")
    def cascadable_replica(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectRetryInterval")
    def connect_retry_interval(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpFilePath")
    def dump_file_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverTarget")
    def failover_target(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterHeartbeatPeriod")
    def master_heartbeat_period(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCipher")
    def ssl_cipher(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifyServerCertificate")
    def verify_server_certificate(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceReplicationClusterResult(dict):
    def __init__(__self__, *, dr_replica: _builtins.bool, failover_dr_replica_name: _builtins.str, psa_write_endpoint: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="drReplica")
    def dr_replica(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverDrReplicaName")
    def failover_dr_replica_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="psaWriteEndpoint")
    def psa_write_endpoint(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceRestoreBackupContextResult(dict):
    def __init__(__self__, *, backup_run_id: _builtins.int, instance_id: _builtins.str, project: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRunId")
    def backup_run_id(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceServerCaCertResult(dict):
    def __init__(__self__, *, cert: _builtins.str, common_name: _builtins.str, create_time: _builtins.str, expiration_time: _builtins.str, sha1_fingerprint: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingResult(dict):
    def __init__(__self__, *, activation_policy: _builtins.str, active_directory_configs: Sequence[outputs.GetDatabaseInstanceSettingActiveDirectoryConfigResult], advanced_machine_features: Sequence[outputs.GetDatabaseInstanceSettingAdvancedMachineFeatureResult], auto_upgrade_enabled: _builtins.bool, availability_type: _builtins.str, backup_configurations: Sequence[outputs.GetDatabaseInstanceSettingBackupConfigurationResult], collation: _builtins.str, connection_pool_configs: Sequence[outputs.GetDatabaseInstanceSettingConnectionPoolConfigResult], connector_enforcement: _builtins.str, data_api_access: _builtins.str, data_cache_configs: Sequence[outputs.GetDatabaseInstanceSettingDataCacheConfigResult], data_disk_provisioned_iops: _builtins.int, data_disk_provisioned_throughput: _builtins.int, database_flags: Sequence[outputs.GetDatabaseInstanceSettingDatabaseFlagResult], deletion_protection_enabled: _builtins.bool, deny_maintenance_periods: Sequence[outputs.GetDatabaseInstanceSettingDenyMaintenancePeriodResult], disk_autoresize: _builtins.bool, disk_autoresize_limit: _builtins.int, disk_size: _builtins.int, disk_type: _builtins.str, edition: _builtins.str, effective_availability_type: _builtins.str, enable_dataplex_integration: _builtins.bool, enable_google_ml_integration: _builtins.bool, final_backup_configs: Sequence[outputs.GetDatabaseInstanceSettingFinalBackupConfigResult], insights_configs: Sequence[outputs.GetDatabaseInstanceSettingInsightsConfigResult], ip_configurations: Sequence[outputs.GetDatabaseInstanceSettingIpConfigurationResult], location_preferences: Sequence[outputs.GetDatabaseInstanceSettingLocationPreferenceResult], maintenance_windows: Sequence[outputs.GetDatabaseInstanceSettingMaintenanceWindowResult], password_validation_policies: Sequence[outputs.GetDatabaseInstanceSettingPasswordValidationPolicyResult], pricing_plan: _builtins.str, read_pool_auto_scale_configs: Sequence[outputs.GetDatabaseInstanceSettingReadPoolAutoScaleConfigResult], retain_backups_on_delete: _builtins.bool, sql_server_audit_configs: Sequence[outputs.GetDatabaseInstanceSettingSqlServerAuditConfigResult], tier: _builtins.str, time_zone: _builtins.str, user_labels: Mapping[str, _builtins.str], version: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationPolicy")
    def activation_policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfigs")
    def active_directory_configs(self) -> Sequence[outputs.GetDatabaseInstanceSettingActiveDirectoryConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(self) -> Sequence[outputs.GetDatabaseInstanceSettingAdvancedMachineFeatureResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpgradeEnabled")
    def auto_upgrade_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityType")
    def availability_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfigurations")
    def backup_configurations(self) -> Sequence[outputs.GetDatabaseInstanceSettingBackupConfigurationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolConfigs")
    def connection_pool_configs(self) -> Sequence[outputs.GetDatabaseInstanceSettingConnectionPoolConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorEnforcement")
    def connector_enforcement(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataApiAccess")
    def data_api_access(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCacheConfigs")
    def data_cache_configs(self) -> Sequence[outputs.GetDatabaseInstanceSettingDataCacheConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskProvisionedIops")
    def data_disk_provisioned_iops(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskProvisionedThroughput")
    def data_disk_provisioned_throughput(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFlags")
    def database_flags(self) -> Sequence[outputs.GetDatabaseInstanceSettingDatabaseFlagResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denyMaintenancePeriods")
    def deny_maintenance_periods(self) -> Sequence[outputs.GetDatabaseInstanceSettingDenyMaintenancePeriodResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskAutoresize")
    def disk_autoresize(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskAutoresizeLimit")
    def disk_autoresize_limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAvailabilityType")
    def effective_availability_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDataplexIntegration")
    def enable_dataplex_integration(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGoogleMlIntegration")
    def enable_google_ml_integration(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalBackupConfigs")
    def final_backup_configs(self) -> Sequence[outputs.GetDatabaseInstanceSettingFinalBackupConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightsConfigs")
    def insights_configs(self) -> Sequence[outputs.GetDatabaseInstanceSettingInsightsConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Sequence[outputs.GetDatabaseInstanceSettingIpConfigurationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationPreferences")
    def location_preferences(self) -> Sequence[outputs.GetDatabaseInstanceSettingLocationPreferenceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence[outputs.GetDatabaseInstanceSettingMaintenanceWindowResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordValidationPolicies")
    def password_validation_policies(self) -> Sequence[outputs.GetDatabaseInstanceSettingPasswordValidationPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingPlan")
    def pricing_plan(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readPoolAutoScaleConfigs")
    def read_pool_auto_scale_configs(self) -> Sequence[outputs.GetDatabaseInstanceSettingReadPoolAutoScaleConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainBackupsOnDelete")
    def retain_backups_on_delete(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerAuditConfigs")
    def sql_server_audit_configs(self) -> Sequence[outputs.GetDatabaseInstanceSettingSqlServerAuditConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingActiveDirectoryConfigResult(dict):
    def __init__(__self__, *, domain: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingAdvancedMachineFeatureResult(dict):
    def __init__(__self__, *, threads_per_core: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingBackupConfigurationResult(dict):
    def __init__(__self__, *, backup_retention_settings: Sequence[outputs.GetDatabaseInstanceSettingBackupConfigurationBackupRetentionSettingResult], backup_tier: _builtins.str, binary_log_enabled: _builtins.bool, enabled: _builtins.bool, location: _builtins.str, point_in_time_recovery_enabled: _builtins.bool, start_time: _builtins.str, transaction_log_retention_days: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionSettings")
    def backup_retention_settings(self) -> Sequence[outputs.GetDatabaseInstanceSettingBackupConfigurationBackupRetentionSettingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupTier")
    def backup_tier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryLogEnabled")
    def binary_log_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecoveryEnabled")
    def point_in_time_recovery_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionLogRetentionDays")
    def transaction_log_retention_days(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingBackupConfigurationBackupRetentionSettingResult(dict):
    def __init__(__self__, *, retained_backups: _builtins.int, retention_unit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainedBackups")
    def retained_backups(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionUnit")
    def retention_unit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingConnectionPoolConfigResult(dict):
    def __init__(__self__, *, connection_pooling_enabled: _builtins.bool, flags: Sequence[outputs.GetDatabaseInstanceSettingConnectionPoolConfigFlagResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolingEnabled")
    def connection_pooling_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Sequence[outputs.GetDatabaseInstanceSettingConnectionPoolConfigFlagResult]:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingConnectionPoolConfigFlagResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingDataCacheConfigResult(dict):
    def __init__(__self__, *, data_cache_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCacheEnabled")
    def data_cache_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingDatabaseFlagResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingDenyMaintenancePeriodResult(dict):
    def __init__(__self__, *, end_date: _builtins.str, start_date: _builtins.str, time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingFinalBackupConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool, retention_days: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingInsightsConfigResult(dict):
    def __init__(__self__, *, enhanced_query_insights_enabled: _builtins.bool, query_insights_enabled: _builtins.bool, query_plans_per_minute: _builtins.int, query_string_length: _builtins.int, record_application_tags: _builtins.bool, record_client_address: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedQueryInsightsEnabled")
    def enhanced_query_insights_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryInsightsEnabled")
    def query_insights_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryPlansPerMinute")
    def query_plans_per_minute(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringLength")
    def query_string_length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordApplicationTags")
    def record_application_tags(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordClientAddress")
    def record_client_address(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingIpConfigurationResult(dict):
    def __init__(__self__, *, allocated_ip_range: _builtins.str, authorized_networks: Sequence[outputs.GetDatabaseInstanceSettingIpConfigurationAuthorizedNetworkResult], custom_subject_alternative_names: Sequence[_builtins.str], enable_private_path_for_google_cloud_services: _builtins.bool, ipv4_enabled: _builtins.bool, private_network: _builtins.str, psc_configs: Sequence[outputs.GetDatabaseInstanceSettingIpConfigurationPscConfigResult], server_ca_mode: _builtins.str, server_ca_pool: _builtins.str, ssl_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedNetworks")
    def authorized_networks(self) -> Sequence[outputs.GetDatabaseInstanceSettingIpConfigurationAuthorizedNetworkResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customSubjectAlternativeNames")
    def custom_subject_alternative_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivatePathForGoogleCloudServices")
    def enable_private_path_for_google_cloud_services(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Enabled")
    def ipv4_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateNetwork")
    def private_network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(self) -> Sequence[outputs.GetDatabaseInstanceSettingIpConfigurationPscConfigResult]:
        
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
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingIpConfigurationAuthorizedNetworkResult(dict):
    def __init__(__self__, *, expiration_time: _builtins.str, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingIpConfigurationPscConfigResult(dict):
    def __init__(__self__, *, allowed_consumer_projects: Sequence[_builtins.str], network_attachment_uri: _builtins.str, psc_auto_connections: Sequence[outputs.GetDatabaseInstanceSettingIpConfigurationPscConfigPscAutoConnectionResult], psc_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedConsumerProjects")
    def allowed_consumer_projects(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAttachmentUri")
    def network_attachment_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscAutoConnections")
    def psc_auto_connections(self) -> Sequence[outputs.GetDatabaseInstanceSettingIpConfigurationPscConfigPscAutoConnectionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscEnabled")
    def psc_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingIpConfigurationPscConfigPscAutoConnectionResult(dict):
    def __init__(__self__, *, consumer_network: _builtins.str, consumer_network_status: _builtins.str, consumer_service_project_id: _builtins.str, ip_address: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerNetwork")
    def consumer_network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerNetworkStatus")
    def consumer_network_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerServiceProjectId")
    def consumer_service_project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingLocationPreferenceResult(dict):
    def __init__(__self__, *, follow_gae_application: _builtins.str, secondary_zone: _builtins.str, zone: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="followGaeApplication")
    def follow_gae_application(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryZone")
    def secondary_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingMaintenanceWindowResult(dict):
    def __init__(__self__, *, day: _builtins.int, hour: _builtins.int, update_track: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTrack")
    def update_track(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingPasswordValidationPolicyResult(dict):
    def __init__(__self__, *, complexity: _builtins.str, disallow_username_substring: _builtins.bool, enable_password_policy: _builtins.bool, min_length: _builtins.int, password_change_interval: _builtins.str, reuse_interval: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def complexity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disallowUsernameSubstring")
    def disallow_username_substring(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePasswordPolicy")
    def enable_password_policy(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minLength")
    def min_length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordChangeInterval")
    def password_change_interval(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reuseInterval")
    def reuse_interval(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingReadPoolAutoScaleConfigResult(dict):
    def __init__(__self__, *, disable_scale_in: _builtins.bool, enabled: _builtins.bool, max_node_count: _builtins.int, min_node_count: _builtins.int, scale_in_cooldown_seconds: _builtins.int, scale_out_cooldown_seconds: _builtins.int, target_metrics: Sequence[outputs.GetDatabaseInstanceSettingReadPoolAutoScaleConfigTargetMetricResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleInCooldownSeconds")
    def scale_in_cooldown_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOutCooldownSeconds")
    def scale_out_cooldown_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetMetrics")
    def target_metrics(self) -> Sequence[outputs.GetDatabaseInstanceSettingReadPoolAutoScaleConfigTargetMetricResult]:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingReadPoolAutoScaleConfigTargetMetricResult(dict):
    def __init__(__self__, *, metric: _builtins.str, target_value: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metric(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstanceSettingSqlServerAuditConfigResult(dict):
    def __init__(__self__, *, bucket: _builtins.str, retention_interval: _builtins.str, upload_interval: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionInterval")
    def retention_interval(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadInterval")
    def upload_interval(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceResult(dict):
    def __init__(__self__, *, available_maintenance_versions: Sequence[_builtins.str], backupdr_backup: _builtins.str, clones: Sequence[outputs.GetDatabaseInstancesInstanceCloneResult], connection_name: _builtins.str, database_version: _builtins.str, deletion_protection: _builtins.bool, dns_name: _builtins.str, dns_names: Sequence[outputs.GetDatabaseInstancesInstanceDnsNameResult], encryption_key_name: _builtins.str, final_backup_description: _builtins.str, first_ip_address: _builtins.str, instance_type: _builtins.str, ip_addresses: Sequence[outputs.GetDatabaseInstancesInstanceIpAddressResult], maintenance_version: _builtins.str, master_instance_name: _builtins.str, name: _builtins.str, node_count: _builtins.int, point_in_time_restore_contexts: Sequence[outputs.GetDatabaseInstancesInstancePointInTimeRestoreContextResult], private_ip_address: _builtins.str, project: _builtins.str, psc_service_attachment_link: _builtins.str, public_ip_address: _builtins.str, region: _builtins.str, replica_configurations: Sequence[outputs.GetDatabaseInstancesInstanceReplicaConfigurationResult], replica_names: Sequence[_builtins.str], replication_clusters: Sequence[outputs.GetDatabaseInstancesInstanceReplicationClusterResult], restore_backup_contexts: Sequence[outputs.GetDatabaseInstancesInstanceRestoreBackupContextResult], root_password: _builtins.str, root_password_wo: _builtins.str, root_password_wo_version: _builtins.str, self_link: _builtins.str, server_ca_certs: Sequence[outputs.GetDatabaseInstancesInstanceServerCaCertResult], service_account_email_address: _builtins.str, settings: Sequence[outputs.GetDatabaseInstancesInstanceSettingResult]) -> None:
        
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
    def clones(self) -> Sequence[outputs.GetDatabaseInstancesInstanceCloneResult]:
        
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
    def dns_names(self) -> Sequence[outputs.GetDatabaseInstancesInstanceDnsNameResult]:
        
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
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[outputs.GetDatabaseInstancesInstanceIpAddressResult]:
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
    def point_in_time_restore_contexts(self) -> Sequence[outputs.GetDatabaseInstancesInstancePointInTimeRestoreContextResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
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
    def replica_configurations(self) -> Sequence[outputs.GetDatabaseInstancesInstanceReplicaConfigurationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaNames")
    def replica_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationClusters")
    def replication_clusters(self) -> Sequence[outputs.GetDatabaseInstancesInstanceReplicationClusterResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreBackupContexts")
    def restore_backup_contexts(self) -> Sequence[outputs.GetDatabaseInstancesInstanceRestoreBackupContextResult]:
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
    def server_ca_certs(self) -> Sequence[outputs.GetDatabaseInstancesInstanceServerCaCertResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmailAddress")
    def service_account_email_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingResult]:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceCloneResult(dict):
    def __init__(__self__, *, allocated_ip_range: _builtins.str, database_names: Sequence[_builtins.str], point_in_time: _builtins.str, preferred_zone: _builtins.str, source_instance_deletion_time: _builtins.str, source_instance_name: _builtins.str, source_project: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseNames")
    def database_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredZone")
    def preferred_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceInstanceDeletionTime")
    def source_instance_deletion_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceInstanceName")
    def source_instance_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceProject")
    def source_project(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceDnsNameResult(dict):
    def __init__(__self__, *, connection_type: _builtins.str, dns_scope: _builtins.str, name: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsScope")
    def dns_scope(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceIpAddressResult(dict):
    def __init__(__self__, *, ip_address: _builtins.str, time_to_retire: _builtins.str, type: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToRetire")
    def time_to_retire(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstancePointInTimeRestoreContextResult(dict):
    def __init__(__self__, *, allocated_ip_range: _builtins.str, datasource: _builtins.str, point_in_time: _builtins.str, preferred_zone: _builtins.str, target_instance: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def datasource(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTime")
    def point_in_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredZone")
    def preferred_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetInstance")
    def target_instance(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceReplicaConfigurationResult(dict):
    def __init__(__self__, *, ca_certificate: _builtins.str, cascadable_replica: _builtins.bool, client_certificate: _builtins.str, client_key: _builtins.str, connect_retry_interval: _builtins.int, dump_file_path: _builtins.str, failover_target: _builtins.bool, master_heartbeat_period: _builtins.int, password: _builtins.str, ssl_cipher: _builtins.str, username: _builtins.str, verify_server_certificate: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cascadableReplica")
    def cascadable_replica(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectRetryInterval")
    def connect_retry_interval(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpFilePath")
    def dump_file_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverTarget")
    def failover_target(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterHeartbeatPeriod")
    def master_heartbeat_period(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCipher")
    def ssl_cipher(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifyServerCertificate")
    def verify_server_certificate(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceReplicationClusterResult(dict):
    def __init__(__self__, *, dr_replica: _builtins.bool, failover_dr_replica_name: _builtins.str, psa_write_endpoint: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="drReplica")
    def dr_replica(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverDrReplicaName")
    def failover_dr_replica_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="psaWriteEndpoint")
    def psa_write_endpoint(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceRestoreBackupContextResult(dict):
    def __init__(__self__, *, backup_run_id: _builtins.int, instance_id: _builtins.str, project: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRunId")
    def backup_run_id(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceServerCaCertResult(dict):
    def __init__(__self__, *, cert: _builtins.str, common_name: _builtins.str, create_time: _builtins.str, expiration_time: _builtins.str, sha1_fingerprint: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonName")
    def common_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sha1Fingerprint")
    def sha1_fingerprint(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingResult(dict):
    def __init__(__self__, *, activation_policy: _builtins.str, active_directory_configs: Sequence[outputs.GetDatabaseInstancesInstanceSettingActiveDirectoryConfigResult], advanced_machine_features: Sequence[outputs.GetDatabaseInstancesInstanceSettingAdvancedMachineFeatureResult], auto_upgrade_enabled: _builtins.bool, availability_type: _builtins.str, backup_configurations: Sequence[outputs.GetDatabaseInstancesInstanceSettingBackupConfigurationResult], collation: _builtins.str, connection_pool_configs: Sequence[outputs.GetDatabaseInstancesInstanceSettingConnectionPoolConfigResult], connector_enforcement: _builtins.str, data_api_access: _builtins.str, data_cache_configs: Sequence[outputs.GetDatabaseInstancesInstanceSettingDataCacheConfigResult], data_disk_provisioned_iops: _builtins.int, data_disk_provisioned_throughput: _builtins.int, database_flags: Sequence[outputs.GetDatabaseInstancesInstanceSettingDatabaseFlagResult], deletion_protection_enabled: _builtins.bool, deny_maintenance_periods: Sequence[outputs.GetDatabaseInstancesInstanceSettingDenyMaintenancePeriodResult], disk_autoresize: _builtins.bool, disk_autoresize_limit: _builtins.int, disk_size: _builtins.int, disk_type: _builtins.str, edition: _builtins.str, effective_availability_type: _builtins.str, enable_dataplex_integration: _builtins.bool, enable_google_ml_integration: _builtins.bool, final_backup_configs: Sequence[outputs.GetDatabaseInstancesInstanceSettingFinalBackupConfigResult], insights_configs: Sequence[outputs.GetDatabaseInstancesInstanceSettingInsightsConfigResult], ip_configurations: Sequence[outputs.GetDatabaseInstancesInstanceSettingIpConfigurationResult], location_preferences: Sequence[outputs.GetDatabaseInstancesInstanceSettingLocationPreferenceResult], maintenance_windows: Sequence[outputs.GetDatabaseInstancesInstanceSettingMaintenanceWindowResult], password_validation_policies: Sequence[outputs.GetDatabaseInstancesInstanceSettingPasswordValidationPolicyResult], pricing_plan: _builtins.str, read_pool_auto_scale_configs: Sequence[outputs.GetDatabaseInstancesInstanceSettingReadPoolAutoScaleConfigResult], retain_backups_on_delete: _builtins.bool, sql_server_audit_configs: Sequence[outputs.GetDatabaseInstancesInstanceSettingSqlServerAuditConfigResult], tier: _builtins.str, time_zone: _builtins.str, user_labels: Mapping[str, _builtins.str], version: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationPolicy")
    def activation_policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConfigs")
    def active_directory_configs(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingActiveDirectoryConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedMachineFeatures")
    def advanced_machine_features(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingAdvancedMachineFeatureResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpgradeEnabled")
    def auto_upgrade_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityType")
    def availability_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupConfigurations")
    def backup_configurations(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingBackupConfigurationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolConfigs")
    def connection_pool_configs(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingConnectionPoolConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorEnforcement")
    def connector_enforcement(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataApiAccess")
    def data_api_access(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCacheConfigs")
    def data_cache_configs(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingDataCacheConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskProvisionedIops")
    def data_disk_provisioned_iops(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDiskProvisionedThroughput")
    def data_disk_provisioned_throughput(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFlags")
    def database_flags(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingDatabaseFlagResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denyMaintenancePeriods")
    def deny_maintenance_periods(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingDenyMaintenancePeriodResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskAutoresize")
    def disk_autoresize(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskAutoresizeLimit")
    def disk_autoresize_limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAvailabilityType")
    def effective_availability_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDataplexIntegration")
    def enable_dataplex_integration(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGoogleMlIntegration")
    def enable_google_ml_integration(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalBackupConfigs")
    def final_backup_configs(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingFinalBackupConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightsConfigs")
    def insights_configs(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingInsightsConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingIpConfigurationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="locationPreferences")
    def location_preferences(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingLocationPreferenceResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingMaintenanceWindowResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordValidationPolicies")
    def password_validation_policies(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingPasswordValidationPolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricingPlan")
    def pricing_plan(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readPoolAutoScaleConfigs")
    def read_pool_auto_scale_configs(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingReadPoolAutoScaleConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainBackupsOnDelete")
    def retain_backups_on_delete(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerAuditConfigs")
    def sql_server_audit_configs(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingSqlServerAuditConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userLabels")
    def user_labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingActiveDirectoryConfigResult(dict):
    def __init__(__self__, *, domain: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingAdvancedMachineFeatureResult(dict):
    def __init__(__self__, *, threads_per_core: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadsPerCore")
    def threads_per_core(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingBackupConfigurationResult(dict):
    def __init__(__self__, *, backup_retention_settings: Sequence[outputs.GetDatabaseInstancesInstanceSettingBackupConfigurationBackupRetentionSettingResult], backup_tier: _builtins.str, binary_log_enabled: _builtins.bool, enabled: _builtins.bool, location: _builtins.str, point_in_time_recovery_enabled: _builtins.bool, start_time: _builtins.str, transaction_log_retention_days: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionSettings")
    def backup_retention_settings(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingBackupConfigurationBackupRetentionSettingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupTier")
    def backup_tier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryLogEnabled")
    def binary_log_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecoveryEnabled")
    def point_in_time_recovery_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionLogRetentionDays")
    def transaction_log_retention_days(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingBackupConfigurationBackupRetentionSettingResult(dict):
    def __init__(__self__, *, retained_backups: _builtins.int, retention_unit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainedBackups")
    def retained_backups(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionUnit")
    def retention_unit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingConnectionPoolConfigResult(dict):
    def __init__(__self__, *, connection_pooling_enabled: _builtins.bool, flags: Sequence[outputs.GetDatabaseInstancesInstanceSettingConnectionPoolConfigFlagResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolingEnabled")
    def connection_pooling_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flags(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingConnectionPoolConfigFlagResult]:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingConnectionPoolConfigFlagResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingDataCacheConfigResult(dict):
    def __init__(__self__, *, data_cache_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCacheEnabled")
    def data_cache_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingDatabaseFlagResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingDenyMaintenancePeriodResult(dict):
    def __init__(__self__, *, end_date: _builtins.str, start_date: _builtins.str, time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingFinalBackupConfigResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool, retention_days: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingInsightsConfigResult(dict):
    def __init__(__self__, *, enhanced_query_insights_enabled: _builtins.bool, query_insights_enabled: _builtins.bool, query_plans_per_minute: _builtins.int, query_string_length: _builtins.int, record_application_tags: _builtins.bool, record_client_address: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedQueryInsightsEnabled")
    def enhanced_query_insights_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryInsightsEnabled")
    def query_insights_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryPlansPerMinute")
    def query_plans_per_minute(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringLength")
    def query_string_length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordApplicationTags")
    def record_application_tags(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordClientAddress")
    def record_client_address(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingIpConfigurationResult(dict):
    def __init__(__self__, *, allocated_ip_range: _builtins.str, authorized_networks: Sequence[outputs.GetDatabaseInstancesInstanceSettingIpConfigurationAuthorizedNetworkResult], custom_subject_alternative_names: Sequence[_builtins.str], enable_private_path_for_google_cloud_services: _builtins.bool, ipv4_enabled: _builtins.bool, private_network: _builtins.str, psc_configs: Sequence[outputs.GetDatabaseInstancesInstanceSettingIpConfigurationPscConfigResult], server_ca_mode: _builtins.str, server_ca_pool: _builtins.str, ssl_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedIpRange")
    def allocated_ip_range(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedNetworks")
    def authorized_networks(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingIpConfigurationAuthorizedNetworkResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customSubjectAlternativeNames")
    def custom_subject_alternative_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivatePathForGoogleCloudServices")
    def enable_private_path_for_google_cloud_services(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Enabled")
    def ipv4_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateNetwork")
    def private_network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscConfigs")
    def psc_configs(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingIpConfigurationPscConfigResult]:
        
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
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingIpConfigurationAuthorizedNetworkResult(dict):
    def __init__(__self__, *, expiration_time: _builtins.str, name: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingIpConfigurationPscConfigResult(dict):
    def __init__(__self__, *, allowed_consumer_projects: Sequence[_builtins.str], network_attachment_uri: _builtins.str, psc_auto_connections: Sequence[outputs.GetDatabaseInstancesInstanceSettingIpConfigurationPscConfigPscAutoConnectionResult], psc_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedConsumerProjects")
    def allowed_consumer_projects(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAttachmentUri")
    def network_attachment_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscAutoConnections")
    def psc_auto_connections(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingIpConfigurationPscConfigPscAutoConnectionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscEnabled")
    def psc_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingIpConfigurationPscConfigPscAutoConnectionResult(dict):
    def __init__(__self__, *, consumer_network: _builtins.str, consumer_network_status: _builtins.str, consumer_service_project_id: _builtins.str, ip_address: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerNetwork")
    def consumer_network(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerNetworkStatus")
    def consumer_network_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerServiceProjectId")
    def consumer_service_project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingLocationPreferenceResult(dict):
    def __init__(__self__, *, follow_gae_application: _builtins.str, secondary_zone: _builtins.str, zone: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="followGaeApplication")
    def follow_gae_application(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryZone")
    def secondary_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingMaintenanceWindowResult(dict):
    def __init__(__self__, *, day: _builtins.int, hour: _builtins.int, update_track: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTrack")
    def update_track(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingPasswordValidationPolicyResult(dict):
    def __init__(__self__, *, complexity: _builtins.str, disallow_username_substring: _builtins.bool, enable_password_policy: _builtins.bool, min_length: _builtins.int, password_change_interval: _builtins.str, reuse_interval: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def complexity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disallowUsernameSubstring")
    def disallow_username_substring(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePasswordPolicy")
    def enable_password_policy(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minLength")
    def min_length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordChangeInterval")
    def password_change_interval(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reuseInterval")
    def reuse_interval(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingReadPoolAutoScaleConfigResult(dict):
    def __init__(__self__, *, disable_scale_in: _builtins.bool, enabled: _builtins.bool, max_node_count: _builtins.int, min_node_count: _builtins.int, scale_in_cooldown_seconds: _builtins.int, scale_out_cooldown_seconds: _builtins.int, target_metrics: Sequence[outputs.GetDatabaseInstancesInstanceSettingReadPoolAutoScaleConfigTargetMetricResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableScaleIn")
    def disable_scale_in(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleInCooldownSeconds")
    def scale_in_cooldown_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleOutCooldownSeconds")
    def scale_out_cooldown_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetMetrics")
    def target_metrics(self) -> Sequence[outputs.GetDatabaseInstancesInstanceSettingReadPoolAutoScaleConfigTargetMetricResult]:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingReadPoolAutoScaleConfigTargetMetricResult(dict):
    def __init__(__self__, *, metric: _builtins.str, target_value: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metric(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetDatabaseInstancesInstanceSettingSqlServerAuditConfigResult(dict):
    def __init__(__self__, *, bucket: _builtins.str, retention_interval: _builtins.str, upload_interval: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionInterval")
    def retention_interval(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadInterval")
    def upload_interval(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetDatabasesDatabaseResult(dict):
    def __init__(__self__, *, charset: _builtins.str, collation: _builtins.str, deletion_policy: _builtins.str, instance: _builtins.str, name: _builtins.str, project: _builtins.str, self_link: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def charset(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetTiersTierResult(dict):
    def __init__(__self__, *, disk_quota: _builtins.int, ram: _builtins.int, regions: Sequence[_builtins.str], tier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskQuota")
    def disk_quota(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ram(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        
        ...
    


