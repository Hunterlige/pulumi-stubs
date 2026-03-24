

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GlobalSecondaryIndexKeySchemaArgs', 'GlobalSecondaryIndexKeySchemaArgsDict', 'GlobalSecondaryIndexOnDemandThroughputArgs', 'GlobalSecondaryIndexOnDemandThroughputArgsDict', 'GlobalSecondaryIndexProjectionArgs', 'GlobalSecondaryIndexProjectionArgsDict', 'GlobalSecondaryIndexProvisionedThroughputArgs', 'GlobalSecondaryIndexProvisionedThroughputArgsDict', 'GlobalSecondaryIndexTimeoutsArgs', 'GlobalSecondaryIndexTimeoutsArgsDict', 'GlobalSecondaryIndexWarmThroughputArgs', 'GlobalSecondaryIndexWarmThroughputArgsDict', 'GlobalTableReplicaArgs', 'GlobalTableReplicaArgsDict', 'TableAttributeArgs', 'TableAttributeArgsDict', 'TableExportIncrementalExportSpecificationArgs', 'TableExportIncrementalExportSpecificationArgsDict', 'TableGlobalSecondaryIndexArgs', 'TableGlobalSecondaryIndexArgsDict', 'TableGlobalSecondaryIndexKeySchemaArgs', 'TableGlobalSecondaryIndexKeySchemaArgsDict', 'TableGlobalSecondaryIndexOnDemandThroughputArgs', ..., 'TableGlobalSecondaryIndexWarmThroughputArgs', 'TableGlobalSecondaryIndexWarmThroughputArgsDict', 'TableGlobalTableWitnessArgs', 'TableGlobalTableWitnessArgsDict', 'TableImportTableArgs', 'TableImportTableArgsDict', 'TableImportTableInputFormatOptionsArgs', 'TableImportTableInputFormatOptionsArgsDict', 'TableImportTableInputFormatOptionsCsvArgs', 'TableImportTableInputFormatOptionsCsvArgsDict', 'TableImportTableS3BucketSourceArgs', 'TableImportTableS3BucketSourceArgsDict', 'TableLocalSecondaryIndexArgs', 'TableLocalSecondaryIndexArgsDict', 'TableOnDemandThroughputArgs', 'TableOnDemandThroughputArgsDict', 'TablePointInTimeRecoveryArgs', 'TablePointInTimeRecoveryArgsDict', 'TableReplicaArgs', 'TableReplicaArgsDict', 'TableServerSideEncryptionArgs', 'TableServerSideEncryptionArgsDict', 'TableTtlArgs', 'TableTtlArgsDict', 'TableWarmThroughputArgs', 'TableWarmThroughputArgsDict', 'GetTableServerSideEncryptionArgs', 'GetTableServerSideEncryptionArgsDict']
class GlobalSecondaryIndexKeySchemaArgsDict(TypedDict):
    attribute_name: pulumi.Input[_builtins.str]
    attribute_type: pulumi.Input[_builtins.str]
    key_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class GlobalSecondaryIndexKeySchemaArgs:
    def __init__(__self__, *, attribute_name: pulumi.Input[_builtins.str], attribute_type: pulumi.Input[_builtins.str], key_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @attribute_name.setter
    def attribute_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @attribute_type.setter
    def attribute_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_type.setter
    def key_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class GlobalSecondaryIndexOnDemandThroughputArgsDict(TypedDict):
    max_read_request_units: NotRequired[pulumi.Input[_builtins.int]]
    max_write_request_units: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class GlobalSecondaryIndexOnDemandThroughputArgs:
    def __init__(__self__, *, max_read_request_units: Optional[pulumi.Input[_builtins.int]] = ..., max_write_request_units: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxReadRequestUnits")
    def max_read_request_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_read_request_units.setter
    def max_read_request_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxWriteRequestUnits")
    def max_write_request_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_write_request_units.setter
    def max_write_request_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class GlobalSecondaryIndexProjectionArgsDict(TypedDict):
    projection_type: pulumi.Input[_builtins.str]
    non_key_attributes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class GlobalSecondaryIndexProjectionArgs:
    def __init__(__self__, *, projection_type: pulumi.Input[_builtins.str], non_key_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectionType")
    def projection_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @projection_type.setter
    def projection_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonKeyAttributes")
    def non_key_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @non_key_attributes.setter
    def non_key_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class GlobalSecondaryIndexProvisionedThroughputArgsDict(TypedDict):
    read_capacity_units: NotRequired[pulumi.Input[_builtins.int]]
    write_capacity_units: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class GlobalSecondaryIndexProvisionedThroughputArgs:
    def __init__(__self__, *, read_capacity_units: Optional[pulumi.Input[_builtins.int]] = ..., write_capacity_units: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readCapacityUnits")
    def read_capacity_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @read_capacity_units.setter
    def read_capacity_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeCapacityUnits")
    def write_capacity_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @write_capacity_units.setter
    def write_capacity_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class GlobalSecondaryIndexTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GlobalSecondaryIndexTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GlobalSecondaryIndexWarmThroughputArgsDict(TypedDict):
    read_units_per_second: pulumi.Input[_builtins.int]
    write_units_per_second: pulumi.Input[_builtins.int]


@pulumi.input_type
class GlobalSecondaryIndexWarmThroughputArgs:
    def __init__(__self__, *, read_units_per_second: pulumi.Input[_builtins.int], write_units_per_second: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readUnitsPerSecond")
    def read_units_per_second(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @read_units_per_second.setter
    def read_units_per_second(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeUnitsPerSecond")
    def write_units_per_second(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @write_units_per_second.setter
    def write_units_per_second(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class GlobalTableReplicaArgsDict(TypedDict):
    region_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class GlobalTableReplicaArgs:
    def __init__(__self__, *, region_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region_name.setter
    def region_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TableAttributeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class TableAttributeArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]) -> None:
        
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
    


class TableExportIncrementalExportSpecificationArgsDict(TypedDict):
    export_from_time: NotRequired[pulumi.Input[_builtins.str]]
    export_to_time: NotRequired[pulumi.Input[_builtins.str]]
    export_view_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TableExportIncrementalExportSpecificationArgs:
    def __init__(__self__, *, export_from_time: Optional[pulumi.Input[_builtins.str]] = ..., export_to_time: Optional[pulumi.Input[_builtins.str]] = ..., export_view_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportFromTime")
    def export_from_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @export_from_time.setter
    def export_from_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportToTime")
    def export_to_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @export_to_time.setter
    def export_to_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportViewType")
    def export_view_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @export_view_type.setter
    def export_view_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TableGlobalSecondaryIndexArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    projection_type: pulumi.Input[_builtins.str]
    hash_key: NotRequired[pulumi.Input[_builtins.str]]
    key_schemas: NotRequired[pulumi.Input[Sequence[pulumi.Input[TableGlobalSecondaryIndexKeySchemaArgsDict]]]]
    non_key_attributes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    on_demand_throughput: NotRequired[pulumi.Input[TableGlobalSecondaryIndexOnDemandThroughputArgsDict]]
    range_key: NotRequired[pulumi.Input[_builtins.str]]
    read_capacity: NotRequired[pulumi.Input[_builtins.int]]
    warm_throughput: NotRequired[pulumi.Input[TableGlobalSecondaryIndexWarmThroughputArgsDict]]
    write_capacity: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TableGlobalSecondaryIndexArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], projection_type: pulumi.Input[_builtins.str], hash_key: Optional[pulumi.Input[_builtins.str]] = ..., key_schemas: Optional[pulumi.Input[Sequence[pulumi.Input[TableGlobalSecondaryIndexKeySchemaArgs]]]] = ..., non_key_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., on_demand_throughput: Optional[pulumi.Input[TableGlobalSecondaryIndexOnDemandThroughputArgs]] = ..., range_key: Optional[pulumi.Input[_builtins.str]] = ..., read_capacity: Optional[pulumi.Input[_builtins.int]] = ..., warm_throughput: Optional[pulumi.Input[TableGlobalSecondaryIndexWarmThroughputArgs]] = ..., write_capacity: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectionType")
    def projection_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @projection_type.setter
    def projection_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hashKey")
    @_utilities.deprecated("""hash_key is deprecated. Use key_schema instead.""")
    def hash_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hash_key.setter
    def hash_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySchemas")
    def key_schemas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TableGlobalSecondaryIndexKeySchemaArgs]]]]:
        
        ...
    
    @key_schemas.setter
    def key_schemas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TableGlobalSecondaryIndexKeySchemaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonKeyAttributes")
    def non_key_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @non_key_attributes.setter
    def non_key_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandThroughput")
    def on_demand_throughput(self) -> Optional[pulumi.Input[TableGlobalSecondaryIndexOnDemandThroughputArgs]]:
        
        ...
    
    @on_demand_throughput.setter
    def on_demand_throughput(self, value: Optional[pulumi.Input[TableGlobalSecondaryIndexOnDemandThroughputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeKey")
    @_utilities.deprecated("""range_key is deprecated. Use key_schema instead.""")
    def range_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @range_key.setter
    def range_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readCapacity")
    def read_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @read_capacity.setter
    def read_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmThroughput")
    def warm_throughput(self) -> Optional[pulumi.Input[TableGlobalSecondaryIndexWarmThroughputArgs]]:
        
        ...
    
    @warm_throughput.setter
    def warm_throughput(self, value: Optional[pulumi.Input[TableGlobalSecondaryIndexWarmThroughputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeCapacity")
    def write_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @write_capacity.setter
    def write_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TableGlobalSecondaryIndexKeySchemaArgsDict(TypedDict):
    attribute_name: pulumi.Input[_builtins.str]
    key_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class TableGlobalSecondaryIndexKeySchemaArgs:
    def __init__(__self__, *, attribute_name: pulumi.Input[_builtins.str], key_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @attribute_name.setter
    def attribute_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_type.setter
    def key_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TableGlobalSecondaryIndexOnDemandThroughputArgsDict(TypedDict):
    max_read_request_units: NotRequired[pulumi.Input[_builtins.int]]
    max_write_request_units: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TableGlobalSecondaryIndexOnDemandThroughputArgs:
    def __init__(__self__, *, max_read_request_units: Optional[pulumi.Input[_builtins.int]] = ..., max_write_request_units: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxReadRequestUnits")
    def max_read_request_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_read_request_units.setter
    def max_read_request_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxWriteRequestUnits")
    def max_write_request_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_write_request_units.setter
    def max_write_request_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TableGlobalSecondaryIndexWarmThroughputArgsDict(TypedDict):
    read_units_per_second: NotRequired[pulumi.Input[_builtins.int]]
    write_units_per_second: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TableGlobalSecondaryIndexWarmThroughputArgs:
    def __init__(__self__, *, read_units_per_second: Optional[pulumi.Input[_builtins.int]] = ..., write_units_per_second: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readUnitsPerSecond")
    def read_units_per_second(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @read_units_per_second.setter
    def read_units_per_second(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeUnitsPerSecond")
    def write_units_per_second(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @write_units_per_second.setter
    def write_units_per_second(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TableGlobalTableWitnessArgsDict(TypedDict):
    region_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TableGlobalTableWitnessArgs:
    def __init__(__self__, *, region_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region_name.setter
    def region_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TableImportTableArgsDict(TypedDict):
    input_format: pulumi.Input[_builtins.str]
    s3_bucket_source: pulumi.Input[TableImportTableS3BucketSourceArgsDict]
    input_compression_type: NotRequired[pulumi.Input[_builtins.str]]
    input_format_options: NotRequired[pulumi.Input[TableImportTableInputFormatOptionsArgsDict]]


@pulumi.input_type
class TableImportTableArgs:
    def __init__(__self__, *, input_format: pulumi.Input[_builtins.str], s3_bucket_source: pulumi.Input[TableImportTableS3BucketSourceArgs], input_compression_type: Optional[pulumi.Input[_builtins.str]] = ..., input_format_options: Optional[pulumi.Input[TableImportTableInputFormatOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @input_format.setter
    def input_format(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketSource")
    def s3_bucket_source(self) -> pulumi.Input[TableImportTableS3BucketSourceArgs]:
        
        ...
    
    @s3_bucket_source.setter
    def s3_bucket_source(self, value: pulumi.Input[TableImportTableS3BucketSourceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputCompressionType")
    def input_compression_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @input_compression_type.setter
    def input_compression_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputFormatOptions")
    def input_format_options(self) -> Optional[pulumi.Input[TableImportTableInputFormatOptionsArgs]]:
        
        ...
    
    @input_format_options.setter
    def input_format_options(self, value: Optional[pulumi.Input[TableImportTableInputFormatOptionsArgs]]): # -> None:
        ...
    


class TableImportTableInputFormatOptionsArgsDict(TypedDict):
    csv: NotRequired[pulumi.Input[TableImportTableInputFormatOptionsCsvArgsDict]]


@pulumi.input_type
class TableImportTableInputFormatOptionsArgs:
    def __init__(__self__, *, csv: Optional[pulumi.Input[TableImportTableInputFormatOptionsCsvArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def csv(self) -> Optional[pulumi.Input[TableImportTableInputFormatOptionsCsvArgs]]:
        
        ...
    
    @csv.setter
    def csv(self, value: Optional[pulumi.Input[TableImportTableInputFormatOptionsCsvArgs]]): # -> None:
        ...
    


class TableImportTableInputFormatOptionsCsvArgsDict(TypedDict):
    delimiter: NotRequired[pulumi.Input[_builtins.str]]
    header_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class TableImportTableInputFormatOptionsCsvArgs:
    def __init__(__self__, *, delimiter: Optional[pulumi.Input[_builtins.str]] = ..., header_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delimiter.setter
    def delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerLists")
    def header_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @header_lists.setter
    def header_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class TableImportTableS3BucketSourceArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    bucket_owner: NotRequired[pulumi.Input[_builtins.str]]
    key_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TableImportTableS3BucketSourceArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], bucket_owner: Optional[pulumi.Input[_builtins.str]] = ..., key_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketOwner")
    def bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_owner.setter
    def bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_prefix.setter
    def key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TableLocalSecondaryIndexArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    projection_type: pulumi.Input[_builtins.str]
    range_key: pulumi.Input[_builtins.str]
    non_key_attributes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class TableLocalSecondaryIndexArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], projection_type: pulumi.Input[_builtins.str], range_key: pulumi.Input[_builtins.str], non_key_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectionType")
    def projection_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @projection_type.setter
    def projection_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeKey")
    def range_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @range_key.setter
    def range_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonKeyAttributes")
    def non_key_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @non_key_attributes.setter
    def non_key_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class TableOnDemandThroughputArgsDict(TypedDict):
    max_read_request_units: NotRequired[pulumi.Input[_builtins.int]]
    max_write_request_units: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TableOnDemandThroughputArgs:
    def __init__(__self__, *, max_read_request_units: Optional[pulumi.Input[_builtins.int]] = ..., max_write_request_units: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxReadRequestUnits")
    def max_read_request_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_read_request_units.setter
    def max_read_request_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxWriteRequestUnits")
    def max_write_request_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_write_request_units.setter
    def max_write_request_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TablePointInTimeRecoveryArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    recovery_period_in_days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TablePointInTimeRecoveryArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], recovery_period_in_days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPeriodInDays")
    def recovery_period_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @recovery_period_in_days.setter
    def recovery_period_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TableReplicaArgsDict(TypedDict):
    region_name: pulumi.Input[_builtins.str]
    arn: NotRequired[pulumi.Input[_builtins.str]]
    consistency_mode: NotRequired[pulumi.Input[_builtins.str]]
    deletion_protection_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    point_in_time_recovery: NotRequired[pulumi.Input[_builtins.bool]]
    propagate_tags: NotRequired[pulumi.Input[_builtins.bool]]
    stream_arn: NotRequired[pulumi.Input[_builtins.str]]
    stream_label: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TableReplicaArgs:
    def __init__(__self__, *, region_name: pulumi.Input[_builtins.str], arn: Optional[pulumi.Input[_builtins.str]] = ..., consistency_mode: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., point_in_time_recovery: Optional[pulumi.Input[_builtins.bool]] = ..., propagate_tags: Optional[pulumi.Input[_builtins.bool]] = ..., stream_arn: Optional[pulumi.Input[_builtins.str]] = ..., stream_label: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region_name.setter
    def region_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consistencyMode")
    def consistency_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @consistency_mode.setter
    def consistency_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecovery")
    def point_in_time_recovery(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @point_in_time_recovery.setter
    def point_in_time_recovery(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @propagate_tags.setter
    def propagate_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stream_arn.setter
    def stream_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamLabel")
    def stream_label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stream_label.setter
    def stream_label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TableServerSideEncryptionArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TableServerSideEncryptionArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TableTtlArgsDict(TypedDict):
    attribute_name: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class TableTtlArgs:
    def __init__(__self__, *, attribute_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeName")
    def attribute_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @attribute_name.setter
    def attribute_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class TableWarmThroughputArgsDict(TypedDict):
    read_units_per_second: NotRequired[pulumi.Input[_builtins.int]]
    write_units_per_second: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TableWarmThroughputArgs:
    def __init__(__self__, *, read_units_per_second: Optional[pulumi.Input[_builtins.int]] = ..., write_units_per_second: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readUnitsPerSecond")
    def read_units_per_second(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @read_units_per_second.setter
    def read_units_per_second(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeUnitsPerSecond")
    def write_units_per_second(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @write_units_per_second.setter
    def write_units_per_second(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class GetTableServerSideEncryptionArgsDict(TypedDict):
    enabled: _builtins.bool
    kms_key_arn: _builtins.str


@pulumi.input_type
class GetTableServerSideEncryptionArgs:
    def __init__(__self__, *, enabled: _builtins.bool, kms_key_arn: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        ...
    
    @enabled.setter
    def enabled(self, value: _builtins.bool): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str:
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: _builtins.str): # -> None:
        ...
    


