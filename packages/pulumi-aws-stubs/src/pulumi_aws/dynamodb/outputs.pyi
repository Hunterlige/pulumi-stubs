import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GlobalSecondaryIndexKeySchema",
    "GlobalSecondaryIndexOnDemandThroughput",
    "GlobalSecondaryIndexProjection",
    "GlobalSecondaryIndexProvisionedThroughput",
    "GlobalSecondaryIndexTimeouts",
    "GlobalSecondaryIndexWarmThroughput",
    "GlobalTableReplica",
    "TableAttribute",
    "TableExportIncrementalExportSpecification",
    "TableGlobalSecondaryIndex",
    "TableGlobalSecondaryIndexKeySchema",
    "TableGlobalSecondaryIndexOnDemandThroughput",
    "TableGlobalSecondaryIndexWarmThroughput",
    "TableGlobalTableWitness",
    "TableImportTable",
    "TableImportTableInputFormatOptions",
    "TableImportTableInputFormatOptionsCsv",
    "TableImportTableS3BucketSource",
    "TableLocalSecondaryIndex",
    "TableOnDemandThroughput",
    "TablePointInTimeRecovery",
    "TableReplica",
    "TableServerSideEncryption",
    "TableTtl",
    "TableWarmThroughput",
    "GetTableAttributeResult",
    "GetTableGlobalSecondaryIndexResult",
    "GetTableGlobalSecondaryIndexKeySchemaResult",
    ...,
    "GetTableGlobalSecondaryIndexWarmThroughputResult",
    "GetTableLocalSecondaryIndexResult",
    "GetTableOnDemandThroughputResult",
    "GetTablePointInTimeRecoveryResult",
    "GetTableReplicaResult",
    "GetTableServerSideEncryptionResult",
    "GetTableTtlResult",
    "GetTableWarmThroughputResult",
]

@pulumi.output_type
class GlobalSecondaryIndexKeySchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        attribute_name: _builtins.str,
        attribute_type: _builtins.str,
        key_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> _builtins.str: ...

@pulumi.output_type
class GlobalSecondaryIndexOnDemandThroughput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_read_request_units: Optional[_builtins.int] = ...,
        max_write_request_units: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxReadRequestUnits")
    def max_read_request_units(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxWriteRequestUnits")
    def max_write_request_units(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GlobalSecondaryIndexProjection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        projection_type: _builtins.str,
        non_key_attributes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectionType")
    def projection_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nonKeyAttributes")
    def non_key_attributes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GlobalSecondaryIndexProvisionedThroughput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        read_capacity_units: Optional[_builtins.int] = ...,
        write_capacity_units: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="readCapacityUnits")
    def read_capacity_units(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="writeCapacityUnits")
    def write_capacity_units(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GlobalSecondaryIndexTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GlobalSecondaryIndexWarmThroughput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        read_units_per_second: _builtins.int,
        write_units_per_second: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="readUnitsPerSecond")
    def read_units_per_second(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="writeUnitsPerSecond")
    def write_units_per_second(self) -> _builtins.int: ...

@pulumi.output_type
class GlobalTableReplica(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, region_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> _builtins.str: ...

@pulumi.output_type
class TableAttribute(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class TableExportIncrementalExportSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        export_from_time: Optional[_builtins.str] = ...,
        export_to_time: Optional[_builtins.str] = ...,
        export_view_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exportFromTime")
    def export_from_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportToTime")
    def export_to_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportViewType")
    def export_view_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableGlobalSecondaryIndex(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        projection_type: _builtins.str,
        hash_key: Optional[_builtins.str] = ...,
        key_schemas: Optional[
            Sequence[outputs.TableGlobalSecondaryIndexKeySchema]
        ] = ...,
        non_key_attributes: Optional[Sequence[_builtins.str]] = ...,
        on_demand_throughput: Optional[
            outputs.TableGlobalSecondaryIndexOnDemandThroughput
        ] = ...,
        range_key: Optional[_builtins.str] = ...,
        read_capacity: Optional[_builtins.int] = ...,
        warm_throughput: Optional[
            outputs.TableGlobalSecondaryIndexWarmThroughput
        ] = ...,
        write_capacity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectionType")
    def projection_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hashKey")
    @_utilities.deprecated("""hash_key is deprecated. Use key_schema instead.""")
    def hash_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keySchemas")
    def key_schemas(
        self,
    ) -> Optional[Sequence[outputs.TableGlobalSecondaryIndexKeySchema]]: ...
    @_builtins.property
    @pulumi.getter(name="nonKeyAttributes")
    def non_key_attributes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="onDemandThroughput")
    def on_demand_throughput(
        self,
    ) -> Optional[outputs.TableGlobalSecondaryIndexOnDemandThroughput]: ...
    @_builtins.property
    @pulumi.getter(name="rangeKey")
    @_utilities.deprecated("""range_key is deprecated. Use key_schema instead.""")
    def range_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="readCapacity")
    def read_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="warmThroughput")
    def warm_throughput(
        self,
    ) -> Optional[outputs.TableGlobalSecondaryIndexWarmThroughput]: ...
    @_builtins.property
    @pulumi.getter(name="writeCapacity")
    def write_capacity(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TableGlobalSecondaryIndexKeySchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, attribute_name: _builtins.str, key_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> _builtins.str: ...

@pulumi.output_type
class TableGlobalSecondaryIndexOnDemandThroughput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_read_request_units: Optional[_builtins.int] = ...,
        max_write_request_units: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxReadRequestUnits")
    def max_read_request_units(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxWriteRequestUnits")
    def max_write_request_units(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TableGlobalSecondaryIndexWarmThroughput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        read_units_per_second: Optional[_builtins.int] = ...,
        write_units_per_second: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="readUnitsPerSecond")
    def read_units_per_second(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="writeUnitsPerSecond")
    def write_units_per_second(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TableGlobalTableWitness(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, region_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableImportTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input_format: _builtins.str,
        s3_bucket_source: outputs.TableImportTableS3BucketSource,
        input_compression_type: Optional[_builtins.str] = ...,
        input_format_options: Optional[
            outputs.TableImportTableInputFormatOptions
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketSource")
    def s3_bucket_source(self) -> outputs.TableImportTableS3BucketSource: ...
    @_builtins.property
    @pulumi.getter(name="inputCompressionType")
    def input_compression_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputFormatOptions")
    def input_format_options(
        self,
    ) -> Optional[outputs.TableImportTableInputFormatOptions]: ...

@pulumi.output_type
class TableImportTableInputFormatOptions(dict):
    def __init__(
        __self__, *, csv: Optional[outputs.TableImportTableInputFormatOptionsCsv] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def csv(self) -> Optional[outputs.TableImportTableInputFormatOptionsCsv]: ...

@pulumi.output_type
class TableImportTableInputFormatOptionsCsv(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delimiter: Optional[_builtins.str] = ...,
        header_lists: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="headerLists")
    def header_lists(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class TableImportTableS3BucketSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        bucket_owner: Optional[_builtins.str] = ...,
        key_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwner")
    def bucket_owner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableLocalSecondaryIndex(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        projection_type: _builtins.str,
        range_key: _builtins.str,
        non_key_attributes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectionType")
    def projection_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rangeKey")
    def range_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nonKeyAttributes")
    def non_key_attributes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class TableOnDemandThroughput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_read_request_units: Optional[_builtins.int] = ...,
        max_write_request_units: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxReadRequestUnits")
    def max_read_request_units(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxWriteRequestUnits")
    def max_write_request_units(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TablePointInTimeRecovery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        recovery_period_in_days: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="recoveryPeriodInDays")
    def recovery_period_in_days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TableReplica(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        region_name: _builtins.str,
        arn: Optional[_builtins.str] = ...,
        consistency_mode: Optional[_builtins.str] = ...,
        deletion_protection_enabled: Optional[_builtins.bool] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
        point_in_time_recovery: Optional[_builtins.bool] = ...,
        propagate_tags: Optional[_builtins.bool] = ...,
        stream_arn: Optional[_builtins.str] = ...,
        stream_label: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="consistencyMode")
    def consistency_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecovery")
    def point_in_time_recovery(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streamLabel")
    def stream_label(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableServerSideEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enabled: _builtins.bool, kms_key_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableTtl(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        attribute_name: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class TableWarmThroughput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        read_units_per_second: Optional[_builtins.int] = ...,
        write_units_per_second: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="readUnitsPerSecond")
    def read_units_per_second(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="writeUnitsPerSecond")
    def write_units_per_second(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GetTableAttributeResult(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableGlobalSecondaryIndexResult(dict):
    def __init__(
        __self__,
        *,
        hash_key: _builtins.str,
        key_schemas: Sequence[outputs.GetTableGlobalSecondaryIndexKeySchemaResult],
        name: _builtins.str,
        non_key_attributes: Sequence[_builtins.str],
        on_demand_throughputs: Sequence[
            outputs.GetTableGlobalSecondaryIndexOnDemandThroughputResult
        ],
        projection_type: _builtins.str,
        range_key: _builtins.str,
        read_capacity: _builtins.int,
        warm_throughputs: Sequence[
            outputs.GetTableGlobalSecondaryIndexWarmThroughputResult
        ],
        write_capacity: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hashKey")
    def hash_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keySchemas")
    def key_schemas(
        self,
    ) -> Sequence[outputs.GetTableGlobalSecondaryIndexKeySchemaResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nonKeyAttributes")
    def non_key_attributes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="onDemandThroughputs")
    def on_demand_throughputs(
        self,
    ) -> Sequence[outputs.GetTableGlobalSecondaryIndexOnDemandThroughputResult]: ...
    @_builtins.property
    @pulumi.getter(name="projectionType")
    def projection_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rangeKey")
    def range_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readCapacity")
    def read_capacity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="warmThroughputs")
    def warm_throughputs(
        self,
    ) -> Sequence[outputs.GetTableGlobalSecondaryIndexWarmThroughputResult]: ...
    @_builtins.property
    @pulumi.getter(name="writeCapacity")
    def write_capacity(self) -> _builtins.int: ...

@pulumi.output_type
class GetTableGlobalSecondaryIndexKeySchemaResult(dict):
    def __init__(
        __self__, *, attribute_name: _builtins.str, key_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableGlobalSecondaryIndexOnDemandThroughputResult(dict):
    def __init__(
        __self__,
        *,
        max_read_request_units: _builtins.int,
        max_write_request_units: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxReadRequestUnits")
    def max_read_request_units(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxWriteRequestUnits")
    def max_write_request_units(self) -> _builtins.int: ...

@pulumi.output_type
class GetTableGlobalSecondaryIndexWarmThroughputResult(dict):
    def __init__(
        __self__,
        *,
        read_units_per_second: _builtins.int,
        write_units_per_second: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="readUnitsPerSecond")
    def read_units_per_second(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="writeUnitsPerSecond")
    def write_units_per_second(self) -> _builtins.int: ...

@pulumi.output_type
class GetTableLocalSecondaryIndexResult(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        non_key_attributes: Sequence[_builtins.str],
        projection_type: _builtins.str,
        range_key: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nonKeyAttributes")
    def non_key_attributes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectionType")
    def projection_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rangeKey")
    def range_key(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableOnDemandThroughputResult(dict):
    def __init__(
        __self__,
        *,
        max_read_request_units: _builtins.int,
        max_write_request_units: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxReadRequestUnits")
    def max_read_request_units(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxWriteRequestUnits")
    def max_write_request_units(self) -> _builtins.int: ...

@pulumi.output_type
class GetTablePointInTimeRecoveryResult(dict):
    def __init__(
        __self__, *, enabled: _builtins.bool, recovery_period_in_days: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="recoveryPeriodInDays")
    def recovery_period_in_days(self) -> _builtins.int: ...

@pulumi.output_type
class GetTableReplicaResult(dict):
    def __init__(
        __self__, *, kms_key_arn: _builtins.str, region_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableServerSideEncryptionResult(dict):
    def __init__(
        __self__, *, enabled: _builtins.bool, kms_key_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableTtlResult(dict):
    def __init__(
        __self__, *, attribute_name: _builtins.str, enabled: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class GetTableWarmThroughputResult(dict):
    def __init__(
        __self__,
        *,
        read_units_per_second: _builtins.int,
        write_units_per_second: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="readUnitsPerSecond")
    def read_units_per_second(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="writeUnitsPerSecond")
    def write_units_per_second(self) -> _builtins.int: ...
