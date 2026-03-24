import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CompositeAlarmActionsSuppressor",
    "EventBusDeadLetterConfig",
    "EventBusLogConfig",
    "EventConnectionAuthParameters",
    "EventConnectionAuthParametersApiKey",
    "EventConnectionAuthParametersBasic",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "EventConnectionAuthParametersOauth",
    "EventConnectionAuthParametersOauthClientParameters",
    ...,
    ...,
    ...,
    ...,
    "EventConnectionInvocationConnectivityParameters",
    ...,
    "EventEndpointEventBus",
    "EventEndpointReplicationConfig",
    "EventEndpointRoutingConfig",
    "EventEndpointRoutingConfigFailoverConfig",
    "EventEndpointRoutingConfigFailoverConfigPrimary",
    "EventEndpointRoutingConfigFailoverConfigSecondary",
    "EventPermissionCondition",
    "EventTargetAppsyncTarget",
    "EventTargetBatchTarget",
    "EventTargetDeadLetterConfig",
    "EventTargetEcsTarget",
    "EventTargetEcsTargetCapacityProviderStrategy",
    "EventTargetEcsTargetNetworkConfiguration",
    "EventTargetEcsTargetOrderedPlacementStrategy",
    "EventTargetEcsTargetPlacementConstraint",
    "EventTargetHttpTarget",
    "EventTargetInputTransformer",
    "EventTargetKinesisTarget",
    "EventTargetRedshiftTarget",
    "EventTargetRetryPolicy",
    "EventTargetRunCommandTarget",
    "EventTargetSagemakerPipelineTarget",
    ...,
    "EventTargetSqsTarget",
    "InternetMonitorHealthEventsConfig",
    "InternetMonitorInternetMeasurementsLogDelivery",
    ...,
    ...,
    "LogDeliveryS3DeliveryConfiguration",
    "LogMetricFilterMetricTransformation",
    "LogTransformerTransformerConfig",
    "LogTransformerTransformerConfigAddKeys",
    "LogTransformerTransformerConfigAddKeysEntry",
    "LogTransformerTransformerConfigCopyValue",
    "LogTransformerTransformerConfigCopyValueEntry",
    "LogTransformerTransformerConfigCsv",
    "LogTransformerTransformerConfigDateTimeConverter",
    "LogTransformerTransformerConfigDeleteKey",
    "LogTransformerTransformerConfigGrok",
    "LogTransformerTransformerConfigListToMap",
    "LogTransformerTransformerConfigLowerCaseString",
    "LogTransformerTransformerConfigMoveKey",
    "LogTransformerTransformerConfigMoveKeyEntry",
    "LogTransformerTransformerConfigParseCloudfront",
    "LogTransformerTransformerConfigParseJson",
    "LogTransformerTransformerConfigParseKeyValue",
    "LogTransformerTransformerConfigParsePostgres",
    "LogTransformerTransformerConfigParseRoute53",
    "LogTransformerTransformerConfigParseToOcsf",
    "LogTransformerTransformerConfigParseVpc",
    "LogTransformerTransformerConfigParseWaf",
    "LogTransformerTransformerConfigRenameKey",
    "LogTransformerTransformerConfigRenameKeyEntry",
    "LogTransformerTransformerConfigSplitString",
    "LogTransformerTransformerConfigSplitStringEntry",
    "LogTransformerTransformerConfigSubstituteString",
    ...,
    "LogTransformerTransformerConfigTrimString",
    "LogTransformerTransformerConfigTypeConverter",
    "LogTransformerTransformerConfigTypeConverterEntry",
    "LogTransformerTransformerConfigUpperCaseString",
    "MetricAlarmMetricQuery",
    "MetricAlarmMetricQueryMetric",
    "MetricStreamExcludeFilter",
    "MetricStreamIncludeFilter",
    "MetricStreamStatisticsConfiguration",
    "MetricStreamStatisticsConfigurationIncludeMetric",
    "GetContributorManagedInsightRulesManagedRuleResult",
    ...,
    "GetEventBusDeadLetterConfigResult",
    "GetEventBusLogConfigResult",
    "GetEventBusesEventBusResult",
    ...,
    ...,
    "GetLogDataProtectionPolicyDocumentStatementResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

@pulumi.output_type
class CompositeAlarmActionsSuppressor(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        alarm: _builtins.str,
        extension_period: _builtins.int,
        wait_period: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alarm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extensionPeriod")
    def extension_period(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="waitPeriod")
    def wait_period(self) -> _builtins.int: ...

@pulumi.output_type
class EventBusDeadLetterConfig(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventBusLogConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        include_detail: Optional[_builtins.str] = ...,
        level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeDetail")
    def include_detail(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventConnectionAuthParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_key: Optional[outputs.EventConnectionAuthParametersApiKey] = ...,
        basic: Optional[outputs.EventConnectionAuthParametersBasic] = ...,
        connectivity_parameters: Optional[
            outputs.EventConnectionAuthParametersConnectivityParameters
        ] = ...,
        invocation_http_parameters: Optional[
            outputs.EventConnectionAuthParametersInvocationHttpParameters
        ] = ...,
        oauth: Optional[outputs.EventConnectionAuthParametersOauth] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[outputs.EventConnectionAuthParametersApiKey]: ...
    @_builtins.property
    @pulumi.getter
    def basic(self) -> Optional[outputs.EventConnectionAuthParametersBasic]: ...
    @_builtins.property
    @pulumi.getter(name="connectivityParameters")
    def connectivity_parameters(
        self,
    ) -> Optional[outputs.EventConnectionAuthParametersConnectivityParameters]: ...
    @_builtins.property
    @pulumi.getter(name="invocationHttpParameters")
    def invocation_http_parameters(
        self,
    ) -> Optional[outputs.EventConnectionAuthParametersInvocationHttpParameters]: ...
    @_builtins.property
    @pulumi.getter
    def oauth(self) -> Optional[outputs.EventConnectionAuthParametersOauth]: ...

@pulumi.output_type
class EventConnectionAuthParametersApiKey(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class EventConnectionAuthParametersBasic(dict):
    def __init__(
        __self__, *, password: _builtins.str, username: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class EventConnectionAuthParametersConnectivityParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_parameters: outputs.EventConnectionAuthParametersConnectivityParametersResourceParameters,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceParameters")
    def resource_parameters(
        self,
    ) -> (
        outputs.EventConnectionAuthParametersConnectivityParametersResourceParameters
    ): ...

@pulumi.output_type
class EventConnectionAuthParametersConnectivityParametersResourceParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_configuration_arn: _builtins.str,
        resource_association_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationArn")
    def resource_configuration_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceAssociationArn")
    def resource_association_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventConnectionAuthParametersInvocationHttpParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bodies: Optional[
            Sequence[outputs.EventConnectionAuthParametersInvocationHttpParametersBody]
        ] = ...,
        headers: Optional[
            Sequence[
                outputs.EventConnectionAuthParametersInvocationHttpParametersHeader
            ]
        ] = ...,
        query_strings: Optional[
            Sequence[
                outputs.EventConnectionAuthParametersInvocationHttpParametersQueryString
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bodies(
        self,
    ) -> Optional[
        Sequence[outputs.EventConnectionAuthParametersInvocationHttpParametersBody]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        Sequence[outputs.EventConnectionAuthParametersInvocationHttpParametersHeader]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(
        self,
    ) -> Optional[
        Sequence[
            outputs.EventConnectionAuthParametersInvocationHttpParametersQueryString
        ]
    ]: ...

@pulumi.output_type
class EventConnectionAuthParametersInvocationHttpParametersBody(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_value_secret: Optional[_builtins.bool] = ...,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isValueSecret")
    def is_value_secret(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventConnectionAuthParametersInvocationHttpParametersHeader(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_value_secret: Optional[_builtins.bool] = ...,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isValueSecret")
    def is_value_secret(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventConnectionAuthParametersInvocationHttpParametersQueryString(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_value_secret: Optional[_builtins.bool] = ...,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isValueSecret")
    def is_value_secret(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventConnectionAuthParametersOauth(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_endpoint: _builtins.str,
        http_method: _builtins.str,
        oauth_http_parameters: outputs.EventConnectionAuthParametersOauthOauthHttpParameters,
        client_parameters: Optional[
            outputs.EventConnectionAuthParametersOauthClientParameters
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oauthHttpParameters")
    def oauth_http_parameters(
        self,
    ) -> outputs.EventConnectionAuthParametersOauthOauthHttpParameters: ...
    @_builtins.property
    @pulumi.getter(name="clientParameters")
    def client_parameters(
        self,
    ) -> Optional[outputs.EventConnectionAuthParametersOauthClientParameters]: ...

@pulumi.output_type
class EventConnectionAuthParametersOauthClientParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, client_secret: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str: ...

@pulumi.output_type
class EventConnectionAuthParametersOauthOauthHttpParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bodies: Optional[
            Sequence[outputs.EventConnectionAuthParametersOauthOauthHttpParametersBody]
        ] = ...,
        headers: Optional[
            Sequence[
                outputs.EventConnectionAuthParametersOauthOauthHttpParametersHeader
            ]
        ] = ...,
        query_strings: Optional[
            Sequence[
                outputs.EventConnectionAuthParametersOauthOauthHttpParametersQueryString
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bodies(
        self,
    ) -> Optional[
        Sequence[outputs.EventConnectionAuthParametersOauthOauthHttpParametersBody]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        Sequence[outputs.EventConnectionAuthParametersOauthOauthHttpParametersHeader]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(
        self,
    ) -> Optional[
        Sequence[
            outputs.EventConnectionAuthParametersOauthOauthHttpParametersQueryString
        ]
    ]: ...

@pulumi.output_type
class EventConnectionAuthParametersOauthOauthHttpParametersBody(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_value_secret: Optional[_builtins.bool] = ...,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isValueSecret")
    def is_value_secret(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventConnectionAuthParametersOauthOauthHttpParametersHeader(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_value_secret: Optional[_builtins.bool] = ...,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isValueSecret")
    def is_value_secret(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventConnectionAuthParametersOauthOauthHttpParametersQueryString(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_value_secret: Optional[_builtins.bool] = ...,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isValueSecret")
    def is_value_secret(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventConnectionInvocationConnectivityParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_parameters: outputs.EventConnectionInvocationConnectivityParametersResourceParameters,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceParameters")
    def resource_parameters(
        self,
    ) -> outputs.EventConnectionInvocationConnectivityParametersResourceParameters: ...

@pulumi.output_type
class EventConnectionInvocationConnectivityParametersResourceParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_configuration_arn: _builtins.str,
        resource_association_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationArn")
    def resource_configuration_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceAssociationArn")
    def resource_association_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventEndpointEventBus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, event_bus_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventBusArn")
    def event_bus_arn(self) -> _builtins.str: ...

@pulumi.output_type
class EventEndpointReplicationConfig(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventEndpointRoutingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, failover_config: outputs.EventEndpointRoutingConfigFailoverConfig
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failoverConfig")
    def failover_config(self) -> outputs.EventEndpointRoutingConfigFailoverConfig: ...

@pulumi.output_type
class EventEndpointRoutingConfigFailoverConfig(dict):
    def __init__(
        __self__,
        *,
        primary: outputs.EventEndpointRoutingConfigFailoverConfigPrimary,
        secondary: outputs.EventEndpointRoutingConfigFailoverConfigSecondary,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def primary(self) -> outputs.EventEndpointRoutingConfigFailoverConfigPrimary: ...
    @_builtins.property
    @pulumi.getter
    def secondary(
        self,
    ) -> outputs.EventEndpointRoutingConfigFailoverConfigSecondary: ...

@pulumi.output_type
class EventEndpointRoutingConfigFailoverConfigPrimary(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, health_check: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventEndpointRoutingConfigFailoverConfigSecondary(dict):
    def __init__(__self__, *, route: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def route(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventPermissionCondition(dict):
    def __init__(
        __self__, *, key: _builtins.str, type: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class EventTargetAppsyncTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, graphql_operation: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="graphqlOperation")
    def graphql_operation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventTargetBatchTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        job_definition: _builtins.str,
        job_name: _builtins.str,
        array_size: Optional[_builtins.int] = ...,
        job_attempts: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobDefinition")
    def job_definition(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="arraySize")
    def array_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="jobAttempts")
    def job_attempts(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EventTargetDeadLetterConfig(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventTargetEcsTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        task_definition_arn: _builtins.str,
        capacity_provider_strategies: Optional[
            Sequence[outputs.EventTargetEcsTargetCapacityProviderStrategy]
        ] = ...,
        enable_ecs_managed_tags: Optional[_builtins.bool] = ...,
        enable_execute_command: Optional[_builtins.bool] = ...,
        group: Optional[_builtins.str] = ...,
        launch_type: Optional[_builtins.str] = ...,
        network_configuration: Optional[
            outputs.EventTargetEcsTargetNetworkConfiguration
        ] = ...,
        ordered_placement_strategies: Optional[
            Sequence[outputs.EventTargetEcsTargetOrderedPlacementStrategy]
        ] = ...,
        placement_constraints: Optional[
            Sequence[outputs.EventTargetEcsTargetPlacementConstraint]
        ] = ...,
        platform_version: Optional[_builtins.str] = ...,
        propagate_tags: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        task_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskDefinitionArn")
    def task_definition_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(
        self,
    ) -> Optional[Sequence[outputs.EventTargetEcsTargetCapacityProviderStrategy]]: ...
    @_builtins.property
    @pulumi.getter(name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableExecuteCommand")
    def enable_execute_command(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[outputs.EventTargetEcsTargetNetworkConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="orderedPlacementStrategies")
    def ordered_placement_strategies(
        self,
    ) -> Optional[Sequence[outputs.EventTargetEcsTargetOrderedPlacementStrategy]]: ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(
        self,
    ) -> Optional[Sequence[outputs.EventTargetEcsTargetPlacementConstraint]]: ...
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="taskCount")
    def task_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EventTargetEcsTargetCapacityProviderStrategy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_provider: _builtins.str,
        base: Optional[_builtins.int] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProvider")
    def capacity_provider(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def base(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EventTargetEcsTargetNetworkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subnets: Sequence[_builtins.str],
        assign_public_ip: Optional[_builtins.bool] = ...,
        security_groups: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EventTargetEcsTargetOrderedPlacementStrategy(dict):
    def __init__(
        __self__, *, type: _builtins.str, field: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventTargetEcsTargetPlacementConstraint(dict):
    def __init__(
        __self__, *, type: _builtins.str, expression: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventTargetHttpTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        header_parameters: Optional[Mapping[str, _builtins.str]] = ...,
        path_parameter_values: Optional[Sequence[_builtins.str]] = ...,
        query_string_parameters: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerParameters")
    def header_parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pathParameterValues")
    def path_parameter_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="queryStringParameters")
    def query_string_parameters(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class EventTargetInputTransformer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input_template: _builtins.str,
        input_paths: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputTemplate")
    def input_template(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputPaths")
    def input_paths(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class EventTargetKinesisTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, partition_key_path: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionKeyPath")
    def partition_key_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventTargetRedshiftTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database: _builtins.str,
        db_user: Optional[_builtins.str] = ...,
        secrets_manager_arn: Optional[_builtins.str] = ...,
        sql: Optional[_builtins.str] = ...,
        statement_name: Optional[_builtins.str] = ...,
        with_event: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbUser")
    def db_user(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretsManagerArn")
    def secrets_manager_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sql(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statementName")
    def statement_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="withEvent")
    def with_event(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class EventTargetRetryPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maximum_event_age_in_seconds: Optional[_builtins.int] = ...,
        maximum_retry_attempts: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EventTargetRunCommandTarget(dict):
    def __init__(
        __self__, *, key: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class EventTargetSagemakerPipelineTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pipeline_parameter_lists: Optional[
            Sequence[outputs.EventTargetSagemakerPipelineTargetPipelineParameterList]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pipelineParameterLists")
    def pipeline_parameter_lists(
        self,
    ) -> Optional[
        Sequence[outputs.EventTargetSagemakerPipelineTargetPipelineParameterList]
    ]: ...

@pulumi.output_type
class EventTargetSagemakerPipelineTargetPipelineParameterList(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class EventTargetSqsTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, message_group_id: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageGroupId")
    def message_group_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InternetMonitorHealthEventsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_score_threshold: Optional[_builtins.float] = ...,
        performance_score_threshold: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityScoreThreshold")
    def availability_score_threshold(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="performanceScoreThreshold")
    def performance_score_threshold(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class InternetMonitorInternetMeasurementsLogDelivery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_config: Optional[
            outputs.InternetMonitorInternetMeasurementsLogDeliveryS3Config
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Config")
    def s3_config(
        self,
    ) -> Optional[outputs.InternetMonitorInternetMeasurementsLogDeliveryS3Config]: ...

@pulumi.output_type
class InternetMonitorInternetMeasurementsLogDeliveryS3Config(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        bucket_prefix: Optional[_builtins.str] = ...,
        log_delivery_status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logDeliveryStatus")
    def log_delivery_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogDeliveryDestinationDeliveryDestinationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, destination_resource_arn: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationResourceArn")
    def destination_resource_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogDeliveryS3DeliveryConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_hive_compatible_path: _builtins.bool,
        suffix_path: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableHiveCompatiblePath")
    def enable_hive_compatible_path(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="suffixPath")
    def suffix_path(self) -> _builtins.str: ...

@pulumi.output_type
class LogMetricFilterMetricTransformation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        namespace: _builtins.str,
        value: _builtins.str,
        default_value: Optional[_builtins.str] = ...,
        dimensions: Optional[Mapping[str, _builtins.str]] = ...,
        unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        add_keys: Optional[outputs.LogTransformerTransformerConfigAddKeys] = ...,
        copy_value: Optional[outputs.LogTransformerTransformerConfigCopyValue] = ...,
        csvs: Optional[Sequence[outputs.LogTransformerTransformerConfigCsv]] = ...,
        date_time_converters: Optional[
            Sequence[outputs.LogTransformerTransformerConfigDateTimeConverter]
        ] = ...,
        delete_keys: Optional[
            Sequence[outputs.LogTransformerTransformerConfigDeleteKey]
        ] = ...,
        grok: Optional[outputs.LogTransformerTransformerConfigGrok] = ...,
        list_to_maps: Optional[
            Sequence[outputs.LogTransformerTransformerConfigListToMap]
        ] = ...,
        lower_case_strings: Optional[
            Sequence[outputs.LogTransformerTransformerConfigLowerCaseString]
        ] = ...,
        move_keys: Optional[
            Sequence[outputs.LogTransformerTransformerConfigMoveKey]
        ] = ...,
        parse_cloudfront: Optional[
            outputs.LogTransformerTransformerConfigParseCloudfront
        ] = ...,
        parse_jsons: Optional[
            Sequence[outputs.LogTransformerTransformerConfigParseJson]
        ] = ...,
        parse_key_values: Optional[
            Sequence[outputs.LogTransformerTransformerConfigParseKeyValue]
        ] = ...,
        parse_postgres: Optional[
            outputs.LogTransformerTransformerConfigParsePostgres
        ] = ...,
        parse_route53: Optional[
            outputs.LogTransformerTransformerConfigParseRoute53
        ] = ...,
        parse_to_ocsf: Optional[
            outputs.LogTransformerTransformerConfigParseToOcsf
        ] = ...,
        parse_vpc: Optional[outputs.LogTransformerTransformerConfigParseVpc] = ...,
        parse_waf: Optional[outputs.LogTransformerTransformerConfigParseWaf] = ...,
        rename_keys: Optional[
            Sequence[outputs.LogTransformerTransformerConfigRenameKey]
        ] = ...,
        split_strings: Optional[
            Sequence[outputs.LogTransformerTransformerConfigSplitString]
        ] = ...,
        substitute_strings: Optional[
            Sequence[outputs.LogTransformerTransformerConfigSubstituteString]
        ] = ...,
        trim_strings: Optional[
            Sequence[outputs.LogTransformerTransformerConfigTrimString]
        ] = ...,
        type_converters: Optional[
            Sequence[outputs.LogTransformerTransformerConfigTypeConverter]
        ] = ...,
        upper_case_strings: Optional[
            Sequence[outputs.LogTransformerTransformerConfigUpperCaseString]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addKeys")
    def add_keys(self) -> Optional[outputs.LogTransformerTransformerConfigAddKeys]: ...
    @_builtins.property
    @pulumi.getter(name="copyValue")
    def copy_value(
        self,
    ) -> Optional[outputs.LogTransformerTransformerConfigCopyValue]: ...
    @_builtins.property
    @pulumi.getter
    def csvs(
        self,
    ) -> Optional[Sequence[outputs.LogTransformerTransformerConfigCsv]]: ...
    @_builtins.property
    @pulumi.getter(name="dateTimeConverters")
    def date_time_converters(
        self,
    ) -> Optional[
        Sequence[outputs.LogTransformerTransformerConfigDateTimeConverter]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="deleteKeys")
    def delete_keys(
        self,
    ) -> Optional[Sequence[outputs.LogTransformerTransformerConfigDeleteKey]]: ...
    @_builtins.property
    @pulumi.getter
    def grok(self) -> Optional[outputs.LogTransformerTransformerConfigGrok]: ...
    @_builtins.property
    @pulumi.getter(name="listToMaps")
    def list_to_maps(
        self,
    ) -> Optional[Sequence[outputs.LogTransformerTransformerConfigListToMap]]: ...
    @_builtins.property
    @pulumi.getter(name="lowerCaseStrings")
    def lower_case_strings(
        self,
    ) -> Optional[Sequence[outputs.LogTransformerTransformerConfigLowerCaseString]]: ...
    @_builtins.property
    @pulumi.getter(name="moveKeys")
    def move_keys(
        self,
    ) -> Optional[Sequence[outputs.LogTransformerTransformerConfigMoveKey]]: ...
    @_builtins.property
    @pulumi.getter(name="parseCloudfront")
    def parse_cloudfront(
        self,
    ) -> Optional[outputs.LogTransformerTransformerConfigParseCloudfront]: ...
    @_builtins.property
    @pulumi.getter(name="parseJsons")
    def parse_jsons(
        self,
    ) -> Optional[Sequence[outputs.LogTransformerTransformerConfigParseJson]]: ...
    @_builtins.property
    @pulumi.getter(name="parseKeyValues")
    def parse_key_values(
        self,
    ) -> Optional[Sequence[outputs.LogTransformerTransformerConfigParseKeyValue]]: ...
    @_builtins.property
    @pulumi.getter(name="parsePostgres")
    def parse_postgres(
        self,
    ) -> Optional[outputs.LogTransformerTransformerConfigParsePostgres]: ...
    @_builtins.property
    @pulumi.getter(name="parseRoute53")
    def parse_route53(
        self,
    ) -> Optional[outputs.LogTransformerTransformerConfigParseRoute53]: ...
    @_builtins.property
    @pulumi.getter(name="parseToOcsf")
    def parse_to_ocsf(
        self,
    ) -> Optional[outputs.LogTransformerTransformerConfigParseToOcsf]: ...
    @_builtins.property
    @pulumi.getter(name="parseVpc")
    def parse_vpc(
        self,
    ) -> Optional[outputs.LogTransformerTransformerConfigParseVpc]: ...
    @_builtins.property
    @pulumi.getter(name="parseWaf")
    def parse_waf(
        self,
    ) -> Optional[outputs.LogTransformerTransformerConfigParseWaf]: ...
    @_builtins.property
    @pulumi.getter(name="renameKeys")
    def rename_keys(
        self,
    ) -> Optional[Sequence[outputs.LogTransformerTransformerConfigRenameKey]]: ...
    @_builtins.property
    @pulumi.getter(name="splitStrings")
    def split_strings(
        self,
    ) -> Optional[Sequence[outputs.LogTransformerTransformerConfigSplitString]]: ...
    @_builtins.property
    @pulumi.getter(name="substituteStrings")
    def substitute_strings(
        self,
    ) -> Optional[
        Sequence[outputs.LogTransformerTransformerConfigSubstituteString]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="trimStrings")
    def trim_strings(
        self,
    ) -> Optional[Sequence[outputs.LogTransformerTransformerConfigTrimString]]: ...
    @_builtins.property
    @pulumi.getter(name="typeConverters")
    def type_converters(
        self,
    ) -> Optional[Sequence[outputs.LogTransformerTransformerConfigTypeConverter]]: ...
    @_builtins.property
    @pulumi.getter(name="upperCaseStrings")
    def upper_case_strings(
        self,
    ) -> Optional[Sequence[outputs.LogTransformerTransformerConfigUpperCaseString]]: ...

@pulumi.output_type
class LogTransformerTransformerConfigAddKeys(dict):
    def __init__(
        __self__,
        *,
        entries: Sequence[outputs.LogTransformerTransformerConfigAddKeysEntry],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> Sequence[outputs.LogTransformerTransformerConfigAddKeysEntry]: ...

@pulumi.output_type
class LogTransformerTransformerConfigAddKeysEntry(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        value: _builtins.str,
        overwrite_if_exists: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="overwriteIfExists")
    def overwrite_if_exists(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class LogTransformerTransformerConfigCopyValue(dict):
    def __init__(
        __self__,
        *,
        entries: Sequence[outputs.LogTransformerTransformerConfigCopyValueEntry],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> Sequence[outputs.LogTransformerTransformerConfigCopyValueEntry]: ...

@pulumi.output_type
class LogTransformerTransformerConfigCopyValueEntry(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source: _builtins.str,
        target: _builtins.str,
        overwrite_if_exists: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="overwriteIfExists")
    def overwrite_if_exists(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class LogTransformerTransformerConfigCsv(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        columns: Optional[Sequence[_builtins.str]] = ...,
        delimiter: Optional[_builtins.str] = ...,
        quote_character: Optional[_builtins.str] = ...,
        source: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="quoteCharacter")
    def quote_character(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigDateTimeConverter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        match_patterns: Sequence[_builtins.str],
        source: _builtins.str,
        target: _builtins.str,
        locale: Optional[_builtins.str] = ...,
        source_timezone: Optional[_builtins.str] = ...,
        target_format: Optional[_builtins.str] = ...,
        target_timezone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceTimezone")
    def source_timezone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetFormat")
    def target_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetTimezone")
    def target_timezone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigDeleteKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, with_keys: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="withKeys")
    def with_keys(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigGrok(dict):
    def __init__(
        __self__, *, match: _builtins.str, source: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigListToMap(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        source: _builtins.str,
        flatten: Optional[_builtins.bool] = ...,
        flattened_element: Optional[_builtins.str] = ...,
        target: Optional[_builtins.str] = ...,
        value_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def flatten(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="flattenedElement")
    def flattened_element(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valueKey")
    def value_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigLowerCaseString(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, with_keys: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="withKeys")
    def with_keys(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigMoveKey(dict):
    def __init__(
        __self__,
        *,
        entries: Sequence[outputs.LogTransformerTransformerConfigMoveKeyEntry],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> Sequence[outputs.LogTransformerTransformerConfigMoveKeyEntry]: ...

@pulumi.output_type
class LogTransformerTransformerConfigMoveKeyEntry(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source: _builtins.str,
        target: _builtins.str,
        overwrite_if_exists: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="overwriteIfExists")
    def overwrite_if_exists(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class LogTransformerTransformerConfigParseCloudfront(dict):
    def __init__(__self__, *, source: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigParseJson(dict):
    def __init__(
        __self__,
        *,
        destination: Optional[_builtins.str] = ...,
        source: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigParseKeyValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: Optional[_builtins.str] = ...,
        field_delimiter: Optional[_builtins.str] = ...,
        key_prefix: Optional[_builtins.str] = ...,
        key_value_delimiter: Optional[_builtins.str] = ...,
        non_match_value: Optional[_builtins.str] = ...,
        overwrite_if_exists: Optional[_builtins.bool] = ...,
        source: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fieldDelimiter")
    def field_delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyValueDelimiter")
    def key_value_delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nonMatchValue")
    def non_match_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="overwriteIfExists")
    def overwrite_if_exists(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigParsePostgres(dict):
    def __init__(__self__, *, source: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigParseRoute53(dict):
    def __init__(__self__, *, source: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigParseToOcsf(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_source: _builtins.str,
        ocsf_version: _builtins.str,
        source: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventSource")
    def event_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ocsfVersion")
    def ocsf_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigParseVpc(dict):
    def __init__(__self__, *, source: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigParseWaf(dict):
    def __init__(__self__, *, source: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigRenameKey(dict):
    def __init__(
        __self__,
        *,
        entries: Sequence[outputs.LogTransformerTransformerConfigRenameKeyEntry],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> Sequence[outputs.LogTransformerTransformerConfigRenameKeyEntry]: ...

@pulumi.output_type
class LogTransformerTransformerConfigRenameKeyEntry(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        rename_to: _builtins.str,
        overwrite_if_exists: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="renameTo")
    def rename_to(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="overwriteIfExists")
    def overwrite_if_exists(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class LogTransformerTransformerConfigSplitString(dict):
    def __init__(
        __self__,
        *,
        entries: Sequence[outputs.LogTransformerTransformerConfigSplitStringEntry],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> Sequence[outputs.LogTransformerTransformerConfigSplitStringEntry]: ...

@pulumi.output_type
class LogTransformerTransformerConfigSplitStringEntry(dict):
    def __init__(
        __self__, *, delimiter: _builtins.str, source: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...

@pulumi.output_type
class LogTransformerTransformerConfigSubstituteString(dict):
    def __init__(
        __self__,
        *,
        entries: Sequence[outputs.LogTransformerTransformerConfigSubstituteStringEntry],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> Sequence[outputs.LogTransformerTransformerConfigSubstituteStringEntry]: ...

@pulumi.output_type
class LogTransformerTransformerConfigSubstituteStringEntry(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, from_: _builtins.str, source: _builtins.str, to: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="from")
    def from_(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> _builtins.str: ...

@pulumi.output_type
class LogTransformerTransformerConfigTrimString(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, with_keys: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="withKeys")
    def with_keys(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class LogTransformerTransformerConfigTypeConverter(dict):
    def __init__(
        __self__,
        *,
        entries: Sequence[outputs.LogTransformerTransformerConfigTypeConverterEntry],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> Sequence[outputs.LogTransformerTransformerConfigTypeConverterEntry]: ...

@pulumi.output_type
class LogTransformerTransformerConfigTypeConverterEntry(dict):
    def __init__(__self__, *, key: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class LogTransformerTransformerConfigUpperCaseString(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, with_keys: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="withKeys")
    def with_keys(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class MetricAlarmMetricQuery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        account_id: Optional[_builtins.str] = ...,
        expression: Optional[_builtins.str] = ...,
        label: Optional[_builtins.str] = ...,
        metric: Optional[outputs.MetricAlarmMetricQueryMetric] = ...,
        period: Optional[_builtins.int] = ...,
        return_data: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metric(self) -> Optional[outputs.MetricAlarmMetricQueryMetric]: ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="returnData")
    def return_data(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MetricAlarmMetricQueryMetric(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_name: _builtins.str,
        period: _builtins.int,
        stat: _builtins.str,
        dimensions: Optional[Mapping[str, _builtins.str]] = ...,
        namespace: Optional[_builtins.str] = ...,
        unit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def stat(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MetricStreamExcludeFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        namespace: _builtins.str,
        metric_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metricNames")
    def metric_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class MetricStreamIncludeFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        namespace: _builtins.str,
        metric_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metricNames")
    def metric_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class MetricStreamStatisticsConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_statistics: Sequence[_builtins.str],
        include_metrics: Sequence[
            outputs.MetricStreamStatisticsConfigurationIncludeMetric
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalStatistics")
    def additional_statistics(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includeMetrics")
    def include_metrics(
        self,
    ) -> Sequence[outputs.MetricStreamStatisticsConfigurationIncludeMetric]: ...

@pulumi.output_type
class MetricStreamStatisticsConfigurationIncludeMetric(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, metric_name: _builtins.str, namespace: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...

@pulumi.output_type
class GetContributorManagedInsightRulesManagedRuleResult(dict):
    def __init__(
        __self__,
        *,
        resource_arn: _builtins.str,
        rule_states: Sequence[
            outputs.GetContributorManagedInsightRulesManagedRuleRuleStateResult
        ],
        template_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleStates")
    def rule_states(
        self,
    ) -> Sequence[
        outputs.GetContributorManagedInsightRulesManagedRuleRuleStateResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="templateName")
    def template_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetContributorManagedInsightRulesManagedRuleRuleStateResult(dict):
    def __init__(
        __self__, *, rule_name: _builtins.str, state: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class GetEventBusDeadLetterConfigResult(dict):
    def __init__(__self__, *, arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetEventBusLogConfigResult(dict):
    def __init__(
        __self__, *, include_detail: _builtins.str, level: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeDetail")
    def include_detail(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> _builtins.str: ...

@pulumi.output_type
class GetEventBusesEventBusResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        creation_time: _builtins.str,
        description: _builtins.str,
        last_modified_time: _builtins.str,
        name: _builtins.str,
        policy: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str: ...

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        custom_data_identifiers: Optional[
            Sequence[
                outputs.GetLogDataProtectionPolicyDocumentConfigurationCustomDataIdentifierResult
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customDataIdentifiers")
    def custom_data_identifiers(
        self,
    ) -> Optional[
        Sequence[
            outputs.GetLogDataProtectionPolicyDocumentConfigurationCustomDataIdentifierResult
        ]
    ]: ...

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentConfigurationCustomDataIdentifierResult(dict):
    def __init__(__self__, *, name: _builtins.str, regex: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentStatementResult(dict):
    def __init__(
        __self__,
        *,
        data_identifiers: Sequence[_builtins.str],
        operation: outputs.GetLogDataProtectionPolicyDocumentStatementOperationResult,
        sid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataIdentifiers")
    def data_identifiers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def operation(
        self,
    ) -> outputs.GetLogDataProtectionPolicyDocumentStatementOperationResult: ...
    @_builtins.property
    @pulumi.getter
    def sid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentStatementOperationResult(dict):
    def __init__(
        __self__,
        *,
        audit: Optional[
            outputs.GetLogDataProtectionPolicyDocumentStatementOperationAuditResult
        ] = ...,
        deidentify: Optional[
            outputs.GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyResult
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audit(
        self,
    ) -> Optional[
        outputs.GetLogDataProtectionPolicyDocumentStatementOperationAuditResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def deidentify(
        self,
    ) -> Optional[
        outputs.GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyResult
    ]: ...

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentStatementOperationAuditResult(dict):
    def __init__(
        __self__,
        *,
        findings_destination: outputs.GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationResult,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="findingsDestination")
    def findings_destination(
        self,
    ) -> outputs.GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationResult: ...

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationResult(
    dict
):
    def __init__(
        __self__,
        *,
        cloudwatch_logs: Optional[
            outputs.GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationCloudwatchLogsResult
        ] = ...,
        firehose: Optional[
            outputs.GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationFirehoseResult
        ] = ...,
        s3: Optional[
            outputs.GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationS3Result
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> Optional[
        outputs.GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationCloudwatchLogsResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def firehose(
        self,
    ) -> Optional[
        outputs.GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationFirehoseResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        outputs.GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationS3Result
    ]: ...

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationCloudwatchLogsResult(
    dict
):
    def __init__(__self__, *, log_group: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logGroup")
    def log_group(self) -> _builtins.str: ...

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationFirehoseResult(
    dict
):
    def __init__(__self__, *, delivery_stream: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deliveryStream")
    def delivery_stream(self) -> _builtins.str: ...

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentStatementOperationAuditFindingsDestinationS3Result(
    dict
):
    def __init__(__self__, *, bucket: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyResult(dict):
    def __init__(
        __self__,
        *,
        mask_config: outputs.GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyMaskConfigResult,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maskConfig")
    def mask_config(
        self,
    ) -> outputs.GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyMaskConfigResult: ...

@pulumi.output_type
class GetLogDataProtectionPolicyDocumentStatementOperationDeidentifyMaskConfigResult(
    dict
):
    def __init__(__self__) -> None: ...
