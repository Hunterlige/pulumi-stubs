import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EventSourcesConfigEventSourceArgs",
    "EventSourcesConfigEventSourceArgsDict",
    ...,
    ...,
    "NotificationChannelFiltersArgs",
    "NotificationChannelFiltersArgsDict",
    "NotificationChannelSnsArgs",
    "NotificationChannelSnsArgsDict",
    "ResourceCollectionCloudformationArgs",
    "ResourceCollectionCloudformationArgsDict",
    "ResourceCollectionTagsArgs",
    "ResourceCollectionTagsArgsDict",
    "ServiceIntegrationKmsServerSideEncryptionArgs",
    "ServiceIntegrationKmsServerSideEncryptionArgsDict",
    "ServiceIntegrationLogsAnomalyDetectionArgs",
    "ServiceIntegrationLogsAnomalyDetectionArgsDict",
    "ServiceIntegrationOpsCenterArgs",
    "ServiceIntegrationOpsCenterArgsDict",
    "GetNotificationChannelFilterArgs",
    "GetNotificationChannelFilterArgsDict",
    "GetNotificationChannelSnArgs",
    "GetNotificationChannelSnArgsDict",
]

class EventSourcesConfigEventSourceArgsDict(TypedDict):
    amazon_code_guru_profilers: pulumi.Input[
        Sequence[
            pulumi.Input[EventSourcesConfigEventSourceAmazonCodeGuruProfilerArgsDict]
        ]
    ]

@pulumi.input_type
class EventSourcesConfigEventSourceArgs:
    def __init__(
        __self__,
        *,
        amazon_code_guru_profilers: pulumi.Input[
            Sequence[
                pulumi.Input[EventSourcesConfigEventSourceAmazonCodeGuruProfilerArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonCodeGuruProfilers")
    def amazon_code_guru_profilers(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[EventSourcesConfigEventSourceAmazonCodeGuruProfilerArgs]]
    ]: ...
    @amazon_code_guru_profilers.setter
    def amazon_code_guru_profilers(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[EventSourcesConfigEventSourceAmazonCodeGuruProfilerArgs]
            ]
        ],
    ): ...

class EventSourcesConfigEventSourceAmazonCodeGuruProfilerArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventSourcesConfigEventSourceAmazonCodeGuruProfilerArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...

class NotificationChannelFiltersArgsDict(TypedDict):
    message_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    severities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class NotificationChannelFiltersArgs:
    def __init__(
        __self__,
        *,
        message_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        severities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageTypes")
    def message_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @message_types.setter
    def message_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def severities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @severities.setter
    def severities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class NotificationChannelSnsArgsDict(TypedDict):
    topic_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class NotificationChannelSnsArgs:
    def __init__(__self__, *, topic_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Input[_builtins.str]: ...
    @topic_arn.setter
    def topic_arn(self, value: pulumi.Input[_builtins.str]): ...

class ResourceCollectionCloudformationArgsDict(TypedDict):
    stack_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ResourceCollectionCloudformationArgs:
    def __init__(
        __self__, *, stack_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stackNames")
    def stack_names(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @stack_names.setter
    def stack_names(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class ResourceCollectionTagsArgsDict(TypedDict):
    app_boundary_key: pulumi.Input[_builtins.str]
    tag_values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ResourceCollectionTagsArgs:
    def __init__(
        __self__,
        *,
        app_boundary_key: pulumi.Input[_builtins.str],
        tag_values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appBoundaryKey")
    def app_boundary_key(self) -> pulumi.Input[_builtins.str]: ...
    @app_boundary_key.setter
    def app_boundary_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @tag_values.setter
    def tag_values(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class ServiceIntegrationKmsServerSideEncryptionArgsDict(TypedDict):
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    opt_in_status: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceIntegrationKmsServerSideEncryptionArgs:
    def __init__(
        __self__,
        *,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        opt_in_status: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="optInStatus")
    def opt_in_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @opt_in_status.setter
    def opt_in_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceIntegrationLogsAnomalyDetectionArgsDict(TypedDict):
    opt_in_status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceIntegrationLogsAnomalyDetectionArgs:
    def __init__(
        __self__, *, opt_in_status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optInStatus")
    def opt_in_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @opt_in_status.setter
    def opt_in_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceIntegrationOpsCenterArgsDict(TypedDict):
    opt_in_status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceIntegrationOpsCenterArgs:
    def __init__(
        __self__, *, opt_in_status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optInStatus")
    def opt_in_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @opt_in_status.setter
    def opt_in_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GetNotificationChannelFilterArgsDict(TypedDict):
    message_types: Sequence[_builtins.str]
    severities: Sequence[_builtins.str]

@pulumi.input_type
class GetNotificationChannelFilterArgs:
    def __init__(
        __self__,
        *,
        message_types: Sequence[_builtins.str],
        severities: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageTypes")
    def message_types(self) -> Sequence[_builtins.str]: ...
    @message_types.setter
    def message_types(self, value: Sequence[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def severities(self) -> Sequence[_builtins.str]: ...
    @severities.setter
    def severities(self, value: Sequence[_builtins.str]): ...

class GetNotificationChannelSnArgsDict(TypedDict):
    topic_arn: _builtins.str

@pulumi.input_type
class GetNotificationChannelSnArgs:
    def __init__(__self__, *, topic_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> _builtins.str: ...
    @topic_arn.setter
    def topic_arn(self, value: _builtins.str): ...
