import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AutonomousDatabaseProperties",
    "AutonomousDatabasePropertiesApexDetail",
    "AutonomousDatabasePropertiesConnectionString",
    ...,
    ...,
    "AutonomousDatabasePropertiesConnectionUrl",
    "AutonomousDatabasePropertiesCustomerContact",
    "AutonomousDatabasePropertiesLocalStandbyDb",
    ...,
    ...,
    ...,
    "AutonomousDatabaseSourceConfig",
    "CloudExadataInfrastructureProperties",
    ...,
    ...,
    "CloudVmClusterProperties",
    ...,
    "CloudVmClusterPropertiesTimeZone",
    "DbSystemProperties",
    "DbSystemPropertiesDataCollectionOptions",
    "DbSystemPropertiesDbHome",
    "DbSystemPropertiesDbHomeDatabase",
    "DbSystemPropertiesDbHomeDatabaseProperties",
    ...,
    ...,
    ...,
    "DbSystemPropertiesDbSystemOptions",
    "DbSystemPropertiesTimeZone",
    "ExadbVmClusterProperties",
    "ExadbVmClusterPropertiesDataCollectionOptions",
    "ExadbVmClusterPropertiesTimeZone",
    "ExadbVmClusterPropertiesVmFileSystemStorage",
    "ExascaleDbStorageVaultProperties",
    ...,
    "ExascaleDbStorageVaultPropertiesTimeZone",
    "GetAutonomousDatabasePropertyResult",
    "GetAutonomousDatabasePropertyApexDetailResult",
    ...,
    ...,
    ...,
    "GetAutonomousDatabasePropertyConnectionUrlResult",
    "GetAutonomousDatabasePropertyCustomerContactResult",
    "GetAutonomousDatabasePropertyLocalStandbyDbResult",
    ...,
    ...,
    ...,
    "GetAutonomousDatabaseSourceConfigResult",
    "GetAutonomousDatabasesAutonomousDatabaseResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetCloudExadataInfrastructurePropertyResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetCloudVmClusterPropertyResult",
    ...,
    "GetCloudVmClusterPropertyTimeZoneResult",
    "GetCloudVmClustersCloudVmClusterResult",
    "GetCloudVmClustersCloudVmClusterPropertyResult",
    ...,
    ...,
    "GetDbNodesDbNodeResult",
    "GetDbNodesDbNodePropertyResult",
    "GetDbServersDbServerResult",
    "GetDbServersDbServerPropertyResult",
]

@pulumi.output_type
class AutonomousDatabaseProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        db_workload: _builtins.str,
        license_type: _builtins.str,
        actual_used_data_storage_size_tb: Optional[_builtins.float] = ...,
        allocated_storage_size_tb: Optional[_builtins.float] = ...,
        apex_details: Optional[
            Sequence[outputs.AutonomousDatabasePropertiesApexDetail]
        ] = ...,
        are_primary_allowlisted_ips_used: Optional[_builtins.bool] = ...,
        autonomous_container_database_id: Optional[_builtins.str] = ...,
        available_upgrade_versions: Optional[Sequence[_builtins.str]] = ...,
        backup_retention_period_days: Optional[_builtins.int] = ...,
        character_set: Optional[_builtins.str] = ...,
        compute_count: Optional[_builtins.float] = ...,
        connection_strings: Optional[
            Sequence[outputs.AutonomousDatabasePropertiesConnectionString]
        ] = ...,
        connection_urls: Optional[
            Sequence[outputs.AutonomousDatabasePropertiesConnectionUrl]
        ] = ...,
        cpu_core_count: Optional[_builtins.int] = ...,
        customer_contacts: Optional[
            Sequence[outputs.AutonomousDatabasePropertiesCustomerContact]
        ] = ...,
        data_safe_state: Optional[_builtins.str] = ...,
        data_storage_size_gb: Optional[_builtins.int] = ...,
        data_storage_size_tb: Optional[_builtins.int] = ...,
        database_management_state: Optional[_builtins.str] = ...,
        db_edition: Optional[_builtins.str] = ...,
        db_version: Optional[_builtins.str] = ...,
        failed_data_recovery_duration: Optional[_builtins.str] = ...,
        is_auto_scaling_enabled: Optional[_builtins.bool] = ...,
        is_local_data_guard_enabled: Optional[_builtins.bool] = ...,
        is_storage_auto_scaling_enabled: Optional[_builtins.bool] = ...,
        lifecycle_details: Optional[_builtins.str] = ...,
        local_adg_auto_failover_max_data_loss_limit: Optional[_builtins.int] = ...,
        local_disaster_recovery_type: Optional[_builtins.str] = ...,
        local_standby_dbs: Optional[
            Sequence[outputs.AutonomousDatabasePropertiesLocalStandbyDb]
        ] = ...,
        maintenance_begin_time: Optional[_builtins.str] = ...,
        maintenance_end_time: Optional[_builtins.str] = ...,
        maintenance_schedule_type: Optional[_builtins.str] = ...,
        memory_per_oracle_compute_unit_gbs: Optional[_builtins.int] = ...,
        memory_table_gbs: Optional[_builtins.int] = ...,
        mtls_connection_required: Optional[_builtins.bool] = ...,
        n_character_set: Optional[_builtins.str] = ...,
        next_long_term_backup_time: Optional[_builtins.str] = ...,
        oci_url: Optional[_builtins.str] = ...,
        ocid: Optional[_builtins.str] = ...,
        open_mode: Optional[_builtins.str] = ...,
        operations_insights_state: Optional[_builtins.str] = ...,
        peer_db_ids: Optional[Sequence[_builtins.str]] = ...,
        permission_level: Optional[_builtins.str] = ...,
        private_endpoint: Optional[_builtins.str] = ...,
        private_endpoint_ip: Optional[_builtins.str] = ...,
        private_endpoint_label: Optional[_builtins.str] = ...,
        refreshable_mode: Optional[_builtins.str] = ...,
        refreshable_state: Optional[_builtins.str] = ...,
        role: Optional[_builtins.str] = ...,
        scheduled_operation_details: Optional[
            Sequence[outputs.AutonomousDatabasePropertiesScheduledOperationDetail]
        ] = ...,
        secret_id: Optional[_builtins.str] = ...,
        sql_web_developer_url: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        supported_clone_regions: Optional[Sequence[_builtins.str]] = ...,
        total_auto_backup_storage_size_gbs: Optional[_builtins.float] = ...,
        used_data_storage_size_tbs: Optional[_builtins.int] = ...,
        vault_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbWorkload")
    def db_workload(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="actualUsedDataStorageSizeTb")
    def actual_used_data_storage_size_tb(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorageSizeTb")
    def allocated_storage_size_tb(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="apexDetails")
    def apex_details(
        self,
    ) -> Optional[Sequence[outputs.AutonomousDatabasePropertiesApexDetail]]: ...
    @_builtins.property
    @pulumi.getter(name="arePrimaryAllowlistedIpsUsed")
    def are_primary_allowlisted_ips_used(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="autonomousContainerDatabaseId")
    def autonomous_container_database_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availableUpgradeVersions")
    def available_upgrade_versions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionPeriodDays")
    def backup_retention_period_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="characterSet")
    def character_set(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="connectionStrings")
    def connection_strings(
        self,
    ) -> Optional[Sequence[outputs.AutonomousDatabasePropertiesConnectionString]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionUrls")
    def connection_urls(
        self,
    ) -> Optional[Sequence[outputs.AutonomousDatabasePropertiesConnectionUrl]]: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="customerContacts")
    def customer_contacts(
        self,
    ) -> Optional[Sequence[outputs.AutonomousDatabasePropertiesCustomerContact]]: ...
    @_builtins.property
    @pulumi.getter(name="dataSafeState")
    def data_safe_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeGb")
    def data_storage_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeTb")
    def data_storage_size_tb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="databaseManagementState")
    def database_management_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbEdition")
    def db_edition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failedDataRecoveryDuration")
    def failed_data_recovery_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isAutoScalingEnabled")
    def is_auto_scaling_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isLocalDataGuardEnabled")
    def is_local_data_guard_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isStorageAutoScalingEnabled")
    def is_storage_auto_scaling_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localAdgAutoFailoverMaxDataLossLimit")
    def local_adg_auto_failover_max_data_loss_limit(
        self,
    ) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="localDisasterRecoveryType")
    def local_disaster_recovery_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localStandbyDbs")
    def local_standby_dbs(
        self,
    ) -> Optional[Sequence[outputs.AutonomousDatabasePropertiesLocalStandbyDb]]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceBeginTime")
    def maintenance_begin_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceEndTime")
    def maintenance_end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceScheduleType")
    def maintenance_schedule_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryPerOracleComputeUnitGbs")
    def memory_per_oracle_compute_unit_gbs(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="memoryTableGbs")
    def memory_table_gbs(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="mtlsConnectionRequired")
    def mtls_connection_required(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="nCharacterSet")
    def n_character_set(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextLongTermBackupTime")
    def next_long_term_backup_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="openMode")
    def open_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="operationsInsightsState")
    def operations_insights_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peerDbIds")
    def peer_db_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="permissionLevel")
    def permission_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointIp")
    def private_endpoint_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointLabel")
    def private_endpoint_label(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshableMode")
    def refreshable_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshableState")
    def refreshable_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduledOperationDetails")
    def scheduled_operation_details(
        self,
    ) -> Optional[
        Sequence[outputs.AutonomousDatabasePropertiesScheduledOperationDetail]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sqlWebDeveloperUrl")
    def sql_web_developer_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedCloneRegions")
    def supported_clone_regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="totalAutoBackupStorageSizeGbs")
    def total_auto_backup_storage_size_gbs(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="usedDataStorageSizeTbs")
    def used_data_storage_size_tbs(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutonomousDatabasePropertiesApexDetail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        apex_version: Optional[_builtins.str] = ...,
        ords_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apexVersion")
    def apex_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ordsVersion")
    def ords_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutonomousDatabasePropertiesConnectionString(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        all_connection_strings: Optional[
            Sequence[
                outputs.AutonomousDatabasePropertiesConnectionStringAllConnectionString
            ]
        ] = ...,
        dedicated: Optional[_builtins.str] = ...,
        high: Optional[_builtins.str] = ...,
        low: Optional[_builtins.str] = ...,
        medium: Optional[_builtins.str] = ...,
        profiles: Optional[
            Sequence[outputs.AutonomousDatabasePropertiesConnectionStringProfile]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allConnectionStrings")
    def all_connection_strings(
        self,
    ) -> Optional[
        Sequence[
            outputs.AutonomousDatabasePropertiesConnectionStringAllConnectionString
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def dedicated(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def high(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def low(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def profiles(
        self,
    ) -> Optional[
        Sequence[outputs.AutonomousDatabasePropertiesConnectionStringProfile]
    ]: ...

@pulumi.output_type
class AutonomousDatabasePropertiesConnectionStringAllConnectionString(dict):
    def __init__(
        __self__,
        *,
        high: Optional[_builtins.str] = ...,
        low: Optional[_builtins.str] = ...,
        medium: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def high(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def low(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutonomousDatabasePropertiesConnectionStringProfile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consumer_group: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        host_format: Optional[_builtins.str] = ...,
        is_regional: Optional[_builtins.bool] = ...,
        protocol: Optional[_builtins.str] = ...,
        session_mode: Optional[_builtins.str] = ...,
        syntax_format: Optional[_builtins.str] = ...,
        tls_authentication: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostFormat")
    def host_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isRegional")
    def is_regional(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionMode")
    def session_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syntaxFormat")
    def syntax_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tlsAuthentication")
    def tls_authentication(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutonomousDatabasePropertiesConnectionUrl(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        apex_uri: Optional[_builtins.str] = ...,
        database_transforms_uri: Optional[_builtins.str] = ...,
        graph_studio_uri: Optional[_builtins.str] = ...,
        machine_learning_notebook_uri: Optional[_builtins.str] = ...,
        machine_learning_user_management_uri: Optional[_builtins.str] = ...,
        mongo_db_uri: Optional[_builtins.str] = ...,
        ords_uri: Optional[_builtins.str] = ...,
        sql_dev_web_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apexUri")
    def apex_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databaseTransformsUri")
    def database_transforms_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="graphStudioUri")
    def graph_studio_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineLearningNotebookUri")
    def machine_learning_notebook_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineLearningUserManagementUri")
    def machine_learning_user_management_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mongoDbUri")
    def mongo_db_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ordsUri")
    def ords_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sqlDevWebUri")
    def sql_dev_web_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutonomousDatabasePropertiesCustomerContact(dict):
    def __init__(__self__, *, email: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...

@pulumi.output_type
class AutonomousDatabasePropertiesLocalStandbyDb(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_guard_role_changed_time: Optional[_builtins.str] = ...,
        disaster_recovery_role_changed_time: Optional[_builtins.str] = ...,
        lag_time_duration: Optional[_builtins.str] = ...,
        lifecycle_details: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataGuardRoleChangedTime")
    def data_guard_role_changed_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disasterRecoveryRoleChangedTime")
    def disaster_recovery_role_changed_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lagTimeDuration")
    def lag_time_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AutonomousDatabasePropertiesScheduledOperationDetail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        day_of_week: Optional[_builtins.str] = ...,
        start_times: Optional[
            Sequence[
                outputs.AutonomousDatabasePropertiesScheduledOperationDetailStartTime
            ]
        ] = ...,
        stop_times: Optional[
            Sequence[
                outputs.AutonomousDatabasePropertiesScheduledOperationDetailStopTime
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> Optional[
        Sequence[outputs.AutonomousDatabasePropertiesScheduledOperationDetailStartTime]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="stopTimes")
    def stop_times(
        self,
    ) -> Optional[
        Sequence[outputs.AutonomousDatabasePropertiesScheduledOperationDetailStopTime]
    ]: ...

@pulumi.output_type
class AutonomousDatabasePropertiesScheduledOperationDetailStartTime(dict):
    def __init__(
        __self__,
        *,
        hours: Optional[_builtins.int] = ...,
        minutes: Optional[_builtins.int] = ...,
        nanos: Optional[_builtins.int] = ...,
        seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AutonomousDatabasePropertiesScheduledOperationDetailStopTime(dict):
    def __init__(
        __self__,
        *,
        hours: Optional[_builtins.int] = ...,
        minutes: Optional[_builtins.int] = ...,
        nanos: Optional[_builtins.int] = ...,
        seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AutonomousDatabaseSourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        automatic_backups_replication_enabled: Optional[_builtins.bool] = ...,
        autonomous_database: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticBackupsReplicationEnabled")
    def automatic_backups_replication_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="autonomousDatabase")
    def autonomous_database(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CloudExadataInfrastructureProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        shape: _builtins.str,
        activated_storage_count: Optional[_builtins.int] = ...,
        additional_storage_count: Optional[_builtins.int] = ...,
        available_storage_size_gb: Optional[_builtins.int] = ...,
        compute_count: Optional[_builtins.int] = ...,
        cpu_count: Optional[_builtins.int] = ...,
        customer_contacts: Optional[
            Sequence[outputs.CloudExadataInfrastructurePropertiesCustomerContact]
        ] = ...,
        data_storage_size_tb: Optional[_builtins.float] = ...,
        db_node_storage_size_gb: Optional[_builtins.int] = ...,
        db_server_version: Optional[_builtins.str] = ...,
        maintenance_window: Optional[
            outputs.CloudExadataInfrastructurePropertiesMaintenanceWindow
        ] = ...,
        max_cpu_count: Optional[_builtins.int] = ...,
        max_data_storage_tb: Optional[_builtins.float] = ...,
        max_db_node_storage_size_gb: Optional[_builtins.int] = ...,
        max_memory_gb: Optional[_builtins.int] = ...,
        memory_size_gb: Optional[_builtins.int] = ...,
        monthly_db_server_version: Optional[_builtins.str] = ...,
        monthly_storage_server_version: Optional[_builtins.str] = ...,
        next_maintenance_run_id: Optional[_builtins.str] = ...,
        next_maintenance_run_time: Optional[_builtins.str] = ...,
        next_security_maintenance_run_time: Optional[_builtins.str] = ...,
        oci_url: Optional[_builtins.str] = ...,
        ocid: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        storage_count: Optional[_builtins.int] = ...,
        storage_server_version: Optional[_builtins.str] = ...,
        total_storage_size_gb: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="activatedStorageCount")
    def activated_storage_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="additionalStorageCount")
    def additional_storage_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="availableStorageSizeGb")
    def available_storage_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="customerContacts")
    def customer_contacts(
        self,
    ) -> Optional[
        Sequence[outputs.CloudExadataInfrastructurePropertiesCustomerContact]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeTb")
    def data_storage_size_tb(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeGb")
    def db_node_storage_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dbServerVersion")
    def db_server_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> Optional[outputs.CloudExadataInfrastructurePropertiesMaintenanceWindow]: ...
    @_builtins.property
    @pulumi.getter(name="maxCpuCount")
    def max_cpu_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxDataStorageTb")
    def max_data_storage_tb(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="maxDbNodeStorageSizeGb")
    def max_db_node_storage_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxMemoryGb")
    def max_memory_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="monthlyDbServerVersion")
    def monthly_db_server_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="monthlyStorageServerVersion")
    def monthly_storage_server_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextMaintenanceRunId")
    def next_maintenance_run_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextMaintenanceRunTime")
    def next_maintenance_run_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextSecurityMaintenanceRunTime")
    def next_security_maintenance_run_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageCount")
    def storage_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="storageServerVersion")
    def storage_server_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="totalStorageSizeGb")
    def total_storage_size_gb(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CloudExadataInfrastructurePropertiesCustomerContact(dict):
    def __init__(__self__, *, email: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...

@pulumi.output_type
class CloudExadataInfrastructurePropertiesMaintenanceWindow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_action_timeout_mins: Optional[_builtins.int] = ...,
        days_of_weeks: Optional[Sequence[_builtins.str]] = ...,
        hours_of_days: Optional[Sequence[_builtins.int]] = ...,
        is_custom_action_timeout_enabled: Optional[_builtins.bool] = ...,
        lead_time_week: Optional[_builtins.int] = ...,
        months: Optional[Sequence[_builtins.str]] = ...,
        patching_mode: Optional[_builtins.str] = ...,
        preference: Optional[_builtins.str] = ...,
        weeks_of_months: Optional[Sequence[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customActionTimeoutMins")
    def custom_action_timeout_mins(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hoursOfDays")
    def hours_of_days(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="isCustomActionTimeoutEnabled")
    def is_custom_action_timeout_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="leadTimeWeek")
    def lead_time_week(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def months(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="patchingMode")
    def patching_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="weeksOfMonths")
    def weeks_of_months(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class CloudVmClusterProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cpu_core_count: _builtins.int,
        license_type: _builtins.str,
        cluster_name: Optional[_builtins.str] = ...,
        compartment_id: Optional[_builtins.str] = ...,
        data_storage_size_tb: Optional[_builtins.float] = ...,
        db_node_storage_size_gb: Optional[_builtins.int] = ...,
        db_server_ocids: Optional[Sequence[_builtins.str]] = ...,
        diagnostics_data_collection_options: Optional[
            outputs.CloudVmClusterPropertiesDiagnosticsDataCollectionOptions
        ] = ...,
        disk_redundancy: Optional[_builtins.str] = ...,
        dns_listener_ip: Optional[_builtins.str] = ...,
        domain: Optional[_builtins.str] = ...,
        gi_version: Optional[_builtins.str] = ...,
        hostname: Optional[_builtins.str] = ...,
        hostname_prefix: Optional[_builtins.str] = ...,
        local_backup_enabled: Optional[_builtins.bool] = ...,
        memory_size_gb: Optional[_builtins.int] = ...,
        node_count: Optional[_builtins.int] = ...,
        oci_url: Optional[_builtins.str] = ...,
        ocid: Optional[_builtins.str] = ...,
        ocpu_count: Optional[_builtins.float] = ...,
        scan_dns: Optional[_builtins.str] = ...,
        scan_dns_record_id: Optional[_builtins.str] = ...,
        scan_ip_ids: Optional[Sequence[_builtins.str]] = ...,
        scan_listener_port_tcp: Optional[_builtins.int] = ...,
        scan_listener_port_tcp_ssl: Optional[_builtins.int] = ...,
        shape: Optional[_builtins.str] = ...,
        sparse_diskgroup_enabled: Optional[_builtins.bool] = ...,
        ssh_public_keys: Optional[Sequence[_builtins.str]] = ...,
        state: Optional[_builtins.str] = ...,
        storage_size_gb: Optional[_builtins.int] = ...,
        system_version: Optional[_builtins.str] = ...,
        time_zone: Optional[outputs.CloudVmClusterPropertiesTimeZone] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeTb")
    def data_storage_size_tb(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeGb")
    def db_node_storage_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dbServerOcids")
    def db_server_ocids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsDataCollectionOptions")
    def diagnostics_data_collection_options(
        self,
    ) -> Optional[outputs.CloudVmClusterPropertiesDiagnosticsDataCollectionOptions]: ...
    @_builtins.property
    @pulumi.getter(name="diskRedundancy")
    def disk_redundancy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsListenerIp")
    def dns_listener_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="giVersion")
    def gi_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localBackupEnabled")
    def local_backup_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ocpuCount")
    def ocpu_count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="scanDns")
    def scan_dns(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scanDnsRecordId")
    def scan_dns_record_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scanIpIds")
    def scan_ip_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcp")
    def scan_listener_port_tcp(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcpSsl")
    def scan_listener_port_tcp_ssl(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sparseDiskgroupEnabled")
    def sparse_diskgroup_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageSizeGb")
    def storage_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="systemVersion")
    def system_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[outputs.CloudVmClusterPropertiesTimeZone]: ...

@pulumi.output_type
class CloudVmClusterPropertiesDiagnosticsDataCollectionOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        diagnostics_events_enabled: Optional[_builtins.bool] = ...,
        health_monitoring_enabled: Optional[_builtins.bool] = ...,
        incident_logs_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsEventsEnabled")
    def diagnostics_events_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="healthMonitoringEnabled")
    def health_monitoring_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="incidentLogsEnabled")
    def incident_logs_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CloudVmClusterPropertiesTimeZone(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DbSystemProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compute_count: _builtins.int,
        database_edition: _builtins.str,
        initial_data_storage_size_gb: _builtins.int,
        license_model: _builtins.str,
        shape: _builtins.str,
        ssh_public_keys: Sequence[_builtins.str],
        compute_model: Optional[_builtins.str] = ...,
        data_collection_options: Optional[
            outputs.DbSystemPropertiesDataCollectionOptions
        ] = ...,
        data_storage_size_gb: Optional[_builtins.int] = ...,
        db_home: Optional[outputs.DbSystemPropertiesDbHome] = ...,
        db_system_options: Optional[outputs.DbSystemPropertiesDbSystemOptions] = ...,
        domain: Optional[_builtins.str] = ...,
        hostname: Optional[_builtins.str] = ...,
        hostname_prefix: Optional[_builtins.str] = ...,
        lifecycle_state: Optional[_builtins.str] = ...,
        memory_size_gb: Optional[_builtins.int] = ...,
        node_count: Optional[_builtins.int] = ...,
        ocid: Optional[_builtins.str] = ...,
        private_ip: Optional[_builtins.str] = ...,
        reco_storage_size_gb: Optional[_builtins.int] = ...,
        time_zone: Optional[outputs.DbSystemPropertiesTimeZone] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="databaseEdition")
    def database_edition(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="initialDataStorageSizeGb")
    def initial_data_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionOptions")
    def data_collection_options(
        self,
    ) -> Optional[outputs.DbSystemPropertiesDataCollectionOptions]: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeGb")
    def data_storage_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dbHome")
    def db_home(self) -> Optional[outputs.DbSystemPropertiesDbHome]: ...
    @_builtins.property
    @pulumi.getter(name="dbSystemOptions")
    def db_system_options(
        self,
    ) -> Optional[outputs.DbSystemPropertiesDbSystemOptions]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recoStorageSizeGb")
    def reco_storage_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[outputs.DbSystemPropertiesTimeZone]: ...

@pulumi.output_type
class DbSystemPropertiesDataCollectionOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_diagnostics_events_enabled: Optional[_builtins.bool] = ...,
        is_incident_logs_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isDiagnosticsEventsEnabled")
    def is_diagnostics_events_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isIncidentLogsEnabled")
    def is_incident_logs_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DbSystemPropertiesDbHome(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database: outputs.DbSystemPropertiesDbHomeDatabase,
        db_version: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        is_unified_auditing_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> outputs.DbSystemPropertiesDbHomeDatabase: ...
    @_builtins.property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isUnifiedAuditingEnabled")
    def is_unified_auditing_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DbSystemPropertiesDbHomeDatabase(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        admin_password: _builtins.str,
        database_id: _builtins.str,
        character_set: Optional[_builtins.str] = ...,
        create_time: Optional[_builtins.str] = ...,
        db_home_name: Optional[_builtins.str] = ...,
        db_name: Optional[_builtins.str] = ...,
        db_unique_name: Optional[_builtins.str] = ...,
        gcp_oracle_zone: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        ncharacter_set: Optional[_builtins.str] = ...,
        oci_url: Optional[_builtins.str] = ...,
        ops_insights_status: Optional[_builtins.str] = ...,
        properties: Optional[outputs.DbSystemPropertiesDbHomeDatabaseProperties] = ...,
        tde_wallet_password: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="characterSet")
    def character_set(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbHomeName")
    def db_home_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbUniqueName")
    def db_unique_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gcpOracleZone")
    def gcp_oracle_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ncharacterSet")
    def ncharacter_set(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="opsInsightsStatus")
    def ops_insights_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[outputs.DbSystemPropertiesDbHomeDatabaseProperties]: ...
    @_builtins.property
    @pulumi.getter(name="tdeWalletPassword")
    def tde_wallet_password(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DbSystemPropertiesDbHomeDatabaseProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        db_version: _builtins.str,
        database_management_config: Optional[
            outputs.DbSystemPropertiesDbHomeDatabasePropertiesDatabaseManagementConfig
        ] = ...,
        db_backup_config: Optional[
            outputs.DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfig
        ] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseManagementConfig")
    def database_management_config(
        self,
    ) -> Optional[
        outputs.DbSystemPropertiesDbHomeDatabasePropertiesDatabaseManagementConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dbBackupConfig")
    def db_backup_config(
        self,
    ) -> Optional[outputs.DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfig]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DbSystemPropertiesDbHomeDatabasePropertiesDatabaseManagementConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        management_state: Optional[_builtins.str] = ...,
        management_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managementState")
    def management_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managementType")
    def management_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_backup_enabled: Optional[_builtins.bool] = ...,
        auto_full_backup_day: Optional[_builtins.str] = ...,
        auto_full_backup_window: Optional[_builtins.str] = ...,
        auto_incremental_backup_window: Optional[_builtins.str] = ...,
        backup_deletion_policy: Optional[_builtins.str] = ...,
        backup_destination_details: Optional[
            Sequence[
                outputs.DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigBackupDestinationDetail
            ]
        ] = ...,
        retention_period_days: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoBackupEnabled")
    def auto_backup_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="autoFullBackupDay")
    def auto_full_backup_day(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoFullBackupWindow")
    def auto_full_backup_window(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoIncrementalBackupWindow")
    def auto_incremental_backup_window(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupDeletionPolicy")
    def backup_deletion_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupDestinationDetails")
    def backup_destination_details(
        self,
    ) -> Optional[
        Sequence[
            outputs.DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigBackupDestinationDetail
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriodDays")
    def retention_period_days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigBackupDestinationDetail(
    dict
):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DbSystemPropertiesDbSystemOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, storage_management: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageManagement")
    def storage_management(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DbSystemPropertiesTimeZone(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExadbVmClusterProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled_ecpu_count_per_node: _builtins.int,
        exascale_db_storage_vault: _builtins.str,
        grid_image_id: _builtins.str,
        hostname_prefix: _builtins.str,
        node_count: _builtins.int,
        shape_attribute: _builtins.str,
        ssh_public_keys: Sequence[_builtins.str],
        vm_file_system_storage: outputs.ExadbVmClusterPropertiesVmFileSystemStorage,
        additional_ecpu_count_per_node: Optional[_builtins.int] = ...,
        cluster_name: Optional[_builtins.str] = ...,
        data_collection_options: Optional[
            outputs.ExadbVmClusterPropertiesDataCollectionOptions
        ] = ...,
        gi_version: Optional[_builtins.str] = ...,
        hostname: Optional[_builtins.str] = ...,
        license_model: Optional[_builtins.str] = ...,
        lifecycle_state: Optional[_builtins.str] = ...,
        memory_size_gb: Optional[_builtins.int] = ...,
        oci_uri: Optional[_builtins.str] = ...,
        scan_listener_port_tcp: Optional[_builtins.int] = ...,
        time_zone: Optional[outputs.ExadbVmClusterPropertiesTimeZone] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledEcpuCountPerNode")
    def enabled_ecpu_count_per_node(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="exascaleDbStorageVault")
    def exascale_db_storage_vault(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gridImageId")
    def grid_image_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="shapeAttribute")
    def shape_attribute(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmFileSystemStorage")
    def vm_file_system_storage(
        self,
    ) -> outputs.ExadbVmClusterPropertiesVmFileSystemStorage: ...
    @_builtins.property
    @pulumi.getter(name="additionalEcpuCountPerNode")
    def additional_ecpu_count_per_node(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionOptions")
    def data_collection_options(
        self,
    ) -> Optional[outputs.ExadbVmClusterPropertiesDataCollectionOptions]: ...
    @_builtins.property
    @pulumi.getter(name="giVersion")
    def gi_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ociUri")
    def oci_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcp")
    def scan_listener_port_tcp(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[outputs.ExadbVmClusterPropertiesTimeZone]: ...

@pulumi.output_type
class ExadbVmClusterPropertiesDataCollectionOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_diagnostics_events_enabled: Optional[_builtins.bool] = ...,
        is_health_monitoring_enabled: Optional[_builtins.bool] = ...,
        is_incident_logs_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isDiagnosticsEventsEnabled")
    def is_diagnostics_events_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isHealthMonitoringEnabled")
    def is_health_monitoring_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isIncidentLogsEnabled")
    def is_incident_logs_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ExadbVmClusterPropertiesTimeZone(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExadbVmClusterPropertiesVmFileSystemStorage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, size_in_gbs_per_node: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeInGbsPerNode")
    def size_in_gbs_per_node(self) -> _builtins.int: ...

@pulumi.output_type
class ExascaleDbStorageVaultProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exascale_db_storage_details: outputs.ExascaleDbStorageVaultPropertiesExascaleDbStorageDetails,
        additional_flash_cache_percent: Optional[_builtins.int] = ...,
        attached_shape_attributes: Optional[Sequence[_builtins.str]] = ...,
        available_shape_attributes: Optional[Sequence[_builtins.str]] = ...,
        oci_uri: Optional[_builtins.str] = ...,
        ocid: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        time_zone: Optional[outputs.ExascaleDbStorageVaultPropertiesTimeZone] = ...,
        vm_cluster_count: Optional[_builtins.int] = ...,
        vm_cluster_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exascaleDbStorageDetails")
    def exascale_db_storage_details(
        self,
    ) -> outputs.ExascaleDbStorageVaultPropertiesExascaleDbStorageDetails: ...
    @_builtins.property
    @pulumi.getter(name="additionalFlashCachePercent")
    def additional_flash_cache_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="attachedShapeAttributes")
    def attached_shape_attributes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="availableShapeAttributes")
    def available_shape_attributes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ociUri")
    def oci_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(
        self,
    ) -> Optional[outputs.ExascaleDbStorageVaultPropertiesTimeZone]: ...
    @_builtins.property
    @pulumi.getter(name="vmClusterCount")
    def vm_cluster_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="vmClusterIds")
    def vm_cluster_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ExascaleDbStorageVaultPropertiesExascaleDbStorageDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        total_size_gbs: _builtins.int,
        available_size_gbs: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalSizeGbs")
    def total_size_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="availableSizeGbs")
    def available_size_gbs(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ExascaleDbStorageVaultPropertiesTimeZone(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetAutonomousDatabasePropertyResult(dict):
    def __init__(
        __self__,
        *,
        actual_used_data_storage_size_tb: _builtins.float,
        allocated_storage_size_tb: _builtins.float,
        apex_details: Sequence[outputs.GetAutonomousDatabasePropertyApexDetailResult],
        are_primary_allowlisted_ips_used: _builtins.bool,
        autonomous_container_database_id: _builtins.str,
        available_upgrade_versions: Sequence[_builtins.str],
        backup_retention_period_days: _builtins.int,
        character_set: _builtins.str,
        compute_count: _builtins.float,
        connection_strings: Sequence[
            outputs.GetAutonomousDatabasePropertyConnectionStringResult
        ],
        connection_urls: Sequence[
            outputs.GetAutonomousDatabasePropertyConnectionUrlResult
        ],
        cpu_core_count: _builtins.int,
        customer_contacts: Sequence[
            outputs.GetAutonomousDatabasePropertyCustomerContactResult
        ],
        data_safe_state: _builtins.str,
        data_storage_size_gb: _builtins.int,
        data_storage_size_tb: _builtins.int,
        database_management_state: _builtins.str,
        db_edition: _builtins.str,
        db_version: _builtins.str,
        db_workload: _builtins.str,
        failed_data_recovery_duration: _builtins.str,
        is_auto_scaling_enabled: _builtins.bool,
        is_local_data_guard_enabled: _builtins.bool,
        is_storage_auto_scaling_enabled: _builtins.bool,
        license_type: _builtins.str,
        lifecycle_details: _builtins.str,
        local_adg_auto_failover_max_data_loss_limit: _builtins.int,
        local_disaster_recovery_type: _builtins.str,
        local_standby_dbs: Sequence[
            outputs.GetAutonomousDatabasePropertyLocalStandbyDbResult
        ],
        maintenance_begin_time: _builtins.str,
        maintenance_end_time: _builtins.str,
        maintenance_schedule_type: _builtins.str,
        memory_per_oracle_compute_unit_gbs: _builtins.int,
        memory_table_gbs: _builtins.int,
        mtls_connection_required: _builtins.bool,
        n_character_set: _builtins.str,
        next_long_term_backup_time: _builtins.str,
        oci_url: _builtins.str,
        ocid: _builtins.str,
        open_mode: _builtins.str,
        operations_insights_state: _builtins.str,
        peer_db_ids: Sequence[_builtins.str],
        permission_level: _builtins.str,
        private_endpoint: _builtins.str,
        private_endpoint_ip: _builtins.str,
        private_endpoint_label: _builtins.str,
        refreshable_mode: _builtins.str,
        refreshable_state: _builtins.str,
        role: _builtins.str,
        scheduled_operation_details: Sequence[
            outputs.GetAutonomousDatabasePropertyScheduledOperationDetailResult
        ],
        secret_id: _builtins.str,
        sql_web_developer_url: _builtins.str,
        state: _builtins.str,
        supported_clone_regions: Sequence[_builtins.str],
        total_auto_backup_storage_size_gbs: _builtins.float,
        used_data_storage_size_tbs: _builtins.int,
        vault_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actualUsedDataStorageSizeTb")
    def actual_used_data_storage_size_tb(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorageSizeTb")
    def allocated_storage_size_tb(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="apexDetails")
    def apex_details(
        self,
    ) -> Sequence[outputs.GetAutonomousDatabasePropertyApexDetailResult]: ...
    @_builtins.property
    @pulumi.getter(name="arePrimaryAllowlistedIpsUsed")
    def are_primary_allowlisted_ips_used(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="autonomousContainerDatabaseId")
    def autonomous_container_database_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availableUpgradeVersions")
    def available_upgrade_versions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionPeriodDays")
    def backup_retention_period_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="characterSet")
    def character_set(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="connectionStrings")
    def connection_strings(
        self,
    ) -> Sequence[outputs.GetAutonomousDatabasePropertyConnectionStringResult]: ...
    @_builtins.property
    @pulumi.getter(name="connectionUrls")
    def connection_urls(
        self,
    ) -> Sequence[outputs.GetAutonomousDatabasePropertyConnectionUrlResult]: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="customerContacts")
    def customer_contacts(
        self,
    ) -> Sequence[outputs.GetAutonomousDatabasePropertyCustomerContactResult]: ...
    @_builtins.property
    @pulumi.getter(name="dataSafeState")
    def data_safe_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeGb")
    def data_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeTb")
    def data_storage_size_tb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="databaseManagementState")
    def database_management_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbEdition")
    def db_edition(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbWorkload")
    def db_workload(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="failedDataRecoveryDuration")
    def failed_data_recovery_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isAutoScalingEnabled")
    def is_auto_scaling_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isLocalDataGuardEnabled")
    def is_local_data_guard_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isStorageAutoScalingEnabled")
    def is_storage_auto_scaling_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localAdgAutoFailoverMaxDataLossLimit")
    def local_adg_auto_failover_max_data_loss_limit(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="localDisasterRecoveryType")
    def local_disaster_recovery_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localStandbyDbs")
    def local_standby_dbs(
        self,
    ) -> Sequence[outputs.GetAutonomousDatabasePropertyLocalStandbyDbResult]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceBeginTime")
    def maintenance_begin_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceEndTime")
    def maintenance_end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceScheduleType")
    def maintenance_schedule_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memoryPerOracleComputeUnitGbs")
    def memory_per_oracle_compute_unit_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memoryTableGbs")
    def memory_table_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="mtlsConnectionRequired")
    def mtls_connection_required(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="nCharacterSet")
    def n_character_set(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextLongTermBackupTime")
    def next_long_term_backup_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="openMode")
    def open_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="operationsInsightsState")
    def operations_insights_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peerDbIds")
    def peer_db_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permissionLevel")
    def permission_level(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointIp")
    def private_endpoint_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointLabel")
    def private_endpoint_label(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="refreshableMode")
    def refreshable_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="refreshableState")
    def refreshable_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scheduledOperationDetails")
    def scheduled_operation_details(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasePropertyScheduledOperationDetailResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sqlWebDeveloperUrl")
    def sql_web_developer_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportedCloneRegions")
    def supported_clone_regions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="totalAutoBackupStorageSizeGbs")
    def total_auto_backup_storage_size_gbs(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="usedDataStorageSizeTbs")
    def used_data_storage_size_tbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasePropertyApexDetailResult(dict):
    def __init__(
        __self__, *, apex_version: _builtins.str, ords_version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apexVersion")
    def apex_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ordsVersion")
    def ords_version(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasePropertyConnectionStringResult(dict):
    def __init__(
        __self__,
        *,
        all_connection_strings: Sequence[
            outputs.GetAutonomousDatabasePropertyConnectionStringAllConnectionStringResult
        ],
        dedicated: _builtins.str,
        high: _builtins.str,
        low: _builtins.str,
        medium: _builtins.str,
        profiles: Sequence[
            outputs.GetAutonomousDatabasePropertyConnectionStringProfileResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allConnectionStrings")
    def all_connection_strings(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasePropertyConnectionStringAllConnectionStringResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def dedicated(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def high(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def low(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def profiles(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasePropertyConnectionStringProfileResult
    ]: ...

@pulumi.output_type
class GetAutonomousDatabasePropertyConnectionStringAllConnectionStringResult(dict):
    def __init__(
        __self__, *, high: _builtins.str, low: _builtins.str, medium: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def high(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def low(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasePropertyConnectionStringProfileResult(dict):
    def __init__(
        __self__,
        *,
        consumer_group: _builtins.str,
        display_name: _builtins.str,
        host_format: _builtins.str,
        is_regional: _builtins.bool,
        protocol: _builtins.str,
        session_mode: _builtins.str,
        syntax_format: _builtins.str,
        tls_authentication: _builtins.str,
        value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostFormat")
    def host_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isRegional")
    def is_regional(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionMode")
    def session_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syntaxFormat")
    def syntax_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tlsAuthentication")
    def tls_authentication(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasePropertyConnectionUrlResult(dict):
    def __init__(
        __self__,
        *,
        apex_uri: _builtins.str,
        database_transforms_uri: _builtins.str,
        graph_studio_uri: _builtins.str,
        machine_learning_notebook_uri: _builtins.str,
        machine_learning_user_management_uri: _builtins.str,
        mongo_db_uri: _builtins.str,
        ords_uri: _builtins.str,
        sql_dev_web_uri: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apexUri")
    def apex_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseTransformsUri")
    def database_transforms_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="graphStudioUri")
    def graph_studio_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineLearningNotebookUri")
    def machine_learning_notebook_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineLearningUserManagementUri")
    def machine_learning_user_management_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mongoDbUri")
    def mongo_db_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ordsUri")
    def ords_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sqlDevWebUri")
    def sql_dev_web_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasePropertyCustomerContactResult(dict):
    def __init__(__self__, *, email: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasePropertyLocalStandbyDbResult(dict):
    def __init__(
        __self__,
        *,
        data_guard_role_changed_time: _builtins.str,
        disaster_recovery_role_changed_time: _builtins.str,
        lag_time_duration: _builtins.str,
        lifecycle_details: _builtins.str,
        state: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataGuardRoleChangedTime")
    def data_guard_role_changed_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="disasterRecoveryRoleChangedTime")
    def disaster_recovery_role_changed_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lagTimeDuration")
    def lag_time_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasePropertyScheduledOperationDetailResult(dict):
    def __init__(
        __self__,
        *,
        day_of_week: _builtins.str,
        start_times: Sequence[
            outputs.GetAutonomousDatabasePropertyScheduledOperationDetailStartTimeResult
        ],
        stop_times: Sequence[
            outputs.GetAutonomousDatabasePropertyScheduledOperationDetailStopTimeResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasePropertyScheduledOperationDetailStartTimeResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="stopTimes")
    def stop_times(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasePropertyScheduledOperationDetailStopTimeResult
    ]: ...

@pulumi.output_type
class GetAutonomousDatabasePropertyScheduledOperationDetailStartTimeResult(dict):
    def __init__(
        __self__,
        *,
        hours: _builtins.int,
        minutes: _builtins.int,
        nanos: _builtins.int,
        seconds: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetAutonomousDatabasePropertyScheduledOperationDetailStopTimeResult(dict):
    def __init__(
        __self__,
        *,
        hours: _builtins.int,
        minutes: _builtins.int,
        nanos: _builtins.int,
        seconds: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetAutonomousDatabaseSourceConfigResult(dict):
    def __init__(
        __self__,
        *,
        automatic_backups_replication_enabled: _builtins.bool,
        autonomous_database: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticBackupsReplicationEnabled")
    def automatic_backups_replication_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="autonomousDatabase")
    def autonomous_database(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabaseResult(dict):
    def __init__(
        __self__,
        *,
        admin_password: _builtins.str,
        autonomous_database_id: _builtins.str,
        cidr: _builtins.str,
        create_time: _builtins.str,
        database: _builtins.str,
        deletion_protection: _builtins.bool,
        disaster_recovery_supported_locations: Sequence[_builtins.str],
        display_name: _builtins.str,
        effective_labels: Mapping[str, _builtins.str],
        entitlement_id: _builtins.str,
        labels: Mapping[str, _builtins.str],
        location: _builtins.str,
        name: _builtins.str,
        network: _builtins.str,
        odb_network: _builtins.str,
        odb_subnet: _builtins.str,
        peer_autonomous_databases: Sequence[_builtins.str],
        project: _builtins.str,
        properties: Sequence[
            outputs.GetAutonomousDatabasesAutonomousDatabasePropertyResult
        ],
        pulumi_labels: Mapping[str, _builtins.str],
        source_configs: Sequence[
            outputs.GetAutonomousDatabasesAutonomousDatabaseSourceConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autonomousDatabaseId")
    def autonomous_database_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="disasterRecoverySupportedLocations")
    def disaster_recovery_supported_locations(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entitlementId")
    def entitlement_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="odbNetwork")
    def odb_network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="odbSubnet")
    def odb_subnet(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peerAutonomousDatabases")
    def peer_autonomous_databases(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Sequence[outputs.GetAutonomousDatabasesAutonomousDatabasePropertyResult]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceConfigs")
    def source_configs(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasesAutonomousDatabaseSourceConfigResult
    ]: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabasePropertyResult(dict):
    def __init__(
        __self__,
        *,
        actual_used_data_storage_size_tb: _builtins.float,
        allocated_storage_size_tb: _builtins.float,
        apex_details: Sequence[
            outputs.GetAutonomousDatabasesAutonomousDatabasePropertyApexDetailResult
        ],
        are_primary_allowlisted_ips_used: _builtins.bool,
        autonomous_container_database_id: _builtins.str,
        available_upgrade_versions: Sequence[_builtins.str],
        backup_retention_period_days: _builtins.int,
        character_set: _builtins.str,
        compute_count: _builtins.float,
        connection_strings: Sequence[
            outputs.GetAutonomousDatabasesAutonomousDatabasePropertyConnectionStringResult
        ],
        connection_urls: Sequence[
            outputs.GetAutonomousDatabasesAutonomousDatabasePropertyConnectionUrlResult
        ],
        cpu_core_count: _builtins.int,
        customer_contacts: Sequence[
            outputs.GetAutonomousDatabasesAutonomousDatabasePropertyCustomerContactResult
        ],
        data_safe_state: _builtins.str,
        data_storage_size_gb: _builtins.int,
        data_storage_size_tb: _builtins.int,
        database_management_state: _builtins.str,
        db_edition: _builtins.str,
        db_version: _builtins.str,
        db_workload: _builtins.str,
        failed_data_recovery_duration: _builtins.str,
        is_auto_scaling_enabled: _builtins.bool,
        is_local_data_guard_enabled: _builtins.bool,
        is_storage_auto_scaling_enabled: _builtins.bool,
        license_type: _builtins.str,
        lifecycle_details: _builtins.str,
        local_adg_auto_failover_max_data_loss_limit: _builtins.int,
        local_disaster_recovery_type: _builtins.str,
        local_standby_dbs: Sequence[
            outputs.GetAutonomousDatabasesAutonomousDatabasePropertyLocalStandbyDbResult
        ],
        maintenance_begin_time: _builtins.str,
        maintenance_end_time: _builtins.str,
        maintenance_schedule_type: _builtins.str,
        memory_per_oracle_compute_unit_gbs: _builtins.int,
        memory_table_gbs: _builtins.int,
        mtls_connection_required: _builtins.bool,
        n_character_set: _builtins.str,
        next_long_term_backup_time: _builtins.str,
        oci_url: _builtins.str,
        ocid: _builtins.str,
        open_mode: _builtins.str,
        operations_insights_state: _builtins.str,
        peer_db_ids: Sequence[_builtins.str],
        permission_level: _builtins.str,
        private_endpoint: _builtins.str,
        private_endpoint_ip: _builtins.str,
        private_endpoint_label: _builtins.str,
        refreshable_mode: _builtins.str,
        refreshable_state: _builtins.str,
        role: _builtins.str,
        scheduled_operation_details: Sequence[
            outputs.GetAutonomousDatabasesAutonomousDatabasePropertyScheduledOperationDetailResult
        ],
        secret_id: _builtins.str,
        sql_web_developer_url: _builtins.str,
        state: _builtins.str,
        supported_clone_regions: Sequence[_builtins.str],
        total_auto_backup_storage_size_gbs: _builtins.float,
        used_data_storage_size_tbs: _builtins.int,
        vault_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actualUsedDataStorageSizeTb")
    def actual_used_data_storage_size_tb(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorageSizeTb")
    def allocated_storage_size_tb(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="apexDetails")
    def apex_details(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasesAutonomousDatabasePropertyApexDetailResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="arePrimaryAllowlistedIpsUsed")
    def are_primary_allowlisted_ips_used(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="autonomousContainerDatabaseId")
    def autonomous_container_database_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availableUpgradeVersions")
    def available_upgrade_versions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionPeriodDays")
    def backup_retention_period_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="characterSet")
    def character_set(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="connectionStrings")
    def connection_strings(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasesAutonomousDatabasePropertyConnectionStringResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="connectionUrls")
    def connection_urls(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasesAutonomousDatabasePropertyConnectionUrlResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="customerContacts")
    def customer_contacts(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasesAutonomousDatabasePropertyCustomerContactResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dataSafeState")
    def data_safe_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeGb")
    def data_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeTb")
    def data_storage_size_tb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="databaseManagementState")
    def database_management_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbEdition")
    def db_edition(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbWorkload")
    def db_workload(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="failedDataRecoveryDuration")
    def failed_data_recovery_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isAutoScalingEnabled")
    def is_auto_scaling_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isLocalDataGuardEnabled")
    def is_local_data_guard_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="isStorageAutoScalingEnabled")
    def is_storage_auto_scaling_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localAdgAutoFailoverMaxDataLossLimit")
    def local_adg_auto_failover_max_data_loss_limit(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="localDisasterRecoveryType")
    def local_disaster_recovery_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localStandbyDbs")
    def local_standby_dbs(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasesAutonomousDatabasePropertyLocalStandbyDbResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceBeginTime")
    def maintenance_begin_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceEndTime")
    def maintenance_end_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceScheduleType")
    def maintenance_schedule_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memoryPerOracleComputeUnitGbs")
    def memory_per_oracle_compute_unit_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memoryTableGbs")
    def memory_table_gbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="mtlsConnectionRequired")
    def mtls_connection_required(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="nCharacterSet")
    def n_character_set(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextLongTermBackupTime")
    def next_long_term_backup_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="openMode")
    def open_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="operationsInsightsState")
    def operations_insights_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="peerDbIds")
    def peer_db_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permissionLevel")
    def permission_level(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointIp")
    def private_endpoint_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointLabel")
    def private_endpoint_label(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="refreshableMode")
    def refreshable_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="refreshableState")
    def refreshable_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scheduledOperationDetails")
    def scheduled_operation_details(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasesAutonomousDatabasePropertyScheduledOperationDetailResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sqlWebDeveloperUrl")
    def sql_web_developer_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="supportedCloneRegions")
    def supported_clone_regions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="totalAutoBackupStorageSizeGbs")
    def total_auto_backup_storage_size_gbs(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="usedDataStorageSizeTbs")
    def used_data_storage_size_tbs(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabasePropertyApexDetailResult(dict):
    def __init__(
        __self__, *, apex_version: _builtins.str, ords_version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apexVersion")
    def apex_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ordsVersion")
    def ords_version(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabasePropertyConnectionStringResult(dict):
    def __init__(
        __self__,
        *,
        all_connection_strings: Sequence[
            outputs.GetAutonomousDatabasesAutonomousDatabasePropertyConnectionStringAllConnectionStringResult
        ],
        dedicated: _builtins.str,
        high: _builtins.str,
        low: _builtins.str,
        medium: _builtins.str,
        profiles: Sequence[
            outputs.GetAutonomousDatabasesAutonomousDatabasePropertyConnectionStringProfileResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allConnectionStrings")
    def all_connection_strings(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasesAutonomousDatabasePropertyConnectionStringAllConnectionStringResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def dedicated(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def high(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def low(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def profiles(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasesAutonomousDatabasePropertyConnectionStringProfileResult
    ]: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabasePropertyConnectionStringAllConnectionStringResult(
    dict
):
    def __init__(
        __self__, *, high: _builtins.str, low: _builtins.str, medium: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def high(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def low(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabasePropertyConnectionStringProfileResult(
    dict
):
    def __init__(
        __self__,
        *,
        consumer_group: _builtins.str,
        display_name: _builtins.str,
        host_format: _builtins.str,
        is_regional: _builtins.bool,
        protocol: _builtins.str,
        session_mode: _builtins.str,
        syntax_format: _builtins.str,
        tls_authentication: _builtins.str,
        value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostFormat")
    def host_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isRegional")
    def is_regional(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionMode")
    def session_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syntaxFormat")
    def syntax_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tlsAuthentication")
    def tls_authentication(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabasePropertyConnectionUrlResult(dict):
    def __init__(
        __self__,
        *,
        apex_uri: _builtins.str,
        database_transforms_uri: _builtins.str,
        graph_studio_uri: _builtins.str,
        machine_learning_notebook_uri: _builtins.str,
        machine_learning_user_management_uri: _builtins.str,
        mongo_db_uri: _builtins.str,
        ords_uri: _builtins.str,
        sql_dev_web_uri: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apexUri")
    def apex_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseTransformsUri")
    def database_transforms_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="graphStudioUri")
    def graph_studio_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineLearningNotebookUri")
    def machine_learning_notebook_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineLearningUserManagementUri")
    def machine_learning_user_management_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mongoDbUri")
    def mongo_db_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ordsUri")
    def ords_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sqlDevWebUri")
    def sql_dev_web_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabasePropertyCustomerContactResult(dict):
    def __init__(__self__, *, email: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabasePropertyLocalStandbyDbResult(dict):
    def __init__(
        __self__,
        *,
        data_guard_role_changed_time: _builtins.str,
        disaster_recovery_role_changed_time: _builtins.str,
        lag_time_duration: _builtins.str,
        lifecycle_details: _builtins.str,
        state: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataGuardRoleChangedTime")
    def data_guard_role_changed_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="disasterRecoveryRoleChangedTime")
    def disaster_recovery_role_changed_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lagTimeDuration")
    def lag_time_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabasePropertyScheduledOperationDetailResult(
    dict
):
    def __init__(
        __self__,
        *,
        day_of_week: _builtins.str,
        start_times: Sequence[
            outputs.GetAutonomousDatabasesAutonomousDatabasePropertyScheduledOperationDetailStartTimeResult
        ],
        stop_times: Sequence[
            outputs.GetAutonomousDatabasesAutonomousDatabasePropertyScheduledOperationDetailStopTimeResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasesAutonomousDatabasePropertyScheduledOperationDetailStartTimeResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="stopTimes")
    def stop_times(
        self,
    ) -> Sequence[
        outputs.GetAutonomousDatabasesAutonomousDatabasePropertyScheduledOperationDetailStopTimeResult
    ]: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabasePropertyScheduledOperationDetailStartTimeResult(
    dict
):
    def __init__(
        __self__,
        *,
        hours: _builtins.int,
        minutes: _builtins.int,
        nanos: _builtins.int,
        seconds: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabasePropertyScheduledOperationDetailStopTimeResult(
    dict
):
    def __init__(
        __self__,
        *,
        hours: _builtins.int,
        minutes: _builtins.int,
        nanos: _builtins.int,
        seconds: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetAutonomousDatabasesAutonomousDatabaseSourceConfigResult(dict):
    def __init__(
        __self__,
        *,
        automatic_backups_replication_enabled: _builtins.bool,
        autonomous_database: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticBackupsReplicationEnabled")
    def automatic_backups_replication_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="autonomousDatabase")
    def autonomous_database(self) -> _builtins.str: ...

@pulumi.output_type
class GetCloudExadataInfrastructurePropertyResult(dict):
    def __init__(
        __self__,
        *,
        activated_storage_count: _builtins.int,
        additional_storage_count: _builtins.int,
        available_storage_size_gb: _builtins.int,
        compute_count: _builtins.int,
        cpu_count: _builtins.int,
        customer_contacts: Sequence[
            outputs.GetCloudExadataInfrastructurePropertyCustomerContactResult
        ],
        data_storage_size_tb: _builtins.float,
        db_node_storage_size_gb: _builtins.int,
        db_server_version: _builtins.str,
        maintenance_windows: Sequence[
            outputs.GetCloudExadataInfrastructurePropertyMaintenanceWindowResult
        ],
        max_cpu_count: _builtins.int,
        max_data_storage_tb: _builtins.float,
        max_db_node_storage_size_gb: _builtins.int,
        max_memory_gb: _builtins.int,
        memory_size_gb: _builtins.int,
        monthly_db_server_version: _builtins.str,
        monthly_storage_server_version: _builtins.str,
        next_maintenance_run_id: _builtins.str,
        next_maintenance_run_time: _builtins.str,
        next_security_maintenance_run_time: _builtins.str,
        oci_url: _builtins.str,
        ocid: _builtins.str,
        shape: _builtins.str,
        state: _builtins.str,
        storage_count: _builtins.int,
        storage_server_version: _builtins.str,
        total_storage_size_gb: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activatedStorageCount")
    def activated_storage_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="additionalStorageCount")
    def additional_storage_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="availableStorageSizeGb")
    def available_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="customerContacts")
    def customer_contacts(
        self,
    ) -> Sequence[
        outputs.GetCloudExadataInfrastructurePropertyCustomerContactResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeTb")
    def data_storage_size_tb(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeGb")
    def db_node_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dbServerVersion")
    def db_server_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(
        self,
    ) -> Sequence[
        outputs.GetCloudExadataInfrastructurePropertyMaintenanceWindowResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxCpuCount")
    def max_cpu_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxDataStorageTb")
    def max_data_storage_tb(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="maxDbNodeStorageSizeGb")
    def max_db_node_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxMemoryGb")
    def max_memory_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="monthlyDbServerVersion")
    def monthly_db_server_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="monthlyStorageServerVersion")
    def monthly_storage_server_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextMaintenanceRunId")
    def next_maintenance_run_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextMaintenanceRunTime")
    def next_maintenance_run_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextSecurityMaintenanceRunTime")
    def next_security_maintenance_run_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageCount")
    def storage_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageServerVersion")
    def storage_server_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="totalStorageSizeGb")
    def total_storage_size_gb(self) -> _builtins.int: ...

@pulumi.output_type
class GetCloudExadataInfrastructurePropertyCustomerContactResult(dict):
    def __init__(__self__, *, email: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...

@pulumi.output_type
class GetCloudExadataInfrastructurePropertyMaintenanceWindowResult(dict):
    def __init__(
        __self__,
        *,
        custom_action_timeout_mins: _builtins.int,
        days_of_weeks: Sequence[_builtins.str],
        hours_of_days: Sequence[_builtins.int],
        is_custom_action_timeout_enabled: _builtins.bool,
        lead_time_week: _builtins.int,
        months: Sequence[_builtins.str],
        patching_mode: _builtins.str,
        preference: _builtins.str,
        weeks_of_months: Sequence[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customActionTimeoutMins")
    def custom_action_timeout_mins(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hoursOfDays")
    def hours_of_days(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="isCustomActionTimeoutEnabled")
    def is_custom_action_timeout_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="leadTimeWeek")
    def lead_time_week(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def months(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="patchingMode")
    def patching_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weeksOfMonths")
    def weeks_of_months(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class GetCloudExadataInfrastructuresCloudExadataInfrastructureResult(dict):
    def __init__(
        __self__,
        *,
        cloud_exadata_infrastructure_id: _builtins.str,
        create_time: _builtins.str,
        deletion_protection: _builtins.bool,
        display_name: _builtins.str,
        effective_labels: Mapping[str, _builtins.str],
        entitlement_id: _builtins.str,
        gcp_oracle_zone: _builtins.str,
        labels: Mapping[str, _builtins.str],
        location: _builtins.str,
        name: _builtins.str,
        project: _builtins.str,
        properties: Sequence[
            outputs.GetCloudExadataInfrastructuresCloudExadataInfrastructurePropertyResult
        ],
        pulumi_labels: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudExadataInfrastructureId")
    def cloud_exadata_infrastructure_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entitlementId")
    def entitlement_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gcpOracleZone")
    def gcp_oracle_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Sequence[
        outputs.GetCloudExadataInfrastructuresCloudExadataInfrastructurePropertyResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetCloudExadataInfrastructuresCloudExadataInfrastructurePropertyResult(dict):
    def __init__(
        __self__,
        *,
        activated_storage_count: _builtins.int,
        additional_storage_count: _builtins.int,
        available_storage_size_gb: _builtins.int,
        compute_count: _builtins.int,
        cpu_count: _builtins.int,
        customer_contacts: Sequence[
            outputs.GetCloudExadataInfrastructuresCloudExadataInfrastructurePropertyCustomerContactResult
        ],
        data_storage_size_tb: _builtins.float,
        db_node_storage_size_gb: _builtins.int,
        db_server_version: _builtins.str,
        maintenance_windows: Sequence[
            outputs.GetCloudExadataInfrastructuresCloudExadataInfrastructurePropertyMaintenanceWindowResult
        ],
        max_cpu_count: _builtins.int,
        max_data_storage_tb: _builtins.float,
        max_db_node_storage_size_gb: _builtins.int,
        max_memory_gb: _builtins.int,
        memory_size_gb: _builtins.int,
        monthly_db_server_version: _builtins.str,
        monthly_storage_server_version: _builtins.str,
        next_maintenance_run_id: _builtins.str,
        next_maintenance_run_time: _builtins.str,
        next_security_maintenance_run_time: _builtins.str,
        oci_url: _builtins.str,
        ocid: _builtins.str,
        shape: _builtins.str,
        state: _builtins.str,
        storage_count: _builtins.int,
        storage_server_version: _builtins.str,
        total_storage_size_gb: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activatedStorageCount")
    def activated_storage_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="additionalStorageCount")
    def additional_storage_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="availableStorageSizeGb")
    def available_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="customerContacts")
    def customer_contacts(
        self,
    ) -> Sequence[
        outputs.GetCloudExadataInfrastructuresCloudExadataInfrastructurePropertyCustomerContactResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeTb")
    def data_storage_size_tb(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeGb")
    def db_node_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dbServerVersion")
    def db_server_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(
        self,
    ) -> Sequence[
        outputs.GetCloudExadataInfrastructuresCloudExadataInfrastructurePropertyMaintenanceWindowResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxCpuCount")
    def max_cpu_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxDataStorageTb")
    def max_data_storage_tb(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="maxDbNodeStorageSizeGb")
    def max_db_node_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxMemoryGb")
    def max_memory_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="monthlyDbServerVersion")
    def monthly_db_server_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="monthlyStorageServerVersion")
    def monthly_storage_server_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextMaintenanceRunId")
    def next_maintenance_run_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextMaintenanceRunTime")
    def next_maintenance_run_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nextSecurityMaintenanceRunTime")
    def next_security_maintenance_run_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageCount")
    def storage_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageServerVersion")
    def storage_server_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="totalStorageSizeGb")
    def total_storage_size_gb(self) -> _builtins.int: ...

@pulumi.output_type
class GetCloudExadataInfrastructuresCloudExadataInfrastructurePropertyCustomerContactResult(
    dict
):
    def __init__(__self__, *, email: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...

@pulumi.output_type
class GetCloudExadataInfrastructuresCloudExadataInfrastructurePropertyMaintenanceWindowResult(
    dict
):
    def __init__(
        __self__,
        *,
        custom_action_timeout_mins: _builtins.int,
        days_of_weeks: Sequence[_builtins.str],
        hours_of_days: Sequence[_builtins.int],
        is_custom_action_timeout_enabled: _builtins.bool,
        lead_time_week: _builtins.int,
        months: Sequence[_builtins.str],
        patching_mode: _builtins.str,
        preference: _builtins.str,
        weeks_of_months: Sequence[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customActionTimeoutMins")
    def custom_action_timeout_mins(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hoursOfDays")
    def hours_of_days(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="isCustomActionTimeoutEnabled")
    def is_custom_action_timeout_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="leadTimeWeek")
    def lead_time_week(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def months(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="patchingMode")
    def patching_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weeksOfMonths")
    def weeks_of_months(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class GetCloudVmClusterPropertyResult(dict):
    def __init__(
        __self__,
        *,
        cluster_name: _builtins.str,
        compartment_id: _builtins.str,
        cpu_core_count: _builtins.int,
        data_storage_size_tb: _builtins.float,
        db_node_storage_size_gb: _builtins.int,
        db_server_ocids: Sequence[_builtins.str],
        diagnostics_data_collection_options: Sequence[
            outputs.GetCloudVmClusterPropertyDiagnosticsDataCollectionOptionResult
        ],
        disk_redundancy: _builtins.str,
        dns_listener_ip: _builtins.str,
        domain: _builtins.str,
        gi_version: _builtins.str,
        hostname: _builtins.str,
        hostname_prefix: _builtins.str,
        license_type: _builtins.str,
        local_backup_enabled: _builtins.bool,
        memory_size_gb: _builtins.int,
        node_count: _builtins.int,
        oci_url: _builtins.str,
        ocid: _builtins.str,
        ocpu_count: _builtins.float,
        scan_dns: _builtins.str,
        scan_dns_record_id: _builtins.str,
        scan_ip_ids: Sequence[_builtins.str],
        scan_listener_port_tcp: _builtins.int,
        scan_listener_port_tcp_ssl: _builtins.int,
        shape: _builtins.str,
        sparse_diskgroup_enabled: _builtins.bool,
        ssh_public_keys: Sequence[_builtins.str],
        state: _builtins.str,
        storage_size_gb: _builtins.int,
        system_version: _builtins.str,
        time_zones: Sequence[outputs.GetCloudVmClusterPropertyTimeZoneResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeTb")
    def data_storage_size_tb(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeGb")
    def db_node_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dbServerOcids")
    def db_server_ocids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsDataCollectionOptions")
    def diagnostics_data_collection_options(
        self,
    ) -> Sequence[
        outputs.GetCloudVmClusterPropertyDiagnosticsDataCollectionOptionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="diskRedundancy")
    def disk_redundancy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsListenerIp")
    def dns_listener_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="giVersion")
    def gi_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localBackupEnabled")
    def local_backup_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ocpuCount")
    def ocpu_count(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="scanDns")
    def scan_dns(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanDnsRecordId")
    def scan_dns_record_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanIpIds")
    def scan_ip_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcp")
    def scan_listener_port_tcp(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcpSsl")
    def scan_listener_port_tcp_ssl(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sparseDiskgroupEnabled")
    def sparse_diskgroup_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageSizeGb")
    def storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="systemVersion")
    def system_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeZones")
    def time_zones(
        self,
    ) -> Sequence[outputs.GetCloudVmClusterPropertyTimeZoneResult]: ...

@pulumi.output_type
class GetCloudVmClusterPropertyDiagnosticsDataCollectionOptionResult(dict):
    def __init__(
        __self__,
        *,
        diagnostics_events_enabled: _builtins.bool,
        health_monitoring_enabled: _builtins.bool,
        incident_logs_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsEventsEnabled")
    def diagnostics_events_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="healthMonitoringEnabled")
    def health_monitoring_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="incidentLogsEnabled")
    def incident_logs_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetCloudVmClusterPropertyTimeZoneResult(dict):
    def __init__(__self__, *, id: _builtins.str, version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class GetCloudVmClustersCloudVmClusterResult(dict):
    def __init__(
        __self__,
        *,
        backup_odb_subnet: _builtins.str,
        backup_subnet_cidr: _builtins.str,
        cidr: _builtins.str,
        cloud_vm_cluster_id: _builtins.str,
        create_time: _builtins.str,
        deletion_protection: _builtins.bool,
        display_name: _builtins.str,
        effective_labels: Mapping[str, _builtins.str],
        exadata_infrastructure: _builtins.str,
        gcp_oracle_zone: _builtins.str,
        labels: Mapping[str, _builtins.str],
        location: _builtins.str,
        name: _builtins.str,
        network: _builtins.str,
        odb_network: _builtins.str,
        odb_subnet: _builtins.str,
        project: _builtins.str,
        properties: Sequence[outputs.GetCloudVmClustersCloudVmClusterPropertyResult],
        pulumi_labels: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupOdbSubnet")
    def backup_odb_subnet(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backupSubnetCidr")
    def backup_subnet_cidr(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudVmClusterId")
    def cloud_vm_cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exadataInfrastructure")
    def exadata_infrastructure(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gcpOracleZone")
    def gcp_oracle_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="odbNetwork")
    def odb_network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="odbSubnet")
    def odb_subnet(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Sequence[outputs.GetCloudVmClustersCloudVmClusterPropertyResult]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetCloudVmClustersCloudVmClusterPropertyResult(dict):
    def __init__(
        __self__,
        *,
        cluster_name: _builtins.str,
        compartment_id: _builtins.str,
        cpu_core_count: _builtins.int,
        data_storage_size_tb: _builtins.float,
        db_node_storage_size_gb: _builtins.int,
        db_server_ocids: Sequence[_builtins.str],
        diagnostics_data_collection_options: Sequence[
            outputs.GetCloudVmClustersCloudVmClusterPropertyDiagnosticsDataCollectionOptionResult
        ],
        disk_redundancy: _builtins.str,
        dns_listener_ip: _builtins.str,
        domain: _builtins.str,
        gi_version: _builtins.str,
        hostname: _builtins.str,
        hostname_prefix: _builtins.str,
        license_type: _builtins.str,
        local_backup_enabled: _builtins.bool,
        memory_size_gb: _builtins.int,
        node_count: _builtins.int,
        oci_url: _builtins.str,
        ocid: _builtins.str,
        ocpu_count: _builtins.float,
        scan_dns: _builtins.str,
        scan_dns_record_id: _builtins.str,
        scan_ip_ids: Sequence[_builtins.str],
        scan_listener_port_tcp: _builtins.int,
        scan_listener_port_tcp_ssl: _builtins.int,
        shape: _builtins.str,
        sparse_diskgroup_enabled: _builtins.bool,
        ssh_public_keys: Sequence[_builtins.str],
        state: _builtins.str,
        storage_size_gb: _builtins.int,
        system_version: _builtins.str,
        time_zones: Sequence[
            outputs.GetCloudVmClustersCloudVmClusterPropertyTimeZoneResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeTb")
    def data_storage_size_tb(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeGb")
    def db_node_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dbServerOcids")
    def db_server_ocids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsDataCollectionOptions")
    def diagnostics_data_collection_options(
        self,
    ) -> Sequence[
        outputs.GetCloudVmClustersCloudVmClusterPropertyDiagnosticsDataCollectionOptionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="diskRedundancy")
    def disk_redundancy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsListenerIp")
    def dns_listener_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="giVersion")
    def gi_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localBackupEnabled")
    def local_backup_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ocpuCount")
    def ocpu_count(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="scanDns")
    def scan_dns(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanDnsRecordId")
    def scan_dns_record_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanIpIds")
    def scan_ip_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcp")
    def scan_listener_port_tcp(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcpSsl")
    def scan_listener_port_tcp_ssl(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sparseDiskgroupEnabled")
    def sparse_diskgroup_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageSizeGb")
    def storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="systemVersion")
    def system_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeZones")
    def time_zones(
        self,
    ) -> Sequence[outputs.GetCloudVmClustersCloudVmClusterPropertyTimeZoneResult]: ...

@pulumi.output_type
class GetCloudVmClustersCloudVmClusterPropertyDiagnosticsDataCollectionOptionResult(
    dict
):
    def __init__(
        __self__,
        *,
        diagnostics_events_enabled: _builtins.bool,
        health_monitoring_enabled: _builtins.bool,
        incident_logs_enabled: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsEventsEnabled")
    def diagnostics_events_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="healthMonitoringEnabled")
    def health_monitoring_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="incidentLogsEnabled")
    def incident_logs_enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetCloudVmClustersCloudVmClusterPropertyTimeZoneResult(dict):
    def __init__(__self__, *, id: _builtins.str, version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class GetDbNodesDbNodeResult(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        properties: Sequence[outputs.GetDbNodesDbNodePropertyResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Sequence[outputs.GetDbNodesDbNodePropertyResult]: ...

@pulumi.output_type
class GetDbNodesDbNodePropertyResult(dict):
    def __init__(
        __self__,
        *,
        db_node_storage_size_gb: _builtins.int,
        db_server_ocid: _builtins.str,
        hostname: _builtins.str,
        memory_size_gb: _builtins.int,
        ocid: _builtins.str,
        ocpu_count: _builtins.int,
        state: _builtins.str,
        total_cpu_core_count: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeGb")
    def db_node_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="dbServerOcid")
    def db_server_ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ocpuCount")
    def ocpu_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="totalCpuCoreCount")
    def total_cpu_core_count(self) -> _builtins.int: ...

@pulumi.output_type
class GetDbServersDbServerResult(dict):
    def __init__(
        __self__,
        *,
        display_name: _builtins.str,
        properties: Sequence[outputs.GetDbServersDbServerPropertyResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Sequence[outputs.GetDbServersDbServerPropertyResult]: ...

@pulumi.output_type
class GetDbServersDbServerPropertyResult(dict):
    def __init__(
        __self__,
        *,
        db_node_ids: Sequence[_builtins.str],
        db_node_storage_size_gb: _builtins.int,
        max_db_node_storage_size_gb: _builtins.int,
        max_memory_size_gb: _builtins.int,
        max_ocpu_count: _builtins.int,
        memory_size_gb: _builtins.int,
        ocid: _builtins.str,
        ocpu_count: _builtins.int,
        state: _builtins.str,
        vm_count: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbNodeIds")
    def db_node_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeGb")
    def db_node_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxDbNodeStorageSizeGb")
    def max_db_node_storage_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxMemorySizeGb")
    def max_memory_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxOcpuCount")
    def max_ocpu_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ocpuCount")
    def ocpu_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vmCount")
    def vm_count(self) -> _builtins.int: ...
