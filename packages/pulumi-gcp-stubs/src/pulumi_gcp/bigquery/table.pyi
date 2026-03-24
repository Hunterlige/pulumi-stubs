

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
    def __init__(__self__, *, dataset_id: pulumi.Input[_builtins.str], table_id: pulumi.Input[_builtins.str], biglake_configuration: Optional[pulumi.Input[TableBiglakeConfigurationArgs]] = ..., clusterings: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configuration: Optional[pulumi.Input[TableEncryptionConfigurationArgs]] = ..., expiration_time: Optional[pulumi.Input[_builtins.int]] = ..., external_catalog_table_options: Optional[pulumi.Input[TableExternalCatalogTableOptionsArgs]] = ..., external_data_configuration: Optional[pulumi.Input[TableExternalDataConfigurationArgs]] = ..., friendly_name: Optional[pulumi.Input[_builtins.str]] = ..., ignore_auto_generated_schema: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_schema_changes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., materialized_view: Optional[pulumi.Input[TableMaterializedViewArgs]] = ..., max_staleness: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., range_partitioning: Optional[pulumi.Input[TableRangePartitioningArgs]] = ..., require_partition_filter: Optional[pulumi.Input[_builtins.bool]] = ..., resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., schema: Optional[pulumi.Input[_builtins.str]] = ..., schema_foreign_type_info: Optional[pulumi.Input[TableSchemaForeignTypeInfoArgs]] = ..., table_constraints: Optional[pulumi.Input[TableTableConstraintsArgs]] = ..., table_metadata_view: Optional[pulumi.Input[_builtins.str]] = ..., table_replication_info: Optional[pulumi.Input[TableTableReplicationInfoArgs]] = ..., time_partitioning: Optional[pulumi.Input[TableTimePartitioningArgs]] = ..., view: Optional[pulumi.Input[TableViewArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_id.setter
    def table_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="biglakeConfiguration")
    def biglake_configuration(self) -> Optional[pulumi.Input[TableBiglakeConfigurationArgs]]:
        
        ...
    
    @biglake_configuration.setter
    def biglake_configuration(self, value: Optional[pulumi.Input[TableBiglakeConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def clusterings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @clusterings.setter
    def clusterings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[TableEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[TableEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @expiration_time.setter
    def expiration_time(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalCatalogTableOptions")
    def external_catalog_table_options(self) -> Optional[pulumi.Input[TableExternalCatalogTableOptionsArgs]]:
        
        ...
    
    @external_catalog_table_options.setter
    def external_catalog_table_options(self, value: Optional[pulumi.Input[TableExternalCatalogTableOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalDataConfiguration")
    def external_data_configuration(self) -> Optional[pulumi.Input[TableExternalDataConfigurationArgs]]:
        
        ...
    
    @external_data_configuration.setter
    def external_data_configuration(self, value: Optional[pulumi.Input[TableExternalDataConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreAutoGeneratedSchema")
    def ignore_auto_generated_schema(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_auto_generated_schema.setter
    def ignore_auto_generated_schema(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreSchemaChanges")
    def ignore_schema_changes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ignore_schema_changes.setter
    def ignore_schema_changes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="materializedView")
    def materialized_view(self) -> Optional[pulumi.Input[TableMaterializedViewArgs]]:
        
        ...
    
    @materialized_view.setter
    def materialized_view(self, value: Optional[pulumi.Input[TableMaterializedViewArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxStaleness")
    def max_staleness(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_staleness.setter
    def max_staleness(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangePartitioning")
    def range_partitioning(self) -> Optional[pulumi.Input[TableRangePartitioningArgs]]:
        
        ...
    
    @range_partitioning.setter
    def range_partitioning(self, value: Optional[pulumi.Input[TableRangePartitioningArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requirePartitionFilter")
    def require_partition_filter(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_partition_filter.setter
    def require_partition_filter(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_tags.setter
    def resource_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaForeignTypeInfo")
    def schema_foreign_type_info(self) -> Optional[pulumi.Input[TableSchemaForeignTypeInfoArgs]]:
        
        ...
    
    @schema_foreign_type_info.setter
    def schema_foreign_type_info(self, value: Optional[pulumi.Input[TableSchemaForeignTypeInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableConstraints")
    def table_constraints(self) -> Optional[pulumi.Input[TableTableConstraintsArgs]]:
        
        ...
    
    @table_constraints.setter
    def table_constraints(self, value: Optional[pulumi.Input[TableTableConstraintsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMetadataView")
    def table_metadata_view(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_metadata_view.setter
    def table_metadata_view(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableReplicationInfo")
    def table_replication_info(self) -> Optional[pulumi.Input[TableTableReplicationInfoArgs]]:
        
        ...
    
    @table_replication_info.setter
    def table_replication_info(self, value: Optional[pulumi.Input[TableTableReplicationInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timePartitioning")
    def time_partitioning(self) -> Optional[pulumi.Input[TableTimePartitioningArgs]]:
        
        ...
    
    @time_partitioning.setter
    def time_partitioning(self, value: Optional[pulumi.Input[TableTimePartitioningArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def view(self) -> Optional[pulumi.Input[TableViewArgs]]:
        
        ...
    
    @view.setter
    def view(self, value: Optional[pulumi.Input[TableViewArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _TableState:
    def __init__(__self__, *, biglake_configuration: Optional[pulumi.Input[TableBiglakeConfigurationArgs]] = ..., clusterings: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., creation_time: Optional[pulumi.Input[_builtins.int]] = ..., dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., encryption_configuration: Optional[pulumi.Input[TableEncryptionConfigurationArgs]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., expiration_time: Optional[pulumi.Input[_builtins.int]] = ..., external_catalog_table_options: Optional[pulumi.Input[TableExternalCatalogTableOptionsArgs]] = ..., external_data_configuration: Optional[pulumi.Input[TableExternalDataConfigurationArgs]] = ..., friendly_name: Optional[pulumi.Input[_builtins.str]] = ..., generated_schema_columns: Optional[pulumi.Input[_builtins.str]] = ..., ignore_auto_generated_schema: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_schema_changes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., last_modified_time: Optional[pulumi.Input[_builtins.int]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., materialized_view: Optional[pulumi.Input[TableMaterializedViewArgs]] = ..., max_staleness: Optional[pulumi.Input[_builtins.str]] = ..., num_bytes: Optional[pulumi.Input[_builtins.int]] = ..., num_long_term_bytes: Optional[pulumi.Input[_builtins.int]] = ..., num_rows: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., range_partitioning: Optional[pulumi.Input[TableRangePartitioningArgs]] = ..., require_partition_filter: Optional[pulumi.Input[_builtins.bool]] = ..., resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., schema: Optional[pulumi.Input[_builtins.str]] = ..., schema_foreign_type_info: Optional[pulumi.Input[TableSchemaForeignTypeInfoArgs]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., table_constraints: Optional[pulumi.Input[TableTableConstraintsArgs]] = ..., table_id: Optional[pulumi.Input[_builtins.str]] = ..., table_metadata_view: Optional[pulumi.Input[_builtins.str]] = ..., table_replication_info: Optional[pulumi.Input[TableTableReplicationInfoArgs]] = ..., time_partitioning: Optional[pulumi.Input[TableTimePartitioningArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., view: Optional[pulumi.Input[TableViewArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biglakeConfiguration")
    def biglake_configuration(self) -> Optional[pulumi.Input[TableBiglakeConfigurationArgs]]:
        
        ...
    
    @biglake_configuration.setter
    def biglake_configuration(self, value: Optional[pulumi.Input[TableBiglakeConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def clusterings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @clusterings.setter
    def clusterings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[TableEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[TableEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @expiration_time.setter
    def expiration_time(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalCatalogTableOptions")
    def external_catalog_table_options(self) -> Optional[pulumi.Input[TableExternalCatalogTableOptionsArgs]]:
        
        ...
    
    @external_catalog_table_options.setter
    def external_catalog_table_options(self, value: Optional[pulumi.Input[TableExternalCatalogTableOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalDataConfiguration")
    def external_data_configuration(self) -> Optional[pulumi.Input[TableExternalDataConfigurationArgs]]:
        
        ...
    
    @external_data_configuration.setter
    def external_data_configuration(self, value: Optional[pulumi.Input[TableExternalDataConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatedSchemaColumns")
    def generated_schema_columns(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @generated_schema_columns.setter
    def generated_schema_columns(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreAutoGeneratedSchema")
    def ignore_auto_generated_schema(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_auto_generated_schema.setter
    def ignore_auto_generated_schema(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreSchemaChanges")
    def ignore_schema_changes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ignore_schema_changes.setter
    def ignore_schema_changes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @last_modified_time.setter
    def last_modified_time(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="materializedView")
    def materialized_view(self) -> Optional[pulumi.Input[TableMaterializedViewArgs]]:
        
        ...
    
    @materialized_view.setter
    def materialized_view(self, value: Optional[pulumi.Input[TableMaterializedViewArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxStaleness")
    def max_staleness(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_staleness.setter
    def max_staleness(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numBytes")
    def num_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_bytes.setter
    def num_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numLongTermBytes")
    def num_long_term_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_long_term_bytes.setter
    def num_long_term_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numRows")
    def num_rows(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_rows.setter
    def num_rows(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangePartitioning")
    def range_partitioning(self) -> Optional[pulumi.Input[TableRangePartitioningArgs]]:
        
        ...
    
    @range_partitioning.setter
    def range_partitioning(self, value: Optional[pulumi.Input[TableRangePartitioningArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requirePartitionFilter")
    def require_partition_filter(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_partition_filter.setter
    def require_partition_filter(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_tags.setter
    def resource_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaForeignTypeInfo")
    def schema_foreign_type_info(self) -> Optional[pulumi.Input[TableSchemaForeignTypeInfoArgs]]:
        
        ...
    
    @schema_foreign_type_info.setter
    def schema_foreign_type_info(self, value: Optional[pulumi.Input[TableSchemaForeignTypeInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableConstraints")
    def table_constraints(self) -> Optional[pulumi.Input[TableTableConstraintsArgs]]:
        
        ...
    
    @table_constraints.setter
    def table_constraints(self, value: Optional[pulumi.Input[TableTableConstraintsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_id.setter
    def table_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMetadataView")
    def table_metadata_view(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_metadata_view.setter
    def table_metadata_view(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableReplicationInfo")
    def table_replication_info(self) -> Optional[pulumi.Input[TableTableReplicationInfoArgs]]:
        
        ...
    
    @table_replication_info.setter
    def table_replication_info(self, value: Optional[pulumi.Input[TableTableReplicationInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timePartitioning")
    def time_partitioning(self) -> Optional[pulumi.Input[TableTimePartitioningArgs]]:
        
        ...
    
    @time_partitioning.setter
    def time_partitioning(self, value: Optional[pulumi.Input[TableTimePartitioningArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def view(self) -> Optional[pulumi.Input[TableViewArgs]]:
        
        ...
    
    @view.setter
    def view(self, value: Optional[pulumi.Input[TableViewArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:bigquery/table:Table")
class Table(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., biglake_configuration: Optional[pulumi.Input[Union[TableBiglakeConfigurationArgs, TableBiglakeConfigurationArgsDict]]] = ..., clusterings: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configuration: Optional[pulumi.Input[Union[TableEncryptionConfigurationArgs, TableEncryptionConfigurationArgsDict]]] = ..., expiration_time: Optional[pulumi.Input[_builtins.int]] = ..., external_catalog_table_options: Optional[pulumi.Input[Union[TableExternalCatalogTableOptionsArgs, TableExternalCatalogTableOptionsArgsDict]]] = ..., external_data_configuration: Optional[pulumi.Input[Union[TableExternalDataConfigurationArgs, TableExternalDataConfigurationArgsDict]]] = ..., friendly_name: Optional[pulumi.Input[_builtins.str]] = ..., ignore_auto_generated_schema: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_schema_changes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., materialized_view: Optional[pulumi.Input[Union[TableMaterializedViewArgs, TableMaterializedViewArgsDict]]] = ..., max_staleness: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., range_partitioning: Optional[pulumi.Input[Union[TableRangePartitioningArgs, TableRangePartitioningArgsDict]]] = ..., require_partition_filter: Optional[pulumi.Input[_builtins.bool]] = ..., resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., schema: Optional[pulumi.Input[_builtins.str]] = ..., schema_foreign_type_info: Optional[pulumi.Input[Union[TableSchemaForeignTypeInfoArgs, TableSchemaForeignTypeInfoArgsDict]]] = ..., table_constraints: Optional[pulumi.Input[Union[TableTableConstraintsArgs, TableTableConstraintsArgsDict]]] = ..., table_id: Optional[pulumi.Input[_builtins.str]] = ..., table_metadata_view: Optional[pulumi.Input[_builtins.str]] = ..., table_replication_info: Optional[pulumi.Input[Union[TableTableReplicationInfoArgs, TableTableReplicationInfoArgsDict]]] = ..., time_partitioning: Optional[pulumi.Input[Union[TableTimePartitioningArgs, TableTimePartitioningArgsDict]]] = ..., view: Optional[pulumi.Input[Union[TableViewArgs, TableViewArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TableArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., biglake_configuration: Optional[pulumi.Input[Union[TableBiglakeConfigurationArgs, TableBiglakeConfigurationArgsDict]]] = ..., clusterings: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., creation_time: Optional[pulumi.Input[_builtins.int]] = ..., dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., encryption_configuration: Optional[pulumi.Input[Union[TableEncryptionConfigurationArgs, TableEncryptionConfigurationArgsDict]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., expiration_time: Optional[pulumi.Input[_builtins.int]] = ..., external_catalog_table_options: Optional[pulumi.Input[Union[TableExternalCatalogTableOptionsArgs, TableExternalCatalogTableOptionsArgsDict]]] = ..., external_data_configuration: Optional[pulumi.Input[Union[TableExternalDataConfigurationArgs, TableExternalDataConfigurationArgsDict]]] = ..., friendly_name: Optional[pulumi.Input[_builtins.str]] = ..., generated_schema_columns: Optional[pulumi.Input[_builtins.str]] = ..., ignore_auto_generated_schema: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_schema_changes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., last_modified_time: Optional[pulumi.Input[_builtins.int]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., materialized_view: Optional[pulumi.Input[Union[TableMaterializedViewArgs, TableMaterializedViewArgsDict]]] = ..., max_staleness: Optional[pulumi.Input[_builtins.str]] = ..., num_bytes: Optional[pulumi.Input[_builtins.int]] = ..., num_long_term_bytes: Optional[pulumi.Input[_builtins.int]] = ..., num_rows: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., range_partitioning: Optional[pulumi.Input[Union[TableRangePartitioningArgs, TableRangePartitioningArgsDict]]] = ..., require_partition_filter: Optional[pulumi.Input[_builtins.bool]] = ..., resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., schema: Optional[pulumi.Input[_builtins.str]] = ..., schema_foreign_type_info: Optional[pulumi.Input[Union[TableSchemaForeignTypeInfoArgs, TableSchemaForeignTypeInfoArgsDict]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., table_constraints: Optional[pulumi.Input[Union[TableTableConstraintsArgs, TableTableConstraintsArgsDict]]] = ..., table_id: Optional[pulumi.Input[_builtins.str]] = ..., table_metadata_view: Optional[pulumi.Input[_builtins.str]] = ..., table_replication_info: Optional[pulumi.Input[Union[TableTableReplicationInfoArgs, TableTableReplicationInfoArgsDict]]] = ..., time_partitioning: Optional[pulumi.Input[Union[TableTimePartitioningArgs, TableTimePartitioningArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., view: Optional[pulumi.Input[Union[TableViewArgs, TableViewArgsDict]]] = ...) -> Table:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biglakeConfiguration")
    def biglake_configuration(self) -> pulumi.Output[Optional[outputs.TableBiglakeConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def clusterings(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> pulumi.Output[Optional[outputs.TableEncryptionConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalCatalogTableOptions")
    def external_catalog_table_options(self) -> pulumi.Output[Optional[outputs.TableExternalCatalogTableOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalDataConfiguration")
    def external_data_configuration(self) -> pulumi.Output[Optional[outputs.TableExternalDataConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatedSchemaColumns")
    def generated_schema_columns(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreAutoGeneratedSchema")
    def ignore_auto_generated_schema(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreSchemaChanges")
    def ignore_schema_changes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="materializedView")
    def materialized_view(self) -> pulumi.Output[Optional[outputs.TableMaterializedView]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxStaleness")
    def max_staleness(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numBytes")
    def num_bytes(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numLongTermBytes")
    def num_long_term_bytes(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numRows")
    def num_rows(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangePartitioning")
    def range_partitioning(self) -> pulumi.Output[Optional[outputs.TableRangePartitioning]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requirePartitionFilter")
    def require_partition_filter(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaForeignTypeInfo")
    def schema_foreign_type_info(self) -> pulumi.Output[Optional[outputs.TableSchemaForeignTypeInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableConstraints")
    def table_constraints(self) -> pulumi.Output[Optional[outputs.TableTableConstraints]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableMetadataView")
    def table_metadata_view(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableReplicationInfo")
    def table_replication_info(self) -> pulumi.Output[Optional[outputs.TableTableReplicationInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timePartitioning")
    def time_partitioning(self) -> pulumi.Output[Optional[outputs.TableTimePartitioning]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def view(self) -> pulumi.Output[Optional[outputs.TableView]]:
        
        ...
    


