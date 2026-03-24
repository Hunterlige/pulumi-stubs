import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DatabaseArgs", "Database"]

@pulumi.input_type
class DatabaseArgs:
    def __init__(
        __self__,
        *,
        blueprint_id: pulumi.Input[_builtins.str],
        bundle_id: pulumi.Input[_builtins.str],
        master_database_name: pulumi.Input[_builtins.str],
        master_password: pulumi.Input[_builtins.str],
        master_username: pulumi.Input[_builtins.str],
        relational_database_name: pulumi.Input[_builtins.str],
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_retention_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        final_snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> pulumi.Input[_builtins.str]: ...
    @blueprint_id.setter
    def blueprint_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Input[_builtins.str]: ...
    @bundle_id.setter
    def bundle_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="masterDatabaseName")
    def master_database_name(self) -> pulumi.Input[_builtins.str]: ...
    @master_database_name.setter
    def master_database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="masterPassword")
    def master_password(self) -> pulumi.Input[_builtins.str]: ...
    @master_password.setter
    def master_password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> pulumi.Input[_builtins.str]: ...
    @master_username.setter
    def master_username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="relationalDatabaseName")
    def relational_database_name(self) -> pulumi.Input[_builtins.str]: ...
    @relational_database_name.setter
    def relational_database_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionEnabled")
    def backup_retention_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @backup_retention_enabled.setter
    def backup_retention_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="finalSnapshotName")
    def final_snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @final_snapshot_name.setter
    def final_snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_backup_window.setter
    def preferred_backup_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_final_snapshot.setter
    def skip_final_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _DatabaseState:
    def __init__(
        __self__,
        *,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_retention_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        blueprint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificate_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu_count: Optional[pulumi.Input[_builtins.int]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size: Optional[pulumi.Input[_builtins.float]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        master_database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        master_endpoint_address: Optional[pulumi.Input[_builtins.str]] = ...,
        master_endpoint_port: Optional[pulumi.Input[_builtins.int]] = ...,
        master_password: Optional[pulumi.Input[_builtins.str]] = ...,
        master_username: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        ram_size: Optional[pulumi.Input[_builtins.float]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        relational_database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        support_code: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionEnabled")
    def backup_retention_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @backup_retention_enabled.setter
    def backup_retention_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blueprint_id.setter
    def blueprint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bundle_id.setter
    def bundle_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertificateIdentifier")
    def ca_certificate_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificate_identifier.setter
    def ca_certificate_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cpu_count.setter
    def cpu_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @disk_size.setter
    def disk_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="finalSnapshotName")
    def final_snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @final_snapshot_name.setter
    def final_snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterDatabaseName")
    def master_database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_database_name.setter
    def master_database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterEndpointAddress")
    def master_endpoint_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_endpoint_address.setter
    def master_endpoint_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterEndpointPort")
    def master_endpoint_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @master_endpoint_port.setter
    def master_endpoint_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="masterPassword")
    def master_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_password.setter
    def master_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_username.setter
    def master_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_backup_window.setter
    def preferred_backup_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ramSize")
    def ram_size(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @ram_size.setter
    def ram_size(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="relationalDatabaseName")
    def relational_database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @relational_database_name.setter
    def relational_database_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondaryAvailabilityZone")
    def secondary_availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_availability_zone.setter
    def secondary_availability_zone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_final_snapshot.setter
    def skip_final_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="supportCode")
    def support_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @support_code.setter
    def support_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:lightsail/database:Database")
class Database(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_retention_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        blueprint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        master_database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password: Optional[pulumi.Input[_builtins.str]] = ...,
        master_username: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        relational_database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DatabaseArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_retention_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        blueprint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bundle_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificate_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu_count: Optional[pulumi.Input[_builtins.int]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size: Optional[pulumi.Input[_builtins.float]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        master_database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        master_endpoint_address: Optional[pulumi.Input[_builtins.str]] = ...,
        master_endpoint_port: Optional[pulumi.Input[_builtins.int]] = ...,
        master_password: Optional[pulumi.Input[_builtins.str]] = ...,
        master_username: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_backup_window: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        ram_size: Optional[pulumi.Input[_builtins.float]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        relational_database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        support_code: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Database: ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupRetentionEnabled")
    def backup_retention_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caCertificateIdentifier")
    def ca_certificate_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuCount")
    def cpu_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finalSnapshotName")
    def final_snapshot_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="masterDatabaseName")
    def master_database_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="masterEndpointAddress")
    def master_endpoint_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="masterEndpointPort")
    def master_endpoint_port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="masterPassword")
    def master_password(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="ramSize")
    def ram_size(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="relationalDatabaseName")
    def relational_database_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryAvailabilityZone")
    def secondary_availability_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="supportCode")
    def support_code(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
