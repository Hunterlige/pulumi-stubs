import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccountThrottleSettingArgs",
    "AccountThrottleSettingArgsDict",
    "DocumentationPartLocationArgs",
    "DocumentationPartLocationArgsDict",
    "DomainNameEndpointConfigurationArgs",
    "DomainNameEndpointConfigurationArgsDict",
    "DomainNameMutualTlsAuthenticationArgs",
    "DomainNameMutualTlsAuthenticationArgsDict",
    "IntegrationTlsConfigArgs",
    "IntegrationTlsConfigArgsDict",
    "MethodSettingsSettingsArgs",
    "MethodSettingsSettingsArgsDict",
    "RestApiEndpointConfigurationArgs",
    "RestApiEndpointConfigurationArgsDict",
    "RestApiPutTimeoutsArgs",
    "RestApiPutTimeoutsArgsDict",
    "StageAccessLogSettingsArgs",
    "StageAccessLogSettingsArgsDict",
    "StageCanarySettingsArgs",
    "StageCanarySettingsArgsDict",
    "UsagePlanApiStageArgs",
    "UsagePlanApiStageArgsDict",
    "UsagePlanApiStageThrottleArgs",
    "UsagePlanApiStageThrottleArgsDict",
    "UsagePlanQuotaSettingsArgs",
    "UsagePlanQuotaSettingsArgsDict",
    "UsagePlanThrottleSettingsArgs",
    "UsagePlanThrottleSettingsArgsDict",
]

class AccountThrottleSettingArgsDict(TypedDict):
    burst_limit: pulumi.Input[_builtins.int]
    rate_limit: pulumi.Input[_builtins.float]

@pulumi.input_type
class AccountThrottleSettingArgs:
    def __init__(
        __self__,
        *,
        burst_limit: pulumi.Input[_builtins.int],
        rate_limit: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="burstLimit")
    def burst_limit(self) -> pulumi.Input[_builtins.int]: ...
    @burst_limit.setter
    def burst_limit(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> pulumi.Input[_builtins.float]: ...
    @rate_limit.setter
    def rate_limit(self, value: pulumi.Input[_builtins.float]): ...

class DocumentationPartLocationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    method: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    status_code: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DocumentationPartLocationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        status_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status_code.setter
    def status_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainNameEndpointConfigurationArgsDict(TypedDict):
    types: pulumi.Input[_builtins.str]
    ip_address_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainNameEndpointConfigurationArgs:
    def __init__(
        __self__,
        *,
        types: pulumi.Input[_builtins.str],
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def types(self) -> pulumi.Input[_builtins.str]: ...
    @types.setter
    def types(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainNameMutualTlsAuthenticationArgsDict(TypedDict):
    truststore_uri: pulumi.Input[_builtins.str]
    truststore_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainNameMutualTlsAuthenticationArgs:
    def __init__(
        __self__,
        *,
        truststore_uri: pulumi.Input[_builtins.str],
        truststore_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="truststoreUri")
    def truststore_uri(self) -> pulumi.Input[_builtins.str]: ...
    @truststore_uri.setter
    def truststore_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="truststoreVersion")
    def truststore_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @truststore_version.setter
    def truststore_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IntegrationTlsConfigArgsDict(TypedDict):
    insecure_skip_verification: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class IntegrationTlsConfigArgs:
    def __init__(
        __self__,
        *,
        insecure_skip_verification: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insecureSkipVerification")
    def insecure_skip_verification(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @insecure_skip_verification.setter
    def insecure_skip_verification(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class MethodSettingsSettingsArgsDict(TypedDict):
    cache_data_encrypted: NotRequired[pulumi.Input[_builtins.bool]]
    cache_ttl_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    caching_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    data_trace_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    logging_level: NotRequired[pulumi.Input[_builtins.str]]
    metrics_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    require_authorization_for_cache_control: NotRequired[pulumi.Input[_builtins.bool]]
    throttling_burst_limit: NotRequired[pulumi.Input[_builtins.int]]
    throttling_rate_limit: NotRequired[pulumi.Input[_builtins.float]]
    unauthorized_cache_control_header_strategy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MethodSettingsSettingsArgs:
    def __init__(
        __self__,
        *,
        cache_data_encrypted: Optional[pulumi.Input[_builtins.bool]] = ...,
        cache_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        caching_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        data_trace_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        logging_level: Optional[pulumi.Input[_builtins.str]] = ...,
        metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_authorization_for_cache_control: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        throttling_burst_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        throttling_rate_limit: Optional[pulumi.Input[_builtins.float]] = ...,
        unauthorized_cache_control_header_strategy: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheDataEncrypted")
    def cache_data_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cache_data_encrypted.setter
    def cache_data_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheTtlInSeconds")
    def cache_ttl_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @cache_ttl_in_seconds.setter
    def cache_ttl_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="cachingEnabled")
    def caching_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @caching_enabled.setter
    def caching_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dataTraceEnabled")
    def data_trace_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @data_trace_enabled.setter
    def data_trace_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logging_level.setter
    def logging_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metricsEnabled")
    def metrics_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @metrics_enabled.setter
    def metrics_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requireAuthorizationForCacheControl")
    def require_authorization_for_cache_control(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_authorization_for_cache_control.setter
    def require_authorization_for_cache_control(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="throttlingBurstLimit")
    def throttling_burst_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @throttling_burst_limit.setter
    def throttling_burst_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="throttlingRateLimit")
    def throttling_rate_limit(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @throttling_rate_limit.setter
    def throttling_rate_limit(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="unauthorizedCacheControlHeaderStrategy")
    def unauthorized_cache_control_header_strategy(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unauthorized_cache_control_header_strategy.setter
    def unauthorized_cache_control_header_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class RestApiEndpointConfigurationArgsDict(TypedDict):
    types: pulumi.Input[_builtins.str]
    ip_address_type: NotRequired[pulumi.Input[_builtins.str]]
    vpc_endpoint_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RestApiEndpointConfigurationArgs:
    def __init__(
        __self__,
        *,
        types: pulumi.Input[_builtins.str],
        ip_address_type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_endpoint_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def types(self) -> pulumi.Input[_builtins.str]: ...
    @types.setter
    def types(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointIds")
    def vpc_endpoint_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_endpoint_ids.setter
    def vpc_endpoint_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RestApiPutTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RestApiPutTimeoutsArgs:
    def __init__(
        __self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StageAccessLogSettingsArgsDict(TypedDict):
    destination_arn: pulumi.Input[_builtins.str]
    format: pulumi.Input[_builtins.str]

@pulumi.input_type
class StageAccessLogSettingsArgs:
    def __init__(
        __self__,
        *,
        destination_arn: pulumi.Input[_builtins.str],
        format: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Input[_builtins.str]: ...
    @destination_arn.setter
    def destination_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]: ...
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): ...

class StageCanarySettingsArgsDict(TypedDict):
    deployment_id: pulumi.Input[_builtins.str]
    percent_traffic: NotRequired[pulumi.Input[_builtins.float]]
    stage_variable_overrides: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    use_stage_cache: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class StageCanarySettingsArgs:
    def __init__(
        __self__,
        *,
        deployment_id: pulumi.Input[_builtins.str],
        percent_traffic: Optional[pulumi.Input[_builtins.float]] = ...,
        stage_variable_overrides: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        use_stage_cache: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Input[_builtins.str]: ...
    @deployment_id.setter
    def deployment_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="percentTraffic")
    def percent_traffic(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @percent_traffic.setter
    def percent_traffic(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="stageVariableOverrides")
    def stage_variable_overrides(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @stage_variable_overrides.setter
    def stage_variable_overrides(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useStageCache")
    def use_stage_cache(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_stage_cache.setter
    def use_stage_cache(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class UsagePlanApiStageArgsDict(TypedDict):
    api_id: pulumi.Input[_builtins.str]
    stage: pulumi.Input[_builtins.str]
    throttles: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[UsagePlanApiStageThrottleArgsDict]]]
    ]

@pulumi.input_type
class UsagePlanApiStageArgs:
    def __init__(
        __self__,
        *,
        api_id: pulumi.Input[_builtins.str],
        stage: pulumi.Input[_builtins.str],
        throttles: Optional[
            pulumi.Input[Sequence[pulumi.Input[UsagePlanApiStageThrottleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[_builtins.str]: ...
    @api_id.setter
    def api_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> pulumi.Input[_builtins.str]: ...
    @stage.setter
    def stage(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def throttles(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[UsagePlanApiStageThrottleArgs]]]
    ]: ...
    @throttles.setter
    def throttles(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[UsagePlanApiStageThrottleArgs]]]
        ],
    ): ...

class UsagePlanApiStageThrottleArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    burst_limit: NotRequired[pulumi.Input[_builtins.int]]
    rate_limit: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class UsagePlanApiStageThrottleArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        burst_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        rate_limit: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="burstLimit")
    def burst_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @burst_limit.setter
    def burst_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @rate_limit.setter
    def rate_limit(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class UsagePlanQuotaSettingsArgsDict(TypedDict):
    limit: pulumi.Input[_builtins.int]
    period: pulumi.Input[_builtins.str]
    offset: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class UsagePlanQuotaSettingsArgs:
    def __init__(
        __self__,
        *,
        limit: pulumi.Input[_builtins.int],
        period: pulumi.Input[_builtins.str],
        offset: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limit(self) -> pulumi.Input[_builtins.int]: ...
    @limit.setter
    def limit(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def period(self) -> pulumi.Input[_builtins.str]: ...
    @period.setter
    def period(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def offset(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @offset.setter
    def offset(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class UsagePlanThrottleSettingsArgsDict(TypedDict):
    burst_limit: NotRequired[pulumi.Input[_builtins.int]]
    rate_limit: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class UsagePlanThrottleSettingsArgs:
    def __init__(
        __self__,
        *,
        burst_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        rate_limit: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="burstLimit")
    def burst_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @burst_limit.setter
    def burst_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @rate_limit.setter
    def rate_limit(self, value: Optional[pulumi.Input[_builtins.float]]): ...
