import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ActionGroupResponse",
    "ActionGroupsInformationResponse",
    "AddActionGroupsResponse",
    "AlertProcessingRulePropertiesResponse",
    "ConditionResponse",
    "ConditionResponseV1",
    "ConditionsResponse",
    "DailyRecurrenceResponse",
    "DetectorParameterDefinitionResponse",
    "DetectorResponse",
    "DiagnosticsResponse",
    "InvestigationExecutionResponse",
    "InvestigationMetadataResponse",
    "InvestigationScopeResponse",
    "IssuePropertiesResponse",
    "MonthlyRecurrenceResponse",
    "OriginResponse",
    "PrometheusRuleGroupActionResponse",
    "PrometheusRuleResolveConfigurationResponse",
    "PrometheusRuleResponse",
    "RelatedAlertResponse",
    "RelatedResourceResponse",
    "RemoveAllActionGroupsResponse",
    "RunParametersResponse",
    "ScheduleResponse",
    "ScopeResponse",
    "SuppressionConfigResponse",
    "SuppressionResponse",
    "SuppressionScheduleResponse",
    "SystemDataResponse",
    "ThrottlingInformationResponse",
    "WeeklyRecurrenceResponse",
]

@pulumi.output_type
class ActionGroupResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_group_id: _builtins.str,
        created_at: _builtins.str,
        created_by: _builtins.str,
        last_modified_at: _builtins.str,
        last_modified_by: _builtins.str,
        type: _builtins.str,
        conditions: Optional[outputs.ConditionsResponse] = ...,
        description: Optional[_builtins.str] = ...,
        scope: Optional[outputs.ScopeResponse] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[outputs.ConditionsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[outputs.ScopeResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ActionGroupsInformationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_ids: Sequence[_builtins.str],
        custom_email_subject: Optional[_builtins.str] = ...,
        custom_webhook_payload: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customEmailSubject")
    def custom_email_subject(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customWebhookPayload")
    def custom_webhook_payload(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AddActionGroupsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_group_ids: Sequence[_builtins.str],
        action_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroupIds")
    def action_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> _builtins.str: ...

@pulumi.output_type
class AlertProcessingRulePropertiesResponse(dict):
    def __init__(
        __self__,
        *,
        actions: Sequence[Any],
        scopes: Sequence[_builtins.str],
        conditions: Optional[Sequence[outputs.ConditionResponseV1]] = ...,
        description: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
        schedule: Optional[outputs.ScheduleResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[Any]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.ConditionResponseV1]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[outputs.ScheduleResponse]: ...

@pulumi.output_type
class ConditionResponse(dict):
    def __init__(
        __self__,
        *,
        operator: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ConditionResponseV1(dict):
    def __init__(
        __self__,
        *,
        field: Optional[_builtins.str] = ...,
        operator: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ConditionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        alert_context: Optional[outputs.ConditionResponse] = ...,
        alert_rule_id: Optional[outputs.ConditionResponse] = ...,
        alert_rule_name: Optional[outputs.ConditionResponse] = ...,
        description: Optional[outputs.ConditionResponse] = ...,
        monitor_condition: Optional[outputs.ConditionResponse] = ...,
        monitor_service: Optional[outputs.ConditionResponse] = ...,
        severity: Optional[outputs.ConditionResponse] = ...,
        target_resource_type: Optional[outputs.ConditionResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alertContext")
    def alert_context(self) -> Optional[outputs.ConditionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="alertRuleId")
    def alert_rule_id(self) -> Optional[outputs.ConditionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="alertRuleName")
    def alert_rule_name(self) -> Optional[outputs.ConditionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[outputs.ConditionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="monitorCondition")
    def monitor_condition(self) -> Optional[outputs.ConditionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="monitorService")
    def monitor_service(self) -> Optional[outputs.ConditionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[outputs.ConditionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="targetResourceType")
    def target_resource_type(self) -> Optional[outputs.ConditionResponse]: ...

@pulumi.output_type
class DailyRecurrenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        recurrence_type: _builtins.str,
        end_time: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DetectorParameterDefinitionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        is_mandatory: Optional[_builtins.bool] = ...,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isMandatory")
    def is_mandatory(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DetectorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        id: _builtins.str,
        image_paths: Sequence[_builtins.str],
        name: _builtins.str,
        parameter_definitions: Sequence[outputs.DetectorParameterDefinitionResponse],
        supported_cadences: Sequence[_builtins.int],
        supported_resource_types: Sequence[_builtins.str],
        parameters: Optional[Mapping[str, Any]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imagePaths")
    def image_paths(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterDefinitions")
    def parameter_definitions(
        self,
    ) -> Sequence[outputs.DetectorParameterDefinitionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="supportedCadences")
    def supported_cadences(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="supportedResourceTypes")
    def supported_resource_types(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, Any]]: ...

@pulumi.output_type
class DiagnosticsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: _builtins.str,
        created_by: _builtins.str,
        last_modified_at: _builtins.str,
        last_modified_by: _builtins.str,
        type: _builtins.str,
        conditions: Optional[outputs.ConditionsResponse] = ...,
        description: Optional[_builtins.str] = ...,
        scope: Optional[outputs.ScopeResponse] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[outputs.ConditionsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[outputs.ScopeResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InvestigationExecutionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, completed_at: _builtins.str, run_state: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="completedAt")
    def completed_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runState")
    def run_state(self) -> _builtins.str: ...

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
class MonthlyRecurrenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        days_of_month: Sequence[_builtins.int],
        recurrence_type: _builtins.str,
        end_time: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfMonth")
    def days_of_month(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

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
class PrometheusRuleGroupActionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_group_id: Optional[_builtins.str] = ...,
        action_properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="actionProperties")
    def action_properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class PrometheusRuleResolveConfigurationResponse(dict):
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
class PrometheusRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        actions: Optional[Sequence[outputs.PrometheusRuleGroupActionResponse]] = ...,
        alert: Optional[_builtins.str] = ...,
        annotations: Optional[Mapping[str, _builtins.str]] = ...,
        enabled: Optional[_builtins.bool] = ...,
        for_: Optional[_builtins.str] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        record: Optional[_builtins.str] = ...,
        resolve_configuration: Optional[
            outputs.PrometheusRuleResolveConfigurationResponse
        ] = ...,
        severity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[Sequence[outputs.PrometheusRuleGroupActionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def alert(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="for")
    def for_(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def record(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resolveConfiguration")
    def resolve_configuration(
        self,
    ) -> Optional[outputs.PrometheusRuleResolveConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.int]: ...

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
class RemoveAllActionGroupsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, action_type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> _builtins.str: ...

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
class ScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        effective_from: Optional[_builtins.str] = ...,
        effective_until: Optional[_builtins.str] = ...,
        recurrences: Optional[Sequence[Any]] = ...,
        time_zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="effectiveFrom")
    def effective_from(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveUntil")
    def effective_until(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def recurrences(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScopeResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        scope_type: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scopeType")
    def scope_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SuppressionConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        recurrence_type: _builtins.str,
        schedule: Optional[outputs.SuppressionScheduleResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[outputs.SuppressionScheduleResponse]: ...

@pulumi.output_type
class SuppressionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: _builtins.str,
        created_by: _builtins.str,
        last_modified_at: _builtins.str,
        last_modified_by: _builtins.str,
        suppression_config: outputs.SuppressionConfigResponse,
        type: _builtins.str,
        conditions: Optional[outputs.ConditionsResponse] = ...,
        description: Optional[_builtins.str] = ...,
        scope: Optional[outputs.ScopeResponse] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="suppressionConfig")
    def suppression_config(self) -> outputs.SuppressionConfigResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[outputs.ConditionsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[outputs.ScopeResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SuppressionScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_date: Optional[_builtins.str] = ...,
        end_time: Optional[_builtins.str] = ...,
        recurrence_values: Optional[Sequence[_builtins.int]] = ...,
        start_date: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recurrenceValues")
    def recurrence_values(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

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
class ThrottlingInformationResponse(dict):
    def __init__(__self__, *, duration: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WeeklyRecurrenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        days_of_week: Sequence[_builtins.str],
        recurrence_type: _builtins.str,
        end_time: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
