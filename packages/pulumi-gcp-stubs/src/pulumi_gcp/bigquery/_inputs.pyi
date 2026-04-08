import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppProfileDataBoostIsolationReadOnlyArgs",
    "AppProfileDataBoostIsolationReadOnlyArgsDict",
    "AppProfileSingleClusterRoutingArgs",
    "AppProfileSingleClusterRoutingArgsDict",
    "AppProfileStandardIsolationArgs",
    "AppProfileStandardIsolationArgsDict",
    "BiReservationPreferredTableArgs",
    "BiReservationPreferredTableArgsDict",
    "ConnectionAwsArgs",
    "ConnectionAwsArgsDict",
    "ConnectionAwsAccessRoleArgs",
    "ConnectionAwsAccessRoleArgsDict",
    "ConnectionAzureArgs",
    "ConnectionAzureArgsDict",
    "ConnectionCloudResourceArgs",
    "ConnectionCloudResourceArgsDict",
    "ConnectionCloudSpannerArgs",
    "ConnectionCloudSpannerArgsDict",
    "ConnectionCloudSqlArgs",
    "ConnectionCloudSqlArgsDict",
    "ConnectionCloudSqlCredentialArgs",
    "ConnectionCloudSqlCredentialArgsDict",
    "ConnectionIamBindingConditionArgs",
    "ConnectionIamBindingConditionArgsDict",
    "ConnectionIamMemberConditionArgs",
    "ConnectionIamMemberConditionArgsDict",
    "ConnectionSparkArgs",
    "ConnectionSparkArgsDict",
    "ConnectionSparkMetastoreServiceConfigArgs",
    "ConnectionSparkMetastoreServiceConfigArgsDict",
    "ConnectionSparkSparkHistoryServerConfigArgs",
    "ConnectionSparkSparkHistoryServerConfigArgsDict",
    "DataTransferConfigEmailPreferencesArgs",
    "DataTransferConfigEmailPreferencesArgsDict",
    "DataTransferConfigEncryptionConfigurationArgs",
    "DataTransferConfigEncryptionConfigurationArgsDict",
    "DataTransferConfigScheduleOptionsArgs",
    "DataTransferConfigScheduleOptionsArgsDict",
    "DataTransferConfigSensitiveParamsArgs",
    "DataTransferConfigSensitiveParamsArgsDict",
    "Datapolicyv2DataPolicyDataMaskingPolicyArgs",
    "Datapolicyv2DataPolicyDataMaskingPolicyArgsDict",
    "Datapolicyv2DataPolicyIamBindingConditionArgs",
    "Datapolicyv2DataPolicyIamBindingConditionArgsDict",
    "Datapolicyv2DataPolicyIamMemberConditionArgs",
    "Datapolicyv2DataPolicyIamMemberConditionArgsDict",
    "DatasetAccessArgs",
    "DatasetAccessArgsDict",
    "DatasetAccessAuthorizedDatasetArgs",
    "DatasetAccessAuthorizedDatasetArgsDict",
    "DatasetAccessAuthorizedDatasetDatasetArgs",
    "DatasetAccessAuthorizedDatasetDatasetArgsDict",
    "DatasetAccessConditionArgs",
    "DatasetAccessConditionArgsDict",
    "DatasetAccessDatasetArgs",
    "DatasetAccessDatasetArgsDict",
    "DatasetAccessDatasetDatasetArgs",
    "DatasetAccessDatasetDatasetArgsDict",
    "DatasetAccessRoutineArgs",
    "DatasetAccessRoutineArgsDict",
    "DatasetAccessViewArgs",
    "DatasetAccessViewArgsDict",
    "DatasetDefaultEncryptionConfigurationArgs",
    "DatasetDefaultEncryptionConfigurationArgsDict",
    "DatasetExternalCatalogDatasetOptionsArgs",
    "DatasetExternalCatalogDatasetOptionsArgsDict",
    "DatasetExternalDatasetReferenceArgs",
    "DatasetExternalDatasetReferenceArgsDict",
    "DatasetIamBindingConditionArgs",
    "DatasetIamBindingConditionArgsDict",
    "DatasetIamMemberConditionArgs",
    "DatasetIamMemberConditionArgsDict",
    "IamBindingConditionArgs",
    "IamBindingConditionArgsDict",
    "IamMemberConditionArgs",
    "IamMemberConditionArgsDict",
    "JobCopyArgs",
    "JobCopyArgsDict",
    "JobCopyDestinationEncryptionConfigurationArgs",
    "JobCopyDestinationEncryptionConfigurationArgsDict",
    "JobCopyDestinationTableArgs",
    "JobCopyDestinationTableArgsDict",
    "JobCopySourceTableArgs",
    "JobCopySourceTableArgsDict",
    "JobExtractArgs",
    "JobExtractArgsDict",
    "JobExtractSourceModelArgs",
    "JobExtractSourceModelArgsDict",
    "JobExtractSourceTableArgs",
    "JobExtractSourceTableArgsDict",
    "JobLoadArgs",
    "JobLoadArgsDict",
    "JobLoadDestinationEncryptionConfigurationArgs",
    "JobLoadDestinationEncryptionConfigurationArgsDict",
    "JobLoadDestinationTableArgs",
    "JobLoadDestinationTableArgsDict",
    "JobLoadParquetOptionsArgs",
    "JobLoadParquetOptionsArgsDict",
    "JobLoadTimePartitioningArgs",
    "JobLoadTimePartitioningArgsDict",
    "JobQueryArgs",
    "JobQueryArgsDict",
    "JobQueryConnectionPropertyArgs",
    "JobQueryConnectionPropertyArgsDict",
    "JobQueryDefaultDatasetArgs",
    "JobQueryDefaultDatasetArgsDict",
    "JobQueryDestinationEncryptionConfigurationArgs",
    "JobQueryDestinationEncryptionConfigurationArgsDict",
    "JobQueryDestinationTableArgs",
    "JobQueryDestinationTableArgsDict",
    "JobQueryScriptOptionsArgs",
    "JobQueryScriptOptionsArgsDict",
    "JobQueryUserDefinedFunctionResourceArgs",
    "JobQueryUserDefinedFunctionResourceArgsDict",
    "JobStatusArgs",
    "JobStatusArgsDict",
    "JobStatusErrorArgs",
    "JobStatusErrorArgsDict",
    "JobStatusErrorResultArgs",
    "JobStatusErrorResultArgsDict",
    "ReservationAutoscaleArgs",
    "ReservationAutoscaleArgsDict",
    "ReservationReplicationStatusArgs",
    "ReservationReplicationStatusArgsDict",
    "ReservationReplicationStatusErrorArgs",
    "ReservationReplicationStatusErrorArgsDict",
    "RoutineArgumentArgs",
    "RoutineArgumentArgsDict",
    "RoutineExternalRuntimeOptionsArgs",
    "RoutineExternalRuntimeOptionsArgsDict",
    "RoutinePythonOptionsArgs",
    "RoutinePythonOptionsArgsDict",
    "RoutineRemoteFunctionOptionsArgs",
    "RoutineRemoteFunctionOptionsArgsDict",
    "RoutineSparkOptionsArgs",
    "RoutineSparkOptionsArgsDict",
    "TableBiglakeConfigurationArgs",
    "TableBiglakeConfigurationArgsDict",
    "TableEncryptionConfigurationArgs",
    "TableEncryptionConfigurationArgsDict",
    "TableExternalCatalogTableOptionsArgs",
    "TableExternalCatalogTableOptionsArgsDict",
    ...,
    ...,
    ...,
    ...,
    "TableExternalDataConfigurationArgs",
    "TableExternalDataConfigurationArgsDict",
    "TableExternalDataConfigurationAvroOptionsArgs",
    "TableExternalDataConfigurationAvroOptionsArgsDict",
    "TableExternalDataConfigurationBigtableOptionsArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "TableExternalDataConfigurationCsvOptionsArgs",
    "TableExternalDataConfigurationCsvOptionsArgsDict",
    ...,
    ...,
    ...,
    ...,
    "TableExternalDataConfigurationJsonOptionsArgs",
    "TableExternalDataConfigurationJsonOptionsArgsDict",
    "TableExternalDataConfigurationParquetOptionsArgs",
    ...,
    "TableMaterializedViewArgs",
    "TableMaterializedViewArgsDict",
    "TableRangePartitioningArgs",
    "TableRangePartitioningArgsDict",
    "TableRangePartitioningRangeArgs",
    "TableRangePartitioningRangeArgsDict",
    "TableSchemaForeignTypeInfoArgs",
    "TableSchemaForeignTypeInfoArgsDict",
    "TableTableConstraintsArgs",
    "TableTableConstraintsArgsDict",
    "TableTableConstraintsForeignKeyArgs",
    "TableTableConstraintsForeignKeyArgsDict",
    ...,
    ...,
    "TableTableConstraintsForeignKeyReferencedTableArgs",
    ...,
    "TableTableConstraintsPrimaryKeyArgs",
    "TableTableConstraintsPrimaryKeyArgsDict",
    "TableTableReplicationInfoArgs",
    "TableTableReplicationInfoArgsDict",
    "TableTimePartitioningArgs",
    "TableTimePartitioningArgsDict",
    "TableViewArgs",
    "TableViewArgsDict",
]

class AppProfileDataBoostIsolationReadOnlyArgsDict(TypedDict):
    compute_billing_owner: pulumi.Input[_builtins.str]

@pulumi.input_type
class AppProfileDataBoostIsolationReadOnlyArgs:
    def __init__(
        __self__, *, compute_billing_owner: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeBillingOwner")
    def compute_billing_owner(self) -> pulumi.Input[_builtins.str]: ...
    @compute_billing_owner.setter
    def compute_billing_owner(self, value: pulumi.Input[_builtins.str]): ...

class AppProfileSingleClusterRoutingArgsDict(TypedDict):
    cluster_id: pulumi.Input[_builtins.str]
    allow_transactional_writes: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AppProfileSingleClusterRoutingArgs:
    def __init__(
        __self__,
        *,
        cluster_id: pulumi.Input[_builtins.str],
        allow_transactional_writes: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowTransactionalWrites")
    def allow_transactional_writes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_transactional_writes.setter
    def allow_transactional_writes(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AppProfileStandardIsolationArgsDict(TypedDict):
    priority: pulumi.Input[_builtins.str]

@pulumi.input_type
class AppProfileStandardIsolationArgs:
    def __init__(__self__, *, priority: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.str]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.str]): ...

class BiReservationPreferredTableArgsDict(TypedDict):
    dataset_id: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    table_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BiReservationPreferredTableArgs:
    def __init__(
        __self__,
        *,
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        table_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_id.setter
    def table_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionAwsArgsDict(TypedDict):
    access_role: pulumi.Input[ConnectionAwsAccessRoleArgsDict]

@pulumi.input_type
class ConnectionAwsArgs:
    def __init__(
        __self__, *, access_role: pulumi.Input[ConnectionAwsAccessRoleArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessRole")
    def access_role(self) -> pulumi.Input[ConnectionAwsAccessRoleArgs]: ...
    @access_role.setter
    def access_role(self, value: pulumi.Input[ConnectionAwsAccessRoleArgs]): ...

class ConnectionAwsAccessRoleArgsDict(TypedDict):
    iam_role_id: pulumi.Input[_builtins.str]
    identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionAwsAccessRoleArgs:
    def __init__(
        __self__,
        *,
        iam_role_id: pulumi.Input[_builtins.str],
        identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamRoleId")
    def iam_role_id(self) -> pulumi.Input[_builtins.str]: ...
    @iam_role_id.setter
    def iam_role_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionAzureArgsDict(TypedDict):
    customer_tenant_id: pulumi.Input[_builtins.str]
    application: NotRequired[pulumi.Input[_builtins.str]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    federated_application_client_id: NotRequired[pulumi.Input[_builtins.str]]
    identity: NotRequired[pulumi.Input[_builtins.str]]
    object_id: NotRequired[pulumi.Input[_builtins.str]]
    redirect_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionAzureArgs:
    def __init__(
        __self__,
        *,
        customer_tenant_id: pulumi.Input[_builtins.str],
        application: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        federated_application_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[_builtins.str]] = ...,
        object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        redirect_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerTenantId")
    def customer_tenant_id(self) -> pulumi.Input[_builtins.str]: ...
    @customer_tenant_id.setter
    def customer_tenant_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def application(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application.setter
    def application(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="federatedApplicationClientId")
    def federated_application_client_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @federated_application_client_id.setter
    def federated_application_client_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redirect_uri.setter
    def redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionCloudResourceArgsDict(TypedDict):
    service_account_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionCloudResourceArgs:
    def __init__(
        __self__, *, service_account_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionCloudSpannerArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    database_role: NotRequired[pulumi.Input[_builtins.str]]
    max_parallelism: NotRequired[pulumi.Input[_builtins.int]]
    use_data_boost: NotRequired[pulumi.Input[_builtins.bool]]
    use_parallelism: NotRequired[pulumi.Input[_builtins.bool]]
    use_serverless_analytics: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ConnectionCloudSpannerArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        database_role: Optional[pulumi.Input[_builtins.str]] = ...,
        max_parallelism: Optional[pulumi.Input[_builtins.int]] = ...,
        use_data_boost: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_parallelism: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_serverless_analytics: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseRole")
    def database_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_role.setter
    def database_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxParallelism")
    def max_parallelism(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_parallelism.setter
    def max_parallelism(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="useDataBoost")
    def use_data_boost(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_data_boost.setter
    def use_data_boost(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useParallelism")
    def use_parallelism(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_parallelism.setter
    def use_parallelism(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useServerlessAnalytics")
    @_utilities.deprecated(...)
    def use_serverless_analytics(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_serverless_analytics.setter
    def use_serverless_analytics(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ConnectionCloudSqlArgsDict(TypedDict):
    credential: pulumi.Input[ConnectionCloudSqlCredentialArgsDict]
    database: pulumi.Input[_builtins.str]
    instance_id: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    service_account_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionCloudSqlArgs:
    def __init__(
        __self__,
        *,
        credential: pulumi.Input[ConnectionCloudSqlCredentialArgs],
        database: pulumi.Input[_builtins.str],
        instance_id: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        service_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credential(self) -> pulumi.Input[ConnectionCloudSqlCredentialArgs]: ...
    @credential.setter
    def credential(self, value: pulumi.Input[ConnectionCloudSqlCredentialArgs]): ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[_builtins.str]: ...
    @instance_id.setter
    def instance_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionCloudSqlCredentialArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionCloudSqlCredentialArgs:
    def __init__(
        __self__,
        *,
        password: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]: ...
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionSparkArgsDict(TypedDict):
    metastore_service_config: NotRequired[
        pulumi.Input[ConnectionSparkMetastoreServiceConfigArgsDict]
    ]
    service_account_id: NotRequired[pulumi.Input[_builtins.str]]
    spark_history_server_config: NotRequired[
        pulumi.Input[ConnectionSparkSparkHistoryServerConfigArgsDict]
    ]

@pulumi.input_type
class ConnectionSparkArgs:
    def __init__(
        __self__,
        *,
        metastore_service_config: Optional[
            pulumi.Input[ConnectionSparkMetastoreServiceConfigArgs]
        ] = ...,
        service_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        spark_history_server_config: Optional[
            pulumi.Input[ConnectionSparkSparkHistoryServerConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metastoreServiceConfig")
    def metastore_service_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionSparkMetastoreServiceConfigArgs]]: ...
    @metastore_service_config.setter
    def metastore_service_config(
        self, value: Optional[pulumi.Input[ConnectionSparkMetastoreServiceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sparkHistoryServerConfig")
    def spark_history_server_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionSparkSparkHistoryServerConfigArgs]]: ...
    @spark_history_server_config.setter
    def spark_history_server_config(
        self, value: Optional[pulumi.Input[ConnectionSparkSparkHistoryServerConfigArgs]]
    ): ...

class ConnectionSparkMetastoreServiceConfigArgsDict(TypedDict):
    metastore_service: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionSparkMetastoreServiceConfigArgs:
    def __init__(
        __self__, *, metastore_service: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metastoreService")
    def metastore_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metastore_service.setter
    def metastore_service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionSparkSparkHistoryServerConfigArgsDict(TypedDict):
    dataproc_cluster: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionSparkSparkHistoryServerConfigArgs:
    def __init__(
        __self__, *, dataproc_cluster: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataprocCluster")
    def dataproc_cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataproc_cluster.setter
    def dataproc_cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataTransferConfigEmailPreferencesArgsDict(TypedDict):
    enable_failure_email: pulumi.Input[_builtins.bool]

@pulumi.input_type
class DataTransferConfigEmailPreferencesArgs:
    def __init__(
        __self__, *, enable_failure_email: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableFailureEmail")
    def enable_failure_email(self) -> pulumi.Input[_builtins.bool]: ...
    @enable_failure_email.setter
    def enable_failure_email(self, value: pulumi.Input[_builtins.bool]): ...

class DataTransferConfigEncryptionConfigurationArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class DataTransferConfigEncryptionConfigurationArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...

class DataTransferConfigScheduleOptionsArgsDict(TypedDict):
    disable_auto_scheduling: NotRequired[pulumi.Input[_builtins.bool]]
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataTransferConfigScheduleOptionsArgs:
    def __init__(
        __self__,
        *,
        disable_auto_scheduling: Optional[pulumi.Input[_builtins.bool]] = ...,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableAutoScheduling")
    def disable_auto_scheduling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_auto_scheduling.setter
    def disable_auto_scheduling(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataTransferConfigSensitiveParamsArgsDict(TypedDict):
    secret_access_key: NotRequired[pulumi.Input[_builtins.str]]
    secret_access_key_wo: NotRequired[pulumi.Input[_builtins.str]]
    secret_access_key_wo_version: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class DataTransferConfigSensitiveParamsArgs:
    def __init__(
        __self__,
        *,
        secret_access_key: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_access_key_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_access_key_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_access_key.setter
    def secret_access_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretAccessKeyWo")
    def secret_access_key_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_access_key_wo.setter
    def secret_access_key_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretAccessKeyWoVersion")
    def secret_access_key_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @secret_access_key_wo_version.setter
    def secret_access_key_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class Datapolicyv2DataPolicyDataMaskingPolicyArgsDict(TypedDict):
    predefined_expression: NotRequired[pulumi.Input[_builtins.str]]
    routine: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class Datapolicyv2DataPolicyDataMaskingPolicyArgs:
    def __init__(
        __self__,
        *,
        predefined_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        routine: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="predefinedExpression")
    def predefined_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @predefined_expression.setter
    def predefined_expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def routine(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routine.setter
    def routine(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class Datapolicyv2DataPolicyIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class Datapolicyv2DataPolicyIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class Datapolicyv2DataPolicyIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class Datapolicyv2DataPolicyIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatasetAccessArgsDict(TypedDict):
    condition: NotRequired[pulumi.Input[DatasetAccessConditionArgsDict]]
    dataset: NotRequired[pulumi.Input[DatasetAccessDatasetArgsDict]]
    domain: NotRequired[pulumi.Input[_builtins.str]]
    group_by_email: NotRequired[pulumi.Input[_builtins.str]]
    iam_member: NotRequired[pulumi.Input[_builtins.str]]
    role: NotRequired[pulumi.Input[_builtins.str]]
    routine: NotRequired[pulumi.Input[DatasetAccessRoutineArgsDict]]
    special_group: NotRequired[pulumi.Input[_builtins.str]]
    user_by_email: NotRequired[pulumi.Input[_builtins.str]]
    view: NotRequired[pulumi.Input[DatasetAccessViewArgsDict]]

@pulumi.input_type
class DatasetAccessArgs:
    def __init__(
        __self__,
        *,
        condition: Optional[pulumi.Input[DatasetAccessConditionArgs]] = ...,
        dataset: Optional[pulumi.Input[DatasetAccessDatasetArgs]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        group_by_email: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_member: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
        routine: Optional[pulumi.Input[DatasetAccessRoutineArgs]] = ...,
        special_group: Optional[pulumi.Input[_builtins.str]] = ...,
        user_by_email: Optional[pulumi.Input[_builtins.str]] = ...,
        view: Optional[pulumi.Input[DatasetAccessViewArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[DatasetAccessConditionArgs]]: ...
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[DatasetAccessConditionArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[DatasetAccessDatasetArgs]]: ...
    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[DatasetAccessDatasetArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupByEmail")
    def group_by_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_by_email.setter
    def group_by_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iamMember")
    def iam_member(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_member.setter
    def iam_member(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def routine(self) -> Optional[pulumi.Input[DatasetAccessRoutineArgs]]: ...
    @routine.setter
    def routine(self, value: Optional[pulumi.Input[DatasetAccessRoutineArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="specialGroup")
    def special_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @special_group.setter
    def special_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userByEmail")
    def user_by_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_by_email.setter
    def user_by_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def view(self) -> Optional[pulumi.Input[DatasetAccessViewArgs]]: ...
    @view.setter
    def view(self, value: Optional[pulumi.Input[DatasetAccessViewArgs]]): ...

class DatasetAccessAuthorizedDatasetArgsDict(TypedDict):
    dataset: pulumi.Input[DatasetAccessAuthorizedDatasetDatasetArgsDict]
    target_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class DatasetAccessAuthorizedDatasetArgs:
    def __init__(
        __self__,
        *,
        dataset: pulumi.Input[DatasetAccessAuthorizedDatasetDatasetArgs],
        target_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> pulumi.Input[DatasetAccessAuthorizedDatasetDatasetArgs]: ...
    @dataset.setter
    def dataset(
        self, value: pulumi.Input[DatasetAccessAuthorizedDatasetDatasetArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetTypes")
    def target_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @target_types.setter
    def target_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class DatasetAccessAuthorizedDatasetDatasetArgsDict(TypedDict):
    dataset_id: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class DatasetAccessAuthorizedDatasetDatasetArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...

class DatasetAccessConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatasetAccessConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatasetAccessDatasetArgsDict(TypedDict):
    dataset: pulumi.Input[DatasetAccessDatasetDatasetArgsDict]
    target_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class DatasetAccessDatasetArgs:
    def __init__(
        __self__,
        *,
        dataset: pulumi.Input[DatasetAccessDatasetDatasetArgs],
        target_types: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> pulumi.Input[DatasetAccessDatasetDatasetArgs]: ...
    @dataset.setter
    def dataset(self, value: pulumi.Input[DatasetAccessDatasetDatasetArgs]): ...
    @_builtins.property
    @pulumi.getter(name="targetTypes")
    def target_types(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @target_types.setter
    def target_types(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class DatasetAccessDatasetDatasetArgsDict(TypedDict):
    dataset_id: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class DatasetAccessDatasetDatasetArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...

class DatasetAccessRoutineArgsDict(TypedDict):
    dataset_id: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    routine_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class DatasetAccessRoutineArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
        routine_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="routineId")
    def routine_id(self) -> pulumi.Input[_builtins.str]: ...
    @routine_id.setter
    def routine_id(self, value: pulumi.Input[_builtins.str]): ...

class DatasetAccessViewArgsDict(TypedDict):
    dataset_id: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    table_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class DatasetAccessViewArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
        table_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_id.setter
    def table_id(self, value: pulumi.Input[_builtins.str]): ...

class DatasetDefaultEncryptionConfigurationArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class DatasetDefaultEncryptionConfigurationArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...

class DatasetExternalCatalogDatasetOptionsArgsDict(TypedDict):
    default_storage_location_uri: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DatasetExternalCatalogDatasetOptionsArgs:
    def __init__(
        __self__,
        *,
        default_storage_location_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultStorageLocationUri")
    def default_storage_location_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_storage_location_uri.setter
    def default_storage_location_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class DatasetExternalDatasetReferenceArgsDict(TypedDict):
    connection: pulumi.Input[_builtins.str]
    external_source: pulumi.Input[_builtins.str]

@pulumi.input_type
class DatasetExternalDatasetReferenceArgs:
    def __init__(
        __self__,
        *,
        connection: pulumi.Input[_builtins.str],
        external_source: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connection(self) -> pulumi.Input[_builtins.str]: ...
    @connection.setter
    def connection(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="externalSource")
    def external_source(self) -> pulumi.Input[_builtins.str]: ...
    @external_source.setter
    def external_source(self, value: pulumi.Input[_builtins.str]): ...

class DatasetIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatasetIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatasetIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DatasetIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobCopyArgsDict(TypedDict):
    source_tables: pulumi.Input[Sequence[pulumi.Input[JobCopySourceTableArgsDict]]]
    create_disposition: NotRequired[pulumi.Input[_builtins.str]]
    destination_encryption_configuration: NotRequired[
        pulumi.Input[JobCopyDestinationEncryptionConfigurationArgsDict]
    ]
    destination_table: NotRequired[pulumi.Input[JobCopyDestinationTableArgsDict]]
    write_disposition: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobCopyArgs:
    def __init__(
        __self__,
        *,
        source_tables: pulumi.Input[Sequence[pulumi.Input[JobCopySourceTableArgs]]],
        create_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_encryption_configuration: Optional[
            pulumi.Input[JobCopyDestinationEncryptionConfigurationArgs]
        ] = ...,
        destination_table: Optional[pulumi.Input[JobCopyDestinationTableArgs]] = ...,
        write_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceTables")
    def source_tables(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[JobCopySourceTableArgs]]]: ...
    @source_tables.setter
    def source_tables(
        self, value: pulumi.Input[Sequence[pulumi.Input[JobCopySourceTableArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createDisposition")
    def create_disposition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_disposition.setter
    def create_disposition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationEncryptionConfiguration")
    def destination_encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[JobCopyDestinationEncryptionConfigurationArgs]]: ...
    @destination_encryption_configuration.setter
    def destination_encryption_configuration(
        self,
        value: Optional[pulumi.Input[JobCopyDestinationEncryptionConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationTable")
    def destination_table(
        self,
    ) -> Optional[pulumi.Input[JobCopyDestinationTableArgs]]: ...
    @destination_table.setter
    def destination_table(
        self, value: Optional[pulumi.Input[JobCopyDestinationTableArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="writeDisposition")
    def write_disposition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @write_disposition.setter
    def write_disposition(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobCopyDestinationEncryptionConfigurationArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    kms_key_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobCopyDestinationEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: pulumi.Input[_builtins.str],
        kms_key_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersion")
    def kms_key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_version.setter
    def kms_key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobCopyDestinationTableArgsDict(TypedDict):
    table_id: pulumi.Input[_builtins.str]
    dataset_id: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobCopyDestinationTableArgs:
    def __init__(
        __self__,
        *,
        table_id: pulumi.Input[_builtins.str],
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_id.setter
    def table_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobCopySourceTableArgsDict(TypedDict):
    table_id: pulumi.Input[_builtins.str]
    dataset_id: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobCopySourceTableArgs:
    def __init__(
        __self__,
        *,
        table_id: pulumi.Input[_builtins.str],
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_id.setter
    def table_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobExtractArgsDict(TypedDict):
    destination_uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    compression: NotRequired[pulumi.Input[_builtins.str]]
    destination_format: NotRequired[pulumi.Input[_builtins.str]]
    field_delimiter: NotRequired[pulumi.Input[_builtins.str]]
    print_header: NotRequired[pulumi.Input[_builtins.bool]]
    source_model: NotRequired[pulumi.Input[JobExtractSourceModelArgsDict]]
    source_table: NotRequired[pulumi.Input[JobExtractSourceTableArgsDict]]
    use_avro_logical_types: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class JobExtractArgs:
    def __init__(
        __self__,
        *,
        destination_uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        compression: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_format: Optional[pulumi.Input[_builtins.str]] = ...,
        field_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        print_header: Optional[pulumi.Input[_builtins.bool]] = ...,
        source_model: Optional[pulumi.Input[JobExtractSourceModelArgs]] = ...,
        source_table: Optional[pulumi.Input[JobExtractSourceTableArgs]] = ...,
        use_avro_logical_types: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationUris")
    def destination_uris(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @destination_uris.setter
    def destination_uris(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression.setter
    def compression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationFormat")
    def destination_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_format.setter
    def destination_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="printHeader")
    def print_header(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @print_header.setter
    def print_header(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceModel")
    def source_model(self) -> Optional[pulumi.Input[JobExtractSourceModelArgs]]: ...
    @source_model.setter
    def source_model(
        self, value: Optional[pulumi.Input[JobExtractSourceModelArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceTable")
    def source_table(self) -> Optional[pulumi.Input[JobExtractSourceTableArgs]]: ...
    @source_table.setter
    def source_table(
        self, value: Optional[pulumi.Input[JobExtractSourceTableArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useAvroLogicalTypes")
    def use_avro_logical_types(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_avro_logical_types.setter
    def use_avro_logical_types(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class JobExtractSourceModelArgsDict(TypedDict):
    dataset_id: pulumi.Input[_builtins.str]
    model_id: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class JobExtractSourceModelArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        model_id: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> pulumi.Input[_builtins.str]: ...
    @model_id.setter
    def model_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...

class JobExtractSourceTableArgsDict(TypedDict):
    table_id: pulumi.Input[_builtins.str]
    dataset_id: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobExtractSourceTableArgs:
    def __init__(
        __self__,
        *,
        table_id: pulumi.Input[_builtins.str],
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_id.setter
    def table_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobLoadArgsDict(TypedDict):
    destination_table: pulumi.Input[JobLoadDestinationTableArgsDict]
    source_uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allow_jagged_rows: NotRequired[pulumi.Input[_builtins.bool]]
    allow_quoted_newlines: NotRequired[pulumi.Input[_builtins.bool]]
    autodetect: NotRequired[pulumi.Input[_builtins.bool]]
    create_disposition: NotRequired[pulumi.Input[_builtins.str]]
    destination_encryption_configuration: NotRequired[
        pulumi.Input[JobLoadDestinationEncryptionConfigurationArgsDict]
    ]
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    field_delimiter: NotRequired[pulumi.Input[_builtins.str]]
    ignore_unknown_values: NotRequired[pulumi.Input[_builtins.bool]]
    json_extension: NotRequired[pulumi.Input[_builtins.str]]
    max_bad_records: NotRequired[pulumi.Input[_builtins.int]]
    null_marker: NotRequired[pulumi.Input[_builtins.str]]
    parquet_options: NotRequired[pulumi.Input[JobLoadParquetOptionsArgsDict]]
    projection_fields: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    quote: NotRequired[pulumi.Input[_builtins.str]]
    schema_update_options: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    skip_leading_rows: NotRequired[pulumi.Input[_builtins.int]]
    source_format: NotRequired[pulumi.Input[_builtins.str]]
    time_partitioning: NotRequired[pulumi.Input[JobLoadTimePartitioningArgsDict]]
    write_disposition: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobLoadArgs:
    def __init__(
        __self__,
        *,
        destination_table: pulumi.Input[JobLoadDestinationTableArgs],
        source_uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        allow_jagged_rows: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_quoted_newlines: Optional[pulumi.Input[_builtins.bool]] = ...,
        autodetect: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_encryption_configuration: Optional[
            pulumi.Input[JobLoadDestinationEncryptionConfigurationArgs]
        ] = ...,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        field_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_unknown_values: Optional[pulumi.Input[_builtins.bool]] = ...,
        json_extension: Optional[pulumi.Input[_builtins.str]] = ...,
        max_bad_records: Optional[pulumi.Input[_builtins.int]] = ...,
        null_marker: Optional[pulumi.Input[_builtins.str]] = ...,
        parquet_options: Optional[pulumi.Input[JobLoadParquetOptionsArgs]] = ...,
        projection_fields: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        quote: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_update_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        skip_leading_rows: Optional[pulumi.Input[_builtins.int]] = ...,
        source_format: Optional[pulumi.Input[_builtins.str]] = ...,
        time_partitioning: Optional[pulumi.Input[JobLoadTimePartitioningArgs]] = ...,
        write_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationTable")
    def destination_table(self) -> pulumi.Input[JobLoadDestinationTableArgs]: ...
    @destination_table.setter
    def destination_table(self, value: pulumi.Input[JobLoadDestinationTableArgs]): ...
    @_builtins.property
    @pulumi.getter(name="sourceUris")
    def source_uris(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @source_uris.setter
    def source_uris(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowJaggedRows")
    def allow_jagged_rows(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_jagged_rows.setter
    def allow_jagged_rows(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowQuotedNewlines")
    def allow_quoted_newlines(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_quoted_newlines.setter
    def allow_quoted_newlines(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def autodetect(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @autodetect.setter
    def autodetect(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="createDisposition")
    def create_disposition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_disposition.setter
    def create_disposition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationEncryptionConfiguration")
    def destination_encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[JobLoadDestinationEncryptionConfigurationArgs]]: ...
    @destination_encryption_configuration.setter
    def destination_encryption_configuration(
        self,
        value: Optional[pulumi.Input[JobLoadDestinationEncryptionConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownValues")
    def ignore_unknown_values(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_unknown_values.setter
    def ignore_unknown_values(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="jsonExtension")
    def json_extension(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @json_extension.setter
    def json_extension(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBadRecords")
    def max_bad_records(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_bad_records.setter
    def max_bad_records(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nullMarker")
    def null_marker(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @null_marker.setter
    def null_marker(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parquetOptions")
    def parquet_options(self) -> Optional[pulumi.Input[JobLoadParquetOptionsArgs]]: ...
    @parquet_options.setter
    def parquet_options(
        self, value: Optional[pulumi.Input[JobLoadParquetOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="projectionFields")
    def projection_fields(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @projection_fields.setter
    def projection_fields(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def quote(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quote.setter
    def quote(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaUpdateOptions")
    def schema_update_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @schema_update_options.setter
    def schema_update_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipLeadingRows")
    def skip_leading_rows(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @skip_leading_rows.setter
    def skip_leading_rows(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFormat")
    def source_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_format.setter
    def source_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timePartitioning")
    def time_partitioning(
        self,
    ) -> Optional[pulumi.Input[JobLoadTimePartitioningArgs]]: ...
    @time_partitioning.setter
    def time_partitioning(
        self, value: Optional[pulumi.Input[JobLoadTimePartitioningArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="writeDisposition")
    def write_disposition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @write_disposition.setter
    def write_disposition(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobLoadDestinationEncryptionConfigurationArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    kms_key_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobLoadDestinationEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: pulumi.Input[_builtins.str],
        kms_key_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersion")
    def kms_key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_version.setter
    def kms_key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobLoadDestinationTableArgsDict(TypedDict):
    table_id: pulumi.Input[_builtins.str]
    dataset_id: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobLoadDestinationTableArgs:
    def __init__(
        __self__,
        *,
        table_id: pulumi.Input[_builtins.str],
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_id.setter
    def table_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobLoadParquetOptionsArgsDict(TypedDict):
    enable_list_inference: NotRequired[pulumi.Input[_builtins.bool]]
    enum_as_string: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class JobLoadParquetOptionsArgs:
    def __init__(
        __self__,
        *,
        enable_list_inference: Optional[pulumi.Input[_builtins.bool]] = ...,
        enum_as_string: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableListInference")
    def enable_list_inference(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_list_inference.setter
    def enable_list_inference(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enumAsString")
    def enum_as_string(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enum_as_string.setter
    def enum_as_string(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class JobLoadTimePartitioningArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    expiration_ms: NotRequired[pulumi.Input[_builtins.str]]
    field: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobLoadTimePartitioningArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        expiration_ms: Optional[pulumi.Input[_builtins.str]] = ...,
        field: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="expirationMs")
    def expiration_ms(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiration_ms.setter
    def expiration_ms(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobQueryArgsDict(TypedDict):
    query: pulumi.Input[_builtins.str]
    allow_large_results: NotRequired[pulumi.Input[_builtins.bool]]
    connection_properties: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[JobQueryConnectionPropertyArgsDict]]]
    ]
    continuous: NotRequired[pulumi.Input[_builtins.bool]]
    create_disposition: NotRequired[pulumi.Input[_builtins.str]]
    default_dataset: NotRequired[pulumi.Input[JobQueryDefaultDatasetArgsDict]]
    destination_encryption_configuration: NotRequired[
        pulumi.Input[JobQueryDestinationEncryptionConfigurationArgsDict]
    ]
    destination_table: NotRequired[pulumi.Input[JobQueryDestinationTableArgsDict]]
    flatten_results: NotRequired[pulumi.Input[_builtins.bool]]
    maximum_billing_tier: NotRequired[pulumi.Input[_builtins.int]]
    maximum_bytes_billed: NotRequired[pulumi.Input[_builtins.str]]
    parameter_mode: NotRequired[pulumi.Input[_builtins.str]]
    priority: NotRequired[pulumi.Input[_builtins.str]]
    schema_update_options: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    script_options: NotRequired[pulumi.Input[JobQueryScriptOptionsArgsDict]]
    use_legacy_sql: NotRequired[pulumi.Input[_builtins.bool]]
    use_query_cache: NotRequired[pulumi.Input[_builtins.bool]]
    user_defined_function_resources: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[JobQueryUserDefinedFunctionResourceArgsDict]]
        ]
    ]
    write_disposition: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobQueryArgs:
    def __init__(
        __self__,
        *,
        query: pulumi.Input[_builtins.str],
        allow_large_results: Optional[pulumi.Input[_builtins.bool]] = ...,
        connection_properties: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobQueryConnectionPropertyArgs]]]
        ] = ...,
        continuous: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
        default_dataset: Optional[pulumi.Input[JobQueryDefaultDatasetArgs]] = ...,
        destination_encryption_configuration: Optional[
            pulumi.Input[JobQueryDestinationEncryptionConfigurationArgs]
        ] = ...,
        destination_table: Optional[pulumi.Input[JobQueryDestinationTableArgs]] = ...,
        flatten_results: Optional[pulumi.Input[_builtins.bool]] = ...,
        maximum_billing_tier: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_bytes_billed: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_update_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        script_options: Optional[pulumi.Input[JobQueryScriptOptionsArgs]] = ...,
        use_legacy_sql: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_query_cache: Optional[pulumi.Input[_builtins.bool]] = ...,
        user_defined_function_resources: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[JobQueryUserDefinedFunctionResourceArgs]]
            ]
        ] = ...,
        write_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Input[_builtins.str]: ...
    @query.setter
    def query(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowLargeResults")
    def allow_large_results(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_large_results.setter
    def allow_large_results(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionProperties")
    def connection_properties(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[JobQueryConnectionPropertyArgs]]]
    ]: ...
    @connection_properties.setter
    def connection_properties(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobQueryConnectionPropertyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def continuous(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @continuous.setter
    def continuous(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="createDisposition")
    def create_disposition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_disposition.setter
    def create_disposition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultDataset")
    def default_dataset(self) -> Optional[pulumi.Input[JobQueryDefaultDatasetArgs]]: ...
    @default_dataset.setter
    def default_dataset(
        self, value: Optional[pulumi.Input[JobQueryDefaultDatasetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationEncryptionConfiguration")
    def destination_encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[JobQueryDestinationEncryptionConfigurationArgs]]: ...
    @destination_encryption_configuration.setter
    def destination_encryption_configuration(
        self,
        value: Optional[pulumi.Input[JobQueryDestinationEncryptionConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="destinationTable")
    def destination_table(
        self,
    ) -> Optional[pulumi.Input[JobQueryDestinationTableArgs]]: ...
    @destination_table.setter
    def destination_table(
        self, value: Optional[pulumi.Input[JobQueryDestinationTableArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="flattenResults")
    def flatten_results(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @flatten_results.setter
    def flatten_results(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumBillingTier")
    def maximum_billing_tier(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_billing_tier.setter
    def maximum_billing_tier(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumBytesBilled")
    def maximum_bytes_billed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maximum_bytes_billed.setter
    def maximum_bytes_billed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parameterMode")
    def parameter_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parameter_mode.setter
    def parameter_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaUpdateOptions")
    def schema_update_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @schema_update_options.setter
    def schema_update_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scriptOptions")
    def script_options(self) -> Optional[pulumi.Input[JobQueryScriptOptionsArgs]]: ...
    @script_options.setter
    def script_options(
        self, value: Optional[pulumi.Input[JobQueryScriptOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useLegacySql")
    def use_legacy_sql(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_legacy_sql.setter
    def use_legacy_sql(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useQueryCache")
    def use_query_cache(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_query_cache.setter
    def use_query_cache(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="userDefinedFunctionResources")
    def user_defined_function_resources(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[JobQueryUserDefinedFunctionResourceArgs]]]
    ]: ...
    @user_defined_function_resources.setter
    def user_defined_function_resources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[JobQueryUserDefinedFunctionResourceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="writeDisposition")
    def write_disposition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @write_disposition.setter
    def write_disposition(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobQueryConnectionPropertyArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class JobQueryConnectionPropertyArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class JobQueryDefaultDatasetArgsDict(TypedDict):
    dataset_id: pulumi.Input[_builtins.str]
    project_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobQueryDefaultDatasetArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobQueryDestinationEncryptionConfigurationArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    kms_key_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobQueryDestinationEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: pulumi.Input[_builtins.str],
        kms_key_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersion")
    def kms_key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_version.setter
    def kms_key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobQueryDestinationTableArgsDict(TypedDict):
    table_id: pulumi.Input[_builtins.str]
    dataset_id: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobQueryDestinationTableArgs:
    def __init__(
        __self__,
        *,
        table_id: pulumi.Input[_builtins.str],
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_id.setter
    def table_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobQueryScriptOptionsArgsDict(TypedDict):
    key_result_statement: NotRequired[pulumi.Input[_builtins.str]]
    statement_byte_budget: NotRequired[pulumi.Input[_builtins.str]]
    statement_timeout_ms: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobQueryScriptOptionsArgs:
    def __init__(
        __self__,
        *,
        key_result_statement: Optional[pulumi.Input[_builtins.str]] = ...,
        statement_byte_budget: Optional[pulumi.Input[_builtins.str]] = ...,
        statement_timeout_ms: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyResultStatement")
    def key_result_statement(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_result_statement.setter
    def key_result_statement(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statementByteBudget")
    def statement_byte_budget(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @statement_byte_budget.setter
    def statement_byte_budget(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statementTimeoutMs")
    def statement_timeout_ms(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @statement_timeout_ms.setter
    def statement_timeout_ms(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobQueryUserDefinedFunctionResourceArgsDict(TypedDict):
    inline_code: NotRequired[pulumi.Input[_builtins.str]]
    resource_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobQueryUserDefinedFunctionResourceArgs:
    def __init__(
        __self__,
        *,
        inline_code: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlineCode")
    def inline_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inline_code.setter
    def inline_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_uri.setter
    def resource_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobStatusArgsDict(TypedDict):
    error_results: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[JobStatusErrorResultArgsDict]]]
    ]
    errors: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobStatusErrorArgsDict]]]]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobStatusArgs:
    def __init__(
        __self__,
        *,
        error_results: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobStatusErrorResultArgs]]]
        ] = ...,
        errors: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobStatusErrorArgs]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorResults")
    def error_results(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobStatusErrorResultArgs]]]]: ...
    @error_results.setter
    def error_results(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[JobStatusErrorResultArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def errors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobStatusErrorArgs]]]]: ...
    @errors.setter
    def errors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobStatusErrorArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobStatusErrorArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobStatusErrorArgs:
    def __init__(
        __self__,
        *,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobStatusErrorResultArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobStatusErrorResultArgs:
    def __init__(
        __self__,
        *,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReservationAutoscaleArgsDict(TypedDict):
    current_slots: NotRequired[pulumi.Input[_builtins.int]]
    max_slots: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ReservationAutoscaleArgs:
    def __init__(
        __self__,
        *,
        current_slots: Optional[pulumi.Input[_builtins.int]] = ...,
        max_slots: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentSlots")
    def current_slots(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @current_slots.setter
    def current_slots(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxSlots")
    def max_slots(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_slots.setter
    def max_slots(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ReservationReplicationStatusArgsDict(TypedDict):
    errors: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ReservationReplicationStatusErrorArgsDict]]]
    ]
    last_error_time: NotRequired[pulumi.Input[_builtins.str]]
    last_replication_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReservationReplicationStatusArgs:
    def __init__(
        __self__,
        *,
        errors: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReservationReplicationStatusErrorArgs]]]
        ] = ...,
        last_error_time: Optional[pulumi.Input[_builtins.str]] = ...,
        last_replication_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def errors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReservationReplicationStatusErrorArgs]]]
    ]: ...
    @errors.setter
    def errors(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReservationReplicationStatusErrorArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastErrorTime")
    def last_error_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_error_time.setter
    def last_error_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastReplicationTime")
    def last_replication_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_replication_time.setter
    def last_replication_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReservationReplicationStatusErrorArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReservationReplicationStatusErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RoutineArgumentArgsDict(TypedDict):
    argument_kind: NotRequired[pulumi.Input[_builtins.str]]
    data_type: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RoutineArgumentArgs:
    def __init__(
        __self__,
        *,
        argument_kind: Optional[pulumi.Input[_builtins.str]] = ...,
        data_type: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="argumentKind")
    def argument_kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @argument_kind.setter
    def argument_kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_type.setter
    def data_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RoutineExternalRuntimeOptionsArgsDict(TypedDict):
    container_cpu: NotRequired[pulumi.Input[_builtins.float]]
    container_memory: NotRequired[pulumi.Input[_builtins.str]]
    max_batching_rows: NotRequired[pulumi.Input[_builtins.str]]
    runtime_connection: NotRequired[pulumi.Input[_builtins.str]]
    runtime_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RoutineExternalRuntimeOptionsArgs:
    def __init__(
        __self__,
        *,
        container_cpu: Optional[pulumi.Input[_builtins.float]] = ...,
        container_memory: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batching_rows: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_connection: Optional[pulumi.Input[_builtins.str]] = ...,
        runtime_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerCpu")
    def container_cpu(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @container_cpu.setter
    def container_cpu(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="containerMemory")
    def container_memory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_memory.setter
    def container_memory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBatchingRows")
    def max_batching_rows(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_batching_rows.setter
    def max_batching_rows(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeConnection")
    def runtime_connection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_connection.setter
    def runtime_connection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_version.setter
    def runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RoutinePythonOptionsArgsDict(TypedDict):
    entry_point: pulumi.Input[_builtins.str]
    packages: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RoutinePythonOptionsArgs:
    def __init__(
        __self__,
        *,
        entry_point: pulumi.Input[_builtins.str],
        packages: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> pulumi.Input[_builtins.str]: ...
    @entry_point.setter
    def entry_point(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def packages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @packages.setter
    def packages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RoutineRemoteFunctionOptionsArgsDict(TypedDict):
    connection: NotRequired[pulumi.Input[_builtins.str]]
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    max_batching_rows: NotRequired[pulumi.Input[_builtins.str]]
    user_defined_context: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class RoutineRemoteFunctionOptionsArgs:
    def __init__(
        __self__,
        *,
        connection: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        max_batching_rows: Optional[pulumi.Input[_builtins.str]] = ...,
        user_defined_context: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection.setter
    def connection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBatchingRows")
    def max_batching_rows(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_batching_rows.setter
    def max_batching_rows(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userDefinedContext")
    def user_defined_context(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @user_defined_context.setter
    def user_defined_context(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class RoutineSparkOptionsArgsDict(TypedDict):
    archive_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    connection: NotRequired[pulumi.Input[_builtins.str]]
    container_image: NotRequired[pulumi.Input[_builtins.str]]
    file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    jar_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    main_class: NotRequired[pulumi.Input[_builtins.str]]
    main_file_uri: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    py_file_uris: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    runtime_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RoutineSparkOptionsArgs:
    def __init__(
        __self__,
        *,
        archive_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        connection: Optional[pulumi.Input[_builtins.str]] = ...,
        container_image: Optional[pulumi.Input[_builtins.str]] = ...,
        file_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        jar_uris: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        main_class: Optional[pulumi.Input[_builtins.str]] = ...,
        main_file_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        py_file_uris: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        runtime_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="archiveUris")
    def archive_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @archive_uris.setter
    def archive_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def connection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection.setter
    def connection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_image.setter
    def container_image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileUris")
    def file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_uris.setter
    def file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jarUris")
    def jar_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @jar_uris.setter
    def jar_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_class.setter
    def main_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mainFileUri")
    def main_file_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @main_file_uri.setter
    def main_file_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pyFileUris")
    def py_file_uris(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @py_file_uris.setter
    def py_file_uris(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_version.setter
    def runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableBiglakeConfigurationArgsDict(TypedDict):
    connection_id: pulumi.Input[_builtins.str]
    file_format: pulumi.Input[_builtins.str]
    storage_uri: pulumi.Input[_builtins.str]
    table_format: pulumi.Input[_builtins.str]

@pulumi.input_type
class TableBiglakeConfigurationArgs:
    def __init__(
        __self__,
        *,
        connection_id: pulumi.Input[_builtins.str],
        file_format: pulumi.Input[_builtins.str],
        storage_uri: pulumi.Input[_builtins.str],
        table_format: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Input[_builtins.str]: ...
    @connection_id.setter
    def connection_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fileFormat")
    def file_format(self) -> pulumi.Input[_builtins.str]: ...
    @file_format.setter
    def file_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageUri")
    def storage_uri(self) -> pulumi.Input[_builtins.str]: ...
    @storage_uri.setter
    def storage_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableFormat")
    def table_format(self) -> pulumi.Input[_builtins.str]: ...
    @table_format.setter
    def table_format(self, value: pulumi.Input[_builtins.str]): ...

class TableEncryptionConfigurationArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]
    kms_key_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: pulumi.Input[_builtins.str],
        kms_key_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersion")
    def kms_key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_version.setter
    def kms_key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableExternalCatalogTableOptionsArgsDict(TypedDict):
    connection_id: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    storage_descriptor: NotRequired[
        pulumi.Input[TableExternalCatalogTableOptionsStorageDescriptorArgsDict]
    ]

@pulumi.input_type
class TableExternalCatalogTableOptionsArgs:
    def __init__(
        __self__,
        *,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        storage_descriptor: Optional[
            pulumi.Input[TableExternalCatalogTableOptionsStorageDescriptorArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageDescriptor")
    def storage_descriptor(
        self,
    ) -> Optional[
        pulumi.Input[TableExternalCatalogTableOptionsStorageDescriptorArgs]
    ]: ...
    @storage_descriptor.setter
    def storage_descriptor(
        self,
        value: Optional[
            pulumi.Input[TableExternalCatalogTableOptionsStorageDescriptorArgs]
        ],
    ): ...

class TableExternalCatalogTableOptionsStorageDescriptorArgsDict(TypedDict):
    input_format: NotRequired[pulumi.Input[_builtins.str]]
    location_uri: NotRequired[pulumi.Input[_builtins.str]]
    output_format: NotRequired[pulumi.Input[_builtins.str]]
    serde_info: NotRequired[
        pulumi.Input[TableExternalCatalogTableOptionsStorageDescriptorSerdeInfoArgsDict]
    ]

@pulumi.input_type
class TableExternalCatalogTableOptionsStorageDescriptorArgs:
    def __init__(
        __self__,
        *,
        input_format: Optional[pulumi.Input[_builtins.str]] = ...,
        location_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        output_format: Optional[pulumi.Input[_builtins.str]] = ...,
        serde_info: Optional[
            pulumi.Input[TableExternalCatalogTableOptionsStorageDescriptorSerdeInfoArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @input_format.setter
    def input_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location_uri.setter
    def location_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_format.setter
    def output_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serdeInfo")
    def serde_info(
        self,
    ) -> Optional[
        pulumi.Input[TableExternalCatalogTableOptionsStorageDescriptorSerdeInfoArgs]
    ]: ...
    @serde_info.setter
    def serde_info(
        self,
        value: Optional[
            pulumi.Input[TableExternalCatalogTableOptionsStorageDescriptorSerdeInfoArgs]
        ],
    ): ...

class TableExternalCatalogTableOptionsStorageDescriptorSerdeInfoArgsDict(TypedDict):
    serialization_library: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class TableExternalCatalogTableOptionsStorageDescriptorSerdeInfoArgs:
    def __init__(
        __self__,
        *,
        serialization_library: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serializationLibrary")
    def serialization_library(self) -> pulumi.Input[_builtins.str]: ...
    @serialization_library.setter
    def serialization_library(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class TableExternalDataConfigurationArgsDict(TypedDict):
    autodetect: pulumi.Input[_builtins.bool]
    source_uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    avro_options: NotRequired[
        pulumi.Input[TableExternalDataConfigurationAvroOptionsArgsDict]
    ]
    bigtable_options: NotRequired[
        pulumi.Input[TableExternalDataConfigurationBigtableOptionsArgsDict]
    ]
    compression: NotRequired[pulumi.Input[_builtins.str]]
    connection_id: NotRequired[pulumi.Input[_builtins.str]]
    csv_options: NotRequired[
        pulumi.Input[TableExternalDataConfigurationCsvOptionsArgsDict]
    ]
    decimal_target_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    file_set_spec_type: NotRequired[pulumi.Input[_builtins.str]]
    google_sheets_options: NotRequired[
        pulumi.Input[TableExternalDataConfigurationGoogleSheetsOptionsArgsDict]
    ]
    hive_partitioning_options: NotRequired[
        pulumi.Input[TableExternalDataConfigurationHivePartitioningOptionsArgsDict]
    ]
    ignore_unknown_values: NotRequired[pulumi.Input[_builtins.bool]]
    json_extension: NotRequired[pulumi.Input[_builtins.str]]
    json_options: NotRequired[
        pulumi.Input[TableExternalDataConfigurationJsonOptionsArgsDict]
    ]
    max_bad_records: NotRequired[pulumi.Input[_builtins.int]]
    metadata_cache_mode: NotRequired[pulumi.Input[_builtins.str]]
    object_metadata: NotRequired[pulumi.Input[_builtins.str]]
    parquet_options: NotRequired[
        pulumi.Input[TableExternalDataConfigurationParquetOptionsArgsDict]
    ]
    reference_file_schema_uri: NotRequired[pulumi.Input[_builtins.str]]
    schema: NotRequired[pulumi.Input[_builtins.str]]
    source_format: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableExternalDataConfigurationArgs:
    def __init__(
        __self__,
        *,
        autodetect: pulumi.Input[_builtins.bool],
        source_uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        avro_options: Optional[
            pulumi.Input[TableExternalDataConfigurationAvroOptionsArgs]
        ] = ...,
        bigtable_options: Optional[
            pulumi.Input[TableExternalDataConfigurationBigtableOptionsArgs]
        ] = ...,
        compression: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        csv_options: Optional[
            pulumi.Input[TableExternalDataConfigurationCsvOptionsArgs]
        ] = ...,
        decimal_target_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        file_set_spec_type: Optional[pulumi.Input[_builtins.str]] = ...,
        google_sheets_options: Optional[
            pulumi.Input[TableExternalDataConfigurationGoogleSheetsOptionsArgs]
        ] = ...,
        hive_partitioning_options: Optional[
            pulumi.Input[TableExternalDataConfigurationHivePartitioningOptionsArgs]
        ] = ...,
        ignore_unknown_values: Optional[pulumi.Input[_builtins.bool]] = ...,
        json_extension: Optional[pulumi.Input[_builtins.str]] = ...,
        json_options: Optional[
            pulumi.Input[TableExternalDataConfigurationJsonOptionsArgs]
        ] = ...,
        max_bad_records: Optional[pulumi.Input[_builtins.int]] = ...,
        metadata_cache_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        object_metadata: Optional[pulumi.Input[_builtins.str]] = ...,
        parquet_options: Optional[
            pulumi.Input[TableExternalDataConfigurationParquetOptionsArgs]
        ] = ...,
        reference_file_schema_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
        source_format: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def autodetect(self) -> pulumi.Input[_builtins.bool]: ...
    @autodetect.setter
    def autodetect(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="sourceUris")
    def source_uris(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @source_uris.setter
    def source_uris(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="avroOptions")
    def avro_options(
        self,
    ) -> Optional[pulumi.Input[TableExternalDataConfigurationAvroOptionsArgs]]: ...
    @avro_options.setter
    def avro_options(
        self,
        value: Optional[pulumi.Input[TableExternalDataConfigurationAvroOptionsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bigtableOptions")
    def bigtable_options(
        self,
    ) -> Optional[pulumi.Input[TableExternalDataConfigurationBigtableOptionsArgs]]: ...
    @bigtable_options.setter
    def bigtable_options(
        self,
        value: Optional[
            pulumi.Input[TableExternalDataConfigurationBigtableOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression.setter
    def compression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="csvOptions")
    def csv_options(
        self,
    ) -> Optional[pulumi.Input[TableExternalDataConfigurationCsvOptionsArgs]]: ...
    @csv_options.setter
    def csv_options(
        self,
        value: Optional[pulumi.Input[TableExternalDataConfigurationCsvOptionsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="decimalTargetTypes")
    def decimal_target_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @decimal_target_types.setter
    def decimal_target_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileSetSpecType")
    def file_set_spec_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_set_spec_type.setter
    def file_set_spec_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="googleSheetsOptions")
    def google_sheets_options(
        self,
    ) -> Optional[
        pulumi.Input[TableExternalDataConfigurationGoogleSheetsOptionsArgs]
    ]: ...
    @google_sheets_options.setter
    def google_sheets_options(
        self,
        value: Optional[
            pulumi.Input[TableExternalDataConfigurationGoogleSheetsOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hivePartitioningOptions")
    def hive_partitioning_options(
        self,
    ) -> Optional[
        pulumi.Input[TableExternalDataConfigurationHivePartitioningOptionsArgs]
    ]: ...
    @hive_partitioning_options.setter
    def hive_partitioning_options(
        self,
        value: Optional[
            pulumi.Input[TableExternalDataConfigurationHivePartitioningOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownValues")
    def ignore_unknown_values(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_unknown_values.setter
    def ignore_unknown_values(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="jsonExtension")
    def json_extension(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @json_extension.setter
    def json_extension(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jsonOptions")
    def json_options(
        self,
    ) -> Optional[pulumi.Input[TableExternalDataConfigurationJsonOptionsArgs]]: ...
    @json_options.setter
    def json_options(
        self,
        value: Optional[pulumi.Input[TableExternalDataConfigurationJsonOptionsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxBadRecords")
    def max_bad_records(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_bad_records.setter
    def max_bad_records(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="metadataCacheMode")
    def metadata_cache_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metadata_cache_mode.setter
    def metadata_cache_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectMetadata")
    def object_metadata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_metadata.setter
    def object_metadata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parquetOptions")
    def parquet_options(
        self,
    ) -> Optional[pulumi.Input[TableExternalDataConfigurationParquetOptionsArgs]]: ...
    @parquet_options.setter
    def parquet_options(
        self,
        value: Optional[pulumi.Input[TableExternalDataConfigurationParquetOptionsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="referenceFileSchemaUri")
    def reference_file_schema_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reference_file_schema_uri.setter
    def reference_file_schema_uri(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFormat")
    def source_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_format.setter
    def source_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableExternalDataConfigurationAvroOptionsArgsDict(TypedDict):
    use_avro_logical_types: pulumi.Input[_builtins.bool]

@pulumi.input_type
class TableExternalDataConfigurationAvroOptionsArgs:
    def __init__(
        __self__, *, use_avro_logical_types: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="useAvroLogicalTypes")
    def use_avro_logical_types(self) -> pulumi.Input[_builtins.bool]: ...
    @use_avro_logical_types.setter
    def use_avro_logical_types(self, value: pulumi.Input[_builtins.bool]): ...

class TableExternalDataConfigurationBigtableOptionsArgsDict(TypedDict):
    column_families: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    TableExternalDataConfigurationBigtableOptionsColumnFamilyArgsDict
                ]
            ]
        ]
    ]
    ignore_unspecified_column_families: NotRequired[pulumi.Input[_builtins.bool]]
    output_column_families_as_json: NotRequired[pulumi.Input[_builtins.bool]]
    read_rowkey_as_string: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class TableExternalDataConfigurationBigtableOptionsArgs:
    def __init__(
        __self__,
        *,
        column_families: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        TableExternalDataConfigurationBigtableOptionsColumnFamilyArgs
                    ]
                ]
            ]
        ] = ...,
        ignore_unspecified_column_families: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        output_column_families_as_json: Optional[pulumi.Input[_builtins.bool]] = ...,
        read_rowkey_as_string: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnFamilies")
    def column_families(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    TableExternalDataConfigurationBigtableOptionsColumnFamilyArgs
                ]
            ]
        ]
    ]: ...
    @column_families.setter
    def column_families(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        TableExternalDataConfigurationBigtableOptionsColumnFamilyArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreUnspecifiedColumnFamilies")
    def ignore_unspecified_column_families(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_unspecified_column_families.setter
    def ignore_unspecified_column_families(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputColumnFamiliesAsJson")
    def output_column_families_as_json(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @output_column_families_as_json.setter
    def output_column_families_as_json(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readRowkeyAsString")
    def read_rowkey_as_string(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_rowkey_as_string.setter
    def read_rowkey_as_string(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TableExternalDataConfigurationBigtableOptionsColumnFamilyArgsDict(TypedDict):
    columns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    TableExternalDataConfigurationBigtableOptionsColumnFamilyColumnArgsDict
                ]
            ]
        ]
    ]
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    family_id: NotRequired[pulumi.Input[_builtins.str]]
    only_read_latest: NotRequired[pulumi.Input[_builtins.bool]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableExternalDataConfigurationBigtableOptionsColumnFamilyArgs:
    def __init__(
        __self__,
        *,
        columns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        TableExternalDataConfigurationBigtableOptionsColumnFamilyColumnArgs
                    ]
                ]
            ]
        ] = ...,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        family_id: Optional[pulumi.Input[_builtins.str]] = ...,
        only_read_latest: Optional[pulumi.Input[_builtins.bool]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    TableExternalDataConfigurationBigtableOptionsColumnFamilyColumnArgs
                ]
            ]
        ]
    ]: ...
    @columns.setter
    def columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        TableExternalDataConfigurationBigtableOptionsColumnFamilyColumnArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="familyId")
    def family_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @family_id.setter
    def family_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="onlyReadLatest")
    def only_read_latest(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @only_read_latest.setter
    def only_read_latest(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableExternalDataConfigurationBigtableOptionsColumnFamilyColumnArgsDict(
    TypedDict
):
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    field_name: NotRequired[pulumi.Input[_builtins.str]]
    only_read_latest: NotRequired[pulumi.Input[_builtins.bool]]
    qualifier_encoded: NotRequired[pulumi.Input[_builtins.str]]
    qualifier_string: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableExternalDataConfigurationBigtableOptionsColumnFamilyColumnArgs:
    def __init__(
        __self__,
        *,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        field_name: Optional[pulumi.Input[_builtins.str]] = ...,
        only_read_latest: Optional[pulumi.Input[_builtins.bool]] = ...,
        qualifier_encoded: Optional[pulumi.Input[_builtins.str]] = ...,
        qualifier_string: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field_name.setter
    def field_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="onlyReadLatest")
    def only_read_latest(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @only_read_latest.setter
    def only_read_latest(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="qualifierEncoded")
    def qualifier_encoded(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @qualifier_encoded.setter
    def qualifier_encoded(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="qualifierString")
    def qualifier_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @qualifier_string.setter
    def qualifier_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableExternalDataConfigurationCsvOptionsArgsDict(TypedDict):
    quote: pulumi.Input[_builtins.str]
    allow_jagged_rows: NotRequired[pulumi.Input[_builtins.bool]]
    allow_quoted_newlines: NotRequired[pulumi.Input[_builtins.bool]]
    encoding: NotRequired[pulumi.Input[_builtins.str]]
    field_delimiter: NotRequired[pulumi.Input[_builtins.str]]
    skip_leading_rows: NotRequired[pulumi.Input[_builtins.int]]
    source_column_match: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableExternalDataConfigurationCsvOptionsArgs:
    def __init__(
        __self__,
        *,
        quote: pulumi.Input[_builtins.str],
        allow_jagged_rows: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_quoted_newlines: Optional[pulumi.Input[_builtins.bool]] = ...,
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        field_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_leading_rows: Optional[pulumi.Input[_builtins.int]] = ...,
        source_column_match: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def quote(self) -> pulumi.Input[_builtins.str]: ...
    @quote.setter
    def quote(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowJaggedRows")
    def allow_jagged_rows(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_jagged_rows.setter
    def allow_jagged_rows(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowQuotedNewlines")
    def allow_quoted_newlines(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_quoted_newlines.setter
    def allow_quoted_newlines(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipLeadingRows")
    def skip_leading_rows(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @skip_leading_rows.setter
    def skip_leading_rows(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceColumnMatch")
    def source_column_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_column_match.setter
    def source_column_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableExternalDataConfigurationGoogleSheetsOptionsArgsDict(TypedDict):
    range: NotRequired[pulumi.Input[_builtins.str]]
    skip_leading_rows: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TableExternalDataConfigurationGoogleSheetsOptionsArgs:
    def __init__(
        __self__,
        *,
        range: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_leading_rows: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @range.setter
    def range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipLeadingRows")
    def skip_leading_rows(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @skip_leading_rows.setter
    def skip_leading_rows(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TableExternalDataConfigurationHivePartitioningOptionsArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[_builtins.str]]
    require_partition_filter: NotRequired[pulumi.Input[_builtins.bool]]
    source_uri_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableExternalDataConfigurationHivePartitioningOptionsArgs:
    def __init__(
        __self__,
        *,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        require_partition_filter: Optional[pulumi.Input[_builtins.bool]] = ...,
        source_uri_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requirePartitionFilter")
    def require_partition_filter(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_partition_filter.setter
    def require_partition_filter(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceUriPrefix")
    def source_uri_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_uri_prefix.setter
    def source_uri_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableExternalDataConfigurationJsonOptionsArgsDict(TypedDict):
    encoding: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableExternalDataConfigurationJsonOptionsArgs:
    def __init__(
        __self__, *, encoding: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableExternalDataConfigurationParquetOptionsArgsDict(TypedDict):
    enable_list_inference: NotRequired[pulumi.Input[_builtins.bool]]
    enum_as_string: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class TableExternalDataConfigurationParquetOptionsArgs:
    def __init__(
        __self__,
        *,
        enable_list_inference: Optional[pulumi.Input[_builtins.bool]] = ...,
        enum_as_string: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableListInference")
    def enable_list_inference(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_list_inference.setter
    def enable_list_inference(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enumAsString")
    def enum_as_string(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enum_as_string.setter
    def enum_as_string(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TableMaterializedViewArgsDict(TypedDict):
    query: pulumi.Input[_builtins.str]
    allow_non_incremental_definition: NotRequired[pulumi.Input[_builtins.bool]]
    enable_refresh: NotRequired[pulumi.Input[_builtins.bool]]
    refresh_interval_ms: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TableMaterializedViewArgs:
    def __init__(
        __self__,
        *,
        query: pulumi.Input[_builtins.str],
        allow_non_incremental_definition: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_refresh: Optional[pulumi.Input[_builtins.bool]] = ...,
        refresh_interval_ms: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Input[_builtins.str]: ...
    @query.setter
    def query(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowNonIncrementalDefinition")
    def allow_non_incremental_definition(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_non_incremental_definition.setter
    def allow_non_incremental_definition(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableRefresh")
    def enable_refresh(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_refresh.setter
    def enable_refresh(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshIntervalMs")
    def refresh_interval_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @refresh_interval_ms.setter
    def refresh_interval_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TableRangePartitioningArgsDict(TypedDict):
    field: pulumi.Input[_builtins.str]
    range: pulumi.Input[TableRangePartitioningRangeArgsDict]

@pulumi.input_type
class TableRangePartitioningArgs:
    def __init__(
        __self__,
        *,
        field: pulumi.Input[_builtins.str],
        range: pulumi.Input[TableRangePartitioningRangeArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> pulumi.Input[_builtins.str]: ...
    @field.setter
    def field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def range(self) -> pulumi.Input[TableRangePartitioningRangeArgs]: ...
    @range.setter
    def range(self, value: pulumi.Input[TableRangePartitioningRangeArgs]): ...

class TableRangePartitioningRangeArgsDict(TypedDict):
    end: pulumi.Input[_builtins.int]
    interval: pulumi.Input[_builtins.int]
    start: pulumi.Input[_builtins.int]

@pulumi.input_type
class TableRangePartitioningRangeArgs:
    def __init__(
        __self__,
        *,
        end: pulumi.Input[_builtins.int],
        interval: pulumi.Input[_builtins.int],
        start: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> pulumi.Input[_builtins.int]: ...
    @end.setter
    def end(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> pulumi.Input[_builtins.int]: ...
    @interval.setter
    def interval(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> pulumi.Input[_builtins.int]: ...
    @start.setter
    def start(self, value: pulumi.Input[_builtins.int]): ...

class TableSchemaForeignTypeInfoArgsDict(TypedDict):
    type_system: pulumi.Input[_builtins.str]

@pulumi.input_type
class TableSchemaForeignTypeInfoArgs:
    def __init__(__self__, *, type_system: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeSystem")
    def type_system(self) -> pulumi.Input[_builtins.str]: ...
    @type_system.setter
    def type_system(self, value: pulumi.Input[_builtins.str]): ...

class TableTableConstraintsArgsDict(TypedDict):
    foreign_keys: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TableTableConstraintsForeignKeyArgsDict]]]
    ]
    primary_key: NotRequired[pulumi.Input[TableTableConstraintsPrimaryKeyArgsDict]]

@pulumi.input_type
class TableTableConstraintsArgs:
    def __init__(
        __self__,
        *,
        foreign_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[TableTableConstraintsForeignKeyArgs]]]
        ] = ...,
        primary_key: Optional[pulumi.Input[TableTableConstraintsPrimaryKeyArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="foreignKeys")
    def foreign_keys(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TableTableConstraintsForeignKeyArgs]]]
    ]: ...
    @foreign_keys.setter
    def foreign_keys(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TableTableConstraintsForeignKeyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(
        self,
    ) -> Optional[pulumi.Input[TableTableConstraintsPrimaryKeyArgs]]: ...
    @primary_key.setter
    def primary_key(
        self, value: Optional[pulumi.Input[TableTableConstraintsPrimaryKeyArgs]]
    ): ...

class TableTableConstraintsForeignKeyArgsDict(TypedDict):
    column_references: pulumi.Input[
        TableTableConstraintsForeignKeyColumnReferencesArgsDict
    ]
    referenced_table: pulumi.Input[
        TableTableConstraintsForeignKeyReferencedTableArgsDict
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableTableConstraintsForeignKeyArgs:
    def __init__(
        __self__,
        *,
        column_references: pulumi.Input[
            TableTableConstraintsForeignKeyColumnReferencesArgs
        ],
        referenced_table: pulumi.Input[
            TableTableConstraintsForeignKeyReferencedTableArgs
        ],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnReferences")
    def column_references(
        self,
    ) -> pulumi.Input[TableTableConstraintsForeignKeyColumnReferencesArgs]: ...
    @column_references.setter
    def column_references(
        self, value: pulumi.Input[TableTableConstraintsForeignKeyColumnReferencesArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="referencedTable")
    def referenced_table(
        self,
    ) -> pulumi.Input[TableTableConstraintsForeignKeyReferencedTableArgs]: ...
    @referenced_table.setter
    def referenced_table(
        self, value: pulumi.Input[TableTableConstraintsForeignKeyReferencedTableArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableTableConstraintsForeignKeyColumnReferencesArgsDict(TypedDict):
    referenced_column: pulumi.Input[_builtins.str]
    referencing_column: pulumi.Input[_builtins.str]

@pulumi.input_type
class TableTableConstraintsForeignKeyColumnReferencesArgs:
    def __init__(
        __self__,
        *,
        referenced_column: pulumi.Input[_builtins.str],
        referencing_column: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="referencedColumn")
    def referenced_column(self) -> pulumi.Input[_builtins.str]: ...
    @referenced_column.setter
    def referenced_column(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="referencingColumn")
    def referencing_column(self) -> pulumi.Input[_builtins.str]: ...
    @referencing_column.setter
    def referencing_column(self, value: pulumi.Input[_builtins.str]): ...

class TableTableConstraintsForeignKeyReferencedTableArgsDict(TypedDict):
    dataset_id: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    table_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class TableTableConstraintsForeignKeyReferencedTableArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
        table_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_id.setter
    def table_id(self, value: pulumi.Input[_builtins.str]): ...

class TableTableConstraintsPrimaryKeyArgsDict(TypedDict):
    columns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class TableTableConstraintsPrimaryKeyArgs:
    def __init__(
        __self__, *, columns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @columns.setter
    def columns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class TableTableReplicationInfoArgsDict(TypedDict):
    source_dataset_id: pulumi.Input[_builtins.str]
    source_project_id: pulumi.Input[_builtins.str]
    source_table_id: pulumi.Input[_builtins.str]
    replication_interval_ms: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TableTableReplicationInfoArgs:
    def __init__(
        __self__,
        *,
        source_dataset_id: pulumi.Input[_builtins.str],
        source_project_id: pulumi.Input[_builtins.str],
        source_table_id: pulumi.Input[_builtins.str],
        replication_interval_ms: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceDatasetId")
    def source_dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_dataset_id.setter
    def source_dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceProjectId")
    def source_project_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_project_id.setter
    def source_project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceTableId")
    def source_table_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_table_id.setter
    def source_table_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="replicationIntervalMs")
    def replication_interval_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replication_interval_ms.setter
    def replication_interval_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TableTimePartitioningArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    expiration_ms: NotRequired[pulumi.Input[_builtins.int]]
    field: NotRequired[pulumi.Input[_builtins.str]]
    require_partition_filter: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class TableTimePartitioningArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        expiration_ms: Optional[pulumi.Input[_builtins.int]] = ...,
        field: Optional[pulumi.Input[_builtins.str]] = ...,
        require_partition_filter: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="expirationMs")
    def expiration_ms(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @expiration_ms.setter
    def expiration_ms(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requirePartitionFilter")
    @_utilities.deprecated(...)
    def require_partition_filter(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_partition_filter.setter
    def require_partition_filter(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class TableViewArgsDict(TypedDict):
    query: pulumi.Input[_builtins.str]
    use_legacy_sql: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class TableViewArgs:
    def __init__(
        __self__,
        *,
        query: pulumi.Input[_builtins.str],
        use_legacy_sql: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Input[_builtins.str]: ...
    @query.setter
    def query(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="useLegacySql")
    def use_legacy_sql(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_legacy_sql.setter
    def use_legacy_sql(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
