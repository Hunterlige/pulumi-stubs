import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AggregateFunctionPropertiesResponse",
    "AvroSerializationResponse",
    "AzureDataLakeStoreOutputDataSourceResponse",
    "AzureFunctionOutputDataSourceResponse",
    ...,
    "AzureMachineLearningWebServiceInputColumnResponse",
    "AzureMachineLearningWebServiceInputsResponse",
    "AzureMachineLearningWebServiceOutputColumnResponse",
    "AzureSqlDatabaseOutputDataSourceResponse",
    "AzureSqlReferenceInputDataSourceResponse",
    "AzureSynapseOutputDataSourceResponse",
    "AzureTableOutputDataSourceResponse",
    "BlobOutputDataSourceResponse",
    "BlobReferenceInputDataSourceResponse",
    "BlobStreamInputDataSourceResponse",
    "ClusterInfoResponse",
    "ClusterJobResponse",
    "ClusterSkuResponse",
    "CompressionResponse",
    "CsvSerializationResponse",
    "DiagnosticConditionResponse",
    "DiagnosticsResponse",
    "DocumentDbOutputDataSourceResponse",
    "EventHubOutputDataSourceResponse",
    "EventHubStreamInputDataSourceResponse",
    "EventHubV2OutputDataSourceResponse",
    "EventHubV2StreamInputDataSourceResponse",
    "FileReferenceInputDataSourceResponse",
    "FunctionInputResponse",
    "FunctionOutputResponse",
    "FunctionResponse",
    "GatewayMessageBusOutputDataSourceResponse",
    "GatewayMessageBusStreamInputDataSourceResponse",
    "IdentityResponse",
    "InputResponse",
    "IoTHubStreamInputDataSourceResponse",
    "JavaScriptFunctionBindingResponse",
    "JobStorageAccountResponse",
    "JsonSerializationResponse",
    "OutputResponse",
    "ParquetSerializationResponse",
    "PowerBIOutputDataSourceResponse",
    "PrivateLinkConnectionStateResponse",
    "PrivateLinkServiceConnectionResponse",
    "ReferenceInputPropertiesResponse",
    "ScalarFunctionPropertiesResponse",
    "ServiceBusQueueOutputDataSourceResponse",
    "ServiceBusTopicOutputDataSourceResponse",
    "SkuResponse",
    "StorageAccountResponse",
    "StreamInputPropertiesResponse",
    "TransformationResponse",
]

@pulumi.output_type
class AggregateFunctionPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        etag: _builtins.str,
        type: _builtins.str,
        binding: Optional[Any] = ...,
        inputs: Optional[Sequence[outputs.FunctionInputResponse]] = ...,
        output: Optional[outputs.FunctionOutputResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def binding(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[Sequence[outputs.FunctionInputResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def output(self) -> Optional[outputs.FunctionOutputResponse]: ...

@pulumi.output_type
class AvroSerializationResponse(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AzureDataLakeStoreOutputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        account_name: Optional[_builtins.str] = ...,
        authentication_mode: Optional[_builtins.str] = ...,
        date_format: Optional[_builtins.str] = ...,
        file_path_prefix: Optional[_builtins.str] = ...,
        refresh_token: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
        time_format: Optional[_builtins.str] = ...,
        token_user_display_name: Optional[_builtins.str] = ...,
        token_user_principal_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dateFormat")
    def date_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filePathPrefix")
    def file_path_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeFormat")
    def time_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenUserDisplayName")
    def token_user_display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenUserPrincipalName")
    def token_user_principal_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureFunctionOutputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        api_key: Optional[_builtins.str] = ...,
        function_app_name: Optional[_builtins.str] = ...,
        function_name: Optional[_builtins.str] = ...,
        max_batch_count: Optional[_builtins.float] = ...,
        max_batch_size: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="functionAppName")
    def function_app_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxBatchCount")
    def max_batch_count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="maxBatchSize")
    def max_batch_size(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class AzureMachineLearningWebServiceFunctionBindingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        api_key: Optional[_builtins.str] = ...,
        batch_size: Optional[_builtins.int] = ...,
        endpoint: Optional[_builtins.str] = ...,
        inputs: Optional[outputs.AzureMachineLearningWebServiceInputsResponse] = ...,
        outputs: Optional[
            Sequence[outputs.AzureMachineLearningWebServiceOutputColumnResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def inputs(
        self,
    ) -> Optional[outputs.AzureMachineLearningWebServiceInputsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def outputs(
        self,
    ) -> Optional[
        Sequence[outputs.AzureMachineLearningWebServiceOutputColumnResponse]
    ]: ...

@pulumi.output_type
class AzureMachineLearningWebServiceInputColumnResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_type: Optional[_builtins.str] = ...,
        map_to: Optional[_builtins.int] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mapTo")
    def map_to(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureMachineLearningWebServiceInputsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column_names: Optional[
            Sequence[outputs.AzureMachineLearningWebServiceInputColumnResponse]
        ] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(
        self,
    ) -> Optional[
        Sequence[outputs.AzureMachineLearningWebServiceInputColumnResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureMachineLearningWebServiceOutputColumnResponse(dict):
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
class AzureSqlDatabaseOutputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authentication_mode: Optional[_builtins.str] = ...,
        database: Optional[_builtins.str] = ...,
        max_batch_count: Optional[_builtins.float] = ...,
        max_writer_count: Optional[_builtins.float] = ...,
        password: Optional[_builtins.str] = ...,
        server: Optional[_builtins.str] = ...,
        table: Optional[_builtins.str] = ...,
        user: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxBatchCount")
    def max_batch_count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="maxWriterCount")
    def max_writer_count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureSqlReferenceInputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        database: Optional[_builtins.str] = ...,
        delta_snapshot_query: Optional[_builtins.str] = ...,
        full_snapshot_query: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        refresh_rate: Optional[_builtins.str] = ...,
        refresh_type: Optional[_builtins.str] = ...,
        server: Optional[_builtins.str] = ...,
        table: Optional[_builtins.str] = ...,
        user: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deltaSnapshotQuery")
    def delta_snapshot_query(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fullSnapshotQuery")
    def full_snapshot_query(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshRate")
    def refresh_rate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshType")
    def refresh_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureSynapseOutputDataSourceResponse(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        database: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        server: Optional[_builtins.str] = ...,
        table: Optional[_builtins.str] = ...,
        user: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureTableOutputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        account_key: Optional[_builtins.str] = ...,
        account_name: Optional[_builtins.str] = ...,
        batch_size: Optional[_builtins.int] = ...,
        columns_to_remove: Optional[Sequence[_builtins.str]] = ...,
        partition_key: Optional[_builtins.str] = ...,
        row_key: Optional[_builtins.str] = ...,
        table: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="columnsToRemove")
    def columns_to_remove(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rowKey")
    def row_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BlobOutputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authentication_mode: Optional[_builtins.str] = ...,
        blob_path_prefix: Optional[_builtins.str] = ...,
        container: Optional[_builtins.str] = ...,
        date_format: Optional[_builtins.str] = ...,
        path_pattern: Optional[_builtins.str] = ...,
        storage_accounts: Optional[Sequence[outputs.StorageAccountResponse]] = ...,
        time_format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="blobPathPrefix")
    def blob_path_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dateFormat")
    def date_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pathPattern")
    def path_pattern(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(
        self,
    ) -> Optional[Sequence[outputs.StorageAccountResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="timeFormat")
    def time_format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BlobReferenceInputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authentication_mode: Optional[_builtins.str] = ...,
        container: Optional[_builtins.str] = ...,
        date_format: Optional[_builtins.str] = ...,
        path_pattern: Optional[_builtins.str] = ...,
        storage_accounts: Optional[Sequence[outputs.StorageAccountResponse]] = ...,
        time_format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dateFormat")
    def date_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pathPattern")
    def path_pattern(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(
        self,
    ) -> Optional[Sequence[outputs.StorageAccountResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="timeFormat")
    def time_format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BlobStreamInputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authentication_mode: Optional[_builtins.str] = ...,
        container: Optional[_builtins.str] = ...,
        date_format: Optional[_builtins.str] = ...,
        path_pattern: Optional[_builtins.str] = ...,
        source_partition_count: Optional[_builtins.int] = ...,
        storage_accounts: Optional[Sequence[outputs.StorageAccountResponse]] = ...,
        time_format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dateFormat")
    def date_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pathPattern")
    def path_pattern(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourcePartitionCount")
    def source_partition_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(
        self,
    ) -> Optional[Sequence[outputs.StorageAccountResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="timeFormat")
    def time_format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterInfoResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterJobResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        job_state: _builtins.str,
        streaming_units: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jobState")
    def job_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="streamingUnits")
    def streaming_units(self) -> _builtins.int: ...

@pulumi.output_type
class ClusterSkuResponse(dict):
    def __init__(
        __self__,
        *,
        capacity: Optional[_builtins.int] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CompressionResponse(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class CsvSerializationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        encoding: Optional[_builtins.str] = ...,
        field_delimiter: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DiagnosticConditionResponse(dict):
    def __init__(
        __self__, *, code: _builtins.str, message: _builtins.str, since: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def since(self) -> _builtins.str: ...

@pulumi.output_type
class DiagnosticsResponse(dict):
    def __init__(
        __self__, *, conditions: Sequence[outputs.DiagnosticConditionResponse]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Sequence[outputs.DiagnosticConditionResponse]: ...

@pulumi.output_type
class DocumentDbOutputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        account_id: Optional[_builtins.str] = ...,
        account_key: Optional[_builtins.str] = ...,
        collection_name_pattern: Optional[_builtins.str] = ...,
        database: Optional[_builtins.str] = ...,
        document_id: Optional[_builtins.str] = ...,
        partition_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="collectionNamePattern")
    def collection_name_pattern(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentId")
    def document_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventHubOutputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authentication_mode: Optional[_builtins.str] = ...,
        event_hub_name: Optional[_builtins.str] = ...,
        partition_key: Optional[_builtins.str] = ...,
        property_columns: Optional[Sequence[_builtins.str]] = ...,
        service_bus_namespace: Optional[_builtins.str] = ...,
        shared_access_policy_key: Optional[_builtins.str] = ...,
        shared_access_policy_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertyColumns")
    def property_columns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceBusNamespace")
    def service_bus_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyKey")
    def shared_access_policy_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventHubStreamInputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authentication_mode: Optional[_builtins.str] = ...,
        consumer_group_name: Optional[_builtins.str] = ...,
        event_hub_name: Optional[_builtins.str] = ...,
        service_bus_namespace: Optional[_builtins.str] = ...,
        shared_access_policy_key: Optional[_builtins.str] = ...,
        shared_access_policy_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroupName")
    def consumer_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceBusNamespace")
    def service_bus_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyKey")
    def shared_access_policy_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventHubV2OutputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authentication_mode: Optional[_builtins.str] = ...,
        event_hub_name: Optional[_builtins.str] = ...,
        partition_key: Optional[_builtins.str] = ...,
        property_columns: Optional[Sequence[_builtins.str]] = ...,
        service_bus_namespace: Optional[_builtins.str] = ...,
        shared_access_policy_key: Optional[_builtins.str] = ...,
        shared_access_policy_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertyColumns")
    def property_columns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceBusNamespace")
    def service_bus_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyKey")
    def shared_access_policy_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventHubV2StreamInputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authentication_mode: Optional[_builtins.str] = ...,
        consumer_group_name: Optional[_builtins.str] = ...,
        event_hub_name: Optional[_builtins.str] = ...,
        service_bus_namespace: Optional[_builtins.str] = ...,
        shared_access_policy_key: Optional[_builtins.str] = ...,
        shared_access_policy_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroupName")
    def consumer_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceBusNamespace")
    def service_bus_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyKey")
    def shared_access_policy_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FileReferenceInputDataSourceResponse(dict):
    def __init__(
        __self__, *, type: _builtins.str, path: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FunctionInputResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_type: Optional[_builtins.str] = ...,
        is_configuration_parameter: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isConfigurationParameter")
    def is_configuration_parameter(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FunctionOutputResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, data_type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FunctionResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        type: _builtins.str,
        name: Optional[_builtins.str] = ...,
        properties: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Any]: ...

@pulumi.output_type
class GatewayMessageBusOutputDataSourceResponse(dict):
    def __init__(
        __self__, *, type: _builtins.str, topic: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayMessageBusStreamInputDataSourceResponse(dict):
    def __init__(
        __self__, *, type: _builtins.str, topic: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InputResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        type: _builtins.str,
        name: Optional[_builtins.str] = ...,
        properties: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Any]: ...

@pulumi.output_type
class IoTHubStreamInputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        consumer_group_name: Optional[_builtins.str] = ...,
        endpoint: Optional[_builtins.str] = ...,
        iot_hub_namespace: Optional[_builtins.str] = ...,
        shared_access_policy_key: Optional[_builtins.str] = ...,
        shared_access_policy_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroupName")
    def consumer_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iotHubNamespace")
    def iot_hub_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyKey")
    def shared_access_policy_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JavaScriptFunctionBindingResponse(dict):
    def __init__(
        __self__, *, type: _builtins.str, script: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def script(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobStorageAccountResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_key: Optional[_builtins.str] = ...,
        account_name: Optional[_builtins.str] = ...,
        authentication_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JsonSerializationResponse(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        encoding: Optional[_builtins.str] = ...,
        format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OutputResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        diagnostics: outputs.DiagnosticsResponse,
        etag: _builtins.str,
        id: _builtins.str,
        type: _builtins.str,
        datasource: Optional[Any] = ...,
        name: Optional[_builtins.str] = ...,
        serialization: Optional[Any] = ...,
        size_window: Optional[_builtins.int] = ...,
        time_window: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> outputs.DiagnosticsResponse: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def datasource(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def serialization(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="sizeWindow")
    def size_window(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ParquetSerializationResponse(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class PowerBIOutputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authentication_mode: Optional[_builtins.str] = ...,
        dataset: Optional[_builtins.str] = ...,
        group_id: Optional[_builtins.str] = ...,
        group_name: Optional[_builtins.str] = ...,
        refresh_token: Optional[_builtins.str] = ...,
        table: Optional[_builtins.str] = ...,
        token_user_display_name: Optional[_builtins.str] = ...,
        token_user_principal_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenUserDisplayName")
    def token_user_display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenUserPrincipalName")
    def token_user_principal_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateLinkConnectionStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions_required: _builtins.str,
        description: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateLinkServiceConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        request_message: _builtins.str,
        group_ids: Optional[Sequence[_builtins.str]] = ...,
        private_link_service_connection_state: Optional[
            outputs.PrivateLinkConnectionStateResponse
        ] = ...,
        private_link_service_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[outputs.PrivateLinkConnectionStateResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceId")
    def private_link_service_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReferenceInputPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        diagnostics: outputs.DiagnosticsResponse,
        etag: _builtins.str,
        type: _builtins.str,
        compression: Optional[outputs.CompressionResponse] = ...,
        datasource: Optional[Any] = ...,
        partition_key: Optional[_builtins.str] = ...,
        serialization: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> outputs.DiagnosticsResponse: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[outputs.CompressionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def datasource(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def serialization(self) -> Optional[Any]: ...

@pulumi.output_type
class ScalarFunctionPropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        etag: _builtins.str,
        type: _builtins.str,
        binding: Optional[Any] = ...,
        inputs: Optional[Sequence[outputs.FunctionInputResponse]] = ...,
        output: Optional[outputs.FunctionOutputResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def binding(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[Sequence[outputs.FunctionInputResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def output(self) -> Optional[outputs.FunctionOutputResponse]: ...

@pulumi.output_type
class ServiceBusQueueOutputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authentication_mode: Optional[_builtins.str] = ...,
        property_columns: Optional[Sequence[_builtins.str]] = ...,
        queue_name: Optional[_builtins.str] = ...,
        service_bus_namespace: Optional[_builtins.str] = ...,
        shared_access_policy_key: Optional[_builtins.str] = ...,
        shared_access_policy_name: Optional[_builtins.str] = ...,
        system_property_columns: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertyColumns")
    def property_columns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceBusNamespace")
    def service_bus_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyKey")
    def shared_access_policy_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemPropertyColumns")
    def system_property_columns(self) -> Optional[Any]: ...

@pulumi.output_type
class ServiceBusTopicOutputDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        authentication_mode: Optional[_builtins.str] = ...,
        property_columns: Optional[Sequence[_builtins.str]] = ...,
        service_bus_namespace: Optional[_builtins.str] = ...,
        shared_access_policy_key: Optional[_builtins.str] = ...,
        shared_access_policy_name: Optional[_builtins.str] = ...,
        system_property_columns: Optional[Mapping[str, _builtins.str]] = ...,
        topic_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propertyColumns")
    def property_columns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceBusNamespace")
    def service_bus_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyKey")
    def shared_access_policy_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharedAccessPolicyName")
    def shared_access_policy_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemPropertyColumns")
    def system_property_columns(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageAccountResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_key: Optional[_builtins.str] = ...,
        account_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamInputPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        diagnostics: outputs.DiagnosticsResponse,
        etag: _builtins.str,
        type: _builtins.str,
        compression: Optional[outputs.CompressionResponse] = ...,
        datasource: Optional[Any] = ...,
        partition_key: Optional[_builtins.str] = ...,
        serialization: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> outputs.DiagnosticsResponse: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[outputs.CompressionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def datasource(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="partitionKey")
    def partition_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def serialization(self) -> Optional[Any]: ...

@pulumi.output_type
class TransformationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        etag: _builtins.str,
        id: _builtins.str,
        type: _builtins.str,
        name: Optional[_builtins.str] = ...,
        query: Optional[_builtins.str] = ...,
        streaming_units: Optional[_builtins.int] = ...,
        valid_streaming_units: Optional[Sequence[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streamingUnits")
    def streaming_units(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="validStreamingUnits")
    def valid_streaming_units(self) -> Optional[Sequence[_builtins.int]]: ...
