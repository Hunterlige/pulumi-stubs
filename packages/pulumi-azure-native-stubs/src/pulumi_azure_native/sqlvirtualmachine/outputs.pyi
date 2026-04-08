import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AADAuthenticationSettingsResponse",
    "AdditionalFeaturesServerConfigurationsResponse",
    "AgConfigurationResponse",
    "AgReplicaResponse",
    "AssessmentSettingsResponse",
    "AutoBackupSettingsResponse",
    "AutoPatchingSettingsResponse",
    "KeyVaultCredentialSettingsResponse",
    "LoadBalancerConfigurationResponse",
    "MultiSubnetIpConfigurationResponse",
    "PrivateIPAddressResponse",
    "ResourceIdentityResponse",
    "SQLInstanceSettingsResponse",
    "SQLStorageSettingsResponse",
    "SQLTempDbSettingsResponse",
    "ScheduleResponse",
    "ServerConfigurationsManagementSettingsResponse",
    "SqlConnectivityUpdateSettingsResponse",
    "SqlStorageUpdateSettingsResponse",
    "SqlWorkloadTypeUpdateSettingsResponse",
    "StorageConfigurationSettingsResponse",
    "SystemDataResponse",
    "TroubleshootingAdditionalPropertiesResponse",
    "TroubleshootingStatusResponse",
    "UnhealthyReplicaInfoResponse",
    "VirtualMachineIdentityResponse",
    "WsfcDomainCredentialsResponse",
    "WsfcDomainProfileResponse",
]

@pulumi.output_type
class AADAuthenticationSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AdditionalFeaturesServerConfigurationsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, is_r_services_enabled: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isRServicesEnabled")
    def is_r_services_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AgConfigurationResponse(dict):
    def __init__(
        __self__, *, replicas: Optional[Sequence[outputs.AgReplicaResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[Sequence[outputs.AgReplicaResponse]]: ...

@pulumi.output_type
class AgReplicaResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        commit: Optional[_builtins.str] = ...,
        failover: Optional[_builtins.str] = ...,
        readable_secondary: Optional[_builtins.str] = ...,
        role: Optional[_builtins.str] = ...,
        sql_virtual_machine_instance_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def failover(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="readableSecondary")
    def readable_secondary(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sqlVirtualMachineInstanceId")
    def sql_virtual_machine_instance_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssessmentSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable: Optional[_builtins.bool] = ...,
        run_immediately: Optional[_builtins.bool] = ...,
        schedule: Optional[outputs.ScheduleResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="runImmediately")
    def run_immediately(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[outputs.ScheduleResponse]: ...

@pulumi.output_type
class AutoBackupSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backup_schedule_type: Optional[_builtins.str] = ...,
        backup_system_dbs: Optional[_builtins.bool] = ...,
        days_of_week: Optional[Sequence[_builtins.str]] = ...,
        enable: Optional[_builtins.bool] = ...,
        enable_encryption: Optional[_builtins.bool] = ...,
        full_backup_frequency: Optional[_builtins.str] = ...,
        full_backup_start_time: Optional[_builtins.int] = ...,
        full_backup_window_hours: Optional[_builtins.int] = ...,
        log_backup_frequency: Optional[_builtins.int] = ...,
        retention_period: Optional[_builtins.int] = ...,
        storage_account_url: Optional[_builtins.str] = ...,
        storage_container_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupScheduleType")
    def backup_schedule_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupSystemDbs")
    def backup_system_dbs(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableEncryption")
    def enable_encryption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="fullBackupFrequency")
    def full_backup_frequency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fullBackupStartTime")
    def full_backup_start_time(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="fullBackupWindowHours")
    def full_backup_window_hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="logBackupFrequency")
    def log_backup_frequency(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountUrl")
    def storage_account_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageContainerName")
    def storage_container_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutoPatchingSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_vm_patch: Optional[_builtins.str] = ...,
        day_of_week: Optional[_builtins.str] = ...,
        enable: Optional[_builtins.bool] = ...,
        maintenance_window_duration: Optional[_builtins.int] = ...,
        maintenance_window_starting_hour: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalVmPatch")
    def additional_vm_patch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindowDuration")
    def maintenance_window_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindowStartingHour")
    def maintenance_window_starting_hour(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class KeyVaultCredentialSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_key_vault_url: Optional[_builtins.str] = ...,
        credential_name: Optional[_builtins.str] = ...,
        enable: Optional[_builtins.bool] = ...,
        service_principal_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureKeyVaultUrl")
    def azure_key_vault_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="credentialName")
    def credential_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="servicePrincipalName")
    def service_principal_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LoadBalancerConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        load_balancer_resource_id: Optional[_builtins.str] = ...,
        private_ip_address: Optional[outputs.PrivateIPAddressResponse] = ...,
        probe_port: Optional[_builtins.int] = ...,
        public_ip_address_resource_id: Optional[_builtins.str] = ...,
        sql_virtual_machine_instances: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancerResourceId")
    def load_balancer_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[outputs.PrivateIPAddressResponse]: ...
    @_builtins.property
    @pulumi.getter(name="probePort")
    def probe_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="publicIpAddressResourceId")
    def public_ip_address_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sqlVirtualMachineInstances")
    def sql_virtual_machine_instances(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class MultiSubnetIpConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_ip_address: outputs.PrivateIPAddressResponse,
        sql_virtual_machine_instance: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> outputs.PrivateIPAddressResponse: ...
    @_builtins.property
    @pulumi.getter(name="sqlVirtualMachineInstance")
    def sql_virtual_machine_instance(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateIPAddressResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ip_address: Optional[_builtins.str] = ...,
        subnet_resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetResourceId")
    def subnet_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SQLInstanceSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        collation: Optional[_builtins.str] = ...,
        is_ifi_enabled: Optional[_builtins.bool] = ...,
        is_lpim_enabled: Optional[_builtins.bool] = ...,
        is_optimize_for_ad_hoc_workloads_enabled: Optional[_builtins.bool] = ...,
        max_dop: Optional[_builtins.int] = ...,
        max_server_memory_mb: Optional[_builtins.int] = ...,
        min_server_memory_mb: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isIfiEnabled")
    def is_ifi_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isLpimEnabled")
    def is_lpim_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isOptimizeForAdHocWorkloadsEnabled")
    def is_optimize_for_ad_hoc_workloads_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="maxDop")
    def max_dop(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxServerMemoryMB")
    def max_server_memory_mb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minServerMemoryMB")
    def min_server_memory_mb(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SQLStorageSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_file_path: Optional[_builtins.str] = ...,
        luns: Optional[Sequence[_builtins.int]] = ...,
        use_storage_pool: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultFilePath")
    def default_file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def luns(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="useStoragePool")
    def use_storage_pool(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class SQLTempDbSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_file_count: Optional[_builtins.int] = ...,
        data_file_size: Optional[_builtins.int] = ...,
        data_growth: Optional[_builtins.int] = ...,
        default_file_path: Optional[_builtins.str] = ...,
        log_file_size: Optional[_builtins.int] = ...,
        log_growth: Optional[_builtins.int] = ...,
        luns: Optional[Sequence[_builtins.int]] = ...,
        persist_folder: Optional[_builtins.bool] = ...,
        persist_folder_path: Optional[_builtins.str] = ...,
        use_storage_pool: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataFileCount")
    def data_file_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dataFileSize")
    def data_file_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dataGrowth")
    def data_growth(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="defaultFilePath")
    def default_file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logFileSize")
    def log_file_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="logGrowth")
    def log_growth(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def luns(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="persistFolder")
    def persist_folder(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="persistFolderPath")
    def persist_folder_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useStoragePool")
    def use_storage_pool(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        day_of_week: Optional[_builtins.str] = ...,
        enable: Optional[_builtins.bool] = ...,
        monthly_occurrence: Optional[_builtins.int] = ...,
        start_time: Optional[_builtins.str] = ...,
        weekly_interval: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="monthlyOccurrence")
    def monthly_occurrence(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeklyInterval")
    def weekly_interval(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ServerConfigurationsManagementSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_features_server_configurations: Optional[
            outputs.AdditionalFeaturesServerConfigurationsResponse
        ] = ...,
        azure_ad_authentication_settings: Optional[
            outputs.AADAuthenticationSettingsResponse
        ] = ...,
        sql_connectivity_update_settings: Optional[
            outputs.SqlConnectivityUpdateSettingsResponse
        ] = ...,
        sql_instance_settings: Optional[outputs.SQLInstanceSettingsResponse] = ...,
        sql_storage_update_settings: Optional[
            outputs.SqlStorageUpdateSettingsResponse
        ] = ...,
        sql_workload_type_update_settings: Optional[
            outputs.SqlWorkloadTypeUpdateSettingsResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalFeaturesServerConfigurations")
    def additional_features_server_configurations(
        self,
    ) -> Optional[outputs.AdditionalFeaturesServerConfigurationsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureAdAuthenticationSettings")
    def azure_ad_authentication_settings(
        self,
    ) -> Optional[outputs.AADAuthenticationSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sqlConnectivityUpdateSettings")
    def sql_connectivity_update_settings(
        self,
    ) -> Optional[outputs.SqlConnectivityUpdateSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sqlInstanceSettings")
    def sql_instance_settings(
        self,
    ) -> Optional[outputs.SQLInstanceSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sqlStorageUpdateSettings")
    def sql_storage_update_settings(
        self,
    ) -> Optional[outputs.SqlStorageUpdateSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sqlWorkloadTypeUpdateSettings")
    def sql_workload_type_update_settings(
        self,
    ) -> Optional[outputs.SqlWorkloadTypeUpdateSettingsResponse]: ...

@pulumi.output_type
class SqlConnectivityUpdateSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connectivity_type: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectivityType")
    def connectivity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SqlStorageUpdateSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_configuration_type: Optional[_builtins.str] = ...,
        disk_count: Optional[_builtins.int] = ...,
        starting_device_id: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskConfigurationType")
    def disk_configuration_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskCount")
    def disk_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="startingDeviceId")
    def starting_device_id(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SqlWorkloadTypeUpdateSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, sql_workload_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sqlWorkloadType")
    def sql_workload_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageConfigurationSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk_configuration_type: Optional[_builtins.str] = ...,
        sql_data_settings: Optional[outputs.SQLStorageSettingsResponse] = ...,
        sql_log_settings: Optional[outputs.SQLStorageSettingsResponse] = ...,
        sql_system_db_on_data_disk: Optional[_builtins.bool] = ...,
        sql_temp_db_settings: Optional[outputs.SQLTempDbSettingsResponse] = ...,
        storage_workload_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskConfigurationType")
    def disk_configuration_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sqlDataSettings")
    def sql_data_settings(self) -> Optional[outputs.SQLStorageSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sqlLogSettings")
    def sql_log_settings(self) -> Optional[outputs.SQLStorageSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sqlSystemDbOnDataDisk")
    def sql_system_db_on_data_disk(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sqlTempDbSettings")
    def sql_temp_db_settings(self) -> Optional[outputs.SQLTempDbSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageWorkloadType")
    def storage_workload_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TroubleshootingAdditionalPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        unhealthy_replica_info: Optional[outputs.UnhealthyReplicaInfoResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyReplicaInfo")
    def unhealthy_replica_info(
        self,
    ) -> Optional[outputs.UnhealthyReplicaInfoResponse]: ...

@pulumi.output_type
class TroubleshootingStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_time_utc: _builtins.str,
        last_trigger_time_utc: _builtins.str,
        properties: outputs.TroubleshootingAdditionalPropertiesResponse,
        root_cause: _builtins.str,
        start_time_utc: _builtins.str,
        troubleshooting_scenario: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTimeUtc")
    def end_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastTriggerTimeUtc")
    def last_trigger_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.TroubleshootingAdditionalPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="rootCause")
    def root_cause(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTimeUtc")
    def start_time_utc(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="troubleshootingScenario")
    def troubleshooting_scenario(self) -> _builtins.str: ...

@pulumi.output_type
class UnhealthyReplicaInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, availability_group_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityGroupName")
    def availability_group_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualMachineIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_id: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WsfcDomainCredentialsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_bootstrap_account_password: Optional[_builtins.str] = ...,
        cluster_operator_account_password: Optional[_builtins.str] = ...,
        sql_service_account_password: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterBootstrapAccountPassword")
    def cluster_bootstrap_account_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterOperatorAccountPassword")
    def cluster_operator_account_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sqlServiceAccountPassword")
    def sql_service_account_password(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WsfcDomainProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_bootstrap_account: Optional[_builtins.str] = ...,
        cluster_operator_account: Optional[_builtins.str] = ...,
        cluster_subnet_type: Optional[_builtins.str] = ...,
        domain_fqdn: Optional[_builtins.str] = ...,
        file_share_witness_path: Optional[_builtins.str] = ...,
        is_sql_service_account_gmsa: Optional[_builtins.bool] = ...,
        ou_path: Optional[_builtins.str] = ...,
        sql_service_account: Optional[_builtins.str] = ...,
        storage_account_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterBootstrapAccount")
    def cluster_bootstrap_account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterOperatorAccount")
    def cluster_operator_account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterSubnetType")
    def cluster_subnet_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainFqdn")
    def domain_fqdn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileShareWitnessPath")
    def file_share_witness_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isSqlServiceAccountGmsa")
    def is_sql_service_account_gmsa(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ouPath")
    def ou_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sqlServiceAccount")
    def sql_service_account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountUrl")
    def storage_account_url(self) -> Optional[_builtins.str]: ...
