import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MigrationArgs", "Migration"]

@pulumi.input_type
class MigrationArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        server_name: pulumi.Input[_builtins.str],
        cancel: Optional[pulumi.Input[Union[_builtins.str, Cancel]]] = ...,
        dbs_to_cancel_migration_on: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        dbs_to_migrate: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        dbs_to_trigger_cutover_on: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        migrate_roles: Optional[
            pulumi.Input[Union[_builtins.str, MigrateRolesAndPermissions]]
        ] = ...,
        migration_instance_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        migration_mode: Optional[
            pulumi.Input[Union[_builtins.str, MigrationMode]]
        ] = ...,
        migration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        migration_option: Optional[
            pulumi.Input[Union[_builtins.str, MigrationOption]]
        ] = ...,
        migration_window_end_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        migration_window_start_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        overwrite_dbs_in_target: Optional[
            pulumi.Input[Union[_builtins.str, OverwriteDatabasesOnTargetServer]]
        ] = ...,
        secret_parameters: Optional[pulumi.Input[MigrationSecretParametersArgs]] = ...,
        setup_logical_replication_on_source_db_if_needed: Optional[
            pulumi.Input[Union[_builtins.str, LogicalReplicationOnSourceServer]]
        ] = ...,
        source_db_server_fully_qualified_domain_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        source_db_server_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_type: Optional[pulumi.Input[Union[_builtins.str, SourceType]]] = ...,
        ssl_mode: Optional[pulumi.Input[Union[_builtins.str, SslMode]]] = ...,
        start_data_migration: Optional[
            pulumi.Input[Union[_builtins.str, StartDataMigration]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_db_server_fully_qualified_domain_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        trigger_cutover: Optional[
            pulumi.Input[Union[_builtins.str, TriggerCutover]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]: ...
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def cancel(self) -> Optional[pulumi.Input[Union[_builtins.str, Cancel]]]: ...
    @cancel.setter
    def cancel(self, value: Optional[pulumi.Input[Union[_builtins.str, Cancel]]]): ...
    @_builtins.property
    @pulumi.getter(name="dbsToCancelMigrationOn")
    def dbs_to_cancel_migration_on(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dbs_to_cancel_migration_on.setter
    def dbs_to_cancel_migration_on(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbsToMigrate")
    def dbs_to_migrate(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dbs_to_migrate.setter
    def dbs_to_migrate(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dbsToTriggerCutoverOn")
    def dbs_to_trigger_cutover_on(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dbs_to_trigger_cutover_on.setter
    def dbs_to_trigger_cutover_on(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="migrateRoles")
    def migrate_roles(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MigrateRolesAndPermissions]]]: ...
    @migrate_roles.setter
    def migrate_roles(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, MigrateRolesAndPermissions]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="migrationInstanceResourceId")
    def migration_instance_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @migration_instance_resource_id.setter
    def migration_instance_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="migrationMode")
    def migration_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MigrationMode]]]: ...
    @migration_mode.setter
    def migration_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MigrationMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="migrationName")
    def migration_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @migration_name.setter
    def migration_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="migrationOption")
    def migration_option(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MigrationOption]]]: ...
    @migration_option.setter
    def migration_option(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MigrationOption]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="migrationWindowEndTimeInUtc")
    def migration_window_end_time_in_utc(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @migration_window_end_time_in_utc.setter
    def migration_window_end_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="migrationWindowStartTimeInUtc")
    def migration_window_start_time_in_utc(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @migration_window_start_time_in_utc.setter
    def migration_window_start_time_in_utc(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="overwriteDbsInTarget")
    def overwrite_dbs_in_target(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, OverwriteDatabasesOnTargetServer]]
    ]: ...
    @overwrite_dbs_in_target.setter
    def overwrite_dbs_in_target(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, OverwriteDatabasesOnTargetServer]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretParameters")
    def secret_parameters(
        self,
    ) -> Optional[pulumi.Input[MigrationSecretParametersArgs]]: ...
    @secret_parameters.setter
    def secret_parameters(
        self, value: Optional[pulumi.Input[MigrationSecretParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="setupLogicalReplicationOnSourceDbIfNeeded")
    def setup_logical_replication_on_source_db_if_needed(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, LogicalReplicationOnSourceServer]]
    ]: ...
    @setup_logical_replication_on_source_db_if_needed.setter
    def setup_logical_replication_on_source_db_if_needed(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, LogicalReplicationOnSourceServer]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceDbServerFullyQualifiedDomainName")
    def source_db_server_fully_qualified_domain_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_db_server_fully_qualified_domain_name.setter
    def source_db_server_fully_qualified_domain_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceDbServerResourceId")
    def source_db_server_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_db_server_resource_id.setter
    def source_db_server_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SourceType]]]: ...
    @source_type.setter
    def source_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SourceType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, SslMode]]]: ...
    @ssl_mode.setter
    def ssl_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SslMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startDataMigration")
    def start_data_migration(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StartDataMigration]]]: ...
    @start_data_migration.setter
    def start_data_migration(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StartDataMigration]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetDbServerFullyQualifiedDomainName")
    def target_db_server_fully_qualified_domain_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_db_server_fully_qualified_domain_name.setter
    def target_db_server_fully_qualified_domain_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="triggerCutover")
    def trigger_cutover(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TriggerCutover]]]: ...
    @trigger_cutover.setter
    def trigger_cutover(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TriggerCutover]]]
    ): ...

@pulumi.type_token("azure-native:dbforpostgresql:Migration")
class Migration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cancel: Optional[pulumi.Input[Union[_builtins.str, Cancel]]] = ...,
        dbs_to_cancel_migration_on: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        dbs_to_migrate: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        dbs_to_trigger_cutover_on: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        migrate_roles: Optional[
            pulumi.Input[Union[_builtins.str, MigrateRolesAndPermissions]]
        ] = ...,
        migration_instance_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        migration_mode: Optional[
            pulumi.Input[Union[_builtins.str, MigrationMode]]
        ] = ...,
        migration_name: Optional[pulumi.Input[_builtins.str]] = ...,
        migration_option: Optional[
            pulumi.Input[Union[_builtins.str, MigrationOption]]
        ] = ...,
        migration_window_end_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        migration_window_start_time_in_utc: Optional[pulumi.Input[_builtins.str]] = ...,
        overwrite_dbs_in_target: Optional[
            pulumi.Input[Union[_builtins.str, OverwriteDatabasesOnTargetServer]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_parameters: Optional[
            pulumi.Input[
                Union[MigrationSecretParametersArgs, MigrationSecretParametersArgsDict]
            ]
        ] = ...,
        server_name: Optional[pulumi.Input[_builtins.str]] = ...,
        setup_logical_replication_on_source_db_if_needed: Optional[
            pulumi.Input[Union[_builtins.str, LogicalReplicationOnSourceServer]]
        ] = ...,
        source_db_server_fully_qualified_domain_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        source_db_server_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        source_type: Optional[pulumi.Input[Union[_builtins.str, SourceType]]] = ...,
        ssl_mode: Optional[pulumi.Input[Union[_builtins.str, SslMode]]] = ...,
        start_data_migration: Optional[
            pulumi.Input[Union[_builtins.str, StartDataMigration]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_db_server_fully_qualified_domain_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        trigger_cutover: Optional[
            pulumi.Input[Union[_builtins.str, TriggerCutover]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MigrationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Migration: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cancel(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="currentStatus")
    def current_status(self) -> pulumi.Output[outputs.MigrationStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dbsToCancelMigrationOn")
    def dbs_to_cancel_migration_on(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="dbsToMigrate")
    def dbs_to_migrate(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="dbsToTriggerCutoverOn")
    def dbs_to_trigger_cutover_on(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="migrateRoles")
    def migrate_roles(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="migrationId")
    def migration_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="migrationInstanceResourceId")
    def migration_instance_resource_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="migrationMode")
    def migration_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="migrationOption")
    def migration_option(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="migrationWindowEndTimeInUtc")
    def migration_window_end_time_in_utc(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="migrationWindowStartTimeInUtc")
    def migration_window_start_time_in_utc(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="overwriteDbsInTarget")
    def overwrite_dbs_in_target(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="setupLogicalReplicationOnSourceDbIfNeeded")
    def setup_logical_replication_on_source_db_if_needed(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDbServerFullyQualifiedDomainName")
    def source_db_server_fully_qualified_domain_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDbServerMetadata")
    def source_db_server_metadata(
        self,
    ) -> pulumi.Output[outputs.DbServerMetadataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDbServerResourceId")
    def source_db_server_resource_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="startDataMigration")
    def start_data_migration(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="targetDbServerFullyQualifiedDomainName")
    def target_db_server_fully_qualified_domain_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetDbServerMetadata")
    def target_db_server_metadata(
        self,
    ) -> pulumi.Output[outputs.DbServerMetadataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="targetDbServerResourceId")
    def target_db_server_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerCutover")
    def trigger_cutover(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
