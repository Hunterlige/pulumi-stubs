

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TableBucketEncryptionConfigurationArgs', 'TableBucketEncryptionConfigurationArgsDict', 'TableBucketMaintenanceConfigurationArgs', 'TableBucketMaintenanceConfigurationArgsDict', ..., ..., ..., ..., 'TableBucketReplicationRuleArgs', 'TableBucketReplicationRuleArgsDict', 'TableBucketReplicationRuleDestinationArgs', 'TableBucketReplicationRuleDestinationArgsDict', 'TableEncryptionConfigurationArgs', 'TableEncryptionConfigurationArgsDict', 'TableMaintenanceConfigurationArgs', 'TableMaintenanceConfigurationArgsDict', 'TableMaintenanceConfigurationIcebergCompactionArgs', ..., ..., ..., ..., ..., ..., ..., 'TableMetadataArgs', 'TableMetadataArgsDict', 'TableMetadataIcebergArgs', 'TableMetadataIcebergArgsDict', 'TableMetadataIcebergSchemaArgs', 'TableMetadataIcebergSchemaArgsDict', 'TableMetadataIcebergSchemaFieldArgs', 'TableMetadataIcebergSchemaFieldArgsDict', 'TableReplicationRuleArgs', 'TableReplicationRuleArgsDict', 'TableReplicationRuleDestinationArgs', 'TableReplicationRuleDestinationArgsDict']
class TableBucketEncryptionConfigurationArgsDict(TypedDict):
    kms_key_arn: pulumi.Input[_builtins.str]
    sse_algorithm: pulumi.Input[_builtins.str]


@pulumi.input_type
class TableBucketEncryptionConfigurationArgs:
    def __init__(__self__, *, kms_key_arn: pulumi.Input[_builtins.str], sse_algorithm: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sse_algorithm.setter
    def sse_algorithm(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TableBucketMaintenanceConfigurationArgsDict(TypedDict):
    iceberg_unreferenced_file_removal: pulumi.Input[TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalArgsDict]


@pulumi.input_type
class TableBucketMaintenanceConfigurationArgs:
    def __init__(__self__, *, iceberg_unreferenced_file_removal: pulumi.Input[TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icebergUnreferencedFileRemoval")
    def iceberg_unreferenced_file_removal(self) -> pulumi.Input[TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalArgs]:
        
        ...
    
    @iceberg_unreferenced_file_removal.setter
    def iceberg_unreferenced_file_removal(self, value: pulumi.Input[TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalArgs]): # -> None:
        ...
    


class TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalArgsDict(TypedDict):
    settings: pulumi.Input[TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalSettingsArgsDict]
    status: pulumi.Input[_builtins.str]


@pulumi.input_type
class TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalArgs:
    def __init__(__self__, *, settings: pulumi.Input[TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalSettingsArgs], status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Input[TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalSettingsArgs]:
        
        ...
    
    @settings.setter
    def settings(self, value: pulumi.Input[TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalSettingsArgsDict(TypedDict):
    non_current_days: pulumi.Input[_builtins.int]
    unreferenced_days: pulumi.Input[_builtins.int]


@pulumi.input_type
class TableBucketMaintenanceConfigurationIcebergUnreferencedFileRemovalSettingsArgs:
    def __init__(__self__, *, non_current_days: pulumi.Input[_builtins.int], unreferenced_days: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonCurrentDays")
    def non_current_days(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @non_current_days.setter
    def non_current_days(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unreferencedDays")
    def unreferenced_days(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @unreferenced_days.setter
    def unreferenced_days(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class TableBucketReplicationRuleArgsDict(TypedDict):
    destinations: pulumi.Input[Sequence[pulumi.Input[TableBucketReplicationRuleDestinationArgsDict]]]


@pulumi.input_type
class TableBucketReplicationRuleArgs:
    def __init__(__self__, *, destinations: pulumi.Input[Sequence[pulumi.Input[TableBucketReplicationRuleDestinationArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> pulumi.Input[Sequence[pulumi.Input[TableBucketReplicationRuleDestinationArgs]]]:
        
        ...
    
    @destinations.setter
    def destinations(self, value: pulumi.Input[Sequence[pulumi.Input[TableBucketReplicationRuleDestinationArgs]]]): # -> None:
        ...
    


class TableBucketReplicationRuleDestinationArgsDict(TypedDict):
    destination_table_bucket_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class TableBucketReplicationRuleDestinationArgs:
    def __init__(__self__, *, destination_table_bucket_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationTableBucketArn")
    def destination_table_bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination_table_bucket_arn.setter
    def destination_table_bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TableEncryptionConfigurationArgsDict(TypedDict):
    kms_key_arn: pulumi.Input[_builtins.str]
    sse_algorithm: pulumi.Input[_builtins.str]


@pulumi.input_type
class TableEncryptionConfigurationArgs:
    def __init__(__self__, *, kms_key_arn: pulumi.Input[_builtins.str], sse_algorithm: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sse_algorithm.setter
    def sse_algorithm(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TableMaintenanceConfigurationArgsDict(TypedDict):
    iceberg_compaction: pulumi.Input[TableMaintenanceConfigurationIcebergCompactionArgsDict]
    iceberg_snapshot_management: pulumi.Input[TableMaintenanceConfigurationIcebergSnapshotManagementArgsDict]


@pulumi.input_type
class TableMaintenanceConfigurationArgs:
    def __init__(__self__, *, iceberg_compaction: pulumi.Input[TableMaintenanceConfigurationIcebergCompactionArgs], iceberg_snapshot_management: pulumi.Input[TableMaintenanceConfigurationIcebergSnapshotManagementArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icebergCompaction")
    def iceberg_compaction(self) -> pulumi.Input[TableMaintenanceConfigurationIcebergCompactionArgs]:
        
        ...
    
    @iceberg_compaction.setter
    def iceberg_compaction(self, value: pulumi.Input[TableMaintenanceConfigurationIcebergCompactionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icebergSnapshotManagement")
    def iceberg_snapshot_management(self) -> pulumi.Input[TableMaintenanceConfigurationIcebergSnapshotManagementArgs]:
        
        ...
    
    @iceberg_snapshot_management.setter
    def iceberg_snapshot_management(self, value: pulumi.Input[TableMaintenanceConfigurationIcebergSnapshotManagementArgs]): # -> None:
        ...
    


class TableMaintenanceConfigurationIcebergCompactionArgsDict(TypedDict):
    settings: pulumi.Input[TableMaintenanceConfigurationIcebergCompactionSettingsArgsDict]
    status: pulumi.Input[_builtins.str]


@pulumi.input_type
class TableMaintenanceConfigurationIcebergCompactionArgs:
    def __init__(__self__, *, settings: pulumi.Input[TableMaintenanceConfigurationIcebergCompactionSettingsArgs], status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Input[TableMaintenanceConfigurationIcebergCompactionSettingsArgs]:
        
        ...
    
    @settings.setter
    def settings(self, value: pulumi.Input[TableMaintenanceConfigurationIcebergCompactionSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TableMaintenanceConfigurationIcebergCompactionSettingsArgsDict(TypedDict):
    target_file_size_mb: pulumi.Input[_builtins.int]


@pulumi.input_type
class TableMaintenanceConfigurationIcebergCompactionSettingsArgs:
    def __init__(__self__, *, target_file_size_mb: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFileSizeMb")
    def target_file_size_mb(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @target_file_size_mb.setter
    def target_file_size_mb(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class TableMaintenanceConfigurationIcebergSnapshotManagementArgsDict(TypedDict):
    settings: pulumi.Input[TableMaintenanceConfigurationIcebergSnapshotManagementSettingsArgsDict]
    status: pulumi.Input[_builtins.str]


@pulumi.input_type
class TableMaintenanceConfigurationIcebergSnapshotManagementArgs:
    def __init__(__self__, *, settings: pulumi.Input[TableMaintenanceConfigurationIcebergSnapshotManagementSettingsArgs], status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> pulumi.Input[TableMaintenanceConfigurationIcebergSnapshotManagementSettingsArgs]:
        
        ...
    
    @settings.setter
    def settings(self, value: pulumi.Input[TableMaintenanceConfigurationIcebergSnapshotManagementSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TableMaintenanceConfigurationIcebergSnapshotManagementSettingsArgsDict(TypedDict):
    max_snapshot_age_hours: pulumi.Input[_builtins.int]
    min_snapshots_to_keep: pulumi.Input[_builtins.int]


@pulumi.input_type
class TableMaintenanceConfigurationIcebergSnapshotManagementSettingsArgs:
    def __init__(__self__, *, max_snapshot_age_hours: pulumi.Input[_builtins.int], min_snapshots_to_keep: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSnapshotAgeHours")
    def max_snapshot_age_hours(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_snapshot_age_hours.setter
    def max_snapshot_age_hours(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minSnapshotsToKeep")
    def min_snapshots_to_keep(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @min_snapshots_to_keep.setter
    def min_snapshots_to_keep(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class TableMetadataArgsDict(TypedDict):
    iceberg: pulumi.Input[TableMetadataIcebergArgsDict]


@pulumi.input_type
class TableMetadataArgs:
    def __init__(__self__, *, iceberg: pulumi.Input[TableMetadataIcebergArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def iceberg(self) -> pulumi.Input[TableMetadataIcebergArgs]:
        
        ...
    
    @iceberg.setter
    def iceberg(self, value: pulumi.Input[TableMetadataIcebergArgs]): # -> None:
        ...
    


class TableMetadataIcebergArgsDict(TypedDict):
    schema: pulumi.Input[TableMetadataIcebergSchemaArgsDict]


@pulumi.input_type
class TableMetadataIcebergArgs:
    def __init__(__self__, *, schema: pulumi.Input[TableMetadataIcebergSchemaArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[TableMetadataIcebergSchemaArgs]:
        
        ...
    
    @schema.setter
    def schema(self, value: pulumi.Input[TableMetadataIcebergSchemaArgs]): # -> None:
        ...
    


class TableMetadataIcebergSchemaArgsDict(TypedDict):
    fields: pulumi.Input[Sequence[pulumi.Input[TableMetadataIcebergSchemaFieldArgsDict]]]


@pulumi.input_type
class TableMetadataIcebergSchemaArgs:
    def __init__(__self__, *, fields: pulumi.Input[Sequence[pulumi.Input[TableMetadataIcebergSchemaFieldArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[TableMetadataIcebergSchemaFieldArgs]]]:
        
        ...
    
    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[TableMetadataIcebergSchemaFieldArgs]]]): # -> None:
        ...
    


class TableMetadataIcebergSchemaFieldArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    required: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class TableMetadataIcebergSchemaFieldArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], required: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
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
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class TableReplicationRuleArgsDict(TypedDict):
    destinations: pulumi.Input[Sequence[pulumi.Input[TableReplicationRuleDestinationArgsDict]]]


@pulumi.input_type
class TableReplicationRuleArgs:
    def __init__(__self__, *, destinations: pulumi.Input[Sequence[pulumi.Input[TableReplicationRuleDestinationArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> pulumi.Input[Sequence[pulumi.Input[TableReplicationRuleDestinationArgs]]]:
        
        ...
    
    @destinations.setter
    def destinations(self, value: pulumi.Input[Sequence[pulumi.Input[TableReplicationRuleDestinationArgs]]]): # -> None:
        ...
    


class TableReplicationRuleDestinationArgsDict(TypedDict):
    destination_table_bucket_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class TableReplicationRuleDestinationArgs:
    def __init__(__self__, *, destination_table_bucket_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationTableBucketArn")
    def destination_table_bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination_table_bucket_arn.setter
    def destination_table_bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


