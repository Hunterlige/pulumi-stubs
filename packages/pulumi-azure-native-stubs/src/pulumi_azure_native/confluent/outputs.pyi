import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AzureBlobStorageSinkConnectorServiceInfoResponse",
    "AzureBlobStorageSourceConnectorServiceInfoResponse",
    "AzureCosmosDBSinkConnectorServiceInfoResponse",
    "AzureCosmosDBSourceConnectorServiceInfoResponse",
    ...,
    "ClusterByokEntityResponse",
    "ClusterConfigEntityResponse",
    "ClusterEnvironmentEntityResponse",
    "ClusterNetworkEntityResponse",
    "ClusterRecordResponse",
    "ClusterSpecEntityResponse",
    "ClusterStatusEntityResponse",
    "ConfluentListMetadataResponse",
    "ConnectorInfoBaseResponse",
    "EnvironmentRecordResponse",
    "InvitationRecordResponse",
    "KafkaAzureBlobStorageSinkConnectorInfoResponse",
    "KafkaAzureBlobStorageSourceConnectorInfoResponse",
    "KafkaAzureCosmosDBSinkConnectorInfoResponse",
    "KafkaAzureCosmosDBSourceConnectorInfoResponse",
    ...,
    "MetadataEntityResponse",
    "OfferDetailResponse",
    "RegionRecordResponse",
    "RegionSpecEntityResponse",
    "RoleBindingRecordResponse",
    "SCClusterByokEntityResponse",
    "SCClusterNetworkEnvironmentEntityResponse",
    "SCClusterSpecEntityResponse",
    "SCMetadataEntityResponse",
    "ServiceAccountRecordResponse",
    "StreamGovernanceConfigResponse",
    "SystemDataResponse",
    "TopicMetadataEntityResponse",
    "TopicsInputConfigResponse",
    "TopicsRelatedLinkResponse",
    "UserDetailResponse",
    "UserRecordResponse",
]

@pulumi.output_type
class AzureBlobStorageSinkConnectorServiceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connector_service_type: _builtins.str,
        storage_account_key: Optional[_builtins.str] = ...,
        storage_account_name: Optional[_builtins.str] = ...,
        storage_container_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorServiceType")
    def connector_service_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountKey")
    def storage_account_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageContainerName")
    def storage_container_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureBlobStorageSourceConnectorServiceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connector_service_type: _builtins.str,
        storage_account_key: Optional[_builtins.str] = ...,
        storage_account_name: Optional[_builtins.str] = ...,
        storage_container_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorServiceType")
    def connector_service_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountKey")
    def storage_account_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageContainerName")
    def storage_container_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureCosmosDBSinkConnectorServiceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connector_service_type: _builtins.str,
        cosmos_connection_endpoint: Optional[_builtins.str] = ...,
        cosmos_containers_topic_mapping: Optional[_builtins.str] = ...,
        cosmos_database_name: Optional[_builtins.str] = ...,
        cosmos_id_strategy: Optional[_builtins.str] = ...,
        cosmos_master_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorServiceType")
    def connector_service_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cosmosConnectionEndpoint")
    def cosmos_connection_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cosmosContainersTopicMapping")
    def cosmos_containers_topic_mapping(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cosmosDatabaseName")
    def cosmos_database_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cosmosIdStrategy")
    def cosmos_id_strategy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cosmosMasterKey")
    def cosmos_master_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureCosmosDBSourceConnectorServiceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connector_service_type: _builtins.str,
        cosmos_connection_endpoint: Optional[_builtins.str] = ...,
        cosmos_containers_topic_mapping: Optional[_builtins.str] = ...,
        cosmos_database_name: Optional[_builtins.str] = ...,
        cosmos_master_key: Optional[_builtins.str] = ...,
        cosmos_message_key_enabled: Optional[_builtins.bool] = ...,
        cosmos_message_key_field: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorServiceType")
    def connector_service_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cosmosConnectionEndpoint")
    def cosmos_connection_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cosmosContainersTopicMapping")
    def cosmos_containers_topic_mapping(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cosmosDatabaseName")
    def cosmos_database_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cosmosMasterKey")
    def cosmos_master_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cosmosMessageKeyEnabled")
    def cosmos_message_key_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="cosmosMessageKeyField")
    def cosmos_message_key_field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureSynapseAnalyticsSinkConnectorServiceInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connector_service_type: _builtins.str,
        synapse_sql_database_name: Optional[_builtins.str] = ...,
        synapse_sql_password: Optional[_builtins.str] = ...,
        synapse_sql_server_name: Optional[_builtins.str] = ...,
        synapse_sql_user: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorServiceType")
    def connector_service_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="synapseSqlDatabaseName")
    def synapse_sql_database_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="synapseSqlPassword")
    def synapse_sql_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="synapseSqlServerName")
    def synapse_sql_server_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="synapseSqlUser")
    def synapse_sql_user(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterByokEntityResponse(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        related: Optional[_builtins.str] = ...,
        resource_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def related(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterConfigEntityResponse(dict):
    def __init__(__self__, *, kind: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterEnvironmentEntityResponse(dict):
    def __init__(
        __self__,
        *,
        environment: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        related: Optional[_builtins.str] = ...,
        resource_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def related(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNetworkEntityResponse(dict):
    def __init__(
        __self__,
        *,
        environment: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        related: Optional[_builtins.str] = ...,
        resource_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def related(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterRecordResponse(dict):
    def __init__(
        __self__,
        *,
        display_name: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
        metadata: Optional[outputs.MetadataEntityResponse] = ...,
        spec: Optional[outputs.ClusterSpecEntityResponse] = ...,
        status: Optional[outputs.ClusterStatusEntityResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.MetadataEntityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[outputs.ClusterSpecEntityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[outputs.ClusterStatusEntityResponse]: ...

@pulumi.output_type
class ClusterSpecEntityResponse(dict):
    def __init__(
        __self__,
        *,
        api_endpoint: Optional[_builtins.str] = ...,
        availability: Optional[_builtins.str] = ...,
        byok: Optional[outputs.ClusterByokEntityResponse] = ...,
        cloud: Optional[_builtins.str] = ...,
        config: Optional[outputs.ClusterConfigEntityResponse] = ...,
        display_name: Optional[_builtins.str] = ...,
        environment: Optional[outputs.ClusterEnvironmentEntityResponse] = ...,
        http_endpoint: Optional[_builtins.str] = ...,
        kafka_bootstrap_endpoint: Optional[_builtins.str] = ...,
        network: Optional[outputs.ClusterNetworkEntityResponse] = ...,
        region: Optional[_builtins.str] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def availability(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def byok(self) -> Optional[outputs.ClusterByokEntityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def cloud(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[outputs.ClusterConfigEntityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[outputs.ClusterEnvironmentEntityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kafkaBootstrapEndpoint")
    def kafka_bootstrap_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[outputs.ClusterNetworkEntityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterStatusEntityResponse(dict):
    def __init__(
        __self__,
        *,
        cku: Optional[_builtins.int] = ...,
        phase: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cku(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def phase(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConfluentListMetadataResponse(dict):
    def __init__(
        __self__,
        *,
        first: Optional[_builtins.str] = ...,
        last: Optional[_builtins.str] = ...,
        next: Optional[_builtins.str] = ...,
        prev: Optional[_builtins.str] = ...,
        total_size: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def first(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def last(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def next(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prev(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="totalSize")
    def total_size(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ConnectorInfoBaseResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connector_class: Optional[_builtins.str] = ...,
        connector_id: Optional[_builtins.str] = ...,
        connector_name: Optional[_builtins.str] = ...,
        connector_state: Optional[_builtins.str] = ...,
        connector_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorClass")
    def connector_class(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorState")
    def connector_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EnvironmentRecordResponse(dict):
    def __init__(
        __self__,
        *,
        display_name: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
        metadata: Optional[outputs.MetadataEntityResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.MetadataEntityResponse]: ...

@pulumi.output_type
class InvitationRecordResponse(dict):
    def __init__(
        __self__,
        *,
        accepted_at: Optional[_builtins.str] = ...,
        auth_type: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        expires_at: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
        metadata: Optional[outputs.MetadataEntityResponse] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptedAt")
    def accepted_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.MetadataEntityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KafkaAzureBlobStorageSinkConnectorInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        partner_connector_type: _builtins.str,
        api_key: Optional[_builtins.str] = ...,
        api_secret: Optional[_builtins.str] = ...,
        auth_type: Optional[_builtins.str] = ...,
        flush_size: Optional[_builtins.str] = ...,
        input_format: Optional[_builtins.str] = ...,
        max_tasks: Optional[_builtins.str] = ...,
        output_format: Optional[_builtins.str] = ...,
        service_account_id: Optional[_builtins.str] = ...,
        time_interval: Optional[_builtins.str] = ...,
        topics: Optional[Sequence[_builtins.str]] = ...,
        topics_dir: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partnerConnectorType")
    def partner_connector_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="apiSecret")
    def api_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="flushSize")
    def flush_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxTasks")
    def max_tasks(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeInterval")
    def time_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topics(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="topicsDir")
    def topics_dir(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KafkaAzureBlobStorageSourceConnectorInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        partner_connector_type: _builtins.str,
        api_key: Optional[_builtins.str] = ...,
        api_secret: Optional[_builtins.str] = ...,
        auth_type: Optional[_builtins.str] = ...,
        input_format: Optional[_builtins.str] = ...,
        max_tasks: Optional[_builtins.str] = ...,
        output_format: Optional[_builtins.str] = ...,
        service_account_id: Optional[_builtins.str] = ...,
        topic_regex: Optional[_builtins.str] = ...,
        topics_dir: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partnerConnectorType")
    def partner_connector_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="apiSecret")
    def api_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxTasks")
    def max_tasks(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="topicRegex")
    def topic_regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="topicsDir")
    def topics_dir(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KafkaAzureCosmosDBSinkConnectorInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        partner_connector_type: _builtins.str,
        api_key: Optional[_builtins.str] = ...,
        api_secret: Optional[_builtins.str] = ...,
        auth_type: Optional[_builtins.str] = ...,
        flush_size: Optional[_builtins.str] = ...,
        input_format: Optional[_builtins.str] = ...,
        max_tasks: Optional[_builtins.str] = ...,
        output_format: Optional[_builtins.str] = ...,
        service_account_id: Optional[_builtins.str] = ...,
        time_interval: Optional[_builtins.str] = ...,
        topics: Optional[Sequence[_builtins.str]] = ...,
        topics_dir: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partnerConnectorType")
    def partner_connector_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="apiSecret")
    def api_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="flushSize")
    def flush_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxTasks")
    def max_tasks(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeInterval")
    def time_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topics(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="topicsDir")
    def topics_dir(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KafkaAzureCosmosDBSourceConnectorInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        partner_connector_type: _builtins.str,
        api_key: Optional[_builtins.str] = ...,
        api_secret: Optional[_builtins.str] = ...,
        auth_type: Optional[_builtins.str] = ...,
        input_format: Optional[_builtins.str] = ...,
        max_tasks: Optional[_builtins.str] = ...,
        output_format: Optional[_builtins.str] = ...,
        service_account_id: Optional[_builtins.str] = ...,
        topic_regex: Optional[_builtins.str] = ...,
        topics_dir: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partnerConnectorType")
    def partner_connector_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="apiSecret")
    def api_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxTasks")
    def max_tasks(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="topicRegex")
    def topic_regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="topicsDir")
    def topics_dir(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KafkaAzureSynapseAnalyticsSinkConnectorInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        partner_connector_type: _builtins.str,
        api_key: Optional[_builtins.str] = ...,
        api_secret: Optional[_builtins.str] = ...,
        auth_type: Optional[_builtins.str] = ...,
        flush_size: Optional[_builtins.str] = ...,
        input_format: Optional[_builtins.str] = ...,
        max_tasks: Optional[_builtins.str] = ...,
        output_format: Optional[_builtins.str] = ...,
        service_account_id: Optional[_builtins.str] = ...,
        time_interval: Optional[_builtins.str] = ...,
        topics: Optional[Sequence[_builtins.str]] = ...,
        topics_dir: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partnerConnectorType")
    def partner_connector_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="apiSecret")
    def api_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="flushSize")
    def flush_size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputFormat")
    def input_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxTasks")
    def max_tasks(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputFormat")
    def output_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeInterval")
    def time_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topics(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="topicsDir")
    def topics_dir(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MetadataEntityResponse(dict):
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        deleted_at: Optional[_builtins.str] = ...,
        resource_name: Optional[_builtins.str] = ...,
        self: Optional[_builtins.str] = ...,
        updated_at: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletedAt")
    def deleted_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OfferDetailResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        plan_id: _builtins.str,
        plan_name: _builtins.str,
        publisher_id: _builtins.str,
        term_unit: _builtins.str,
        private_offer_id: Optional[_builtins.str] = ...,
        private_offer_ids: Optional[Sequence[_builtins.str]] = ...,
        status: Optional[_builtins.str] = ...,
        term_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="planName")
    def plan_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="termUnit")
    def term_unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateOfferId")
    def private_offer_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateOfferIds")
    def private_offer_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="termId")
    def term_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RegionRecordResponse(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
        metadata: Optional[outputs.SCMetadataEntityResponse] = ...,
        spec: Optional[outputs.RegionSpecEntityResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.SCMetadataEntityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[outputs.RegionSpecEntityResponse]: ...

@pulumi.output_type
class RegionSpecEntityResponse(dict):
    def __init__(
        __self__,
        *,
        cloud: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        packages: Optional[Sequence[_builtins.str]] = ...,
        region_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cloud(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def packages(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RoleBindingRecordResponse(dict):
    def __init__(
        __self__,
        *,
        crn_pattern: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
        metadata: Optional[outputs.MetadataEntityResponse] = ...,
        principal: Optional[_builtins.str] = ...,
        role_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crnPattern")
    def crn_pattern(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.MetadataEntityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SCClusterByokEntityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        related: Optional[_builtins.str] = ...,
        resource_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def related(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SCClusterNetworkEnvironmentEntityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        environment: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        related: Optional[_builtins.str] = ...,
        resource_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def related(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SCClusterSpecEntityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_endpoint: Optional[_builtins.str] = ...,
        availability: Optional[_builtins.str] = ...,
        byok: Optional[outputs.SCClusterByokEntityResponse] = ...,
        cloud: Optional[_builtins.str] = ...,
        config: Optional[outputs.ClusterConfigEntityResponse] = ...,
        environment: Optional[outputs.SCClusterNetworkEnvironmentEntityResponse] = ...,
        http_endpoint: Optional[_builtins.str] = ...,
        kafka_bootstrap_endpoint: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        network: Optional[outputs.SCClusterNetworkEnvironmentEntityResponse] = ...,
        package: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def availability(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def byok(self) -> Optional[outputs.SCClusterByokEntityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def cloud(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[outputs.ClusterConfigEntityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def environment(
        self,
    ) -> Optional[outputs.SCClusterNetworkEnvironmentEntityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kafkaBootstrapEndpoint")
    def kafka_bootstrap_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(
        self,
    ) -> Optional[outputs.SCClusterNetworkEnvironmentEntityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def package(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SCMetadataEntityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_timestamp: Optional[_builtins.str] = ...,
        deleted_timestamp: Optional[_builtins.str] = ...,
        resource_name: Optional[_builtins.str] = ...,
        self: Optional[_builtins.str] = ...,
        updated_timestamp: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletedTimestamp")
    def deleted_timestamp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceAccountRecordResponse(dict):
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
        metadata: Optional[outputs.MetadataEntityResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.MetadataEntityResponse]: ...

@pulumi.output_type
class StreamGovernanceConfigResponse(dict):
    def __init__(__self__, *, package: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def package(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TopicMetadataEntityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_name: Optional[_builtins.str] = ...,
        self: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def self(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TopicsInputConfigResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TopicsRelatedLinkResponse(dict):
    def __init__(__self__, *, related: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def related(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserDetailResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        email_address: _builtins.str,
        aad_email: Optional[_builtins.str] = ...,
        first_name: Optional[_builtins.str] = ...,
        last_name: Optional[_builtins.str] = ...,
        user_principal_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="aadEmail")
    def aad_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserRecordResponse(dict):
    def __init__(
        __self__,
        *,
        auth_type: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        full_name: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
        metadata: Optional[outputs.MetadataEntityResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fullName")
    def full_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.MetadataEntityResponse]: ...
