import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessModeSettingsExclusionResponse",
    "AccessModeSettingsResponse",
    "ActionGroupResponse",
    "ActionListResponse",
    "ActionsResponse",
    "AlertConfigurationResponse",
    "AlertRuleAllOfConditionResponse",
    "AlertRuleAnyOfOrLeafConditionResponse",
    "AlertRuleLeafConditionResponse",
    ...,
    "ArmRoleReceiverResponse",
    "AutomationRunbookReceiverResponse",
    "AutoscaleNotificationResponse",
    "AutoscaleProfileResponse",
    "AutoscaleSettingResponse",
    "AzureAppPushReceiverResponse",
    "AzureFunctionReceiverResponse",
    "AzureMonitorWorkspaceLogsApiConfigResponse",
    "AzureMonitorWorkspaceLogsExporterResponse",
    ...,
    "AzureMonitorWorkspaceResponseMetrics",
    "AzureMonitorWorkspaceSignalGroupResponse",
    ...,
    "AzureResourceSignalGroupResponse",
    "BatchProcessorResponse",
    "CacheConfigurationResponse",
    "ColumnDefinitionResponse",
    "ConcurrencyConfigurationResponse",
    "ConditionResponse",
    "ConditionResponseFailingPeriods",
    "DataCollectionEndpointResourceResponseIdentity",
    "DataCollectionEndpointResourceResponseSystemData",
    "DataCollectionEndpointResponseConfigurationAccess",
    ...,
    "DataCollectionEndpointResponseLogsIngestion",
    "DataCollectionEndpointResponseMetadata",
    "DataCollectionEndpointResponseMetricsIngestion",
    "DataCollectionEndpointResponseNetworkAcls",
    ...,
    "DataCollectionRuleAssociationResponseMetadata",
    "DataCollectionRuleResourceResponseIdentity",
    "DataCollectionRuleResourceResponseSystemData",
    "DataCollectionRuleResponseDataSources",
    "DataCollectionRuleResponseDestinations",
    "DataCollectionRuleResponseMetadata",
    "DataFlowResponse",
    "DataImportSourcesResponseEventHub",
    "DataSourcesSpecResponseDataImports",
    "DependenciesSignalGroupResponse",
    "DestinationsSpecResponseAzureMonitorMetrics",
    "DiagnosticSettingsCategoryResourceResponse",
    "DimensionResponse",
    "DiscoveryErrorResponse",
    "DynamicDetectionRuleResponse",
    "DynamicMetricCriteriaResponse",
    "DynamicThresholdFailingPeriodsResponse",
    "EmailNotificationResponse",
    "EmailReceiverResponse",
    "EntityAlertsResponse",
    "EntityCoordinatesResponse",
    "EntityPropertiesResponse",
    "EvaluationRuleResponse",
    "EventHubDestinationResponse",
    "EventHubDirectDestinationResponse",
    "EventHubReceiverResponse",
    "ExporterResponse",
    "ExtensionDataSourceResponse",
    "HealthModelPropertiesResponse",
    "IconDefinitionResponse",
    "IdentityResponse",
    "IisLogsDataSourceResponse",
    "IncidentReceiverResponse",
    "IncidentServiceConnectionResponse",
    "InvestigationExecutionResponse",
    "InvestigationMetadataResponse",
    "InvestigationScopeResponse",
    "IssuePropertiesResponse",
    "ItsmReceiverResponse",
    "JsonArrayMapperResponse",
    "JsonMapperDestinationFieldResponse",
    "JsonMapperSourceFieldResponse",
    "LocationSpecResponse",
    "LogAnalyticsDestinationResponse",
    ...,
    "LogAnalyticsSignalGroupResponse",
    "LogFileSettingsResponseText",
    "LogFilesDataSourceResponse",
    "LogFilesDataSourceResponseSettings",
    "LogSettingsResponse",
    "LogicAppReceiverResponse",
    ...,
    "ManagedServiceIdentityResponse",
    "ManagementGroupLogSettingsResponse",
    "MetricAlertActionResponse",
    ...,
    ...,
    "MetricCriteriaResponse",
    "MetricDimensionResponse",
    "MetricSettingsResponse",
    "MetricTriggerResponse",
    "ModelDiscoverySettingsResponse",
    "MonitoringAccountDestinationResponse",
    "NetworkingConfigurationResponse",
    "NetworkingRouteResponse",
    "OriginResponse",
    "OtlpReceiverResponse",
    "PerfCounterDataSourceResponse",
    "PersistenceConfigurationsResponse",
    "PipelineGroupPropertiesResponse",
    "PipelineResponse",
    "PlatformTelemetryDataSourceResponse",
    "PredictiveAutoscalePolicyResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointConnectionResponseV1",
    "PrivateEndpointResponse",
    "PrivateLinkScopedResourceResponse",
    "PrivateLinkServiceConnectionStateResponse",
    "ProcessorResponse",
    "PrometheusForwarderDataSourceResponse",
    ...,
    "ReceiverResponse",
    "RecordMapResponse",
    "RecurrenceResponse",
    "RecurrentScheduleResponse",
    "RelatedAlertResponse",
    "RelatedResourceResponse",
    "RelationshipPropertiesResponse",
    "ResourceGraphQueryDiscoveryRulePropertiesResponse",
    "ResourceMapResponse",
    "ResourceMetricSignalDefinitionPropertiesResponse",
    "RetentionPolicyResponse",
    "RuleResolveConfigurationResponse",
    "RunParametersResponse",
    "ScaleActionResponse",
    "ScaleCapacityResponse",
    "ScaleRuleMetricDimensionResponse",
    "ScaleRuleResponse",
    "ScheduledQueryRuleCriteriaResponse",
    "SchemaMapResponse",
    "ScopeMapResponse",
    "ServiceResponse",
    "SignalAssignmentResponse",
    "SignalGroupResponse",
    "SmsReceiverResponse",
    "StorageBlobDestinationResponse",
    "StorageTableDestinationResponse",
    "StreamDeclarationResponse",
    "SubscriptionLogSettingsResponse",
    "SyslogDataSourceResponse",
    "SyslogReceiverResponse",
    "SystemDataResponse",
    "TcpExporterResponse",
    "ThresholdRuleResponse",
    "TimeWindowResponse",
    "UdpReceiverResponse",
    "UserAssignedIdentityResponse",
    "UserIdentityPropertiesResponse",
    "VoiceReceiverResponse",
    "WebhookNotificationResponse",
    "WebhookReceiverResponse",
    "WebhookReceiverResponseV1",
    "WebtestLocationAvailabilityCriteriaResponse",
    "WindowsEventLogDataSourceResponse",
    "WindowsFirewallLogsDataSourceResponse",
]

@pulumi.output_type
class AccessModeSettingsExclusionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ingestion_access_mode: Optional[_builtins.str] = ...,
        private_endpoint_connection_name: Optional[_builtins.str] = ...,
        query_access_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingestionAccessMode")
    def ingestion_access_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnectionName")
    def private_endpoint_connection_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryAccessMode")
    def query_access_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AccessModeSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ingestion_access_mode: _builtins.str,
        query_access_mode: _builtins.str,
        exclusions: Optional[
            Sequence[outputs.AccessModeSettingsExclusionResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingestionAccessMode")
    def ingestion_access_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryAccessMode")
    def query_access_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[Sequence[outputs.AccessModeSettingsExclusionResponse]]: ...

@pulumi.output_type
class ActionGroupResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_group_id: _builtins.str,
        webhook_properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="webhookProperties")
    def webhook_properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ActionListResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_groups: Optional[Sequence[outputs.ActionGroupResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroups")
    def action_groups(self) -> Optional[Sequence[outputs.ActionGroupResponse]]: ...

@pulumi.output_type
class ActionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_groups: Optional[Sequence[_builtins.str]] = ...,
        action_properties: Optional[Mapping[str, _builtins.str]] = ...,
        custom_properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroups")
    def action_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="actionProperties")
    def action_properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class AlertConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        severity: _builtins.str,
        action_group_ids: Optional[Sequence[_builtins.str]] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="actionGroupIds")
    def action_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AlertRuleAllOfConditionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, all_of: Sequence[outputs.AlertRuleAnyOfOrLeafConditionResponse]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allOf")
    def all_of(self) -> Sequence[outputs.AlertRuleAnyOfOrLeafConditionResponse]: ...

@pulumi.output_type
class AlertRuleAnyOfOrLeafConditionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        any_of: Optional[Sequence[outputs.AlertRuleLeafConditionResponse]] = ...,
        contains_any: Optional[Sequence[_builtins.str]] = ...,
        equals: Optional[_builtins.str] = ...,
        field: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[Sequence[outputs.AlertRuleLeafConditionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="containsAny")
    def contains_any(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def equals(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AlertRuleLeafConditionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        contains_any: Optional[Sequence[_builtins.str]] = ...,
        equals: Optional[_builtins.str] = ...,
        field: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containsAny")
    def contains_any(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def equals(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationInsightsTopologyDiscoveryRulePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        add_recommended_signals: _builtins.str,
        application_insights_resource_id: _builtins.str,
        authentication_setting: _builtins.str,
        deletion_date: _builtins.str,
        discover_relationships: _builtins.str,
        discovery_rule_kind: _builtins.str,
        entity_name: _builtins.str,
        error: outputs.DiscoveryErrorResponse,
        provisioning_state: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addRecommendedSignals")
    def add_recommended_signals(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applicationInsightsResourceId")
    def application_insights_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationSetting")
    def authentication_setting(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionDate")
    def deletion_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="discoverRelationships")
    def discover_relationships(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="discoveryRuleKind")
    def discovery_rule_kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.DiscoveryErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ArmRoleReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        role_id: _builtins.str,
        use_common_alert_schema: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleId")
    def role_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AutomationRunbookReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        automation_account_id: _builtins.str,
        is_global_runbook: _builtins.bool,
        runbook_name: _builtins.str,
        webhook_resource_id: _builtins.str,
        managed_identity: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        service_uri: Optional[_builtins.str] = ...,
        use_common_alert_schema: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automationAccountId")
    def automation_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isGlobalRunbook")
    def is_global_runbook(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="runbookName")
    def runbook_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="webhookResourceId")
    def webhook_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AutoscaleNotificationResponse(dict):
    def __init__(
        __self__,
        *,
        operation: _builtins.str,
        email: Optional[outputs.EmailNotificationResponse] = ...,
        webhooks: Optional[Sequence[outputs.WebhookNotificationResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[outputs.EmailNotificationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def webhooks(self) -> Optional[Sequence[outputs.WebhookNotificationResponse]]: ...

@pulumi.output_type
class AutoscaleProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity: outputs.ScaleCapacityResponse,
        name: _builtins.str,
        rules: Sequence[outputs.ScaleRuleResponse],
        fixed_date: Optional[outputs.TimeWindowResponse] = ...,
        recurrence: Optional[outputs.RecurrenceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> outputs.ScaleCapacityResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.ScaleRuleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="fixedDate")
    def fixed_date(self) -> Optional[outputs.TimeWindowResponse]: ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[outputs.RecurrenceResponse]: ...

@pulumi.output_type
class AutoscaleSettingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        profiles: Sequence[outputs.AutoscaleProfileResponse],
        enabled: Optional[_builtins.bool] = ...,
        name: Optional[_builtins.str] = ...,
        notifications: Optional[Sequence[outputs.AutoscaleNotificationResponse]] = ...,
        predictive_autoscale_policy: Optional[
            outputs.PredictiveAutoscalePolicyResponse
        ] = ...,
        target_resource_location: Optional[_builtins.str] = ...,
        target_resource_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def profiles(self) -> Sequence[outputs.AutoscaleProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def notifications(
        self,
    ) -> Optional[Sequence[outputs.AutoscaleNotificationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="predictiveAutoscalePolicy")
    def predictive_autoscale_policy(
        self,
    ) -> Optional[outputs.PredictiveAutoscalePolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceLocation")
    def target_resource_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceUri")
    def target_resource_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureAppPushReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, email_address: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class AzureFunctionReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        function_app_resource_id: _builtins.str,
        function_name: _builtins.str,
        http_trigger_url: _builtins.str,
        name: _builtins.str,
        managed_identity: Optional[_builtins.str] = ...,
        use_common_alert_schema: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionAppResourceId")
    def function_app_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="httpTriggerUrl")
    def http_trigger_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AzureMonitorWorkspaceLogsApiConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_collection_endpoint_url: _builtins.str,
        data_collection_rule: _builtins.str,
        schema: outputs.SchemaMapResponse,
        stream: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionEndpointUrl")
    def data_collection_endpoint_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionRule")
    def data_collection_rule(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> outputs.SchemaMapResponse: ...
    @_builtins.property
    @pulumi.getter
    def stream(self) -> _builtins.str: ...

@pulumi.output_type
class AzureMonitorWorkspaceLogsExporterResponse(dict):
    def __init__(
        __self__,
        *,
        api: outputs.AzureMonitorWorkspaceLogsApiConfigResponse,
        cache: Optional[outputs.CacheConfigurationResponse] = ...,
        concurrency: Optional[outputs.ConcurrencyConfigurationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def api(self) -> outputs.AzureMonitorWorkspaceLogsApiConfigResponse: ...
    @_builtins.property
    @pulumi.getter
    def cache(self) -> Optional[outputs.CacheConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def concurrency(self) -> Optional[outputs.ConcurrencyConfigurationResponse]: ...

@pulumi.output_type
class AzureMonitorWorkspaceResponseDefaultIngestionSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_collection_endpoint_resource_id: _builtins.str,
        data_collection_rule_resource_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionEndpointResourceId")
    def data_collection_endpoint_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionRuleResourceId")
    def data_collection_rule_resource_id(self) -> _builtins.str: ...

@pulumi.output_type
class AzureMonitorWorkspaceResponseMetrics(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        internal_id: _builtins.str,
        prometheus_query_endpoint: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="prometheusQueryEndpoint")
    def prometheus_query_endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class AzureMonitorWorkspaceSignalGroupResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authentication_setting: _builtins.str,
        azure_monitor_workspace_resource_id: _builtins.str,
        signal_assignments: Optional[Sequence[outputs.SignalAssignmentResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationSetting")
    def authentication_setting(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorWorkspaceResourceId")
    def azure_monitor_workspace_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signalAssignments")
    def signal_assignments(
        self,
    ) -> Optional[Sequence[outputs.SignalAssignmentResponse]]: ...

@pulumi.output_type
class AzureResourceManagerCommonTypesExtendedLocationResponse(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AzureResourceSignalGroupResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authentication_setting: _builtins.str,
        azure_resource_id: _builtins.str,
        signal_assignments: Optional[Sequence[outputs.SignalAssignmentResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationSetting")
    def authentication_setting(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureResourceId")
    def azure_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signalAssignments")
    def signal_assignments(
        self,
    ) -> Optional[Sequence[outputs.SignalAssignmentResponse]]: ...

@pulumi.output_type
class BatchProcessorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        batch_size: Optional[_builtins.int] = ...,
        timeout: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CacheConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_storage_usage: Optional[_builtins.int] = ...,
        retention_period: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxStorageUsage")
    def max_storage_usage(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ColumnDefinitionResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConcurrencyConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        batch_queue_size: Optional[_builtins.int] = ...,
        worker_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchQueueSize")
    def batch_queue_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ConditionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        alert_sensitivity: Optional[_builtins.str] = ...,
        criterion_type: Optional[_builtins.str] = ...,
        dimensions: Optional[Sequence[outputs.DimensionResponse]] = ...,
        failing_periods: Optional[outputs.ConditionResponseFailingPeriods] = ...,
        ignore_data_before: Optional[_builtins.str] = ...,
        metric_measure_column: Optional[_builtins.str] = ...,
        metric_name: Optional[_builtins.str] = ...,
        min_recurrence_count: Optional[_builtins.float] = ...,
        operator: Optional[_builtins.str] = ...,
        query: Optional[_builtins.str] = ...,
        resource_id_column: Optional[_builtins.str] = ...,
        threshold: Optional[_builtins.float] = ...,
        time_aggregation: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alertSensitivity")
    def alert_sensitivity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="criterionType")
    def criterion_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence[outputs.DimensionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="failingPeriods")
    def failing_periods(self) -> Optional[outputs.ConditionResponseFailingPeriods]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreDataBefore")
    def ignore_data_before(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricMeasureColumn")
    def metric_measure_column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minRecurrenceCount")
    def min_recurrence_count(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceIdColumn")
    def resource_id_column(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="timeAggregation")
    def time_aggregation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConditionResponseFailingPeriods(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        min_failing_periods_to_alert: Optional[_builtins.float] = ...,
        number_of_evaluation_periods: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minFailingPeriodsToAlert")
    def min_failing_periods_to_alert(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfEvaluationPeriods")
    def number_of_evaluation_periods(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class DataCollectionEndpointResourceResponseIdentity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class DataCollectionEndpointResourceResponseSystemData(dict):
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
class DataCollectionEndpointResponseConfigurationAccess(dict):
    def __init__(__self__, *, endpoint: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class DataCollectionEndpointResponseFailoverConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        active_location: Optional[_builtins.str] = ...,
        locations: Optional[Sequence[outputs.LocationSpecResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeLocation")
    def active_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[outputs.LocationSpecResponse]]: ...

@pulumi.output_type
class DataCollectionEndpointResponseLogsIngestion(dict):
    def __init__(__self__, *, endpoint: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class DataCollectionEndpointResponseMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioned_by: _builtins.str,
        provisioned_by_resource_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisionedBy")
    def provisioned_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisionedByResourceId")
    def provisioned_by_resource_id(self) -> _builtins.str: ...

@pulumi.output_type
class DataCollectionEndpointResponseMetricsIngestion(dict):
    def __init__(__self__, *, endpoint: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class DataCollectionEndpointResponseNetworkAcls(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, public_network_access: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataCollectionRuleAssociationProxyOnlyResourceResponseSystemData(dict):
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
class DataCollectionRuleAssociationResponseMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioned_by: _builtins.str,
        provisioned_by_resource_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisionedBy")
    def provisioned_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisionedByResourceId")
    def provisioned_by_resource_id(self) -> _builtins.str: ...

@pulumi.output_type
class DataCollectionRuleResourceResponseIdentity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class DataCollectionRuleResourceResponseSystemData(dict):
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
class DataCollectionRuleResponseDataSources(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_imports: Optional[outputs.DataSourcesSpecResponseDataImports] = ...,
        extensions: Optional[Sequence[outputs.ExtensionDataSourceResponse]] = ...,
        iis_logs: Optional[Sequence[outputs.IisLogsDataSourceResponse]] = ...,
        log_files: Optional[Sequence[outputs.LogFilesDataSourceResponse]] = ...,
        performance_counters: Optional[
            Sequence[outputs.PerfCounterDataSourceResponse]
        ] = ...,
        platform_telemetry: Optional[
            Sequence[outputs.PlatformTelemetryDataSourceResponse]
        ] = ...,
        prometheus_forwarder: Optional[
            Sequence[outputs.PrometheusForwarderDataSourceResponse]
        ] = ...,
        syslog: Optional[Sequence[outputs.SyslogDataSourceResponse]] = ...,
        windows_event_logs: Optional[
            Sequence[outputs.WindowsEventLogDataSourceResponse]
        ] = ...,
        windows_firewall_logs: Optional[
            Sequence[outputs.WindowsFirewallLogsDataSourceResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataImports")
    def data_imports(self) -> Optional[outputs.DataSourcesSpecResponseDataImports]: ...
    @_builtins.property
    @pulumi.getter
    def extensions(self) -> Optional[Sequence[outputs.ExtensionDataSourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="iisLogs")
    def iis_logs(self) -> Optional[Sequence[outputs.IisLogsDataSourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="logFiles")
    def log_files(self) -> Optional[Sequence[outputs.LogFilesDataSourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="performanceCounters")
    def performance_counters(
        self,
    ) -> Optional[Sequence[outputs.PerfCounterDataSourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="platformTelemetry")
    def platform_telemetry(
        self,
    ) -> Optional[Sequence[outputs.PlatformTelemetryDataSourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="prometheusForwarder")
    def prometheus_forwarder(
        self,
    ) -> Optional[Sequence[outputs.PrometheusForwarderDataSourceResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def syslog(self) -> Optional[Sequence[outputs.SyslogDataSourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="windowsEventLogs")
    def windows_event_logs(
        self,
    ) -> Optional[Sequence[outputs.WindowsEventLogDataSourceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="windowsFirewallLogs")
    def windows_firewall_logs(
        self,
    ) -> Optional[Sequence[outputs.WindowsFirewallLogsDataSourceResponse]]: ...

@pulumi.output_type
class DataCollectionRuleResponseDestinations(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_monitor_metrics: Optional[
            outputs.DestinationsSpecResponseAzureMonitorMetrics
        ] = ...,
        event_hubs: Optional[Sequence[outputs.EventHubDestinationResponse]] = ...,
        event_hubs_direct: Optional[
            Sequence[outputs.EventHubDirectDestinationResponse]
        ] = ...,
        log_analytics: Optional[
            Sequence[outputs.LogAnalyticsDestinationResponse]
        ] = ...,
        monitoring_accounts: Optional[
            Sequence[outputs.MonitoringAccountDestinationResponse]
        ] = ...,
        storage_accounts: Optional[
            Sequence[outputs.StorageBlobDestinationResponse]
        ] = ...,
        storage_blobs_direct: Optional[
            Sequence[outputs.StorageBlobDestinationResponse]
        ] = ...,
        storage_tables_direct: Optional[
            Sequence[outputs.StorageTableDestinationResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorMetrics")
    def azure_monitor_metrics(
        self,
    ) -> Optional[outputs.DestinationsSpecResponseAzureMonitorMetrics]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubs")
    def event_hubs(self) -> Optional[Sequence[outputs.EventHubDestinationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="eventHubsDirect")
    def event_hubs_direct(
        self,
    ) -> Optional[Sequence[outputs.EventHubDirectDestinationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="logAnalytics")
    def log_analytics(
        self,
    ) -> Optional[Sequence[outputs.LogAnalyticsDestinationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="monitoringAccounts")
    def monitoring_accounts(
        self,
    ) -> Optional[Sequence[outputs.MonitoringAccountDestinationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(
        self,
    ) -> Optional[Sequence[outputs.StorageBlobDestinationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="storageBlobsDirect")
    def storage_blobs_direct(
        self,
    ) -> Optional[Sequence[outputs.StorageBlobDestinationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="storageTablesDirect")
    def storage_tables_direct(
        self,
    ) -> Optional[Sequence[outputs.StorageTableDestinationResponse]]: ...

@pulumi.output_type
class DataCollectionRuleResponseMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioned_by: _builtins.str,
        provisioned_by_resource_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisionedBy")
    def provisioned_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisionedByResourceId")
    def provisioned_by_resource_id(self) -> _builtins.str: ...

@pulumi.output_type
class DataFlowResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        built_in_transform: Optional[_builtins.str] = ...,
        destinations: Optional[Sequence[_builtins.str]] = ...,
        output_stream: Optional[_builtins.str] = ...,
        streams: Optional[Sequence[_builtins.str]] = ...,
        transform_kql: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="builtInTransform")
    def built_in_transform(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="outputStream")
    def output_stream(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transformKql")
    def transform_kql(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataImportSourcesResponseEventHub(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consumer_group: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        stream: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def stream(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourcesSpecResponseDataImports(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_hub: Optional[outputs.DataImportSourcesResponseEventHub] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventHub")
    def event_hub(self) -> Optional[outputs.DataImportSourcesResponseEventHub]: ...

@pulumi.output_type
class DependenciesSignalGroupResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aggregation_type: Optional[_builtins.str] = ...,
        degraded_threshold: Optional[_builtins.str] = ...,
        unhealthy_threshold: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggregationType")
    def aggregation_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="degradedThreshold")
    def degraded_threshold(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DestinationsSpecResponseAzureMonitorMetrics(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DiagnosticSettingsCategoryResourceResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        category_groups: Optional[Sequence[_builtins.str]] = ...,
        category_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="categoryGroups")
    def category_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="categoryType")
    def category_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DimensionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        operator: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class DiscoveryErrorResponse(dict):
    def __init__(
        __self__, *, context: Sequence[_builtins.str], message: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...

@pulumi.output_type
class DynamicDetectionRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dynamic_threshold_direction: _builtins.str,
        dynamic_threshold_model: _builtins.str,
        model_sensitivity: _builtins.float,
        training_start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dynamicThresholdDirection")
    def dynamic_threshold_direction(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dynamicThresholdModel")
    def dynamic_threshold_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelSensitivity")
    def model_sensitivity(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="trainingStartTime")
    def training_start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DynamicMetricCriteriaResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        alert_sensitivity: _builtins.str,
        criterion_type: _builtins.str,
        failing_periods: outputs.DynamicThresholdFailingPeriodsResponse,
        metric_name: _builtins.str,
        name: _builtins.str,
        operator: _builtins.str,
        time_aggregation: _builtins.str,
        dimensions: Optional[Sequence[outputs.MetricDimensionResponse]] = ...,
        ignore_data_before: Optional[_builtins.str] = ...,
        metric_namespace: Optional[_builtins.str] = ...,
        skip_metric_validation: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alertSensitivity")
    def alert_sensitivity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="criterionType")
    def criterion_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="failingPeriods")
    def failing_periods(self) -> outputs.DynamicThresholdFailingPeriodsResponse: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeAggregation")
    def time_aggregation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence[outputs.MetricDimensionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreDataBefore")
    def ignore_data_before(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipMetricValidation")
    def skip_metric_validation(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DynamicThresholdFailingPeriodsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        min_failing_periods_to_alert: _builtins.float,
        number_of_evaluation_periods: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minFailingPeriodsToAlert")
    def min_failing_periods_to_alert(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="numberOfEvaluationPeriods")
    def number_of_evaluation_periods(self) -> _builtins.float: ...

@pulumi.output_type
class EmailNotificationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_emails: Optional[Sequence[_builtins.str]] = ...,
        send_to_subscription_administrator: Optional[_builtins.bool] = ...,
        send_to_subscription_co_administrators: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customEmails")
    def custom_emails(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sendToSubscriptionAdministrator")
    def send_to_subscription_administrator(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sendToSubscriptionCoAdministrators")
    def send_to_subscription_co_administrators(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class EmailReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        email_address: _builtins.str,
        name: _builtins.str,
        status: _builtins.str,
        use_common_alert_schema: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class EntityAlertsResponse(dict):
    def __init__(
        __self__,
        *,
        degraded: Optional[outputs.AlertConfigurationResponse] = ...,
        unhealthy: Optional[outputs.AlertConfigurationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def degraded(self) -> Optional[outputs.AlertConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def unhealthy(self) -> Optional[outputs.AlertConfigurationResponse]: ...

@pulumi.output_type
class EntityCoordinatesResponse(dict):
    def __init__(__self__, *, x: _builtins.float, y: _builtins.float) -> None: ...
    @_builtins.property
    @pulumi.getter
    def x(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def y(self) -> _builtins.float: ...

@pulumi.output_type
class EntityPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deletion_date: _builtins.str,
        discovered_by: _builtins.str,
        health_state: _builtins.str,
        provisioning_state: _builtins.str,
        alerts: Optional[outputs.EntityAlertsResponse] = ...,
        canvas_position: Optional[outputs.EntityCoordinatesResponse] = ...,
        display_name: Optional[_builtins.str] = ...,
        health_objective: Optional[_builtins.float] = ...,
        icon: Optional[outputs.IconDefinitionResponse] = ...,
        impact: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
        signals: Optional[outputs.SignalGroupResponse] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deletionDate")
    def deletion_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="discoveredBy")
    def discovered_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthState")
    def health_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def alerts(self) -> Optional[outputs.EntityAlertsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="canvasPosition")
    def canvas_position(self) -> Optional[outputs.EntityCoordinatesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="healthObjective")
    def health_objective(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def icon(self) -> Optional[outputs.IconDefinitionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def impact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def signals(self) -> Optional[outputs.SignalGroupResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class EvaluationRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        degraded_rule: Optional[outputs.ThresholdRuleResponse] = ...,
        dynamic_detection_rule: Optional[outputs.DynamicDetectionRuleResponse] = ...,
        unhealthy_rule: Optional[outputs.ThresholdRuleResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="degradedRule")
    def degraded_rule(self) -> Optional[outputs.ThresholdRuleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dynamicDetectionRule")
    def dynamic_detection_rule(
        self,
    ) -> Optional[outputs.DynamicDetectionRuleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyRule")
    def unhealthy_rule(self) -> Optional[outputs.ThresholdRuleResponse]: ...

@pulumi.output_type
class EventHubDestinationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_hub_resource_id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventHubDirectDestinationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_hub_resource_id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventHubReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_hub_name: _builtins.str,
        event_hub_name_space: _builtins.str,
        name: _builtins.str,
        subscription_id: _builtins.str,
        managed_identity: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
        use_common_alert_schema: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eventHubNameSpace")
    def event_hub_name_space(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ExporterResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        azure_monitor_workspace_logs: Optional[
            outputs.AzureMonitorWorkspaceLogsExporterResponse
        ] = ...,
        tcp: Optional[outputs.TcpExporterResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorWorkspaceLogs")
    def azure_monitor_workspace_logs(
        self,
    ) -> Optional[outputs.AzureMonitorWorkspaceLogsExporterResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tcp(self) -> Optional[outputs.TcpExporterResponse]: ...

@pulumi.output_type
class ExtensionDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        extension_name: _builtins.str,
        extension_settings: Optional[Any] = ...,
        input_data_sources: Optional[Sequence[_builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        streams: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="extensionName")
    def extension_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extensionSettings")
    def extension_settings(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="inputDataSources")
    def input_data_sources(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class HealthModelPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        query_endpoint: _builtins.str,
        discovery: Optional[outputs.ModelDiscoverySettingsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryEndpoint")
    def query_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def discovery(self) -> Optional[outputs.ModelDiscoverySettingsResponse]: ...

@pulumi.output_type
class IconDefinitionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        icon_name: _builtins.str,
        custom_data: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iconName")
    def icon_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customData")
    def custom_data(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserIdentityPropertiesResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserIdentityPropertiesResponse]]: ...

@pulumi.output_type
class IisLogsDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        streams: Sequence[_builtins.str],
        log_directories: Optional[Sequence[_builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logDirectories")
    def log_directories(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IncidentReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection: outputs.IncidentServiceConnectionResponse,
        incident_management_service: _builtins.str,
        mappings: Mapping[str, _builtins.str],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connection(self) -> outputs.IncidentServiceConnectionResponse: ...
    @_builtins.property
    @pulumi.getter(name="incidentManagementService")
    def incident_management_service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mappings(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class IncidentServiceConnectionResponse(dict):
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class InvestigationExecutionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        run_state: _builtins.str,
        completed_at: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="runState")
    def run_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="completedAt")
    def completed_at(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InvestigationMetadataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: _builtins.str,
        execution: outputs.InvestigationExecutionResponse,
        id: _builtins.str,
        run_parameters: outputs.RunParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def execution(self) -> outputs.InvestigationExecutionResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runParameters")
    def run_parameters(self) -> outputs.RunParametersResponse: ...

@pulumi.output_type
class InvestigationScopeResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        origin: outputs.OriginResponse,
        relevance: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def origin(self) -> outputs.OriginResponse: ...
    @_builtins.property
    @pulumi.getter
    def relevance(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IssuePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        impact_time: _builtins.str,
        investigations: Sequence[outputs.InvestigationMetadataResponse],
        investigations_count: _builtins.int,
        provisioning_state: _builtins.str,
        severity: _builtins.str,
        status: _builtins.str,
        title: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="impactTime")
    def impact_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def investigations(self) -> Sequence[outputs.InvestigationMetadataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="investigationsCount")
    def investigations_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...

@pulumi.output_type
class ItsmReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_id: _builtins.str,
        name: _builtins.str,
        region: _builtins.str,
        ticket_configuration: _builtins.str,
        workspace_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ticketConfiguration")
    def ticket_configuration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> _builtins.str: ...

@pulumi.output_type
class JsonArrayMapperResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        keys: Sequence[_builtins.str],
        destination_field: Optional[outputs.JsonMapperDestinationFieldResponse] = ...,
        source_field: Optional[outputs.JsonMapperSourceFieldResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationField")
    def destination_field(
        self,
    ) -> Optional[outputs.JsonMapperDestinationFieldResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sourceField")
    def source_field(self) -> Optional[outputs.JsonMapperSourceFieldResponse]: ...

@pulumi.output_type
class JsonMapperDestinationFieldResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: Optional[_builtins.str] = ...,
        field_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JsonMapperSourceFieldResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, field_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LocationSpecResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location: Optional[_builtins.str] = ...,
        provisioning_status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStatus")
    def provisioning_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogAnalyticsDestinationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        workspace_id: _builtins.str,
        name: Optional[_builtins.str] = ...,
        workspace_resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogAnalyticsQuerySignalDefinitionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deletion_date: _builtins.str,
        evaluation_rules: outputs.EvaluationRuleResponse,
        provisioning_state: _builtins.str,
        query_text: _builtins.str,
        signal_kind: _builtins.str,
        data_unit: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        refresh_interval: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        time_grain: Optional[_builtins.str] = ...,
        value_column_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deletionDate")
    def deletion_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="evaluationRules")
    def evaluation_rules(self) -> outputs.EvaluationRuleResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryText")
    def query_text(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signalKind")
    def signal_kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataUnit")
    def data_unit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valueColumnName")
    def value_column_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogAnalyticsSignalGroupResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authentication_setting: _builtins.str,
        log_analytics_workspace_resource_id: _builtins.str,
        signal_assignments: Optional[Sequence[outputs.SignalAssignmentResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationSetting")
    def authentication_setting(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsWorkspaceResourceId")
    def log_analytics_workspace_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signalAssignments")
    def signal_assignments(
        self,
    ) -> Optional[Sequence[outputs.SignalAssignmentResponse]]: ...

@pulumi.output_type
class LogFileSettingsResponseText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, record_start_timestamp_format: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordStartTimestampFormat")
    def record_start_timestamp_format(self) -> _builtins.str: ...

@pulumi.output_type
class LogFilesDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        file_patterns: Sequence[_builtins.str],
        format: _builtins.str,
        streams: Sequence[_builtins.str],
        name: Optional[_builtins.str] = ...,
        settings: Optional[outputs.LogFilesDataSourceResponseSettings] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filePatterns")
    def file_patterns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.LogFilesDataSourceResponseSettings]: ...

@pulumi.output_type
class LogFilesDataSourceResponseSettings(dict):
    def __init__(
        __self__, *, text: Optional[outputs.LogFileSettingsResponseText] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[outputs.LogFileSettingsResponseText]: ...

@pulumi.output_type
class LogSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        category: Optional[_builtins.str] = ...,
        category_group: Optional[_builtins.str] = ...,
        retention_policy: Optional[outputs.RetentionPolicyResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="categoryGroup")
    def category_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[outputs.RetentionPolicyResponse]: ...

@pulumi.output_type
class LogicAppReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        callback_url: _builtins.str,
        name: _builtins.str,
        resource_id: _builtins.str,
        managed_identity: Optional[_builtins.str] = ...,
        use_common_alert_schema: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="callbackUrl")
    def callback_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ManagedIdentityAuthenticationSettingPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authentication_kind: _builtins.str,
        managed_identity_name: _builtins.str,
        provisioning_state: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationKind")
    def authentication_kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="managedIdentityName")
    def managed_identity_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class ManagementGroupLogSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        category: Optional[_builtins.str] = ...,
        category_group: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="categoryGroup")
    def category_group(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MetricAlertActionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_group_id: Optional[_builtins.str] = ...,
        web_hook_properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webHookProperties")
    def web_hook_properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class MetricAlertMultipleResourceMultipleMetricCriteriaResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, odata_type: _builtins.str, all_of: Optional[Sequence[Any]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allOf")
    def all_of(self) -> Optional[Sequence[Any]]: ...

@pulumi.output_type
class MetricAlertSingleResourceMultipleMetricCriteriaResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        odata_type: _builtins.str,
        all_of: Optional[Sequence[outputs.MetricCriteriaResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allOf")
    def all_of(self) -> Optional[Sequence[outputs.MetricCriteriaResponse]]: ...

@pulumi.output_type
class MetricCriteriaResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        criterion_type: _builtins.str,
        metric_name: _builtins.str,
        name: _builtins.str,
        operator: _builtins.str,
        threshold: _builtins.float,
        time_aggregation: _builtins.str,
        dimensions: Optional[Sequence[outputs.MetricDimensionResponse]] = ...,
        metric_namespace: Optional[_builtins.str] = ...,
        skip_metric_validation: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="criterionType")
    def criterion_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="timeAggregation")
    def time_aggregation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence[outputs.MetricDimensionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipMetricValidation")
    def skip_metric_validation(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MetricDimensionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        operator: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class MetricSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        category: Optional[_builtins.str] = ...,
        retention_policy: Optional[outputs.RetentionPolicyResponse] = ...,
        time_grain: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[outputs.RetentionPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MetricTriggerResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_name: _builtins.str,
        metric_resource_uri: _builtins.str,
        operator: _builtins.str,
        statistic: _builtins.str,
        threshold: _builtins.float,
        time_aggregation: _builtins.str,
        time_grain: _builtins.str,
        time_window: _builtins.str,
        dimensions: Optional[Sequence[outputs.ScaleRuleMetricDimensionResponse]] = ...,
        divide_per_instance: Optional[_builtins.bool] = ...,
        metric_namespace: Optional[_builtins.str] = ...,
        metric_resource_location: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metricResourceUri")
    def metric_resource_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="timeAggregation")
    def time_aggregation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[Sequence[outputs.ScaleRuleMetricDimensionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="dividePerInstance")
    def divide_per_instance(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricResourceLocation")
    def metric_resource_location(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ModelDiscoverySettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        add_recommended_signals: _builtins.str,
        scope: _builtins.str,
        identity: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addRecommendedSignals")
    def add_recommended_signals(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MonitoringAccountDestinationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_id: _builtins.str,
        account_resource_id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountResourceId")
    def account_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkingConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        external_networking_mode: _builtins.str,
        routes: Sequence[outputs.NetworkingRouteResponse],
        host: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalNetworkingMode")
    def external_networking_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Sequence[outputs.NetworkingRouteResponse]: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NetworkingRouteResponse(dict):
    def __init__(
        __self__,
        *,
        receiver: _builtins.str,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        subdomain: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def receiver(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def subdomain(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OriginResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, added_by: _builtins.str, added_by_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addedBy")
    def added_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addedByType")
    def added_by_type(self) -> _builtins.str: ...

@pulumi.output_type
class OtlpReceiverResponse(dict):
    def __init__(__self__, *, endpoint: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...

@pulumi.output_type
class PerfCounterDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        counter_specifiers: Optional[Sequence[_builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        sampling_frequency_in_seconds: Optional[_builtins.int] = ...,
        streams: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="counterSpecifiers")
    def counter_specifiers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="samplingFrequencyInSeconds")
    def sampling_frequency_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PersistenceConfigurationsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, persistent_volume_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="persistentVolumeName")
    def persistent_volume_name(self) -> _builtins.str: ...

@pulumi.output_type
class PipelineGroupPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exporters: Sequence[outputs.ExporterResponse],
        processors: Sequence[outputs.ProcessorResponse],
        provisioning_state: _builtins.str,
        receivers: Sequence[outputs.ReceiverResponse],
        service: outputs.ServiceResponse,
        networking_configurations: Optional[
            Sequence[outputs.NetworkingConfigurationResponse]
        ] = ...,
        replicas: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exporters(self) -> Sequence[outputs.ExporterResponse]: ...
    @_builtins.property
    @pulumi.getter
    def processors(self) -> Sequence[outputs.ProcessorResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def receivers(self) -> Sequence[outputs.ReceiverResponse]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> outputs.ServiceResponse: ...
    @_builtins.property
    @pulumi.getter(name="networkingConfigurations")
    def networking_configurations(
        self,
    ) -> Optional[Sequence[outputs.NetworkingConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class PipelineResponse(dict):
    def __init__(
        __self__,
        *,
        exporters: Sequence[_builtins.str],
        name: _builtins.str,
        receivers: Sequence[_builtins.str],
        type: _builtins.str,
        processors: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exporters(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def receivers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def processors(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PlatformTelemetryDataSourceResponse(dict):
    def __init__(
        __self__,
        *,
        streams: Sequence[_builtins.str],
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PredictiveAutoscalePolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        scale_mode: _builtins.str,
        scale_look_ahead_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scaleMode")
    def scale_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scaleLookAheadTime")
    def scale_look_ahead_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_ids: Sequence[_builtins.str],
        id: _builtins.str,
        name: _builtins.str,
        private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse,
        provisioning_state: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> outputs.PrivateLinkServiceConnectionStateResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]: ...

@pulumi.output_type
class PrivateEndpointConnectionResponseV1(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse,
        provisioning_state: _builtins.str,
        type: _builtins.str,
        private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> outputs.PrivateLinkServiceConnectionStateResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]: ...

@pulumi.output_type
class PrivateEndpointResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateLinkScopedResourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_id: Optional[_builtins.str] = ...,
        scope_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions_required: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProcessorResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        batch: Optional[outputs.BatchProcessorResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def batch(self) -> Optional[outputs.BatchProcessorResponse]: ...

@pulumi.output_type
class PrometheusForwarderDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        label_include_filter: Optional[Mapping[str, _builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        streams: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labelIncludeFilter")
    def label_include_filter(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PrometheusMetricsSignalDefinitionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deletion_date: _builtins.str,
        evaluation_rules: outputs.EvaluationRuleResponse,
        provisioning_state: _builtins.str,
        query_text: _builtins.str,
        signal_kind: _builtins.str,
        data_unit: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        refresh_interval: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        time_grain: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deletionDate")
    def deletion_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="evaluationRules")
    def evaluation_rules(self) -> outputs.EvaluationRuleResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryText")
    def query_text(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signalKind")
    def signal_kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataUnit")
    def data_unit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReceiverResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        otlp: Optional[outputs.OtlpReceiverResponse] = ...,
        syslog: Optional[outputs.SyslogReceiverResponse] = ...,
        udp: Optional[outputs.UdpReceiverResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def otlp(self) -> Optional[outputs.OtlpReceiverResponse]: ...
    @_builtins.property
    @pulumi.getter
    def syslog(self) -> Optional[outputs.SyslogReceiverResponse]: ...
    @_builtins.property
    @pulumi.getter
    def udp(self) -> Optional[outputs.UdpReceiverResponse]: ...

@pulumi.output_type
class RecordMapResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, from_: _builtins.str, to: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.str: ...

@pulumi.output_type
class RecurrenceResponse(dict):
    def __init__(
        __self__,
        *,
        frequency: _builtins.str,
        schedule: outputs.RecurrentScheduleResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> outputs.RecurrentScheduleResponse: ...

@pulumi.output_type
class RecurrentScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        days: Sequence[_builtins.str],
        hours: Sequence[_builtins.int],
        minutes: Sequence[_builtins.int],
        time_zone: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str: ...

@pulumi.output_type
class RelatedAlertResponse(dict):
    def __init__(
        __self__,
        *,
        added_at: _builtins.str,
        id: _builtins.str,
        last_modified_at: _builtins.str,
        origin: outputs.OriginResponse,
        relevance: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addedAt")
    def added_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def origin(self) -> outputs.OriginResponse: ...
    @_builtins.property
    @pulumi.getter
    def relevance(self) -> _builtins.str: ...

@pulumi.output_type
class RelatedResourceResponse(dict):
    def __init__(
        __self__,
        *,
        added_at: _builtins.str,
        id: _builtins.str,
        last_modified_at: _builtins.str,
        origin: outputs.OriginResponse,
        relevance: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addedAt")
    def added_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def origin(self) -> outputs.OriginResponse: ...
    @_builtins.property
    @pulumi.getter
    def relevance(self) -> _builtins.str: ...

@pulumi.output_type
class RelationshipPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        child_entity_name: _builtins.str,
        deletion_date: _builtins.str,
        discovered_by: _builtins.str,
        parent_entity_name: _builtins.str,
        provisioning_state: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="childEntityName")
    def child_entity_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionDate")
    def deletion_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="discoveredBy")
    def discovered_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parentEntityName")
    def parent_entity_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ResourceGraphQueryDiscoveryRulePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        add_recommended_signals: _builtins.str,
        authentication_setting: _builtins.str,
        deletion_date: _builtins.str,
        discover_relationships: _builtins.str,
        discovery_rule_kind: _builtins.str,
        entity_name: _builtins.str,
        error: outputs.DiscoveryErrorResponse,
        provisioning_state: _builtins.str,
        resource_graph_query: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addRecommendedSignals")
    def add_recommended_signals(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="authenticationSetting")
    def authentication_setting(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionDate")
    def deletion_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="discoverRelationships")
    def discover_relationships(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="discoveryRuleKind")
    def discovery_rule_kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.DiscoveryErrorResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGraphQuery")
    def resource_graph_query(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceMapResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, from_: _builtins.str, to: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceMetricSignalDefinitionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aggregation_type: _builtins.str,
        deletion_date: _builtins.str,
        evaluation_rules: outputs.EvaluationRuleResponse,
        metric_name: _builtins.str,
        metric_namespace: _builtins.str,
        provisioning_state: _builtins.str,
        signal_kind: _builtins.str,
        time_grain: _builtins.str,
        data_unit: Optional[_builtins.str] = ...,
        dimension: Optional[_builtins.str] = ...,
        dimension_filter: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        refresh_interval: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggregationType")
    def aggregation_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deletionDate")
    def deletion_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="evaluationRules")
    def evaluation_rules(self) -> outputs.EvaluationRuleResponse: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="signalKind")
    def signal_kind(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataUnit")
    def data_unit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dimensionFilter")
    def dimension_filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class RetentionPolicyResponse(dict):
    def __init__(__self__, *, days: _builtins.int, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class RuleResolveConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_resolved: Optional[_builtins.bool] = ...,
        time_to_resolve: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoResolved")
    def auto_resolved(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="timeToResolve")
    def time_to_resolve(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RunParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        alerts: Sequence[outputs.InvestigationScopeResponse],
        impact_time: _builtins.str,
        resources: Sequence[outputs.InvestigationScopeResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alerts(self) -> Sequence[outputs.InvestigationScopeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="impactTime")
    def impact_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[outputs.InvestigationScopeResponse]: ...

@pulumi.output_type
class ScaleActionResponse(dict):
    def __init__(
        __self__,
        *,
        cooldown: _builtins.str,
        direction: _builtins.str,
        type: _builtins.str,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cooldown(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScaleCapacityResponse(dict):
    def __init__(
        __self__,
        *,
        default: _builtins.str,
        maximum: _builtins.str,
        minimum: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> _builtins.str: ...

@pulumi.output_type
class ScaleRuleMetricDimensionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dimension_name: _builtins.str,
        operator: _builtins.str,
        values: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dimensionName")
    def dimension_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ScaleRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_trigger: outputs.MetricTriggerResponse,
        scale_action: outputs.ScaleActionResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricTrigger")
    def metric_trigger(self) -> outputs.MetricTriggerResponse: ...
    @_builtins.property
    @pulumi.getter(name="scaleAction")
    def scale_action(self) -> outputs.ScaleActionResponse: ...

@pulumi.output_type
class ScheduledQueryRuleCriteriaResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, all_of: Optional[Sequence[outputs.ConditionResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allOf")
    def all_of(self) -> Optional[Sequence[outputs.ConditionResponse]]: ...

@pulumi.output_type
class SchemaMapResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        record_map: Sequence[outputs.RecordMapResponse],
        resource_map: Optional[Sequence[outputs.ResourceMapResponse]] = ...,
        scope_map: Optional[Sequence[outputs.ScopeMapResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordMap")
    def record_map(self) -> Sequence[outputs.RecordMapResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceMap")
    def resource_map(self) -> Optional[Sequence[outputs.ResourceMapResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="scopeMap")
    def scope_map(self) -> Optional[Sequence[outputs.ScopeMapResponse]]: ...

@pulumi.output_type
class ScopeMapResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, from_: _builtins.str, to: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceResponse(dict):
    def __init__(
        __self__,
        *,
        pipelines: Sequence[outputs.PipelineResponse],
        persistence: Optional[outputs.PersistenceConfigurationsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pipelines(self) -> Sequence[outputs.PipelineResponse]: ...
    @_builtins.property
    @pulumi.getter
    def persistence(self) -> Optional[outputs.PersistenceConfigurationsResponse]: ...

@pulumi.output_type
class SignalAssignmentResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, signal_definitions: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="signalDefinitions")
    def signal_definitions(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class SignalGroupResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_log_analytics: Optional[outputs.LogAnalyticsSignalGroupResponse] = ...,
        azure_monitor_workspace: Optional[
            outputs.AzureMonitorWorkspaceSignalGroupResponse
        ] = ...,
        azure_resource: Optional[outputs.AzureResourceSignalGroupResponse] = ...,
        dependencies: Optional[outputs.DependenciesSignalGroupResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureLogAnalytics")
    def azure_log_analytics(
        self,
    ) -> Optional[outputs.LogAnalyticsSignalGroupResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorWorkspace")
    def azure_monitor_workspace(
        self,
    ) -> Optional[outputs.AzureMonitorWorkspaceSignalGroupResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureResource")
    def azure_resource(self) -> Optional[outputs.AzureResourceSignalGroupResponse]: ...
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> Optional[outputs.DependenciesSignalGroupResponse]: ...

@pulumi.output_type
class SmsReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        country_code: _builtins.str,
        name: _builtins.str,
        phone_number: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class StorageBlobDestinationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_name: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        storage_account_resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageTableDestinationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        storage_account_resource_id: Optional[_builtins.str] = ...,
        table_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamDeclarationResponse(dict):
    def __init__(
        __self__, *, columns: Optional[Sequence[outputs.ColumnDefinitionResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Optional[Sequence[outputs.ColumnDefinitionResponse]]: ...

@pulumi.output_type
class SubscriptionLogSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        category: Optional[_builtins.str] = ...,
        category_group: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="categoryGroup")
    def category_group(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SyslogDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        facility_names: Optional[Sequence[_builtins.str]] = ...,
        log_levels: Optional[Sequence[_builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        streams: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="facilityNames")
    def facility_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="logLevels")
    def log_levels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SyslogReceiverResponse(dict):
    def __init__(
        __self__, *, endpoint: _builtins.str, protocol: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...

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
class TcpExporterResponse(dict):
    def __init__(__self__, *, url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...

@pulumi.output_type
class ThresholdRuleResponse(dict):
    def __init__(
        __self__, *, operator: _builtins.str, threshold: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.str: ...

@pulumi.output_type
class TimeWindowResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end: _builtins.str,
        start: _builtins.str,
        time_zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UdpReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint: _builtins.str,
        encoding: Optional[_builtins.str] = ...,
        json_array_mapper: Optional[outputs.JsonArrayMapperResponse] = ...,
        read_queue_length: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jsonArrayMapper")
    def json_array_mapper(self) -> Optional[outputs.JsonArrayMapperResponse]: ...
    @_builtins.property
    @pulumi.getter(name="readQueueLength")
    def read_queue_length(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...

@pulumi.output_type
class UserIdentityPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...

@pulumi.output_type
class VoiceReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        country_code: _builtins.str,
        name: _builtins.str,
        phone_number: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...

@pulumi.output_type
class WebhookNotificationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
        service_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebhookReceiverResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        service_uri: _builtins.str,
        identifier_uri: Optional[_builtins.str] = ...,
        managed_identity: Optional[_builtins.str] = ...,
        object_id: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
        use_aad_auth: Optional[_builtins.bool] = ...,
        use_common_alert_schema: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identifierUri")
    def identifier_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useAadAuth")
    def use_aad_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class WebhookReceiverResponseV1(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        service_uri: _builtins.str,
        identifier_uri: Optional[_builtins.str] = ...,
        object_id: Optional[_builtins.str] = ...,
        tenant_id: Optional[_builtins.str] = ...,
        use_aad_auth: Optional[_builtins.bool] = ...,
        use_common_alert_schema: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identifierUri")
    def identifier_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useAadAuth")
    def use_aad_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class WebtestLocationAvailabilityCriteriaResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        component_id: _builtins.str,
        failed_location_count: _builtins.float,
        odata_type: _builtins.str,
        web_test_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="failedLocationCount")
    def failed_location_count(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="webTestId")
    def web_test_id(self) -> _builtins.str: ...

@pulumi.output_type
class WindowsEventLogDataSourceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        streams: Optional[Sequence[_builtins.str]] = ...,
        x_path_queries: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="xPathQueries")
    def x_path_queries(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class WindowsFirewallLogsDataSourceResponse(dict):
    def __init__(
        __self__,
        *,
        streams: Sequence[_builtins.str],
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
