

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CatalogDatabaseCreateTableDefaultPermissionArgs', ..., ..., ..., 'CatalogDatabaseFederatedDatabaseArgs', 'CatalogDatabaseFederatedDatabaseArgsDict', 'CatalogDatabaseTargetDatabaseArgs', 'CatalogDatabaseTargetDatabaseArgsDict', 'CatalogTableOpenTableFormatInputArgs', 'CatalogTableOpenTableFormatInputArgsDict', 'CatalogTableOpenTableFormatInputIcebergInputArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'CatalogTableOptimizerConfigurationArgs', 'CatalogTableOptimizerConfigurationArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'CatalogTablePartitionIndexArgs', 'CatalogTablePartitionIndexArgsDict', 'CatalogTablePartitionKeyArgs', 'CatalogTablePartitionKeyArgsDict', 'CatalogTableStorageDescriptorArgs', 'CatalogTableStorageDescriptorArgsDict', 'CatalogTableStorageDescriptorColumnArgs', 'CatalogTableStorageDescriptorColumnArgsDict', 'CatalogTableStorageDescriptorSchemaReferenceArgs', ..., ..., ..., 'CatalogTableStorageDescriptorSerDeInfoArgs', 'CatalogTableStorageDescriptorSerDeInfoArgsDict', 'CatalogTableStorageDescriptorSkewedInfoArgs', 'CatalogTableStorageDescriptorSkewedInfoArgsDict', 'CatalogTableStorageDescriptorSortColumnArgs', 'CatalogTableStorageDescriptorSortColumnArgsDict', 'CatalogTableTargetTableArgs', 'CatalogTableTargetTableArgsDict', 'CatalogTableViewDefinitionArgs', 'CatalogTableViewDefinitionArgsDict', 'CatalogTableViewDefinitionRepresentationArgs', 'CatalogTableViewDefinitionRepresentationArgsDict', 'ClassifierCsvClassifierArgs', 'ClassifierCsvClassifierArgsDict', 'ClassifierGrokClassifierArgs', 'ClassifierGrokClassifierArgsDict', 'ClassifierJsonClassifierArgs', 'ClassifierJsonClassifierArgsDict', 'ClassifierXmlClassifierArgs', 'ClassifierXmlClassifierArgsDict', 'ConnectionPhysicalConnectionRequirementsArgs', 'ConnectionPhysicalConnectionRequirementsArgsDict', 'CrawlerCatalogTargetArgs', 'CrawlerCatalogTargetArgsDict', 'CrawlerDeltaTargetArgs', 'CrawlerDeltaTargetArgsDict', 'CrawlerDynamodbTargetArgs', 'CrawlerDynamodbTargetArgsDict', 'CrawlerHudiTargetArgs', 'CrawlerHudiTargetArgsDict', 'CrawlerIcebergTargetArgs', 'CrawlerIcebergTargetArgsDict', 'CrawlerJdbcTargetArgs', 'CrawlerJdbcTargetArgsDict', 'CrawlerLakeFormationConfigurationArgs', 'CrawlerLakeFormationConfigurationArgsDict', 'CrawlerLineageConfigurationArgs', 'CrawlerLineageConfigurationArgsDict', 'CrawlerMongodbTargetArgs', 'CrawlerMongodbTargetArgsDict', 'CrawlerRecrawlPolicyArgs', 'CrawlerRecrawlPolicyArgsDict', 'CrawlerS3TargetArgs', 'CrawlerS3TargetArgsDict', 'CrawlerSchemaChangePolicyArgs', 'CrawlerSchemaChangePolicyArgsDict', ..., ..., ..., ..., ..., ..., 'DataQualityRulesetTargetTableArgs', 'DataQualityRulesetTargetTableArgsDict', 'JobCommandArgs', 'JobCommandArgsDict', 'JobExecutionPropertyArgs', 'JobExecutionPropertyArgsDict', 'JobNotificationPropertyArgs', 'JobNotificationPropertyArgsDict', 'JobSourceControlDetailsArgs', 'JobSourceControlDetailsArgsDict', 'MLTransformInputRecordTableArgs', 'MLTransformInputRecordTableArgsDict', 'MLTransformParametersArgs', 'MLTransformParametersArgsDict', 'MLTransformParametersFindMatchesParametersArgs', 'MLTransformParametersFindMatchesParametersArgsDict', 'MLTransformSchemaArgs', 'MLTransformSchemaArgsDict', 'PartitionIndexPartitionIndexArgs', 'PartitionIndexPartitionIndexArgsDict', 'PartitionStorageDescriptorArgs', 'PartitionStorageDescriptorArgsDict', 'PartitionStorageDescriptorColumnArgs', 'PartitionStorageDescriptorColumnArgsDict', 'PartitionStorageDescriptorSerDeInfoArgs', 'PartitionStorageDescriptorSerDeInfoArgsDict', 'PartitionStorageDescriptorSkewedInfoArgs', 'PartitionStorageDescriptorSkewedInfoArgsDict', 'PartitionStorageDescriptorSortColumnArgs', 'PartitionStorageDescriptorSortColumnArgsDict', 'SecurityConfigurationEncryptionConfigurationArgs', ..., ..., ..., ..., ..., ..., ..., 'TriggerActionArgs', 'TriggerActionArgsDict', 'TriggerActionNotificationPropertyArgs', 'TriggerActionNotificationPropertyArgsDict', 'TriggerEventBatchingConditionArgs', 'TriggerEventBatchingConditionArgsDict', 'TriggerPredicateArgs', 'TriggerPredicateArgsDict', 'TriggerPredicateConditionArgs', 'TriggerPredicateConditionArgsDict', 'UserDefinedFunctionResourceUriArgs', 'UserDefinedFunctionResourceUriArgsDict', 'GetScriptDagEdgeArgs', 'GetScriptDagEdgeArgsDict', 'GetScriptDagNodeArgs', 'GetScriptDagNodeArgsDict', 'GetScriptDagNodeArgArgs', 'GetScriptDagNodeArgArgsDict']
class CatalogDatabaseCreateTableDefaultPermissionArgsDict(TypedDict):
    permissions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    principal: NotRequired[pulumi.Input[CatalogDatabaseCreateTableDefaultPermissionPrincipalArgsDict]]


@pulumi.input_type
class CatalogDatabaseCreateTableDefaultPermissionArgs:
    def __init__(__self__, *, permissions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., principal: Optional[pulumi.Input[CatalogDatabaseCreateTableDefaultPermissionPrincipalArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[CatalogDatabaseCreateTableDefaultPermissionPrincipalArgs]]:
        
        ...
    
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[CatalogDatabaseCreateTableDefaultPermissionPrincipalArgs]]): # -> None:
        ...
    


class CatalogDatabaseCreateTableDefaultPermissionPrincipalArgsDict(TypedDict):
    data_lake_principal_identifier: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogDatabaseCreateTableDefaultPermissionPrincipalArgs:
    def __init__(__self__, *, data_lake_principal_identifier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLakePrincipalIdentifier")
    def data_lake_principal_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_lake_principal_identifier.setter
    def data_lake_principal_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogDatabaseFederatedDatabaseArgsDict(TypedDict):
    connection_name: NotRequired[pulumi.Input[_builtins.str]]
    identifier: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogDatabaseFederatedDatabaseArgs:
    def __init__(__self__, *, connection_name: Optional[pulumi.Input[_builtins.str]] = ..., identifier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogDatabaseTargetDatabaseArgsDict(TypedDict):
    catalog_id: pulumi.Input[_builtins.str]
    database_name: pulumi.Input[_builtins.str]
    region: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogDatabaseTargetDatabaseArgs:
    def __init__(__self__, *, catalog_id: pulumi.Input[_builtins.str], database_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @catalog_id.setter
    def catalog_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogTableOpenTableFormatInputArgsDict(TypedDict):
    iceberg_input: pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputArgsDict]


@pulumi.input_type
class CatalogTableOpenTableFormatInputArgs:
    def __init__(__self__, *, iceberg_input: pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icebergInput")
    def iceberg_input(self) -> pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputArgs]:
        
        ...
    
    @iceberg_input.setter
    def iceberg_input(self, value: pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputArgs]): # -> None:
        ...
    


class CatalogTableOpenTableFormatInputIcebergInputArgsDict(TypedDict):
    metadata_operation: pulumi.Input[_builtins.str]
    iceberg_table_input: NotRequired[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputArgsDict]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogTableOpenTableFormatInputIcebergInputArgs:
    def __init__(__self__, *, metadata_operation: pulumi.Input[_builtins.str], iceberg_table_input: Optional[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputArgs]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOperation")
    def metadata_operation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @metadata_operation.setter
    def metadata_operation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="icebergTableInput")
    def iceberg_table_input(self) -> Optional[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputArgs]]:
        
        ...
    
    @iceberg_table_input.setter
    def iceberg_table_input(self, value: Optional[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]
    schema: pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaArgsDict]
    partition_spec: NotRequired[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecArgsDict]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    sort_order: NotRequired[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderArgsDict]]


@pulumi.input_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], schema: pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaArgs], partition_spec: Optional[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecArgs]] = ..., properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., sort_order: Optional[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaArgs]:
        
        ...
    
    @schema.setter
    def schema(self, value: pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionSpec")
    def partition_spec(self) -> Optional[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecArgs]]:
        
        ...
    
    @partition_spec.setter
    def partition_spec(self, value: Optional[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> Optional[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderArgs]]:
        
        ...
    
    @sort_order.setter
    def sort_order(self, value: Optional[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderArgs]]): # -> None:
        ...
    


class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecArgsDict(TypedDict):
    fields: pulumi.Input[Sequence[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecFieldArgsDict]]]
    spec_id: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecArgs:
    def __init__(__self__, *, fields: pulumi.Input[Sequence[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecFieldArgs]]], spec_id: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecFieldArgs]]]:
        
        ...
    
    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecFieldArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="specId")
    def spec_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @spec_id.setter
    def spec_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecFieldArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    source_id: pulumi.Input[_builtins.int]
    transform: pulumi.Input[_builtins.str]
    field_id: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecFieldArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], source_id: pulumi.Input[_builtins.int], transform: pulumi.Input[_builtins.str], field_id: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Input[_builtins.int]:
        ...
    
    @source_id.setter
    def source_id(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transform(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @transform.setter
    def transform(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldId")
    def field_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @field_id.setter
    def field_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaArgsDict(TypedDict):
    fields: pulumi.Input[Sequence[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaFieldArgsDict]]]
    identifier_field_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    schema_id: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaArgs:
    def __init__(__self__, *, fields: pulumi.Input[Sequence[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaFieldArgs]]], identifier_field_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., schema_id: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaFieldArgs]]]:
        
        ...
    
    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaFieldArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identifierFieldIds")
    def identifier_field_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @identifier_field_ids.setter
    def identifier_field_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaId")
    def schema_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @schema_id.setter
    def schema_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaFieldArgsDict(TypedDict):
    id: pulumi.Input[_builtins.int]
    name: pulumi.Input[_builtins.str]
    required: pulumi.Input[_builtins.bool]
    type: pulumi.Input[_builtins.str]
    doc: NotRequired[pulumi.Input[_builtins.str]]
    initial_default: NotRequired[pulumi.Input[_builtins.str]]
    write_default: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaFieldArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.int], name: pulumi.Input[_builtins.str], required: pulumi.Input[_builtins.bool], type: pulumi.Input[_builtins.str], doc: Optional[pulumi.Input[_builtins.str]] = ..., initial_default: Optional[pulumi.Input[_builtins.str]] = ..., write_default: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.int]): # -> None:
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
    def required(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @required.setter
    def required(self, value: pulumi.Input[_builtins.bool]): # -> None:
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
    def doc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @doc.setter
    def doc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDefault")
    def initial_default(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @initial_default.setter
    def initial_default(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeDefault")
    def write_default(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @write_default.setter
    def write_default(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderArgsDict(TypedDict):
    fields: pulumi.Input[Sequence[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderFieldArgsDict]]]
    order_id: pulumi.Input[_builtins.int]


@pulumi.input_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderArgs:
    def __init__(__self__, *, fields: pulumi.Input[Sequence[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderFieldArgs]]], order_id: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderFieldArgs]]]:
        
        ...
    
    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input[CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderFieldArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orderId")
    def order_id(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @order_id.setter
    def order_id(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderFieldArgsDict(TypedDict):
    direction: pulumi.Input[_builtins.str]
    null_order: pulumi.Input[_builtins.str]
    source_id: pulumi.Input[_builtins.int]
    transform: pulumi.Input[_builtins.str]


@pulumi.input_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderFieldArgs:
    def __init__(__self__, *, direction: pulumi.Input[_builtins.str], null_order: pulumi.Input[_builtins.str], source_id: pulumi.Input[_builtins.int], transform: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @direction.setter
    def direction(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nullOrder")
    def null_order(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @null_order.setter
    def null_order(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Input[_builtins.int]:
        ...
    
    @source_id.setter
    def source_id(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transform(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @transform.setter
    def transform(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CatalogTableOptimizerConfigurationArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    role_arn: pulumi.Input[_builtins.str]
    orphan_file_deletion_configuration: NotRequired[pulumi.Input[CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationArgsDict]]
    retention_configuration: NotRequired[pulumi.Input[CatalogTableOptimizerConfigurationRetentionConfigurationArgsDict]]


@pulumi.input_type
class CatalogTableOptimizerConfigurationArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], role_arn: pulumi.Input[_builtins.str], orphan_file_deletion_configuration: Optional[pulumi.Input[CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationArgs]] = ..., retention_configuration: Optional[pulumi.Input[CatalogTableOptimizerConfigurationRetentionConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orphanFileDeletionConfiguration")
    def orphan_file_deletion_configuration(self) -> Optional[pulumi.Input[CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationArgs]]:
        
        ...
    
    @orphan_file_deletion_configuration.setter
    def orphan_file_deletion_configuration(self, value: Optional[pulumi.Input[CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionConfiguration")
    def retention_configuration(self) -> Optional[pulumi.Input[CatalogTableOptimizerConfigurationRetentionConfigurationArgs]]:
        
        ...
    
    @retention_configuration.setter
    def retention_configuration(self, value: Optional[pulumi.Input[CatalogTableOptimizerConfigurationRetentionConfigurationArgs]]): # -> None:
        ...
    


class CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationArgsDict(TypedDict):
    iceberg_configuration: NotRequired[pulumi.Input[CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationIcebergConfigurationArgsDict]]


@pulumi.input_type
class CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationArgs:
    def __init__(__self__, *, iceberg_configuration: Optional[pulumi.Input[CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationIcebergConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icebergConfiguration")
    def iceberg_configuration(self) -> Optional[pulumi.Input[CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationIcebergConfigurationArgs]]:
        
        ...
    
    @iceberg_configuration.setter
    def iceberg_configuration(self, value: Optional[pulumi.Input[CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationIcebergConfigurationArgs]]): # -> None:
        ...
    


class CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationIcebergConfigurationArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    orphan_file_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]
    run_rate_in_hours: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationIcebergConfigurationArgs:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ..., orphan_file_retention_period_in_days: Optional[pulumi.Input[_builtins.int]] = ..., run_rate_in_hours: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orphanFileRetentionPeriodInDays")
    def orphan_file_retention_period_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @orphan_file_retention_period_in_days.setter
    def orphan_file_retention_period_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runRateInHours")
    def run_rate_in_hours(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @run_rate_in_hours.setter
    def run_rate_in_hours(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CatalogTableOptimizerConfigurationRetentionConfigurationArgsDict(TypedDict):
    iceberg_configuration: NotRequired[pulumi.Input[CatalogTableOptimizerConfigurationRetentionConfigurationIcebergConfigurationArgsDict]]


@pulumi.input_type
class CatalogTableOptimizerConfigurationRetentionConfigurationArgs:
    def __init__(__self__, *, iceberg_configuration: Optional[pulumi.Input[CatalogTableOptimizerConfigurationRetentionConfigurationIcebergConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="icebergConfiguration")
    def iceberg_configuration(self) -> Optional[pulumi.Input[CatalogTableOptimizerConfigurationRetentionConfigurationIcebergConfigurationArgs]]:
        
        ...
    
    @iceberg_configuration.setter
    def iceberg_configuration(self, value: Optional[pulumi.Input[CatalogTableOptimizerConfigurationRetentionConfigurationIcebergConfigurationArgs]]): # -> None:
        ...
    


class CatalogTableOptimizerConfigurationRetentionConfigurationIcebergConfigurationArgsDict(TypedDict):
    clean_expired_files: NotRequired[pulumi.Input[_builtins.bool]]
    number_of_snapshots_to_retain: NotRequired[pulumi.Input[_builtins.int]]
    run_rate_in_hours: NotRequired[pulumi.Input[_builtins.int]]
    snapshot_retention_period_in_days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CatalogTableOptimizerConfigurationRetentionConfigurationIcebergConfigurationArgs:
    def __init__(__self__, *, clean_expired_files: Optional[pulumi.Input[_builtins.bool]] = ..., number_of_snapshots_to_retain: Optional[pulumi.Input[_builtins.int]] = ..., run_rate_in_hours: Optional[pulumi.Input[_builtins.int]] = ..., snapshot_retention_period_in_days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cleanExpiredFiles")
    def clean_expired_files(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @clean_expired_files.setter
    def clean_expired_files(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfSnapshotsToRetain")
    def number_of_snapshots_to_retain(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @number_of_snapshots_to_retain.setter
    def number_of_snapshots_to_retain(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runRateInHours")
    def run_rate_in_hours(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @run_rate_in_hours.setter
    def run_rate_in_hours(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionPeriodInDays")
    def snapshot_retention_period_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @snapshot_retention_period_in_days.setter
    def snapshot_retention_period_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CatalogTablePartitionIndexArgsDict(TypedDict):
    index_name: pulumi.Input[_builtins.str]
    keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    index_status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogTablePartitionIndexArgs:
    def __init__(__self__, *, index_name: pulumi.Input[_builtins.str], keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], index_status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @index_name.setter
    def index_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @keys.setter
    def keys(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexStatus")
    def index_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @index_status.setter
    def index_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogTablePartitionKeyArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    comment: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogTablePartitionKeyArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], comment: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogTableStorageDescriptorArgsDict(TypedDict):
    additional_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    bucket_columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[CatalogTableStorageDescriptorColumnArgsDict]]]]
    compressed: NotRequired[pulumi.Input[_builtins.bool]]
    input_format: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    number_of_buckets: NotRequired[pulumi.Input[_builtins.int]]
    output_format: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    schema_reference: NotRequired[pulumi.Input[CatalogTableStorageDescriptorSchemaReferenceArgsDict]]
    ser_de_info: NotRequired[pulumi.Input[CatalogTableStorageDescriptorSerDeInfoArgsDict]]
    skewed_info: NotRequired[pulumi.Input[CatalogTableStorageDescriptorSkewedInfoArgsDict]]
    sort_columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[CatalogTableStorageDescriptorSortColumnArgsDict]]]]
    stored_as_sub_directories: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CatalogTableStorageDescriptorArgs:
    def __init__(__self__, *, additional_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., bucket_columns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., columns: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTableStorageDescriptorColumnArgs]]]] = ..., compressed: Optional[pulumi.Input[_builtins.bool]] = ..., input_format: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., number_of_buckets: Optional[pulumi.Input[_builtins.int]] = ..., output_format: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., schema_reference: Optional[pulumi.Input[CatalogTableStorageDescriptorSchemaReferenceArgs]] = ..., ser_de_info: Optional[pulumi.Input[CatalogTableStorageDescriptorSerDeInfoArgs]] = ..., skewed_info: Optional[pulumi.Input[CatalogTableStorageDescriptorSkewedInfoArgs]] = ..., sort_columns: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTableStorageDescriptorSortColumnArgs]]]] = ..., stored_as_sub_directories: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalLocations")
    def additional_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @additional_locations.setter
    def additional_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketColumns")
    def bucket_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @bucket_columns.setter
    def bucket_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTableStorageDescriptorColumnArgs]]]]:
        
        ...
    
    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTableStorageDescriptorColumnArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def compressed(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @compressed.setter
    def compressed(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @input_format.setter
    def input_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfBuckets")
    def number_of_buckets(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @number_of_buckets.setter
    def number_of_buckets(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @output_format.setter
    def output_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaReference")
    def schema_reference(self) -> Optional[pulumi.Input[CatalogTableStorageDescriptorSchemaReferenceArgs]]:
        
        ...
    
    @schema_reference.setter
    def schema_reference(self, value: Optional[pulumi.Input[CatalogTableStorageDescriptorSchemaReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serDeInfo")
    def ser_de_info(self) -> Optional[pulumi.Input[CatalogTableStorageDescriptorSerDeInfoArgs]]:
        
        ...
    
    @ser_de_info.setter
    def ser_de_info(self, value: Optional[pulumi.Input[CatalogTableStorageDescriptorSerDeInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skewedInfo")
    def skewed_info(self) -> Optional[pulumi.Input[CatalogTableStorageDescriptorSkewedInfoArgs]]:
        
        ...
    
    @skewed_info.setter
    def skewed_info(self, value: Optional[pulumi.Input[CatalogTableStorageDescriptorSkewedInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sortColumns")
    def sort_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTableStorageDescriptorSortColumnArgs]]]]:
        
        ...
    
    @sort_columns.setter
    def sort_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTableStorageDescriptorSortColumnArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storedAsSubDirectories")
    def stored_as_sub_directories(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @stored_as_sub_directories.setter
    def stored_as_sub_directories(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CatalogTableStorageDescriptorColumnArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    comment: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogTableStorageDescriptorColumnArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], comment: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogTableStorageDescriptorSchemaReferenceArgsDict(TypedDict):
    schema_version_number: pulumi.Input[_builtins.int]
    schema_id: NotRequired[pulumi.Input[CatalogTableStorageDescriptorSchemaReferenceSchemaIdArgsDict]]
    schema_version_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogTableStorageDescriptorSchemaReferenceArgs:
    def __init__(__self__, *, schema_version_number: pulumi.Input[_builtins.int], schema_id: Optional[pulumi.Input[CatalogTableStorageDescriptorSchemaReferenceSchemaIdArgs]] = ..., schema_version_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaVersionNumber")
    def schema_version_number(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @schema_version_number.setter
    def schema_version_number(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaId")
    def schema_id(self) -> Optional[pulumi.Input[CatalogTableStorageDescriptorSchemaReferenceSchemaIdArgs]]:
        
        ...
    
    @schema_id.setter
    def schema_id(self, value: Optional[pulumi.Input[CatalogTableStorageDescriptorSchemaReferenceSchemaIdArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaVersionId")
    def schema_version_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema_version_id.setter
    def schema_version_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogTableStorageDescriptorSchemaReferenceSchemaIdArgsDict(TypedDict):
    registry_name: NotRequired[pulumi.Input[_builtins.str]]
    schema_arn: NotRequired[pulumi.Input[_builtins.str]]
    schema_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogTableStorageDescriptorSchemaReferenceSchemaIdArgs:
    def __init__(__self__, *, registry_name: Optional[pulumi.Input[_builtins.str]] = ..., schema_arn: Optional[pulumi.Input[_builtins.str]] = ..., schema_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @registry_name.setter
    def registry_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaArn")
    def schema_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema_arn.setter
    def schema_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema_name.setter
    def schema_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogTableStorageDescriptorSerDeInfoArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    serialization_library: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogTableStorageDescriptorSerDeInfoArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., serialization_library: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serializationLibrary")
    def serialization_library(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serialization_library.setter
    def serialization_library(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogTableStorageDescriptorSkewedInfoArgsDict(TypedDict):
    skewed_column_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    skewed_column_value_location_maps: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    skewed_column_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CatalogTableStorageDescriptorSkewedInfoArgs:
    def __init__(__self__, *, skewed_column_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., skewed_column_value_location_maps: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., skewed_column_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skewedColumnNames")
    def skewed_column_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @skewed_column_names.setter
    def skewed_column_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skewedColumnValueLocationMaps")
    def skewed_column_value_location_maps(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @skewed_column_value_location_maps.setter
    def skewed_column_value_location_maps(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skewedColumnValues")
    def skewed_column_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @skewed_column_values.setter
    def skewed_column_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CatalogTableStorageDescriptorSortColumnArgsDict(TypedDict):
    column: pulumi.Input[_builtins.str]
    sort_order: pulumi.Input[_builtins.int]


@pulumi.input_type
class CatalogTableStorageDescriptorSortColumnArgs:
    def __init__(__self__, *, column: pulumi.Input[_builtins.str], sort_order: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def column(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @column.setter
    def column(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @sort_order.setter
    def sort_order(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class CatalogTableTargetTableArgsDict(TypedDict):
    catalog_id: pulumi.Input[_builtins.str]
    database_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    region: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogTableTargetTableArgs:
    def __init__(__self__, *, catalog_id: pulumi.Input[_builtins.str], database_name: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @catalog_id.setter
    def catalog_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogTableViewDefinitionArgsDict(TypedDict):
    definer: NotRequired[pulumi.Input[_builtins.str]]
    is_protected: NotRequired[pulumi.Input[_builtins.bool]]
    last_refresh_type: NotRequired[pulumi.Input[_builtins.str]]
    refresh_seconds: NotRequired[pulumi.Input[_builtins.int]]
    representations: NotRequired[pulumi.Input[Sequence[pulumi.Input[CatalogTableViewDefinitionRepresentationArgsDict]]]]
    sub_object_version_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    sub_objects: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    view_version_id: NotRequired[pulumi.Input[_builtins.int]]
    view_version_token: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogTableViewDefinitionArgs:
    def __init__(__self__, *, definer: Optional[pulumi.Input[_builtins.str]] = ..., is_protected: Optional[pulumi.Input[_builtins.bool]] = ..., last_refresh_type: Optional[pulumi.Input[_builtins.str]] = ..., refresh_seconds: Optional[pulumi.Input[_builtins.int]] = ..., representations: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTableViewDefinitionRepresentationArgs]]]] = ..., sub_object_version_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., sub_objects: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., view_version_id: Optional[pulumi.Input[_builtins.int]] = ..., view_version_token: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @definer.setter
    def definer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isProtected")
    def is_protected(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_protected.setter
    def is_protected(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRefreshType")
    def last_refresh_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_refresh_type.setter
    def last_refresh_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshSeconds")
    def refresh_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @refresh_seconds.setter
    def refresh_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def representations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTableViewDefinitionRepresentationArgs]]]]:
        
        ...
    
    @representations.setter
    def representations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CatalogTableViewDefinitionRepresentationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subObjectVersionIds")
    def sub_object_version_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @sub_object_version_ids.setter
    def sub_object_version_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subObjects")
    def sub_objects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @sub_objects.setter
    def sub_objects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewVersionId")
    def view_version_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @view_version_id.setter
    def view_version_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewVersionToken")
    def view_version_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @view_version_token.setter
    def view_version_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CatalogTableViewDefinitionRepresentationArgsDict(TypedDict):
    dialect: NotRequired[pulumi.Input[_builtins.str]]
    dialect_version: NotRequired[pulumi.Input[_builtins.str]]
    validation_connection: NotRequired[pulumi.Input[_builtins.str]]
    view_expanded_text: NotRequired[pulumi.Input[_builtins.str]]
    view_original_text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CatalogTableViewDefinitionRepresentationArgs:
    def __init__(__self__, *, dialect: Optional[pulumi.Input[_builtins.str]] = ..., dialect_version: Optional[pulumi.Input[_builtins.str]] = ..., validation_connection: Optional[pulumi.Input[_builtins.str]] = ..., view_expanded_text: Optional[pulumi.Input[_builtins.str]] = ..., view_original_text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dialect(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dialect.setter
    def dialect(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialectVersion")
    def dialect_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dialect_version.setter
    def dialect_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationConnection")
    def validation_connection(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @validation_connection.setter
    def validation_connection(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewExpandedText")
    def view_expanded_text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @view_expanded_text.setter
    def view_expanded_text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewOriginalText")
    def view_original_text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @view_original_text.setter
    def view_original_text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClassifierCsvClassifierArgsDict(TypedDict):
    allow_single_column: NotRequired[pulumi.Input[_builtins.bool]]
    contains_header: NotRequired[pulumi.Input[_builtins.str]]
    custom_datatype_configured: NotRequired[pulumi.Input[_builtins.bool]]
    custom_datatypes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    delimiter: NotRequired[pulumi.Input[_builtins.str]]
    disable_value_trimming: NotRequired[pulumi.Input[_builtins.bool]]
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    quote_symbol: NotRequired[pulumi.Input[_builtins.str]]
    serde: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClassifierCsvClassifierArgs:
    def __init__(__self__, *, allow_single_column: Optional[pulumi.Input[_builtins.bool]] = ..., contains_header: Optional[pulumi.Input[_builtins.str]] = ..., custom_datatype_configured: Optional[pulumi.Input[_builtins.bool]] = ..., custom_datatypes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., delimiter: Optional[pulumi.Input[_builtins.str]] = ..., disable_value_trimming: Optional[pulumi.Input[_builtins.bool]] = ..., headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., quote_symbol: Optional[pulumi.Input[_builtins.str]] = ..., serde: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowSingleColumn")
    def allow_single_column(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_single_column.setter
    def allow_single_column(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containsHeader")
    def contains_header(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contains_header.setter
    def contains_header(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDatatypeConfigured")
    def custom_datatype_configured(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @custom_datatype_configured.setter
    def custom_datatype_configured(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDatatypes")
    def custom_datatypes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @custom_datatypes.setter
    def custom_datatypes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delimiter.setter
    def delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableValueTrimming")
    def disable_value_trimming(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_value_trimming.setter
    def disable_value_trimming(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quoteSymbol")
    def quote_symbol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @quote_symbol.setter
    def quote_symbol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def serde(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serde.setter
    def serde(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClassifierGrokClassifierArgsDict(TypedDict):
    classification: pulumi.Input[_builtins.str]
    grok_pattern: pulumi.Input[_builtins.str]
    custom_patterns: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClassifierGrokClassifierArgs:
    def __init__(__self__, *, classification: pulumi.Input[_builtins.str], grok_pattern: pulumi.Input[_builtins.str], custom_patterns: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def classification(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @classification.setter
    def classification(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grokPattern")
    def grok_pattern(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @grok_pattern.setter
    def grok_pattern(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPatterns")
    def custom_patterns(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_patterns.setter
    def custom_patterns(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClassifierJsonClassifierArgsDict(TypedDict):
    json_path: pulumi.Input[_builtins.str]


@pulumi.input_type
class ClassifierJsonClassifierArgs:
    def __init__(__self__, *, json_path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonPath")
    def json_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @json_path.setter
    def json_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ClassifierXmlClassifierArgsDict(TypedDict):
    classification: pulumi.Input[_builtins.str]
    row_tag: pulumi.Input[_builtins.str]


@pulumi.input_type
class ClassifierXmlClassifierArgs:
    def __init__(__self__, *, classification: pulumi.Input[_builtins.str], row_tag: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def classification(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @classification.setter
    def classification(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowTag")
    def row_tag(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @row_tag.setter
    def row_tag(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectionPhysicalConnectionRequirementsArgsDict(TypedDict):
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    security_group_id_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionPhysicalConnectionRequirementsArgs:
    def __init__(__self__, *, availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., security_group_id_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIdLists")
    def security_group_id_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_id_lists.setter
    def security_group_id_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CrawlerCatalogTargetArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    tables: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    connection_name: NotRequired[pulumi.Input[_builtins.str]]
    dlq_event_queue_arn: NotRequired[pulumi.Input[_builtins.str]]
    event_queue_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CrawlerCatalogTargetArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], tables: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], connection_name: Optional[pulumi.Input[_builtins.str]] = ..., dlq_event_queue_arn: Optional[pulumi.Input[_builtins.str]] = ..., event_queue_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tables(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @tables.setter
    def tables(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dlqEventQueueArn")
    def dlq_event_queue_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dlq_event_queue_arn.setter
    def dlq_event_queue_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventQueueArn")
    def event_queue_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_queue_arn.setter
    def event_queue_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CrawlerDeltaTargetArgsDict(TypedDict):
    delta_tables: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    write_manifest: pulumi.Input[_builtins.bool]
    connection_name: NotRequired[pulumi.Input[_builtins.str]]
    create_native_delta_table: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CrawlerDeltaTargetArgs:
    def __init__(__self__, *, delta_tables: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], write_manifest: pulumi.Input[_builtins.bool], connection_name: Optional[pulumi.Input[_builtins.str]] = ..., create_native_delta_table: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deltaTables")
    def delta_tables(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @delta_tables.setter
    def delta_tables(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeManifest")
    def write_manifest(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @write_manifest.setter
    def write_manifest(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createNativeDeltaTable")
    def create_native_delta_table(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_native_delta_table.setter
    def create_native_delta_table(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CrawlerDynamodbTargetArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    scan_all: NotRequired[pulumi.Input[_builtins.bool]]
    scan_rate: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class CrawlerDynamodbTargetArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str], scan_all: Optional[pulumi.Input[_builtins.bool]] = ..., scan_rate: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanAll")
    def scan_all(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @scan_all.setter
    def scan_all(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanRate")
    def scan_rate(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @scan_rate.setter
    def scan_rate(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class CrawlerHudiTargetArgsDict(TypedDict):
    maximum_traversal_depth: pulumi.Input[_builtins.int]
    paths: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    connection_name: NotRequired[pulumi.Input[_builtins.str]]
    exclusions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CrawlerHudiTargetArgs:
    def __init__(__self__, *, maximum_traversal_depth: pulumi.Input[_builtins.int], paths: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], connection_name: Optional[pulumi.Input[_builtins.str]] = ..., exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumTraversalDepth")
    def maximum_traversal_depth(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @maximum_traversal_depth.setter
    def maximum_traversal_depth(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @paths.setter
    def paths(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CrawlerIcebergTargetArgsDict(TypedDict):
    maximum_traversal_depth: pulumi.Input[_builtins.int]
    paths: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    connection_name: NotRequired[pulumi.Input[_builtins.str]]
    exclusions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CrawlerIcebergTargetArgs:
    def __init__(__self__, *, maximum_traversal_depth: pulumi.Input[_builtins.int], paths: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], connection_name: Optional[pulumi.Input[_builtins.str]] = ..., exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumTraversalDepth")
    def maximum_traversal_depth(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @maximum_traversal_depth.setter
    def maximum_traversal_depth(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def paths(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @paths.setter
    def paths(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CrawlerJdbcTargetArgsDict(TypedDict):
    connection_name: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]
    enable_additional_metadatas: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    exclusions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CrawlerJdbcTargetArgs:
    def __init__(__self__, *, connection_name: pulumi.Input[_builtins.str], path: pulumi.Input[_builtins.str], enable_additional_metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAdditionalMetadatas")
    def enable_additional_metadatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @enable_additional_metadatas.setter
    def enable_additional_metadatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CrawlerLakeFormationConfigurationArgsDict(TypedDict):
    account_id: NotRequired[pulumi.Input[_builtins.str]]
    use_lake_formation_credentials: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CrawlerLakeFormationConfigurationArgs:
    def __init__(__self__, *, account_id: Optional[pulumi.Input[_builtins.str]] = ..., use_lake_formation_credentials: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useLakeFormationCredentials")
    def use_lake_formation_credentials(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_lake_formation_credentials.setter
    def use_lake_formation_credentials(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CrawlerLineageConfigurationArgsDict(TypedDict):
    crawler_lineage_settings: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CrawlerLineageConfigurationArgs:
    def __init__(__self__, *, crawler_lineage_settings: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crawlerLineageSettings")
    def crawler_lineage_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @crawler_lineage_settings.setter
    def crawler_lineage_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CrawlerMongodbTargetArgsDict(TypedDict):
    connection_name: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]
    scan_all: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CrawlerMongodbTargetArgs:
    def __init__(__self__, *, connection_name: pulumi.Input[_builtins.str], path: pulumi.Input[_builtins.str], scan_all: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scanAll")
    def scan_all(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @scan_all.setter
    def scan_all(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CrawlerRecrawlPolicyArgsDict(TypedDict):
    recrawl_behavior: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CrawlerRecrawlPolicyArgs:
    def __init__(__self__, *, recrawl_behavior: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recrawlBehavior")
    def recrawl_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @recrawl_behavior.setter
    def recrawl_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CrawlerS3TargetArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    connection_name: NotRequired[pulumi.Input[_builtins.str]]
    dlq_event_queue_arn: NotRequired[pulumi.Input[_builtins.str]]
    event_queue_arn: NotRequired[pulumi.Input[_builtins.str]]
    exclusions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    sample_size: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CrawlerS3TargetArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str], connection_name: Optional[pulumi.Input[_builtins.str]] = ..., dlq_event_queue_arn: Optional[pulumi.Input[_builtins.str]] = ..., event_queue_arn: Optional[pulumi.Input[_builtins.str]] = ..., exclusions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., sample_size: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dlqEventQueueArn")
    def dlq_event_queue_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dlq_event_queue_arn.setter
    def dlq_event_queue_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventQueueArn")
    def event_queue_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_queue_arn.setter
    def event_queue_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exclusions.setter
    def exclusions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleSize")
    def sample_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @sample_size.setter
    def sample_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CrawlerSchemaChangePolicyArgsDict(TypedDict):
    delete_behavior: NotRequired[pulumi.Input[_builtins.str]]
    update_behavior: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CrawlerSchemaChangePolicyArgs:
    def __init__(__self__, *, delete_behavior: Optional[pulumi.Input[_builtins.str]] = ..., update_behavior: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteBehavior")
    def delete_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_behavior.setter
    def delete_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateBehavior")
    def update_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_behavior.setter
    def update_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgsDict(TypedDict):
    connection_password_encryption: pulumi.Input[DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionArgsDict]
    encryption_at_rest: pulumi.Input[DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestArgsDict]


@pulumi.input_type
class DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgs:
    def __init__(__self__, *, connection_password_encryption: pulumi.Input[DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionArgs], encryption_at_rest: pulumi.Input[DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPasswordEncryption")
    def connection_password_encryption(self) -> pulumi.Input[DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionArgs]:
        
        ...
    
    @connection_password_encryption.setter
    def connection_password_encryption(self, value: pulumi.Input[DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAtRest")
    def encryption_at_rest(self) -> pulumi.Input[DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestArgs]:
        
        ...
    
    @encryption_at_rest.setter
    def encryption_at_rest(self, value: pulumi.Input[DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestArgs]): # -> None:
        ...
    


class DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionArgsDict(TypedDict):
    return_connection_password_encrypted: pulumi.Input[_builtins.bool]
    aws_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionArgs:
    def __init__(__self__, *, return_connection_password_encrypted: pulumi.Input[_builtins.bool], aws_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnConnectionPasswordEncrypted")
    def return_connection_password_encrypted(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @return_connection_password_encrypted.setter
    def return_connection_password_encrypted(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsKmsKeyId")
    def aws_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_kms_key_id.setter
    def aws_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestArgsDict(TypedDict):
    catalog_encryption_mode: pulumi.Input[_builtins.str]
    catalog_encryption_service_role: NotRequired[pulumi.Input[_builtins.str]]
    sse_aws_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestArgs:
    def __init__(__self__, *, catalog_encryption_mode: pulumi.Input[_builtins.str], catalog_encryption_service_role: Optional[pulumi.Input[_builtins.str]] = ..., sse_aws_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogEncryptionMode")
    def catalog_encryption_mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @catalog_encryption_mode.setter
    def catalog_encryption_mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogEncryptionServiceRole")
    def catalog_encryption_service_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @catalog_encryption_service_role.setter
    def catalog_encryption_service_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseAwsKmsKeyId")
    def sse_aws_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sse_aws_kms_key_id.setter
    def sse_aws_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DataQualityRulesetTargetTableArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataQualityRulesetTargetTableArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], table_name: pulumi.Input[_builtins.str], catalog_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobCommandArgsDict(TypedDict):
    script_location: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]
    python_version: NotRequired[pulumi.Input[_builtins.str]]
    runtime: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobCommandArgs:
    def __init__(__self__, *, script_location: pulumi.Input[_builtins.str], name: Optional[pulumi.Input[_builtins.str]] = ..., python_version: Optional[pulumi.Input[_builtins.str]] = ..., runtime: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptLocation")
    def script_location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @script_location.setter
    def script_location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonVersion")
    def python_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @python_version.setter
    def python_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobExecutionPropertyArgsDict(TypedDict):
    max_concurrent_runs: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobExecutionPropertyArgs:
    def __init__(__self__, *, max_concurrent_runs: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRuns")
    def max_concurrent_runs(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrent_runs.setter
    def max_concurrent_runs(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobNotificationPropertyArgsDict(TypedDict):
    notify_delay_after: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobNotificationPropertyArgs:
    def __init__(__self__, *, notify_delay_after: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notifyDelayAfter")
    def notify_delay_after(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @notify_delay_after.setter
    def notify_delay_after(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobSourceControlDetailsArgsDict(TypedDict):
    auth_strategy: NotRequired[pulumi.Input[_builtins.str]]
    auth_token: NotRequired[pulumi.Input[_builtins.str]]
    branch: NotRequired[pulumi.Input[_builtins.str]]
    folder: NotRequired[pulumi.Input[_builtins.str]]
    last_commit_id: NotRequired[pulumi.Input[_builtins.str]]
    owner: NotRequired[pulumi.Input[_builtins.str]]
    provider: NotRequired[pulumi.Input[_builtins.str]]
    repository: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobSourceControlDetailsArgs:
    def __init__(__self__, *, auth_strategy: Optional[pulumi.Input[_builtins.str]] = ..., auth_token: Optional[pulumi.Input[_builtins.str]] = ..., branch: Optional[pulumi.Input[_builtins.str]] = ..., folder: Optional[pulumi.Input[_builtins.str]] = ..., last_commit_id: Optional[pulumi.Input[_builtins.str]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., provider: Optional[pulumi.Input[_builtins.str]] = ..., repository: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authStrategy")
    def auth_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_strategy.setter
    def auth_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_token.setter
    def auth_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @folder.setter
    def folder(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastCommitId")
    def last_commit_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_commit_id.setter
    def last_commit_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provider.setter
    def provider(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MLTransformInputRecordTableArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    table_name: pulumi.Input[_builtins.str]
    catalog_id: NotRequired[pulumi.Input[_builtins.str]]
    connection_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MLTransformInputRecordTableArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], table_name: pulumi.Input[_builtins.str], catalog_id: Optional[pulumi.Input[_builtins.str]] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MLTransformParametersArgsDict(TypedDict):
    find_matches_parameters: pulumi.Input[MLTransformParametersFindMatchesParametersArgsDict]
    transform_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class MLTransformParametersArgs:
    def __init__(__self__, *, find_matches_parameters: pulumi.Input[MLTransformParametersFindMatchesParametersArgs], transform_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="findMatchesParameters")
    def find_matches_parameters(self) -> pulumi.Input[MLTransformParametersFindMatchesParametersArgs]:
        
        ...
    
    @find_matches_parameters.setter
    def find_matches_parameters(self, value: pulumi.Input[MLTransformParametersFindMatchesParametersArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transformType")
    def transform_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @transform_type.setter
    def transform_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MLTransformParametersFindMatchesParametersArgsDict(TypedDict):
    accuracy_cost_trade_off: NotRequired[pulumi.Input[_builtins.float]]
    enforce_provided_labels: NotRequired[pulumi.Input[_builtins.bool]]
    precision_recall_trade_off: NotRequired[pulumi.Input[_builtins.float]]
    primary_key_column_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MLTransformParametersFindMatchesParametersArgs:
    def __init__(__self__, *, accuracy_cost_trade_off: Optional[pulumi.Input[_builtins.float]] = ..., enforce_provided_labels: Optional[pulumi.Input[_builtins.bool]] = ..., precision_recall_trade_off: Optional[pulumi.Input[_builtins.float]] = ..., primary_key_column_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accuracyCostTradeOff")
    def accuracy_cost_trade_off(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @accuracy_cost_trade_off.setter
    def accuracy_cost_trade_off(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceProvidedLabels")
    def enforce_provided_labels(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enforce_provided_labels.setter
    def enforce_provided_labels(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="precisionRecallTradeOff")
    def precision_recall_trade_off(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @precision_recall_trade_off.setter
    def precision_recall_trade_off(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryKeyColumnName")
    def primary_key_column_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_key_column_name.setter
    def primary_key_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MLTransformSchemaArgsDict(TypedDict):
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MLTransformSchemaArgs:
    def __init__(__self__, *, data_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PartitionIndexPartitionIndexArgsDict(TypedDict):
    index_name: NotRequired[pulumi.Input[_builtins.str]]
    index_status: NotRequired[pulumi.Input[_builtins.str]]
    keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class PartitionIndexPartitionIndexArgs:
    def __init__(__self__, *, index_name: Optional[pulumi.Input[_builtins.str]] = ..., index_status: Optional[pulumi.Input[_builtins.str]] = ..., keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @index_name.setter
    def index_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexStatus")
    def index_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @index_status.setter
    def index_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @keys.setter
    def keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class PartitionStorageDescriptorArgsDict(TypedDict):
    additional_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    bucket_columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[PartitionStorageDescriptorColumnArgsDict]]]]
    compressed: NotRequired[pulumi.Input[_builtins.bool]]
    input_format: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    number_of_buckets: NotRequired[pulumi.Input[_builtins.int]]
    output_format: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ser_de_info: NotRequired[pulumi.Input[PartitionStorageDescriptorSerDeInfoArgsDict]]
    skewed_info: NotRequired[pulumi.Input[PartitionStorageDescriptorSkewedInfoArgsDict]]
    sort_columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[PartitionStorageDescriptorSortColumnArgsDict]]]]
    stored_as_sub_directories: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class PartitionStorageDescriptorArgs:
    def __init__(__self__, *, additional_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., bucket_columns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., columns: Optional[pulumi.Input[Sequence[pulumi.Input[PartitionStorageDescriptorColumnArgs]]]] = ..., compressed: Optional[pulumi.Input[_builtins.bool]] = ..., input_format: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., number_of_buckets: Optional[pulumi.Input[_builtins.int]] = ..., output_format: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ser_de_info: Optional[pulumi.Input[PartitionStorageDescriptorSerDeInfoArgs]] = ..., skewed_info: Optional[pulumi.Input[PartitionStorageDescriptorSkewedInfoArgs]] = ..., sort_columns: Optional[pulumi.Input[Sequence[pulumi.Input[PartitionStorageDescriptorSortColumnArgs]]]] = ..., stored_as_sub_directories: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalLocations")
    def additional_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @additional_locations.setter
    def additional_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketColumns")
    def bucket_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @bucket_columns.setter
    def bucket_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PartitionStorageDescriptorColumnArgs]]]]:
        
        ...
    
    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PartitionStorageDescriptorColumnArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def compressed(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @compressed.setter
    def compressed(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @input_format.setter
    def input_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfBuckets")
    def number_of_buckets(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @number_of_buckets.setter
    def number_of_buckets(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @output_format.setter
    def output_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serDeInfo")
    def ser_de_info(self) -> Optional[pulumi.Input[PartitionStorageDescriptorSerDeInfoArgs]]:
        
        ...
    
    @ser_de_info.setter
    def ser_de_info(self, value: Optional[pulumi.Input[PartitionStorageDescriptorSerDeInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skewedInfo")
    def skewed_info(self) -> Optional[pulumi.Input[PartitionStorageDescriptorSkewedInfoArgs]]:
        
        ...
    
    @skewed_info.setter
    def skewed_info(self, value: Optional[pulumi.Input[PartitionStorageDescriptorSkewedInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sortColumns")
    def sort_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PartitionStorageDescriptorSortColumnArgs]]]]:
        
        ...
    
    @sort_columns.setter
    def sort_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PartitionStorageDescriptorSortColumnArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storedAsSubDirectories")
    def stored_as_sub_directories(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @stored_as_sub_directories.setter
    def stored_as_sub_directories(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class PartitionStorageDescriptorColumnArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    comment: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PartitionStorageDescriptorColumnArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], comment: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PartitionStorageDescriptorSerDeInfoArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    serialization_library: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PartitionStorageDescriptorSerDeInfoArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., serialization_library: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serializationLibrary")
    def serialization_library(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @serialization_library.setter
    def serialization_library(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PartitionStorageDescriptorSkewedInfoArgsDict(TypedDict):
    skewed_column_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    skewed_column_value_location_maps: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    skewed_column_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class PartitionStorageDescriptorSkewedInfoArgs:
    def __init__(__self__, *, skewed_column_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., skewed_column_value_location_maps: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., skewed_column_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skewedColumnNames")
    def skewed_column_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @skewed_column_names.setter
    def skewed_column_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skewedColumnValueLocationMaps")
    def skewed_column_value_location_maps(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @skewed_column_value_location_maps.setter
    def skewed_column_value_location_maps(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skewedColumnValues")
    def skewed_column_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @skewed_column_values.setter
    def skewed_column_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class PartitionStorageDescriptorSortColumnArgsDict(TypedDict):
    column: pulumi.Input[_builtins.str]
    sort_order: pulumi.Input[_builtins.int]


@pulumi.input_type
class PartitionStorageDescriptorSortColumnArgs:
    def __init__(__self__, *, column: pulumi.Input[_builtins.str], sort_order: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def column(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @column.setter
    def column(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @sort_order.setter
    def sort_order(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class SecurityConfigurationEncryptionConfigurationArgsDict(TypedDict):
    cloudwatch_encryption: pulumi.Input[SecurityConfigurationEncryptionConfigurationCloudwatchEncryptionArgsDict]
    job_bookmarks_encryption: pulumi.Input[SecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionArgsDict]
    s3_encryption: pulumi.Input[SecurityConfigurationEncryptionConfigurationS3EncryptionArgsDict]


@pulumi.input_type
class SecurityConfigurationEncryptionConfigurationArgs:
    def __init__(__self__, *, cloudwatch_encryption: pulumi.Input[SecurityConfigurationEncryptionConfigurationCloudwatchEncryptionArgs], job_bookmarks_encryption: pulumi.Input[SecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionArgs], s3_encryption: pulumi.Input[SecurityConfigurationEncryptionConfigurationS3EncryptionArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchEncryption")
    def cloudwatch_encryption(self) -> pulumi.Input[SecurityConfigurationEncryptionConfigurationCloudwatchEncryptionArgs]:
        ...
    
    @cloudwatch_encryption.setter
    def cloudwatch_encryption(self, value: pulumi.Input[SecurityConfigurationEncryptionConfigurationCloudwatchEncryptionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobBookmarksEncryption")
    def job_bookmarks_encryption(self) -> pulumi.Input[SecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionArgs]:
        ...
    
    @job_bookmarks_encryption.setter
    def job_bookmarks_encryption(self, value: pulumi.Input[SecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Encryption")
    def s3_encryption(self) -> pulumi.Input[SecurityConfigurationEncryptionConfigurationS3EncryptionArgs]:
        
        ...
    
    @s3_encryption.setter
    def s3_encryption(self, value: pulumi.Input[SecurityConfigurationEncryptionConfigurationS3EncryptionArgs]): # -> None:
        ...
    


class SecurityConfigurationEncryptionConfigurationCloudwatchEncryptionArgsDict(TypedDict):
    cloudwatch_encryption_mode: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecurityConfigurationEncryptionConfigurationCloudwatchEncryptionArgs:
    def __init__(__self__, *, cloudwatch_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchEncryptionMode")
    def cloudwatch_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloudwatch_encryption_mode.setter
    def cloudwatch_encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionArgsDict(TypedDict):
    job_bookmarks_encryption_mode: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecurityConfigurationEncryptionConfigurationJobBookmarksEncryptionArgs:
    def __init__(__self__, *, job_bookmarks_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobBookmarksEncryptionMode")
    def job_bookmarks_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @job_bookmarks_encryption_mode.setter
    def job_bookmarks_encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecurityConfigurationEncryptionConfigurationS3EncryptionArgsDict(TypedDict):
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    s3_encryption_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecurityConfigurationEncryptionConfigurationS3EncryptionArgs:
    def __init__(__self__, *, kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., s3_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3EncryptionMode")
    def s3_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_encryption_mode.setter
    def s3_encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TriggerActionArgsDict(TypedDict):
    arguments: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    crawler_name: NotRequired[pulumi.Input[_builtins.str]]
    job_name: NotRequired[pulumi.Input[_builtins.str]]
    notification_property: NotRequired[pulumi.Input[TriggerActionNotificationPropertyArgsDict]]
    security_configuration: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TriggerActionArgs:
    def __init__(__self__, *, arguments: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., crawler_name: Optional[pulumi.Input[_builtins.str]] = ..., job_name: Optional[pulumi.Input[_builtins.str]] = ..., notification_property: Optional[pulumi.Input[TriggerActionNotificationPropertyArgs]] = ..., security_configuration: Optional[pulumi.Input[_builtins.str]] = ..., timeout: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @arguments.setter
    def arguments(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crawlerName")
    def crawler_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @crawler_name.setter
    def crawler_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @job_name.setter
    def job_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationProperty")
    def notification_property(self) -> Optional[pulumi.Input[TriggerActionNotificationPropertyArgs]]:
        
        ...
    
    @notification_property.setter
    def notification_property(self, value: Optional[pulumi.Input[TriggerActionNotificationPropertyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_configuration.setter
    def security_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TriggerActionNotificationPropertyArgsDict(TypedDict):
    notify_delay_after: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TriggerActionNotificationPropertyArgs:
    def __init__(__self__, *, notify_delay_after: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notifyDelayAfter")
    def notify_delay_after(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @notify_delay_after.setter
    def notify_delay_after(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TriggerEventBatchingConditionArgsDict(TypedDict):
    batch_size: pulumi.Input[_builtins.int]
    batch_window: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TriggerEventBatchingConditionArgs:
    def __init__(__self__, *, batch_size: pulumi.Input[_builtins.int], batch_window: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @batch_size.setter
    def batch_size(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchWindow")
    def batch_window(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @batch_window.setter
    def batch_window(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TriggerPredicateArgsDict(TypedDict):
    conditions: pulumi.Input[Sequence[pulumi.Input[TriggerPredicateConditionArgsDict]]]
    logical: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TriggerPredicateArgs:
    def __init__(__self__, *, conditions: pulumi.Input[Sequence[pulumi.Input[TriggerPredicateConditionArgs]]], logical: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Input[Sequence[pulumi.Input[TriggerPredicateConditionArgs]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: pulumi.Input[Sequence[pulumi.Input[TriggerPredicateConditionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def logical(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logical.setter
    def logical(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TriggerPredicateConditionArgsDict(TypedDict):
    crawl_state: NotRequired[pulumi.Input[_builtins.str]]
    crawler_name: NotRequired[pulumi.Input[_builtins.str]]
    job_name: NotRequired[pulumi.Input[_builtins.str]]
    logical_operator: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TriggerPredicateConditionArgs:
    def __init__(__self__, *, crawl_state: Optional[pulumi.Input[_builtins.str]] = ..., crawler_name: Optional[pulumi.Input[_builtins.str]] = ..., job_name: Optional[pulumi.Input[_builtins.str]] = ..., logical_operator: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crawlState")
    def crawl_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @crawl_state.setter
    def crawl_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crawlerName")
    def crawler_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @crawler_name.setter
    def crawler_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @job_name.setter
    def job_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicalOperator")
    def logical_operator(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logical_operator.setter
    def logical_operator(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UserDefinedFunctionResourceUriArgsDict(TypedDict):
    resource_type: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]


@pulumi.input_type
class UserDefinedFunctionResourceUriArgs:
    def __init__(__self__, *, resource_type: pulumi.Input[_builtins.str], uri: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class GetScriptDagEdgeArgsDict(TypedDict):
    source: _builtins.str
    target: _builtins.str
    target_parameter: NotRequired[_builtins.str]


@pulumi.input_type
class GetScriptDagEdgeArgs:
    def __init__(__self__, *, source: _builtins.str, target: _builtins.str, target_parameter: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    
    @source.setter
    def source(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        
        ...
    
    @target.setter
    def target(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetParameter")
    def target_parameter(self) -> Optional[_builtins.str]:
        
        ...
    
    @target_parameter.setter
    def target_parameter(self, value: Optional[_builtins.str]): # -> None:
        ...
    


class GetScriptDagNodeArgsDict(TypedDict):
    args: Sequence[GetScriptDagNodeArgArgsDict]
    id: _builtins.str
    node_type: _builtins.str
    line_number: NotRequired[_builtins.int]


@pulumi.input_type
class GetScriptDagNodeArgs:
    def __init__(__self__, *, args: Sequence[GetScriptDagNodeArgArgs], id: _builtins.str, node_type: _builtins.str, line_number: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Sequence[GetScriptDagNodeArgArgs]:
        
        ...
    
    @args.setter
    def args(self, value: Sequence[GetScriptDagNodeArgArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @id.setter
    def id(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> _builtins.str:
        
        ...
    
    @node_type.setter
    def node_type(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lineNumber")
    def line_number(self) -> Optional[_builtins.int]:
        
        ...
    
    @line_number.setter
    def line_number(self, value: Optional[_builtins.int]): # -> None:
        ...
    


class GetScriptDagNodeArgArgsDict(TypedDict):
    name: _builtins.str
    value: _builtins.str
    param: NotRequired[_builtins.bool]


@pulumi.input_type
class GetScriptDagNodeArgArgs:
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str, param: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @value.setter
    def value(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def param(self) -> Optional[_builtins.bool]:
        
        ...
    
    @param.setter
    def param(self, value: Optional[_builtins.bool]): # -> None:
        ...
    


