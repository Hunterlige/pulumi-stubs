import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AlertConfigurationArgs",
    "AlertConfigurationArgsDict",
    "AzureMonitorWorkspaceSignalGroupArgs",
    "AzureMonitorWorkspaceSignalGroupArgsDict",
    "AzureResourceSignalGroupArgs",
    "AzureResourceSignalGroupArgsDict",
    "DependenciesSignalGroupArgs",
    "DependenciesSignalGroupArgsDict",
    "DiscoveryRulePropertiesArgs",
    "DiscoveryRulePropertiesArgsDict",
    "DynamicDetectionRuleArgs",
    "DynamicDetectionRuleArgsDict",
    "EntityAlertsArgs",
    "EntityAlertsArgsDict",
    "EntityCoordinatesArgs",
    "EntityCoordinatesArgsDict",
    "EntityPropertiesArgs",
    "EntityPropertiesArgsDict",
    "EvaluationRuleArgs",
    "EvaluationRuleArgsDict",
    "HealthModelPropertiesArgs",
    "HealthModelPropertiesArgsDict",
    "IconDefinitionArgs",
    "IconDefinitionArgsDict",
    "LogAnalyticsQuerySignalDefinitionPropertiesArgs",
    ...,
    "LogAnalyticsSignalGroupArgs",
    "LogAnalyticsSignalGroupArgsDict",
    "ManagedIdentityAuthenticationSettingPropertiesArgs",
    ...,
    "ManagedServiceIdentityArgs",
    "ManagedServiceIdentityArgsDict",
    "ModelDiscoverySettingsArgs",
    "ModelDiscoverySettingsArgsDict",
    "PrometheusMetricsSignalDefinitionPropertiesArgs",
    ...,
    "RelationshipPropertiesArgs",
    "RelationshipPropertiesArgsDict",
    "ResourceMetricSignalDefinitionPropertiesArgs",
    "ResourceMetricSignalDefinitionPropertiesArgsDict",
    "SignalAssignmentArgs",
    "SignalAssignmentArgsDict",
    "SignalGroupArgs",
    "SignalGroupArgsDict",
    "ThresholdRuleArgs",
    "ThresholdRuleArgsDict",
]

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

class DiscoveryRulePropertiesArgsDict(TypedDict):
    add_recommended_signals: pulumi.Input[
        Union[_builtins.str, DiscoveryRuleRecommendedSignalsBehavior]
    ]
    authentication_setting: pulumi.Input[_builtins.str]
    discover_relationships: pulumi.Input[
        Union[_builtins.str, DiscoveryRuleRelationshipDiscoveryBehavior]
    ]
    resource_graph_query: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DiscoveryRulePropertiesArgs:
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
    @pulumi.getter(name="resourceGraphQuery")
    def resource_graph_query(self) -> pulumi.Input[_builtins.str]: ...
    @resource_graph_query.setter
    def resource_graph_query(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

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
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    signals: NotRequired[pulumi.Input[SignalGroupArgsDict]]

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
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        signals: Optional[pulumi.Input[SignalGroupArgs]] = ...,
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
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def signals(self) -> Optional[pulumi.Input[SignalGroupArgs]]: ...
    @signals.setter
    def signals(self, value: Optional[pulumi.Input[SignalGroupArgs]]): ...

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

class LogAnalyticsQuerySignalDefinitionPropertiesArgsDict(TypedDict):
    evaluation_rules: pulumi.Input[EvaluationRuleArgsDict]
    query_text: pulumi.Input[_builtins.str]
    signal_kind: pulumi.Input[_builtins.str]
    data_unit: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    refresh_interval: NotRequired[pulumi.Input[Union[_builtins.str, RefreshInterval]]]
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
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        refresh_interval: Optional[
            pulumi.Input[Union[_builtins.str, RefreshInterval]]
        ] = ...,
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
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
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

class PrometheusMetricsSignalDefinitionPropertiesArgsDict(TypedDict):
    evaluation_rules: pulumi.Input[EvaluationRuleArgsDict]
    query_text: pulumi.Input[_builtins.str]
    signal_kind: pulumi.Input[_builtins.str]
    data_unit: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    refresh_interval: NotRequired[pulumi.Input[Union[_builtins.str, RefreshInterval]]]
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
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        refresh_interval: Optional[
            pulumi.Input[Union[_builtins.str, RefreshInterval]]
        ] = ...,
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
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_grain.setter
    def time_grain(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RelationshipPropertiesArgsDict(TypedDict):
    child_entity_name: pulumi.Input[_builtins.str]
    parent_entity_name: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RelationshipPropertiesArgs:
    def __init__(
        __self__,
        *,
        child_entity_name: pulumi.Input[_builtins.str],
        parent_entity_name: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
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
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

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
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    refresh_interval: NotRequired[pulumi.Input[Union[_builtins.str, RefreshInterval]]]

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
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        refresh_interval: Optional[
            pulumi.Input[Union[_builtins.str, RefreshInterval]]
        ] = ...,
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
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RefreshInterval]]]: ...
    @refresh_interval.setter
    def refresh_interval(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RefreshInterval]]]
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
