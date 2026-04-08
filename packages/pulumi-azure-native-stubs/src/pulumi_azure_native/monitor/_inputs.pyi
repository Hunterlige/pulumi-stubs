import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessModeSettingsExclusionArgs",
    "AccessModeSettingsExclusionArgsDict",
    "AccessModeSettingsArgs",
    "AccessModeSettingsArgsDict",
    "ActionGroupArgs",
    "ActionGroupArgsDict",
    "ActionListArgs",
    "ActionListArgsDict",
    "ActionsArgs",
    "ActionsArgsDict",
    "AlertConfigurationArgs",
    "AlertConfigurationArgsDict",
    "AlertRuleAllOfConditionArgs",
    "AlertRuleAllOfConditionArgsDict",
    "AlertRuleAnyOfOrLeafConditionArgs",
    "AlertRuleAnyOfOrLeafConditionArgsDict",
    "AlertRuleLeafConditionArgs",
    "AlertRuleLeafConditionArgsDict",
    ...,
    ...,
    "ArmRoleReceiverArgs",
    "ArmRoleReceiverArgsDict",
    "AutomationRunbookReceiverArgs",
    "AutomationRunbookReceiverArgsDict",
    "AutoscaleNotificationArgs",
    "AutoscaleNotificationArgsDict",
    "AutoscaleProfileArgs",
    "AutoscaleProfileArgsDict",
    "AzureAppPushReceiverArgs",
    "AzureAppPushReceiverArgsDict",
    "AzureFunctionReceiverArgs",
    "AzureFunctionReceiverArgsDict",
    "AzureMonitorWorkspaceLogsApiConfigArgs",
    "AzureMonitorWorkspaceLogsApiConfigArgsDict",
    "AzureMonitorWorkspaceLogsExporterArgs",
    "AzureMonitorWorkspaceLogsExporterArgsDict",
    "AzureMonitorWorkspaceSignalGroupArgs",
    "AzureMonitorWorkspaceSignalGroupArgsDict",
    ...,
    ...,
    "AzureResourceSignalGroupArgs",
    "AzureResourceSignalGroupArgsDict",
    "BatchProcessorArgs",
    "BatchProcessorArgsDict",
    "CacheConfigurationArgs",
    "CacheConfigurationArgsDict",
    "ColumnDefinitionArgs",
    "ColumnDefinitionArgsDict",
    "ConcurrencyConfigurationArgs",
    "ConcurrencyConfigurationArgsDict",
    "ConditionFailingPeriodsArgs",
    "ConditionFailingPeriodsArgsDict",
    "ConditionArgs",
    "ConditionArgsDict",
    "DataCollectionEndpointNetworkAclsArgs",
    "DataCollectionEndpointNetworkAclsArgsDict",
    "DataCollectionEndpointResourceIdentityArgs",
    "DataCollectionEndpointResourceIdentityArgsDict",
    "DataCollectionRuleDataSourcesArgs",
    "DataCollectionRuleDataSourcesArgsDict",
    "DataCollectionRuleDestinationsArgs",
    "DataCollectionRuleDestinationsArgsDict",
    "DataCollectionRuleResourceIdentityArgs",
    "DataCollectionRuleResourceIdentityArgsDict",
    "DataFlowArgs",
    "DataFlowArgsDict",
    "DataImportSourcesEventHubArgs",
    "DataImportSourcesEventHubArgsDict",
    "DataSourcesSpecDataImportsArgs",
    "DataSourcesSpecDataImportsArgsDict",
    "DependenciesSignalGroupArgs",
    "DependenciesSignalGroupArgsDict",
    "DestinationsSpecAzureMonitorMetricsArgs",
    "DestinationsSpecAzureMonitorMetricsArgsDict",
    "DimensionArgs",
    "DimensionArgsDict",
    "DynamicDetectionRuleArgs",
    "DynamicDetectionRuleArgsDict",
    "DynamicMetricCriteriaArgs",
    "DynamicMetricCriteriaArgsDict",
    "DynamicThresholdFailingPeriodsArgs",
    "DynamicThresholdFailingPeriodsArgsDict",
    "EmailNotificationArgs",
    "EmailNotificationArgsDict",
    "EmailReceiverArgs",
    "EmailReceiverArgsDict",
    "EntityAlertsArgs",
    "EntityAlertsArgsDict",
    "EntityCoordinatesArgs",
    "EntityCoordinatesArgsDict",
    "EntityPropertiesArgs",
    "EntityPropertiesArgsDict",
    "EvaluationRuleArgs",
    "EvaluationRuleArgsDict",
    "EventHubDestinationArgs",
    "EventHubDestinationArgsDict",
    "EventHubDirectDestinationArgs",
    "EventHubDirectDestinationArgsDict",
    "EventHubReceiverArgs",
    "EventHubReceiverArgsDict",
    "ExporterArgs",
    "ExporterArgsDict",
    "ExtensionDataSourceArgs",
    "ExtensionDataSourceArgsDict",
    "HealthModelPropertiesArgs",
    "HealthModelPropertiesArgsDict",
    "IconDefinitionArgs",
    "IconDefinitionArgsDict",
    "IdentityArgs",
    "IdentityArgsDict",
    "IisLogsDataSourceArgs",
    "IisLogsDataSourceArgsDict",
    "IncidentReceiverArgs",
    "IncidentReceiverArgsDict",
    "IncidentServiceConnectionArgs",
    "IncidentServiceConnectionArgsDict",
    "IssuePropertiesArgs",
    "IssuePropertiesArgsDict",
    "ItsmReceiverArgs",
    "ItsmReceiverArgsDict",
    "JsonArrayMapperArgs",
    "JsonArrayMapperArgsDict",
    "JsonMapperDestinationFieldArgs",
    "JsonMapperDestinationFieldArgsDict",
    "JsonMapperSourceFieldArgs",
    "JsonMapperSourceFieldArgsDict",
    "LogAnalyticsDestinationArgs",
    "LogAnalyticsDestinationArgsDict",
    "LogAnalyticsQuerySignalDefinitionPropertiesArgs",
    ...,
    "LogAnalyticsSignalGroupArgs",
    "LogAnalyticsSignalGroupArgsDict",
    "LogFileSettingsTextArgs",
    "LogFileSettingsTextArgsDict",
    "LogFilesDataSourceSettingsArgs",
    "LogFilesDataSourceSettingsArgsDict",
    "LogFilesDataSourceArgs",
    "LogFilesDataSourceArgsDict",
    "LogSettingsArgs",
    "LogSettingsArgsDict",
    "LogicAppReceiverArgs",
    "LogicAppReceiverArgsDict",
    "ManagedIdentityAuthenticationSettingPropertiesArgs",
    ...,
    "ManagedServiceIdentityArgs",
    "ManagedServiceIdentityArgsDict",
    "ManagementGroupLogSettingsArgs",
    "ManagementGroupLogSettingsArgsDict",
    "MetricAlertActionArgs",
    "MetricAlertActionArgsDict",
    ...,
    ...,
    ...,
    ...,
    "MetricCriteriaArgs",
    "MetricCriteriaArgsDict",
    "MetricDimensionArgs",
    "MetricDimensionArgsDict",
    "MetricSettingsArgs",
    "MetricSettingsArgsDict",
    "MetricTriggerArgs",
    "MetricTriggerArgsDict",
    "ModelDiscoverySettingsArgs",
    "ModelDiscoverySettingsArgsDict",
    "MonitoringAccountDestinationArgs",
    "MonitoringAccountDestinationArgsDict",
    "NetworkingConfigurationArgs",
    "NetworkingConfigurationArgsDict",
    "NetworkingRouteArgs",
    "NetworkingRouteArgsDict",
    "OtlpReceiverArgs",
    "OtlpReceiverArgsDict",
    "PerfCounterDataSourceArgs",
    "PerfCounterDataSourceArgsDict",
    "PersistenceConfigurationsArgs",
    "PersistenceConfigurationsArgsDict",
    "PipelineGroupPropertiesArgs",
    "PipelineGroupPropertiesArgsDict",
    "PipelineArgs",
    "PipelineArgsDict",
    "PlatformTelemetryDataSourceArgs",
    "PlatformTelemetryDataSourceArgsDict",
    "PredictiveAutoscalePolicyArgs",
    "PredictiveAutoscalePolicyArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "ProcessorArgs",
    "ProcessorArgsDict",
    "PrometheusForwarderDataSourceArgs",
    "PrometheusForwarderDataSourceArgsDict",
    "PrometheusMetricsSignalDefinitionPropertiesArgs",
    ...,
    "ReceiverArgs",
    "ReceiverArgsDict",
    "RecordMapArgs",
    "RecordMapArgsDict",
    "RecurrenceArgs",
    "RecurrenceArgsDict",
    "RecurrentScheduleArgs",
    "RecurrentScheduleArgsDict",
    "RelationshipPropertiesArgs",
    "RelationshipPropertiesArgsDict",
    "ResourceGraphQueryDiscoveryRulePropertiesArgs",
    "ResourceGraphQueryDiscoveryRulePropertiesArgsDict",
    "ResourceMapArgs",
    "ResourceMapArgsDict",
    "ResourceMetricSignalDefinitionPropertiesArgs",
    "ResourceMetricSignalDefinitionPropertiesArgsDict",
    "RetentionPolicyArgs",
    "RetentionPolicyArgsDict",
    "RuleResolveConfigurationArgs",
    "RuleResolveConfigurationArgsDict",
    "ScaleActionArgs",
    "ScaleActionArgsDict",
    "ScaleCapacityArgs",
    "ScaleCapacityArgsDict",
    "ScaleRuleMetricDimensionArgs",
    "ScaleRuleMetricDimensionArgsDict",
    "ScaleRuleArgs",
    "ScaleRuleArgsDict",
    "ScheduledQueryRuleCriteriaArgs",
    "ScheduledQueryRuleCriteriaArgsDict",
    "SchemaMapArgs",
    "SchemaMapArgsDict",
    "ScopeMapArgs",
    "ScopeMapArgsDict",
    "ServiceArgs",
    "ServiceArgsDict",
    "SignalAssignmentArgs",
    "SignalAssignmentArgsDict",
    "SignalGroupArgs",
    "SignalGroupArgsDict",
    "SmsReceiverArgs",
    "SmsReceiverArgsDict",
    "StorageBlobDestinationArgs",
    "StorageBlobDestinationArgsDict",
    "StorageTableDestinationArgs",
    "StorageTableDestinationArgsDict",
    "StreamDeclarationArgs",
    "StreamDeclarationArgsDict",
    "SubscriptionLogSettingsArgs",
    "SubscriptionLogSettingsArgsDict",
    "SyslogDataSourceArgs",
    "SyslogDataSourceArgsDict",
    "SyslogReceiverArgs",
    "SyslogReceiverArgsDict",
    "TcpExporterArgs",
    "TcpExporterArgsDict",
    "ThresholdRuleArgs",
    "ThresholdRuleArgsDict",
    "TimeWindowArgs",
    "TimeWindowArgsDict",
    "UdpReceiverArgs",
    "UdpReceiverArgsDict",
    "VoiceReceiverArgs",
    "VoiceReceiverArgsDict",
    "WebhookNotificationArgs",
    "WebhookNotificationArgsDict",
    "WebhookReceiverArgs",
    "WebhookReceiverArgsDict",
    "WebtestLocationAvailabilityCriteriaArgs",
    "WebtestLocationAvailabilityCriteriaArgsDict",
    "WindowsEventLogDataSourceArgs",
    "WindowsEventLogDataSourceArgsDict",
    "WindowsFirewallLogsDataSourceArgs",
    "WindowsFirewallLogsDataSourceArgsDict",
]

class AccessModeSettingsExclusionArgsDict(TypedDict):
    ingestion_access_mode: NotRequired[pulumi.Input[Union[_builtins.str, AccessMode]]]
    private_endpoint_connection_name: NotRequired[pulumi.Input[_builtins.str]]
    query_access_mode: NotRequired[pulumi.Input[Union[_builtins.str, AccessMode]]]

@pulumi.input_type
class AccessModeSettingsExclusionArgs:
    def __init__(
        __self__,
        *,
        ingestion_access_mode: Optional[
            pulumi.Input[Union[_builtins.str, AccessMode]]
        ] = ...,
        private_endpoint_connection_name: Optional[pulumi.Input[_builtins.str]] = ...,
        query_access_mode: Optional[
            pulumi.Input[Union[_builtins.str, AccessMode]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingestionAccessMode")
    def ingestion_access_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AccessMode]]]: ...
    @ingestion_access_mode.setter
    def ingestion_access_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AccessMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnectionName")
    def private_endpoint_connection_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_endpoint_connection_name.setter
    def private_endpoint_connection_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryAccessMode")
    def query_access_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AccessMode]]]: ...
    @query_access_mode.setter
    def query_access_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AccessMode]]]
    ): ...

class AccessModeSettingsArgsDict(TypedDict):
    ingestion_access_mode: pulumi.Input[Union[_builtins.str, AccessMode]]
    query_access_mode: pulumi.Input[Union[_builtins.str, AccessMode]]
    exclusions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AccessModeSettingsExclusionArgsDict]]]
    ]

@pulumi.input_type
class AccessModeSettingsArgs:
    def __init__(
        __self__,
        *,
        ingestion_access_mode: pulumi.Input[Union[_builtins.str, AccessMode]],
        query_access_mode: pulumi.Input[Union[_builtins.str, AccessMode]],
        exclusions: Optional[
            pulumi.Input[Sequence[pulumi.Input[AccessModeSettingsExclusionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ingestionAccessMode")
    def ingestion_access_mode(
        self,
    ) -> pulumi.Input[Union[_builtins.str, AccessMode]]: ...
    @ingestion_access_mode.setter
    def ingestion_access_mode(
        self, value: pulumi.Input[Union[_builtins.str, AccessMode]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryAccessMode")
    def query_access_mode(self) -> pulumi.Input[Union[_builtins.str, AccessMode]]: ...
    @query_access_mode.setter
    def query_access_mode(
        self, value: pulumi.Input[Union[_builtins.str, AccessMode]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AccessModeSettingsExclusionArgs]]]
    ]: ...
    @exclusions.setter
    def exclusions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AccessModeSettingsExclusionArgs]]]
        ],
    ): ...

class ActionGroupArgsDict(TypedDict):
    action_group_id: pulumi.Input[_builtins.str]
    webhook_properties: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ActionGroupArgs:
    def __init__(
        __self__,
        *,
        action_group_id: pulumi.Input[_builtins.str],
        webhook_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @action_group_id.setter
    def action_group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="webhookProperties")
    def webhook_properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @webhook_properties.setter
    def webhook_properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ActionListArgsDict(TypedDict):
    action_groups: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ActionGroupArgsDict]]]
    ]

@pulumi.input_type
class ActionListArgs:
    def __init__(
        __self__,
        *,
        action_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[ActionGroupArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroups")
    def action_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ActionGroupArgs]]]]: ...
    @action_groups.setter
    def action_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ActionGroupArgs]]]]
    ): ...

class ActionsArgsDict(TypedDict):
    action_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    action_properties: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    custom_properties: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ActionsArgs:
    def __init__(
        __self__,
        *,
        action_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        action_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        custom_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroups")
    def action_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @action_groups.setter
    def action_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="actionProperties")
    def action_properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @action_properties.setter
    def action_properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @custom_properties.setter
    def custom_properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class AlertConfigurationArgsDict(TypedDict):
    severity: pulumi.Input[Union[_builtins.str, AlertSeverity]]
    action_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AlertConfigurationArgs:
    def __init__(
        __self__,
        *,
        severity: pulumi.Input[Union[_builtins.str, AlertSeverity]],
        action_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[Union[_builtins.str, AlertSeverity]]: ...
    @severity.setter
    def severity(self, value: pulumi.Input[Union[_builtins.str, AlertSeverity]]): ...
    @_builtins.property
    @pulumi.getter(name="actionGroupIds")
    def action_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @action_group_ids.setter
    def action_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AlertRuleAllOfConditionArgsDict(TypedDict):
    all_of: pulumi.Input[Sequence[pulumi.Input[AlertRuleAnyOfOrLeafConditionArgsDict]]]

@pulumi.input_type
class AlertRuleAllOfConditionArgs:
    def __init__(
        __self__,
        *,
        all_of: pulumi.Input[Sequence[pulumi.Input[AlertRuleAnyOfOrLeafConditionArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allOf")
    def all_of(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[AlertRuleAnyOfOrLeafConditionArgs]]]: ...
    @all_of.setter
    def all_of(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[AlertRuleAnyOfOrLeafConditionArgs]]],
    ): ...

class AlertRuleAnyOfOrLeafConditionArgsDict(TypedDict):
    any_of: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AlertRuleLeafConditionArgsDict]]]
    ]
    contains_any: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    equals: NotRequired[pulumi.Input[_builtins.str]]
    field: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AlertRuleAnyOfOrLeafConditionArgs:
    def __init__(
        __self__,
        *,
        any_of: Optional[
            pulumi.Input[Sequence[pulumi.Input[AlertRuleLeafConditionArgs]]]
        ] = ...,
        contains_any: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        equals: Optional[pulumi.Input[_builtins.str]] = ...,
        field: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AlertRuleLeafConditionArgs]]]]: ...
    @any_of.setter
    def any_of(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AlertRuleLeafConditionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="containsAny")
    def contains_any(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @contains_any.setter
    def contains_any(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def equals(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @equals.setter
    def equals(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AlertRuleLeafConditionArgsDict(TypedDict):
    contains_any: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    equals: NotRequired[pulumi.Input[_builtins.str]]
    field: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AlertRuleLeafConditionArgs:
    def __init__(
        __self__,
        *,
        contains_any: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        equals: Optional[pulumi.Input[_builtins.str]] = ...,
        field: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containsAny")
    def contains_any(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @contains_any.setter
    def contains_any(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def equals(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @equals.setter
    def equals(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationInsightsTopologyDiscoveryRulePropertiesArgsDict(TypedDict):
    add_recommended_signals: pulumi.Input[
        Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
    ]
    application_insights_resource_id: pulumi.Input[_builtins.str]
    authentication_setting: pulumi.Input[_builtins.str]
    discover_relationships: pulumi.Input[
        Union[_builtins.str, DiscoveryRuleRelationshipDiscoveryBehavior]
    ]
    discovery_rule_kind: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApplicationInsightsTopologyDiscoveryRulePropertiesArgs:
    def __init__(
        __self__,
        *,
        add_recommended_signals: pulumi.Input[
            Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
        ],
        application_insights_resource_id: pulumi.Input[_builtins.str],
        authentication_setting: pulumi.Input[_builtins.str],
        discover_relationships: pulumi.Input[
            Union[_builtins.str, DiscoveryRuleRelationshipDiscoveryBehavior]
        ],
        discovery_rule_kind: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addRecommendedSignals")
    def add_recommended_signals(
        self,
    ) -> pulumi.Input[
        Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
    ]: ...
    @add_recommended_signals.setter
    def add_recommended_signals(
        self,
        value: pulumi.Input[
            Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="applicationInsightsResourceId")
    def application_insights_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @application_insights_resource_id.setter
    def application_insights_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationSetting")
    def authentication_setting(self) -> pulumi.Input[_builtins.str]: ...
    @authentication_setting.setter
    def authentication_setting(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="discoverRelationships")
    def discover_relationships(
        self,
    ) -> pulumi.Input[
        Union[_builtins.str, DiscoveryRuleRelationshipDiscoveryBehavior]
    ]: ...
    @discover_relationships.setter
    def discover_relationships(
        self,
        value: pulumi.Input[
            Union[_builtins.str, DiscoveryRuleRelationshipDiscoveryBehavior]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveryRuleKind")
    def discovery_rule_kind(self) -> pulumi.Input[_builtins.str]: ...
    @discovery_rule_kind.setter
    def discovery_rule_kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ArmRoleReceiverArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    role_id: pulumi.Input[_builtins.str]
    use_common_alert_schema: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ArmRoleReceiverArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        role_id: pulumi.Input[_builtins.str],
        use_common_alert_schema: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleId")
    def role_id(self) -> pulumi.Input[_builtins.str]: ...
    @role_id.setter
    def role_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AutomationRunbookReceiverArgsDict(TypedDict):
    automation_account_id: pulumi.Input[_builtins.str]
    is_global_runbook: pulumi.Input[_builtins.bool]
    runbook_name: pulumi.Input[_builtins.str]
    webhook_resource_id: pulumi.Input[_builtins.str]
    managed_identity: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    service_uri: NotRequired[pulumi.Input[_builtins.str]]
    use_common_alert_schema: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AutomationRunbookReceiverArgs:
    def __init__(
        __self__,
        *,
        automation_account_id: pulumi.Input[_builtins.str],
        is_global_runbook: pulumi.Input[_builtins.bool],
        runbook_name: pulumi.Input[_builtins.str],
        webhook_resource_id: pulumi.Input[_builtins.str],
        managed_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        use_common_alert_schema: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automationAccountId")
    def automation_account_id(self) -> pulumi.Input[_builtins.str]: ...
    @automation_account_id.setter
    def automation_account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isGlobalRunbook")
    def is_global_runbook(self) -> pulumi.Input[_builtins.bool]: ...
    @is_global_runbook.setter
    def is_global_runbook(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="runbookName")
    def runbook_name(self) -> pulumi.Input[_builtins.str]: ...
    @runbook_name.setter
    def runbook_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="webhookResourceId")
    def webhook_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @webhook_resource_id.setter
    def webhook_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_identity.setter
    def managed_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_uri.setter
    def service_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AutoscaleNotificationArgsDict(TypedDict):
    operation: pulumi.Input[OperationType]
    email: NotRequired[pulumi.Input[EmailNotificationArgsDict]]
    webhooks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WebhookNotificationArgsDict]]]
    ]

@pulumi.input_type
class AutoscaleNotificationArgs:
    def __init__(
        __self__,
        *,
        operation: pulumi.Input[OperationType],
        email: Optional[pulumi.Input[EmailNotificationArgs]] = ...,
        webhooks: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebhookNotificationArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> pulumi.Input[OperationType]: ...
    @operation.setter
    def operation(self, value: pulumi.Input[OperationType]): ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[EmailNotificationArgs]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[EmailNotificationArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def webhooks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebhookNotificationArgs]]]]: ...
    @webhooks.setter
    def webhooks(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[WebhookNotificationArgs]]]],
    ): ...

class AutoscaleProfileArgsDict(TypedDict):
    capacity: pulumi.Input[ScaleCapacityArgsDict]
    name: pulumi.Input[_builtins.str]
    rules: pulumi.Input[Sequence[pulumi.Input[ScaleRuleArgsDict]]]
    fixed_date: NotRequired[pulumi.Input[TimeWindowArgsDict]]
    recurrence: NotRequired[pulumi.Input[RecurrenceArgsDict]]

@pulumi.input_type
class AutoscaleProfileArgs:
    def __init__(
        __self__,
        *,
        capacity: pulumi.Input[ScaleCapacityArgs],
        name: pulumi.Input[_builtins.str],
        rules: pulumi.Input[Sequence[pulumi.Input[ScaleRuleArgs]]],
        fixed_date: Optional[pulumi.Input[TimeWindowArgs]] = ...,
        recurrence: Optional[pulumi.Input[RecurrenceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> pulumi.Input[ScaleCapacityArgs]: ...
    @capacity.setter
    def capacity(self, value: pulumi.Input[ScaleCapacityArgs]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input[ScaleRuleArgs]]]: ...
    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input[ScaleRuleArgs]]]): ...
    @_builtins.property
    @pulumi.getter(name="fixedDate")
    def fixed_date(self) -> Optional[pulumi.Input[TimeWindowArgs]]: ...
    @fixed_date.setter
    def fixed_date(self, value: Optional[pulumi.Input[TimeWindowArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[pulumi.Input[RecurrenceArgs]]: ...
    @recurrence.setter
    def recurrence(self, value: Optional[pulumi.Input[RecurrenceArgs]]): ...

class AzureAppPushReceiverArgsDict(TypedDict):
    email_address: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureAppPushReceiverArgs:
    def __init__(
        __self__,
        *,
        email_address: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Input[_builtins.str]: ...
    @email_address.setter
    def email_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class AzureFunctionReceiverArgsDict(TypedDict):
    function_app_resource_id: pulumi.Input[_builtins.str]
    function_name: pulumi.Input[_builtins.str]
    http_trigger_url: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    managed_identity: NotRequired[pulumi.Input[_builtins.str]]
    use_common_alert_schema: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AzureFunctionReceiverArgs:
    def __init__(
        __self__,
        *,
        function_app_resource_id: pulumi.Input[_builtins.str],
        function_name: pulumi.Input[_builtins.str],
        http_trigger_url: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        managed_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        use_common_alert_schema: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionAppResourceId")
    def function_app_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @function_app_resource_id.setter
    def function_app_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Input[_builtins.str]: ...
    @function_name.setter
    def function_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="httpTriggerUrl")
    def http_trigger_url(self) -> pulumi.Input[_builtins.str]: ...
    @http_trigger_url.setter
    def http_trigger_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_identity.setter
    def managed_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AzureMonitorWorkspaceLogsApiConfigArgsDict(TypedDict):
    data_collection_endpoint_url: pulumi.Input[_builtins.str]
    data_collection_rule: pulumi.Input[_builtins.str]
    schema: pulumi.Input[SchemaMapArgsDict]
    stream: pulumi.Input[_builtins.str]

@pulumi.input_type
class AzureMonitorWorkspaceLogsApiConfigArgs:
    def __init__(
        __self__,
        *,
        data_collection_endpoint_url: pulumi.Input[_builtins.str],
        data_collection_rule: pulumi.Input[_builtins.str],
        schema: pulumi.Input[SchemaMapArgs],
        stream: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionEndpointUrl")
    def data_collection_endpoint_url(self) -> pulumi.Input[_builtins.str]: ...
    @data_collection_endpoint_url.setter
    def data_collection_endpoint_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataCollectionRule")
    def data_collection_rule(self) -> pulumi.Input[_builtins.str]: ...
    @data_collection_rule.setter
    def data_collection_rule(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[SchemaMapArgs]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[SchemaMapArgs]): ...
    @_builtins.property
    @pulumi.getter
    def stream(self) -> pulumi.Input[_builtins.str]: ...
    @stream.setter
    def stream(self, value: pulumi.Input[_builtins.str]): ...

class AzureMonitorWorkspaceLogsExporterArgsDict(TypedDict):
    api: pulumi.Input[AzureMonitorWorkspaceLogsApiConfigArgsDict]
    cache: NotRequired[pulumi.Input[CacheConfigurationArgsDict]]
    concurrency: NotRequired[pulumi.Input[ConcurrencyConfigurationArgsDict]]

@pulumi.input_type
class AzureMonitorWorkspaceLogsExporterArgs:
    def __init__(
        __self__,
        *,
        api: pulumi.Input[AzureMonitorWorkspaceLogsApiConfigArgs],
        cache: Optional[pulumi.Input[CacheConfigurationArgs]] = ...,
        concurrency: Optional[pulumi.Input[ConcurrencyConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def api(self) -> pulumi.Input[AzureMonitorWorkspaceLogsApiConfigArgs]: ...
    @api.setter
    def api(self, value: pulumi.Input[AzureMonitorWorkspaceLogsApiConfigArgs]): ...
    @_builtins.property
    @pulumi.getter
    def cache(self) -> Optional[pulumi.Input[CacheConfigurationArgs]]: ...
    @cache.setter
    def cache(self, value: Optional[pulumi.Input[CacheConfigurationArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def concurrency(self) -> Optional[pulumi.Input[ConcurrencyConfigurationArgs]]: ...
    @concurrency.setter
    def concurrency(
        self, value: Optional[pulumi.Input[ConcurrencyConfigurationArgs]]
    ): ...

class AzureMonitorWorkspaceSignalGroupArgsDict(TypedDict):
    authentication_setting: pulumi.Input[_builtins.str]
    azure_monitor_workspace_resource_id: pulumi.Input[_builtins.str]
    signal_assignments: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SignalAssignmentArgsDict]]]
    ]

@pulumi.input_type
class AzureMonitorWorkspaceSignalGroupArgs:
    def __init__(
        __self__,
        *,
        authentication_setting: pulumi.Input[_builtins.str],
        azure_monitor_workspace_resource_id: pulumi.Input[_builtins.str],
        signal_assignments: Optional[
            pulumi.Input[Sequence[pulumi.Input[SignalAssignmentArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationSetting")
    def authentication_setting(self) -> pulumi.Input[_builtins.str]: ...
    @authentication_setting.setter
    def authentication_setting(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorWorkspaceResourceId")
    def azure_monitor_workspace_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @azure_monitor_workspace_resource_id.setter
    def azure_monitor_workspace_resource_id(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signalAssignments")
    def signal_assignments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SignalAssignmentArgs]]]]: ...
    @signal_assignments.setter
    def signal_assignments(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SignalAssignmentArgs]]]],
    ): ...

class AzureResourceManagerCommonTypesExtendedLocationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[Union[_builtins.str, ExtendedLocationType]]

@pulumi.input_type
class AzureResourceManagerCommonTypesExtendedLocationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[Union[_builtins.str, ExtendedLocationType]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ExtendedLocationType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ExtendedLocationType]]): ...

class AzureResourceSignalGroupArgsDict(TypedDict):
    authentication_setting: pulumi.Input[_builtins.str]
    azure_resource_id: pulumi.Input[_builtins.str]
    signal_assignments: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SignalAssignmentArgsDict]]]
    ]

@pulumi.input_type
class AzureResourceSignalGroupArgs:
    def __init__(
        __self__,
        *,
        authentication_setting: pulumi.Input[_builtins.str],
        azure_resource_id: pulumi.Input[_builtins.str],
        signal_assignments: Optional[
            pulumi.Input[Sequence[pulumi.Input[SignalAssignmentArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationSetting")
    def authentication_setting(self) -> pulumi.Input[_builtins.str]: ...
    @authentication_setting.setter
    def authentication_setting(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="azureResourceId")
    def azure_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @azure_resource_id.setter
    def azure_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="signalAssignments")
    def signal_assignments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SignalAssignmentArgs]]]]: ...
    @signal_assignments.setter
    def signal_assignments(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SignalAssignmentArgs]]]],
    ): ...

class BatchProcessorArgsDict(TypedDict):
    batch_size: NotRequired[pulumi.Input[_builtins.int]]
    timeout: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class BatchProcessorArgs:
    def __init__(
        __self__,
        *,
        batch_size: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @batch_size.setter
    def batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CacheConfigurationArgsDict(TypedDict):
    max_storage_usage: NotRequired[pulumi.Input[_builtins.int]]
    retention_period: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class CacheConfigurationArgs:
    def __init__(
        __self__,
        *,
        max_storage_usage: Optional[pulumi.Input[_builtins.int]] = ...,
        retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxStorageUsage")
    def max_storage_usage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_storage_usage.setter
    def max_storage_usage(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ColumnDefinitionArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, KnownColumnDefinitionType]]]

@pulumi.input_type
class ColumnDefinitionArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[
            pulumi.Input[Union[_builtins.str, KnownColumnDefinitionType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, KnownColumnDefinitionType]]]: ...
    @type.setter
    def type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, KnownColumnDefinitionType]]],
    ): ...

class ConcurrencyConfigurationArgsDict(TypedDict):
    batch_queue_size: NotRequired[pulumi.Input[_builtins.int]]
    worker_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ConcurrencyConfigurationArgs:
    def __init__(
        __self__,
        *,
        batch_queue_size: Optional[pulumi.Input[_builtins.int]] = ...,
        worker_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchQueueSize")
    def batch_queue_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @batch_queue_size.setter
    def batch_queue_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="workerCount")
    def worker_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @worker_count.setter
    def worker_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ConditionFailingPeriodsArgsDict(TypedDict):
    min_failing_periods_to_alert: NotRequired[pulumi.Input[_builtins.float]]
    number_of_evaluation_periods: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ConditionFailingPeriodsArgs:
    def __init__(
        __self__,
        *,
        min_failing_periods_to_alert: Optional[pulumi.Input[_builtins.float]] = ...,
        number_of_evaluation_periods: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minFailingPeriodsToAlert")
    def min_failing_periods_to_alert(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min_failing_periods_to_alert.setter
    def min_failing_periods_to_alert(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="numberOfEvaluationPeriods")
    def number_of_evaluation_periods(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @number_of_evaluation_periods.setter
    def number_of_evaluation_periods(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class ConditionArgsDict(TypedDict):
    alert_sensitivity: NotRequired[pulumi.Input[_builtins.str]]
    criterion_type: NotRequired[pulumi.Input[Union[_builtins.str, CriterionType]]]
    dimensions: NotRequired[pulumi.Input[Sequence[pulumi.Input[DimensionArgsDict]]]]
    failing_periods: NotRequired[pulumi.Input[ConditionFailingPeriodsArgsDict]]
    ignore_data_before: NotRequired[pulumi.Input[_builtins.str]]
    metric_measure_column: NotRequired[pulumi.Input[_builtins.str]]
    metric_name: NotRequired[pulumi.Input[_builtins.str]]
    min_recurrence_count: NotRequired[pulumi.Input[_builtins.float]]
    operator: NotRequired[pulumi.Input[Union[_builtins.str, ConditionOperator]]]
    query: NotRequired[pulumi.Input[_builtins.str]]
    resource_id_column: NotRequired[pulumi.Input[_builtins.str]]
    threshold: NotRequired[pulumi.Input[_builtins.float]]
    time_aggregation: NotRequired[pulumi.Input[Union[_builtins.str, TimeAggregation]]]

@pulumi.input_type
class ConditionArgs:
    def __init__(
        __self__,
        *,
        alert_sensitivity: Optional[pulumi.Input[_builtins.str]] = ...,
        criterion_type: Optional[
            pulumi.Input[Union[_builtins.str, CriterionType]]
        ] = ...,
        dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[DimensionArgs]]]] = ...,
        failing_periods: Optional[pulumi.Input[ConditionFailingPeriodsArgs]] = ...,
        ignore_data_before: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_measure_column: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_name: Optional[pulumi.Input[_builtins.str]] = ...,
        min_recurrence_count: Optional[pulumi.Input[_builtins.float]] = ...,
        operator: Optional[pulumi.Input[Union[_builtins.str, ConditionOperator]]] = ...,
        query: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id_column: Optional[pulumi.Input[_builtins.str]] = ...,
        threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        time_aggregation: Optional[
            pulumi.Input[Union[_builtins.str, TimeAggregation]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alertSensitivity")
    def alert_sensitivity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alert_sensitivity.setter
    def alert_sensitivity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="criterionType")
    def criterion_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CriterionType]]]: ...
    @criterion_type.setter
    def criterion_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CriterionType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DimensionArgs]]]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DimensionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failingPeriods")
    def failing_periods(
        self,
    ) -> Optional[pulumi.Input[ConditionFailingPeriodsArgs]]: ...
    @failing_periods.setter
    def failing_periods(
        self, value: Optional[pulumi.Input[ConditionFailingPeriodsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreDataBefore")
    def ignore_data_before(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ignore_data_before.setter
    def ignore_data_before(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricMeasureColumn")
    def metric_measure_column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_measure_column.setter
    def metric_measure_column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minRecurrenceCount")
    def min_recurrence_count(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min_recurrence_count.setter
    def min_recurrence_count(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def operator(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConditionOperator]]]: ...
    @operator.setter
    def operator(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConditionOperator]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query.setter
    def query(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceIdColumn")
    def resource_id_column(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id_column.setter
    def resource_id_column(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="timeAggregation")
    def time_aggregation(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TimeAggregation]]]: ...
    @time_aggregation.setter
    def time_aggregation(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TimeAggregation]]]
    ): ...

class DataCollectionEndpointNetworkAclsArgsDict(TypedDict):
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, KnownPublicNetworkAccessOptions]]
    ]

@pulumi.input_type
class DataCollectionEndpointNetworkAclsArgs:
    def __init__(
        __self__,
        *,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, KnownPublicNetworkAccessOptions]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, KnownPublicNetworkAccessOptions]]
    ]: ...
    @public_network_access.setter
    def public_network_access(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, KnownPublicNetworkAccessOptions]]
        ],
    ): ...

class DataCollectionEndpointResourceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class DataCollectionEndpointResourceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataCollectionRuleDataSourcesArgsDict(TypedDict):
    data_imports: NotRequired[pulumi.Input[DataSourcesSpecDataImportsArgsDict]]
    extensions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ExtensionDataSourceArgsDict]]]
    ]
    iis_logs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[IisLogsDataSourceArgsDict]]]
    ]
    log_files: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LogFilesDataSourceArgsDict]]]
    ]
    performance_counters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PerfCounterDataSourceArgsDict]]]
    ]
    platform_telemetry: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PlatformTelemetryDataSourceArgsDict]]]
    ]
    prometheus_forwarder: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[PrometheusForwarderDataSourceArgsDict]]]
    ]
    syslog: NotRequired[pulumi.Input[Sequence[pulumi.Input[SyslogDataSourceArgsDict]]]]
    windows_event_logs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WindowsEventLogDataSourceArgsDict]]]
    ]
    windows_firewall_logs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WindowsFirewallLogsDataSourceArgsDict]]]
    ]

@pulumi.input_type
class DataCollectionRuleDataSourcesArgs:
    def __init__(
        __self__,
        *,
        data_imports: Optional[pulumi.Input[DataSourcesSpecDataImportsArgs]] = ...,
        extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExtensionDataSourceArgs]]]
        ] = ...,
        iis_logs: Optional[
            pulumi.Input[Sequence[pulumi.Input[IisLogsDataSourceArgs]]]
        ] = ...,
        log_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[LogFilesDataSourceArgs]]]
        ] = ...,
        performance_counters: Optional[
            pulumi.Input[Sequence[pulumi.Input[PerfCounterDataSourceArgs]]]
        ] = ...,
        platform_telemetry: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlatformTelemetryDataSourceArgs]]]
        ] = ...,
        prometheus_forwarder: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrometheusForwarderDataSourceArgs]]]
        ] = ...,
        syslog: Optional[
            pulumi.Input[Sequence[pulumi.Input[SyslogDataSourceArgs]]]
        ] = ...,
        windows_event_logs: Optional[
            pulumi.Input[Sequence[pulumi.Input[WindowsEventLogDataSourceArgs]]]
        ] = ...,
        windows_firewall_logs: Optional[
            pulumi.Input[Sequence[pulumi.Input[WindowsFirewallLogsDataSourceArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataImports")
    def data_imports(
        self,
    ) -> Optional[pulumi.Input[DataSourcesSpecDataImportsArgs]]: ...
    @data_imports.setter
    def data_imports(
        self, value: Optional[pulumi.Input[DataSourcesSpecDataImportsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExtensionDataSourceArgs]]]]: ...
    @extensions.setter
    def extensions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ExtensionDataSourceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="iisLogs")
    def iis_logs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IisLogsDataSourceArgs]]]]: ...
    @iis_logs.setter
    def iis_logs(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[IisLogsDataSourceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logFiles")
    def log_files(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LogFilesDataSourceArgs]]]]: ...
    @log_files.setter
    def log_files(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[LogFilesDataSourceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceCounters")
    def performance_counters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PerfCounterDataSourceArgs]]]]: ...
    @performance_counters.setter
    def performance_counters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PerfCounterDataSourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="platformTelemetry")
    def platform_telemetry(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PlatformTelemetryDataSourceArgs]]]
    ]: ...
    @platform_telemetry.setter
    def platform_telemetry(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PlatformTelemetryDataSourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="prometheusForwarder")
    def prometheus_forwarder(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PrometheusForwarderDataSourceArgs]]]
    ]: ...
    @prometheus_forwarder.setter
    def prometheus_forwarder(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrometheusForwarderDataSourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def syslog(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SyslogDataSourceArgs]]]]: ...
    @syslog.setter
    def syslog(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SyslogDataSourceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsEventLogs")
    def windows_event_logs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WindowsEventLogDataSourceArgs]]]
    ]: ...
    @windows_event_logs.setter
    def windows_event_logs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WindowsEventLogDataSourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="windowsFirewallLogs")
    def windows_firewall_logs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WindowsFirewallLogsDataSourceArgs]]]
    ]: ...
    @windows_firewall_logs.setter
    def windows_firewall_logs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WindowsFirewallLogsDataSourceArgs]]]
        ],
    ): ...

class DataCollectionRuleDestinationsArgsDict(TypedDict):
    azure_monitor_metrics: NotRequired[
        pulumi.Input[DestinationsSpecAzureMonitorMetricsArgsDict]
    ]
    event_hubs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[EventHubDestinationArgsDict]]]
    ]
    event_hubs_direct: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[EventHubDirectDestinationArgsDict]]]
    ]
    log_analytics: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LogAnalyticsDestinationArgsDict]]]
    ]
    monitoring_accounts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[MonitoringAccountDestinationArgsDict]]]
    ]
    storage_accounts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[StorageBlobDestinationArgsDict]]]
    ]
    storage_blobs_direct: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[StorageBlobDestinationArgsDict]]]
    ]
    storage_tables_direct: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[StorageTableDestinationArgsDict]]]
    ]

@pulumi.input_type
class DataCollectionRuleDestinationsArgs:
    def __init__(
        __self__,
        *,
        azure_monitor_metrics: Optional[
            pulumi.Input[DestinationsSpecAzureMonitorMetricsArgs]
        ] = ...,
        event_hubs: Optional[
            pulumi.Input[Sequence[pulumi.Input[EventHubDestinationArgs]]]
        ] = ...,
        event_hubs_direct: Optional[
            pulumi.Input[Sequence[pulumi.Input[EventHubDirectDestinationArgs]]]
        ] = ...,
        log_analytics: Optional[
            pulumi.Input[Sequence[pulumi.Input[LogAnalyticsDestinationArgs]]]
        ] = ...,
        monitoring_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[MonitoringAccountDestinationArgs]]]
        ] = ...,
        storage_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[StorageBlobDestinationArgs]]]
        ] = ...,
        storage_blobs_direct: Optional[
            pulumi.Input[Sequence[pulumi.Input[StorageBlobDestinationArgs]]]
        ] = ...,
        storage_tables_direct: Optional[
            pulumi.Input[Sequence[pulumi.Input[StorageTableDestinationArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorMetrics")
    def azure_monitor_metrics(
        self,
    ) -> Optional[pulumi.Input[DestinationsSpecAzureMonitorMetricsArgs]]: ...
    @azure_monitor_metrics.setter
    def azure_monitor_metrics(
        self, value: Optional[pulumi.Input[DestinationsSpecAzureMonitorMetricsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventHubs")
    def event_hubs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EventHubDestinationArgs]]]]: ...
    @event_hubs.setter
    def event_hubs(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[EventHubDestinationArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventHubsDirect")
    def event_hubs_direct(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EventHubDirectDestinationArgs]]]
    ]: ...
    @event_hubs_direct.setter
    def event_hubs_direct(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EventHubDirectDestinationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logAnalytics")
    def log_analytics(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LogAnalyticsDestinationArgs]]]
    ]: ...
    @log_analytics.setter
    def log_analytics(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LogAnalyticsDestinationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="monitoringAccounts")
    def monitoring_accounts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MonitoringAccountDestinationArgs]]]
    ]: ...
    @monitoring_accounts.setter
    def monitoring_accounts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MonitoringAccountDestinationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[StorageBlobDestinationArgs]]]]: ...
    @storage_accounts.setter
    def storage_accounts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StorageBlobDestinationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageBlobsDirect")
    def storage_blobs_direct(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[StorageBlobDestinationArgs]]]]: ...
    @storage_blobs_direct.setter
    def storage_blobs_direct(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StorageBlobDestinationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageTablesDirect")
    def storage_tables_direct(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[StorageTableDestinationArgs]]]
    ]: ...
    @storage_tables_direct.setter
    def storage_tables_direct(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[StorageTableDestinationArgs]]]
        ],
    ): ...

class DataCollectionRuleResourceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class DataCollectionRuleResourceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataFlowArgsDict(TypedDict):
    built_in_transform: NotRequired[pulumi.Input[_builtins.str]]
    destinations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    output_stream: NotRequired[pulumi.Input[_builtins.str]]
    streams: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, KnownDataFlowStreams]]]]
    ]
    transform_kql: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataFlowArgs:
    def __init__(
        __self__,
        *,
        built_in_transform: Optional[pulumi.Input[_builtins.str]] = ...,
        destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        output_stream: Optional[pulumi.Input[_builtins.str]] = ...,
        streams: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, KnownDataFlowStreams]]]
            ]
        ] = ...,
        transform_kql: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="builtInTransform")
    def built_in_transform(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @built_in_transform.setter
    def built_in_transform(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @destinations.setter
    def destinations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputStream")
    def output_stream(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_stream.setter
    def output_stream(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def streams(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, KnownDataFlowStreams]]]]
    ]: ...
    @streams.setter
    def streams(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, KnownDataFlowStreams]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="transformKql")
    def transform_kql(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transform_kql.setter
    def transform_kql(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataImportSourcesEventHubArgsDict(TypedDict):
    consumer_group: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    stream: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataImportSourcesEventHubArgs:
    def __init__(
        __self__,
        *,
        consumer_group: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        stream: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @consumer_group.setter
    def consumer_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def stream(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream.setter
    def stream(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourcesSpecDataImportsArgsDict(TypedDict):
    event_hub: NotRequired[pulumi.Input[DataImportSourcesEventHubArgsDict]]

@pulumi.input_type
class DataSourcesSpecDataImportsArgs:
    def __init__(
        __self__,
        *,
        event_hub: Optional[pulumi.Input[DataImportSourcesEventHubArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventHub")
    def event_hub(self) -> Optional[pulumi.Input[DataImportSourcesEventHubArgs]]: ...
    @event_hub.setter
    def event_hub(
        self, value: Optional[pulumi.Input[DataImportSourcesEventHubArgs]]
    ): ...

class DependenciesSignalGroupArgsDict(TypedDict):
    aggregation_type: pulumi.Input[Union[_builtins.str, DependenciesAggregationType]]
    degraded_threshold: NotRequired[pulumi.Input[_builtins.str]]
    unhealthy_threshold: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DependenciesSignalGroupArgs:
    def __init__(
        __self__,
        *,
        aggregation_type: Optional[
            pulumi.Input[Union[_builtins.str, DependenciesAggregationType]]
        ] = ...,
        degraded_threshold: Optional[pulumi.Input[_builtins.str]] = ...,
        unhealthy_threshold: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggregationType")
    def aggregation_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, DependenciesAggregationType]]: ...
    @aggregation_type.setter
    def aggregation_type(
        self, value: pulumi.Input[Union[_builtins.str, DependenciesAggregationType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="degradedThreshold")
    def degraded_threshold(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @degraded_threshold.setter
    def degraded_threshold(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DestinationsSpecAzureMonitorMetricsArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DestinationsSpecAzureMonitorMetricsArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DimensionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    operator: pulumi.Input[Union[_builtins.str, DimensionOperator]]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class DimensionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        operator: pulumi.Input[Union[_builtins.str, DimensionOperator]],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, DimensionOperator]]: ...
    @operator.setter
    def operator(
        self, value: pulumi.Input[Union[_builtins.str, DimensionOperator]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class DynamicDetectionRuleArgsDict(TypedDict):
    dynamic_threshold_direction: pulumi.Input[
        Union[_builtins.str, DynamicThresholdDirection]
    ]
    dynamic_threshold_model: pulumi.Input[Union[_builtins.str, DynamicThresholdModel]]
    model_sensitivity: pulumi.Input[_builtins.float]
    training_start_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DynamicDetectionRuleArgs:
    def __init__(
        __self__,
        *,
        dynamic_threshold_direction: pulumi.Input[
            Union[_builtins.str, DynamicThresholdDirection]
        ],
        dynamic_threshold_model: pulumi.Input[
            Union[_builtins.str, DynamicThresholdModel]
        ],
        model_sensitivity: pulumi.Input[_builtins.float],
        training_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dynamicThresholdDirection")
    def dynamic_threshold_direction(
        self,
    ) -> pulumi.Input[Union[_builtins.str, DynamicThresholdDirection]]: ...
    @dynamic_threshold_direction.setter
    def dynamic_threshold_direction(
        self, value: pulumi.Input[Union[_builtins.str, DynamicThresholdDirection]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dynamicThresholdModel")
    def dynamic_threshold_model(
        self,
    ) -> pulumi.Input[Union[_builtins.str, DynamicThresholdModel]]: ...
    @dynamic_threshold_model.setter
    def dynamic_threshold_model(
        self, value: pulumi.Input[Union[_builtins.str, DynamicThresholdModel]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelSensitivity")
    def model_sensitivity(self) -> pulumi.Input[_builtins.float]: ...
    @model_sensitivity.setter
    def model_sensitivity(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="trainingStartTime")
    def training_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @training_start_time.setter
    def training_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DynamicMetricCriteriaArgsDict(TypedDict):
    alert_sensitivity: pulumi.Input[Union[_builtins.str, DynamicThresholdSensitivity]]
    criterion_type: pulumi.Input[_builtins.str]
    failing_periods: pulumi.Input[DynamicThresholdFailingPeriodsArgsDict]
    metric_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    operator: pulumi.Input[Union[_builtins.str, DynamicThresholdOperator]]
    time_aggregation: pulumi.Input[Union[_builtins.str, AggregationTypeEnum]]
    dimensions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgsDict]]]
    ]
    ignore_data_before: NotRequired[pulumi.Input[_builtins.str]]
    metric_namespace: NotRequired[pulumi.Input[_builtins.str]]
    skip_metric_validation: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DynamicMetricCriteriaArgs:
    def __init__(
        __self__,
        *,
        alert_sensitivity: pulumi.Input[
            Union[_builtins.str, DynamicThresholdSensitivity]
        ],
        criterion_type: pulumi.Input[_builtins.str],
        failing_periods: pulumi.Input[DynamicThresholdFailingPeriodsArgs],
        metric_name: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        operator: pulumi.Input[Union[_builtins.str, DynamicThresholdOperator]],
        time_aggregation: pulumi.Input[Union[_builtins.str, AggregationTypeEnum]],
        dimensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgs]]]
        ] = ...,
        ignore_data_before: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_metric_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alertSensitivity")
    def alert_sensitivity(
        self,
    ) -> pulumi.Input[Union[_builtins.str, DynamicThresholdSensitivity]]: ...
    @alert_sensitivity.setter
    def alert_sensitivity(
        self, value: pulumi.Input[Union[_builtins.str, DynamicThresholdSensitivity]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="criterionType")
    def criterion_type(self) -> pulumi.Input[_builtins.str]: ...
    @criterion_type.setter
    def criterion_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failingPeriods")
    def failing_periods(self) -> pulumi.Input[DynamicThresholdFailingPeriodsArgs]: ...
    @failing_periods.setter
    def failing_periods(
        self, value: pulumi.Input[DynamicThresholdFailingPeriodsArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(
        self,
    ) -> pulumi.Input[Union[_builtins.str, DynamicThresholdOperator]]: ...
    @operator.setter
    def operator(
        self, value: pulumi.Input[Union[_builtins.str, DynamicThresholdOperator]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeAggregation")
    def time_aggregation(
        self,
    ) -> pulumi.Input[Union[_builtins.str, AggregationTypeEnum]]: ...
    @time_aggregation.setter
    def time_aggregation(
        self, value: pulumi.Input[Union[_builtins.str, AggregationTypeEnum]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgs]]]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreDataBefore")
    def ignore_data_before(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ignore_data_before.setter
    def ignore_data_before(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_namespace.setter
    def metric_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipMetricValidation")
    def skip_metric_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_metric_validation.setter
    def skip_metric_validation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DynamicThresholdFailingPeriodsArgsDict(TypedDict):
    min_failing_periods_to_alert: pulumi.Input[_builtins.float]
    number_of_evaluation_periods: pulumi.Input[_builtins.float]

@pulumi.input_type
class DynamicThresholdFailingPeriodsArgs:
    def __init__(
        __self__,
        *,
        min_failing_periods_to_alert: pulumi.Input[_builtins.float],
        number_of_evaluation_periods: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minFailingPeriodsToAlert")
    def min_failing_periods_to_alert(self) -> pulumi.Input[_builtins.float]: ...
    @min_failing_periods_to_alert.setter
    def min_failing_periods_to_alert(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfEvaluationPeriods")
    def number_of_evaluation_periods(self) -> pulumi.Input[_builtins.float]: ...
    @number_of_evaluation_periods.setter
    def number_of_evaluation_periods(self, value: pulumi.Input[_builtins.float]): ...

class EmailNotificationArgsDict(TypedDict):
    custom_emails: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    send_to_subscription_administrator: NotRequired[pulumi.Input[_builtins.bool]]
    send_to_subscription_co_administrators: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class EmailNotificationArgs:
    def __init__(
        __self__,
        *,
        custom_emails: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        send_to_subscription_administrator: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        send_to_subscription_co_administrators: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customEmails")
    def custom_emails(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @custom_emails.setter
    def custom_emails(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sendToSubscriptionAdministrator")
    def send_to_subscription_administrator(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @send_to_subscription_administrator.setter
    def send_to_subscription_administrator(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sendToSubscriptionCoAdministrators")
    def send_to_subscription_co_administrators(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @send_to_subscription_co_administrators.setter
    def send_to_subscription_co_administrators(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class EmailReceiverArgsDict(TypedDict):
    email_address: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    use_common_alert_schema: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class EmailReceiverArgs:
    def __init__(
        __self__,
        *,
        email_address: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        use_common_alert_schema: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Input[_builtins.str]: ...
    @email_address.setter
    def email_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class EntityAlertsArgsDict(TypedDict):
    degraded: NotRequired[pulumi.Input[AlertConfigurationArgsDict]]
    unhealthy: NotRequired[pulumi.Input[AlertConfigurationArgsDict]]

@pulumi.input_type
class EntityAlertsArgs:
    def __init__(
        __self__,
        *,
        degraded: Optional[pulumi.Input[AlertConfigurationArgs]] = ...,
        unhealthy: Optional[pulumi.Input[AlertConfigurationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def degraded(self) -> Optional[pulumi.Input[AlertConfigurationArgs]]: ...
    @degraded.setter
    def degraded(self, value: Optional[pulumi.Input[AlertConfigurationArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def unhealthy(self) -> Optional[pulumi.Input[AlertConfigurationArgs]]: ...
    @unhealthy.setter
    def unhealthy(self, value: Optional[pulumi.Input[AlertConfigurationArgs]]): ...

class EntityCoordinatesArgsDict(TypedDict):
    x: pulumi.Input[_builtins.float]
    y: pulumi.Input[_builtins.float]

@pulumi.input_type
class EntityCoordinatesArgs:
    def __init__(
        __self__, *, x: pulumi.Input[_builtins.float], y: pulumi.Input[_builtins.float]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def x(self) -> pulumi.Input[_builtins.float]: ...
    @x.setter
    def x(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter
    def y(self) -> pulumi.Input[_builtins.float]: ...
    @y.setter
    def y(self, value: pulumi.Input[_builtins.float]): ...

class EntityPropertiesArgsDict(TypedDict):
    alerts: NotRequired[pulumi.Input[EntityAlertsArgsDict]]
    canvas_position: NotRequired[pulumi.Input[EntityCoordinatesArgsDict]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    health_objective: NotRequired[pulumi.Input[_builtins.float]]
    icon: NotRequired[pulumi.Input[IconDefinitionArgsDict]]
    impact: NotRequired[pulumi.Input[Union[_builtins.str, EntityImpact]]]
    kind: NotRequired[pulumi.Input[_builtins.str]]
    signals: NotRequired[pulumi.Input[SignalGroupArgsDict]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class EntityPropertiesArgs:
    def __init__(
        __self__,
        *,
        alerts: Optional[pulumi.Input[EntityAlertsArgs]] = ...,
        canvas_position: Optional[pulumi.Input[EntityCoordinatesArgs]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        health_objective: Optional[pulumi.Input[_builtins.float]] = ...,
        icon: Optional[pulumi.Input[IconDefinitionArgs]] = ...,
        impact: Optional[pulumi.Input[Union[_builtins.str, EntityImpact]]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        signals: Optional[pulumi.Input[SignalGroupArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alerts(self) -> Optional[pulumi.Input[EntityAlertsArgs]]: ...
    @alerts.setter
    def alerts(self, value: Optional[pulumi.Input[EntityAlertsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="canvasPosition")
    def canvas_position(self) -> Optional[pulumi.Input[EntityCoordinatesArgs]]: ...
    @canvas_position.setter
    def canvas_position(self, value: Optional[pulumi.Input[EntityCoordinatesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="healthObjective")
    def health_objective(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @health_objective.setter
    def health_objective(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def icon(self) -> Optional[pulumi.Input[IconDefinitionArgs]]: ...
    @icon.setter
    def icon(self, value: Optional[pulumi.Input[IconDefinitionArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def impact(self) -> Optional[pulumi.Input[Union[_builtins.str, EntityImpact]]]: ...
    @impact.setter
    def impact(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EntityImpact]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def signals(self) -> Optional[pulumi.Input[SignalGroupArgs]]: ...
    @signals.setter
    def signals(self, value: Optional[pulumi.Input[SignalGroupArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class EvaluationRuleArgsDict(TypedDict):
    degraded_rule: NotRequired[pulumi.Input[ThresholdRuleArgsDict]]
    dynamic_detection_rule: NotRequired[pulumi.Input[DynamicDetectionRuleArgsDict]]
    unhealthy_rule: NotRequired[pulumi.Input[ThresholdRuleArgsDict]]

@pulumi.input_type
class EvaluationRuleArgs:
    def __init__(
        __self__,
        *,
        degraded_rule: Optional[pulumi.Input[ThresholdRuleArgs]] = ...,
        dynamic_detection_rule: Optional[pulumi.Input[DynamicDetectionRuleArgs]] = ...,
        unhealthy_rule: Optional[pulumi.Input[ThresholdRuleArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="degradedRule")
    def degraded_rule(self) -> Optional[pulumi.Input[ThresholdRuleArgs]]: ...
    @degraded_rule.setter
    def degraded_rule(self, value: Optional[pulumi.Input[ThresholdRuleArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="dynamicDetectionRule")
    def dynamic_detection_rule(
        self,
    ) -> Optional[pulumi.Input[DynamicDetectionRuleArgs]]: ...
    @dynamic_detection_rule.setter
    def dynamic_detection_rule(
        self, value: Optional[pulumi.Input[DynamicDetectionRuleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="unhealthyRule")
    def unhealthy_rule(self) -> Optional[pulumi.Input[ThresholdRuleArgs]]: ...
    @unhealthy_rule.setter
    def unhealthy_rule(self, value: Optional[pulumi.Input[ThresholdRuleArgs]]): ...

class EventHubDestinationArgsDict(TypedDict):
    event_hub_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventHubDestinationArgs:
    def __init__(
        __self__,
        *,
        event_hub_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_hub_resource_id.setter
    def event_hub_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventHubDirectDestinationArgsDict(TypedDict):
    event_hub_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventHubDirectDestinationArgs:
    def __init__(
        __self__,
        *,
        event_hub_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event_hub_resource_id.setter
    def event_hub_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventHubReceiverArgsDict(TypedDict):
    event_hub_name: pulumi.Input[_builtins.str]
    event_hub_name_space: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    subscription_id: pulumi.Input[_builtins.str]
    managed_identity: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    use_common_alert_schema: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class EventHubReceiverArgs:
    def __init__(
        __self__,
        *,
        event_hub_name: pulumi.Input[_builtins.str],
        event_hub_name_space: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        subscription_id: pulumi.Input[_builtins.str],
        managed_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        use_common_alert_schema: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> pulumi.Input[_builtins.str]: ...
    @event_hub_name.setter
    def event_hub_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eventHubNameSpace")
    def event_hub_name_space(self) -> pulumi.Input[_builtins.str]: ...
    @event_hub_name_space.setter
    def event_hub_name_space(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Input[_builtins.str]: ...
    @subscription_id.setter
    def subscription_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_identity.setter
    def managed_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ExporterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[Union[_builtins.str, ExporterType]]
    azure_monitor_workspace_logs: NotRequired[
        pulumi.Input[AzureMonitorWorkspaceLogsExporterArgsDict]
    ]
    tcp: NotRequired[pulumi.Input[TcpExporterArgsDict]]

@pulumi.input_type
class ExporterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[Union[_builtins.str, ExporterType]],
        azure_monitor_workspace_logs: Optional[
            pulumi.Input[AzureMonitorWorkspaceLogsExporterArgs]
        ] = ...,
        tcp: Optional[pulumi.Input[TcpExporterArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ExporterType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ExporterType]]): ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorWorkspaceLogs")
    def azure_monitor_workspace_logs(
        self,
    ) -> Optional[pulumi.Input[AzureMonitorWorkspaceLogsExporterArgs]]: ...
    @azure_monitor_workspace_logs.setter
    def azure_monitor_workspace_logs(
        self, value: Optional[pulumi.Input[AzureMonitorWorkspaceLogsExporterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tcp(self) -> Optional[pulumi.Input[TcpExporterArgs]]: ...
    @tcp.setter
    def tcp(self, value: Optional[pulumi.Input[TcpExporterArgs]]): ...

class ExtensionDataSourceArgsDict(TypedDict):
    extension_name: pulumi.Input[_builtins.str]
    extension_settings: NotRequired[Any]
    input_data_sources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    streams: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[Union[_builtins.str, KnownExtensionDataSourceStreams]]
            ]
        ]
    ]

@pulumi.input_type
class ExtensionDataSourceArgs:
    def __init__(
        __self__,
        *,
        extension_name: pulumi.Input[_builtins.str],
        extension_settings: Optional[Any] = ...,
        input_data_sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        streams: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[_builtins.str, KnownExtensionDataSourceStreams]]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="extensionName")
    def extension_name(self) -> pulumi.Input[_builtins.str]: ...
    @extension_name.setter
    def extension_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="extensionSettings")
    def extension_settings(self) -> Optional[Any]: ...
    @extension_settings.setter
    def extension_settings(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="inputDataSources")
    def input_data_sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @input_data_sources.setter
    def input_data_sources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def streams(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[Union[_builtins.str, KnownExtensionDataSourceStreams]]
            ]
        ]
    ]: ...
    @streams.setter
    def streams(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[_builtins.str, KnownExtensionDataSourceStreams]]
                ]
            ]
        ],
    ): ...

class HealthModelPropertiesArgsDict(TypedDict):
    discovery: NotRequired[pulumi.Input[ModelDiscoverySettingsArgsDict]]

@pulumi.input_type
class HealthModelPropertiesArgs:
    def __init__(
        __self__, *, discovery: Optional[pulumi.Input[ModelDiscoverySettingsArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def discovery(self) -> Optional[pulumi.Input[ModelDiscoverySettingsArgs]]: ...
    @discovery.setter
    def discovery(self, value: Optional[pulumi.Input[ModelDiscoverySettingsArgs]]): ...

class IconDefinitionArgsDict(TypedDict):
    icon_name: pulumi.Input[_builtins.str]
    custom_data: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IconDefinitionArgs:
    def __init__(
        __self__,
        *,
        icon_name: pulumi.Input[_builtins.str],
        custom_data: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iconName")
    def icon_name(self) -> pulumi.Input[_builtins.str]: ...
    @icon_name.setter
    def icon_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customData")
    def custom_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_data.setter
    def custom_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IdentityArgsDict(TypedDict):
    type: pulumi.Input[IdentityType]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class IdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[IdentityType],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[IdentityType]: ...
    @type.setter
    def type(self, value: pulumi.Input[IdentityType]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class IisLogsDataSourceArgsDict(TypedDict):
    streams: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    log_directories: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IisLogsDataSourceArgs:
    def __init__(
        __self__,
        *,
        streams: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        log_directories: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @streams.setter
    def streams(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="logDirectories")
    def log_directories(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @log_directories.setter
    def log_directories(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IncidentReceiverArgsDict(TypedDict):
    connection: pulumi.Input[IncidentServiceConnectionArgsDict]
    incident_management_service: pulumi.Input[
        Union[_builtins.str, IncidentManagementService]
    ]
    mappings: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class IncidentReceiverArgs:
    def __init__(
        __self__,
        *,
        connection: pulumi.Input[IncidentServiceConnectionArgs],
        incident_management_service: pulumi.Input[
            Union[_builtins.str, IncidentManagementService]
        ],
        mappings: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connection(self) -> pulumi.Input[IncidentServiceConnectionArgs]: ...
    @connection.setter
    def connection(self, value: pulumi.Input[IncidentServiceConnectionArgs]): ...
    @_builtins.property
    @pulumi.getter(name="incidentManagementService")
    def incident_management_service(
        self,
    ) -> pulumi.Input[Union[_builtins.str, IncidentManagementService]]: ...
    @incident_management_service.setter
    def incident_management_service(
        self, value: pulumi.Input[Union[_builtins.str, IncidentManagementService]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mappings(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @mappings.setter
    def mappings(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class IncidentServiceConnectionArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class IncidentServiceConnectionArgs:
    def __init__(
        __self__, *, id: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class IssuePropertiesArgsDict(TypedDict):
    impact_time: pulumi.Input[_builtins.str]
    severity: pulumi.Input[_builtins.str]
    status: pulumi.Input[Union[_builtins.str, Status]]
    title: pulumi.Input[_builtins.str]

@pulumi.input_type
class IssuePropertiesArgs:
    def __init__(
        __self__,
        *,
        impact_time: pulumi.Input[_builtins.str],
        severity: pulumi.Input[_builtins.str],
        status: pulumi.Input[Union[_builtins.str, Status]],
        title: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="impactTime")
    def impact_time(self) -> pulumi.Input[_builtins.str]: ...
    @impact_time.setter
    def impact_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[_builtins.str]: ...
    @severity.setter
    def severity(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[_builtins.str, Status]]: ...
    @status.setter
    def status(self, value: pulumi.Input[Union[_builtins.str, Status]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...

class ItsmReceiverArgsDict(TypedDict):
    connection_id: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    region: pulumi.Input[_builtins.str]
    ticket_configuration: pulumi.Input[_builtins.str]
    workspace_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ItsmReceiverArgs:
    def __init__(
        __self__,
        *,
        connection_id: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        region: pulumi.Input[_builtins.str],
        ticket_configuration: pulumi.Input[_builtins.str],
        workspace_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Input[_builtins.str]: ...
    @connection_id.setter
    def connection_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ticketConfiguration")
    def ticket_configuration(self) -> pulumi.Input[_builtins.str]: ...
    @ticket_configuration.setter
    def ticket_configuration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): ...

class JsonArrayMapperArgsDict(TypedDict):
    keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    destination_field: NotRequired[pulumi.Input[JsonMapperDestinationFieldArgsDict]]
    source_field: NotRequired[pulumi.Input[JsonMapperSourceFieldArgsDict]]

@pulumi.input_type
class JsonArrayMapperArgs:
    def __init__(
        __self__,
        *,
        keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        destination_field: Optional[pulumi.Input[JsonMapperDestinationFieldArgs]] = ...,
        source_field: Optional[pulumi.Input[JsonMapperSourceFieldArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def keys(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @keys.setter
    def keys(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationField")
    def destination_field(
        self,
    ) -> Optional[pulumi.Input[JsonMapperDestinationFieldArgs]]: ...
    @destination_field.setter
    def destination_field(
        self, value: Optional[pulumi.Input[JsonMapperDestinationFieldArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceField")
    def source_field(self) -> Optional[pulumi.Input[JsonMapperSourceFieldArgs]]: ...
    @source_field.setter
    def source_field(
        self, value: Optional[pulumi.Input[JsonMapperSourceFieldArgs]]
    ): ...

class JsonMapperDestinationFieldArgsDict(TypedDict):
    destination: NotRequired[pulumi.Input[Union[_builtins.str, JsonMapperElement]]]
    field_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JsonMapperDestinationFieldArgs:
    def __init__(
        __self__,
        *,
        destination: Optional[
            pulumi.Input[Union[_builtins.str, JsonMapperElement]]
        ] = ...,
        field_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, JsonMapperElement]]]: ...
    @destination.setter
    def destination(
        self, value: Optional[pulumi.Input[Union[_builtins.str, JsonMapperElement]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field_name.setter
    def field_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JsonMapperSourceFieldArgsDict(TypedDict):
    field_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JsonMapperSourceFieldArgs:
    def __init__(
        __self__, *, field_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field_name.setter
    def field_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogAnalyticsDestinationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    workspace_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogAnalyticsDestinationArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_resource_id.setter
    def workspace_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogAnalyticsQuerySignalDefinitionPropertiesArgsDict(TypedDict):
    evaluation_rules: pulumi.Input[EvaluationRuleArgsDict]
    query_text: pulumi.Input[_builtins.str]
    signal_kind: pulumi.Input[_builtins.str]
    data_unit: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    refresh_interval: NotRequired[pulumi.Input[Union[_builtins.str, RefreshInterval]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    time_grain: NotRequired[pulumi.Input[_builtins.str]]
    value_column_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogAnalyticsQuerySignalDefinitionPropertiesArgs:
    def __init__(
        __self__,
        *,
        evaluation_rules: pulumi.Input[EvaluationRuleArgs],
        query_text: pulumi.Input[_builtins.str],
        signal_kind: pulumi.Input[_builtins.str],
        data_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        refresh_interval: Optional[
            pulumi.Input[Union[_builtins.str, RefreshInterval]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        time_grain: Optional[pulumi.Input[_builtins.str]] = ...,
        value_column_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="evaluationRules")
    def evaluation_rules(self) -> pulumi.Input[EvaluationRuleArgs]: ...
    @evaluation_rules.setter
    def evaluation_rules(self, value: pulumi.Input[EvaluationRuleArgs]): ...
    @_builtins.property
    @pulumi.getter(name="queryText")
    def query_text(self) -> pulumi.Input[_builtins.str]: ...
    @query_text.setter
    def query_text(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="signalKind")
    def signal_kind(self) -> pulumi.Input[_builtins.str]: ...
    @signal_kind.setter
    def signal_kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataUnit")
    def data_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_unit.setter
    def data_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RefreshInterval]]]: ...
    @refresh_interval.setter
    def refresh_interval(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RefreshInterval]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_grain.setter
    def time_grain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="valueColumnName")
    def value_column_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value_column_name.setter
    def value_column_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogAnalyticsSignalGroupArgsDict(TypedDict):
    authentication_setting: pulumi.Input[_builtins.str]
    log_analytics_workspace_resource_id: pulumi.Input[_builtins.str]
    signal_assignments: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SignalAssignmentArgsDict]]]
    ]

@pulumi.input_type
class LogAnalyticsSignalGroupArgs:
    def __init__(
        __self__,
        *,
        authentication_setting: pulumi.Input[_builtins.str],
        log_analytics_workspace_resource_id: pulumi.Input[_builtins.str],
        signal_assignments: Optional[
            pulumi.Input[Sequence[pulumi.Input[SignalAssignmentArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationSetting")
    def authentication_setting(self) -> pulumi.Input[_builtins.str]: ...
    @authentication_setting.setter
    def authentication_setting(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsWorkspaceResourceId")
    def log_analytics_workspace_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @log_analytics_workspace_resource_id.setter
    def log_analytics_workspace_resource_id(
        self, value: pulumi.Input[_builtins.str]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signalAssignments")
    def signal_assignments(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SignalAssignmentArgs]]]]: ...
    @signal_assignments.setter
    def signal_assignments(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SignalAssignmentArgs]]]],
    ): ...

class LogFileSettingsTextArgsDict(TypedDict):
    record_start_timestamp_format: pulumi.Input[
        Union[_builtins.str, KnownLogFileTextSettingsRecordStartTimestampFormat]
    ]

@pulumi.input_type
class LogFileSettingsTextArgs:
    def __init__(
        __self__,
        *,
        record_start_timestamp_format: pulumi.Input[
            Union[_builtins.str, KnownLogFileTextSettingsRecordStartTimestampFormat]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordStartTimestampFormat")
    def record_start_timestamp_format(
        self,
    ) -> pulumi.Input[
        Union[_builtins.str, KnownLogFileTextSettingsRecordStartTimestampFormat]
    ]: ...
    @record_start_timestamp_format.setter
    def record_start_timestamp_format(
        self,
        value: pulumi.Input[
            Union[_builtins.str, KnownLogFileTextSettingsRecordStartTimestampFormat]
        ],
    ): ...

class LogFilesDataSourceSettingsArgsDict(TypedDict):
    text: NotRequired[pulumi.Input[LogFileSettingsTextArgsDict]]

@pulumi.input_type
class LogFilesDataSourceSettingsArgs:
    def __init__(
        __self__, *, text: Optional[pulumi.Input[LogFileSettingsTextArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[LogFileSettingsTextArgs]]: ...
    @text.setter
    def text(self, value: Optional[pulumi.Input[LogFileSettingsTextArgs]]): ...

class LogFilesDataSourceArgsDict(TypedDict):
    file_patterns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    format: pulumi.Input[Union[_builtins.str, KnownLogFilesDataSourceFormat]]
    streams: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    settings: NotRequired[pulumi.Input[LogFilesDataSourceSettingsArgsDict]]

@pulumi.input_type
class LogFilesDataSourceArgs:
    def __init__(
        __self__,
        *,
        file_patterns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        format: pulumi.Input[Union[_builtins.str, KnownLogFilesDataSourceFormat]],
        streams: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        settings: Optional[pulumi.Input[LogFilesDataSourceSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filePatterns")
    def file_patterns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @file_patterns.setter
    def file_patterns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def format(
        self,
    ) -> pulumi.Input[Union[_builtins.str, KnownLogFilesDataSourceFormat]]: ...
    @format.setter
    def format(
        self, value: pulumi.Input[Union[_builtins.str, KnownLogFilesDataSourceFormat]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @streams.setter
    def streams(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[LogFilesDataSourceSettingsArgs]]: ...
    @settings.setter
    def settings(
        self, value: Optional[pulumi.Input[LogFilesDataSourceSettingsArgs]]
    ): ...

class LogSettingsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    category: NotRequired[pulumi.Input[_builtins.str]]
    category_group: NotRequired[pulumi.Input[_builtins.str]]
    retention_policy: NotRequired[pulumi.Input[RetentionPolicyArgsDict]]

@pulumi.input_type
class LogSettingsArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        category_group: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_policy: Optional[pulumi.Input[RetentionPolicyArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="categoryGroup")
    def category_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category_group.setter
    def category_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[pulumi.Input[RetentionPolicyArgs]]: ...
    @retention_policy.setter
    def retention_policy(self, value: Optional[pulumi.Input[RetentionPolicyArgs]]): ...

class LogicAppReceiverArgsDict(TypedDict):
    callback_url: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    resource_id: pulumi.Input[_builtins.str]
    managed_identity: NotRequired[pulumi.Input[_builtins.str]]
    use_common_alert_schema: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class LogicAppReceiverArgs:
    def __init__(
        __self__,
        *,
        callback_url: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        resource_id: pulumi.Input[_builtins.str],
        managed_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        use_common_alert_schema: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="callbackUrl")
    def callback_url(self) -> pulumi.Input[_builtins.str]: ...
    @callback_url.setter
    def callback_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_identity.setter
    def managed_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ManagedIdentityAuthenticationSettingPropertiesArgsDict(TypedDict):
    authentication_kind: pulumi.Input[_builtins.str]
    managed_identity_name: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagedIdentityAuthenticationSettingPropertiesArgs:
    def __init__(
        __self__,
        *,
        authentication_kind: pulumi.Input[_builtins.str],
        managed_identity_name: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationKind")
    def authentication_kind(self) -> pulumi.Input[_builtins.str]: ...
    @authentication_kind.setter
    def authentication_kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managedIdentityName")
    def managed_identity_name(self) -> pulumi.Input[_builtins.str]: ...
    @managed_identity_name.setter
    def managed_identity_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedServiceIdentityArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ManagementGroupLogSettingsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    category: NotRequired[pulumi.Input[_builtins.str]]
    category_group: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagementGroupLogSettingsArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        category_group: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="categoryGroup")
    def category_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category_group.setter
    def category_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetricAlertActionArgsDict(TypedDict):
    action_group_id: NotRequired[pulumi.Input[_builtins.str]]
    web_hook_properties: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class MetricAlertActionArgs:
    def __init__(
        __self__,
        *,
        action_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        web_hook_properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action_group_id.setter
    def action_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webHookProperties")
    def web_hook_properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @web_hook_properties.setter
    def web_hook_properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class MetricAlertMultipleResourceMultipleMetricCriteriaArgsDict(TypedDict):
    odata_type: pulumi.Input[_builtins.str]
    all_of: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[DynamicMetricCriteriaArgsDict, MetricCriteriaArgsDict]
                ]
            ]
        ]
    ]

@pulumi.input_type
class MetricAlertMultipleResourceMultipleMetricCriteriaArgs:
    def __init__(
        __self__,
        *,
        odata_type: pulumi.Input[_builtins.str],
        all_of: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[DynamicMetricCriteriaArgs, MetricCriteriaArgs]]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[_builtins.str]: ...
    @odata_type.setter
    def odata_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allOf")
    def all_of(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[DynamicMetricCriteriaArgs, MetricCriteriaArgs]]]
        ]
    ]: ...
    @all_of.setter
    def all_of(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[DynamicMetricCriteriaArgs, MetricCriteriaArgs]]
                ]
            ]
        ],
    ): ...

class MetricAlertSingleResourceMultipleMetricCriteriaArgsDict(TypedDict):
    odata_type: pulumi.Input[_builtins.str]
    all_of: NotRequired[pulumi.Input[Sequence[pulumi.Input[MetricCriteriaArgsDict]]]]

@pulumi.input_type
class MetricAlertSingleResourceMultipleMetricCriteriaArgs:
    def __init__(
        __self__,
        *,
        odata_type: pulumi.Input[_builtins.str],
        all_of: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricCriteriaArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[_builtins.str]: ...
    @odata_type.setter
    def odata_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allOf")
    def all_of(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetricCriteriaArgs]]]]: ...
    @all_of.setter
    def all_of(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MetricCriteriaArgs]]]]
    ): ...

class MetricCriteriaArgsDict(TypedDict):
    criterion_type: pulumi.Input[_builtins.str]
    metric_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    operator: pulumi.Input[Union[_builtins.str, Operator]]
    threshold: pulumi.Input[_builtins.float]
    time_aggregation: pulumi.Input[Union[_builtins.str, AggregationTypeEnum]]
    dimensions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgsDict]]]
    ]
    metric_namespace: NotRequired[pulumi.Input[_builtins.str]]
    skip_metric_validation: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class MetricCriteriaArgs:
    def __init__(
        __self__,
        *,
        criterion_type: pulumi.Input[_builtins.str],
        metric_name: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        operator: pulumi.Input[Union[_builtins.str, Operator]],
        threshold: pulumi.Input[_builtins.float],
        time_aggregation: pulumi.Input[Union[_builtins.str, AggregationTypeEnum]],
        dimensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgs]]]
        ] = ...,
        metric_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_metric_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="criterionType")
    def criterion_type(self) -> pulumi.Input[_builtins.str]: ...
    @criterion_type.setter
    def criterion_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, Operator]]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, Operator]]): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[_builtins.float]: ...
    @threshold.setter
    def threshold(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="timeAggregation")
    def time_aggregation(
        self,
    ) -> pulumi.Input[Union[_builtins.str, AggregationTypeEnum]]: ...
    @time_aggregation.setter
    def time_aggregation(
        self, value: pulumi.Input[Union[_builtins.str, AggregationTypeEnum]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgs]]]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MetricDimensionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_namespace.setter
    def metric_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipMetricValidation")
    def skip_metric_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_metric_validation.setter
    def skip_metric_validation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class MetricDimensionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    operator: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class MetricDimensionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        operator: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[_builtins.str]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class MetricSettingsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    category: NotRequired[pulumi.Input[_builtins.str]]
    retention_policy: NotRequired[pulumi.Input[RetentionPolicyArgsDict]]
    time_grain: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetricSettingsArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_policy: Optional[pulumi.Input[RetentionPolicyArgs]] = ...,
        time_grain: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[pulumi.Input[RetentionPolicyArgs]]: ...
    @retention_policy.setter
    def retention_policy(self, value: Optional[pulumi.Input[RetentionPolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_grain.setter
    def time_grain(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetricTriggerArgsDict(TypedDict):
    metric_name: pulumi.Input[_builtins.str]
    metric_resource_uri: pulumi.Input[_builtins.str]
    operator: pulumi.Input[ComparisonOperationType]
    statistic: pulumi.Input[MetricStatisticType]
    threshold: pulumi.Input[_builtins.float]
    time_aggregation: pulumi.Input[TimeAggregationType]
    time_grain: pulumi.Input[_builtins.str]
    time_window: pulumi.Input[_builtins.str]
    dimensions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ScaleRuleMetricDimensionArgsDict]]]
    ]
    divide_per_instance: NotRequired[pulumi.Input[_builtins.bool]]
    metric_namespace: NotRequired[pulumi.Input[_builtins.str]]
    metric_resource_location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetricTriggerArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        metric_resource_uri: pulumi.Input[_builtins.str],
        operator: pulumi.Input[ComparisonOperationType],
        statistic: pulumi.Input[MetricStatisticType],
        threshold: pulumi.Input[_builtins.float],
        time_aggregation: pulumi.Input[TimeAggregationType],
        time_grain: pulumi.Input[_builtins.str],
        time_window: pulumi.Input[_builtins.str],
        dimensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ScaleRuleMetricDimensionArgs]]]
        ] = ...,
        divide_per_instance: Optional[pulumi.Input[_builtins.bool]] = ...,
        metric_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        metric_resource_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricResourceUri")
    def metric_resource_uri(self) -> pulumi.Input[_builtins.str]: ...
    @metric_resource_uri.setter
    def metric_resource_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[ComparisonOperationType]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[ComparisonOperationType]): ...
    @_builtins.property
    @pulumi.getter
    def statistic(self) -> pulumi.Input[MetricStatisticType]: ...
    @statistic.setter
    def statistic(self, value: pulumi.Input[MetricStatisticType]): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[_builtins.float]: ...
    @threshold.setter
    def threshold(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="timeAggregation")
    def time_aggregation(self) -> pulumi.Input[TimeAggregationType]: ...
    @time_aggregation.setter
    def time_aggregation(self, value: pulumi.Input[TimeAggregationType]): ...
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> pulumi.Input[_builtins.str]: ...
    @time_grain.setter
    def time_grain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> pulumi.Input[_builtins.str]: ...
    @time_window.setter
    def time_window(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ScaleRuleMetricDimensionArgs]]]
    ]: ...
    @dimensions.setter
    def dimensions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ScaleRuleMetricDimensionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dividePerInstance")
    def divide_per_instance(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @divide_per_instance.setter
    def divide_per_instance(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_namespace.setter
    def metric_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricResourceLocation")
    def metric_resource_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_resource_location.setter
    def metric_resource_location(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ModelDiscoverySettingsArgsDict(TypedDict):
    add_recommended_signals: pulumi.Input[
        Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
    ]
    scope: pulumi.Input[_builtins.str]
    identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ModelDiscoverySettingsArgs:
    def __init__(
        __self__,
        *,
        add_recommended_signals: pulumi.Input[
            Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
        ],
        scope: pulumi.Input[_builtins.str],
        identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addRecommendedSignals")
    def add_recommended_signals(
        self,
    ) -> pulumi.Input[
        Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
    ]: ...
    @add_recommended_signals.setter
    def add_recommended_signals(
        self,
        value: pulumi.Input[
            Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MonitoringAccountDestinationArgsDict(TypedDict):
    account_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MonitoringAccountDestinationArgs:
    def __init__(
        __self__,
        *,
        account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountResourceId")
    def account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_resource_id.setter
    def account_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkingConfigurationArgsDict(TypedDict):
    external_networking_mode: pulumi.Input[Union[_builtins.str, ExternalNetworkingMode]]
    routes: pulumi.Input[Sequence[pulumi.Input[NetworkingRouteArgsDict]]]
    host: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkingConfigurationArgs:
    def __init__(
        __self__,
        *,
        external_networking_mode: pulumi.Input[
            Union[_builtins.str, ExternalNetworkingMode]
        ],
        routes: pulumi.Input[Sequence[pulumi.Input[NetworkingRouteArgs]]],
        host: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalNetworkingMode")
    def external_networking_mode(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ExternalNetworkingMode]]: ...
    @external_networking_mode.setter
    def external_networking_mode(
        self, value: pulumi.Input[Union[_builtins.str, ExternalNetworkingMode]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> pulumi.Input[Sequence[pulumi.Input[NetworkingRouteArgs]]]: ...
    @routes.setter
    def routes(
        self, value: pulumi.Input[Sequence[pulumi.Input[NetworkingRouteArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkingRouteArgsDict(TypedDict):
    receiver: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    subdomain: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NetworkingRouteArgs:
    def __init__(
        __self__,
        *,
        receiver: pulumi.Input[_builtins.str],
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        subdomain: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def receiver(self) -> pulumi.Input[_builtins.str]: ...
    @receiver.setter
    def receiver(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def subdomain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subdomain.setter
    def subdomain(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OtlpReceiverArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]

@pulumi.input_type
class OtlpReceiverArgs:
    def __init__(__self__, *, endpoint: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...

class PerfCounterDataSourceArgsDict(TypedDict):
    counter_specifiers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    sampling_frequency_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    streams: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[Union[_builtins.str, KnownPerfCounterDataSourceStreams]]
            ]
        ]
    ]

@pulumi.input_type
class PerfCounterDataSourceArgs:
    def __init__(
        __self__,
        *,
        counter_specifiers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        sampling_frequency_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        streams: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[_builtins.str, KnownPerfCounterDataSourceStreams]
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="counterSpecifiers")
    def counter_specifiers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @counter_specifiers.setter
    def counter_specifiers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samplingFrequencyInSeconds")
    def sampling_frequency_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @sampling_frequency_in_seconds.setter
    def sampling_frequency_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def streams(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[Union[_builtins.str, KnownPerfCounterDataSourceStreams]]
            ]
        ]
    ]: ...
    @streams.setter
    def streams(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[_builtins.str, KnownPerfCounterDataSourceStreams]
                    ]
                ]
            ]
        ],
    ): ...

class PersistenceConfigurationsArgsDict(TypedDict):
    persistent_volume_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class PersistenceConfigurationsArgs:
    def __init__(
        __self__, *, persistent_volume_name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="persistentVolumeName")
    def persistent_volume_name(self) -> pulumi.Input[_builtins.str]: ...
    @persistent_volume_name.setter
    def persistent_volume_name(self, value: pulumi.Input[_builtins.str]): ...

class PipelineGroupPropertiesArgsDict(TypedDict):
    exporters: pulumi.Input[Sequence[pulumi.Input[ExporterArgsDict]]]
    processors: pulumi.Input[Sequence[pulumi.Input[ProcessorArgsDict]]]
    receivers: pulumi.Input[Sequence[pulumi.Input[ReceiverArgsDict]]]
    service: pulumi.Input[ServiceArgsDict]
    networking_configurations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NetworkingConfigurationArgsDict]]]
    ]
    replicas: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class PipelineGroupPropertiesArgs:
    def __init__(
        __self__,
        *,
        exporters: pulumi.Input[Sequence[pulumi.Input[ExporterArgs]]],
        processors: pulumi.Input[Sequence[pulumi.Input[ProcessorArgs]]],
        receivers: pulumi.Input[Sequence[pulumi.Input[ReceiverArgs]]],
        service: pulumi.Input[ServiceArgs],
        networking_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkingConfigurationArgs]]]
        ] = ...,
        replicas: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exporters(self) -> pulumi.Input[Sequence[pulumi.Input[ExporterArgs]]]: ...
    @exporters.setter
    def exporters(self, value: pulumi.Input[Sequence[pulumi.Input[ExporterArgs]]]): ...
    @_builtins.property
    @pulumi.getter
    def processors(self) -> pulumi.Input[Sequence[pulumi.Input[ProcessorArgs]]]: ...
    @processors.setter
    def processors(
        self, value: pulumi.Input[Sequence[pulumi.Input[ProcessorArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def receivers(self) -> pulumi.Input[Sequence[pulumi.Input[ReceiverArgs]]]: ...
    @receivers.setter
    def receivers(self, value: pulumi.Input[Sequence[pulumi.Input[ReceiverArgs]]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[ServiceArgs]: ...
    @service.setter
    def service(self, value: pulumi.Input[ServiceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="networkingConfigurations")
    def networking_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NetworkingConfigurationArgs]]]
    ]: ...
    @networking_configurations.setter
    def networking_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NetworkingConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PipelineArgsDict(TypedDict):
    exporters: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    name: pulumi.Input[_builtins.str]
    receivers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    type: pulumi.Input[Union[_builtins.str, PipelineType]]
    processors: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class PipelineArgs:
    def __init__(
        __self__,
        *,
        exporters: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        name: pulumi.Input[_builtins.str],
        receivers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        type: pulumi.Input[Union[_builtins.str, PipelineType]],
        processors: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exporters(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @exporters.setter
    def exporters(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def receivers(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @receivers.setter
    def receivers(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, PipelineType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, PipelineType]]): ...
    @_builtins.property
    @pulumi.getter
    def processors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @processors.setter
    def processors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PlatformTelemetryDataSourceArgsDict(TypedDict):
    streams: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PlatformTelemetryDataSourceArgs:
    def __init__(
        __self__,
        *,
        streams: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @streams.setter
    def streams(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PredictiveAutoscalePolicyArgsDict(TypedDict):
    scale_mode: pulumi.Input[PredictiveAutoscalePolicyScaleMode]
    scale_look_ahead_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PredictiveAutoscalePolicyArgs:
    def __init__(
        __self__,
        *,
        scale_mode: pulumi.Input[PredictiveAutoscalePolicyScaleMode],
        scale_look_ahead_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scaleMode")
    def scale_mode(self) -> pulumi.Input[PredictiveAutoscalePolicyScaleMode]: ...
    @scale_mode.setter
    def scale_mode(self, value: pulumi.Input[PredictiveAutoscalePolicyScaleMode]): ...
    @_builtins.property
    @pulumi.getter(name="scaleLookAheadTime")
    def scale_look_ahead_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scale_look_ahead_time.setter
    def scale_look_ahead_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ],
    ): ...

class ProcessorArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[Union[_builtins.str, ProcessorType]]
    batch: NotRequired[pulumi.Input[BatchProcessorArgsDict]]

@pulumi.input_type
class ProcessorArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[Union[_builtins.str, ProcessorType]],
        batch: Optional[pulumi.Input[BatchProcessorArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ProcessorType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ProcessorType]]): ...
    @_builtins.property
    @pulumi.getter
    def batch(self) -> Optional[pulumi.Input[BatchProcessorArgs]]: ...
    @batch.setter
    def batch(self, value: Optional[pulumi.Input[BatchProcessorArgs]]): ...

class PrometheusForwarderDataSourceArgsDict(TypedDict):
    label_include_filter: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    streams: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[_builtins.str, KnownPrometheusForwarderDataSourceStreams]
                ]
            ]
        ]
    ]

@pulumi.input_type
class PrometheusForwarderDataSourceArgs:
    def __init__(
        __self__,
        *,
        label_include_filter: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        streams: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[_builtins.str, KnownPrometheusForwarderDataSourceStreams]
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labelIncludeFilter")
    def label_include_filter(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @label_include_filter.setter
    def label_include_filter(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def streams(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[_builtins.str, KnownPrometheusForwarderDataSourceStreams]
                ]
            ]
        ]
    ]: ...
    @streams.setter
    def streams(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[_builtins.str, KnownPrometheusForwarderDataSourceStreams]
                    ]
                ]
            ]
        ],
    ): ...

class PrometheusMetricsSignalDefinitionPropertiesArgsDict(TypedDict):
    evaluation_rules: pulumi.Input[EvaluationRuleArgsDict]
    query_text: pulumi.Input[_builtins.str]
    signal_kind: pulumi.Input[_builtins.str]
    data_unit: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    refresh_interval: NotRequired[pulumi.Input[Union[_builtins.str, RefreshInterval]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    time_grain: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrometheusMetricsSignalDefinitionPropertiesArgs:
    def __init__(
        __self__,
        *,
        evaluation_rules: pulumi.Input[EvaluationRuleArgs],
        query_text: pulumi.Input[_builtins.str],
        signal_kind: pulumi.Input[_builtins.str],
        data_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        refresh_interval: Optional[
            pulumi.Input[Union[_builtins.str, RefreshInterval]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        time_grain: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="evaluationRules")
    def evaluation_rules(self) -> pulumi.Input[EvaluationRuleArgs]: ...
    @evaluation_rules.setter
    def evaluation_rules(self, value: pulumi.Input[EvaluationRuleArgs]): ...
    @_builtins.property
    @pulumi.getter(name="queryText")
    def query_text(self) -> pulumi.Input[_builtins.str]: ...
    @query_text.setter
    def query_text(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="signalKind")
    def signal_kind(self) -> pulumi.Input[_builtins.str]: ...
    @signal_kind.setter
    def signal_kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataUnit")
    def data_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_unit.setter
    def data_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RefreshInterval]]]: ...
    @refresh_interval.setter
    def refresh_interval(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RefreshInterval]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_grain.setter
    def time_grain(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReceiverArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[Union[_builtins.str, ReceiverType]]
    otlp: NotRequired[pulumi.Input[OtlpReceiverArgsDict]]
    syslog: NotRequired[pulumi.Input[SyslogReceiverArgsDict]]
    udp: NotRequired[pulumi.Input[UdpReceiverArgsDict]]

@pulumi.input_type
class ReceiverArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[Union[_builtins.str, ReceiverType]],
        otlp: Optional[pulumi.Input[OtlpReceiverArgs]] = ...,
        syslog: Optional[pulumi.Input[SyslogReceiverArgs]] = ...,
        udp: Optional[pulumi.Input[UdpReceiverArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ReceiverType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ReceiverType]]): ...
    @_builtins.property
    @pulumi.getter
    def otlp(self) -> Optional[pulumi.Input[OtlpReceiverArgs]]: ...
    @otlp.setter
    def otlp(self, value: Optional[pulumi.Input[OtlpReceiverArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def syslog(self) -> Optional[pulumi.Input[SyslogReceiverArgs]]: ...
    @syslog.setter
    def syslog(self, value: Optional[pulumi.Input[SyslogReceiverArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def udp(self) -> Optional[pulumi.Input[UdpReceiverArgs]]: ...
    @udp.setter
    def udp(self, value: Optional[pulumi.Input[UdpReceiverArgs]]): ...

class RecordMapArgsDict(TypedDict):
    from_: pulumi.Input[_builtins.str]
    to: pulumi.Input[_builtins.str]

@pulumi.input_type
class RecordMapArgs:
    def __init__(
        __self__, *, from_: pulumi.Input[_builtins.str], to: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> pulumi.Input[_builtins.str]: ...
    @from_.setter
    def from_(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> pulumi.Input[_builtins.str]: ...
    @to.setter
    def to(self, value: pulumi.Input[_builtins.str]): ...

class RecurrenceArgsDict(TypedDict):
    frequency: pulumi.Input[RecurrenceFrequency]
    schedule: pulumi.Input[RecurrentScheduleArgsDict]

@pulumi.input_type
class RecurrenceArgs:
    def __init__(
        __self__,
        *,
        frequency: pulumi.Input[RecurrenceFrequency],
        schedule: pulumi.Input[RecurrentScheduleArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[RecurrenceFrequency]: ...
    @frequency.setter
    def frequency(self, value: pulumi.Input[RecurrenceFrequency]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> pulumi.Input[RecurrentScheduleArgs]: ...
    @schedule.setter
    def schedule(self, value: pulumi.Input[RecurrentScheduleArgs]): ...

class RecurrentScheduleArgsDict(TypedDict):
    days: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    hours: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    minutes: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    time_zone: pulumi.Input[_builtins.str]

@pulumi.input_type
class RecurrentScheduleArgs:
    def __init__(
        __self__,
        *,
        days: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        hours: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
        minutes: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
        time_zone: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @days.setter
    def days(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @hours.setter
    def hours(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @minutes.setter
    def minutes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[_builtins.str]: ...
    @time_zone.setter
    def time_zone(self, value: pulumi.Input[_builtins.str]): ...

class RelationshipPropertiesArgsDict(TypedDict):
    child_entity_name: pulumi.Input[_builtins.str]
    parent_entity_name: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RelationshipPropertiesArgs:
    def __init__(
        __self__,
        *,
        child_entity_name: pulumi.Input[_builtins.str],
        parent_entity_name: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="childEntityName")
    def child_entity_name(self) -> pulumi.Input[_builtins.str]: ...
    @child_entity_name.setter
    def child_entity_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="parentEntityName")
    def parent_entity_name(self) -> pulumi.Input[_builtins.str]: ...
    @parent_entity_name.setter
    def parent_entity_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ResourceGraphQueryDiscoveryRulePropertiesArgsDict(TypedDict):
    add_recommended_signals: pulumi.Input[
        Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
    ]
    authentication_setting: pulumi.Input[_builtins.str]
    discover_relationships: pulumi.Input[
        Union[_builtins.str, DiscoveryRuleRelationshipDiscoveryBehavior]
    ]
    discovery_rule_kind: pulumi.Input[_builtins.str]
    resource_graph_query: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceGraphQueryDiscoveryRulePropertiesArgs:
    def __init__(
        __self__,
        *,
        add_recommended_signals: pulumi.Input[
            Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
        ],
        authentication_setting: pulumi.Input[_builtins.str],
        discover_relationships: pulumi.Input[
            Union[_builtins.str, DiscoveryRuleRelationshipDiscoveryBehavior]
        ],
        discovery_rule_kind: pulumi.Input[_builtins.str],
        resource_graph_query: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addRecommendedSignals")
    def add_recommended_signals(
        self,
    ) -> pulumi.Input[
        Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
    ]: ...
    @add_recommended_signals.setter
    def add_recommended_signals(
        self,
        value: pulumi.Input[
            Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="authenticationSetting")
    def authentication_setting(self) -> pulumi.Input[_builtins.str]: ...
    @authentication_setting.setter
    def authentication_setting(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="discoverRelationships")
    def discover_relationships(
        self,
    ) -> pulumi.Input[
        Union[_builtins.str, DiscoveryRuleRelationshipDiscoveryBehavior]
    ]: ...
    @discover_relationships.setter
    def discover_relationships(
        self,
        value: pulumi.Input[
            Union[_builtins.str, DiscoveryRuleRelationshipDiscoveryBehavior]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveryRuleKind")
    def discovery_rule_kind(self) -> pulumi.Input[_builtins.str]: ...
    @discovery_rule_kind.setter
    def discovery_rule_kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGraphQuery")
    def resource_graph_query(self) -> pulumi.Input[_builtins.str]: ...
    @resource_graph_query.setter
    def resource_graph_query(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceMapArgsDict(TypedDict):
    from_: pulumi.Input[_builtins.str]
    to: pulumi.Input[_builtins.str]

@pulumi.input_type
class ResourceMapArgs:
    def __init__(
        __self__, *, from_: pulumi.Input[_builtins.str], to: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> pulumi.Input[_builtins.str]: ...
    @from_.setter
    def from_(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> pulumi.Input[_builtins.str]: ...
    @to.setter
    def to(self, value: pulumi.Input[_builtins.str]): ...

class ResourceMetricSignalDefinitionPropertiesArgsDict(TypedDict):
    aggregation_type: pulumi.Input[Union[_builtins.str, MetricAggregationType]]
    evaluation_rules: pulumi.Input[EvaluationRuleArgsDict]
    metric_name: pulumi.Input[_builtins.str]
    metric_namespace: pulumi.Input[_builtins.str]
    signal_kind: pulumi.Input[_builtins.str]
    time_grain: pulumi.Input[_builtins.str]
    data_unit: NotRequired[pulumi.Input[_builtins.str]]
    dimension: NotRequired[pulumi.Input[_builtins.str]]
    dimension_filter: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    refresh_interval: NotRequired[pulumi.Input[Union[_builtins.str, RefreshInterval]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ResourceMetricSignalDefinitionPropertiesArgs:
    def __init__(
        __self__,
        *,
        aggregation_type: pulumi.Input[Union[_builtins.str, MetricAggregationType]],
        evaluation_rules: pulumi.Input[EvaluationRuleArgs],
        metric_name: pulumi.Input[_builtins.str],
        metric_namespace: pulumi.Input[_builtins.str],
        signal_kind: pulumi.Input[_builtins.str],
        time_grain: pulumi.Input[_builtins.str],
        data_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        dimension: Optional[pulumi.Input[_builtins.str]] = ...,
        dimension_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        refresh_interval: Optional[
            pulumi.Input[Union[_builtins.str, RefreshInterval]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggregationType")
    def aggregation_type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, MetricAggregationType]]: ...
    @aggregation_type.setter
    def aggregation_type(
        self, value: pulumi.Input[Union[_builtins.str, MetricAggregationType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="evaluationRules")
    def evaluation_rules(self) -> pulumi.Input[EvaluationRuleArgs]: ...
    @evaluation_rules.setter
    def evaluation_rules(self, value: pulumi.Input[EvaluationRuleArgs]): ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> pulumi.Input[_builtins.str]: ...
    @metric_namespace.setter
    def metric_namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="signalKind")
    def signal_kind(self) -> pulumi.Input[_builtins.str]: ...
    @signal_kind.setter
    def signal_kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> pulumi.Input[_builtins.str]: ...
    @time_grain.setter
    def time_grain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataUnit")
    def data_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_unit.setter
    def data_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dimensionFilter")
    def dimension_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dimension_filter.setter
    def dimension_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RefreshInterval]]]: ...
    @refresh_interval.setter
    def refresh_interval(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RefreshInterval]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class RetentionPolicyArgsDict(TypedDict):
    days: pulumi.Input[_builtins.int]
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class RetentionPolicyArgs:
    def __init__(
        __self__,
        *,
        days: pulumi.Input[_builtins.int],
        enabled: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> pulumi.Input[_builtins.int]: ...
    @days.setter
    def days(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class RuleResolveConfigurationArgsDict(TypedDict):
    auto_resolved: NotRequired[pulumi.Input[_builtins.bool]]
    time_to_resolve: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RuleResolveConfigurationArgs:
    def __init__(
        __self__,
        *,
        auto_resolved: Optional[pulumi.Input[_builtins.bool]] = ...,
        time_to_resolve: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoResolved")
    def auto_resolved(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_resolved.setter
    def auto_resolved(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="timeToResolve")
    def time_to_resolve(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_to_resolve.setter
    def time_to_resolve(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScaleActionArgsDict(TypedDict):
    cooldown: pulumi.Input[_builtins.str]
    direction: pulumi.Input[ScaleDirection]
    type: pulumi.Input[ScaleType]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScaleActionArgs:
    def __init__(
        __self__,
        *,
        cooldown: pulumi.Input[_builtins.str],
        direction: pulumi.Input[ScaleDirection],
        type: pulumi.Input[ScaleType],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cooldown(self) -> pulumi.Input[_builtins.str]: ...
    @cooldown.setter
    def cooldown(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Input[ScaleDirection]: ...
    @direction.setter
    def direction(self, value: pulumi.Input[ScaleDirection]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[ScaleType]: ...
    @type.setter
    def type(self, value: pulumi.Input[ScaleType]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScaleCapacityArgsDict(TypedDict):
    default: pulumi.Input[_builtins.str]
    maximum: pulumi.Input[_builtins.str]
    minimum: pulumi.Input[_builtins.str]

@pulumi.input_type
class ScaleCapacityArgs:
    def __init__(
        __self__,
        *,
        default: pulumi.Input[_builtins.str],
        maximum: pulumi.Input[_builtins.str],
        minimum: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> pulumi.Input[_builtins.str]: ...
    @default.setter
    def default(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> pulumi.Input[_builtins.str]: ...
    @maximum.setter
    def maximum(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> pulumi.Input[_builtins.str]: ...
    @minimum.setter
    def minimum(self, value: pulumi.Input[_builtins.str]): ...

class ScaleRuleMetricDimensionArgsDict(TypedDict):
    dimension_name: pulumi.Input[_builtins.str]
    operator: pulumi.Input[Union[_builtins.str, ScaleRuleMetricDimensionOperationType]]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ScaleRuleMetricDimensionArgs:
    def __init__(
        __self__,
        *,
        dimension_name: pulumi.Input[_builtins.str],
        operator: pulumi.Input[
            Union[_builtins.str, ScaleRuleMetricDimensionOperationType]
        ],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dimensionName")
    def dimension_name(self) -> pulumi.Input[_builtins.str]: ...
    @dimension_name.setter
    def dimension_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ScaleRuleMetricDimensionOperationType]]: ...
    @operator.setter
    def operator(
        self,
        value: pulumi.Input[
            Union[_builtins.str, ScaleRuleMetricDimensionOperationType]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ScaleRuleArgsDict(TypedDict):
    metric_trigger: pulumi.Input[MetricTriggerArgsDict]
    scale_action: pulumi.Input[ScaleActionArgsDict]

@pulumi.input_type
class ScaleRuleArgs:
    def __init__(
        __self__,
        *,
        metric_trigger: pulumi.Input[MetricTriggerArgs],
        scale_action: pulumi.Input[ScaleActionArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricTrigger")
    def metric_trigger(self) -> pulumi.Input[MetricTriggerArgs]: ...
    @metric_trigger.setter
    def metric_trigger(self, value: pulumi.Input[MetricTriggerArgs]): ...
    @_builtins.property
    @pulumi.getter(name="scaleAction")
    def scale_action(self) -> pulumi.Input[ScaleActionArgs]: ...
    @scale_action.setter
    def scale_action(self, value: pulumi.Input[ScaleActionArgs]): ...

class ScheduledQueryRuleCriteriaArgsDict(TypedDict):
    all_of: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConditionArgsDict]]]]

@pulumi.input_type
class ScheduledQueryRuleCriteriaArgs:
    def __init__(
        __self__,
        *,
        all_of: Optional[pulumi.Input[Sequence[pulumi.Input[ConditionArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allOf")
    def all_of(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConditionArgs]]]]: ...
    @all_of.setter
    def all_of(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConditionArgs]]]]
    ): ...

class SchemaMapArgsDict(TypedDict):
    record_map: pulumi.Input[Sequence[pulumi.Input[RecordMapArgsDict]]]
    resource_map: NotRequired[pulumi.Input[Sequence[pulumi.Input[ResourceMapArgsDict]]]]
    scope_map: NotRequired[pulumi.Input[Sequence[pulumi.Input[ScopeMapArgsDict]]]]

@pulumi.input_type
class SchemaMapArgs:
    def __init__(
        __self__,
        *,
        record_map: pulumi.Input[Sequence[pulumi.Input[RecordMapArgs]]],
        resource_map: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceMapArgs]]]
        ] = ...,
        scope_map: Optional[pulumi.Input[Sequence[pulumi.Input[ScopeMapArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordMap")
    def record_map(self) -> pulumi.Input[Sequence[pulumi.Input[RecordMapArgs]]]: ...
    @record_map.setter
    def record_map(
        self, value: pulumi.Input[Sequence[pulumi.Input[RecordMapArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceMap")
    def resource_map(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceMapArgs]]]]: ...
    @resource_map.setter
    def resource_map(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceMapArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scopeMap")
    def scope_map(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScopeMapArgs]]]]: ...
    @scope_map.setter
    def scope_map(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScopeMapArgs]]]]
    ): ...

class ScopeMapArgsDict(TypedDict):
    from_: pulumi.Input[_builtins.str]
    to: pulumi.Input[_builtins.str]

@pulumi.input_type
class ScopeMapArgs:
    def __init__(
        __self__, *, from_: pulumi.Input[_builtins.str], to: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> pulumi.Input[_builtins.str]: ...
    @from_.setter
    def from_(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> pulumi.Input[_builtins.str]: ...
    @to.setter
    def to(self, value: pulumi.Input[_builtins.str]): ...

class ServiceArgsDict(TypedDict):
    pipelines: pulumi.Input[Sequence[pulumi.Input[PipelineArgsDict]]]
    persistence: NotRequired[pulumi.Input[PersistenceConfigurationsArgsDict]]

@pulumi.input_type
class ServiceArgs:
    def __init__(
        __self__,
        *,
        pipelines: pulumi.Input[Sequence[pulumi.Input[PipelineArgs]]],
        persistence: Optional[pulumi.Input[PersistenceConfigurationsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pipelines(self) -> pulumi.Input[Sequence[pulumi.Input[PipelineArgs]]]: ...
    @pipelines.setter
    def pipelines(self, value: pulumi.Input[Sequence[pulumi.Input[PipelineArgs]]]): ...
    @_builtins.property
    @pulumi.getter
    def persistence(self) -> Optional[pulumi.Input[PersistenceConfigurationsArgs]]: ...
    @persistence.setter
    def persistence(
        self, value: Optional[pulumi.Input[PersistenceConfigurationsArgs]]
    ): ...

class SignalAssignmentArgsDict(TypedDict):
    signal_definitions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class SignalAssignmentArgs:
    def __init__(
        __self__,
        *,
        signal_definitions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="signalDefinitions")
    def signal_definitions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @signal_definitions.setter
    def signal_definitions(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class SignalGroupArgsDict(TypedDict):
    azure_log_analytics: NotRequired[pulumi.Input[LogAnalyticsSignalGroupArgsDict]]
    azure_monitor_workspace: NotRequired[
        pulumi.Input[AzureMonitorWorkspaceSignalGroupArgsDict]
    ]
    azure_resource: NotRequired[pulumi.Input[AzureResourceSignalGroupArgsDict]]
    dependencies: NotRequired[pulumi.Input[DependenciesSignalGroupArgsDict]]

@pulumi.input_type
class SignalGroupArgs:
    def __init__(
        __self__,
        *,
        azure_log_analytics: Optional[pulumi.Input[LogAnalyticsSignalGroupArgs]] = ...,
        azure_monitor_workspace: Optional[
            pulumi.Input[AzureMonitorWorkspaceSignalGroupArgs]
        ] = ...,
        azure_resource: Optional[pulumi.Input[AzureResourceSignalGroupArgs]] = ...,
        dependencies: Optional[pulumi.Input[DependenciesSignalGroupArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureLogAnalytics")
    def azure_log_analytics(
        self,
    ) -> Optional[pulumi.Input[LogAnalyticsSignalGroupArgs]]: ...
    @azure_log_analytics.setter
    def azure_log_analytics(
        self, value: Optional[pulumi.Input[LogAnalyticsSignalGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureMonitorWorkspace")
    def azure_monitor_workspace(
        self,
    ) -> Optional[pulumi.Input[AzureMonitorWorkspaceSignalGroupArgs]]: ...
    @azure_monitor_workspace.setter
    def azure_monitor_workspace(
        self, value: Optional[pulumi.Input[AzureMonitorWorkspaceSignalGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="azureResource")
    def azure_resource(
        self,
    ) -> Optional[pulumi.Input[AzureResourceSignalGroupArgs]]: ...
    @azure_resource.setter
    def azure_resource(
        self, value: Optional[pulumi.Input[AzureResourceSignalGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> Optional[pulumi.Input[DependenciesSignalGroupArgs]]: ...
    @dependencies.setter
    def dependencies(
        self, value: Optional[pulumi.Input[DependenciesSignalGroupArgs]]
    ): ...

class SmsReceiverArgsDict(TypedDict):
    country_code: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    phone_number: pulumi.Input[_builtins.str]

@pulumi.input_type
class SmsReceiverArgs:
    def __init__(
        __self__,
        *,
        country_code: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        phone_number: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> pulumi.Input[_builtins.str]: ...
    @country_code.setter
    def country_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]: ...
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): ...

class StorageBlobDestinationArgsDict(TypedDict):
    container_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageBlobDestinationArgs:
    def __init__(
        __self__,
        *,
        container_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_resource_id.setter
    def storage_account_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class StorageTableDestinationArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    table_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageTableDestinationArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        table_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_resource_id.setter
    def storage_account_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StreamDeclarationArgsDict(TypedDict):
    columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[ColumnDefinitionArgsDict]]]]

@pulumi.input_type
class StreamDeclarationArgs:
    def __init__(
        __self__,
        *,
        columns: Optional[
            pulumi.Input[Sequence[pulumi.Input[ColumnDefinitionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ColumnDefinitionArgs]]]]: ...
    @columns.setter
    def columns(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ColumnDefinitionArgs]]]],
    ): ...

class SubscriptionLogSettingsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    category: NotRequired[pulumi.Input[_builtins.str]]
    category_group: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SubscriptionLogSettingsArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        category_group: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="categoryGroup")
    def category_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category_group.setter
    def category_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SyslogDataSourceArgsDict(TypedDict):
    facility_names: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[Union[_builtins.str, KnownSyslogDataSourceFacilityNames]]
            ]
        ]
    ]
    log_levels: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, KnownSyslogDataSourceLogLevels]]]
        ]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    streams: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, KnownSyslogDataSourceStreams]]]
        ]
    ]

@pulumi.input_type
class SyslogDataSourceArgs:
    def __init__(
        __self__,
        *,
        facility_names: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[_builtins.str, KnownSyslogDataSourceFacilityNames]
                    ]
                ]
            ]
        ] = ...,
        log_levels: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[_builtins.str, KnownSyslogDataSourceLogLevels]]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        streams: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[_builtins.str, KnownSyslogDataSourceStreams]]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="facilityNames")
    def facility_names(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[Union[_builtins.str, KnownSyslogDataSourceFacilityNames]]
            ]
        ]
    ]: ...
    @facility_names.setter
    def facility_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[_builtins.str, KnownSyslogDataSourceFacilityNames]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logLevels")
    def log_levels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, KnownSyslogDataSourceLogLevels]]]
        ]
    ]: ...
    @log_levels.setter
    def log_levels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[_builtins.str, KnownSyslogDataSourceLogLevels]]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def streams(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[Union[_builtins.str, KnownSyslogDataSourceStreams]]]
        ]
    ]: ...
    @streams.setter
    def streams(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[_builtins.str, KnownSyslogDataSourceStreams]]
                ]
            ]
        ],
    ): ...

class SyslogReceiverArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]
    protocol: NotRequired[pulumi.Input[Union[_builtins.str, SyslogProtocol]]]

@pulumi.input_type
class SyslogReceiverArgs:
    def __init__(
        __self__,
        *,
        endpoint: pulumi.Input[_builtins.str],
        protocol: Optional[pulumi.Input[Union[_builtins.str, SyslogProtocol]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SyslogProtocol]]]: ...
    @protocol.setter
    def protocol(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SyslogProtocol]]]
    ): ...

class TcpExporterArgsDict(TypedDict):
    url: pulumi.Input[_builtins.str]

@pulumi.input_type
class TcpExporterArgs:
    def __init__(__self__, *, url: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...

class ThresholdRuleArgsDict(TypedDict):
    operator: pulumi.Input[Union[_builtins.str, SignalOperator]]
    threshold: pulumi.Input[_builtins.str]

@pulumi.input_type
class ThresholdRuleArgs:
    def __init__(
        __self__,
        *,
        operator: pulumi.Input[Union[_builtins.str, SignalOperator]],
        threshold: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, SignalOperator]]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, SignalOperator]]): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[_builtins.str]: ...
    @threshold.setter
    def threshold(self, value: pulumi.Input[_builtins.str]): ...

class TimeWindowArgsDict(TypedDict):
    end: pulumi.Input[_builtins.str]
    start: pulumi.Input[_builtins.str]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TimeWindowArgs:
    def __init__(
        __self__,
        *,
        end: pulumi.Input[_builtins.str],
        start: pulumi.Input[_builtins.str],
        time_zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> pulumi.Input[_builtins.str]: ...
    @end.setter
    def end(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> pulumi.Input[_builtins.str]: ...
    @start.setter
    def start(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UdpReceiverArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]
    encoding: NotRequired[pulumi.Input[Union[_builtins.str, StreamEncodingType]]]
    json_array_mapper: NotRequired[pulumi.Input[JsonArrayMapperArgsDict]]
    read_queue_length: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class UdpReceiverArgs:
    def __init__(
        __self__,
        *,
        endpoint: pulumi.Input[_builtins.str],
        encoding: Optional[
            pulumi.Input[Union[_builtins.str, StreamEncodingType]]
        ] = ...,
        json_array_mapper: Optional[pulumi.Input[JsonArrayMapperArgs]] = ...,
        read_queue_length: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def encoding(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StreamEncodingType]]]: ...
    @encoding.setter
    def encoding(
        self, value: Optional[pulumi.Input[Union[_builtins.str, StreamEncodingType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jsonArrayMapper")
    def json_array_mapper(self) -> Optional[pulumi.Input[JsonArrayMapperArgs]]: ...
    @json_array_mapper.setter
    def json_array_mapper(self, value: Optional[pulumi.Input[JsonArrayMapperArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="readQueueLength")
    def read_queue_length(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @read_queue_length.setter
    def read_queue_length(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class VoiceReceiverArgsDict(TypedDict):
    country_code: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    phone_number: pulumi.Input[_builtins.str]

@pulumi.input_type
class VoiceReceiverArgs:
    def __init__(
        __self__,
        *,
        country_code: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        phone_number: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> pulumi.Input[_builtins.str]: ...
    @country_code.setter
    def country_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]: ...
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): ...

class WebhookNotificationArgsDict(TypedDict):
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    service_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WebhookNotificationArgs:
    def __init__(
        __self__,
        *,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        service_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_uri.setter
    def service_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WebhookReceiverArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    service_uri: pulumi.Input[_builtins.str]
    identifier_uri: NotRequired[pulumi.Input[_builtins.str]]
    managed_identity: NotRequired[pulumi.Input[_builtins.str]]
    object_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    use_aad_auth: NotRequired[pulumi.Input[_builtins.bool]]
    use_common_alert_schema: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class WebhookReceiverArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        service_uri: pulumi.Input[_builtins.str],
        identifier_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        object_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        use_aad_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_common_alert_schema: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> pulumi.Input[_builtins.str]: ...
    @service_uri.setter
    def service_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="identifierUri")
    def identifier_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identifier_uri.setter
    def identifier_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_identity.setter
    def managed_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useAadAuth")
    def use_aad_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_aad_auth.setter
    def use_aad_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useCommonAlertSchema")
    def use_common_alert_schema(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_common_alert_schema.setter
    def use_common_alert_schema(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class WebtestLocationAvailabilityCriteriaArgsDict(TypedDict):
    component_id: pulumi.Input[_builtins.str]
    failed_location_count: pulumi.Input[_builtins.float]
    odata_type: pulumi.Input[_builtins.str]
    web_test_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class WebtestLocationAvailabilityCriteriaArgs:
    def __init__(
        __self__,
        *,
        component_id: pulumi.Input[_builtins.str],
        failed_location_count: pulumi.Input[_builtins.float],
        odata_type: pulumi.Input[_builtins.str],
        web_test_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> pulumi.Input[_builtins.str]: ...
    @component_id.setter
    def component_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failedLocationCount")
    def failed_location_count(self) -> pulumi.Input[_builtins.float]: ...
    @failed_location_count.setter
    def failed_location_count(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[_builtins.str]: ...
    @odata_type.setter
    def odata_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="webTestId")
    def web_test_id(self) -> pulumi.Input[_builtins.str]: ...
    @web_test_id.setter
    def web_test_id(self, value: pulumi.Input[_builtins.str]): ...

class WindowsEventLogDataSourceArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    streams: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[_builtins.str, KnownWindowsEventLogDataSourceStreams]
                ]
            ]
        ]
    ]
    x_path_queries: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WindowsEventLogDataSourceArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        streams: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[_builtins.str, KnownWindowsEventLogDataSourceStreams]
                    ]
                ]
            ]
        ] = ...,
        x_path_queries: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def streams(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[_builtins.str, KnownWindowsEventLogDataSourceStreams]
                ]
            ]
        ]
    ]: ...
    @streams.setter
    def streams(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[_builtins.str, KnownWindowsEventLogDataSourceStreams]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="xPathQueries")
    def x_path_queries(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @x_path_queries.setter
    def x_path_queries(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class WindowsFirewallLogsDataSourceArgsDict(TypedDict):
    streams: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WindowsFirewallLogsDataSourceArgs:
    def __init__(
        __self__,
        *,
        streams: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def streams(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @streams.setter
    def streams(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
