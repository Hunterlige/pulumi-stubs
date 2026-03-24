

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AntivirusRulesetResponse', 'ApiFlowOptionsResponse', 'ArchiveRulesetResponse', 'ConnectionPropertiesResponse', 'DataSizeRulesetResponse', 'FlowProfileMetadataResponse', 'FlowProfilePropertiesResponse', 'FlowProfileRulesetsResponse', 'FlowPropertiesResponse', 'FlowPropertiesResponseV1', 'FlowResponse', 'InternalMetadataPropertiesResponse', 'ListFlowsByPipelineConnectionResponse', 'ManagedServiceIdentityResponse', 'MessagingOptionsResponse', 'MimeFilterRulesetResponse', 'MimeTypeFilterResponse', 'OperationStatusPropertiesResponse', 'PendingConnectionResponse', 'PendingFlowResponse', 'PipelineConnectionResponse', 'PipelineConnectionResponseProperties', 'PipelinePropertiesResponse', 'PlanResponse', 'SchemaResponse', 'SelectedResourceResponse', 'StreamSourceAddressesResponse', 'SubscriberResponse', 'SystemDataResponse', 'TextMatchResponse', 'TextMatchingRulesetResponse', 'UserAssignedIdentityResponse', 'XmlFilterRulesetResponse']
@pulumi.output_type
class AntivirusRulesetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, av_solutions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avSolutions")
    def av_solutions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ApiFlowOptionsResponse(dict):
    
    def __init__(__self__, *, api_mode: Optional[_builtins.str] = ..., audience_override: Optional[_builtins.str] = ..., cname: Optional[_builtins.str] = ..., identity_translation: Optional[_builtins.str] = ..., remote_calling_mode_client_id: Optional[_builtins.str] = ..., remote_endpoint: Optional[_builtins.str] = ..., sender_client_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiMode")
    def api_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audienceOverride")
    def audience_override(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cname(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityTranslation")
    def identity_translation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteCallingModeClientId")
    def remote_calling_mode_client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteEndpoint")
    def remote_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderClientId")
    def sender_client_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ArchiveRulesetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, maximum_compression_ratio_limit: Optional[_builtins.float] = ..., maximum_depth_limit: Optional[_builtins.float] = ..., maximum_expansion_size_limit: Optional[_builtins.float] = ..., minimum_size_for_expansion: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumCompressionRatioLimit")
    def maximum_compression_ratio_limit(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumDepthLimit")
    def maximum_depth_limit(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumExpansionSizeLimit")
    def maximum_expansion_size_limit(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumSizeForExpansion")
    def minimum_size_for_expansion(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ConnectionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, approver: _builtins.str, date_submitted: _builtins.str, link_status: _builtins.str, linked_connection_id: _builtins.str, pipeline: _builtins.str, provisioning_state: _builtins.str, status: _builtins.str, status_reason: _builtins.str, direction: Optional[_builtins.str] = ..., flow_types: Optional[Sequence[_builtins.str]] = ..., justification: Optional[_builtins.str] = ..., pin: Optional[_builtins.str] = ..., policies: Optional[Sequence[_builtins.str]] = ..., primary_contact: Optional[_builtins.str] = ..., remote_subscription_id: Optional[_builtins.str] = ..., requirement_id: Optional[_builtins.str] = ..., schema_uris: Optional[Sequence[_builtins.str]] = ..., schemas: Optional[Sequence[outputs.SchemaResponse]] = ..., secondary_contacts: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def approver(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateSubmitted")
    def date_submitted(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkStatus")
    def link_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedConnectionId")
    def linked_connection_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pipeline(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowTypes")
    def flow_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def justification(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pin(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteSubscriptionId")
    def remote_subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requirementId")
    def requirement_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaUris")
    def schema_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schemas(self) -> Optional[Sequence[outputs.SchemaResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryContacts")
    def secondary_contacts(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class DataSizeRulesetResponse(dict):
    
    def __init__(__self__, *, maximum: Optional[_builtins.float] = ..., minimum: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class FlowProfileMetadataResponse(dict):
    
    def __init__(__self__, *, description: _builtins.str, flow_profile_id: _builtins.str, name: _builtins.str, pipeline: _builtins.str, replication_scenario: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowProfileId")
    def flow_profile_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pipeline(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationScenario")
    def replication_scenario(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FlowProfilePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: _builtins.str, flow_profile_id: _builtins.str, provisioning_state: _builtins.str, replication_scenario: _builtins.str, status: _builtins.str, rulesets: Optional[outputs.FlowProfileRulesetsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowProfileId")
    def flow_profile_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationScenario")
    def replication_scenario(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rulesets(self) -> Optional[outputs.FlowProfileRulesetsResponse]:
        
        ...
    


@pulumi.output_type
class FlowProfileRulesetsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, antivirus: Optional[outputs.AntivirusRulesetResponse] = ..., archives: Optional[outputs.ArchiveRulesetResponse] = ..., data_size: Optional[outputs.DataSizeRulesetResponse] = ..., mime_filters: Optional[outputs.MimeFilterRulesetResponse] = ..., text_matching: Optional[outputs.TextMatchingRulesetResponse] = ..., xml_filters: Optional[outputs.XmlFilterRulesetResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def antivirus(self) -> Optional[outputs.AntivirusRulesetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def archives(self) -> Optional[outputs.ArchiveRulesetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSize")
    def data_size(self) -> Optional[outputs.DataSizeRulesetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mimeFilters")
    def mime_filters(self) -> Optional[outputs.MimeFilterRulesetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textMatching")
    def text_matching(self) -> Optional[outputs.TextMatchingRulesetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="xmlFilters")
    def xml_filters(self) -> Optional[outputs.XmlFilterRulesetResponse]:
        
        ...
    


@pulumi.output_type
class FlowPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, flow_id: _builtins.str, link_status: _builtins.str, linked_flow_id: _builtins.str, provisioning_state: _builtins.str, connection: Optional[outputs.SelectedResourceResponse] = ..., customer_managed_key_vault_uri: Optional[_builtins.str] = ..., data_type: Optional[_builtins.str] = ..., destination_endpoint_ports: Optional[Sequence[_builtins.float]] = ..., destination_endpoints: Optional[Sequence[_builtins.str]] = ..., flow_type: Optional[_builtins.str] = ..., key_vault_uri: Optional[_builtins.str] = ..., messaging_options: Optional[outputs.MessagingOptionsResponse] = ..., passphrase: Optional[_builtins.str] = ..., policies: Optional[Sequence[_builtins.str]] = ..., schema: Optional[outputs.SchemaResponse] = ..., service_bus_queue_id: Optional[_builtins.str] = ..., source_addresses: Optional[outputs.StreamSourceAddressesResponse] = ..., status: Optional[_builtins.str] = ..., storage_account_id: Optional[_builtins.str] = ..., storage_account_name: Optional[_builtins.str] = ..., storage_container_name: Optional[_builtins.str] = ..., stream_id: Optional[_builtins.str] = ..., stream_latency: Optional[_builtins.float] = ..., stream_protocol: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowId")
    def flow_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkStatus")
    def link_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedFlowId")
    def linked_flow_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connection(self) -> Optional[outputs.SelectedResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyVaultUri")
    def customer_managed_key_vault_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationEndpointPorts")
    def destination_endpoint_ports(self) -> Optional[Sequence[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationEndpoints")
    def destination_endpoints(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowType")
    def flow_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messagingOptions")
    def messaging_options(self) -> Optional[outputs.MessagingOptionsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[outputs.SchemaResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusQueueId")
    def service_bus_queue_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[outputs.StreamSourceAddressesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerName")
    def storage_container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamId")
    def stream_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamLatency")
    def stream_latency(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamProtocol")
    def stream_protocol(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlowPropertiesResponseV1(dict):
    
    def __init__(__self__, *, flow_id: _builtins.str, force_disabled_status: Sequence[_builtins.str], link_status: _builtins.str, linked_flow_id: _builtins.str, provisioning_state: _builtins.str, api_flow_options: Optional[outputs.ApiFlowOptionsResponse] = ..., connection: Optional[outputs.SelectedResourceResponse] = ..., consumer_group: Optional[_builtins.str] = ..., customer_managed_key_vault_uri: Optional[_builtins.str] = ..., data_type: Optional[_builtins.str] = ..., destination_endpoint_ports: Optional[Sequence[_builtins.float]] = ..., destination_endpoints: Optional[Sequence[_builtins.str]] = ..., event_hub_id: Optional[_builtins.str] = ..., flow_type: Optional[_builtins.str] = ..., key_vault_uri: Optional[_builtins.str] = ..., messaging_options: Optional[outputs.MessagingOptionsResponse] = ..., passphrase: Optional[_builtins.str] = ..., policies: Optional[Sequence[_builtins.str]] = ..., schema: Optional[outputs.SchemaResponse] = ..., service_bus_queue_id: Optional[_builtins.str] = ..., source_addresses: Optional[outputs.StreamSourceAddressesResponse] = ..., status: Optional[_builtins.str] = ..., storage_account_id: Optional[_builtins.str] = ..., storage_account_name: Optional[_builtins.str] = ..., storage_container_name: Optional[_builtins.str] = ..., storage_table_name: Optional[_builtins.str] = ..., stream_id: Optional[_builtins.str] = ..., stream_latency: Optional[_builtins.float] = ..., stream_protocol: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowId")
    def flow_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDisabledStatus")
    def force_disabled_status(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkStatus")
    def link_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedFlowId")
    def linked_flow_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiFlowOptions")
    def api_flow_options(self) -> Optional[outputs.ApiFlowOptionsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connection(self) -> Optional[outputs.SelectedResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyVaultUri")
    def customer_managed_key_vault_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationEndpointPorts")
    def destination_endpoint_ports(self) -> Optional[Sequence[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationEndpoints")
    def destination_endpoints(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubId")
    def event_hub_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowType")
    def flow_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messagingOptions")
    def messaging_options(self) -> Optional[outputs.MessagingOptionsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[outputs.SchemaResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusQueueId")
    def service_bus_queue_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[outputs.StreamSourceAddressesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerName")
    def storage_container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageTableName")
    def storage_table_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamId")
    def stream_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamLatency")
    def stream_latency(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamProtocol")
    def stream_protocol(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FlowResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, location: _builtins.str, name: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, identity: Optional[outputs.ManagedServiceIdentityResponse] = ..., plan: Optional[outputs.PlanResponse] = ..., properties: Optional[outputs.FlowPropertiesResponseV1] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[outputs.PlanResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.FlowPropertiesResponseV1]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class InternalMetadataPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, status_set_by: _builtins.str, operation_status: Optional[outputs.OperationStatusPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusSetBy")
    def status_set_by(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationStatus")
    def operation_status(self) -> Optional[outputs.OperationStatusPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class ListFlowsByPipelineConnectionResponse(dict):
    
    def __init__(__self__, *, flows: Optional[Sequence[outputs.FlowResponse]] = ..., id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flows(self) -> Optional[Sequence[outputs.FlowResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: _builtins.str, user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedIdentityResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class MessagingOptionsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, billing_tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingTier")
    def billing_tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MimeFilterRulesetResponse(dict):
    
    def __init__(__self__, *, filters: Optional[Sequence[outputs.MimeTypeFilterResponse]] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.MimeTypeFilterResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MimeTypeFilterResponse(dict):
    
    def __init__(__self__, *, extensions: Optional[Sequence[_builtins.str]] = ..., media: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def extensions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def media(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OperationStatusPropertiesResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, message: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PendingConnectionResponse(dict):
    
    def __init__(__self__, *, approver: _builtins.str, date_submitted: _builtins.str, id: _builtins.str, link_status: _builtins.str, linked_connection_id: _builtins.str, location: _builtins.str, name: _builtins.str, pipeline: _builtins.str, provisioning_state: _builtins.str, status: _builtins.str, status_reason: _builtins.str, subscription_id: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, direction: Optional[_builtins.str] = ..., flow_types: Optional[Sequence[_builtins.str]] = ..., justification: Optional[_builtins.str] = ..., pin: Optional[_builtins.str] = ..., policies: Optional[Sequence[_builtins.str]] = ..., primary_contact: Optional[_builtins.str] = ..., remote_subscription_id: Optional[_builtins.str] = ..., requirement_id: Optional[_builtins.str] = ..., schema_uris: Optional[Sequence[_builtins.str]] = ..., schemas: Optional[Sequence[outputs.SchemaResponse]] = ..., secondary_contacts: Optional[Sequence[_builtins.str]] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def approver(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateSubmitted")
    def date_submitted(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkStatus")
    def link_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedConnectionId")
    def linked_connection_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pipeline(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowTypes")
    def flow_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def justification(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pin(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteSubscriptionId")
    def remote_subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requirementId")
    def requirement_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaUris")
    def schema_uris(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schemas(self) -> Optional[Sequence[outputs.SchemaResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryContacts")
    def secondary_contacts(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class PendingFlowResponse(dict):
    
    def __init__(__self__, *, connection_id: _builtins.str, flow_id: _builtins.str, id: _builtins.str, link_status: _builtins.str, linked_flow_id: _builtins.str, location: _builtins.str, name: _builtins.str, provisioning_state: _builtins.str, subscription_id: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, connection: Optional[outputs.SelectedResourceResponse] = ..., customer_managed_key_vault_uri: Optional[_builtins.str] = ..., data_type: Optional[_builtins.str] = ..., destination_endpoint_ports: Optional[Sequence[_builtins.float]] = ..., destination_endpoints: Optional[Sequence[_builtins.str]] = ..., flow_type: Optional[_builtins.str] = ..., key_vault_uri: Optional[_builtins.str] = ..., messaging_options: Optional[outputs.MessagingOptionsResponse] = ..., passphrase: Optional[_builtins.str] = ..., policies: Optional[Sequence[_builtins.str]] = ..., schema: Optional[outputs.SchemaResponse] = ..., service_bus_queue_id: Optional[_builtins.str] = ..., source_addresses: Optional[outputs.StreamSourceAddressesResponse] = ..., status: Optional[_builtins.str] = ..., storage_account_id: Optional[_builtins.str] = ..., storage_account_name: Optional[_builtins.str] = ..., storage_container_name: Optional[_builtins.str] = ..., stream_id: Optional[_builtins.str] = ..., stream_latency: Optional[_builtins.float] = ..., stream_protocol: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowId")
    def flow_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkStatus")
    def link_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedFlowId")
    def linked_flow_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connection(self) -> Optional[outputs.SelectedResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyVaultUri")
    def customer_managed_key_vault_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationEndpointPorts")
    def destination_endpoint_ports(self) -> Optional[Sequence[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationEndpoints")
    def destination_endpoints(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowType")
    def flow_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messagingOptions")
    def messaging_options(self) -> Optional[outputs.MessagingOptionsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[outputs.SchemaResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBusQueueId")
    def service_bus_queue_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[outputs.StreamSourceAddressesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerName")
    def storage_container_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamId")
    def stream_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamLatency")
    def stream_latency(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamProtocol")
    def stream_protocol(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class PipelineConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, location: _builtins.str, name: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, properties: Optional[outputs.PipelineConnectionResponseProperties] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.PipelineConnectionResponseProperties]:
        
        ...
    


@pulumi.output_type
class PipelineConnectionResponseProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, internal_metadata: Optional[outputs.InternalMetadataPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalMetadata")
    def internal_metadata(self) -> Optional[outputs.InternalMetadataPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class PipelinePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connections: Sequence[outputs.PipelineConnectionResponse], provisioning_state: _builtins.str, remote_cloud: _builtins.str, display_name: Optional[_builtins.str] = ..., flow_types: Optional[Sequence[_builtins.str]] = ..., policies: Optional[Sequence[_builtins.str]] = ..., subscribers: Optional[Sequence[outputs.SubscriberResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connections(self) -> Sequence[outputs.PipelineConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteCloud")
    def remote_cloud(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowTypes")
    def flow_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscribers(self) -> Optional[Sequence[outputs.SubscriberResponse]]:
        
        ...
    


@pulumi.output_type
class PlanResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, product: _builtins.str, publisher: _builtins.str, promotion_code: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def product(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SchemaResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_id: Optional[_builtins.str] = ..., content: Optional[_builtins.str] = ..., direction: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., schema_type: Optional[_builtins.str] = ..., schema_uri: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaUri")
    def schema_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SelectedResourceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., subscription_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StreamSourceAddressesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_addresses: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAddresses")
    def source_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class SubscriberResponse(dict):
    def __init__(__self__, *, email: Optional[_builtins.str] = ..., notifications: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TextMatchResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, case_sensitivity: Optional[_builtins.str] = ..., match_type: Optional[_builtins.str] = ..., text: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caseSensitivity")
    def case_sensitivity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchType")
    def match_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TextMatchingRulesetResponse(dict):
    
    def __init__(__self__, *, deny: Optional[Sequence[outputs.TextMatchResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deny(self) -> Optional[Sequence[outputs.TextMatchResponse]]:
        
        ...
    


@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, principal_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class XmlFilterRulesetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_namespace: Optional[_builtins.str] = ..., reference: Optional[_builtins.str] = ..., schema: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultNamespace")
    def default_namespace(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reference(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[_builtins.str]:
        
        ...
    


