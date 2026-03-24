import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CatalogDatabaseCreateTableDefaultPermission",
    ...,
    "CatalogDatabaseFederatedDatabase",
    "CatalogDatabaseTargetDatabase",
    "CatalogTableOpenTableFormatInput",
    "CatalogTableOpenTableFormatInputIcebergInput",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "CatalogTableOptimizerConfiguration",
    ...,
    ...,
    ...,
    ...,
    "CatalogTablePartitionIndex",
    "CatalogTablePartitionKey",
    "CatalogTableStorageDescriptor",
    "CatalogTableStorageDescriptorColumn",
    "CatalogTableStorageDescriptorSchemaReference",
    ...,
    "CatalogTableStorageDescriptorSerDeInfo",
    "CatalogTableStorageDescriptorSkewedInfo",
    "CatalogTableStorageDescriptorSortColumn",
    "CatalogTableTargetTable",
    "CatalogTableViewDefinition",
    "CatalogTableViewDefinitionRepresentation",
    "ClassifierCsvClassifier",
    "ClassifierGrokClassifier",
    "ClassifierJsonClassifier",
    "ClassifierXmlClassifier",
    "ConnectionPhysicalConnectionRequirements",
    "CrawlerCatalogTarget",
    "CrawlerDeltaTarget",
    "CrawlerDynamodbTarget",
    "CrawlerHudiTarget",
    "CrawlerIcebergTarget",
    "CrawlerJdbcTarget",
    "CrawlerLakeFormationConfiguration",
    "CrawlerLineageConfiguration",
    "CrawlerMongodbTarget",
    "CrawlerRecrawlPolicy",
    "CrawlerS3Target",
    "CrawlerSchemaChangePolicy",
    ...,
    ...,
    ...,
    "DataQualityRulesetTargetTable",
    "JobCommand",
    "JobExecutionProperty",
    "JobNotificationProperty",
    "JobSourceControlDetails",
    "MLTransformInputRecordTable",
    "MLTransformParameters",
    "MLTransformParametersFindMatchesParameters",
    "MLTransformSchema",
    "PartitionIndexPartitionIndex",
    "PartitionStorageDescriptor",
    "PartitionStorageDescriptorColumn",
    "PartitionStorageDescriptorSerDeInfo",
    "PartitionStorageDescriptorSkewedInfo",
    "PartitionStorageDescriptorSortColumn",
    "SecurityConfigurationEncryptionConfiguration",
    ...,
    ...,
    ...,
    "TriggerAction",
    "TriggerActionNotificationProperty",
    "TriggerEventBatchingCondition",
    "TriggerPredicate",
    "TriggerPredicateCondition",
    "UserDefinedFunctionResourceUri",
    "GetCatalogTablePartitionIndexResult",
    "GetCatalogTablePartitionKeyResult",
    "GetCatalogTableStorageDescriptorResult",
    "GetCatalogTableStorageDescriptorColumnResult",
    ...,
    ...,
    "GetCatalogTableStorageDescriptorSerDeInfoResult",
    "GetCatalogTableStorageDescriptorSkewedInfoResult",
    "GetCatalogTableStorageDescriptorSortColumnResult",
    "GetCatalogTableTargetTableResult",
    "GetConnectionPhysicalConnectionRequirementResult",
    ...,
    ...,
    ...,
    "GetScriptDagEdgeResult",
    "GetScriptDagNodeResult",
    "GetScriptDagNodeArgResult",
]

@pulumi.output_type
class CatalogDatabaseCreateTableDefaultPermission(dict):
    def __init__(
        __self__,
        *,
        permissions: Optional[Sequence[_builtins.str]] = ...,
        principal: Optional[
            outputs.CatalogDatabaseCreateTableDefaultPermissionPrincipal
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def principal(
        self,
    ) -> Optional[outputs.CatalogDatabaseCreateTableDefaultPermissionPrincipal]: ...

@pulumi.output_type
class CatalogDatabaseCreateTableDefaultPermissionPrincipal(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, data_lake_principal_identifier: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataLakePrincipalIdentifier")
    def data_lake_principal_identifier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogDatabaseFederatedDatabase(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_name: Optional[_builtins.str] = ...,
        identifier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogDatabaseTargetDatabase(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        catalog_id: _builtins.str,
        database_name: _builtins.str,
        region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogTableOpenTableFormatInput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, iceberg_input: outputs.CatalogTableOpenTableFormatInputIcebergInput
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="icebergInput")
    def iceberg_input(self) -> outputs.CatalogTableOpenTableFormatInputIcebergInput: ...

@pulumi.output_type
class CatalogTableOpenTableFormatInputIcebergInput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metadata_operation: _builtins.str,
        iceberg_table_input: Optional[
            outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInput
        ] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataOperation")
    def metadata_operation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="icebergTableInput")
    def iceberg_table_input(
        self,
    ) -> Optional[
        outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInput
    ]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location: _builtins.str,
        schema: outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchema,
        partition_spec: Optional[
            outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpec
        ] = ...,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
        sort_order: Optional[
            outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrder
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schema(
        self,
    ) -> (
        outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchema
    ): ...
    @_builtins.property
    @pulumi.getter(name="partitionSpec")
    def partition_spec(
        self,
    ) -> Optional[
        outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpec
    ]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(
        self,
    ) -> Optional[
        outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrder
    ]: ...

@pulumi.output_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fields: Sequence[
            outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecField
        ],
        spec_id: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Sequence[
        outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecField
    ]: ...
    @_builtins.property
    @pulumi.getter(name="specId")
    def spec_id(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputPartitionSpecField(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        source_id: _builtins.int,
        transform: _builtins.str,
        field_id: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def transform(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fieldId")
    def field_id(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fields: Sequence[
            outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaField
        ],
        identifier_field_ids: Optional[Sequence[_builtins.int]] = ...,
        schema_id: Optional[_builtins.int] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Sequence[
        outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaField
    ]: ...
    @_builtins.property
    @pulumi.getter(name="identifierFieldIds")
    def identifier_field_ids(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="schemaId")
    def schema_id(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSchemaField(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.int,
        name: _builtins.str,
        required: _builtins.bool,
        type: _builtins.str,
        doc: Optional[_builtins.str] = ...,
        initial_default: Optional[_builtins.str] = ...,
        write_default: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def doc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="initialDefault")
    def initial_default(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="writeDefault")
    def write_default(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrder(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fields: Sequence[
            outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderField
        ],
        order_id: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> Sequence[
        outputs.CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderField
    ]: ...
    @_builtins.property
    @pulumi.getter(name="orderId")
    def order_id(self) -> _builtins.int: ...

@pulumi.output_type
class CatalogTableOpenTableFormatInputIcebergInputIcebergTableInputSortOrderField(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        direction: _builtins.str,
        null_order: _builtins.str,
        source_id: _builtins.int,
        transform: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nullOrder")
    def null_order(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def transform(self) -> _builtins.str: ...

@pulumi.output_type
class CatalogTableOptimizerConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        role_arn: _builtins.str,
        orphan_file_deletion_configuration: Optional[
            outputs.CatalogTableOptimizerConfigurationOrphanFileDeletionConfiguration
        ] = ...,
        retention_configuration: Optional[
            outputs.CatalogTableOptimizerConfigurationRetentionConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="orphanFileDeletionConfiguration")
    def orphan_file_deletion_configuration(
        self,
    ) -> Optional[
        outputs.CatalogTableOptimizerConfigurationOrphanFileDeletionConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="retentionConfiguration")
    def retention_configuration(
        self,
    ) -> Optional[outputs.CatalogTableOptimizerConfigurationRetentionConfiguration]: ...

@pulumi.output_type
class CatalogTableOptimizerConfigurationOrphanFileDeletionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        iceberg_configuration: Optional[
            outputs.CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationIcebergConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="icebergConfiguration")
    def iceberg_configuration(
        self,
    ) -> Optional[
        outputs.CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationIcebergConfiguration
    ]: ...

@pulumi.output_type
class CatalogTableOptimizerConfigurationOrphanFileDeletionConfigurationIcebergConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location: Optional[_builtins.str] = ...,
        orphan_file_retention_period_in_days: Optional[_builtins.int] = ...,
        run_rate_in_hours: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orphanFileRetentionPeriodInDays")
    def orphan_file_retention_period_in_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="runRateInHours")
    def run_rate_in_hours(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CatalogTableOptimizerConfigurationRetentionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        iceberg_configuration: Optional[
            outputs.CatalogTableOptimizerConfigurationRetentionConfigurationIcebergConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="icebergConfiguration")
    def iceberg_configuration(
        self,
    ) -> Optional[
        outputs.CatalogTableOptimizerConfigurationRetentionConfigurationIcebergConfiguration
    ]: ...

@pulumi.output_type
class CatalogTableOptimizerConfigurationRetentionConfigurationIcebergConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        clean_expired_files: Optional[_builtins.bool] = ...,
        number_of_snapshots_to_retain: Optional[_builtins.int] = ...,
        run_rate_in_hours: Optional[_builtins.int] = ...,
        snapshot_retention_period_in_days: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cleanExpiredFiles")
    def clean_expired_files(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfSnapshotsToRetain")
    def number_of_snapshots_to_retain(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="runRateInHours")
    def run_rate_in_hours(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionPeriodInDays")
    def snapshot_retention_period_in_days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CatalogTablePartitionIndex(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        index_name: _builtins.str,
        keys: Sequence[_builtins.str],
        index_status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="indexStatus")
    def index_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogTablePartitionKey(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        comment: Optional[_builtins.str] = ...,
        parameters: Optional[Mapping[str, _builtins.str]] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogTableStorageDescriptor(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_locations: Optional[Sequence[_builtins.str]] = ...,
        bucket_columns: Optional[Sequence[_builtins.str]] = ...,
        columns: Optional[Sequence[outputs.CatalogTableStorageDescriptorColumn]] = ...,
        compressed: Optional[_builtins.bool] = ...,
        input_format: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        number_of_buckets: Optional[_builtins.int] = ...,
        output_format: Optional[_builtins.str] = ...,
        parameters: Optional[Mapping[str, _builtins.str]] = ...,
        schema_reference: Optional[
            outputs.CatalogTableStorageDescriptorSchemaReference
        ] = ...,
        ser_de_info: Optional[outputs.CatalogTableStorageDescriptorSerDeInfo] = ...,
        skewed_info: Optional[outputs.CatalogTableStorageDescriptorSkewedInfo] = ...,
        sort_columns: Optional[
            Sequence[outputs.CatalogTableStorageDescriptorSortColumn]
        ] = ...,
        stored_as_sub_directories: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalLocations")
    def additional_locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="bucketColumns")
    def bucket_columns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[Sequence[outputs.CatalogTableStorageDescriptorColumn]]: ...
    @_builtins.property
    @pulumi.getter
    def compressed(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfBuckets")
    def number_of_buckets(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="schemaReference")
    def schema_reference(
        self,
    ) -> Optional[outputs.CatalogTableStorageDescriptorSchemaReference]: ...
    @_builtins.property
    @pulumi.getter(name="serDeInfo")
    def ser_de_info(
        self,
    ) -> Optional[outputs.CatalogTableStorageDescriptorSerDeInfo]: ...
    @_builtins.property
    @pulumi.getter(name="skewedInfo")
    def skewed_info(
        self,
    ) -> Optional[outputs.CatalogTableStorageDescriptorSkewedInfo]: ...
    @_builtins.property
    @pulumi.getter(name="sortColumns")
    def sort_columns(
        self,
    ) -> Optional[Sequence[outputs.CatalogTableStorageDescriptorSortColumn]]: ...
    @_builtins.property
    @pulumi.getter(name="storedAsSubDirectories")
    def stored_as_sub_directories(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CatalogTableStorageDescriptorColumn(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        comment: Optional[_builtins.str] = ...,
        parameters: Optional[Mapping[str, _builtins.str]] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogTableStorageDescriptorSchemaReference(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schema_version_number: _builtins.int,
        schema_id: Optional[
            outputs.CatalogTableStorageDescriptorSchemaReferenceSchemaId
        ] = ...,
        schema_version_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schemaVersionNumber")
    def schema_version_number(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="schemaId")
    def schema_id(
        self,
    ) -> Optional[outputs.CatalogTableStorageDescriptorSchemaReferenceSchemaId]: ...
    @_builtins.property
    @pulumi.getter(name="schemaVersionId")
    def schema_version_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogTableStorageDescriptorSchemaReferenceSchemaId(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        registry_name: Optional[_builtins.str] = ...,
        schema_arn: Optional[_builtins.str] = ...,
        schema_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaArn")
    def schema_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogTableStorageDescriptorSerDeInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        parameters: Optional[Mapping[str, _builtins.str]] = ...,
        serialization_library: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serializationLibrary")
    def serialization_library(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogTableStorageDescriptorSkewedInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        skewed_column_names: Optional[Sequence[_builtins.str]] = ...,
        skewed_column_value_location_maps: Optional[Mapping[str, _builtins.str]] = ...,
        skewed_column_values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="skewedColumnNames")
    def skewed_column_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="skewedColumnValueLocationMaps")
    def skewed_column_value_location_maps(
        self,
    ) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="skewedColumnValues")
    def skewed_column_values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CatalogTableStorageDescriptorSortColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, column: _builtins.str, sort_order: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> _builtins.int: ...

@pulumi.output_type
class CatalogTableTargetTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        catalog_id: _builtins.str,
        database_name: _builtins.str,
        name: _builtins.str,
        region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogTableViewDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        definer: Optional[_builtins.str] = ...,
        is_protected: Optional[_builtins.bool] = ...,
        last_refresh_type: Optional[_builtins.str] = ...,
        refresh_seconds: Optional[_builtins.int] = ...,
        representations: Optional[
            Sequence[outputs.CatalogTableViewDefinitionRepresentation]
        ] = ...,
        sub_object_version_ids: Optional[Sequence[_builtins.int]] = ...,
        sub_objects: Optional[Sequence[_builtins.str]] = ...,
        view_version_id: Optional[_builtins.int] = ...,
        view_version_token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isProtected")
    def is_protected(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastRefreshType")
    def last_refresh_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshSeconds")
    def refresh_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def representations(
        self,
    ) -> Optional[Sequence[outputs.CatalogTableViewDefinitionRepresentation]]: ...
    @_builtins.property
    @pulumi.getter(name="subObjectVersionIds")
    def sub_object_version_ids(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="subObjects")
    def sub_objects(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="viewVersionId")
    def view_version_id(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="viewVersionToken")
    def view_version_token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CatalogTableViewDefinitionRepresentation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dialect: Optional[_builtins.str] = ...,
        dialect_version: Optional[_builtins.str] = ...,
        validation_connection: Optional[_builtins.str] = ...,
        view_expanded_text: Optional[_builtins.str] = ...,
        view_original_text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dialect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dialectVersion")
    def dialect_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validationConnection")
    def validation_connection(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="viewExpandedText")
    def view_expanded_text(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="viewOriginalText")
    def view_original_text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClassifierCsvClassifier(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_single_column: Optional[_builtins.bool] = ...,
        contains_header: Optional[_builtins.str] = ...,
        custom_datatype_configured: Optional[_builtins.bool] = ...,
        custom_datatypes: Optional[Sequence[_builtins.str]] = ...,
        delimiter: Optional[_builtins.str] = ...,
        disable_value_trimming: Optional[_builtins.bool] = ...,
        headers: Optional[Sequence[_builtins.str]] = ...,
        quote_symbol: Optional[_builtins.str] = ...,
        serde: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowSingleColumn")
    def allow_single_column(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="containsHeader")
    def contains_header(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customDatatypeConfigured")
    def custom_datatype_configured(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="customDatatypes")
    def custom_datatypes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableValueTrimming")
    def disable_value_trimming(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="quoteSymbol")
    def quote_symbol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def serde(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClassifierGrokClassifier(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        classification: _builtins.str,
        grok_pattern: _builtins.str,
        custom_patterns: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classification(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="grokPattern")
    def grok_pattern(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customPatterns")
    def custom_patterns(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClassifierJsonClassifier(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, json_path: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jsonPath")
    def json_path(self) -> _builtins.str: ...

@pulumi.output_type
class ClassifierXmlClassifier(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, classification: _builtins.str, row_tag: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classification(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rowTag")
    def row_tag(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionPhysicalConnectionRequirements(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_zone: Optional[_builtins.str] = ...,
        security_group_id_lists: Optional[Sequence[_builtins.str]] = ...,
        subnet_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIdLists")
    def security_group_id_lists(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CrawlerCatalogTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_name: _builtins.str,
        tables: Sequence[_builtins.str],
        connection_name: Optional[_builtins.str] = ...,
        dlq_event_queue_arn: Optional[_builtins.str] = ...,
        event_queue_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tables(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dlqEventQueueArn")
    def dlq_event_queue_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventQueueArn")
    def event_queue_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CrawlerDeltaTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delta_tables: Sequence[_builtins.str],
        write_manifest: _builtins.bool,
        connection_name: Optional[_builtins.str] = ...,
        create_native_delta_table: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deltaTables")
    def delta_tables(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="writeManifest")
    def write_manifest(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createNativeDeltaTable")
    def create_native_delta_table(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CrawlerDynamodbTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        path: _builtins.str,
        scan_all: Optional[_builtins.bool] = ...,
        scan_rate: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanAll")
    def scan_all(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="scanRate")
    def scan_rate(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class CrawlerHudiTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maximum_traversal_depth: _builtins.int,
        paths: Sequence[_builtins.str],
        connection_name: Optional[_builtins.str] = ...,
        exclusions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumTraversalDepth")
    def maximum_traversal_depth(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CrawlerIcebergTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maximum_traversal_depth: _builtins.int,
        paths: Sequence[_builtins.str],
        connection_name: Optional[_builtins.str] = ...,
        exclusions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumTraversalDepth")
    def maximum_traversal_depth(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CrawlerJdbcTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_name: _builtins.str,
        path: _builtins.str,
        enable_additional_metadatas: Optional[Sequence[_builtins.str]] = ...,
        exclusions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableAdditionalMetadatas")
    def enable_additional_metadatas(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CrawlerLakeFormationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_id: Optional[_builtins.str] = ...,
        use_lake_formation_credentials: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useLakeFormationCredentials")
    def use_lake_formation_credentials(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CrawlerLineageConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, crawler_lineage_settings: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlerLineageSettings")
    def crawler_lineage_settings(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CrawlerMongodbTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_name: _builtins.str,
        path: _builtins.str,
        scan_all: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scanAll")
    def scan_all(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CrawlerRecrawlPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, recrawl_behavior: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recrawlBehavior")
    def recrawl_behavior(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CrawlerS3Target(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        path: _builtins.str,
        connection_name: Optional[_builtins.str] = ...,
        dlq_event_queue_arn: Optional[_builtins.str] = ...,
        event_queue_arn: Optional[_builtins.str] = ...,
        exclusions: Optional[Sequence[_builtins.str]] = ...,
        sample_size: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dlqEventQueueArn")
    def dlq_event_queue_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventQueueArn")
    def event_queue_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def exclusions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sampleSize")
    def sample_size(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CrawlerSchemaChangePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delete_behavior: Optional[_builtins.str] = ...,
        update_behavior: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deleteBehavior")
    def delete_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateBehavior")
    def update_behavior(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataCatalogEncryptionSettingsDataCatalogEncryptionSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_password_encryption: outputs.DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption,
        encryption_at_rest: outputs.DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionPasswordEncryption")
    def connection_password_encryption(
        self,
    ) -> outputs.DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAtRest")
    def encryption_at_rest(
        self,
    ) -> outputs.DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest: ...

@pulumi.output_type
class DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryption(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        return_connection_password_encrypted: _builtins.bool,
        aws_kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="returnConnectionPasswordEncrypted")
    def return_connection_password_encrypted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="awsKmsKeyId")
    def aws_kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRest(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        catalog_encryption_mode: _builtins.str,
        catalog_encryption_service_role: Optional[_builtins.str] = ...,
        sse_aws_kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogEncryptionMode")
    def catalog_encryption_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="catalogEncryptionServiceRole")
    def catalog_encryption_service_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sseAwsKmsKeyId")
    def sse_aws_kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataQualityRulesetTargetTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_name: _builtins.str,
        table_name: _builtins.str,
        catalog_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobCommand(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        script_location: _builtins.str,
        name: Optional[_builtins.str] = ...,
        python_version: Optional[_builtins.str] = ...,
        runtime: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scriptLocation")
    def script_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pythonVersion")
    def python_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobExecutionProperty(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, max_concurrent_runs: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentRuns")
    def max_concurrent_runs(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class JobNotificationProperty(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, notify_delay_after: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notifyDelayAfter")
    def notify_delay_after(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class JobSourceControlDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_strategy: Optional[_builtins.str] = ...,
        auth_token: Optional[_builtins.str] = ...,
        branch: Optional[_builtins.str] = ...,
        folder: Optional[_builtins.str] = ...,
        last_commit_id: Optional[_builtins.str] = ...,
        owner: Optional[_builtins.str] = ...,
        provider: Optional[_builtins.str] = ...,
        repository: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authStrategy")
    def auth_strategy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastCommitId")
    def last_commit_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MLTransformInputRecordTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_name: _builtins.str,
        table_name: _builtins.str,
        catalog_id: Optional[_builtins.str] = ...,
        connection_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MLTransformParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        find_matches_parameters: outputs.MLTransformParametersFindMatchesParameters,
        transform_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="findMatchesParameters")
    def find_matches_parameters(
        self,
    ) -> outputs.MLTransformParametersFindMatchesParameters: ...
    @_builtins.property
    @pulumi.getter(name="transformType")
    def transform_type(self) -> _builtins.str: ...

@pulumi.output_type
class MLTransformParametersFindMatchesParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        accuracy_cost_trade_off: Optional[_builtins.float] = ...,
        enforce_provided_labels: Optional[_builtins.bool] = ...,
        precision_recall_trade_off: Optional[_builtins.float] = ...,
        primary_key_column_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accuracyCostTradeOff")
    def accuracy_cost_trade_off(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="enforceProvidedLabels")
    def enforce_provided_labels(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="precisionRecallTradeOff")
    def precision_recall_trade_off(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKeyColumnName")
    def primary_key_column_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MLTransformSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_type: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PartitionIndexPartitionIndex(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        index_name: Optional[_builtins.str] = ...,
        index_status: Optional[_builtins.str] = ...,
        keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="indexStatus")
    def index_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PartitionStorageDescriptor(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_locations: Optional[Sequence[_builtins.str]] = ...,
        bucket_columns: Optional[Sequence[_builtins.str]] = ...,
        columns: Optional[Sequence[outputs.PartitionStorageDescriptorColumn]] = ...,
        compressed: Optional[_builtins.bool] = ...,
        input_format: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        number_of_buckets: Optional[_builtins.int] = ...,
        output_format: Optional[_builtins.str] = ...,
        parameters: Optional[Mapping[str, _builtins.str]] = ...,
        ser_de_info: Optional[outputs.PartitionStorageDescriptorSerDeInfo] = ...,
        skewed_info: Optional[outputs.PartitionStorageDescriptorSkewedInfo] = ...,
        sort_columns: Optional[
            Sequence[outputs.PartitionStorageDescriptorSortColumn]
        ] = ...,
        stored_as_sub_directories: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalLocations")
    def additional_locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="bucketColumns")
    def bucket_columns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[Sequence[outputs.PartitionStorageDescriptorColumn]]: ...
    @_builtins.property
    @pulumi.getter
    def compressed(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfBuckets")
    def number_of_buckets(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serDeInfo")
    def ser_de_info(self) -> Optional[outputs.PartitionStorageDescriptorSerDeInfo]: ...
    @_builtins.property
    @pulumi.getter(name="skewedInfo")
    def skewed_info(self) -> Optional[outputs.PartitionStorageDescriptorSkewedInfo]: ...
    @_builtins.property
    @pulumi.getter(name="sortColumns")
    def sort_columns(
        self,
    ) -> Optional[Sequence[outputs.PartitionStorageDescriptorSortColumn]]: ...
    @_builtins.property
    @pulumi.getter(name="storedAsSubDirectories")
    def stored_as_sub_directories(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PartitionStorageDescriptorColumn(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        comment: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PartitionStorageDescriptorSerDeInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        parameters: Optional[Mapping[str, _builtins.str]] = ...,
        serialization_library: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serializationLibrary")
    def serialization_library(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PartitionStorageDescriptorSkewedInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        skewed_column_names: Optional[Sequence[_builtins.str]] = ...,
        skewed_column_value_location_maps: Optional[Mapping[str, _builtins.str]] = ...,
        skewed_column_values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="skewedColumnNames")
    def skewed_column_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="skewedColumnValueLocationMaps")
    def skewed_column_value_location_maps(
        self,
    ) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="skewedColumnValues")
    def skewed_column_values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PartitionStorageDescriptorSortColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, column: _builtins.str, sort_order: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> _builtins.int: ...

@pulumi.output_type
class SecurityConfigurationEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloudwatch_encryption: outputs.SecurityConfigurationEncryptionConfigurationCloudwatchEncryption,
        job_bookmarks_encryption: outputs.SecurityConfigurationEncryptionConfigurationJobBookmarksEncryption,
        s3_encryption: outputs.SecurityConfigurationEncryptionConfigurationS3Encryption,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchEncryption")
    def cloudwatch_encryption(
        self,
    ) -> outputs.SecurityConfigurationEncryptionConfigurationCloudwatchEncryption: ...
    @_builtins.property
    @pulumi.getter(name="jobBookmarksEncryption")
    def job_bookmarks_encryption(
        self,
    ) -> outputs.SecurityConfigurationEncryptionConfigurationJobBookmarksEncryption: ...
    @_builtins.property
    @pulumi.getter(name="s3Encryption")
    def s3_encryption(
        self,
    ) -> outputs.SecurityConfigurationEncryptionConfigurationS3Encryption: ...

@pulumi.output_type
class SecurityConfigurationEncryptionConfigurationCloudwatchEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloudwatch_encryption_mode: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchEncryptionMode")
    def cloudwatch_encryption_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SecurityConfigurationEncryptionConfigurationJobBookmarksEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        job_bookmarks_encryption_mode: Optional[_builtins.str] = ...,
        kms_key_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobBookmarksEncryptionMode")
    def job_bookmarks_encryption_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SecurityConfigurationEncryptionConfigurationS3Encryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_arn: Optional[_builtins.str] = ...,
        s3_encryption_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3EncryptionMode")
    def s3_encryption_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TriggerAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arguments: Optional[Mapping[str, _builtins.str]] = ...,
        crawler_name: Optional[_builtins.str] = ...,
        job_name: Optional[_builtins.str] = ...,
        notification_property: Optional[
            outputs.TriggerActionNotificationProperty
        ] = ...,
        security_configuration: Optional[_builtins.str] = ...,
        timeout: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="crawlerName")
    def crawler_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationProperty")
    def notification_property(
        self,
    ) -> Optional[outputs.TriggerActionNotificationProperty]: ...
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TriggerActionNotificationProperty(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, notify_delay_after: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notifyDelayAfter")
    def notify_delay_after(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TriggerEventBatchingCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        batch_size: _builtins.int,
        batch_window: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="batchWindow")
    def batch_window(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TriggerPredicate(dict):
    def __init__(
        __self__,
        *,
        conditions: Sequence[outputs.TriggerPredicateCondition],
        logical: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Sequence[outputs.TriggerPredicateCondition]: ...
    @_builtins.property
    @pulumi.getter
    def logical(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TriggerPredicateCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        crawl_state: Optional[_builtins.str] = ...,
        crawler_name: Optional[_builtins.str] = ...,
        job_name: Optional[_builtins.str] = ...,
        logical_operator: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crawlState")
    def crawl_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="crawlerName")
    def crawler_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logicalOperator")
    def logical_operator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserDefinedFunctionResourceUri(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, resource_type: _builtins.str, uri: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetCatalogTablePartitionIndexResult(dict):
    def __init__(
        __self__,
        *,
        index_name: _builtins.str,
        index_status: _builtins.str,
        keys: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="indexStatus")
    def index_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCatalogTablePartitionKeyResult(dict):
    def __init__(
        __self__,
        *,
        comment: _builtins.str,
        name: _builtins.str,
        parameters: Mapping[str, _builtins.str],
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetCatalogTableStorageDescriptorResult(dict):
    def __init__(
        __self__,
        *,
        additional_locations: Sequence[_builtins.str],
        bucket_columns: Sequence[_builtins.str],
        columns: Sequence[outputs.GetCatalogTableStorageDescriptorColumnResult],
        compressed: _builtins.bool,
        input_format: _builtins.str,
        location: _builtins.str,
        number_of_buckets: _builtins.int,
        output_format: _builtins.str,
        parameters: Mapping[str, _builtins.str],
        schema_references: Sequence[
            outputs.GetCatalogTableStorageDescriptorSchemaReferenceResult
        ],
        ser_de_infos: Sequence[outputs.GetCatalogTableStorageDescriptorSerDeInfoResult],
        skewed_infos: Sequence[
            outputs.GetCatalogTableStorageDescriptorSkewedInfoResult
        ],
        sort_columns: Sequence[
            outputs.GetCatalogTableStorageDescriptorSortColumnResult
        ],
        stored_as_sub_directories: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalLocations")
    def additional_locations(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketColumns")
    def bucket_columns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Sequence[outputs.GetCatalogTableStorageDescriptorColumnResult]: ...
    @_builtins.property
    @pulumi.getter
    def compressed(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="numberOfBuckets")
    def number_of_buckets(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaReferences")
    def schema_references(
        self,
    ) -> Sequence[outputs.GetCatalogTableStorageDescriptorSchemaReferenceResult]: ...
    @_builtins.property
    @pulumi.getter(name="serDeInfos")
    def ser_de_infos(
        self,
    ) -> Sequence[outputs.GetCatalogTableStorageDescriptorSerDeInfoResult]: ...
    @_builtins.property
    @pulumi.getter(name="skewedInfos")
    def skewed_infos(
        self,
    ) -> Sequence[outputs.GetCatalogTableStorageDescriptorSkewedInfoResult]: ...
    @_builtins.property
    @pulumi.getter(name="sortColumns")
    def sort_columns(
        self,
    ) -> Sequence[outputs.GetCatalogTableStorageDescriptorSortColumnResult]: ...
    @_builtins.property
    @pulumi.getter(name="storedAsSubDirectories")
    def stored_as_sub_directories(self) -> _builtins.bool: ...

@pulumi.output_type
class GetCatalogTableStorageDescriptorColumnResult(dict):
    def __init__(
        __self__,
        *,
        comment: _builtins.str,
        name: _builtins.str,
        parameters: Mapping[str, _builtins.str],
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetCatalogTableStorageDescriptorSchemaReferenceResult(dict):
    def __init__(
        __self__,
        *,
        schema_ids: Sequence[
            outputs.GetCatalogTableStorageDescriptorSchemaReferenceSchemaIdResult
        ],
        schema_version_id: _builtins.str,
        schema_version_number: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schemaIds")
    def schema_ids(
        self,
    ) -> Sequence[
        outputs.GetCatalogTableStorageDescriptorSchemaReferenceSchemaIdResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="schemaVersionId")
    def schema_version_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="schemaVersionNumber")
    def schema_version_number(self) -> _builtins.int: ...

@pulumi.output_type
class GetCatalogTableStorageDescriptorSchemaReferenceSchemaIdResult(dict):
    def __init__(
        __self__,
        *,
        registry_name: _builtins.str,
        schema_arn: _builtins.str,
        schema_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="schemaArn")
    def schema_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetCatalogTableStorageDescriptorSerDeInfoResult(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: Mapping[str, _builtins.str],
        serialization_library: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serializationLibrary")
    def serialization_library(self) -> _builtins.str: ...

@pulumi.output_type
class GetCatalogTableStorageDescriptorSkewedInfoResult(dict):
    def __init__(
        __self__,
        *,
        skewed_column_names: Sequence[_builtins.str],
        skewed_column_value_location_maps: Mapping[str, _builtins.str],
        skewed_column_values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="skewedColumnNames")
    def skewed_column_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skewedColumnValueLocationMaps")
    def skewed_column_value_location_maps(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skewedColumnValues")
    def skewed_column_values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCatalogTableStorageDescriptorSortColumnResult(dict):
    def __init__(
        __self__, *, column: _builtins.str, sort_order: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> _builtins.int: ...

@pulumi.output_type
class GetCatalogTableTargetTableResult(dict):
    def __init__(
        __self__,
        *,
        catalog_id: _builtins.str,
        database_name: _builtins.str,
        name: _builtins.str,
        region: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

@pulumi.output_type
class GetConnectionPhysicalConnectionRequirementResult(dict):
    def __init__(
        __self__,
        *,
        availability_zone: _builtins.str,
        security_group_id_lists: Sequence[_builtins.str],
        subnet_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIdLists")
    def security_group_id_lists(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataCatalogEncryptionSettingsDataCatalogEncryptionSettingResult(dict):
    def __init__(
        __self__,
        *,
        connection_password_encryptions: Sequence[
            outputs.GetDataCatalogEncryptionSettingsDataCatalogEncryptionSettingConnectionPasswordEncryptionResult
        ],
        encryption_at_rests: Sequence[
            outputs.GetDataCatalogEncryptionSettingsDataCatalogEncryptionSettingEncryptionAtRestResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionPasswordEncryptions")
    def connection_password_encryptions(
        self,
    ) -> Sequence[
        outputs.GetDataCatalogEncryptionSettingsDataCatalogEncryptionSettingConnectionPasswordEncryptionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionAtRests")
    def encryption_at_rests(
        self,
    ) -> Sequence[
        outputs.GetDataCatalogEncryptionSettingsDataCatalogEncryptionSettingEncryptionAtRestResult
    ]: ...

@pulumi.output_type
class GetDataCatalogEncryptionSettingsDataCatalogEncryptionSettingConnectionPasswordEncryptionResult(
    dict
):
    def __init__(
        __self__,
        *,
        aws_kms_key_id: _builtins.str,
        return_connection_password_encrypted: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsKmsKeyId")
    def aws_kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="returnConnectionPasswordEncrypted")
    def return_connection_password_encrypted(self) -> _builtins.bool: ...

@pulumi.output_type
class GetDataCatalogEncryptionSettingsDataCatalogEncryptionSettingEncryptionAtRestResult(
    dict
):
    def __init__(
        __self__,
        *,
        catalog_encryption_mode: _builtins.str,
        catalog_encryption_service_role: _builtins.str,
        sse_aws_kms_key_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="catalogEncryptionMode")
    def catalog_encryption_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="catalogEncryptionServiceRole")
    def catalog_encryption_service_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sseAwsKmsKeyId")
    def sse_aws_kms_key_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetScriptDagEdgeResult(dict):
    def __init__(
        __self__,
        *,
        source: _builtins.str,
        target: _builtins.str,
        target_parameter: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetParameter")
    def target_parameter(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetScriptDagNodeResult(dict):
    def __init__(
        __self__,
        *,
        args: Sequence[outputs.GetScriptDagNodeArgResult],
        id: _builtins.str,
        node_type: _builtins.str,
        line_number: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Sequence[outputs.GetScriptDagNodeArgResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lineNumber")
    def line_number(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GetScriptDagNodeArgResult(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        value: _builtins.str,
        param: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def param(self) -> Optional[_builtins.bool]: ...
