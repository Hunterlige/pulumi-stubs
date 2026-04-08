import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from .. import iam

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CompositeAlarmActionsSuppressorArgs",
    "CompositeAlarmActionsSuppressorArgsDict",
    "EventBusDeadLetterConfigArgs",
    "EventBusDeadLetterConfigArgsDict",
    "EventBusLogConfigArgs",
    "EventBusLogConfigArgsDict",
    "EventConnectionAuthParametersArgs",
    "EventConnectionAuthParametersArgsDict",
    "EventConnectionAuthParametersApiKeyArgs",
    "EventConnectionAuthParametersApiKeyArgsDict",
    "EventConnectionAuthParametersBasicArgs",
    "EventConnectionAuthParametersBasicArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "EventConnectionAuthParametersOauthArgs",
    "EventConnectionAuthParametersOauthArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "EventEndpointEventBusArgs",
    "EventEndpointEventBusArgsDict",
    "EventEndpointReplicationConfigArgs",
    "EventEndpointReplicationConfigArgsDict",
    "EventEndpointRoutingConfigArgs",
    "EventEndpointRoutingConfigArgsDict",
    "EventEndpointRoutingConfigFailoverConfigArgs",
    "EventEndpointRoutingConfigFailoverConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "EventPermissionConditionArgs",
    "EventPermissionConditionArgsDict",
    "EventTargetAppsyncTargetArgs",
    "EventTargetAppsyncTargetArgsDict",
    "EventTargetBatchTargetArgs",
    "EventTargetBatchTargetArgsDict",
    "EventTargetDeadLetterConfigArgs",
    "EventTargetDeadLetterConfigArgsDict",
    "EventTargetEcsTargetArgs",
    "EventTargetEcsTargetArgsDict",
    "EventTargetEcsTargetCapacityProviderStrategyArgs",
    ...,
    "EventTargetEcsTargetNetworkConfigurationArgs",
    "EventTargetEcsTargetNetworkConfigurationArgsDict",
    "EventTargetEcsTargetOrderedPlacementStrategyArgs",
    ...,
    "EventTargetEcsTargetPlacementConstraintArgs",
    "EventTargetEcsTargetPlacementConstraintArgsDict",
    "EventTargetHttpTargetArgs",
    "EventTargetHttpTargetArgsDict",
    "EventTargetInputTransformerArgs",
    "EventTargetInputTransformerArgsDict",
    "EventTargetKinesisTargetArgs",
    "EventTargetKinesisTargetArgsDict",
    "EventTargetRedshiftTargetArgs",
    "EventTargetRedshiftTargetArgsDict",
    "EventTargetRetryPolicyArgs",
    "EventTargetRetryPolicyArgsDict",
    "EventTargetRunCommandTargetArgs",
    "EventTargetRunCommandTargetArgsDict",
    "EventTargetSagemakerPipelineTargetArgs",
    "EventTargetSagemakerPipelineTargetArgsDict",
    ...,
    ...,
    "EventTargetSqsTargetArgs",
    "EventTargetSqsTargetArgsDict",
    "InternetMonitorHealthEventsConfigArgs",
    "InternetMonitorHealthEventsConfigArgsDict",
    "InternetMonitorInternetMeasurementsLogDeliveryArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "LogDeliveryS3DeliveryConfigurationArgs",
    "LogDeliveryS3DeliveryConfigurationArgsDict",
    "LogMetricFilterMetricTransformationArgs",
    "LogMetricFilterMetricTransformationArgsDict",
    "LogTransformerTransformerConfigArgs",
    "LogTransformerTransformerConfigArgsDict",
    "LogTransformerTransformerConfigAddKeysArgs",
    "LogTransformerTransformerConfigAddKeysArgsDict",
    "LogTransformerTransformerConfigAddKeysEntryArgs",
    ...,
    "LogTransformerTransformerConfigCopyValueArgs",
    "LogTransformerTransformerConfigCopyValueArgsDict",
    "LogTransformerTransformerConfigCopyValueEntryArgs",
    ...,
    "LogTransformerTransformerConfigCsvArgs",
    "LogTransformerTransformerConfigCsvArgsDict",
    ...,
    ...,
    "LogTransformerTransformerConfigDeleteKeyArgs",
    "LogTransformerTransformerConfigDeleteKeyArgsDict",
    "LogTransformerTransformerConfigGrokArgs",
    "LogTransformerTransformerConfigGrokArgsDict",
    "LogTransformerTransformerConfigListToMapArgs",
    "LogTransformerTransformerConfigListToMapArgsDict",
    "LogTransformerTransformerConfigLowerCaseStringArgs",
    ...,
    "LogTransformerTransformerConfigMoveKeyArgs",
    "LogTransformerTransformerConfigMoveKeyArgsDict",
    "LogTransformerTransformerConfigMoveKeyEntryArgs",
    ...,
    "LogTransformerTransformerConfigParseCloudfrontArgs",
    ...,
    "LogTransformerTransformerConfigParseJsonArgs",
    "LogTransformerTransformerConfigParseJsonArgsDict",
    "LogTransformerTransformerConfigParseKeyValueArgs",
    ...,
    "LogTransformerTransformerConfigParsePostgresArgs",
    ...,
    "LogTransformerTransformerConfigParseRoute53Args",
    ...,
    "LogTransformerTransformerConfigParseToOcsfArgs",
    "LogTransformerTransformerConfigParseToOcsfArgsDict",
    "LogTransformerTransformerConfigParseVpcArgs",
    "LogTransformerTransformerConfigParseVpcArgsDict",
    "LogTransformerTransformerConfigParseWafArgs",
    "LogTransformerTransformerConfigParseWafArgsDict",
    "LogTransformerTransformerConfigRenameKeyArgs",
    "LogTransformerTransformerConfigRenameKeyArgsDict",
    "LogTransformerTransformerConfigRenameKeyEntryArgs",
    ...,
    "LogTransformerTransformerConfigSplitStringArgs",
    "LogTransformerTransformerConfigSplitStringArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "LogTransformerTransformerConfigTrimStringArgs",
    "LogTransformerTransformerConfigTrimStringArgsDict",
    "LogTransformerTransformerConfigTypeConverterArgs",
    ...,
    ...,
    ...,
    "LogTransformerTransformerConfigUpperCaseStringArgs",
    ...,
    "MetricAlarmMetricQueryArgs",
    "MetricAlarmMetricQueryArgsDict",
    "MetricAlarmMetricQueryMetricArgs",
    "MetricAlarmMetricQueryMetricArgsDict",
    "MetricStreamExcludeFilterArgs",
    "MetricStreamExcludeFilterArgsDict",
    "MetricStreamIncludeFilterArgs",
    "MetricStreamIncludeFilterArgsDict",
    "MetricStreamStatisticsConfigurationArgs",
    "MetricStreamStatisticsConfigurationArgsDict",
    ...,
    ...,
    "PolicyDocumentArgs",
    "PolicyDocumentArgsDict",
    ...,
    ...,
    ...,
    ...,
    "GetLogDataProtectionPolicyDocumentStatementArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

class CompositeAlarmActionsSuppressorArgsDict(TypedDict):
    alarm: pulumi.Input[_builtins.str]
    extension_period: pulumi.Input[_builtins.int]
    wait_period: pulumi.Input[_builtins.int]

@pulumi.input_type
class CompositeAlarmActionsSuppressorArgs:
    def __init__(
        __self__,
        *,
        alarm: pulumi.Input[_builtins.str],
        extension_period: pulumi.Input[_builtins.int],
        wait_period: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alarm(self) -> pulumi.Input[_builtins.str]: ...
    @alarm.setter
    def alarm(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="extensionPeriod")
    def extension_period(self) -> pulumi.Input[_builtins.int]: ...
    @extension_period.setter
    def extension_period(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="waitPeriod")
    def wait_period(self) -> pulumi.Input[_builtins.int]: ...
    @wait_period.setter
    def wait_period(self, value: pulumi.Input[_builtins.int]): ...

class EventBusDeadLetterConfigArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventBusDeadLetterConfigArgs:
    def __init__(
        __self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventBusLogConfigArgsDict(TypedDict):
    include_detail: NotRequired[pulumi.Input[_builtins.str]]
    level: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventBusLogConfigArgs:
    def __init__(
        __self__,
        *,
        include_detail: Optional[pulumi.Input[_builtins.str]] = ...,
        level: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeDetail")
    def include_detail(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @include_detail.setter
    def include_detail(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @level.setter
    def level(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventConnectionAuthParametersArgsDict(TypedDict):
    api_key: NotRequired[pulumi.Input[EventConnectionAuthParametersApiKeyArgsDict]]
    basic: NotRequired[pulumi.Input[EventConnectionAuthParametersBasicArgsDict]]
    connectivity_parameters: NotRequired[
        pulumi.Input[EventConnectionAuthParametersConnectivityParametersArgsDict]
    ]
    invocation_http_parameters: NotRequired[
        pulumi.Input[EventConnectionAuthParametersInvocationHttpParametersArgsDict]
    ]
    oauth: NotRequired[pulumi.Input[EventConnectionAuthParametersOauthArgsDict]]

@pulumi.input_type
class EventConnectionAuthParametersArgs:
    def __init__(
        __self__,
        *,
        api_key: Optional[pulumi.Input[EventConnectionAuthParametersApiKeyArgs]] = ...,
        basic: Optional[pulumi.Input[EventConnectionAuthParametersBasicArgs]] = ...,
        connectivity_parameters: Optional[
            pulumi.Input[EventConnectionAuthParametersConnectivityParametersArgs]
        ] = ...,
        invocation_http_parameters: Optional[
            pulumi.Input[EventConnectionAuthParametersInvocationHttpParametersArgs]
        ] = ...,
        oauth: Optional[pulumi.Input[EventConnectionAuthParametersOauthArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(
        self,
    ) -> Optional[pulumi.Input[EventConnectionAuthParametersApiKeyArgs]]: ...
    @api_key.setter
    def api_key(
        self, value: Optional[pulumi.Input[EventConnectionAuthParametersApiKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def basic(
        self,
    ) -> Optional[pulumi.Input[EventConnectionAuthParametersBasicArgs]]: ...
    @basic.setter
    def basic(
        self, value: Optional[pulumi.Input[EventConnectionAuthParametersBasicArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectivityParameters")
    def connectivity_parameters(
        self,
    ) -> Optional[
        pulumi.Input[EventConnectionAuthParametersConnectivityParametersArgs]
    ]: ...
    @connectivity_parameters.setter
    def connectivity_parameters(
        self,
        value: Optional[
            pulumi.Input[EventConnectionAuthParametersConnectivityParametersArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="invocationHttpParameters")
    def invocation_http_parameters(
        self,
    ) -> Optional[
        pulumi.Input[EventConnectionAuthParametersInvocationHttpParametersArgs]
    ]: ...
    @invocation_http_parameters.setter
    def invocation_http_parameters(
        self,
        value: Optional[
            pulumi.Input[EventConnectionAuthParametersInvocationHttpParametersArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def oauth(
        self,
    ) -> Optional[pulumi.Input[EventConnectionAuthParametersOauthArgs]]: ...
    @oauth.setter
    def oauth(
        self, value: Optional[pulumi.Input[EventConnectionAuthParametersOauthArgs]]
    ): ...

class EventConnectionAuthParametersApiKeyArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventConnectionAuthParametersApiKeyArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class EventConnectionAuthParametersBasicArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventConnectionAuthParametersBasicArgs:
    def __init__(
        __self__,
        *,
        password: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]: ...
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...

class EventConnectionAuthParametersConnectivityParametersArgsDict(TypedDict):
    resource_parameters: pulumi.Input[
        EventConnectionAuthParametersConnectivityParametersResourceParametersArgsDict
    ]

@pulumi.input_type
class EventConnectionAuthParametersConnectivityParametersArgs:
    def __init__(
        __self__,
        *,
        resource_parameters: pulumi.Input[
            EventConnectionAuthParametersConnectivityParametersResourceParametersArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceParameters")
    def resource_parameters(
        self,
    ) -> pulumi.Input[
        EventConnectionAuthParametersConnectivityParametersResourceParametersArgs
    ]: ...
    @resource_parameters.setter
    def resource_parameters(
        self,
        value: pulumi.Input[
            EventConnectionAuthParametersConnectivityParametersResourceParametersArgs
        ],
    ): ...

class EventConnectionAuthParametersConnectivityParametersResourceParametersArgsDict(
    TypedDict
):
    resource_configuration_arn: pulumi.Input[_builtins.str]
    resource_association_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventConnectionAuthParametersConnectivityParametersResourceParametersArgs:
    def __init__(
        __self__,
        *,
        resource_configuration_arn: pulumi.Input[_builtins.str],
        resource_association_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationArn")
    def resource_configuration_arn(self) -> pulumi.Input[_builtins.str]: ...
    @resource_configuration_arn.setter
    def resource_configuration_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceAssociationArn")
    def resource_association_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_association_arn.setter
    def resource_association_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class EventConnectionAuthParametersInvocationHttpParametersArgsDict(TypedDict):
    bodies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventConnectionAuthParametersInvocationHttpParametersBodyArgsDict
                ]
            ]
        ]
    ]
    headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventConnectionAuthParametersInvocationHttpParametersHeaderArgsDict
                ]
            ]
        ]
    ]
    query_strings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventConnectionAuthParametersInvocationHttpParametersQueryStringArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class EventConnectionAuthParametersInvocationHttpParametersArgs:
    def __init__(
        __self__,
        *,
        bodies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventConnectionAuthParametersInvocationHttpParametersBodyArgs
                    ]
                ]
            ]
        ] = ...,
        headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventConnectionAuthParametersInvocationHttpParametersHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        query_strings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventConnectionAuthParametersInvocationHttpParametersQueryStringArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bodies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventConnectionAuthParametersInvocationHttpParametersBodyArgs
                ]
            ]
        ]
    ]: ...
    @bodies.setter
    def bodies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventConnectionAuthParametersInvocationHttpParametersBodyArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventConnectionAuthParametersInvocationHttpParametersHeaderArgs
                ]
            ]
        ]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventConnectionAuthParametersInvocationHttpParametersHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventConnectionAuthParametersInvocationHttpParametersQueryStringArgs
                ]
            ]
        ]
    ]: ...
    @query_strings.setter
    def query_strings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventConnectionAuthParametersInvocationHttpParametersQueryStringArgs
                    ]
                ]
            ]
        ],
    ): ...

class EventConnectionAuthParametersInvocationHttpParametersBodyArgsDict(TypedDict):
    is_value_secret: NotRequired[pulumi.Input[_builtins.bool]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventConnectionAuthParametersInvocationHttpParametersBodyArgs:
    def __init__(
        __self__,
        *,
        is_value_secret: Optional[pulumi.Input[_builtins.bool]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isValueSecret")
    def is_value_secret(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_value_secret.setter
    def is_value_secret(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventConnectionAuthParametersInvocationHttpParametersHeaderArgsDict(TypedDict):
    is_value_secret: NotRequired[pulumi.Input[_builtins.bool]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventConnectionAuthParametersInvocationHttpParametersHeaderArgs:
    def __init__(
        __self__,
        *,
        is_value_secret: Optional[pulumi.Input[_builtins.bool]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isValueSecret")
    def is_value_secret(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_value_secret.setter
    def is_value_secret(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventConnectionAuthParametersInvocationHttpParametersQueryStringArgsDict(
    TypedDict
):
    is_value_secret: NotRequired[pulumi.Input[_builtins.bool]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventConnectionAuthParametersInvocationHttpParametersQueryStringArgs:
    def __init__(
        __self__,
        *,
        is_value_secret: Optional[pulumi.Input[_builtins.bool]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isValueSecret")
    def is_value_secret(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_value_secret.setter
    def is_value_secret(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventConnectionAuthParametersOauthArgsDict(TypedDict):
    authorization_endpoint: pulumi.Input[_builtins.str]
    http_method: pulumi.Input[_builtins.str]
    oauth_http_parameters: pulumi.Input[
        EventConnectionAuthParametersOauthOauthHttpParametersArgsDict
    ]
    client_parameters: NotRequired[
        pulumi.Input[EventConnectionAuthParametersOauthClientParametersArgsDict]
    ]

@pulumi.input_type
class EventConnectionAuthParametersOauthArgs:
    def __init__(
        __self__,
        *,
        authorization_endpoint: pulumi.Input[_builtins.str],
        http_method: pulumi.Input[_builtins.str],
        oauth_http_parameters: pulumi.Input[
            EventConnectionAuthParametersOauthOauthHttpParametersArgs
        ],
        client_parameters: Optional[
            pulumi.Input[EventConnectionAuthParametersOauthClientParametersArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> pulumi.Input[_builtins.str]: ...
    @http_method.setter
    def http_method(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oauthHttpParameters")
    def oauth_http_parameters(
        self,
    ) -> pulumi.Input[EventConnectionAuthParametersOauthOauthHttpParametersArgs]: ...
    @oauth_http_parameters.setter
    def oauth_http_parameters(
        self,
        value: pulumi.Input[EventConnectionAuthParametersOauthOauthHttpParametersArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientParameters")
    def client_parameters(
        self,
    ) -> Optional[
        pulumi.Input[EventConnectionAuthParametersOauthClientParametersArgs]
    ]: ...
    @client_parameters.setter
    def client_parameters(
        self,
        value: Optional[
            pulumi.Input[EventConnectionAuthParametersOauthClientParametersArgs]
        ],
    ): ...

class EventConnectionAuthParametersOauthClientParametersArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventConnectionAuthParametersOauthClientParametersArgs:
    def __init__(
        __self__,
        *,
        client_id: pulumi.Input[_builtins.str],
        client_secret: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]: ...
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): ...

class EventConnectionAuthParametersOauthOauthHttpParametersArgsDict(TypedDict):
    bodies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventConnectionAuthParametersOauthOauthHttpParametersBodyArgsDict
                ]
            ]
        ]
    ]
    headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventConnectionAuthParametersOauthOauthHttpParametersHeaderArgsDict
                ]
            ]
        ]
    ]
    query_strings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventConnectionAuthParametersOauthOauthHttpParametersQueryStringArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class EventConnectionAuthParametersOauthOauthHttpParametersArgs:
    def __init__(
        __self__,
        *,
        bodies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventConnectionAuthParametersOauthOauthHttpParametersBodyArgs
                    ]
                ]
            ]
        ] = ...,
        headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventConnectionAuthParametersOauthOauthHttpParametersHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        query_strings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventConnectionAuthParametersOauthOauthHttpParametersQueryStringArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bodies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventConnectionAuthParametersOauthOauthHttpParametersBodyArgs
                ]
            ]
        ]
    ]: ...
    @bodies.setter
    def bodies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventConnectionAuthParametersOauthOauthHttpParametersBodyArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventConnectionAuthParametersOauthOauthHttpParametersHeaderArgs
                ]
            ]
        ]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventConnectionAuthParametersOauthOauthHttpParametersHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventConnectionAuthParametersOauthOauthHttpParametersQueryStringArgs
                ]
            ]
        ]
    ]: ...
    @query_strings.setter
    def query_strings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventConnectionAuthParametersOauthOauthHttpParametersQueryStringArgs
                    ]
                ]
            ]
        ],
    ): ...

class EventConnectionAuthParametersOauthOauthHttpParametersBodyArgsDict(TypedDict):
    is_value_secret: NotRequired[pulumi.Input[_builtins.bool]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventConnectionAuthParametersOauthOauthHttpParametersBodyArgs:
    def __init__(
        __self__,
        *,
        is_value_secret: Optional[pulumi.Input[_builtins.bool]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isValueSecret")
    def is_value_secret(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_value_secret.setter
    def is_value_secret(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventConnectionAuthParametersOauthOauthHttpParametersHeaderArgsDict(TypedDict):
    is_value_secret: NotRequired[pulumi.Input[_builtins.bool]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventConnectionAuthParametersOauthOauthHttpParametersHeaderArgs:
    def __init__(
        __self__,
        *,
        is_value_secret: Optional[pulumi.Input[_builtins.bool]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isValueSecret")
    def is_value_secret(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_value_secret.setter
    def is_value_secret(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventConnectionAuthParametersOauthOauthHttpParametersQueryStringArgsDict(
    TypedDict
):
    is_value_secret: NotRequired[pulumi.Input[_builtins.bool]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventConnectionAuthParametersOauthOauthHttpParametersQueryStringArgs:
    def __init__(
        __self__,
        *,
        is_value_secret: Optional[pulumi.Input[_builtins.bool]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isValueSecret")
    def is_value_secret(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_value_secret.setter
    def is_value_secret(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventConnectionInvocationConnectivityParametersArgsDict(TypedDict):
    resource_parameters: pulumi.Input[
        EventConnectionInvocationConnectivityParametersResourceParametersArgsDict
    ]

@pulumi.input_type
class EventConnectionInvocationConnectivityParametersArgs:
    def __init__(
        __self__,
        *,
        resource_parameters: pulumi.Input[
            EventConnectionInvocationConnectivityParametersResourceParametersArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceParameters")
    def resource_parameters(
        self,
    ) -> pulumi.Input[
        EventConnectionInvocationConnectivityParametersResourceParametersArgs
    ]: ...
    @resource_parameters.setter
    def resource_parameters(
        self,
        value: pulumi.Input[
            EventConnectionInvocationConnectivityParametersResourceParametersArgs
        ],
    ): ...

class EventConnectionInvocationConnectivityParametersResourceParametersArgsDict(
    TypedDict
):
    resource_configuration_arn: pulumi.Input[_builtins.str]
    resource_association_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventConnectionInvocationConnectivityParametersResourceParametersArgs:
    def __init__(
        __self__,
        *,
        resource_configuration_arn: pulumi.Input[_builtins.str],
        resource_association_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationArn")
    def resource_configuration_arn(self) -> pulumi.Input[_builtins.str]: ...
    @resource_configuration_arn.setter
    def resource_configuration_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceAssociationArn")
    def resource_association_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_association_arn.setter
    def resource_association_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class EventEndpointEventBusArgsDict(TypedDict):
    event_bus_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventEndpointEventBusArgs:
    def __init__(__self__, *, event_bus_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventBusArn")
    def event_bus_arn(self) -> pulumi.Input[_builtins.str]: ...
    @event_bus_arn.setter
    def event_bus_arn(self, value: pulumi.Input[_builtins.str]): ...

class EventEndpointReplicationConfigArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventEndpointReplicationConfigArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventEndpointRoutingConfigArgsDict(TypedDict):
    failover_config: pulumi.Input[EventEndpointRoutingConfigFailoverConfigArgsDict]

@pulumi.input_type
class EventEndpointRoutingConfigArgs:
    def __init__(
        __self__,
        *,
        failover_config: pulumi.Input[EventEndpointRoutingConfigFailoverConfigArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failoverConfig")
    def failover_config(
        self,
    ) -> pulumi.Input[EventEndpointRoutingConfigFailoverConfigArgs]: ...
    @failover_config.setter
    def failover_config(
        self, value: pulumi.Input[EventEndpointRoutingConfigFailoverConfigArgs]
    ): ...

class EventEndpointRoutingConfigFailoverConfigArgsDict(TypedDict):
    primary: pulumi.Input[EventEndpointRoutingConfigFailoverConfigPrimaryArgsDict]
    secondary: pulumi.Input[EventEndpointRoutingConfigFailoverConfigSecondaryArgsDict]

@pulumi.input_type
class EventEndpointRoutingConfigFailoverConfigArgs:
    def __init__(
        __self__,
        *,
        primary: pulumi.Input[EventEndpointRoutingConfigFailoverConfigPrimaryArgs],
        secondary: pulumi.Input[EventEndpointRoutingConfigFailoverConfigSecondaryArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def primary(
        self,
    ) -> pulumi.Input[EventEndpointRoutingConfigFailoverConfigPrimaryArgs]: ...
    @primary.setter
    def primary(
        self, value: pulumi.Input[EventEndpointRoutingConfigFailoverConfigPrimaryArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def secondary(
        self,
    ) -> pulumi.Input[EventEndpointRoutingConfigFailoverConfigSecondaryArgs]: ...
    @secondary.setter
    def secondary(
        self, value: pulumi.Input[EventEndpointRoutingConfigFailoverConfigSecondaryArgs]
    ): ...

class EventEndpointRoutingConfigFailoverConfigPrimaryArgsDict(TypedDict):
    health_check: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventEndpointRoutingConfigFailoverConfigPrimaryArgs:
    def __init__(
        __self__, *, health_check: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_check.setter
    def health_check(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventEndpointRoutingConfigFailoverConfigSecondaryArgsDict(TypedDict):
    route: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventEndpointRoutingConfigFailoverConfigSecondaryArgs:
    def __init__(
        __self__, *, route: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def route(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @route.setter
    def route(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventPermissionConditionArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventPermissionConditionArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class EventTargetAppsyncTargetArgsDict(TypedDict):
    graphql_operation: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventTargetAppsyncTargetArgs:
    def __init__(
        __self__, *, graphql_operation: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="graphqlOperation")
    def graphql_operation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @graphql_operation.setter
    def graphql_operation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventTargetBatchTargetArgsDict(TypedDict):
    job_definition: pulumi.Input[_builtins.str]
    job_name: pulumi.Input[_builtins.str]
    array_size: NotRequired[pulumi.Input[_builtins.int]]
    job_attempts: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class EventTargetBatchTargetArgs:
    def __init__(
        __self__,
        *,
        job_definition: pulumi.Input[_builtins.str],
        job_name: pulumi.Input[_builtins.str],
        array_size: Optional[pulumi.Input[_builtins.int]] = ...,
        job_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobDefinition")
    def job_definition(self) -> pulumi.Input[_builtins.str]: ...
    @job_definition.setter
    def job_definition(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Input[_builtins.str]: ...
    @job_name.setter
    def job_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="arraySize")
    def array_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @array_size.setter
    def array_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="jobAttempts")
    def job_attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @job_attempts.setter
    def job_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class EventTargetDeadLetterConfigArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventTargetDeadLetterConfigArgs:
    def __init__(
        __self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventTargetEcsTargetArgsDict(TypedDict):
    task_definition_arn: pulumi.Input[_builtins.str]
    capacity_provider_strategies: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[EventTargetEcsTargetCapacityProviderStrategyArgsDict]]
        ]
    ]
    enable_ecs_managed_tags: NotRequired[pulumi.Input[_builtins.bool]]
    enable_execute_command: NotRequired[pulumi.Input[_builtins.bool]]
    group: NotRequired[pulumi.Input[_builtins.str]]
    launch_type: NotRequired[pulumi.Input[_builtins.str]]
    network_configuration: NotRequired[
        pulumi.Input[EventTargetEcsTargetNetworkConfigurationArgsDict]
    ]
    ordered_placement_strategies: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[EventTargetEcsTargetOrderedPlacementStrategyArgsDict]]
        ]
    ]
    placement_constraints: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[EventTargetEcsTargetPlacementConstraintArgsDict]]
        ]
    ]
    platform_version: NotRequired[pulumi.Input[_builtins.str]]
    propagate_tags: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    task_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class EventTargetEcsTargetArgs:
    def __init__(
        __self__,
        *,
        task_definition_arn: pulumi.Input[_builtins.str],
        capacity_provider_strategies: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EventTargetEcsTargetCapacityProviderStrategyArgs]]
            ]
        ] = ...,
        enable_ecs_managed_tags: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_execute_command: Optional[pulumi.Input[_builtins.bool]] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        launch_type: Optional[pulumi.Input[_builtins.str]] = ...,
        network_configuration: Optional[
            pulumi.Input[EventTargetEcsTargetNetworkConfigurationArgs]
        ] = ...,
        ordered_placement_strategies: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EventTargetEcsTargetOrderedPlacementStrategyArgs]]
            ]
        ] = ...,
        placement_constraints: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EventTargetEcsTargetPlacementConstraintArgs]]
            ]
        ] = ...,
        platform_version: Optional[pulumi.Input[_builtins.str]] = ...,
        propagate_tags: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        task_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskDefinitionArn")
    def task_definition_arn(self) -> pulumi.Input[_builtins.str]: ...
    @task_definition_arn.setter
    def task_definition_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[EventTargetEcsTargetCapacityProviderStrategyArgs]]
        ]
    ]: ...
    @capacity_provider_strategies.setter
    def capacity_provider_strategies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EventTargetEcsTargetCapacityProviderStrategyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_ecs_managed_tags.setter
    def enable_ecs_managed_tags(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableExecuteCommand")
    def enable_execute_command(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_execute_command.setter
    def enable_execute_command(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group.setter
    def group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_type.setter
    def launch_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[pulumi.Input[EventTargetEcsTargetNetworkConfigurationArgs]]: ...
    @network_configuration.setter
    def network_configuration(
        self,
        value: Optional[pulumi.Input[EventTargetEcsTargetNetworkConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="orderedPlacementStrategies")
    def ordered_placement_strategies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[EventTargetEcsTargetOrderedPlacementStrategyArgs]]
        ]
    ]: ...
    @ordered_placement_strategies.setter
    def ordered_placement_strategies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EventTargetEcsTargetOrderedPlacementStrategyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[EventTargetEcsTargetPlacementConstraintArgs]]
        ]
    ]: ...
    @placement_constraints.setter
    def placement_constraints(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EventTargetEcsTargetPlacementConstraintArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @propagate_tags.setter
    def propagate_tags(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="taskCount")
    def task_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @task_count.setter
    def task_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class EventTargetEcsTargetCapacityProviderStrategyArgsDict(TypedDict):
    capacity_provider: pulumi.Input[_builtins.str]
    base: NotRequired[pulumi.Input[_builtins.int]]
    weight: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class EventTargetEcsTargetCapacityProviderStrategyArgs:
    def __init__(
        __self__,
        *,
        capacity_provider: pulumi.Input[_builtins.str],
        base: Optional[pulumi.Input[_builtins.int]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_provider.setter
    def capacity_provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @base.setter
    def base(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class EventTargetEcsTargetNetworkConfigurationArgsDict(TypedDict):
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    assign_public_ip: NotRequired[pulumi.Input[_builtins.bool]]
    security_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class EventTargetEcsTargetNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        assign_public_ip: Optional[pulumi.Input[_builtins.bool]] = ...,
        security_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @assign_public_ip.setter
    def assign_public_ip(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_groups.setter
    def security_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class EventTargetEcsTargetOrderedPlacementStrategyArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    field: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventTargetEcsTargetOrderedPlacementStrategyArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        field: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field.setter
    def field(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventTargetEcsTargetPlacementConstraintArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    expression: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventTargetEcsTargetPlacementConstraintArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventTargetHttpTargetArgsDict(TypedDict):
    header_parameters: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    path_parameter_values: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    query_string_parameters: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class EventTargetHttpTargetArgs:
    def __init__(
        __self__,
        *,
        header_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        path_parameter_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        query_string_parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerParameters")
    def header_parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @header_parameters.setter
    def header_parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pathParameterValues")
    def path_parameter_values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @path_parameter_values.setter
    def path_parameter_values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryStringParameters")
    def query_string_parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @query_string_parameters.setter
    def query_string_parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class EventTargetInputTransformerArgsDict(TypedDict):
    input_template: pulumi.Input[_builtins.str]
    input_paths: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class EventTargetInputTransformerArgs:
    def __init__(
        __self__,
        *,
        input_template: pulumi.Input[_builtins.str],
        input_paths: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputTemplate")
    def input_template(self) -> pulumi.Input[_builtins.str]: ...
    @input_template.setter
    def input_template(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputPaths")
    def input_paths(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @input_paths.setter
    def input_paths(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class EventTargetKinesisTargetArgsDict(TypedDict):
    partition_key_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventTargetKinesisTargetArgs:
    def __init__(
        __self__, *, partition_key_path: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionKeyPath")
    def partition_key_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partition_key_path.setter
    def partition_key_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventTargetRedshiftTargetArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    db_user: NotRequired[pulumi.Input[_builtins.str]]
    secrets_manager_arn: NotRequired[pulumi.Input[_builtins.str]]
    sql: NotRequired[pulumi.Input[_builtins.str]]
    statement_name: NotRequired[pulumi.Input[_builtins.str]]
    with_event: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class EventTargetRedshiftTargetArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        db_user: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets_manager_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        sql: Optional[pulumi.Input[_builtins.str]] = ...,
        statement_name: Optional[pulumi.Input[_builtins.str]] = ...,
        with_event: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dbUser")
    def db_user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_user.setter
    def db_user(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerArn")
    def secrets_manager_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secrets_manager_arn.setter
    def secrets_manager_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sql(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sql.setter
    def sql(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statementName")
    def statement_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @statement_name.setter
    def statement_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="withEvent")
    def with_event(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @with_event.setter
    def with_event(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EventTargetRetryPolicyArgsDict(TypedDict):
    maximum_event_age_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    maximum_retry_attempts: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class EventTargetRetryPolicyArgs:
    def __init__(
        __self__,
        *,
        maximum_event_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_retry_attempts: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_event_age_in_seconds.setter
    def maximum_event_age_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class EventTargetRunCommandTargetArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class EventTargetRunCommandTargetArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class EventTargetSagemakerPipelineTargetArgsDict(TypedDict):
    pipeline_parameter_lists: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventTargetSagemakerPipelineTargetPipelineParameterListArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class EventTargetSagemakerPipelineTargetArgs:
    def __init__(
        __self__,
        *,
        pipeline_parameter_lists: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventTargetSagemakerPipelineTargetPipelineParameterListArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pipelineParameterLists")
    def pipeline_parameter_lists(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EventTargetSagemakerPipelineTargetPipelineParameterListArgs
                ]
            ]
        ]
    ]: ...
    @pipeline_parameter_lists.setter
    def pipeline_parameter_lists(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EventTargetSagemakerPipelineTargetPipelineParameterListArgs
                    ]
                ]
            ]
        ],
    ): ...

class EventTargetSagemakerPipelineTargetPipelineParameterListArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventTargetSagemakerPipelineTargetPipelineParameterListArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class EventTargetSqsTargetArgsDict(TypedDict):
    message_group_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventTargetSqsTargetArgs:
    def __init__(
        __self__, *, message_group_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageGroupId")
    def message_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_group_id.setter
    def message_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InternetMonitorHealthEventsConfigArgsDict(TypedDict):
    availability_score_threshold: NotRequired[pulumi.Input[_builtins.float]]
    performance_score_threshold: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class InternetMonitorHealthEventsConfigArgs:
    def __init__(
        __self__,
        *,
        availability_score_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
        performance_score_threshold: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityScoreThreshold")
    def availability_score_threshold(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @availability_score_threshold.setter
    def availability_score_threshold(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="performanceScoreThreshold")
    def performance_score_threshold(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @performance_score_threshold.setter
    def performance_score_threshold(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class InternetMonitorInternetMeasurementsLogDeliveryArgsDict(TypedDict):
    s3_config: NotRequired[
        pulumi.Input[InternetMonitorInternetMeasurementsLogDeliveryS3ConfigArgsDict]
    ]

@pulumi.input_type
class InternetMonitorInternetMeasurementsLogDeliveryArgs:
    def __init__(
        __self__,
        *,
        s3_config: Optional[
            pulumi.Input[InternetMonitorInternetMeasurementsLogDeliveryS3ConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Config")
    def s3_config(
        self,
    ) -> Optional[
        pulumi.Input[InternetMonitorInternetMeasurementsLogDeliveryS3ConfigArgs]
    ]: ...
    @s3_config.setter
    def s3_config(
        self,
        value: Optional[
            pulumi.Input[InternetMonitorInternetMeasurementsLogDeliveryS3ConfigArgs]
        ],
    ): ...

class InternetMonitorInternetMeasurementsLogDeliveryS3ConfigArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    log_delivery_status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InternetMonitorInternetMeasurementsLogDeliveryS3ConfigArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logDeliveryStatus")
    def log_delivery_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_delivery_status.setter
    def log_delivery_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogDeliveryDestinationDeliveryDestinationConfigurationArgsDict(TypedDict):
    destination_resource_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogDeliveryDestinationDeliveryDestinationConfigurationArgs:
    def __init__(
        __self__,
        *,
        destination_resource_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationResourceArn")
    def destination_resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_resource_arn.setter
    def destination_resource_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class LogDeliveryS3DeliveryConfigurationArgsDict(TypedDict):
    enable_hive_compatible_path: pulumi.Input[_builtins.bool]
    suffix_path: pulumi.Input[_builtins.str]

@pulumi.input_type
class LogDeliveryS3DeliveryConfigurationArgs:
    def __init__(
        __self__,
        *,
        enable_hive_compatible_path: pulumi.Input[_builtins.bool],
        suffix_path: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableHiveCompatiblePath")
    def enable_hive_compatible_path(self) -> pulumi.Input[_builtins.bool]: ...
    @enable_hive_compatible_path.setter
    def enable_hive_compatible_path(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="suffixPath")
    def suffix_path(self) -> pulumi.Input[_builtins.str]: ...
    @suffix_path.setter
    def suffix_path(self, value: pulumi.Input[_builtins.str]): ...

class LogMetricFilterMetricTransformationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    default_value: NotRequired[pulumi.Input[_builtins.str]]
    dimensions: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogMetricFilterMetricTransformationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        default_value: Optional[pulumi.Input[_builtins.str]] = ...,
        dimensions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigArgsDict(TypedDict):
    add_keys: NotRequired[pulumi.Input[LogTransformerTransformerConfigAddKeysArgsDict]]
    copy_value: NotRequired[
        pulumi.Input[LogTransformerTransformerConfigCopyValueArgsDict]
    ]
    csvs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LogTransformerTransformerConfigCsvArgsDict]]]
    ]
    date_time_converters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[LogTransformerTransformerConfigDateTimeConverterArgsDict]
            ]
        ]
    ]
    delete_keys: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigDeleteKeyArgsDict]]
        ]
    ]
    grok: NotRequired[pulumi.Input[LogTransformerTransformerConfigGrokArgsDict]]
    list_to_maps: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigListToMapArgsDict]]
        ]
    ]
    lower_case_strings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[LogTransformerTransformerConfigLowerCaseStringArgsDict]
            ]
        ]
    ]
    move_keys: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigMoveKeyArgsDict]]
        ]
    ]
    parse_cloudfront: NotRequired[
        pulumi.Input[LogTransformerTransformerConfigParseCloudfrontArgsDict]
    ]
    parse_jsons: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigParseJsonArgsDict]]
        ]
    ]
    parse_key_values: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigParseKeyValueArgsDict]]
        ]
    ]
    parse_postgres: NotRequired[
        pulumi.Input[LogTransformerTransformerConfigParsePostgresArgsDict]
    ]
    parse_route53: NotRequired[
        pulumi.Input[LogTransformerTransformerConfigParseRoute53ArgsDict]
    ]
    parse_to_ocsf: NotRequired[
        pulumi.Input[LogTransformerTransformerConfigParseToOcsfArgsDict]
    ]
    parse_vpc: NotRequired[
        pulumi.Input[LogTransformerTransformerConfigParseVpcArgsDict]
    ]
    parse_waf: NotRequired[
        pulumi.Input[LogTransformerTransformerConfigParseWafArgsDict]
    ]
    rename_keys: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigRenameKeyArgsDict]]
        ]
    ]
    split_strings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigSplitStringArgsDict]]
        ]
    ]
    substitute_strings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[LogTransformerTransformerConfigSubstituteStringArgsDict]
            ]
        ]
    ]
    trim_strings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigTrimStringArgsDict]]
        ]
    ]
    type_converters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigTypeConverterArgsDict]]
        ]
    ]
    upper_case_strings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[LogTransformerTransformerConfigUpperCaseStringArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class LogTransformerTransformerConfigArgs:
    def __init__(
        __self__,
        *,
        add_keys: Optional[
            pulumi.Input[LogTransformerTransformerConfigAddKeysArgs]
        ] = ...,
        copy_value: Optional[
            pulumi.Input[LogTransformerTransformerConfigCopyValueArgs]
        ] = ...,
        csvs: Optional[
            pulumi.Input[Sequence[pulumi.Input[LogTransformerTransformerConfigCsvArgs]]]
        ] = ...,
        date_time_converters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[LogTransformerTransformerConfigDateTimeConverterArgs]
                ]
            ]
        ] = ...,
        delete_keys: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigDeleteKeyArgs]]
            ]
        ] = ...,
        grok: Optional[pulumi.Input[LogTransformerTransformerConfigGrokArgs]] = ...,
        list_to_maps: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigListToMapArgs]]
            ]
        ] = ...,
        lower_case_strings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[LogTransformerTransformerConfigLowerCaseStringArgs]
                ]
            ]
        ] = ...,
        move_keys: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigMoveKeyArgs]]
            ]
        ] = ...,
        parse_cloudfront: Optional[
            pulumi.Input[LogTransformerTransformerConfigParseCloudfrontArgs]
        ] = ...,
        parse_jsons: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigParseJsonArgs]]
            ]
        ] = ...,
        parse_key_values: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigParseKeyValueArgs]]
            ]
        ] = ...,
        parse_postgres: Optional[
            pulumi.Input[LogTransformerTransformerConfigParsePostgresArgs]
        ] = ...,
        parse_route53: Optional[
            pulumi.Input[LogTransformerTransformerConfigParseRoute53Args]
        ] = ...,
        parse_to_ocsf: Optional[
            pulumi.Input[LogTransformerTransformerConfigParseToOcsfArgs]
        ] = ...,
        parse_vpc: Optional[
            pulumi.Input[LogTransformerTransformerConfigParseVpcArgs]
        ] = ...,
        parse_waf: Optional[
            pulumi.Input[LogTransformerTransformerConfigParseWafArgs]
        ] = ...,
        rename_keys: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigRenameKeyArgs]]
            ]
        ] = ...,
        split_strings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigSplitStringArgs]]
            ]
        ] = ...,
        substitute_strings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[LogTransformerTransformerConfigSubstituteStringArgs]
                ]
            ]
        ] = ...,
        trim_strings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigTrimStringArgs]]
            ]
        ] = ...,
        type_converters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigTypeConverterArgs]]
            ]
        ] = ...,
        upper_case_strings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[LogTransformerTransformerConfigUpperCaseStringArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addKeys")
    def add_keys(
        self,
    ) -> Optional[pulumi.Input[LogTransformerTransformerConfigAddKeysArgs]]: ...
    @add_keys.setter
    def add_keys(
        self, value: Optional[pulumi.Input[LogTransformerTransformerConfigAddKeysArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="copyValue")
    def copy_value(
        self,
    ) -> Optional[pulumi.Input[LogTransformerTransformerConfigCopyValueArgs]]: ...
    @copy_value.setter
    def copy_value(
        self,
        value: Optional[pulumi.Input[LogTransformerTransformerConfigCopyValueArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def csvs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LogTransformerTransformerConfigCsvArgs]]]
    ]: ...
    @csvs.setter
    def csvs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LogTransformerTransformerConfigCsvArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dateTimeConverters")
    def date_time_converters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigDateTimeConverterArgs]]
        ]
    ]: ...
    @date_time_converters.setter
    def date_time_converters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[LogTransformerTransformerConfigDateTimeConverterArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteKeys")
    def delete_keys(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigDeleteKeyArgs]]
        ]
    ]: ...
    @delete_keys.setter
    def delete_keys(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigDeleteKeyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def grok(
        self,
    ) -> Optional[pulumi.Input[LogTransformerTransformerConfigGrokArgs]]: ...
    @grok.setter
    def grok(
        self, value: Optional[pulumi.Input[LogTransformerTransformerConfigGrokArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="listToMaps")
    def list_to_maps(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigListToMapArgs]]
        ]
    ]: ...
    @list_to_maps.setter
    def list_to_maps(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigListToMapArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lowerCaseStrings")
    def lower_case_strings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigLowerCaseStringArgs]]
        ]
    ]: ...
    @lower_case_strings.setter
    def lower_case_strings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[LogTransformerTransformerConfigLowerCaseStringArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="moveKeys")
    def move_keys(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LogTransformerTransformerConfigMoveKeyArgs]]]
    ]: ...
    @move_keys.setter
    def move_keys(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigMoveKeyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parseCloudfront")
    def parse_cloudfront(
        self,
    ) -> Optional[pulumi.Input[LogTransformerTransformerConfigParseCloudfrontArgs]]: ...
    @parse_cloudfront.setter
    def parse_cloudfront(
        self,
        value: Optional[
            pulumi.Input[LogTransformerTransformerConfigParseCloudfrontArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parseJsons")
    def parse_jsons(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigParseJsonArgs]]
        ]
    ]: ...
    @parse_jsons.setter
    def parse_jsons(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigParseJsonArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parseKeyValues")
    def parse_key_values(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigParseKeyValueArgs]]
        ]
    ]: ...
    @parse_key_values.setter
    def parse_key_values(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigParseKeyValueArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parsePostgres")
    def parse_postgres(
        self,
    ) -> Optional[pulumi.Input[LogTransformerTransformerConfigParsePostgresArgs]]: ...
    @parse_postgres.setter
    def parse_postgres(
        self,
        value: Optional[pulumi.Input[LogTransformerTransformerConfigParsePostgresArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parseRoute53")
    def parse_route53(
        self,
    ) -> Optional[pulumi.Input[LogTransformerTransformerConfigParseRoute53Args]]: ...
    @parse_route53.setter
    def parse_route53(
        self,
        value: Optional[pulumi.Input[LogTransformerTransformerConfigParseRoute53Args]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parseToOcsf")
    def parse_to_ocsf(
        self,
    ) -> Optional[pulumi.Input[LogTransformerTransformerConfigParseToOcsfArgs]]: ...
    @parse_to_ocsf.setter
    def parse_to_ocsf(
        self,
        value: Optional[pulumi.Input[LogTransformerTransformerConfigParseToOcsfArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parseVpc")
    def parse_vpc(
        self,
    ) -> Optional[pulumi.Input[LogTransformerTransformerConfigParseVpcArgs]]: ...
    @parse_vpc.setter
    def parse_vpc(
        self, value: Optional[pulumi.Input[LogTransformerTransformerConfigParseVpcArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="parseWaf")
    def parse_waf(
        self,
    ) -> Optional[pulumi.Input[LogTransformerTransformerConfigParseWafArgs]]: ...
    @parse_waf.setter
    def parse_waf(
        self, value: Optional[pulumi.Input[LogTransformerTransformerConfigParseWafArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="renameKeys")
    def rename_keys(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigRenameKeyArgs]]
        ]
    ]: ...
    @rename_keys.setter
    def rename_keys(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigRenameKeyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="splitStrings")
    def split_strings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigSplitStringArgs]]
        ]
    ]: ...
    @split_strings.setter
    def split_strings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigSplitStringArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="substituteStrings")
    def substitute_strings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigSubstituteStringArgs]]
        ]
    ]: ...
    @substitute_strings.setter
    def substitute_strings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[LogTransformerTransformerConfigSubstituteStringArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="trimStrings")
    def trim_strings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigTrimStringArgs]]
        ]
    ]: ...
    @trim_strings.setter
    def trim_strings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigTrimStringArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="typeConverters")
    def type_converters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigTypeConverterArgs]]
        ]
    ]: ...
    @type_converters.setter
    def type_converters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[LogTransformerTransformerConfigTypeConverterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="upperCaseStrings")
    def upper_case_strings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigUpperCaseStringArgs]]
        ]
    ]: ...
    @upper_case_strings.setter
    def upper_case_strings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[LogTransformerTransformerConfigUpperCaseStringArgs]
                ]
            ]
        ],
    ): ...

class LogTransformerTransformerConfigAddKeysArgsDict(TypedDict):
    entries: pulumi.Input[
        Sequence[pulumi.Input[LogTransformerTransformerConfigAddKeysEntryArgsDict]]
    ]

@pulumi.input_type
class LogTransformerTransformerConfigAddKeysArgs:
    def __init__(
        __self__,
        *,
        entries: pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigAddKeysEntryArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[LogTransformerTransformerConfigAddKeysEntryArgs]]
    ]: ...
    @entries.setter
    def entries(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigAddKeysEntryArgs]]
        ],
    ): ...

class LogTransformerTransformerConfigAddKeysEntryArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    overwrite_if_exists: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class LogTransformerTransformerConfigAddKeysEntryArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        overwrite_if_exists: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="overwriteIfExists")
    def overwrite_if_exists(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @overwrite_if_exists.setter
    def overwrite_if_exists(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class LogTransformerTransformerConfigCopyValueArgsDict(TypedDict):
    entries: pulumi.Input[
        Sequence[pulumi.Input[LogTransformerTransformerConfigCopyValueEntryArgsDict]]
    ]

@pulumi.input_type
class LogTransformerTransformerConfigCopyValueArgs:
    def __init__(
        __self__,
        *,
        entries: pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigCopyValueEntryArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[LogTransformerTransformerConfigCopyValueEntryArgs]]
    ]: ...
    @entries.setter
    def entries(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigCopyValueEntryArgs]]
        ],
    ): ...

class LogTransformerTransformerConfigCopyValueEntryArgsDict(TypedDict):
    source: pulumi.Input[_builtins.str]
    target: pulumi.Input[_builtins.str]
    overwrite_if_exists: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class LogTransformerTransformerConfigCopyValueEntryArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[_builtins.str],
        target: pulumi.Input[_builtins.str],
        overwrite_if_exists: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="overwriteIfExists")
    def overwrite_if_exists(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @overwrite_if_exists.setter
    def overwrite_if_exists(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class LogTransformerTransformerConfigCsvArgsDict(TypedDict):
    columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    delimiter: NotRequired[pulumi.Input[_builtins.str]]
    quote_character: NotRequired[pulumi.Input[_builtins.str]]
    source: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogTransformerTransformerConfigCsvArgs:
    def __init__(
        __self__,
        *,
        columns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        quote_character: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @columns.setter
    def columns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delimiter.setter
    def delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="quoteCharacter")
    def quote_character(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quote_character.setter
    def quote_character(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigDateTimeConverterArgsDict(TypedDict):
    match_patterns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    source: pulumi.Input[_builtins.str]
    target: pulumi.Input[_builtins.str]
    locale: NotRequired[pulumi.Input[_builtins.str]]
    source_timezone: NotRequired[pulumi.Input[_builtins.str]]
    target_format: NotRequired[pulumi.Input[_builtins.str]]
    target_timezone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogTransformerTransformerConfigDateTimeConverterArgs:
    def __init__(
        __self__,
        *,
        match_patterns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        source: pulumi.Input[_builtins.str],
        target: pulumi.Input[_builtins.str],
        locale: Optional[pulumi.Input[_builtins.str]] = ...,
        source_timezone: Optional[pulumi.Input[_builtins.str]] = ...,
        target_format: Optional[pulumi.Input[_builtins.str]] = ...,
        target_timezone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @match_patterns.setter
    def match_patterns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locale.setter
    def locale(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceTimezone")
    def source_timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_timezone.setter
    def source_timezone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetFormat")
    def target_format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_format.setter
    def target_format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetTimezone")
    def target_timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_timezone.setter
    def target_timezone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigDeleteKeyArgsDict(TypedDict):
    with_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class LogTransformerTransformerConfigDeleteKeyArgs:
    def __init__(
        __self__, *, with_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="withKeys")
    def with_keys(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @with_keys.setter
    def with_keys(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class LogTransformerTransformerConfigGrokArgsDict(TypedDict):
    match: pulumi.Input[_builtins.str]
    source: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogTransformerTransformerConfigGrokArgs:
    def __init__(
        __self__,
        *,
        match: pulumi.Input[_builtins.str],
        source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Input[_builtins.str]: ...
    @match.setter
    def match(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigListToMapArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    source: pulumi.Input[_builtins.str]
    flatten: NotRequired[pulumi.Input[_builtins.bool]]
    flattened_element: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    value_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogTransformerTransformerConfigListToMapArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        source: pulumi.Input[_builtins.str],
        flatten: Optional[pulumi.Input[_builtins.bool]] = ...,
        flattened_element: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        value_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def flatten(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @flatten.setter
    def flatten(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="flattenedElement")
    def flattened_element(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flattened_element.setter
    def flattened_element(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="valueKey")
    def value_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value_key.setter
    def value_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigLowerCaseStringArgsDict(TypedDict):
    with_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class LogTransformerTransformerConfigLowerCaseStringArgs:
    def __init__(
        __self__, *, with_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="withKeys")
    def with_keys(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @with_keys.setter
    def with_keys(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class LogTransformerTransformerConfigMoveKeyArgsDict(TypedDict):
    entries: pulumi.Input[
        Sequence[pulumi.Input[LogTransformerTransformerConfigMoveKeyEntryArgsDict]]
    ]

@pulumi.input_type
class LogTransformerTransformerConfigMoveKeyArgs:
    def __init__(
        __self__,
        *,
        entries: pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigMoveKeyEntryArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[LogTransformerTransformerConfigMoveKeyEntryArgs]]
    ]: ...
    @entries.setter
    def entries(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigMoveKeyEntryArgs]]
        ],
    ): ...

class LogTransformerTransformerConfigMoveKeyEntryArgsDict(TypedDict):
    source: pulumi.Input[_builtins.str]
    target: pulumi.Input[_builtins.str]
    overwrite_if_exists: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class LogTransformerTransformerConfigMoveKeyEntryArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[_builtins.str],
        target: pulumi.Input[_builtins.str],
        overwrite_if_exists: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="overwriteIfExists")
    def overwrite_if_exists(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @overwrite_if_exists.setter
    def overwrite_if_exists(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class LogTransformerTransformerConfigParseCloudfrontArgsDict(TypedDict):
    source: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogTransformerTransformerConfigParseCloudfrontArgs:
    def __init__(
        __self__, *, source: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigParseJsonArgsDict(TypedDict):
    destination: NotRequired[pulumi.Input[_builtins.str]]
    source: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogTransformerTransformerConfigParseJsonArgs:
    def __init__(
        __self__,
        *,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigParseKeyValueArgsDict(TypedDict):
    destination: NotRequired[pulumi.Input[_builtins.str]]
    field_delimiter: NotRequired[pulumi.Input[_builtins.str]]
    key_prefix: NotRequired[pulumi.Input[_builtins.str]]
    key_value_delimiter: NotRequired[pulumi.Input[_builtins.str]]
    non_match_value: NotRequired[pulumi.Input[_builtins.str]]
    overwrite_if_exists: NotRequired[pulumi.Input[_builtins.bool]]
    source: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogTransformerTransformerConfigParseKeyValueArgs:
    def __init__(
        __self__,
        *,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        field_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        key_value_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        non_match_value: Optional[pulumi.Input[_builtins.str]] = ...,
        overwrite_if_exists: Optional[pulumi.Input[_builtins.bool]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field_delimiter.setter
    def field_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_prefix.setter
    def key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyValueDelimiter")
    def key_value_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_value_delimiter.setter
    def key_value_delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nonMatchValue")
    def non_match_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @non_match_value.setter
    def non_match_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="overwriteIfExists")
    def overwrite_if_exists(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @overwrite_if_exists.setter
    def overwrite_if_exists(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigParsePostgresArgsDict(TypedDict):
    source: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogTransformerTransformerConfigParsePostgresArgs:
    def __init__(
        __self__, *, source: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigParseRoute53ArgsDict(TypedDict):
    source: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogTransformerTransformerConfigParseRoute53Args:
    def __init__(
        __self__, *, source: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigParseToOcsfArgsDict(TypedDict):
    event_source: pulumi.Input[_builtins.str]
    ocsf_version: pulumi.Input[_builtins.str]
    source: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogTransformerTransformerConfigParseToOcsfArgs:
    def __init__(
        __self__,
        *,
        event_source: pulumi.Input[_builtins.str],
        ocsf_version: pulumi.Input[_builtins.str],
        source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventSource")
    def event_source(self) -> pulumi.Input[_builtins.str]: ...
    @event_source.setter
    def event_source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ocsfVersion")
    def ocsf_version(self) -> pulumi.Input[_builtins.str]: ...
    @ocsf_version.setter
    def ocsf_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigParseVpcArgsDict(TypedDict):
    source: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogTransformerTransformerConfigParseVpcArgs:
    def __init__(
        __self__, *, source: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigParseWafArgsDict(TypedDict):
    source: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogTransformerTransformerConfigParseWafArgs:
    def __init__(
        __self__, *, source: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LogTransformerTransformerConfigRenameKeyArgsDict(TypedDict):
    entries: pulumi.Input[
        Sequence[pulumi.Input[LogTransformerTransformerConfigRenameKeyEntryArgsDict]]
    ]

@pulumi.input_type
class LogTransformerTransformerConfigRenameKeyArgs:
    def __init__(
        __self__,
        *,
        entries: pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigRenameKeyEntryArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[LogTransformerTransformerConfigRenameKeyEntryArgs]]
    ]: ...
    @entries.setter
    def entries(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigRenameKeyEntryArgs]]
        ],
    ): ...

class LogTransformerTransformerConfigRenameKeyEntryArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    rename_to: pulumi.Input[_builtins.str]
    overwrite_if_exists: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class LogTransformerTransformerConfigRenameKeyEntryArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        rename_to: pulumi.Input[_builtins.str],
        overwrite_if_exists: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="renameTo")
    def rename_to(self) -> pulumi.Input[_builtins.str]: ...
    @rename_to.setter
    def rename_to(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="overwriteIfExists")
    def overwrite_if_exists(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @overwrite_if_exists.setter
    def overwrite_if_exists(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class LogTransformerTransformerConfigSplitStringArgsDict(TypedDict):
    entries: pulumi.Input[
        Sequence[pulumi.Input[LogTransformerTransformerConfigSplitStringEntryArgsDict]]
    ]

@pulumi.input_type
class LogTransformerTransformerConfigSplitStringArgs:
    def __init__(
        __self__,
        *,
        entries: pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigSplitStringEntryArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[LogTransformerTransformerConfigSplitStringEntryArgs]]
    ]: ...
    @entries.setter
    def entries(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[LogTransformerTransformerConfigSplitStringEntryArgs]]
        ],
    ): ...

class LogTransformerTransformerConfigSplitStringEntryArgsDict(TypedDict):
    delimiter: pulumi.Input[_builtins.str]
    source: pulumi.Input[_builtins.str]

@pulumi.input_type
class LogTransformerTransformerConfigSplitStringEntryArgs:
    def __init__(
        __self__,
        *,
        delimiter: pulumi.Input[_builtins.str],
        source: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> pulumi.Input[_builtins.str]: ...
    @delimiter.setter
    def delimiter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...

class LogTransformerTransformerConfigSubstituteStringArgsDict(TypedDict):
    entries: pulumi.Input[
        Sequence[
            pulumi.Input[LogTransformerTransformerConfigSubstituteStringEntryArgsDict]
        ]
    ]

@pulumi.input_type
class LogTransformerTransformerConfigSubstituteStringArgs:
    def __init__(
        __self__,
        *,
        entries: pulumi.Input[
            Sequence[
                pulumi.Input[LogTransformerTransformerConfigSubstituteStringEntryArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[LogTransformerTransformerConfigSubstituteStringEntryArgs]]
    ]: ...
    @entries.setter
    def entries(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[LogTransformerTransformerConfigSubstituteStringEntryArgs]
            ]
        ],
    ): ...

class LogTransformerTransformerConfigSubstituteStringEntryArgsDict(TypedDict):
    from_: pulumi.Input[_builtins.str]
    source: pulumi.Input[_builtins.str]
    to: pulumi.Input[_builtins.str]

@pulumi.input_type
class LogTransformerTransformerConfigSubstituteStringEntryArgs:
    def __init__(
        __self__,
        *,
        from_: pulumi.Input[_builtins.str],
        source: pulumi.Input[_builtins.str],
        to: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> pulumi.Input[_builtins.str]: ...
    @from_.setter
    def from_(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> pulumi.Input[_builtins.str]: ...
    @to.setter
    def to(self, value: pulumi.Input[_builtins.str]): ...

class LogTransformerTransformerConfigTrimStringArgsDict(TypedDict):
    with_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class LogTransformerTransformerConfigTrimStringArgs:
    def __init__(
        __self__, *, with_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="withKeys")
    def with_keys(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @with_keys.setter
    def with_keys(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class LogTransformerTransformerConfigTypeConverterArgsDict(TypedDict):
    entries: pulumi.Input[
        Sequence[
            pulumi.Input[LogTransformerTransformerConfigTypeConverterEntryArgsDict]
        ]
    ]

@pulumi.input_type
class LogTransformerTransformerConfigTypeConverterArgs:
    def __init__(
        __self__,
        *,
        entries: pulumi.Input[
            Sequence[
                pulumi.Input[LogTransformerTransformerConfigTypeConverterEntryArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[LogTransformerTransformerConfigTypeConverterEntryArgs]]
    ]: ...
    @entries.setter
    def entries(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[LogTransformerTransformerConfigTypeConverterEntryArgs]
            ]
        ],
    ): ...

class LogTransformerTransformerConfigTypeConverterEntryArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class LogTransformerTransformerConfigTypeConverterEntryArgs:
    def __init__(
        __self__, *, key: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class LogTransformerTransformerConfigUpperCaseStringArgsDict(TypedDict):
    with_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class LogTransformerTransformerConfigUpperCaseStringArgs:
    def __init__(
        __self__, *, with_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="withKeys")
    def with_keys(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @with_keys.setter
    def with_keys(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class MetricAlarmMetricQueryArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    account_id: NotRequired[pulumi.Input[_builtins.str]]
    expression: NotRequired[pulumi.Input[_builtins.str]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    metric: NotRequired[pulumi.Input[MetricAlarmMetricQueryMetricArgsDict]]
    period: NotRequired[pulumi.Input[_builtins.int]]
    return_data: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class MetricAlarmMetricQueryArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        expression: Optional[pulumi.Input[_builtins.str]] = ...,
        label: Optional[pulumi.Input[_builtins.str]] = ...,
        metric: Optional[pulumi.Input[MetricAlarmMetricQueryMetricArgs]] = ...,
        period: Optional[pulumi.Input[_builtins.int]] = ...,
        return_data: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expression.setter
    def expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metric(self) -> Optional[pulumi.Input[MetricAlarmMetricQueryMetricArgs]]: ...
    @metric.setter
    def metric(
        self, value: Optional[pulumi.Input[MetricAlarmMetricQueryMetricArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period.setter
    def period(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @return_data.setter
    def return_data(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class MetricAlarmMetricQueryMetricArgsDict(TypedDict):
    metric_name: pulumi.Input[_builtins.str]
    period: pulumi.Input[_builtins.int]
    stat: pulumi.Input[_builtins.str]
    dimensions: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    unit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MetricAlarmMetricQueryMetricArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        period: pulumi.Input[_builtins.int],
        stat: pulumi.Input[_builtins.str],
        dimensions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> pulumi.Input[_builtins.int]: ...
    @period.setter
    def period(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def stat(self) -> pulumi.Input[_builtins.str]: ...
    @stat.setter
    def stat(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MetricStreamExcludeFilterArgsDict(TypedDict):
    namespace: pulumi.Input[_builtins.str]
    metric_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class MetricStreamExcludeFilterArgs:
    def __init__(
        __self__,
        *,
        namespace: pulumi.Input[_builtins.str],
        metric_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricNames")
    def metric_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @metric_names.setter
    def metric_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class MetricStreamIncludeFilterArgsDict(TypedDict):
    namespace: pulumi.Input[_builtins.str]
    metric_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class MetricStreamIncludeFilterArgs:
    def __init__(
        __self__,
        *,
        namespace: pulumi.Input[_builtins.str],
        metric_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricNames")
    def metric_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @metric_names.setter
    def metric_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class MetricStreamStatisticsConfigurationArgsDict(TypedDict):
    additional_statistics: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    include_metrics: pulumi.Input[
        Sequence[pulumi.Input[MetricStreamStatisticsConfigurationIncludeMetricArgsDict]]
    ]

@pulumi.input_type
class MetricStreamStatisticsConfigurationArgs:
    def __init__(
        __self__,
        *,
        additional_statistics: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        include_metrics: pulumi.Input[
            Sequence[pulumi.Input[MetricStreamStatisticsConfigurationIncludeMetricArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalStatistics")
    def additional_statistics(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @additional_statistics.setter
    def additional_statistics(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeMetrics")
    def include_metrics(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[MetricStreamStatisticsConfigurationIncludeMetricArgs]]
    ]: ...
    @include_metrics.setter
    def include_metrics(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[MetricStreamStatisticsConfigurationIncludeMetricArgs]]
        ],
    ): ...

class MetricStreamStatisticsConfigurationIncludeMetricArgsDict(TypedDict):
    metric_name: pulumi.Input[_builtins.str]
    namespace: pulumi.Input[_builtins.str]

@pulumi.input_type
class MetricStreamStatisticsConfigurationIncludeMetricArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        namespace: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...

class PolicyDocumentArgsDict(TypedDict):
    statement: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgsDict]]]
    version: pulumi.Input[iam.PolicyDocumentVersion]
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyDocumentArgs:
    def __init__(
        __self__,
        *,
        statement: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]],
        version: pulumi.Input[iam.PolicyDocumentVersion],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="Statement")
    def statement(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]]: ...
    @statement.setter
    def statement(
        self, value: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="Version")
    def version(self) -> pulumi.Input[iam.PolicyDocumentVersion]: ...
    @version.setter
    def version(self, value: pulumi.Input[iam.PolicyDocumentVersion]): ...
    @_builtins.property
    @pulumi.getter(name="Id")
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GetLogDataProtectionPolicyDocumentConfigurationArgsDict(TypedDict):
    custom_data_identifiers: NotRequired[
        Sequence[
            GetLogDataProtectionPolicyDocumentConfigurationCustomDataIdentifierArgsDict
        ]
    ]

@pulumi.input_type
class GetLogDataProtectionPolicyDocumentConfigurationArgs:
    def __init__(
        __self__,
        *,
        custom_data_identifiers: Optional[
            Sequence[
                GetLogDataProtectionPolicyDocumentConfigurationCustomDataIdentifierArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customDataIdentifiers")
    def custom_data_identifiers(
        self,
    ) -> Optional[
        Sequence[
            GetLogDataProtectionPolicyDocumentConfigurationCustomDataIdentifierArgs
        ]
    ]: ...
    @custom_data_identifiers.setter
    def custom_data_identifiers(
        self,
        value: Optional[
            Sequence[
                GetLogDataProtectionPolicyDocumentConfigurationCustomDataIdentifierArgs
            ]
        ],
    ): ...

class GetLogDataProtectionPolicyDocumentConfigurationCustomDataIdentifierArgsDict(
    TypedDict
):
    name: _builtins.str
    regex: _builtins.str

@pulumi.input_type
class GetLogDataProtectionPolicyDocumentConfigurationCustomDataIdentifierArgs:
    def __init__(__self__, *, name: _builtins.str, regex: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...
    @regex.setter
    def regex(self, value: _builtins.str): ...

class GetLogDataProtectionPolicyDocumentStatementArgsDict(TypedDict):
    data_identifiers: Sequence[_builtins.str]
    operation: GetLogDataProtectionPolicyDocumentStatementOperationArgsDict
    sid: NotRequired[_builtins.str]

@pulumi.input_type
class GetLogDataProtectionPolicyDocumentStatementArgs:
    def __init__(
        __self__,
        *,
        data_identifiers: Sequence[_builtins.str],
        operation: GetLogDataProtectionPolicyDocumentStatementOperationArgs,
        sid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataIdentifiers")
    def data_identifiers(self) -> Sequence[_builtins.str]: ...
    @data_identifiers.setter
    def data_identifiers(self, value: Sequence[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> GetLogDataProtectionPolicyDocumentStatementOperationArgs: ...
    @operation.setter
    def operation(
        self, value: GetLogDataProtectionPolicyDocumentStatementOperationArgs
    ): ...
    @_builtins.property
    @pulumi.getter
    def sid(self) -> Optional[_builtins.str]: ...
    @sid.setter
    def sid(self, value: Optional[_builtins.str]): ...

class GetLogDataProtectionPolicyDocumentStatementOperationArgsDict(TypedDict):
    audit: NotRequired[
        GetLogDataProtectionPolicyDocumentStatementOperationAuditArgsDict
    ]
    deidentify: NotRequired[
        GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyArgsDict
    ]

@pulumi.input_type
class GetLogDataProtectionPolicyDocumentStatementOperationArgs:
    def __init__(
        __self__,
        *,
        audit: Optional[
            GetLogDataProtectionPolicyDocumentStatementOperationAuditArgs
        ] = ...,
        deidentify: Optional[
            GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyArgs
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audit(
        self,
    ) -> Optional[GetLogDataProtectionPolicyDocumentStatementOperationAuditArgs]: ...
    @audit.setter
    def audit(
        self,
        value: Optional[GetLogDataProtectionPolicyDocumentStatementOperationAuditArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def deidentify(
        self,
    ) -> Optional[
        GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyArgs
    ]: ...
    @deidentify.setter
    def deidentify(
        self,
        value: Optional[
            GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyArgs
        ],
    ): ...

class GetLogDataProtectionPolicyDocumentStatementOperationAuditArgsDict(TypedDict):
    findings_destination: GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationArgsDict

@pulumi.input_type
class GetLogDataProtectionPolicyDocumentStatementOperationAuditArgs:
    def __init__(
        __self__,
        *,
        findings_destination: GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationArgs,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="findingsDestination")
    def findings_destination(
        self,
    ) -> (
        GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationArgs
    ): ...
    @findings_destination.setter
    def findings_destination(
        self,
        value: GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationArgs,
    ): ...

class GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationArgsDict(
    TypedDict
):
    cloudwatch_logs: NotRequired[
        GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationCloudwatchLogsArgsDict
    ]
    firehose: NotRequired[
        GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationFirehoseArgsDict
    ]
    s3: NotRequired[
        GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationS3ArgsDict
    ]

@pulumi.input_type
class GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_logs: Optional[
            GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationCloudwatchLogsArgs
        ] = ...,
        firehose: Optional[
            GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationFirehoseArgs
        ] = ...,
        s3: Optional[
            GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationS3Args
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> Optional[
        GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationCloudwatchLogsArgs
    ]: ...
    @cloudwatch_logs.setter
    def cloudwatch_logs(
        self,
        value: Optional[
            GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationCloudwatchLogsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def firehose(
        self,
    ) -> Optional[
        GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationFirehoseArgs
    ]: ...
    @firehose.setter
    def firehose(
        self,
        value: Optional[
            GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationFirehoseArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationS3Args
    ]: ...
    @s3.setter
    def s3(
        self,
        value: Optional[
            GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationS3Args
        ],
    ): ...

class GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationCloudwatchLogsArgsDict(
    TypedDict
):
    log_group: _builtins.str

@pulumi.input_type
class GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationCloudwatchLogsArgs:
    def __init__(__self__, *, log_group: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> _builtins.str: ...
    @log_group.setter
    def log_group(self, value: _builtins.str): ...

class GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationFirehoseArgsDict(
    TypedDict
):
    delivery_stream: _builtins.str

@pulumi.input_type
class GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationFirehoseArgs:
    def __init__(__self__, *, delivery_stream: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryStream")
    def delivery_stream(self) -> _builtins.str: ...
    @delivery_stream.setter
    def delivery_stream(self, value: _builtins.str): ...

class GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationS3ArgsDict(
    TypedDict
):
    bucket: _builtins.str

@pulumi.input_type
class GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationS3Args:
    def __init__(__self__, *, bucket: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @bucket.setter
    def bucket(self, value: _builtins.str): ...

class GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyArgsDict(TypedDict):
    mask_config: (
        GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyMaskConfigArgsDict
    )

@pulumi.input_type
class GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyArgs:
    def __init__(
        __self__,
        *,
        mask_config: GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyMaskConfigArgs,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maskConfig")
    def mask_config(
        self,
    ) -> (
        GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyMaskConfigArgs
    ): ...
    @mask_config.setter
    def mask_config(
        self,
        value: GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyMaskConfigArgs,
    ): ...

class GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyMaskConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyMaskConfigArgs:
    def __init__(__self__) -> None: ...
