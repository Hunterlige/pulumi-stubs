import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ReplicationSetRegionArgs",
    "ReplicationSetRegionArgsDict",
    "ResponsePlanActionArgs",
    "ResponsePlanActionArgsDict",
    "ResponsePlanActionSsmAutomationArgs",
    "ResponsePlanActionSsmAutomationArgsDict",
    "ResponsePlanActionSsmAutomationParameterArgs",
    "ResponsePlanActionSsmAutomationParameterArgsDict",
    "ResponsePlanIncidentTemplateArgs",
    "ResponsePlanIncidentTemplateArgsDict",
    "ResponsePlanIncidentTemplateNotificationTargetArgs",
    ...,
    "ResponsePlanIntegrationArgs",
    "ResponsePlanIntegrationArgsDict",
    "ResponsePlanIntegrationPagerdutyArgs",
    "ResponsePlanIntegrationPagerdutyArgsDict",
]

class ReplicationSetRegionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    status_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReplicationSetRegionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        status_message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status_message.setter
    def status_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResponsePlanActionArgsDict(TypedDict):
    ssm_automations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResponsePlanActionSsmAutomationArgsDict]]]
    ]

@pulumi.input_type
class ResponsePlanActionArgs:
    def __init__(
        __self__,
        *,
        ssm_automations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResponsePlanActionSsmAutomationArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ssmAutomations")
    def ssm_automations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResponsePlanActionSsmAutomationArgs]]]
    ]: ...
    @ssm_automations.setter
    def ssm_automations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResponsePlanActionSsmAutomationArgs]]]
        ],
    ): ...

class ResponsePlanActionSsmAutomationArgsDict(TypedDict):
    document_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    document_version: NotRequired[pulumi.Input[_builtins.str]]
    dynamic_parameters: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    parameters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ResponsePlanActionSsmAutomationParameterArgsDict]]
        ]
    ]
    target_account: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResponsePlanActionSsmAutomationArgs:
    def __init__(
        __self__,
        *,
        document_name: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        document_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        parameters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ResponsePlanActionSsmAutomationParameterArgs]]
            ]
        ] = ...,
        target_account: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="documentName")
    def document_name(self) -> pulumi.Input[_builtins.str]: ...
    @document_name.setter
    def document_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_version.setter
    def document_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dynamicParameters")
    def dynamic_parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @dynamic_parameters.setter
    def dynamic_parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ResponsePlanActionSsmAutomationParameterArgs]]
        ]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ResponsePlanActionSsmAutomationParameterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetAccount")
    def target_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_account.setter
    def target_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResponsePlanActionSsmAutomationParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ResponsePlanActionSsmAutomationParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ResponsePlanIncidentTemplateArgsDict(TypedDict):
    impact: pulumi.Input[_builtins.int]
    title: pulumi.Input[_builtins.str]
    dedupe_string: NotRequired[pulumi.Input[_builtins.str]]
    incident_tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    notification_targets: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ResponsePlanIncidentTemplateNotificationTargetArgsDict]
            ]
        ]
    ]
    summary: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResponsePlanIncidentTemplateArgs:
    def __init__(
        __self__,
        *,
        impact: pulumi.Input[_builtins.int],
        title: pulumi.Input[_builtins.str],
        dedupe_string: Optional[pulumi.Input[_builtins.str]] = ...,
        incident_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        notification_targets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ResponsePlanIncidentTemplateNotificationTargetArgs]
                ]
            ]
        ] = ...,
        summary: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def impact(self) -> pulumi.Input[_builtins.int]: ...
    @impact.setter
    def impact(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dedupeString")
    def dedupe_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dedupe_string.setter
    def dedupe_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="incidentTags")
    def incident_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @incident_tags.setter
    def incident_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationTargets")
    def notification_targets(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ResponsePlanIncidentTemplateNotificationTargetArgs]]
        ]
    ]: ...
    @notification_targets.setter
    def notification_targets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ResponsePlanIncidentTemplateNotificationTargetArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def summary(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @summary.setter
    def summary(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResponsePlanIncidentTemplateNotificationTargetArgsDict(TypedDict):
    sns_topic_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class ResponsePlanIncidentTemplateNotificationTargetArgs:
    def __init__(__self__, *, sns_topic_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> pulumi.Input[_builtins.str]: ...
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: pulumi.Input[_builtins.str]): ...

class ResponsePlanIntegrationArgsDict(TypedDict):
    pagerduties: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResponsePlanIntegrationPagerdutyArgsDict]]]
    ]

@pulumi.input_type
class ResponsePlanIntegrationArgs:
    def __init__(
        __self__,
        *,
        pagerduties: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResponsePlanIntegrationPagerdutyArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pagerduties(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResponsePlanIntegrationPagerdutyArgs]]]
    ]: ...
    @pagerduties.setter
    def pagerduties(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResponsePlanIntegrationPagerdutyArgs]]]
        ],
    ): ...

class ResponsePlanIntegrationPagerdutyArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    secret_id: pulumi.Input[_builtins.str]
    service_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ResponsePlanIntegrationPagerdutyArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        secret_id: pulumi.Input[_builtins.str],
        service_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Input[_builtins.str]: ...
    @secret_id.setter
    def secret_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Input[_builtins.str]: ...
    @service_id.setter
    def service_id(self, value: pulumi.Input[_builtins.str]): ...
