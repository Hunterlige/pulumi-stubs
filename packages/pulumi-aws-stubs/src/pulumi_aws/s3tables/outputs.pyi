import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "TableBucketEncryptionConfiguration",
    "TableBucketMaintenanceConfiguration",
    ...,
    ...,
    "TableBucketReplicationRule",
    "TableBucketReplicationRuleDestination",
    "TableEncryptionConfiguration",
    "TableMaintenanceConfiguration",
    "TableMaintenanceConfigurationIcebergCompaction",
    ...,
    ...,
    ...,
    "TableMetadata",
    "TableMetadataIceberg",
    "TableMetadataIcebergSchema",
    "TableMetadataIcebergSchemaField",
    "TableReplicationRule",
    "TableReplicationRuleDestination",
]

@pulumi.output_type
class TableBucketEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, kms_key_arn: _builtins.str, sse_algorithm: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> _builtins.str: ...

@pulumi.output_type
class TableBucketMaintenanceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        iceberg_unreferenced_file_removal: outputs.TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemoval,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="icebergUnreferencedFileRemoval")
    def iceberg_unreferenced_file_removal(
        self,
    ) -> outputs.TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemoval: ...

@pulumi.output_type
class TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemoval(dict):
    def __init__(
        __self__,
        *,
        settings: outputs.TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalSettings,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def settings(
        self,
    ) -> outputs.TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalSettings: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, non_current_days: _builtins.int, unreferenced_days: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nonCurrentDays")
    def non_current_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="unreferencedDays")
    def unreferenced_days(self) -> _builtins.int: ...

@pulumi.output_type
class TableBucketReplicationRule(dict):
    def __init__(
        __self__,
        *,
        destinations: Sequence[outputs.TableBucketReplicationRuleDestination],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Sequence[outputs.TableBucketReplicationRuleDestination]: ...

@pulumi.output_type
class TableBucketReplicationRuleDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, destination_table_bucket_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationTableBucketArn")
    def destination_table_bucket_arn(self) -> _builtins.str: ...

@pulumi.output_type
class TableEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, kms_key_arn: _builtins.str, sse_algorithm: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> _builtins.str: ...

@pulumi.output_type
class TableMaintenanceConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        iceberg_compaction: outputs.TableMaintenanceConfigurationIcebergCompaction,
        iceberg_snapshot_management: outputs.TableMaintenanceConfigurationIcebergSnapshotManagement,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="icebergCompaction")
    def iceberg_compaction(
        self,
    ) -> outputs.TableMaintenanceConfigurationIcebergCompaction: ...
    @_builtins.property
    @pulumi.getter(name="icebergSnapshotManagement")
    def iceberg_snapshot_management(
        self,
    ) -> outputs.TableMaintenanceConfigurationIcebergSnapshotManagement: ...

@pulumi.output_type
class TableMaintenanceConfigurationIcebergCompaction(dict):
    def __init__(
        __self__,
        *,
        settings: outputs.TableMaintenanceConfigurationIcebergCompactionSettings,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def settings(
        self,
    ) -> outputs.TableMaintenanceConfigurationIcebergCompactionSettings: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class TableMaintenanceConfigurationIcebergCompactionSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, target_file_size_mb: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetFileSizeMb")
    def target_file_size_mb(self) -> _builtins.int: ...

@pulumi.output_type
class TableMaintenanceConfigurationIcebergSnapshotManagement(dict):
    def __init__(
        __self__,
        *,
        settings: outputs.TableMaintenanceConfigurationIcebergSnapshotManagementSettings,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def settings(
        self,
    ) -> outputs.TableMaintenanceConfigurationIcebergSnapshotManagementSettings: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class TableMaintenanceConfigurationIcebergSnapshotManagementSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_snapshot_age_hours: _builtins.int,
        min_snapshots_to_keep: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxSnapshotAgeHours")
    def max_snapshot_age_hours(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minSnapshotsToKeep")
    def min_snapshots_to_keep(self) -> _builtins.int: ...

@pulumi.output_type
class TableMetadata(dict):
    def __init__(__self__, *, iceberg: outputs.TableMetadataIceberg) -> None: ...
    @_builtins.property
    @pulumi.getter
    def iceberg(self) -> outputs.TableMetadataIceberg: ...

@pulumi.output_type
class TableMetadataIceberg(dict):
    def __init__(__self__, *, schema: outputs.TableMetadataIcebergSchema) -> None: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> outputs.TableMetadataIcebergSchema: ...

@pulumi.output_type
class TableMetadataIcebergSchema(dict):
    def __init__(
        __self__, *, fields: Sequence[outputs.TableMetadataIcebergSchemaField]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(self) -> Sequence[outputs.TableMetadataIcebergSchemaField]: ...

@pulumi.output_type
class TableMetadataIcebergSchemaField(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class TableReplicationRule(dict):
    def __init__(
        __self__, *, destinations: Sequence[outputs.TableReplicationRuleDestination]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Sequence[outputs.TableReplicationRuleDestination]: ...

@pulumi.output_type
class TableReplicationRuleDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, destination_table_bucket_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationTableBucketArn")
    def destination_table_bucket_arn(self) -> _builtins.str: ...
