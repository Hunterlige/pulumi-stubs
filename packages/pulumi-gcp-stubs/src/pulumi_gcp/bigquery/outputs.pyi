import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppProfileDataBoostIsolationReadOnly",
    "AppProfileSingleClusterRouting",
    "AppProfileStandardIsolation",
    "BiReservationPreferredTable",
    "ConnectionAws",
    "ConnectionAwsAccessRole",
    "ConnectionAzure",
    "ConnectionCloudResource",
    "ConnectionCloudSpanner",
    "ConnectionCloudSql",
    "ConnectionCloudSqlCredential",
    "ConnectionIamBindingCondition",
    "ConnectionIamMemberCondition",
    "ConnectionSpark",
    "ConnectionSparkMetastoreServiceConfig",
    "ConnectionSparkSparkHistoryServerConfig",
    "DataTransferConfigEmailPreferences",
    "DataTransferConfigEncryptionConfiguration",
    "DataTransferConfigScheduleOptions",
    "DataTransferConfigSensitiveParams",
    "Datapolicyv2DataPolicyDataMaskingPolicy",
    "Datapolicyv2DataPolicyIamBindingCondition",
    "Datapolicyv2DataPolicyIamMemberCondition",
    "DatasetAccess",
    "DatasetAccessAuthorizedDataset",
    "DatasetAccessAuthorizedDatasetDataset",
    "DatasetAccessCondition",
    "DatasetAccessDataset",
    "DatasetAccessDatasetDataset",
    "DatasetAccessRoutine",
    "DatasetAccessView",
    "DatasetDefaultEncryptionConfiguration",
    "DatasetExternalCatalogDatasetOptions",
    "DatasetExternalDatasetReference",
    "DatasetIamBindingCondition",
    "DatasetIamMemberCondition",
    "IamBindingCondition",
    "IamMemberCondition",
    "JobCopy",
    "JobCopyDestinationEncryptionConfiguration",
    "JobCopyDestinationTable",
    "JobCopySourceTable",
    "JobExtract",
    "JobExtractSourceModel",
    "JobExtractSourceTable",
    "JobLoad",
    "JobLoadDestinationEncryptionConfiguration",
    "JobLoadDestinationTable",
    "JobLoadParquetOptions",
    "JobLoadTimePartitioning",
    "JobQuery",
    "JobQueryConnectionProperty",
    "JobQueryDefaultDataset",
    "JobQueryDestinationEncryptionConfiguration",
    "JobQueryDestinationTable",
    "JobQueryScriptOptions",
    "JobQueryUserDefinedFunctionResource",
    "JobStatus",
    "JobStatusError",
    "JobStatusErrorResult",
    "ReservationAutoscale",
    "ReservationReplicationStatus",
    "ReservationReplicationStatusError",
    "RoutineArgument",
    "RoutineExternalRuntimeOptions",
    "RoutinePythonOptions",
    "RoutineRemoteFunctionOptions",
    "RoutineSparkOptions",
    "TableBiglakeConfiguration",
    "TableEncryptionConfiguration",
    "TableExternalCatalogTableOptions",
    "TableExternalCatalogTableOptionsStorageDescriptor",
    ...,
    "TableExternalDataConfiguration",
    "TableExternalDataConfigurationAvroOptions",
    "TableExternalDataConfigurationBigtableOptions",
    ...,
    ...,
    "TableExternalDataConfigurationCsvOptions",
    "TableExternalDataConfigurationGoogleSheetsOptions",
    ...,
    "TableExternalDataConfigurationJsonOptions",
    "TableExternalDataConfigurationParquetOptions",
    "TableMaterializedView",
    "TableRangePartitioning",
    "TableRangePartitioningRange",
    "TableSchemaForeignTypeInfo",
    "TableTableConstraints",
    "TableTableConstraintsForeignKey",
    "TableTableConstraintsForeignKeyColumnReferences",
    "TableTableConstraintsForeignKeyReferencedTable",
    "TableTableConstraintsPrimaryKey",
    "TableTableReplicationInfo",
    "TableTimePartitioning",
    "TableView",
    "GetDatasetAccessResult",
    "GetDatasetAccessConditionResult",
    "GetDatasetAccessDatasetResult",
    "GetDatasetAccessDatasetDatasetResult",
    "GetDatasetAccessRoutineResult",
    "GetDatasetAccessViewResult",
    "GetDatasetDefaultEncryptionConfigurationResult",
    "GetDatasetExternalCatalogDatasetOptionResult",
    "GetDatasetExternalDatasetReferenceResult",
    "GetDatasetsDatasetResult",
    "GetTableBiglakeConfigurationResult",
    "GetTableEncryptionConfigurationResult",
    "GetTableExternalCatalogTableOptionResult",
    ...,
    ...,
    "GetTableExternalDataConfigurationResult",
    "GetTableExternalDataConfigurationAvroOptionResult",
    ...,
    ...,
    ...,
    "GetTableExternalDataConfigurationCsvOptionResult",
    ...,
    ...,
    "GetTableExternalDataConfigurationJsonOptionResult",
    ...,
    "GetTableMaterializedViewResult",
    "GetTableRangePartitioningResult",
    "GetTableRangePartitioningRangeResult",
    "GetTableSchemaForeignTypeInfoResult",
    "GetTableTableConstraintResult",
    "GetTableTableConstraintForeignKeyResult",
    ...,
    ...,
    "GetTableTableConstraintPrimaryKeyResult",
    "GetTableTableReplicationInfoResult",
    "GetTableTimePartitioningResult",
    "GetTableViewResult",
    "GetTablesTableResult",
]

@pulumi.output_type
class AppProfileDataBoostIsolationReadOnly(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, compute_billing_owner: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeBillingOwner")
    def compute_billing_owner(self) -> _builtins.str: ...

@pulumi.output_type
class AppProfileSingleClusterRouting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_id: _builtins.str,
        allow_transactional_writes: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowTransactionalWrites")
    def allow_transactional_writes(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AppProfileStandardIsolation(dict):
    def __init__(__self__, *, priority: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.str: ...

@pulumi.output_type
class BiReservationPreferredTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset_id: Optional[_builtins.str] = ...,
        project_id: Optional[_builtins.str] = ...,
        table_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionAws(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, access_role: outputs.ConnectionAwsAccessRole) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessRole")
    def access_role(self) -> outputs.ConnectionAwsAccessRole: ...

@pulumi.output_type
class ConnectionAwsAccessRole(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, iam_role_id: _builtins.str, identity: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamRoleId")
    def iam_role_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionAzure(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        customer_tenant_id: _builtins.str,
        application: Optional[_builtins.str] = ...,
        client_id: Optional[_builtins.str] = ...,
        federated_application_client_id: Optional[_builtins.str] = ...,
        identity: Optional[_builtins.str] = ...,
        object_id: Optional[_builtins.str] = ...,
        redirect_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerTenantId")
    def customer_tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def application(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="federatedApplicationClientId")
    def federated_application_client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionCloudResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, service_account_id: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionCloudSpanner(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database: _builtins.str,
        database_role: Optional[_builtins.str] = ...,
        max_parallelism: Optional[_builtins.int] = ...,
        use_data_boost: Optional[_builtins.bool] = ...,
        use_parallelism: Optional[_builtins.bool] = ...,
        use_serverless_analytics: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseRole")
    def database_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxParallelism")
    def max_parallelism(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="useDataBoost")
    def use_data_boost(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="useParallelism")
    def use_parallelism(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="useServerlessAnalytics")
    @_utilities.deprecated(...)
    def use_serverless_analytics(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConnectionCloudSql(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        credential: outputs.ConnectionCloudSqlCredential,
        database: _builtins.str,
        instance_id: _builtins.str,
        type: _builtins.str,
        service_account_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credential(self) -> outputs.ConnectionCloudSqlCredential: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionCloudSqlCredential(dict):
    def __init__(
        __self__, *, password: _builtins.str, username: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionSpark(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metastore_service_config: Optional[
            outputs.ConnectionSparkMetastoreServiceConfig
        ] = ...,
        service_account_id: Optional[_builtins.str] = ...,
        spark_history_server_config: Optional[
            outputs.ConnectionSparkSparkHistoryServerConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metastoreServiceConfig")
    def metastore_service_config(
        self,
    ) -> Optional[outputs.ConnectionSparkMetastoreServiceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sparkHistoryServerConfig")
    def spark_history_server_config(
        self,
    ) -> Optional[outputs.ConnectionSparkSparkHistoryServerConfig]: ...

@pulumi.output_type
class ConnectionSparkMetastoreServiceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, metastore_service: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metastoreService")
    def metastore_service(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionSparkSparkHistoryServerConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, dataproc_cluster: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataprocCluster")
    def dataproc_cluster(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataTransferConfigEmailPreferences(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enable_failure_email: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableFailureEmail")
    def enable_failure_email(self) -> _builtins.bool: ...

@pulumi.output_type
class DataTransferConfigEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class DataTransferConfigScheduleOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_auto_scheduling: Optional[_builtins.bool] = ...,
        end_time: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableAutoScheduling")
    def disable_auto_scheduling(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataTransferConfigSensitiveParams(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secret_access_key: Optional[_builtins.str] = ...,
        secret_access_key_wo: Optional[_builtins.str] = ...,
        secret_access_key_wo_version: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretAccessKeyWo")
    def secret_access_key_wo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretAccessKeyWoVersion")
    def secret_access_key_wo_version(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class Datapolicyv2DataPolicyDataMaskingPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        predefined_expression: Optional[_builtins.str] = ...,
        routine: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedExpression")
    def predefined_expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def routine(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class Datapolicyv2DataPolicyIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class Datapolicyv2DataPolicyIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatasetAccess(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        condition: Optional[outputs.DatasetAccessCondition] = ...,
        dataset: Optional[outputs.DatasetAccessDataset] = ...,
        domain: Optional[_builtins.str] = ...,
        group_by_email: Optional[_builtins.str] = ...,
        iam_member: Optional[_builtins.str] = ...,
        role: Optional[_builtins.str] = ...,
        routine: Optional[outputs.DatasetAccessRoutine] = ...,
        special_group: Optional[_builtins.str] = ...,
        user_by_email: Optional[_builtins.str] = ...,
        view: Optional[outputs.DatasetAccessView] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.DatasetAccessCondition]: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[outputs.DatasetAccessDataset]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupByEmail")
    def group_by_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iamMember")
    def iam_member(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def routine(self) -> Optional[outputs.DatasetAccessRoutine]: ...
    @_builtins.property
    @pulumi.getter(name="specialGroup")
    def special_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userByEmail")
    def user_by_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def view(self) -> Optional[outputs.DatasetAccessView]: ...

@pulumi.output_type
class DatasetAccessAuthorizedDataset(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset: outputs.DatasetAccessAuthorizedDatasetDataset,
        target_types: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> outputs.DatasetAccessAuthorizedDatasetDataset: ...
    @_builtins.property
    @pulumi.getter(name="targetTypes")
    def target_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class DatasetAccessAuthorizedDatasetDataset(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, dataset_id: _builtins.str, project_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...

@pulumi.output_type
class DatasetAccessCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        description: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatasetAccessDataset(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset: outputs.DatasetAccessDatasetDataset,
        target_types: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> outputs.DatasetAccessDatasetDataset: ...
    @_builtins.property
    @pulumi.getter(name="targetTypes")
    def target_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class DatasetAccessDatasetDataset(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, dataset_id: _builtins.str, project_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...

@pulumi.output_type
class DatasetAccessRoutine(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset_id: _builtins.str,
        project_id: _builtins.str,
        routine_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routineId")
    def routine_id(self) -> _builtins.str: ...

@pulumi.output_type
class DatasetAccessView(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset_id: _builtins.str,
        project_id: _builtins.str,
        table_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str: ...

@pulumi.output_type
class DatasetDefaultEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class DatasetExternalCatalogDatasetOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_storage_location_uri: Optional[_builtins.str] = ...,
        parameters: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultStorageLocationUri")
    def default_storage_location_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class DatasetExternalDatasetReference(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, connection: _builtins.str, external_source: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connection(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="externalSource")
    def external_source(self) -> _builtins.str: ...

@pulumi.output_type
class DatasetIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatasetIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobCopy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_tables: Sequence[outputs.JobCopySourceTable],
        create_disposition: Optional[_builtins.str] = ...,
        destination_encryption_configuration: Optional[
            outputs.JobCopyDestinationEncryptionConfiguration
        ] = ...,
        destination_table: Optional[outputs.JobCopyDestinationTable] = ...,
        write_disposition: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceTables")
    def source_tables(self) -> Sequence[outputs.JobCopySourceTable]: ...
    @_builtins.property
    @pulumi.getter(name="createDisposition")
    def create_disposition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationEncryptionConfiguration")
    def destination_encryption_configuration(
        self,
    ) -> Optional[outputs.JobCopyDestinationEncryptionConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="destinationTable")
    def destination_table(self) -> Optional[outputs.JobCopyDestinationTable]: ...
    @_builtins.property
    @pulumi.getter(name="writeDisposition")
    def write_disposition(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobCopyDestinationEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_name: _builtins.str,
        kms_key_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersion")
    def kms_key_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobCopyDestinationTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table_id: _builtins.str,
        dataset_id: Optional[_builtins.str] = ...,
        project_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobCopySourceTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table_id: _builtins.str,
        dataset_id: Optional[_builtins.str] = ...,
        project_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobExtract(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_uris: Sequence[_builtins.str],
        compression: Optional[_builtins.str] = ...,
        destination_format: Optional[_builtins.str] = ...,
        field_delimiter: Optional[_builtins.str] = ...,
        print_header: Optional[_builtins.bool] = ...,
        source_model: Optional[outputs.JobExtractSourceModel] = ...,
        source_table: Optional[outputs.JobExtractSourceTable] = ...,
        use_avro_logical_types: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationUris")
    def destination_uris(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationFormat")
    def destination_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="printHeader")
    def print_header(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sourceModel")
    def source_model(self) -> Optional[outputs.JobExtractSourceModel]: ...
    @_builtins.property
    @pulumi.getter(name="sourceTable")
    def source_table(self) -> Optional[outputs.JobExtractSourceTable]: ...
    @_builtins.property
    @pulumi.getter(name="useAvroLogicalTypes")
    def use_avro_logical_types(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class JobExtractSourceModel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset_id: _builtins.str,
        model_id: _builtins.str,
        project_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...

@pulumi.output_type
class JobExtractSourceTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table_id: _builtins.str,
        dataset_id: Optional[_builtins.str] = ...,
        project_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobLoad(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_table: outputs.JobLoadDestinationTable,
        source_uris: Sequence[_builtins.str],
        allow_jagged_rows: Optional[_builtins.bool] = ...,
        allow_quoted_newlines: Optional[_builtins.bool] = ...,
        autodetect: Optional[_builtins.bool] = ...,
        create_disposition: Optional[_builtins.str] = ...,
        destination_encryption_configuration: Optional[
            outputs.JobLoadDestinationEncryptionConfiguration
        ] = ...,
        encoding: Optional[_builtins.str] = ...,
        field_delimiter: Optional[_builtins.str] = ...,
        ignore_unknown_values: Optional[_builtins.bool] = ...,
        json_extension: Optional[_builtins.str] = ...,
        max_bad_records: Optional[_builtins.int] = ...,
        null_marker: Optional[_builtins.str] = ...,
        parquet_options: Optional[outputs.JobLoadParquetOptions] = ...,
        projection_fields: Optional[Sequence[_builtins.str]] = ...,
        quote: Optional[_builtins.str] = ...,
        schema_update_options: Optional[Sequence[_builtins.str]] = ...,
        skip_leading_rows: Optional[_builtins.int] = ...,
        source_format: Optional[_builtins.str] = ...,
        time_partitioning: Optional[outputs.JobLoadTimePartitioning] = ...,
        write_disposition: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationTable")
    def destination_table(self) -> outputs.JobLoadDestinationTable: ...
    @_builtins.property
    @pulumi.getter(name="sourceUris")
    def source_uris(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowJaggedRows")
    def allow_jagged_rows(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowQuotedNewlines")
    def allow_quoted_newlines(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def autodetect(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="createDisposition")
    def create_disposition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationEncryptionConfiguration")
    def destination_encryption_configuration(
        self,
    ) -> Optional[outputs.JobLoadDestinationEncryptionConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownValues")
    def ignore_unknown_values(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="jsonExtension")
    def json_extension(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxBadRecords")
    def max_bad_records(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="nullMarker")
    def null_marker(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parquetOptions")
    def parquet_options(self) -> Optional[outputs.JobLoadParquetOptions]: ...
    @_builtins.property
    @pulumi.getter(name="projectionFields")
    def projection_fields(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def quote(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaUpdateOptions")
    def schema_update_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="skipLeadingRows")
    def skip_leading_rows(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sourceFormat")
    def source_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timePartitioning")
    def time_partitioning(self) -> Optional[outputs.JobLoadTimePartitioning]: ...
    @_builtins.property
    @pulumi.getter(name="writeDisposition")
    def write_disposition(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobLoadDestinationEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_name: _builtins.str,
        kms_key_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersion")
    def kms_key_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobLoadDestinationTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table_id: _builtins.str,
        dataset_id: Optional[_builtins.str] = ...,
        project_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobLoadParquetOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_list_inference: Optional[_builtins.bool] = ...,
        enum_as_string: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableListInference")
    def enable_list_inference(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enumAsString")
    def enum_as_string(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class JobLoadTimePartitioning(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        expiration_ms: Optional[_builtins.str] = ...,
        field: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expirationMs")
    def expiration_ms(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobQuery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        query: _builtins.str,
        allow_large_results: Optional[_builtins.bool] = ...,
        connection_properties: Optional[
            Sequence[outputs.JobQueryConnectionProperty]
        ] = ...,
        continuous: Optional[_builtins.bool] = ...,
        create_disposition: Optional[_builtins.str] = ...,
        default_dataset: Optional[outputs.JobQueryDefaultDataset] = ...,
        destination_encryption_configuration: Optional[
            outputs.JobQueryDestinationEncryptionConfiguration
        ] = ...,
        destination_table: Optional[outputs.JobQueryDestinationTable] = ...,
        flatten_results: Optional[_builtins.bool] = ...,
        maximum_billing_tier: Optional[_builtins.int] = ...,
        maximum_bytes_billed: Optional[_builtins.str] = ...,
        parameter_mode: Optional[_builtins.str] = ...,
        priority: Optional[_builtins.str] = ...,
        schema_update_options: Optional[Sequence[_builtins.str]] = ...,
        script_options: Optional[outputs.JobQueryScriptOptions] = ...,
        use_legacy_sql: Optional[_builtins.bool] = ...,
        use_query_cache: Optional[_builtins.bool] = ...,
        user_defined_function_resources: Optional[
            Sequence[outputs.JobQueryUserDefinedFunctionResource]
        ] = ...,
        write_disposition: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowLargeResults")
    def allow_large_results(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="connectionProperties")
    def connection_properties(
        self,
    ) -> Optional[Sequence[outputs.JobQueryConnectionProperty]]: ...
    @_builtins.property
    @pulumi.getter
    def continuous(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="createDisposition")
    def create_disposition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultDataset")
    def default_dataset(self) -> Optional[outputs.JobQueryDefaultDataset]: ...
    @_builtins.property
    @pulumi.getter(name="destinationEncryptionConfiguration")
    def destination_encryption_configuration(
        self,
    ) -> Optional[outputs.JobQueryDestinationEncryptionConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="destinationTable")
    def destination_table(self) -> Optional[outputs.JobQueryDestinationTable]: ...
    @_builtins.property
    @pulumi.getter(name="flattenResults")
    def flatten_results(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="maximumBillingTier")
    def maximum_billing_tier(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maximumBytesBilled")
    def maximum_bytes_billed(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parameterMode")
    def parameter_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaUpdateOptions")
    def schema_update_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="scriptOptions")
    def script_options(self) -> Optional[outputs.JobQueryScriptOptions]: ...
    @_builtins.property
    @pulumi.getter(name="useLegacySql")
    def use_legacy_sql(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="useQueryCache")
    def use_query_cache(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="userDefinedFunctionResources")
    def user_defined_function_resources(
        self,
    ) -> Optional[Sequence[outputs.JobQueryUserDefinedFunctionResource]]: ...
    @_builtins.property
    @pulumi.getter(name="writeDisposition")
    def write_disposition(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobQueryConnectionProperty(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class JobQueryDefaultDataset(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset_id: _builtins.str,
        project_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobQueryDestinationEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_name: _builtins.str,
        kms_key_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersion")
    def kms_key_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobQueryDestinationTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table_id: _builtins.str,
        dataset_id: Optional[_builtins.str] = ...,
        project_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobQueryScriptOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_result_statement: Optional[_builtins.str] = ...,
        statement_byte_budget: Optional[_builtins.str] = ...,
        statement_timeout_ms: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyResultStatement")
    def key_result_statement(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statementByteBudget")
    def statement_byte_budget(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statementTimeoutMs")
    def statement_timeout_ms(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobQueryUserDefinedFunctionResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        inline_code: Optional[_builtins.str] = ...,
        resource_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlineCode")
    def inline_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_results: Optional[Sequence[outputs.JobStatusErrorResult]] = ...,
        errors: Optional[Sequence[outputs.JobStatusError]] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorResults")
    def error_results(self) -> Optional[Sequence[outputs.JobStatusErrorResult]]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[Sequence[outputs.JobStatusError]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobStatusError(dict):
    def __init__(
        __self__,
        *,
        location: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
        reason: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobStatusErrorResult(dict):
    def __init__(
        __self__,
        *,
        location: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
        reason: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReservationAutoscale(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        current_slots: Optional[_builtins.int] = ...,
        max_slots: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentSlots")
    def current_slots(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxSlots")
    def max_slots(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ReservationReplicationStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        errors: Optional[Sequence[outputs.ReservationReplicationStatusError]] = ...,
        last_error_time: Optional[_builtins.str] = ...,
        last_replication_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def errors(
        self,
    ) -> Optional[Sequence[outputs.ReservationReplicationStatusError]]: ...
    @_builtins.property
    @pulumi.getter(name="lastErrorTime")
    def last_error_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastReplicationTime")
    def last_replication_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReservationReplicationStatusError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.int] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoutineArgument(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        argument_kind: Optional[_builtins.str] = ...,
        data_type: Optional[_builtins.str] = ...,
        mode: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="argumentKind")
    def argument_kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoutineExternalRuntimeOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_cpu: Optional[_builtins.float] = ...,
        container_memory: Optional[_builtins.str] = ...,
        max_batching_rows: Optional[_builtins.str] = ...,
        runtime_connection: Optional[_builtins.str] = ...,
        runtime_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerCpu")
    def container_cpu(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="containerMemory")
    def container_memory(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxBatchingRows")
    def max_batching_rows(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeConnection")
    def runtime_connection(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoutinePythonOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        entry_point: _builtins.str,
        packages: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def packages(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RoutineRemoteFunctionOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection: Optional[_builtins.str] = ...,
        endpoint: Optional[_builtins.str] = ...,
        max_batching_rows: Optional[_builtins.str] = ...,
        user_defined_context: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connection(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxBatchingRows")
    def max_batching_rows(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userDefinedContext")
    def user_defined_context(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class RoutineSparkOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        archive_uris: Optional[Sequence[_builtins.str]] = ...,
        connection: Optional[_builtins.str] = ...,
        container_image: Optional[_builtins.str] = ...,
        file_uris: Optional[Sequence[_builtins.str]] = ...,
        jar_uris: Optional[Sequence[_builtins.str]] = ...,
        main_class: Optional[_builtins.str] = ...,
        main_file_uri: Optional[_builtins.str] = ...,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
        py_file_uris: Optional[Sequence[_builtins.str]] = ...,
        runtime_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def connection(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="jarUris")
    def jar_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mainFileUri")
    def main_file_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pyFileUris")
    def py_file_uris(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableBiglakeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_id: _builtins.str,
        file_format: _builtins.str,
        storage_uri: _builtins.str,
        table_format: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileFormat")
    def file_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageUri")
    def storage_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableFormat")
    def table_format(self) -> _builtins.str: ...

@pulumi.output_type
class TableEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_name: _builtins.str,
        kms_key_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersion")
    def kms_key_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableExternalCatalogTableOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_id: Optional[_builtins.str] = ...,
        parameters: Optional[Mapping[str, _builtins.str]] = ...,
        storage_descriptor: Optional[
            outputs.TableExternalCatalogTableOptionsStorageDescriptor
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageDescriptor")
    def storage_descriptor(
        self,
    ) -> Optional[outputs.TableExternalCatalogTableOptionsStorageDescriptor]: ...

@pulumi.output_type
class TableExternalCatalogTableOptionsStorageDescriptor(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input_format: Optional[_builtins.str] = ...,
        location_uri: Optional[_builtins.str] = ...,
        output_format: Optional[_builtins.str] = ...,
        serde_info: Optional[
            outputs.TableExternalCatalogTableOptionsStorageDescriptorSerdeInfo
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serdeInfo")
    def serde_info(
        self,
    ) -> Optional[
        outputs.TableExternalCatalogTableOptionsStorageDescriptorSerdeInfo
    ]: ...

@pulumi.output_type
class TableExternalCatalogTableOptionsStorageDescriptorSerdeInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        serialization_library: _builtins.str,
        name: Optional[_builtins.str] = ...,
        parameters: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serializationLibrary")
    def serialization_library(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class TableExternalDataConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        autodetect: _builtins.bool,
        source_uris: Sequence[_builtins.str],
        avro_options: Optional[outputs.TableExternalDataConfigurationAvroOptions] = ...,
        bigtable_options: Optional[
            outputs.TableExternalDataConfigurationBigtableOptions
        ] = ...,
        compression: Optional[_builtins.str] = ...,
        connection_id: Optional[_builtins.str] = ...,
        csv_options: Optional[outputs.TableExternalDataConfigurationCsvOptions] = ...,
        decimal_target_types: Optional[Sequence[_builtins.str]] = ...,
        file_set_spec_type: Optional[_builtins.str] = ...,
        google_sheets_options: Optional[
            outputs.TableExternalDataConfigurationGoogleSheetsOptions
        ] = ...,
        hive_partitioning_options: Optional[
            outputs.TableExternalDataConfigurationHivePartitioningOptions
        ] = ...,
        ignore_unknown_values: Optional[_builtins.bool] = ...,
        json_extension: Optional[_builtins.str] = ...,
        json_options: Optional[outputs.TableExternalDataConfigurationJsonOptions] = ...,
        max_bad_records: Optional[_builtins.int] = ...,
        metadata_cache_mode: Optional[_builtins.str] = ...,
        object_metadata: Optional[_builtins.str] = ...,
        parquet_options: Optional[
            outputs.TableExternalDataConfigurationParquetOptions
        ] = ...,
        reference_file_schema_uri: Optional[_builtins.str] = ...,
        schema: Optional[_builtins.str] = ...,
        source_format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def autodetect(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="sourceUris")
    def source_uris(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="avroOptions")
    def avro_options(
        self,
    ) -> Optional[outputs.TableExternalDataConfigurationAvroOptions]: ...
    @_builtins.property
    @pulumi.getter(name="bigtableOptions")
    def bigtable_options(
        self,
    ) -> Optional[outputs.TableExternalDataConfigurationBigtableOptions]: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="csvOptions")
    def csv_options(
        self,
    ) -> Optional[outputs.TableExternalDataConfigurationCsvOptions]: ...
    @_builtins.property
    @pulumi.getter(name="decimalTargetTypes")
    def decimal_target_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fileSetSpecType")
    def file_set_spec_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="googleSheetsOptions")
    def google_sheets_options(
        self,
    ) -> Optional[outputs.TableExternalDataConfigurationGoogleSheetsOptions]: ...
    @_builtins.property
    @pulumi.getter(name="hivePartitioningOptions")
    def hive_partitioning_options(
        self,
    ) -> Optional[outputs.TableExternalDataConfigurationHivePartitioningOptions]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownValues")
    def ignore_unknown_values(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="jsonExtension")
    def json_extension(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jsonOptions")
    def json_options(
        self,
    ) -> Optional[outputs.TableExternalDataConfigurationJsonOptions]: ...
    @_builtins.property
    @pulumi.getter(name="maxBadRecords")
    def max_bad_records(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="metadataCacheMode")
    def metadata_cache_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectMetadata")
    def object_metadata(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parquetOptions")
    def parquet_options(
        self,
    ) -> Optional[outputs.TableExternalDataConfigurationParquetOptions]: ...
    @_builtins.property
    @pulumi.getter(name="referenceFileSchemaUri")
    def reference_file_schema_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceFormat")
    def source_format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableExternalDataConfigurationAvroOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, use_avro_logical_types: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="useAvroLogicalTypes")
    def use_avro_logical_types(self) -> _builtins.bool: ...

@pulumi.output_type
class TableExternalDataConfigurationBigtableOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column_families: Optional[
            Sequence[outputs.TableExternalDataConfigurationBigtableOptionsColumnFamily]
        ] = ...,
        ignore_unspecified_column_families: Optional[_builtins.bool] = ...,
        output_column_families_as_json: Optional[_builtins.bool] = ...,
        read_rowkey_as_string: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnFamilies")
    def column_families(
        self,
    ) -> Optional[
        Sequence[outputs.TableExternalDataConfigurationBigtableOptionsColumnFamily]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreUnspecifiedColumnFamilies")
    def ignore_unspecified_column_families(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="outputColumnFamiliesAsJson")
    def output_column_families_as_json(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="readRowkeyAsString")
    def read_rowkey_as_string(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class TableExternalDataConfigurationBigtableOptionsColumnFamily(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        columns: Optional[
            Sequence[
                outputs.TableExternalDataConfigurationBigtableOptionsColumnFamilyColumn
            ]
        ] = ...,
        encoding: Optional[_builtins.str] = ...,
        family_id: Optional[_builtins.str] = ...,
        only_read_latest: Optional[_builtins.bool] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        Sequence[
            outputs.TableExternalDataConfigurationBigtableOptionsColumnFamilyColumn
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="familyId")
    def family_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="onlyReadLatest")
    def only_read_latest(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableExternalDataConfigurationBigtableOptionsColumnFamilyColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encoding: Optional[_builtins.str] = ...,
        field_name: Optional[_builtins.str] = ...,
        only_read_latest: Optional[_builtins.bool] = ...,
        qualifier_encoded: Optional[_builtins.str] = ...,
        qualifier_string: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="onlyReadLatest")
    def only_read_latest(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="qualifierEncoded")
    def qualifier_encoded(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="qualifierString")
    def qualifier_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableExternalDataConfigurationCsvOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        quote: _builtins.str,
        allow_jagged_rows: Optional[_builtins.bool] = ...,
        allow_quoted_newlines: Optional[_builtins.bool] = ...,
        encoding: Optional[_builtins.str] = ...,
        field_delimiter: Optional[_builtins.str] = ...,
        skip_leading_rows: Optional[_builtins.int] = ...,
        source_column_match: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def quote(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowJaggedRows")
    def allow_jagged_rows(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowQuotedNewlines")
    def allow_quoted_newlines(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipLeadingRows")
    def skip_leading_rows(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sourceColumnMatch")
    def source_column_match(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableExternalDataConfigurationGoogleSheetsOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        range: Optional[_builtins.str] = ...,
        skip_leading_rows: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def range(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipLeadingRows")
    def skip_leading_rows(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TableExternalDataConfigurationHivePartitioningOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mode: Optional[_builtins.str] = ...,
        require_partition_filter: Optional[_builtins.bool] = ...,
        source_uri_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requirePartitionFilter")
    def require_partition_filter(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sourceUriPrefix")
    def source_uri_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableExternalDataConfigurationJsonOptions(dict):
    def __init__(__self__, *, encoding: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableExternalDataConfigurationParquetOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_list_inference: Optional[_builtins.bool] = ...,
        enum_as_string: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableListInference")
    def enable_list_inference(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enumAsString")
    def enum_as_string(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class TableMaterializedView(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        query: _builtins.str,
        allow_non_incremental_definition: Optional[_builtins.bool] = ...,
        enable_refresh: Optional[_builtins.bool] = ...,
        refresh_interval_ms: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowNonIncrementalDefinition")
    def allow_non_incremental_definition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableRefresh")
    def enable_refresh(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="refreshIntervalMs")
    def refresh_interval_ms(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TableRangePartitioning(dict):
    def __init__(
        __self__, *, field: _builtins.str, range: outputs.TableRangePartitioningRange
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def range(self) -> outputs.TableRangePartitioningRange: ...

@pulumi.output_type
class TableRangePartitioningRange(dict):
    def __init__(
        __self__, *, end: _builtins.int, interval: _builtins.int, start: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class TableSchemaForeignTypeInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, type_system: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeSystem")
    def type_system(self) -> _builtins.str: ...

@pulumi.output_type
class TableTableConstraints(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        foreign_keys: Optional[Sequence[outputs.TableTableConstraintsForeignKey]] = ...,
        primary_key: Optional[outputs.TableTableConstraintsPrimaryKey] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="foreignKeys")
    def foreign_keys(
        self,
    ) -> Optional[Sequence[outputs.TableTableConstraintsForeignKey]]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[outputs.TableTableConstraintsPrimaryKey]: ...

@pulumi.output_type
class TableTableConstraintsForeignKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column_references: outputs.TableTableConstraintsForeignKeyColumnReferences,
        referenced_table: outputs.TableTableConstraintsForeignKeyReferencedTable,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnReferences")
    def column_references(
        self,
    ) -> outputs.TableTableConstraintsForeignKeyColumnReferences: ...
    @_builtins.property
    @pulumi.getter(name="referencedTable")
    def referenced_table(
        self,
    ) -> outputs.TableTableConstraintsForeignKeyReferencedTable: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableTableConstraintsForeignKeyColumnReferences(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, referenced_column: _builtins.str, referencing_column: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="referencedColumn")
    def referenced_column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="referencingColumn")
    def referencing_column(self) -> _builtins.str: ...

@pulumi.output_type
class TableTableConstraintsForeignKeyReferencedTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset_id: _builtins.str,
        project_id: _builtins.str,
        table_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str: ...

@pulumi.output_type
class TableTableConstraintsPrimaryKey(dict):
    def __init__(__self__, *, columns: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class TableTableReplicationInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_dataset_id: _builtins.str,
        source_project_id: _builtins.str,
        source_table_id: _builtins.str,
        replication_interval_ms: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceDatasetId")
    def source_dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceProjectId")
    def source_project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceTableId")
    def source_table_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicationIntervalMs")
    def replication_interval_ms(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TableTimePartitioning(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        expiration_ms: Optional[_builtins.int] = ...,
        field: Optional[_builtins.str] = ...,
        require_partition_filter: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expirationMs")
    def expiration_ms(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requirePartitionFilter")
    @_utilities.deprecated(...)
    def require_partition_filter(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class TableView(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        query: _builtins.str,
        use_legacy_sql: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="useLegacySql")
    def use_legacy_sql(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GetDatasetAccessResult(dict):
    def __init__(
        __self__,
        *,
        conditions: Sequence[outputs.GetDatasetAccessConditionResult],
        datasets: Sequence[outputs.GetDatasetAccessDatasetResult],
        domain: _builtins.str,
        group_by_email: _builtins.str,
        iam_member: _builtins.str,
        role: _builtins.str,
        routines: Sequence[outputs.GetDatasetAccessRoutineResult],
        special_group: _builtins.str,
        user_by_email: _builtins.str,
        views: Sequence[outputs.GetDatasetAccessViewResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Sequence[outputs.GetDatasetAccessConditionResult]: ...
    @_builtins.property
    @pulumi.getter
    def datasets(self) -> Sequence[outputs.GetDatasetAccessDatasetResult]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groupByEmail")
    def group_by_email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="iamMember")
    def iam_member(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def routines(self) -> Sequence[outputs.GetDatasetAccessRoutineResult]: ...
    @_builtins.property
    @pulumi.getter(name="specialGroup")
    def special_group(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userByEmail")
    def user_by_email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def views(self) -> Sequence[outputs.GetDatasetAccessViewResult]: ...

@pulumi.output_type
class GetDatasetAccessConditionResult(dict):
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        expression: _builtins.str,
        location: _builtins.str,
        title: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...

@pulumi.output_type
class GetDatasetAccessDatasetResult(dict):
    def __init__(
        __self__,
        *,
        datasets: Sequence[outputs.GetDatasetAccessDatasetDatasetResult],
        target_types: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def datasets(self) -> Sequence[outputs.GetDatasetAccessDatasetDatasetResult]: ...
    @_builtins.property
    @pulumi.getter(name="targetTypes")
    def target_types(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetDatasetAccessDatasetDatasetResult(dict):
    def __init__(
        __self__, *, dataset_id: _builtins.str, project_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetDatasetAccessRoutineResult(dict):
    def __init__(
        __self__,
        *,
        dataset_id: _builtins.str,
        project_id: _builtins.str,
        routine_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routineId")
    def routine_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetDatasetAccessViewResult(dict):
    def __init__(
        __self__,
        *,
        dataset_id: _builtins.str,
        project_id: _builtins.str,
        table_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetDatasetDefaultEncryptionConfigurationResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetDatasetExternalCatalogDatasetOptionResult(dict):
    def __init__(
        __self__,
        *,
        default_storage_location_uri: _builtins.str,
        parameters: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultStorageLocationUri")
    def default_storage_location_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetDatasetExternalDatasetReferenceResult(dict):
    def __init__(
        __self__, *, connection: _builtins.str, external_source: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connection(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="externalSource")
    def external_source(self) -> _builtins.str: ...

@pulumi.output_type
class GetDatasetsDatasetResult(dict):
    def __init__(
        __self__,
        *,
        dataset_id: _builtins.str,
        friendly_name: _builtins.str,
        labels: Mapping[str, _builtins.str],
        location: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableBiglakeConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        connection_id: _builtins.str,
        file_format: _builtins.str,
        storage_uri: _builtins.str,
        table_format: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileFormat")
    def file_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageUri")
    def storage_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableFormat")
    def table_format(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableEncryptionConfigurationResult(dict):
    def __init__(
        __self__, *, kms_key_name: _builtins.str, kms_key_version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersion")
    def kms_key_version(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableExternalCatalogTableOptionResult(dict):
    def __init__(
        __self__,
        *,
        connection_id: _builtins.str,
        parameters: Mapping[str, _builtins.str],
        storage_descriptors: Sequence[
            outputs.GetTableExternalCatalogTableOptionStorageDescriptorResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageDescriptors")
    def storage_descriptors(
        self,
    ) -> Sequence[
        outputs.GetTableExternalCatalogTableOptionStorageDescriptorResult
    ]: ...

@pulumi.output_type
class GetTableExternalCatalogTableOptionStorageDescriptorResult(dict):
    def __init__(
        __self__,
        *,
        input_format: _builtins.str,
        location_uri: _builtins.str,
        output_format: _builtins.str,
        serde_infos: Sequence[
            outputs.GetTableExternalCatalogTableOptionStorageDescriptorSerdeInfoResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serdeInfos")
    def serde_infos(
        self,
    ) -> Sequence[
        outputs.GetTableExternalCatalogTableOptionStorageDescriptorSerdeInfoResult
    ]: ...

@pulumi.output_type
class GetTableExternalCatalogTableOptionStorageDescriptorSerdeInfoResult(dict):
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
class GetTableExternalDataConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        autodetect: _builtins.bool,
        avro_options: Sequence[
            outputs.GetTableExternalDataConfigurationAvroOptionResult
        ],
        bigtable_options: Sequence[
            outputs.GetTableExternalDataConfigurationBigtableOptionResult
        ],
        compression: _builtins.str,
        connection_id: _builtins.str,
        csv_options: Sequence[outputs.GetTableExternalDataConfigurationCsvOptionResult],
        decimal_target_types: Sequence[_builtins.str],
        file_set_spec_type: _builtins.str,
        google_sheets_options: Sequence[
            outputs.GetTableExternalDataConfigurationGoogleSheetsOptionResult
        ],
        hive_partitioning_options: Sequence[
            outputs.GetTableExternalDataConfigurationHivePartitioningOptionResult
        ],
        ignore_unknown_values: _builtins.bool,
        json_extension: _builtins.str,
        json_options: Sequence[
            outputs.GetTableExternalDataConfigurationJsonOptionResult
        ],
        max_bad_records: _builtins.int,
        metadata_cache_mode: _builtins.str,
        object_metadata: _builtins.str,
        parquet_options: Sequence[
            outputs.GetTableExternalDataConfigurationParquetOptionResult
        ],
        reference_file_schema_uri: _builtins.str,
        schema: _builtins.str,
        source_format: _builtins.str,
        source_uris: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def autodetect(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="avroOptions")
    def avro_options(
        self,
    ) -> Sequence[outputs.GetTableExternalDataConfigurationAvroOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="bigtableOptions")
    def bigtable_options(
        self,
    ) -> Sequence[outputs.GetTableExternalDataConfigurationBigtableOptionResult]: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="csvOptions")
    def csv_options(
        self,
    ) -> Sequence[outputs.GetTableExternalDataConfigurationCsvOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="decimalTargetTypes")
    def decimal_target_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileSetSpecType")
    def file_set_spec_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="googleSheetsOptions")
    def google_sheets_options(
        self,
    ) -> Sequence[
        outputs.GetTableExternalDataConfigurationGoogleSheetsOptionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hivePartitioningOptions")
    def hive_partitioning_options(
        self,
    ) -> Sequence[
        outputs.GetTableExternalDataConfigurationHivePartitioningOptionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownValues")
    def ignore_unknown_values(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="jsonExtension")
    def json_extension(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jsonOptions")
    def json_options(
        self,
    ) -> Sequence[outputs.GetTableExternalDataConfigurationJsonOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="maxBadRecords")
    def max_bad_records(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="metadataCacheMode")
    def metadata_cache_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectMetadata")
    def object_metadata(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parquetOptions")
    def parquet_options(
        self,
    ) -> Sequence[outputs.GetTableExternalDataConfigurationParquetOptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="referenceFileSchemaUri")
    def reference_file_schema_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceFormat")
    def source_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceUris")
    def source_uris(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetTableExternalDataConfigurationAvroOptionResult(dict):
    def __init__(__self__, *, use_avro_logical_types: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="useAvroLogicalTypes")
    def use_avro_logical_types(self) -> _builtins.bool: ...

@pulumi.output_type
class GetTableExternalDataConfigurationBigtableOptionResult(dict):
    def __init__(
        __self__,
        *,
        column_families: Sequence[
            outputs.GetTableExternalDataConfigurationBigtableOptionColumnFamilyResult
        ],
        ignore_unspecified_column_families: _builtins.bool,
        output_column_families_as_json: _builtins.bool,
        read_rowkey_as_string: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnFamilies")
    def column_families(
        self,
    ) -> Sequence[
        outputs.GetTableExternalDataConfigurationBigtableOptionColumnFamilyResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreUnspecifiedColumnFamilies")
    def ignore_unspecified_column_families(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="outputColumnFamiliesAsJson")
    def output_column_families_as_json(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="readRowkeyAsString")
    def read_rowkey_as_string(self) -> _builtins.bool: ...

@pulumi.output_type
class GetTableExternalDataConfigurationBigtableOptionColumnFamilyResult(dict):
    def __init__(
        __self__,
        *,
        columns: Sequence[
            outputs.GetTableExternalDataConfigurationBigtableOptionColumnFamilyColumnResult
        ],
        encoding: _builtins.str,
        family_id: _builtins.str,
        only_read_latest: _builtins.bool,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Sequence[
        outputs.GetTableExternalDataConfigurationBigtableOptionColumnFamilyColumnResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="familyId")
    def family_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onlyReadLatest")
    def only_read_latest(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableExternalDataConfigurationBigtableOptionColumnFamilyColumnResult(dict):
    def __init__(
        __self__,
        *,
        encoding: _builtins.str,
        field_name: _builtins.str,
        only_read_latest: _builtins.bool,
        qualifier_encoded: _builtins.str,
        qualifier_string: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onlyReadLatest")
    def only_read_latest(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="qualifierEncoded")
    def qualifier_encoded(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="qualifierString")
    def qualifier_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableExternalDataConfigurationCsvOptionResult(dict):
    def __init__(
        __self__,
        *,
        allow_jagged_rows: _builtins.bool,
        allow_quoted_newlines: _builtins.bool,
        encoding: _builtins.str,
        field_delimiter: _builtins.str,
        quote: _builtins.str,
        skip_leading_rows: _builtins.int,
        source_column_match: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowJaggedRows")
    def allow_jagged_rows(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="allowQuotedNewlines")
    def allow_quoted_newlines(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def quote(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="skipLeadingRows")
    def skip_leading_rows(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sourceColumnMatch")
    def source_column_match(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableExternalDataConfigurationGoogleSheetsOptionResult(dict):
    def __init__(
        __self__, *, range: _builtins.str, skip_leading_rows: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="skipLeadingRows")
    def skip_leading_rows(self) -> _builtins.int: ...

@pulumi.output_type
class GetTableExternalDataConfigurationHivePartitioningOptionResult(dict):
    def __init__(
        __self__,
        *,
        mode: _builtins.str,
        require_partition_filter: _builtins.bool,
        source_uri_prefix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requirePartitionFilter")
    def require_partition_filter(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="sourceUriPrefix")
    def source_uri_prefix(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableExternalDataConfigurationJsonOptionResult(dict):
    def __init__(__self__, *, encoding: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableExternalDataConfigurationParquetOptionResult(dict):
    def __init__(
        __self__,
        *,
        enable_list_inference: _builtins.bool,
        enum_as_string: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableListInference")
    def enable_list_inference(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enumAsString")
    def enum_as_string(self) -> _builtins.bool: ...

@pulumi.output_type
class GetTableMaterializedViewResult(dict):
    def __init__(
        __self__,
        *,
        allow_non_incremental_definition: _builtins.bool,
        enable_refresh: _builtins.bool,
        query: _builtins.str,
        refresh_interval_ms: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowNonIncrementalDefinition")
    def allow_non_incremental_definition(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableRefresh")
    def enable_refresh(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="refreshIntervalMs")
    def refresh_interval_ms(self) -> _builtins.int: ...

@pulumi.output_type
class GetTableRangePartitioningResult(dict):
    def __init__(
        __self__,
        *,
        field: _builtins.str,
        ranges: Sequence[outputs.GetTableRangePartitioningRangeResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ranges(self) -> Sequence[outputs.GetTableRangePartitioningRangeResult]: ...

@pulumi.output_type
class GetTableRangePartitioningRangeResult(dict):
    def __init__(
        __self__, *, end: _builtins.int, interval: _builtins.int, start: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class GetTableSchemaForeignTypeInfoResult(dict):
    def __init__(__self__, *, type_system: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeSystem")
    def type_system(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableTableConstraintResult(dict):
    def __init__(
        __self__,
        *,
        foreign_keys: Sequence[outputs.GetTableTableConstraintForeignKeyResult],
        primary_keys: Sequence[outputs.GetTableTableConstraintPrimaryKeyResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="foreignKeys")
    def foreign_keys(
        self,
    ) -> Sequence[outputs.GetTableTableConstraintForeignKeyResult]: ...
    @_builtins.property
    @pulumi.getter(name="primaryKeys")
    def primary_keys(
        self,
    ) -> Sequence[outputs.GetTableTableConstraintPrimaryKeyResult]: ...

@pulumi.output_type
class GetTableTableConstraintForeignKeyResult(dict):
    def __init__(
        __self__,
        *,
        column_references: Sequence[
            outputs.GetTableTableConstraintForeignKeyColumnReferenceResult
        ],
        name: _builtins.str,
        referenced_tables: Sequence[
            outputs.GetTableTableConstraintForeignKeyReferencedTableResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnReferences")
    def column_references(
        self,
    ) -> Sequence[outputs.GetTableTableConstraintForeignKeyColumnReferenceResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="referencedTables")
    def referenced_tables(
        self,
    ) -> Sequence[outputs.GetTableTableConstraintForeignKeyReferencedTableResult]: ...

@pulumi.output_type
class GetTableTableConstraintForeignKeyColumnReferenceResult(dict):
    def __init__(
        __self__, *, referenced_column: _builtins.str, referencing_column: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="referencedColumn")
    def referenced_column(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="referencingColumn")
    def referencing_column(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableTableConstraintForeignKeyReferencedTableResult(dict):
    def __init__(
        __self__,
        *,
        dataset_id: _builtins.str,
        project_id: _builtins.str,
        table_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableTableConstraintPrimaryKeyResult(dict):
    def __init__(__self__, *, columns: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetTableTableReplicationInfoResult(dict):
    def __init__(
        __self__,
        *,
        replication_interval_ms: _builtins.int,
        source_dataset_id: _builtins.str,
        source_project_id: _builtins.str,
        source_table_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replicationIntervalMs")
    def replication_interval_ms(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sourceDatasetId")
    def source_dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceProjectId")
    def source_project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceTableId")
    def source_table_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableTimePartitioningResult(dict):
    def __init__(
        __self__,
        *,
        expiration_ms: _builtins.int,
        field: _builtins.str,
        require_partition_filter: _builtins.bool,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expirationMs")
    def expiration_ms(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requirePartitionFilter")
    def require_partition_filter(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetTableViewResult(dict):
    def __init__(
        __self__, *, query: _builtins.str, use_legacy_sql: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="useLegacySql")
    def use_legacy_sql(self) -> _builtins.bool: ...

@pulumi.output_type
class GetTablesTableResult(dict):
    def __init__(
        __self__, *, labels: Mapping[str, _builtins.str], table_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str: ...
