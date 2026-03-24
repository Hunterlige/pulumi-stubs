import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ReplicationSetRegion",
    "ResponsePlanAction",
    "ResponsePlanActionSsmAutomation",
    "ResponsePlanActionSsmAutomationParameter",
    "ResponsePlanIncidentTemplate",
    "ResponsePlanIncidentTemplateNotificationTarget",
    "ResponsePlanIntegration",
    "ResponsePlanIntegrationPagerduty",
    "GetReplicationSetRegionResult",
    "GetResponsePlanActionResult",
    "GetResponsePlanActionSsmAutomationResult",
    "GetResponsePlanActionSsmAutomationParameterResult",
    "GetResponsePlanIncidentTemplateResult",
    ...,
    "GetResponsePlanIntegrationResult",
    "GetResponsePlanIntegrationPagerdutyResult",
]

@pulumi.output_type
class ReplicationSetRegion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        kms_key_arn: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        status_message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResponsePlanAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ssm_automations: Optional[
            Sequence[outputs.ResponsePlanActionSsmAutomation]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ssmAutomations")
    def ssm_automations(
        self,
    ) -> Optional[Sequence[outputs.ResponsePlanActionSsmAutomation]]: ...

@pulumi.output_type
class ResponsePlanActionSsmAutomation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        document_name: _builtins.str,
        role_arn: _builtins.str,
        document_version: Optional[_builtins.str] = ...,
        dynamic_parameters: Optional[Mapping[str, _builtins.str]] = ...,
        parameters: Optional[
            Sequence[outputs.ResponsePlanActionSsmAutomationParameter]
        ] = ...,
        target_account: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="documentName")
    def document_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dynamicParameters")
    def dynamic_parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[Sequence[outputs.ResponsePlanActionSsmAutomationParameter]]: ...
    @_builtins.property
    @pulumi.getter(name="targetAccount")
    def target_account(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResponsePlanActionSsmAutomationParameter(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ResponsePlanIncidentTemplate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        impact: _builtins.int,
        title: _builtins.str,
        dedupe_string: Optional[_builtins.str] = ...,
        incident_tags: Optional[Mapping[str, _builtins.str]] = ...,
        notification_targets: Optional[
            Sequence[outputs.ResponsePlanIncidentTemplateNotificationTarget]
        ] = ...,
        summary: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def impact(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dedupeString")
    def dedupe_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="incidentTags")
    def incident_tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="notificationTargets")
    def notification_targets(
        self,
    ) -> Optional[Sequence[outputs.ResponsePlanIncidentTemplateNotificationTarget]]: ...
    @_builtins.property
    @pulumi.getter
    def summary(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResponsePlanIncidentTemplateNotificationTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, sns_topic_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ResponsePlanIntegration(dict):
    def __init__(
        __self__,
        *,
        pagerduties: Optional[Sequence[outputs.ResponsePlanIntegrationPagerduty]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pagerduties(
        self,
    ) -> Optional[Sequence[outputs.ResponsePlanIntegrationPagerduty]]: ...

@pulumi.output_type
class ResponsePlanIntegrationPagerduty(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        secret_id: _builtins.str,
        service_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetReplicationSetRegionResult(dict):
    def __init__(
        __self__,
        *,
        kms_key_arn: _builtins.str,
        name: _builtins.str,
        status: _builtins.str,
        status_message: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str: ...

@pulumi.output_type
class GetResponsePlanActionResult(dict):
    def __init__(
        __self__,
        *,
        ssm_automations: Sequence[outputs.GetResponsePlanActionSsmAutomationResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ssmAutomations")
    def ssm_automations(
        self,
    ) -> Sequence[outputs.GetResponsePlanActionSsmAutomationResult]: ...

@pulumi.output_type
class GetResponsePlanActionSsmAutomationResult(dict):
    def __init__(
        __self__,
        *,
        document_name: _builtins.str,
        document_version: _builtins.str,
        dynamic_parameters: Mapping[str, _builtins.str],
        parameters: Sequence[outputs.GetResponsePlanActionSsmAutomationParameterResult],
        role_arn: _builtins.str,
        target_account: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="documentName")
    def document_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dynamicParameters")
    def dynamic_parameters(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Sequence[outputs.GetResponsePlanActionSsmAutomationParameterResult]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetAccount")
    def target_account(self) -> _builtins.str: ...

@pulumi.output_type
class GetResponsePlanActionSsmAutomationParameterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetResponsePlanIncidentTemplateResult(dict):
    def __init__(
        __self__,
        *,
        dedupe_string: _builtins.str,
        impact: _builtins.int,
        incident_tags: Mapping[str, _builtins.str],
        notification_targets: Sequence[
            outputs.GetResponsePlanIncidentTemplateNotificationTargetResult
        ],
        summary: _builtins.str,
        title: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dedupeString")
    def dedupe_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def impact(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="incidentTags")
    def incident_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationTargets")
    def notification_targets(
        self,
    ) -> Sequence[outputs.GetResponsePlanIncidentTemplateNotificationTargetResult]: ...
    @_builtins.property
    @pulumi.getter
    def summary(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...

@pulumi.output_type
class GetResponsePlanIncidentTemplateNotificationTargetResult(dict):
    def __init__(__self__, *, sns_topic_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetResponsePlanIntegrationResult(dict):
    def __init__(
        __self__,
        *,
        pagerduties: Sequence[outputs.GetResponsePlanIntegrationPagerdutyResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pagerduties(
        self,
    ) -> Sequence[outputs.GetResponsePlanIntegrationPagerdutyResult]: ...

@pulumi.output_type
class GetResponsePlanIntegrationPagerdutyResult(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        secret_id: _builtins.str,
        service_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> _builtins.str: ...
