

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TableArgs', 'Table']
@pulumi.input_type
class TableArgs:
    def __init__(__self__, *, attributes: Optional[pulumi.Input[Sequence[pulumi.Input[TableAttributeArgs]]]] = ..., billing_mode: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., global_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[TableGlobalSecondaryIndexArgs]]]] = ..., global_table_witness: Optional[pulumi.Input[TableGlobalTableWitnessArgs]] = ..., hash_key: Optional[pulumi.Input[_builtins.str]] = ..., import_table: Optional[pulumi.Input[TableImportTableArgs]] = ..., local_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[TableLocalSecondaryIndexArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., on_demand_throughput: Optional[pulumi.Input[TableOnDemandThroughputArgs]] = ..., point_in_time_recovery: Optional[pulumi.Input[TablePointInTimeRecoveryArgs]] = ..., range_key: Optional[pulumi.Input[_builtins.str]] = ..., read_capacity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replicas: Optional[pulumi.Input[Sequence[pulumi.Input[TableReplicaArgs]]]] = ..., restore_date_time: Optional[pulumi.Input[_builtins.str]] = ..., restore_source_name: Optional[pulumi.Input[_builtins.str]] = ..., restore_source_table_arn: Optional[pulumi.Input[_builtins.str]] = ..., restore_to_latest_time: Optional[pulumi.Input[_builtins.bool]] = ..., server_side_encryption: Optional[pulumi.Input[TableServerSideEncryptionArgs]] = ..., stream_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., stream_view_type: Optional[pulumi.Input[_builtins.str]] = ..., table_class: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ttl: Optional[pulumi.Input[TableTtlArgs]] = ..., warm_throughput: Optional[pulumi.Input[TableWarmThroughputArgs]] = ..., write_capacity: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TableAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TableAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @billing_mode.setter
    def billing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TableGlobalSecondaryIndexArgs]]]]:
        
        ...
    
    @global_secondary_indexes.setter
    def global_secondary_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TableGlobalSecondaryIndexArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalTableWitness")
    def global_table_witness(self) -> Optional[pulumi.Input[TableGlobalTableWitnessArgs]]:
        
        ...
    
    @global_table_witness.setter
    def global_table_witness(self, value: Optional[pulumi.Input[TableGlobalTableWitnessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hashKey")
    def hash_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hash_key.setter
    def hash_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importTable")
    def import_table(self) -> Optional[pulumi.Input[TableImportTableArgs]]:
        
        ...
    
    @import_table.setter
    def import_table(self, value: Optional[pulumi.Input[TableImportTableArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localSecondaryIndexes")
    def local_secondary_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TableLocalSecondaryIndexArgs]]]]:
        
        ...
    
    @local_secondary_indexes.setter
    def local_secondary_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TableLocalSecondaryIndexArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandThroughput")
    def on_demand_throughput(self) -> Optional[pulumi.Input[TableOnDemandThroughputArgs]]:
        
        ...
    
    @on_demand_throughput.setter
    def on_demand_throughput(self, value: Optional[pulumi.Input[TableOnDemandThroughputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecovery")
    def point_in_time_recovery(self) -> Optional[pulumi.Input[TablePointInTimeRecoveryArgs]]:
        
        ...
    
    @point_in_time_recovery.setter
    def point_in_time_recovery(self, value: Optional[pulumi.Input[TablePointInTimeRecoveryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeKey")
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TableReplicaArgs]]]]:
        
        ...
    
    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TableReplicaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreDateTime")
    def restore_date_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_date_time.setter
    def restore_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreSourceName")
    def restore_source_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_source_name.setter
    def restore_source_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreSourceTableArn")
    def restore_source_table_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_source_table_arn.setter
    def restore_source_table_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreToLatestTime")
    def restore_to_latest_time(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @restore_to_latest_time.setter
    def restore_to_latest_time(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> Optional[pulumi.Input[TableServerSideEncryptionArgs]]:
        
        ...
    
    @server_side_encryption.setter
    def server_side_encryption(self, value: Optional[pulumi.Input[TableServerSideEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamEnabled")
    def stream_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @stream_enabled.setter
    def stream_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamViewType")
    def stream_view_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stream_view_type.setter
    def stream_view_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableClass")
    def table_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_class.setter
    def table_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[TableTtlArgs]]:
        
        ...
    
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[TableTtlArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmThroughput")
    def warm_throughput(self) -> Optional[pulumi.Input[TableWarmThroughputArgs]]:
        
        ...
    
    @warm_throughput.setter
    def warm_throughput(self, value: Optional[pulumi.Input[TableWarmThroughputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeCapacity")
    def write_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @write_capacity.setter
    def write_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _TableState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[TableAttributeArgs]]]] = ..., billing_mode: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., global_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[TableGlobalSecondaryIndexArgs]]]] = ..., global_table_witness: Optional[pulumi.Input[TableGlobalTableWitnessArgs]] = ..., hash_key: Optional[pulumi.Input[_builtins.str]] = ..., import_table: Optional[pulumi.Input[TableImportTableArgs]] = ..., local_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[TableLocalSecondaryIndexArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., on_demand_throughput: Optional[pulumi.Input[TableOnDemandThroughputArgs]] = ..., point_in_time_recovery: Optional[pulumi.Input[TablePointInTimeRecoveryArgs]] = ..., range_key: Optional[pulumi.Input[_builtins.str]] = ..., read_capacity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replicas: Optional[pulumi.Input[Sequence[pulumi.Input[TableReplicaArgs]]]] = ..., restore_date_time: Optional[pulumi.Input[_builtins.str]] = ..., restore_source_name: Optional[pulumi.Input[_builtins.str]] = ..., restore_source_table_arn: Optional[pulumi.Input[_builtins.str]] = ..., restore_to_latest_time: Optional[pulumi.Input[_builtins.bool]] = ..., server_side_encryption: Optional[pulumi.Input[TableServerSideEncryptionArgs]] = ..., stream_arn: Optional[pulumi.Input[_builtins.str]] = ..., stream_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., stream_label: Optional[pulumi.Input[_builtins.str]] = ..., stream_view_type: Optional[pulumi.Input[_builtins.str]] = ..., table_class: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ttl: Optional[pulumi.Input[TableTtlArgs]] = ..., warm_throughput: Optional[pulumi.Input[TableWarmThroughputArgs]] = ..., write_capacity: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TableAttributeArgs]]]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TableAttributeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @billing_mode.setter
    def billing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TableGlobalSecondaryIndexArgs]]]]:
        
        ...
    
    @global_secondary_indexes.setter
    def global_secondary_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TableGlobalSecondaryIndexArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalTableWitness")
    def global_table_witness(self) -> Optional[pulumi.Input[TableGlobalTableWitnessArgs]]:
        
        ...
    
    @global_table_witness.setter
    def global_table_witness(self, value: Optional[pulumi.Input[TableGlobalTableWitnessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hashKey")
    def hash_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hash_key.setter
    def hash_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importTable")
    def import_table(self) -> Optional[pulumi.Input[TableImportTableArgs]]:
        
        ...
    
    @import_table.setter
    def import_table(self, value: Optional[pulumi.Input[TableImportTableArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localSecondaryIndexes")
    def local_secondary_indexes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TableLocalSecondaryIndexArgs]]]]:
        
        ...
    
    @local_secondary_indexes.setter
    def local_secondary_indexes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TableLocalSecondaryIndexArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandThroughput")
    def on_demand_throughput(self) -> Optional[pulumi.Input[TableOnDemandThroughputArgs]]:
        
        ...
    
    @on_demand_throughput.setter
    def on_demand_throughput(self, value: Optional[pulumi.Input[TableOnDemandThroughputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecovery")
    def point_in_time_recovery(self) -> Optional[pulumi.Input[TablePointInTimeRecoveryArgs]]:
        
        ...
    
    @point_in_time_recovery.setter
    def point_in_time_recovery(self, value: Optional[pulumi.Input[TablePointInTimeRecoveryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeKey")
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TableReplicaArgs]]]]:
        
        ...
    
    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TableReplicaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreDateTime")
    def restore_date_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_date_time.setter
    def restore_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreSourceName")
    def restore_source_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_source_name.setter
    def restore_source_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreSourceTableArn")
    def restore_source_table_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_source_table_arn.setter
    def restore_source_table_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreToLatestTime")
    def restore_to_latest_time(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @restore_to_latest_time.setter
    def restore_to_latest_time(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> Optional[pulumi.Input[TableServerSideEncryptionArgs]]:
        
        ...
    
    @server_side_encryption.setter
    def server_side_encryption(self, value: Optional[pulumi.Input[TableServerSideEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stream_arn.setter
    def stream_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamEnabled")
    def stream_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @stream_enabled.setter
    def stream_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamLabel")
    def stream_label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stream_label.setter
    def stream_label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamViewType")
    def stream_view_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stream_view_type.setter
    def stream_view_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableClass")
    def table_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_class.setter
    def table_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[TableTtlArgs]]:
        
        ...
    
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[TableTtlArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmThroughput")
    def warm_throughput(self) -> Optional[pulumi.Input[TableWarmThroughputArgs]]:
        
        ...
    
    @warm_throughput.setter
    def warm_throughput(self, value: Optional[pulumi.Input[TableWarmThroughputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeCapacity")
    def write_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @write_capacity.setter
    def write_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("aws:dynamodb/table:Table")
class Table(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TableAttributeArgs, TableAttributeArgsDict]]]]] = ..., billing_mode: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., global_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TableGlobalSecondaryIndexArgs, TableGlobalSecondaryIndexArgsDict]]]]] = ..., global_table_witness: Optional[pulumi.Input[Union[TableGlobalTableWitnessArgs, TableGlobalTableWitnessArgsDict]]] = ..., hash_key: Optional[pulumi.Input[_builtins.str]] = ..., import_table: Optional[pulumi.Input[Union[TableImportTableArgs, TableImportTableArgsDict]]] = ..., local_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TableLocalSecondaryIndexArgs, TableLocalSecondaryIndexArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., on_demand_throughput: Optional[pulumi.Input[Union[TableOnDemandThroughputArgs, TableOnDemandThroughputArgsDict]]] = ..., point_in_time_recovery: Optional[pulumi.Input[Union[TablePointInTimeRecoveryArgs, TablePointInTimeRecoveryArgsDict]]] = ..., range_key: Optional[pulumi.Input[_builtins.str]] = ..., read_capacity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replicas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TableReplicaArgs, TableReplicaArgsDict]]]]] = ..., restore_date_time: Optional[pulumi.Input[_builtins.str]] = ..., restore_source_name: Optional[pulumi.Input[_builtins.str]] = ..., restore_source_table_arn: Optional[pulumi.Input[_builtins.str]] = ..., restore_to_latest_time: Optional[pulumi.Input[_builtins.bool]] = ..., server_side_encryption: Optional[pulumi.Input[Union[TableServerSideEncryptionArgs, TableServerSideEncryptionArgsDict]]] = ..., stream_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., stream_view_type: Optional[pulumi.Input[_builtins.str]] = ..., table_class: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ttl: Optional[pulumi.Input[Union[TableTtlArgs, TableTtlArgsDict]]] = ..., warm_throughput: Optional[pulumi.Input[Union[TableWarmThroughputArgs, TableWarmThroughputArgsDict]]] = ..., write_capacity: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[TableArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., attributes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TableAttributeArgs, TableAttributeArgsDict]]]]] = ..., billing_mode: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., global_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TableGlobalSecondaryIndexArgs, TableGlobalSecondaryIndexArgsDict]]]]] = ..., global_table_witness: Optional[pulumi.Input[Union[TableGlobalTableWitnessArgs, TableGlobalTableWitnessArgsDict]]] = ..., hash_key: Optional[pulumi.Input[_builtins.str]] = ..., import_table: Optional[pulumi.Input[Union[TableImportTableArgs, TableImportTableArgsDict]]] = ..., local_secondary_indexes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TableLocalSecondaryIndexArgs, TableLocalSecondaryIndexArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., on_demand_throughput: Optional[pulumi.Input[Union[TableOnDemandThroughputArgs, TableOnDemandThroughputArgsDict]]] = ..., point_in_time_recovery: Optional[pulumi.Input[Union[TablePointInTimeRecoveryArgs, TablePointInTimeRecoveryArgsDict]]] = ..., range_key: Optional[pulumi.Input[_builtins.str]] = ..., read_capacity: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replicas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TableReplicaArgs, TableReplicaArgsDict]]]]] = ..., restore_date_time: Optional[pulumi.Input[_builtins.str]] = ..., restore_source_name: Optional[pulumi.Input[_builtins.str]] = ..., restore_source_table_arn: Optional[pulumi.Input[_builtins.str]] = ..., restore_to_latest_time: Optional[pulumi.Input[_builtins.bool]] = ..., server_side_encryption: Optional[pulumi.Input[Union[TableServerSideEncryptionArgs, TableServerSideEncryptionArgsDict]]] = ..., stream_arn: Optional[pulumi.Input[_builtins.str]] = ..., stream_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., stream_label: Optional[pulumi.Input[_builtins.str]] = ..., stream_view_type: Optional[pulumi.Input[_builtins.str]] = ..., table_class: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ttl: Optional[pulumi.Input[Union[TableTtlArgs, TableTtlArgsDict]]] = ..., warm_throughput: Optional[pulumi.Input[Union[TableWarmThroughputArgs, TableWarmThroughputArgsDict]]] = ..., write_capacity: Optional[pulumi.Input[_builtins.int]] = ...) -> Table:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Sequence[outputs.TableAttribute]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> pulumi.Output[Sequence[outputs.TableGlobalSecondaryIndex]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalTableWitness")
    def global_table_witness(self) -> pulumi.Output[outputs.TableGlobalTableWitness]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hashKey")
    def hash_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importTable")
    def import_table(self) -> pulumi.Output[Optional[outputs.TableImportTable]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localSecondaryIndexes")
    def local_secondary_indexes(self) -> pulumi.Output[Optional[Sequence[outputs.TableLocalSecondaryIndex]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onDemandThroughput")
    def on_demand_throughput(self) -> pulumi.Output[Optional[outputs.TableOnDemandThroughput]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pointInTimeRecovery")
    def point_in_time_recovery(self) -> pulumi.Output[outputs.TablePointInTimeRecovery]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeKey")
    def range_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readCapacity")
    def read_capacity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> pulumi.Output[Optional[Sequence[outputs.TableReplica]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreDateTime")
    def restore_date_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreSourceName")
    def restore_source_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreSourceTableArn")
    def restore_source_table_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restoreToLatestTime")
    def restore_to_latest_time(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> pulumi.Output[outputs.TableServerSideEncryption]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamEnabled")
    def stream_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamLabel")
    def stream_label(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamViewType")
    def stream_view_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableClass")
    def table_class(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[outputs.TableTtl]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="warmThroughput")
    def warm_throughput(self) -> pulumi.Output[outputs.TableWarmThroughput]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeCapacity")
    def write_capacity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


