import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "TableMagneticStoreWriteProperties",
    ...,
    ...,
    "TableRetentionProperties",
    "TableSchema",
    "TableSchemaCompositePartitionKey",
    "GetTableMagneticStoreWritePropertyResult",
    ...,
    ...,
    "GetTableRetentionPropertyResult",
    "GetTableSchemaResult",
    "GetTableSchemaCompositePartitionKeyResult",
]

@pulumi.output_type
class TableMagneticStoreWriteProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_magnetic_store_writes: Optional[_builtins.bool] = ...,
        magnetic_store_rejected_data_location: Optional[
            outputs.TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableMagneticStoreWrites")
    def enable_magnetic_store_writes(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="magneticStoreRejectedDataLocation")
    def magnetic_store_rejected_data_location(
        self,
    ) -> Optional[
        outputs.TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation
    ]: ...

@pulumi.output_type
class TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_configuration: Optional[
            outputs.TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Configuration")
    def s3_configuration(
        self,
    ) -> Optional[
        outputs.TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration
    ]: ...

@pulumi.output_type
class TableMagneticStoreWritePropertiesMagneticStoreRejectedDataLocationS3Configuration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        encryption_option: Optional[_builtins.str] = ...,
        kms_key_id: Optional[_builtins.str] = ...,
        object_key_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectKeyPrefix")
    def object_key_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableRetentionProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        magnetic_store_retention_period_in_days: _builtins.int,
        memory_store_retention_period_in_hours: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="magneticStoreRetentionPeriodInDays")
    def magnetic_store_retention_period_in_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memoryStoreRetentionPeriodInHours")
    def memory_store_retention_period_in_hours(self) -> _builtins.int: ...

@pulumi.output_type
class TableSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        composite_partition_key: Optional[
            outputs.TableSchemaCompositePartitionKey
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="compositePartitionKey")
    def composite_partition_key(
        self,
    ) -> Optional[outputs.TableSchemaCompositePartitionKey]: ...

@pulumi.output_type
class TableSchemaCompositePartitionKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        enforcement_in_record: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enforcementInRecord")
    def enforcement_in_record(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetTableMagneticStoreWritePropertyResult(dict):
    def __init__(
        __self__,
        *,
        enable_magnetic_store_writes: _builtins.bool,
        magnetic_store_rejected_data_locations: Sequence[
            outputs.GetTableMagneticStoreWritePropertyMagneticStoreRejectedDataLocationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableMagneticStoreWrites")
    def enable_magnetic_store_writes(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="magneticStoreRejectedDataLocations")
    def magnetic_store_rejected_data_locations(
        self,
    ) -> Sequence[
        outputs.GetTableMagneticStoreWritePropertyMagneticStoreRejectedDataLocationResult
    ]: ...

@pulumi.output_type
class GetTableMagneticStoreWritePropertyMagneticStoreRejectedDataLocationResult(dict):
    def __init__(
        __self__,
        *,
        s3_configurations: Sequence[
            outputs.GetTableMagneticStoreWritePropertyMagneticStoreRejectedDataLocationS3ConfigurationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Configurations")
    def s3_configurations(
        self,
    ) -> Sequence[
        outputs.GetTableMagneticStoreWritePropertyMagneticStoreRejectedDataLocationS3ConfigurationResult
    ]: ...

@pulumi.output_type
class GetTableMagneticStoreWritePropertyMagneticStoreRejectedDataLocationS3ConfigurationResult(
    dict
):
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        encryption_option: _builtins.str,
        kms_key_id: _builtins.str,
        object_key_prefix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectKeyPrefix")
    def object_key_prefix(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableRetentionPropertyResult(dict):
    def __init__(
        __self__,
        *,
        magnetic_store_retention_period_in_days: _builtins.int,
        memory_store_retention_period_in_hours: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="magneticStoreRetentionPeriodInDays")
    def magnetic_store_retention_period_in_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="memoryStoreRetentionPeriodInHours")
    def memory_store_retention_period_in_hours(self) -> _builtins.int: ...

@pulumi.output_type
class GetTableSchemaResult(dict):
    def __init__(
        __self__,
        *,
        composite_partition_keys: Sequence[
            outputs.GetTableSchemaCompositePartitionKeyResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="compositePartitionKeys")
    def composite_partition_keys(
        self,
    ) -> Sequence[outputs.GetTableSchemaCompositePartitionKeyResult]: ...

@pulumi.output_type
class GetTableSchemaCompositePartitionKeyResult(dict):
    def __init__(
        __self__,
        *,
        enforcement_in_record: _builtins.str,
        name: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enforcementInRecord")
    def enforcement_in_record(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
