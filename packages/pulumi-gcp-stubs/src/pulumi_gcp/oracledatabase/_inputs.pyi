import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AutonomousDatabasePropertiesArgs",
    "AutonomousDatabasePropertiesArgsDict",
    "AutonomousDatabasePropertiesApexDetailArgs",
    "AutonomousDatabasePropertiesApexDetailArgsDict",
    "AutonomousDatabasePropertiesConnectionStringArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "AutonomousDatabasePropertiesConnectionUrlArgs",
    "AutonomousDatabasePropertiesConnectionUrlArgsDict",
    "AutonomousDatabasePropertiesCustomerContactArgs",
    ...,
    "AutonomousDatabasePropertiesLocalStandbyDbArgs",
    "AutonomousDatabasePropertiesLocalStandbyDbArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AutonomousDatabaseSourceConfigArgs",
    "AutonomousDatabaseSourceConfigArgsDict",
    "CloudExadataInfrastructurePropertiesArgs",
    "CloudExadataInfrastructurePropertiesArgsDict",
    ...,
    ...,
    ...,
    ...,
    "CloudVmClusterPropertiesArgs",
    "CloudVmClusterPropertiesArgsDict",
    ...,
    ...,
    "CloudVmClusterPropertiesTimeZoneArgs",
    "CloudVmClusterPropertiesTimeZoneArgsDict",
    "DbSystemPropertiesArgs",
    "DbSystemPropertiesArgsDict",
    "DbSystemPropertiesDataCollectionOptionsArgs",
    "DbSystemPropertiesDataCollectionOptionsArgsDict",
    "DbSystemPropertiesDbHomeArgs",
    "DbSystemPropertiesDbHomeArgsDict",
    "DbSystemPropertiesDbHomeDatabaseArgs",
    "DbSystemPropertiesDbHomeDatabaseArgsDict",
    "DbSystemPropertiesDbHomeDatabasePropertiesArgs",
    "DbSystemPropertiesDbHomeDatabasePropertiesArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DbSystemPropertiesDbSystemOptionsArgs",
    "DbSystemPropertiesDbSystemOptionsArgsDict",
    "DbSystemPropertiesTimeZoneArgs",
    "DbSystemPropertiesTimeZoneArgsDict",
    "ExadbVmClusterPropertiesArgs",
    "ExadbVmClusterPropertiesArgsDict",
    "ExadbVmClusterPropertiesDataCollectionOptionsArgs",
    ...,
    "ExadbVmClusterPropertiesTimeZoneArgs",
    "ExadbVmClusterPropertiesTimeZoneArgsDict",
    "ExadbVmClusterPropertiesVmFileSystemStorageArgs",
    ...,
    "ExascaleDbStorageVaultPropertiesArgs",
    "ExascaleDbStorageVaultPropertiesArgsDict",
    ...,
    ...,
    "ExascaleDbStorageVaultPropertiesTimeZoneArgs",
    "ExascaleDbStorageVaultPropertiesTimeZoneArgsDict",
]

class AutonomousDatabasePropertiesArgsDict(TypedDict):
    db_workload: pulumi.Input[_builtins.str]
    license_type: pulumi.Input[_builtins.str]
    actual_used_data_storage_size_tb: NotRequired[pulumi.Input[_builtins.float]]
    allocated_storage_size_tb: NotRequired[pulumi.Input[_builtins.float]]
    apex_details: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutonomousDatabasePropertiesApexDetailArgsDict]]
        ]
    ]
    are_primary_allowlisted_ips_used: NotRequired[pulumi.Input[_builtins.bool]]
    autonomous_container_database_id: NotRequired[pulumi.Input[_builtins.str]]
    available_upgrade_versions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    backup_retention_period_days: NotRequired[pulumi.Input[_builtins.int]]
    character_set: NotRequired[pulumi.Input[_builtins.str]]
    compute_count: NotRequired[pulumi.Input[_builtins.float]]
    connection_strings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutonomousDatabasePropertiesConnectionStringArgsDict]]
        ]
    ]
    connection_urls: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutonomousDatabasePropertiesConnectionUrlArgsDict]]
        ]
    ]
    cpu_core_count: NotRequired[pulumi.Input[_builtins.int]]
    customer_contacts: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutonomousDatabasePropertiesCustomerContactArgsDict]]
        ]
    ]
    data_safe_state: NotRequired[pulumi.Input[_builtins.str]]
    data_storage_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    data_storage_size_tb: NotRequired[pulumi.Input[_builtins.int]]
    database_management_state: NotRequired[pulumi.Input[_builtins.str]]
    db_edition: NotRequired[pulumi.Input[_builtins.str]]
    db_version: NotRequired[pulumi.Input[_builtins.str]]
    failed_data_recovery_duration: NotRequired[pulumi.Input[_builtins.str]]
    is_auto_scaling_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_local_data_guard_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_storage_auto_scaling_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    lifecycle_details: NotRequired[pulumi.Input[_builtins.str]]
    local_adg_auto_failover_max_data_loss_limit: NotRequired[
        pulumi.Input[_builtins.int]
    ]
    local_disaster_recovery_type: NotRequired[pulumi.Input[_builtins.str]]
    local_standby_dbs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutonomousDatabasePropertiesLocalStandbyDbArgsDict]]
        ]
    ]
    maintenance_begin_time: NotRequired[pulumi.Input[_builtins.str]]
    maintenance_end_time: NotRequired[pulumi.Input[_builtins.str]]
    maintenance_schedule_type: NotRequired[pulumi.Input[_builtins.str]]
    memory_per_oracle_compute_unit_gbs: NotRequired[pulumi.Input[_builtins.int]]
    memory_table_gbs: NotRequired[pulumi.Input[_builtins.int]]
    mtls_connection_required: NotRequired[pulumi.Input[_builtins.bool]]
    n_character_set: NotRequired[pulumi.Input[_builtins.str]]
    next_long_term_backup_time: NotRequired[pulumi.Input[_builtins.str]]
    oci_url: NotRequired[pulumi.Input[_builtins.str]]
    ocid: NotRequired[pulumi.Input[_builtins.str]]
    open_mode: NotRequired[pulumi.Input[_builtins.str]]
    operations_insights_state: NotRequired[pulumi.Input[_builtins.str]]
    peer_db_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    permission_level: NotRequired[pulumi.Input[_builtins.str]]
    private_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    private_endpoint_ip: NotRequired[pulumi.Input[_builtins.str]]
    private_endpoint_label: NotRequired[pulumi.Input[_builtins.str]]
    refreshable_mode: NotRequired[pulumi.Input[_builtins.str]]
    refreshable_state: NotRequired[pulumi.Input[_builtins.str]]
    role: NotRequired[pulumi.Input[_builtins.str]]
    scheduled_operation_details: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AutonomousDatabasePropertiesScheduledOperationDetailArgsDict
                ]
            ]
        ]
    ]
    secret_id: NotRequired[pulumi.Input[_builtins.str]]
    sql_web_developer_url: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    supported_clone_regions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    total_auto_backup_storage_size_gbs: NotRequired[pulumi.Input[_builtins.float]]
    used_data_storage_size_tbs: NotRequired[pulumi.Input[_builtins.int]]
    vault_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutonomousDatabasePropertiesArgs:
    def __init__(
        __self__,
        *,
        db_workload: pulumi.Input[_builtins.str],
        license_type: pulumi.Input[_builtins.str],
        actual_used_data_storage_size_tb: Optional[pulumi.Input[_builtins.float]] = ...,
        allocated_storage_size_tb: Optional[pulumi.Input[_builtins.float]] = ...,
        apex_details: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutonomousDatabasePropertiesApexDetailArgs]]
            ]
        ] = ...,
        are_primary_allowlisted_ips_used: Optional[pulumi.Input[_builtins.bool]] = ...,
        autonomous_container_database_id: Optional[pulumi.Input[_builtins.str]] = ...,
        available_upgrade_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        backup_retention_period_days: Optional[pulumi.Input[_builtins.int]] = ...,
        character_set: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_count: Optional[pulumi.Input[_builtins.float]] = ...,
        connection_strings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutonomousDatabasePropertiesConnectionStringArgs]]
            ]
        ] = ...,
        connection_urls: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutonomousDatabasePropertiesConnectionUrlArgs]]
            ]
        ] = ...,
        cpu_core_count: Optional[pulumi.Input[_builtins.int]] = ...,
        customer_contacts: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutonomousDatabasePropertiesCustomerContactArgs]]
            ]
        ] = ...,
        data_safe_state: Optional[pulumi.Input[_builtins.str]] = ...,
        data_storage_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        data_storage_size_tb: Optional[pulumi.Input[_builtins.int]] = ...,
        database_management_state: Optional[pulumi.Input[_builtins.str]] = ...,
        db_edition: Optional[pulumi.Input[_builtins.str]] = ...,
        db_version: Optional[pulumi.Input[_builtins.str]] = ...,
        failed_data_recovery_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        is_auto_scaling_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_local_data_guard_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_storage_auto_scaling_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        lifecycle_details: Optional[pulumi.Input[_builtins.str]] = ...,
        local_adg_auto_failover_max_data_loss_limit: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        local_disaster_recovery_type: Optional[pulumi.Input[_builtins.str]] = ...,
        local_standby_dbs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutonomousDatabasePropertiesLocalStandbyDbArgs]]
            ]
        ] = ...,
        maintenance_begin_time: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_schedule_type: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_per_oracle_compute_unit_gbs: Optional[pulumi.Input[_builtins.int]] = ...,
        memory_table_gbs: Optional[pulumi.Input[_builtins.int]] = ...,
        mtls_connection_required: Optional[pulumi.Input[_builtins.bool]] = ...,
        n_character_set: Optional[pulumi.Input[_builtins.str]] = ...,
        next_long_term_backup_time: Optional[pulumi.Input[_builtins.str]] = ...,
        oci_url: Optional[pulumi.Input[_builtins.str]] = ...,
        ocid: Optional[pulumi.Input[_builtins.str]] = ...,
        open_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        operations_insights_state: Optional[pulumi.Input[_builtins.str]] = ...,
        peer_db_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        permission_level: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoint_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        private_endpoint_label: Optional[pulumi.Input[_builtins.str]] = ...,
        refreshable_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        refreshable_state: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        scheduled_operation_details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutonomousDatabasePropertiesScheduledOperationDetailArgs
                    ]
                ]
            ]
        ] = ...,
        secret_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sql_web_developer_url: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        supported_clone_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        total_auto_backup_storage_size_gbs: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        used_data_storage_size_tbs: Optional[pulumi.Input[_builtins.int]] = ...,
        vault_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbWorkload")
    def db_workload(self) -> pulumi.Input[_builtins.str]: ...
    @db_workload.setter
    def db_workload(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Input[_builtins.str]: ...
    @license_type.setter
    def license_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="actualUsedDataStorageSizeTb")
    def actual_used_data_storage_size_tb(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @actual_used_data_storage_size_tb.setter
    def actual_used_data_storage_size_tb(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorageSizeTb")
    def allocated_storage_size_tb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @allocated_storage_size_tb.setter
    def allocated_storage_size_tb(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="apexDetails")
    def apex_details(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutonomousDatabasePropertiesApexDetailArgs]]]
    ]: ...
    @apex_details.setter
    def apex_details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutonomousDatabasePropertiesApexDetailArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="arePrimaryAllowlistedIpsUsed")
    def are_primary_allowlisted_ips_used(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @are_primary_allowlisted_ips_used.setter
    def are_primary_allowlisted_ips_used(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autonomousContainerDatabaseId")
    def autonomous_container_database_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @autonomous_container_database_id.setter
    def autonomous_container_database_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availableUpgradeVersions")
    def available_upgrade_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @available_upgrade_versions.setter
    def available_upgrade_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionPeriodDays")
    def backup_retention_period_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @backup_retention_period_days.setter
    def backup_retention_period_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="characterSet")
    def character_set(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @character_set.setter
    def character_set(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @compute_count.setter
    def compute_count(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionStrings")
    def connection_strings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AutonomousDatabasePropertiesConnectionStringArgs]]
        ]
    ]: ...
    @connection_strings.setter
    def connection_strings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutonomousDatabasePropertiesConnectionStringArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionUrls")
    def connection_urls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AutonomousDatabasePropertiesConnectionUrlArgs]]
        ]
    ]: ...
    @connection_urls.setter
    def connection_urls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutonomousDatabasePropertiesConnectionUrlArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpu_core_count.setter
    def cpu_core_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="customerContacts")
    def customer_contacts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AutonomousDatabasePropertiesCustomerContactArgs]]
        ]
    ]: ...
    @customer_contacts.setter
    def customer_contacts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutonomousDatabasePropertiesCustomerContactArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataSafeState")
    def data_safe_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_safe_state.setter
    def data_safe_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeGb")
    def data_storage_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_storage_size_gb.setter
    def data_storage_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeTb")
    def data_storage_size_tb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_storage_size_tb.setter
    def data_storage_size_tb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseManagementState")
    def database_management_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_management_state.setter
    def database_management_state(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbEdition")
    def db_edition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_edition.setter
    def db_edition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_version.setter
    def db_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failedDataRecoveryDuration")
    def failed_data_recovery_duration(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failed_data_recovery_duration.setter
    def failed_data_recovery_duration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isAutoScalingEnabled")
    def is_auto_scaling_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isLocalDataGuardEnabled")
    def is_local_data_guard_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_local_data_guard_enabled.setter
    def is_local_data_guard_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isStorageAutoScalingEnabled")
    def is_storage_auto_scaling_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_storage_auto_scaling_enabled.setter
    def is_storage_auto_scaling_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localAdgAutoFailoverMaxDataLossLimit")
    def local_adg_auto_failover_max_data_loss_limit(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @local_adg_auto_failover_max_data_loss_limit.setter
    def local_adg_auto_failover_max_data_loss_limit(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localDisasterRecoveryType")
    def local_disaster_recovery_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @local_disaster_recovery_type.setter
    def local_disaster_recovery_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="localStandbyDbs")
    def local_standby_dbs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AutonomousDatabasePropertiesLocalStandbyDbArgs]]
        ]
    ]: ...
    @local_standby_dbs.setter
    def local_standby_dbs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutonomousDatabasePropertiesLocalStandbyDbArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceBeginTime")
    def maintenance_begin_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_begin_time.setter
    def maintenance_begin_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceEndTime")
    def maintenance_end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_end_time.setter
    def maintenance_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceScheduleType")
    def maintenance_schedule_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_schedule_type.setter
    def maintenance_schedule_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="memoryPerOracleComputeUnitGbs")
    def memory_per_oracle_compute_unit_gbs(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory_per_oracle_compute_unit_gbs.setter
    def memory_per_oracle_compute_unit_gbs(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="memoryTableGbs")
    def memory_table_gbs(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory_table_gbs.setter
    def memory_table_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="mtlsConnectionRequired")
    def mtls_connection_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @mtls_connection_required.setter
    def mtls_connection_required(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nCharacterSet")
    def n_character_set(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @n_character_set.setter
    def n_character_set(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextLongTermBackupTime")
    def next_long_term_backup_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_long_term_backup_time.setter
    def next_long_term_backup_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oci_url.setter
    def oci_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ocid.setter
    def ocid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="openMode")
    def open_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @open_mode.setter
    def open_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="operationsInsightsState")
    def operations_insights_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operations_insights_state.setter
    def operations_insights_state(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peerDbIds")
    def peer_db_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @peer_db_ids.setter
    def peer_db_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="permissionLevel")
    def permission_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission_level.setter
    def permission_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointIp")
    def private_endpoint_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_endpoint_ip.setter
    def private_endpoint_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointLabel")
    def private_endpoint_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_endpoint_label.setter
    def private_endpoint_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshableMode")
    def refreshable_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @refreshable_mode.setter
    def refreshable_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshableState")
    def refreshable_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @refreshable_state.setter
    def refreshable_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduledOperationDetails")
    def scheduled_operation_details(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AutonomousDatabasePropertiesScheduledOperationDetailArgs]
            ]
        ]
    ]: ...
    @scheduled_operation_details.setter
    def scheduled_operation_details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutonomousDatabasePropertiesScheduledOperationDetailArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_id.setter
    def secret_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sqlWebDeveloperUrl")
    def sql_web_developer_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sql_web_developer_url.setter
    def sql_web_developer_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="supportedCloneRegions")
    def supported_clone_regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @supported_clone_regions.setter
    def supported_clone_regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="totalAutoBackupStorageSizeGbs")
    def total_auto_backup_storage_size_gbs(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @total_auto_backup_storage_size_gbs.setter
    def total_auto_backup_storage_size_gbs(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="usedDataStorageSizeTbs")
    def used_data_storage_size_tbs(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @used_data_storage_size_tbs.setter
    def used_data_storage_size_tbs(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vault_id.setter
    def vault_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutonomousDatabasePropertiesApexDetailArgsDict(TypedDict):
    apex_version: NotRequired[pulumi.Input[_builtins.str]]
    ords_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutonomousDatabasePropertiesApexDetailArgs:
    def __init__(
        __self__,
        *,
        apex_version: Optional[pulumi.Input[_builtins.str]] = ...,
        ords_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apexVersion")
    def apex_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apex_version.setter
    def apex_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ordsVersion")
    def ords_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ords_version.setter
    def ords_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutonomousDatabasePropertiesConnectionStringArgsDict(TypedDict):
    all_connection_strings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AutonomousDatabasePropertiesConnectionStringAllConnectionStringArgsDict
                ]
            ]
        ]
    ]
    dedicated: NotRequired[pulumi.Input[_builtins.str]]
    high: NotRequired[pulumi.Input[_builtins.str]]
    low: NotRequired[pulumi.Input[_builtins.str]]
    medium: NotRequired[pulumi.Input[_builtins.str]]
    profiles: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AutonomousDatabasePropertiesConnectionStringProfileArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AutonomousDatabasePropertiesConnectionStringArgs:
    def __init__(
        __self__,
        *,
        all_connection_strings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutonomousDatabasePropertiesConnectionStringAllConnectionStringArgs
                    ]
                ]
            ]
        ] = ...,
        dedicated: Optional[pulumi.Input[_builtins.str]] = ...,
        high: Optional[pulumi.Input[_builtins.str]] = ...,
        low: Optional[pulumi.Input[_builtins.str]] = ...,
        medium: Optional[pulumi.Input[_builtins.str]] = ...,
        profiles: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutonomousDatabasePropertiesConnectionStringProfileArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allConnectionStrings")
    def all_connection_strings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AutonomousDatabasePropertiesConnectionStringAllConnectionStringArgs
                ]
            ]
        ]
    ]: ...
    @all_connection_strings.setter
    def all_connection_strings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutonomousDatabasePropertiesConnectionStringAllConnectionStringArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dedicated(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dedicated.setter
    def dedicated(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def high(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @high.setter
    def high(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def low(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @low.setter
    def low(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @medium.setter
    def medium(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def profiles(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AutonomousDatabasePropertiesConnectionStringProfileArgs]
            ]
        ]
    ]: ...
    @profiles.setter
    def profiles(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutonomousDatabasePropertiesConnectionStringProfileArgs
                    ]
                ]
            ]
        ],
    ): ...

class AutonomousDatabasePropertiesConnectionStringAllConnectionStringArgsDict(
    TypedDict
):
    high: NotRequired[pulumi.Input[_builtins.str]]
    low: NotRequired[pulumi.Input[_builtins.str]]
    medium: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutonomousDatabasePropertiesConnectionStringAllConnectionStringArgs:
    def __init__(
        __self__,
        *,
        high: Optional[pulumi.Input[_builtins.str]] = ...,
        low: Optional[pulumi.Input[_builtins.str]] = ...,
        medium: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def high(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @high.setter
    def high(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def low(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @low.setter
    def low(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @medium.setter
    def medium(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutonomousDatabasePropertiesConnectionStringProfileArgsDict(TypedDict):
    consumer_group: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    host_format: NotRequired[pulumi.Input[_builtins.str]]
    is_regional: NotRequired[pulumi.Input[_builtins.bool]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    session_mode: NotRequired[pulumi.Input[_builtins.str]]
    syntax_format: NotRequired[pulumi.Input[_builtins.str]]
    tls_authentication: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutonomousDatabasePropertiesConnectionStringProfileArgs:
    def __init__(
        __self__,
        *,
        consumer_group: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        host_format: Optional[pulumi.Input[_builtins.str]] = ...,
        is_regional: Optional[pulumi.Input[_builtins.bool]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        session_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        syntax_format: Optional[pulumi.Input[_builtins.str]] = ...,
        tls_authentication: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_group.setter
    def consumer_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostFormat")
    def host_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_format.setter
    def host_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isRegional")
    def is_regional(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_regional.setter
    def is_regional(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionMode")
    def session_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_mode.setter
    def session_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="syntaxFormat")
    def syntax_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @syntax_format.setter
    def syntax_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tlsAuthentication")
    def tls_authentication(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tls_authentication.setter
    def tls_authentication(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutonomousDatabasePropertiesConnectionUrlArgsDict(TypedDict):
    apex_uri: NotRequired[pulumi.Input[_builtins.str]]
    database_transforms_uri: NotRequired[pulumi.Input[_builtins.str]]
    graph_studio_uri: NotRequired[pulumi.Input[_builtins.str]]
    machine_learning_notebook_uri: NotRequired[pulumi.Input[_builtins.str]]
    machine_learning_user_management_uri: NotRequired[pulumi.Input[_builtins.str]]
    mongo_db_uri: NotRequired[pulumi.Input[_builtins.str]]
    ords_uri: NotRequired[pulumi.Input[_builtins.str]]
    sql_dev_web_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutonomousDatabasePropertiesConnectionUrlArgs:
    def __init__(
        __self__,
        *,
        apex_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        database_transforms_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        graph_studio_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_learning_notebook_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_learning_user_management_uri: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        mongo_db_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        ords_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        sql_dev_web_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apexUri")
    def apex_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @apex_uri.setter
    def apex_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseTransformsUri")
    def database_transforms_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_transforms_uri.setter
    def database_transforms_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="graphStudioUri")
    def graph_studio_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @graph_studio_uri.setter
    def graph_studio_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="machineLearningNotebookUri")
    def machine_learning_notebook_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_learning_notebook_uri.setter
    def machine_learning_notebook_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="machineLearningUserManagementUri")
    def machine_learning_user_management_uri(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_learning_user_management_uri.setter
    def machine_learning_user_management_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mongoDbUri")
    def mongo_db_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mongo_db_uri.setter
    def mongo_db_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ordsUri")
    def ords_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ords_uri.setter
    def ords_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sqlDevWebUri")
    def sql_dev_web_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sql_dev_web_uri.setter
    def sql_dev_web_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutonomousDatabasePropertiesCustomerContactArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutonomousDatabasePropertiesCustomerContactArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]: ...
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): ...

class AutonomousDatabasePropertiesLocalStandbyDbArgsDict(TypedDict):
    data_guard_role_changed_time: NotRequired[pulumi.Input[_builtins.str]]
    disaster_recovery_role_changed_time: NotRequired[pulumi.Input[_builtins.str]]
    lag_time_duration: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_details: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutonomousDatabasePropertiesLocalStandbyDbArgs:
    def __init__(
        __self__,
        *,
        data_guard_role_changed_time: Optional[pulumi.Input[_builtins.str]] = ...,
        disaster_recovery_role_changed_time: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        lag_time_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        lifecycle_details: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataGuardRoleChangedTime")
    def data_guard_role_changed_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_guard_role_changed_time.setter
    def data_guard_role_changed_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disasterRecoveryRoleChangedTime")
    def disaster_recovery_role_changed_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disaster_recovery_role_changed_time.setter
    def disaster_recovery_role_changed_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lagTimeDuration")
    def lag_time_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lag_time_duration.setter
    def lag_time_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleDetails")
    def lifecycle_details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifecycle_details.setter
    def lifecycle_details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutonomousDatabasePropertiesScheduledOperationDetailArgsDict(TypedDict):
    day_of_week: NotRequired[pulumi.Input[_builtins.str]]
    start_times: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AutonomousDatabasePropertiesScheduledOperationDetailStartTimeArgsDict
                ]
            ]
        ]
    ]
    stop_times: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AutonomousDatabasePropertiesScheduledOperationDetailStopTimeArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class AutonomousDatabasePropertiesScheduledOperationDetailArgs:
    def __init__(
        __self__,
        *,
        day_of_week: Optional[pulumi.Input[_builtins.str]] = ...,
        start_times: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutonomousDatabasePropertiesScheduledOperationDetailStartTimeArgs
                    ]
                ]
            ]
        ] = ...,
        stop_times: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutonomousDatabasePropertiesScheduledOperationDetailStopTimeArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTimes")
    def start_times(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AutonomousDatabasePropertiesScheduledOperationDetailStartTimeArgs
                ]
            ]
        ]
    ]: ...
    @start_times.setter
    def start_times(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutonomousDatabasePropertiesScheduledOperationDetailStartTimeArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stopTimes")
    def stop_times(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AutonomousDatabasePropertiesScheduledOperationDetailStopTimeArgs
                ]
            ]
        ]
    ]: ...
    @stop_times.setter
    def stop_times(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutonomousDatabasePropertiesScheduledOperationDetailStopTimeArgs
                    ]
                ]
            ]
        ],
    ): ...

class AutonomousDatabasePropertiesScheduledOperationDetailStartTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AutonomousDatabasePropertiesScheduledOperationDetailStartTimeArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AutonomousDatabasePropertiesScheduledOperationDetailStopTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AutonomousDatabasePropertiesScheduledOperationDetailStopTimeArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AutonomousDatabaseSourceConfigArgsDict(TypedDict):
    automatic_backups_replication_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    autonomous_database: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutonomousDatabaseSourceConfigArgs:
    def __init__(
        __self__,
        *,
        automatic_backups_replication_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        autonomous_database: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticBackupsReplicationEnabled")
    def automatic_backups_replication_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @automatic_backups_replication_enabled.setter
    def automatic_backups_replication_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autonomousDatabase")
    def autonomous_database(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @autonomous_database.setter
    def autonomous_database(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CloudExadataInfrastructurePropertiesArgsDict(TypedDict):
    shape: pulumi.Input[_builtins.str]
    activated_storage_count: NotRequired[pulumi.Input[_builtins.int]]
    additional_storage_count: NotRequired[pulumi.Input[_builtins.int]]
    available_storage_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    compute_count: NotRequired[pulumi.Input[_builtins.int]]
    cpu_count: NotRequired[pulumi.Input[_builtins.int]]
    customer_contacts: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CloudExadataInfrastructurePropertiesCustomerContactArgsDict
                ]
            ]
        ]
    ]
    data_storage_size_tb: NotRequired[pulumi.Input[_builtins.float]]
    db_node_storage_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    db_server_version: NotRequired[pulumi.Input[_builtins.str]]
    maintenance_window: NotRequired[
        pulumi.Input[CloudExadataInfrastructurePropertiesMaintenanceWindowArgsDict]
    ]
    max_cpu_count: NotRequired[pulumi.Input[_builtins.int]]
    max_data_storage_tb: NotRequired[pulumi.Input[_builtins.float]]
    max_db_node_storage_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    max_memory_gb: NotRequired[pulumi.Input[_builtins.int]]
    memory_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    monthly_db_server_version: NotRequired[pulumi.Input[_builtins.str]]
    monthly_storage_server_version: NotRequired[pulumi.Input[_builtins.str]]
    next_maintenance_run_id: NotRequired[pulumi.Input[_builtins.str]]
    next_maintenance_run_time: NotRequired[pulumi.Input[_builtins.str]]
    next_security_maintenance_run_time: NotRequired[pulumi.Input[_builtins.str]]
    oci_url: NotRequired[pulumi.Input[_builtins.str]]
    ocid: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    storage_count: NotRequired[pulumi.Input[_builtins.int]]
    storage_server_version: NotRequired[pulumi.Input[_builtins.str]]
    total_storage_size_gb: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CloudExadataInfrastructurePropertiesArgs:
    def __init__(
        __self__,
        *,
        shape: pulumi.Input[_builtins.str],
        activated_storage_count: Optional[pulumi.Input[_builtins.int]] = ...,
        additional_storage_count: Optional[pulumi.Input[_builtins.int]] = ...,
        available_storage_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        compute_count: Optional[pulumi.Input[_builtins.int]] = ...,
        cpu_count: Optional[pulumi.Input[_builtins.int]] = ...,
        customer_contacts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CloudExadataInfrastructurePropertiesCustomerContactArgs
                    ]
                ]
            ]
        ] = ...,
        data_storage_size_tb: Optional[pulumi.Input[_builtins.float]] = ...,
        db_node_storage_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        db_server_version: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[
            pulumi.Input[CloudExadataInfrastructurePropertiesMaintenanceWindowArgs]
        ] = ...,
        max_cpu_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_data_storage_tb: Optional[pulumi.Input[_builtins.float]] = ...,
        max_db_node_storage_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        max_memory_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        memory_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        monthly_db_server_version: Optional[pulumi.Input[_builtins.str]] = ...,
        monthly_storage_server_version: Optional[pulumi.Input[_builtins.str]] = ...,
        next_maintenance_run_id: Optional[pulumi.Input[_builtins.str]] = ...,
        next_maintenance_run_time: Optional[pulumi.Input[_builtins.str]] = ...,
        next_security_maintenance_run_time: Optional[pulumi.Input[_builtins.str]] = ...,
        oci_url: Optional[pulumi.Input[_builtins.str]] = ...,
        ocid: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_count: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_server_version: Optional[pulumi.Input[_builtins.str]] = ...,
        total_storage_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> pulumi.Input[_builtins.str]: ...
    @shape.setter
    def shape(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="activatedStorageCount")
    def activated_storage_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @activated_storage_count.setter
    def activated_storage_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="additionalStorageCount")
    def additional_storage_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @additional_storage_count.setter
    def additional_storage_count(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availableStorageSizeGb")
    def available_storage_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @available_storage_size_gb.setter
    def available_storage_size_gb(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @compute_count.setter
    def compute_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpu_count.setter
    def cpu_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="customerContacts")
    def customer_contacts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[CloudExadataInfrastructurePropertiesCustomerContactArgs]
            ]
        ]
    ]: ...
    @customer_contacts.setter
    def customer_contacts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CloudExadataInfrastructurePropertiesCustomerContactArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeTb")
    def data_storage_size_tb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @data_storage_size_tb.setter
    def data_storage_size_tb(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeGb")
    def db_node_storage_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @db_node_storage_size_gb.setter
    def db_node_storage_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="dbServerVersion")
    def db_server_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_server_version.setter
    def db_server_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(
        self,
    ) -> Optional[
        pulumi.Input[CloudExadataInfrastructurePropertiesMaintenanceWindowArgs]
    ]: ...
    @maintenance_window.setter
    def maintenance_window(
        self,
        value: Optional[
            pulumi.Input[CloudExadataInfrastructurePropertiesMaintenanceWindowArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxCpuCount")
    def max_cpu_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_cpu_count.setter
    def max_cpu_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxDataStorageTb")
    def max_data_storage_tb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_data_storage_tb.setter
    def max_data_storage_tb(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="maxDbNodeStorageSizeGb")
    def max_db_node_storage_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_db_node_storage_size_gb.setter
    def max_db_node_storage_size_gb(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxMemoryGb")
    def max_memory_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_memory_gb.setter
    def max_memory_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory_size_gb.setter
    def memory_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="monthlyDbServerVersion")
    def monthly_db_server_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @monthly_db_server_version.setter
    def monthly_db_server_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="monthlyStorageServerVersion")
    def monthly_storage_server_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @monthly_storage_server_version.setter
    def monthly_storage_server_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nextMaintenanceRunId")
    def next_maintenance_run_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_maintenance_run_id.setter
    def next_maintenance_run_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nextMaintenanceRunTime")
    def next_maintenance_run_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_maintenance_run_time.setter
    def next_maintenance_run_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nextSecurityMaintenanceRunTime")
    def next_security_maintenance_run_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_security_maintenance_run_time.setter
    def next_security_maintenance_run_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oci_url.setter
    def oci_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ocid.setter
    def ocid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageCount")
    def storage_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_count.setter
    def storage_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="storageServerVersion")
    def storage_server_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_server_version.setter
    def storage_server_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="totalStorageSizeGb")
    def total_storage_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total_storage_size_gb.setter
    def total_storage_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CloudExadataInfrastructurePropertiesCustomerContactArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]

@pulumi.input_type
class CloudExadataInfrastructurePropertiesCustomerContactArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]: ...
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): ...

class CloudExadataInfrastructurePropertiesMaintenanceWindowArgsDict(TypedDict):
    custom_action_timeout_mins: NotRequired[pulumi.Input[_builtins.int]]
    days_of_weeks: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    hours_of_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    is_custom_action_timeout_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    lead_time_week: NotRequired[pulumi.Input[_builtins.int]]
    months: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    patching_mode: NotRequired[pulumi.Input[_builtins.str]]
    preference: NotRequired[pulumi.Input[_builtins.str]]
    weeks_of_months: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]

@pulumi.input_type
class CloudExadataInfrastructurePropertiesMaintenanceWindowArgs:
    def __init__(
        __self__,
        *,
        custom_action_timeout_mins: Optional[pulumi.Input[_builtins.int]] = ...,
        days_of_weeks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        hours_of_days: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        is_custom_action_timeout_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        lead_time_week: Optional[pulumi.Input[_builtins.int]] = ...,
        months: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        patching_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        preference: Optional[pulumi.Input[_builtins.str]] = ...,
        weeks_of_months: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customActionTimeoutMins")
    def custom_action_timeout_mins(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @custom_action_timeout_mins.setter
    def custom_action_timeout_mins(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @days_of_weeks.setter
    def days_of_weeks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hoursOfDays")
    def hours_of_days(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @hours_of_days.setter
    def hours_of_days(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isCustomActionTimeoutEnabled")
    def is_custom_action_timeout_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_custom_action_timeout_enabled.setter
    def is_custom_action_timeout_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="leadTimeWeek")
    def lead_time_week(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @lead_time_week.setter
    def lead_time_week(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def months(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @months.setter
    def months(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="patchingMode")
    def patching_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @patching_mode.setter
    def patching_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def preference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preference.setter
    def preference(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="weeksOfMonths")
    def weeks_of_months(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @weeks_of_months.setter
    def weeks_of_months(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class CloudVmClusterPropertiesArgsDict(TypedDict):
    cpu_core_count: pulumi.Input[_builtins.int]
    license_type: pulumi.Input[_builtins.str]
    cluster_name: NotRequired[pulumi.Input[_builtins.str]]
    compartment_id: NotRequired[pulumi.Input[_builtins.str]]
    data_storage_size_tb: NotRequired[pulumi.Input[_builtins.float]]
    db_node_storage_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    db_server_ocids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    diagnostics_data_collection_options: NotRequired[
        pulumi.Input[CloudVmClusterPropertiesDiagnosticsDataCollectionOptionsArgsDict]
    ]
    disk_redundancy: NotRequired[pulumi.Input[_builtins.str]]
    dns_listener_ip: NotRequired[pulumi.Input[_builtins.str]]
    domain: NotRequired[pulumi.Input[_builtins.str]]
    gi_version: NotRequired[pulumi.Input[_builtins.str]]
    hostname: NotRequired[pulumi.Input[_builtins.str]]
    hostname_prefix: NotRequired[pulumi.Input[_builtins.str]]
    local_backup_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    memory_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    node_count: NotRequired[pulumi.Input[_builtins.int]]
    oci_url: NotRequired[pulumi.Input[_builtins.str]]
    ocid: NotRequired[pulumi.Input[_builtins.str]]
    ocpu_count: NotRequired[pulumi.Input[_builtins.float]]
    scan_dns: NotRequired[pulumi.Input[_builtins.str]]
    scan_dns_record_id: NotRequired[pulumi.Input[_builtins.str]]
    scan_ip_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    scan_listener_port_tcp: NotRequired[pulumi.Input[_builtins.int]]
    scan_listener_port_tcp_ssl: NotRequired[pulumi.Input[_builtins.int]]
    shape: NotRequired[pulumi.Input[_builtins.str]]
    sparse_diskgroup_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ssh_public_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    storage_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    system_version: NotRequired[pulumi.Input[_builtins.str]]
    time_zone: NotRequired[pulumi.Input[CloudVmClusterPropertiesTimeZoneArgsDict]]

@pulumi.input_type
class CloudVmClusterPropertiesArgs:
    def __init__(
        __self__,
        *,
        cpu_core_count: pulumi.Input[_builtins.int],
        license_type: pulumi.Input[_builtins.str],
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        compartment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        data_storage_size_tb: Optional[pulumi.Input[_builtins.float]] = ...,
        db_node_storage_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        db_server_ocids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        diagnostics_data_collection_options: Optional[
            pulumi.Input[CloudVmClusterPropertiesDiagnosticsDataCollectionOptionsArgs]
        ] = ...,
        disk_redundancy: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_listener_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        gi_version: Optional[pulumi.Input[_builtins.str]] = ...,
        hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        hostname_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        local_backup_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        memory_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        oci_url: Optional[pulumi.Input[_builtins.str]] = ...,
        ocid: Optional[pulumi.Input[_builtins.str]] = ...,
        ocpu_count: Optional[pulumi.Input[_builtins.float]] = ...,
        scan_dns: Optional[pulumi.Input[_builtins.str]] = ...,
        scan_dns_record_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scan_ip_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        scan_listener_port_tcp: Optional[pulumi.Input[_builtins.int]] = ...,
        scan_listener_port_tcp_ssl: Optional[pulumi.Input[_builtins.int]] = ...,
        shape: Optional[pulumi.Input[_builtins.str]] = ...,
        sparse_diskgroup_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ssh_public_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        system_version: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[pulumi.Input[CloudVmClusterPropertiesTimeZoneArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuCoreCount")
    def cpu_core_count(self) -> pulumi.Input[_builtins.int]: ...
    @cpu_core_count.setter
    def cpu_core_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Input[_builtins.str]: ...
    @license_type.setter
    def license_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="compartmentId")
    def compartment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compartment_id.setter
    def compartment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeTb")
    def data_storage_size_tb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @data_storage_size_tb.setter
    def data_storage_size_tb(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="dbNodeStorageSizeGb")
    def db_node_storage_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @db_node_storage_size_gb.setter
    def db_node_storage_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="dbServerOcids")
    def db_server_ocids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @db_server_ocids.setter
    def db_server_ocids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsDataCollectionOptions")
    def diagnostics_data_collection_options(
        self,
    ) -> Optional[
        pulumi.Input[CloudVmClusterPropertiesDiagnosticsDataCollectionOptionsArgs]
    ]: ...
    @diagnostics_data_collection_options.setter
    def diagnostics_data_collection_options(
        self,
        value: Optional[
            pulumi.Input[CloudVmClusterPropertiesDiagnosticsDataCollectionOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskRedundancy")
    def disk_redundancy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_redundancy.setter
    def disk_redundancy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsListenerIp")
    def dns_listener_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_listener_ip.setter
    def dns_listener_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="giVersion")
    def gi_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gi_version.setter
    def gi_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hostname_prefix.setter
    def hostname_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localBackupEnabled")
    def local_backup_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @local_backup_enabled.setter
    def local_backup_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory_size_gb.setter
    def memory_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oci_url.setter
    def oci_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ocid.setter
    def ocid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ocpuCount")
    def ocpu_count(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @ocpu_count.setter
    def ocpu_count(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="scanDns")
    def scan_dns(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scan_dns.setter
    def scan_dns(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scanDnsRecordId")
    def scan_dns_record_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scan_dns_record_id.setter
    def scan_dns_record_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scanIpIds")
    def scan_ip_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scan_ip_ids.setter
    def scan_ip_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcp")
    def scan_listener_port_tcp(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scan_listener_port_tcp.setter
    def scan_listener_port_tcp(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcpSsl")
    def scan_listener_port_tcp_ssl(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scan_listener_port_tcp_ssl.setter
    def scan_listener_port_tcp_ssl(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shape.setter
    def shape(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sparseDiskgroupEnabled")
    def sparse_diskgroup_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @sparse_diskgroup_enabled.setter
    def sparse_diskgroup_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ssh_public_keys.setter
    def ssh_public_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageSizeGb")
    def storage_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_size_gb.setter
    def storage_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="systemVersion")
    def system_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @system_version.setter
    def system_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(
        self,
    ) -> Optional[pulumi.Input[CloudVmClusterPropertiesTimeZoneArgs]]: ...
    @time_zone.setter
    def time_zone(
        self, value: Optional[pulumi.Input[CloudVmClusterPropertiesTimeZoneArgs]]
    ): ...

class CloudVmClusterPropertiesDiagnosticsDataCollectionOptionsArgsDict(TypedDict):
    diagnostics_events_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    health_monitoring_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    incident_logs_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class CloudVmClusterPropertiesDiagnosticsDataCollectionOptionsArgs:
    def __init__(
        __self__,
        *,
        diagnostics_events_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        health_monitoring_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        incident_logs_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diagnosticsEventsEnabled")
    def diagnostics_events_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @diagnostics_events_enabled.setter
    def diagnostics_events_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthMonitoringEnabled")
    def health_monitoring_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @health_monitoring_enabled.setter
    def health_monitoring_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="incidentLogsEnabled")
    def incident_logs_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @incident_logs_enabled.setter
    def incident_logs_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class CloudVmClusterPropertiesTimeZoneArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CloudVmClusterPropertiesTimeZoneArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DbSystemPropertiesArgsDict(TypedDict):
    compute_count: pulumi.Input[_builtins.int]
    database_edition: pulumi.Input[_builtins.str]
    initial_data_storage_size_gb: pulumi.Input[_builtins.int]
    license_model: pulumi.Input[_builtins.str]
    shape: pulumi.Input[_builtins.str]
    ssh_public_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    compute_model: NotRequired[pulumi.Input[_builtins.str]]
    data_collection_options: NotRequired[
        pulumi.Input[DbSystemPropertiesDataCollectionOptionsArgsDict]
    ]
    data_storage_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    db_home: NotRequired[pulumi.Input[DbSystemPropertiesDbHomeArgsDict]]
    db_system_options: NotRequired[
        pulumi.Input[DbSystemPropertiesDbSystemOptionsArgsDict]
    ]
    domain: NotRequired[pulumi.Input[_builtins.str]]
    hostname: NotRequired[pulumi.Input[_builtins.str]]
    hostname_prefix: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_state: NotRequired[pulumi.Input[_builtins.str]]
    memory_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    node_count: NotRequired[pulumi.Input[_builtins.int]]
    ocid: NotRequired[pulumi.Input[_builtins.str]]
    private_ip: NotRequired[pulumi.Input[_builtins.str]]
    reco_storage_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    time_zone: NotRequired[pulumi.Input[DbSystemPropertiesTimeZoneArgsDict]]

@pulumi.input_type
class DbSystemPropertiesArgs:
    def __init__(
        __self__,
        *,
        compute_count: pulumi.Input[_builtins.int],
        database_edition: pulumi.Input[_builtins.str],
        initial_data_storage_size_gb: pulumi.Input[_builtins.int],
        license_model: pulumi.Input[_builtins.str],
        shape: pulumi.Input[_builtins.str],
        ssh_public_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        compute_model: Optional[pulumi.Input[_builtins.str]] = ...,
        data_collection_options: Optional[
            pulumi.Input[DbSystemPropertiesDataCollectionOptionsArgs]
        ] = ...,
        data_storage_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        db_home: Optional[pulumi.Input[DbSystemPropertiesDbHomeArgs]] = ...,
        db_system_options: Optional[
            pulumi.Input[DbSystemPropertiesDbSystemOptionsArgs]
        ] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        hostname_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        lifecycle_state: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        ocid: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        reco_storage_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        time_zone: Optional[pulumi.Input[DbSystemPropertiesTimeZoneArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeCount")
    def compute_count(self) -> pulumi.Input[_builtins.int]: ...
    @compute_count.setter
    def compute_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="databaseEdition")
    def database_edition(self) -> pulumi.Input[_builtins.str]: ...
    @database_edition.setter
    def database_edition(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="initialDataStorageSizeGb")
    def initial_data_storage_size_gb(self) -> pulumi.Input[_builtins.int]: ...
    @initial_data_storage_size_gb.setter
    def initial_data_storage_size_gb(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> pulumi.Input[_builtins.str]: ...
    @license_model.setter
    def license_model(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> pulumi.Input[_builtins.str]: ...
    @shape.setter
    def shape(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @ssh_public_keys.setter
    def ssh_public_keys(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="computeModel")
    def compute_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_model.setter
    def compute_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionOptions")
    def data_collection_options(
        self,
    ) -> Optional[pulumi.Input[DbSystemPropertiesDataCollectionOptionsArgs]]: ...
    @data_collection_options.setter
    def data_collection_options(
        self, value: Optional[pulumi.Input[DbSystemPropertiesDataCollectionOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataStorageSizeGb")
    def data_storage_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @data_storage_size_gb.setter
    def data_storage_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="dbHome")
    def db_home(self) -> Optional[pulumi.Input[DbSystemPropertiesDbHomeArgs]]: ...
    @db_home.setter
    def db_home(self, value: Optional[pulumi.Input[DbSystemPropertiesDbHomeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="dbSystemOptions")
    def db_system_options(
        self,
    ) -> Optional[pulumi.Input[DbSystemPropertiesDbSystemOptionsArgs]]: ...
    @db_system_options.setter
    def db_system_options(
        self, value: Optional[pulumi.Input[DbSystemPropertiesDbSystemOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hostname_prefix.setter
    def hostname_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifecycle_state.setter
    def lifecycle_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory_size_gb.setter
    def memory_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ocid.setter
    def ocid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIp")
    def private_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ip.setter
    def private_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recoStorageSizeGb")
    def reco_storage_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @reco_storage_size_gb.setter
    def reco_storage_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[DbSystemPropertiesTimeZoneArgs]]: ...
    @time_zone.setter
    def time_zone(
        self, value: Optional[pulumi.Input[DbSystemPropertiesTimeZoneArgs]]
    ): ...

class DbSystemPropertiesDataCollectionOptionsArgsDict(TypedDict):
    is_diagnostics_events_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_incident_logs_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DbSystemPropertiesDataCollectionOptionsArgs:
    def __init__(
        __self__,
        *,
        is_diagnostics_events_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_incident_logs_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isDiagnosticsEventsEnabled")
    def is_diagnostics_events_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_diagnostics_events_enabled.setter
    def is_diagnostics_events_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isIncidentLogsEnabled")
    def is_incident_logs_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_incident_logs_enabled.setter
    def is_incident_logs_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class DbSystemPropertiesDbHomeArgsDict(TypedDict):
    database: pulumi.Input[DbSystemPropertiesDbHomeDatabaseArgsDict]
    db_version: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    is_unified_auditing_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DbSystemPropertiesDbHomeArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[DbSystemPropertiesDbHomeDatabaseArgs],
        db_version: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        is_unified_auditing_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[DbSystemPropertiesDbHomeDatabaseArgs]: ...
    @database.setter
    def database(self, value: pulumi.Input[DbSystemPropertiesDbHomeDatabaseArgs]): ...
    @_builtins.property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> pulumi.Input[_builtins.str]: ...
    @db_version.setter
    def db_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isUnifiedAuditingEnabled")
    def is_unified_auditing_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_unified_auditing_enabled.setter
    def is_unified_auditing_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class DbSystemPropertiesDbHomeDatabaseArgsDict(TypedDict):
    admin_password: pulumi.Input[_builtins.str]
    database_id: pulumi.Input[_builtins.str]
    character_set: NotRequired[pulumi.Input[_builtins.str]]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    db_home_name: NotRequired[pulumi.Input[_builtins.str]]
    db_name: NotRequired[pulumi.Input[_builtins.str]]
    db_unique_name: NotRequired[pulumi.Input[_builtins.str]]
    gcp_oracle_zone: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ncharacter_set: NotRequired[pulumi.Input[_builtins.str]]
    oci_url: NotRequired[pulumi.Input[_builtins.str]]
    ops_insights_status: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[
        pulumi.Input[DbSystemPropertiesDbHomeDatabasePropertiesArgsDict]
    ]
    tde_wallet_password: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DbSystemPropertiesDbHomeDatabaseArgs:
    def __init__(
        __self__,
        *,
        admin_password: pulumi.Input[_builtins.str],
        database_id: pulumi.Input[_builtins.str],
        character_set: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        db_home_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_name: Optional[pulumi.Input[_builtins.str]] = ...,
        db_unique_name: Optional[pulumi.Input[_builtins.str]] = ...,
        gcp_oracle_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ncharacter_set: Optional[pulumi.Input[_builtins.str]] = ...,
        oci_url: Optional[pulumi.Input[_builtins.str]] = ...,
        ops_insights_status: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[DbSystemPropertiesDbHomeDatabasePropertiesArgs]
        ] = ...,
        tde_wallet_password: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> pulumi.Input[_builtins.str]: ...
    @admin_password.setter
    def admin_password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> pulumi.Input[_builtins.str]: ...
    @database_id.setter
    def database_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="characterSet")
    def character_set(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @character_set.setter
    def character_set(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbHomeName")
    def db_home_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_home_name.setter
    def db_home_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_name.setter
    def db_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbUniqueName")
    def db_unique_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_unique_name.setter
    def db_unique_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcpOracleZone")
    def gcp_oracle_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_oracle_zone.setter
    def gcp_oracle_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ncharacterSet")
    def ncharacter_set(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ncharacter_set.setter
    def ncharacter_set(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ociUrl")
    def oci_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oci_url.setter
    def oci_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="opsInsightsStatus")
    def ops_insights_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ops_insights_status.setter
    def ops_insights_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[DbSystemPropertiesDbHomeDatabasePropertiesArgs]]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[pulumi.Input[DbSystemPropertiesDbHomeDatabasePropertiesArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tdeWalletPassword")
    def tde_wallet_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tde_wallet_password.setter
    def tde_wallet_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DbSystemPropertiesDbHomeDatabasePropertiesArgsDict(TypedDict):
    db_version: pulumi.Input[_builtins.str]
    database_management_config: NotRequired[
        pulumi.Input[
            DbSystemPropertiesDbHomeDatabasePropertiesDatabaseManagementConfigArgsDict
        ]
    ]
    db_backup_config: NotRequired[
        pulumi.Input[DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigArgsDict]
    ]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DbSystemPropertiesDbHomeDatabasePropertiesArgs:
    def __init__(
        __self__,
        *,
        db_version: pulumi.Input[_builtins.str],
        database_management_config: Optional[
            pulumi.Input[
                DbSystemPropertiesDbHomeDatabasePropertiesDatabaseManagementConfigArgs
            ]
        ] = ...,
        db_backup_config: Optional[
            pulumi.Input[DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigArgs]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbVersion")
    def db_version(self) -> pulumi.Input[_builtins.str]: ...
    @db_version.setter
    def db_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseManagementConfig")
    def database_management_config(
        self,
    ) -> Optional[
        pulumi.Input[
            DbSystemPropertiesDbHomeDatabasePropertiesDatabaseManagementConfigArgs
        ]
    ]: ...
    @database_management_config.setter
    def database_management_config(
        self,
        value: Optional[
            pulumi.Input[
                DbSystemPropertiesDbHomeDatabasePropertiesDatabaseManagementConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbBackupConfig")
    def db_backup_config(
        self,
    ) -> Optional[
        pulumi.Input[DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigArgs]
    ]: ...
    @db_backup_config.setter
    def db_backup_config(
        self,
        value: Optional[
            pulumi.Input[DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DbSystemPropertiesDbHomeDatabasePropertiesDatabaseManagementConfigArgsDict(
    TypedDict
):
    management_state: NotRequired[pulumi.Input[_builtins.str]]
    management_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DbSystemPropertiesDbHomeDatabasePropertiesDatabaseManagementConfigArgs:
    def __init__(
        __self__,
        *,
        management_state: Optional[pulumi.Input[_builtins.str]] = ...,
        management_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managementState")
    def management_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @management_state.setter
    def management_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managementType")
    def management_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @management_type.setter
    def management_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigArgsDict(TypedDict):
    auto_backup_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    auto_full_backup_day: NotRequired[pulumi.Input[_builtins.str]]
    auto_full_backup_window: NotRequired[pulumi.Input[_builtins.str]]
    auto_incremental_backup_window: NotRequired[pulumi.Input[_builtins.str]]
    backup_deletion_policy: NotRequired[pulumi.Input[_builtins.str]]
    backup_destination_details: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigBackupDestinationDetailArgsDict
                ]
            ]
        ]
    ]
    retention_period_days: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigArgs:
    def __init__(
        __self__,
        *,
        auto_backup_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_full_backup_day: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_full_backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_incremental_backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_destination_details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigBackupDestinationDetailArgs
                    ]
                ]
            ]
        ] = ...,
        retention_period_days: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoBackupEnabled")
    def auto_backup_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_backup_enabled.setter
    def auto_backup_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="autoFullBackupDay")
    def auto_full_backup_day(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_full_backup_day.setter
    def auto_full_backup_day(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoFullBackupWindow")
    def auto_full_backup_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_full_backup_window.setter
    def auto_full_backup_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoIncrementalBackupWindow")
    def auto_incremental_backup_window(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_incremental_backup_window.setter
    def auto_incremental_backup_window(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupDeletionPolicy")
    def backup_deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_deletion_policy.setter
    def backup_deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupDestinationDetails")
    def backup_destination_details(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigBackupDestinationDetailArgs
                ]
            ]
        ]
    ]: ...
    @backup_destination_details.setter
    def backup_destination_details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigBackupDestinationDetailArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriodDays")
    def retention_period_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_period_days.setter
    def retention_period_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigBackupDestinationDetailArgsDict(
    TypedDict
):
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DbSystemPropertiesDbHomeDatabasePropertiesDbBackupConfigBackupDestinationDetailArgs:
    def __init__(
        __self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DbSystemPropertiesDbSystemOptionsArgsDict(TypedDict):
    storage_management: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DbSystemPropertiesDbSystemOptionsArgs:
    def __init__(
        __self__, *, storage_management: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageManagement")
    def storage_management(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_management.setter
    def storage_management(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DbSystemPropertiesTimeZoneArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DbSystemPropertiesTimeZoneArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExadbVmClusterPropertiesArgsDict(TypedDict):
    enabled_ecpu_count_per_node: pulumi.Input[_builtins.int]
    exascale_db_storage_vault: pulumi.Input[_builtins.str]
    grid_image_id: pulumi.Input[_builtins.str]
    hostname_prefix: pulumi.Input[_builtins.str]
    node_count: pulumi.Input[_builtins.int]
    shape_attribute: pulumi.Input[_builtins.str]
    ssh_public_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vm_file_system_storage: pulumi.Input[
        ExadbVmClusterPropertiesVmFileSystemStorageArgsDict
    ]
    additional_ecpu_count_per_node: NotRequired[pulumi.Input[_builtins.int]]
    cluster_name: NotRequired[pulumi.Input[_builtins.str]]
    data_collection_options: NotRequired[
        pulumi.Input[ExadbVmClusterPropertiesDataCollectionOptionsArgsDict]
    ]
    gi_version: NotRequired[pulumi.Input[_builtins.str]]
    hostname: NotRequired[pulumi.Input[_builtins.str]]
    license_model: NotRequired[pulumi.Input[_builtins.str]]
    lifecycle_state: NotRequired[pulumi.Input[_builtins.str]]
    memory_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    oci_uri: NotRequired[pulumi.Input[_builtins.str]]
    scan_listener_port_tcp: NotRequired[pulumi.Input[_builtins.int]]
    time_zone: NotRequired[pulumi.Input[ExadbVmClusterPropertiesTimeZoneArgsDict]]

@pulumi.input_type
class ExadbVmClusterPropertiesArgs:
    def __init__(
        __self__,
        *,
        enabled_ecpu_count_per_node: pulumi.Input[_builtins.int],
        exascale_db_storage_vault: pulumi.Input[_builtins.str],
        grid_image_id: pulumi.Input[_builtins.str],
        hostname_prefix: pulumi.Input[_builtins.str],
        node_count: pulumi.Input[_builtins.int],
        shape_attribute: pulumi.Input[_builtins.str],
        ssh_public_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        vm_file_system_storage: pulumi.Input[
            ExadbVmClusterPropertiesVmFileSystemStorageArgs
        ],
        additional_ecpu_count_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        data_collection_options: Optional[
            pulumi.Input[ExadbVmClusterPropertiesDataCollectionOptionsArgs]
        ] = ...,
        gi_version: Optional[pulumi.Input[_builtins.str]] = ...,
        hostname: Optional[pulumi.Input[_builtins.str]] = ...,
        license_model: Optional[pulumi.Input[_builtins.str]] = ...,
        lifecycle_state: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        oci_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        scan_listener_port_tcp: Optional[pulumi.Input[_builtins.int]] = ...,
        time_zone: Optional[pulumi.Input[ExadbVmClusterPropertiesTimeZoneArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledEcpuCountPerNode")
    def enabled_ecpu_count_per_node(self) -> pulumi.Input[_builtins.int]: ...
    @enabled_ecpu_count_per_node.setter
    def enabled_ecpu_count_per_node(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="exascaleDbStorageVault")
    def exascale_db_storage_vault(self) -> pulumi.Input[_builtins.str]: ...
    @exascale_db_storage_vault.setter
    def exascale_db_storage_vault(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gridImageId")
    def grid_image_id(self) -> pulumi.Input[_builtins.str]: ...
    @grid_image_id.setter
    def grid_image_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> pulumi.Input[_builtins.str]: ...
    @hostname_prefix.setter
    def hostname_prefix(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Input[_builtins.int]: ...
    @node_count.setter
    def node_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="shapeAttribute")
    def shape_attribute(self) -> pulumi.Input[_builtins.str]: ...
    @shape_attribute.setter
    def shape_attribute(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @ssh_public_keys.setter
    def ssh_public_keys(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmFileSystemStorage")
    def vm_file_system_storage(
        self,
    ) -> pulumi.Input[ExadbVmClusterPropertiesVmFileSystemStorageArgs]: ...
    @vm_file_system_storage.setter
    def vm_file_system_storage(
        self, value: pulumi.Input[ExadbVmClusterPropertiesVmFileSystemStorageArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalEcpuCountPerNode")
    def additional_ecpu_count_per_node(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @additional_ecpu_count_per_node.setter
    def additional_ecpu_count_per_node(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionOptions")
    def data_collection_options(
        self,
    ) -> Optional[pulumi.Input[ExadbVmClusterPropertiesDataCollectionOptionsArgs]]: ...
    @data_collection_options.setter
    def data_collection_options(
        self,
        value: Optional[
            pulumi.Input[ExadbVmClusterPropertiesDataCollectionOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="giVersion")
    def gi_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gi_version.setter
    def gi_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @license_model.setter
    def license_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifecycle_state.setter
    def lifecycle_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory_size_gb.setter
    def memory_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ociUri")
    def oci_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oci_uri.setter
    def oci_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scanListenerPortTcp")
    def scan_listener_port_tcp(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scan_listener_port_tcp.setter
    def scan_listener_port_tcp(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(
        self,
    ) -> Optional[pulumi.Input[ExadbVmClusterPropertiesTimeZoneArgs]]: ...
    @time_zone.setter
    def time_zone(
        self, value: Optional[pulumi.Input[ExadbVmClusterPropertiesTimeZoneArgs]]
    ): ...

class ExadbVmClusterPropertiesDataCollectionOptionsArgsDict(TypedDict):
    is_diagnostics_events_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_health_monitoring_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_incident_logs_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ExadbVmClusterPropertiesDataCollectionOptionsArgs:
    def __init__(
        __self__,
        *,
        is_diagnostics_events_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_health_monitoring_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_incident_logs_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isDiagnosticsEventsEnabled")
    def is_diagnostics_events_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_diagnostics_events_enabled.setter
    def is_diagnostics_events_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isHealthMonitoringEnabled")
    def is_health_monitoring_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_health_monitoring_enabled.setter
    def is_health_monitoring_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isIncidentLogsEnabled")
    def is_incident_logs_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_incident_logs_enabled.setter
    def is_incident_logs_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ExadbVmClusterPropertiesTimeZoneArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExadbVmClusterPropertiesTimeZoneArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExadbVmClusterPropertiesVmFileSystemStorageArgsDict(TypedDict):
    size_in_gbs_per_node: pulumi.Input[_builtins.int]

@pulumi.input_type
class ExadbVmClusterPropertiesVmFileSystemStorageArgs:
    def __init__(
        __self__, *, size_in_gbs_per_node: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeInGbsPerNode")
    def size_in_gbs_per_node(self) -> pulumi.Input[_builtins.int]: ...
    @size_in_gbs_per_node.setter
    def size_in_gbs_per_node(self, value: pulumi.Input[_builtins.int]): ...

class ExascaleDbStorageVaultPropertiesArgsDict(TypedDict):
    exascale_db_storage_details: pulumi.Input[
        ExascaleDbStorageVaultPropertiesExascaleDbStorageDetailsArgsDict
    ]
    additional_flash_cache_percent: NotRequired[pulumi.Input[_builtins.int]]
    attached_shape_attributes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    available_shape_attributes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    oci_uri: NotRequired[pulumi.Input[_builtins.str]]
    ocid: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    time_zone: NotRequired[
        pulumi.Input[ExascaleDbStorageVaultPropertiesTimeZoneArgsDict]
    ]
    vm_cluster_count: NotRequired[pulumi.Input[_builtins.int]]
    vm_cluster_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ExascaleDbStorageVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        exascale_db_storage_details: pulumi.Input[
            ExascaleDbStorageVaultPropertiesExascaleDbStorageDetailsArgs
        ],
        additional_flash_cache_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        attached_shape_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        available_shape_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        oci_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        ocid: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone: Optional[
            pulumi.Input[ExascaleDbStorageVaultPropertiesTimeZoneArgs]
        ] = ...,
        vm_cluster_count: Optional[pulumi.Input[_builtins.int]] = ...,
        vm_cluster_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exascaleDbStorageDetails")
    def exascale_db_storage_details(
        self,
    ) -> pulumi.Input[ExascaleDbStorageVaultPropertiesExascaleDbStorageDetailsArgs]: ...
    @exascale_db_storage_details.setter
    def exascale_db_storage_details(
        self,
        value: pulumi.Input[
            ExascaleDbStorageVaultPropertiesExascaleDbStorageDetailsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalFlashCachePercent")
    def additional_flash_cache_percent(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @additional_flash_cache_percent.setter
    def additional_flash_cache_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="attachedShapeAttributes")
    def attached_shape_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @attached_shape_attributes.setter
    def attached_shape_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availableShapeAttributes")
    def available_shape_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @available_shape_attributes.setter
    def available_shape_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ociUri")
    def oci_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oci_uri.setter
    def oci_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ocid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ocid.setter
    def ocid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(
        self,
    ) -> Optional[pulumi.Input[ExascaleDbStorageVaultPropertiesTimeZoneArgs]]: ...
    @time_zone.setter
    def time_zone(
        self,
        value: Optional[pulumi.Input[ExascaleDbStorageVaultPropertiesTimeZoneArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmClusterCount")
    def vm_cluster_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @vm_cluster_count.setter
    def vm_cluster_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="vmClusterIds")
    def vm_cluster_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vm_cluster_ids.setter
    def vm_cluster_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ExascaleDbStorageVaultPropertiesExascaleDbStorageDetailsArgsDict(TypedDict):
    total_size_gbs: pulumi.Input[_builtins.int]
    available_size_gbs: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ExascaleDbStorageVaultPropertiesExascaleDbStorageDetailsArgs:
    def __init__(
        __self__,
        *,
        total_size_gbs: pulumi.Input[_builtins.int],
        available_size_gbs: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalSizeGbs")
    def total_size_gbs(self) -> pulumi.Input[_builtins.int]: ...
    @total_size_gbs.setter
    def total_size_gbs(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="availableSizeGbs")
    def available_size_gbs(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @available_size_gbs.setter
    def available_size_gbs(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ExascaleDbStorageVaultPropertiesTimeZoneArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExascaleDbStorageVaultPropertiesTimeZoneArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
