import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMigrationResult",
    "AwaitableGetMigrationResult",
    "get_migration",
    "get_migration_output",
]

@pulumi.output_type
class GetMigrationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        cancel=...,
        current_status=...,
        dbs_to_cancel_migration_on=...,
        dbs_to_migrate=...,
        dbs_to_trigger_cutover_on=...,
        id=...,
        location=...,
        migrate_roles=...,
        migration_id=...,
        migration_instance_resource_id=...,
        migration_mode=...,
        migration_option=...,
        migration_window_end_time_in_utc=...,
        migration_window_start_time_in_utc=...,
        name=...,
        overwrite_dbs_in_target=...,
        setup_logical_replication_on_source_db_if_needed=...,
        source_db_server_fully_qualified_domain_name=...,
        source_db_server_metadata=...,
        source_db_server_resource_id=...,
        source_type=...,
        ssl_mode=...,
        start_data_migration=...,
        system_data=...,
        tags=...,
        target_db_server_fully_qualified_domain_name=...,
        target_db_server_metadata=...,
        target_db_server_resource_id=...,
        trigger_cutover=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cancel(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="currentStatus")
    def current_status(self) -> outputs.MigrationStatusResponse: ...
    @_builtins.property
    @pulumi.getter(name="dbsToCancelMigrationOn")
    def dbs_to_cancel_migration_on(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dbsToMigrate")
    def dbs_to_migrate(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dbsToTriggerCutoverOn")
    def dbs_to_trigger_cutover_on(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="migrateRoles")
    def migrate_roles(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="migrationId")
    def migration_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="migrationInstanceResourceId")
    def migration_instance_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="migrationMode")
    def migration_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="migrationOption")
    def migration_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="migrationWindowEndTimeInUtc")
    def migration_window_end_time_in_utc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="migrationWindowStartTimeInUtc")
    def migration_window_start_time_in_utc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="overwriteDbsInTarget")
    def overwrite_dbs_in_target(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="setupLogicalReplicationOnSourceDbIfNeeded")
    def setup_logical_replication_on_source_db_if_needed(
        self,
    ) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDbServerFullyQualifiedDomainName")
    def source_db_server_fully_qualified_domain_name(
        self,
    ) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDbServerMetadata")
    def source_db_server_metadata(self) -> outputs.DbServerMetadataResponse: ...
    @_builtins.property
    @pulumi.getter(name="sourceDbServerResourceId")
    def source_db_server_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startDataMigration")
    def start_data_migration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetDbServerFullyQualifiedDomainName")
    def target_db_server_fully_qualified_domain_name(
        self,
    ) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetDbServerMetadata")
    def target_db_server_metadata(self) -> outputs.DbServerMetadataResponse: ...
    @_builtins.property
    @pulumi.getter(name="targetDbServerResourceId")
    def target_db_server_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="triggerCutover")
    def trigger_cutover(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetMigrationResult(GetMigrationResult):
    def __await__(self): ...

def get_migration(
    migration_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMigrationResult: ...
def get_migration_output(
    migration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMigrationResult]: ...
