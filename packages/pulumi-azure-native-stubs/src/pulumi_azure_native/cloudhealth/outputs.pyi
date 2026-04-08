import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AlertConfigurationResponse",
    "AzureMonitorWorkspaceSignalGroupResponse",
    "AzureResourceSignalGroupResponse",
    "DependenciesSignalGroupResponse",
    "DiscoveryRulePropertiesResponse",
    "DynamicDetectionRuleResponse",
    "EntityAlertsResponse",
    "EntityCoordinatesResponse",
    "EntityPropertiesResponse",
    "EvaluationRuleResponse",
    "HealthModelPropertiesResponse",
    "HealthStateTransitionResponse",
    "IconDefinitionResponse",
    ...,
    "LogAnalyticsSignalGroupResponse",
    ...,
    "ManagedServiceIdentityResponse",
    "ModelDiscoverySettingsResponse",
    ...,
    "RelationshipPropertiesResponse",
    "ResourceMetricSignalDefinitionPropertiesResponse",
    "SignalAssignmentResponse",
    "SignalGroupResponse",
    "SignalHistoryDataPointResponse",
    "SystemDataResponse",
    "ThresholdRuleResponse",
    "UserAssignedIdentityResponse",
]

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
class DiscoveryRulePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        add_recommended_signals: _builtins.str,
        authentication_setting: _builtins.str,
        deletion_date: _builtins.str,
        discover_relationships: _builtins.str,
        entity_name: _builtins.str,
        error_message: _builtins.str,
        number_of_discovered_entities: _builtins.int,
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
    @pulumi.getter(name="entityName")
    def entity_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="numberOfDiscoveredEntities")
    def number_of_discovered_entities(self) -> _builtins.int: ...
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
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        signals: Optional[outputs.SignalGroupResponse] = ...,
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
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def signals(self) -> Optional[outputs.SignalGroupResponse]: ...

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
class HealthModelPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataplane_endpoint: _builtins.str,
        provisioning_state: _builtins.str,
        discovery: Optional[outputs.ModelDiscoverySettingsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataplaneEndpoint")
    def dataplane_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def discovery(self) -> Optional[outputs.ModelDiscoverySettingsResponse]: ...

@pulumi.output_type
class HealthStateTransitionResponse(dict):
    def __init__(
        __self__,
        *,
        new_state: _builtins.str,
        occurred_at: _builtins.str,
        previous_state: _builtins.str,
        reason: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="newState")
    def new_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="occurredAt")
    def occurred_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="previousState")
    def previous_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]: ...

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
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        refresh_interval: Optional[_builtins.str] = ...,
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
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(self) -> Optional[_builtins.str]: ...
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
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        refresh_interval: Optional[_builtins.str] = ...,
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
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> Optional[_builtins.str]: ...

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
        labels: Optional[Mapping[str, _builtins.str]] = ...,
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
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

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
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        refresh_interval: Optional[_builtins.str] = ...,
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
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(self) -> Optional[_builtins.str]: ...

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
class SignalHistoryDataPointResponse(dict):
    def __init__(
        __self__,
        *,
        health_state: _builtins.str,
        occurred_at: _builtins.str,
        additional_context: Optional[_builtins.str] = ...,
        value: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthState")
    def health_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="occurredAt")
    def occurred_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalContext")
    def additional_context(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.float]: ...

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
