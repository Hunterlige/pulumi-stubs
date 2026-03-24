import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AnycastIpListTimeouts",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ConnectionFunctionConnectionFunctionConfig",
    ...,
    "ConnectionGroupTimeouts",
    ...,
    "ContinuousDeploymentPolicyTrafficConfig",
    ...,
    ...,
    ...,
    "DistributionConnectionFunctionAssociation",
    "DistributionCustomErrorResponse",
    "DistributionDefaultCacheBehavior",
    "DistributionDefaultCacheBehaviorForwardedValues",
    ...,
    ...,
    "DistributionDefaultCacheBehaviorGrpcConfig",
    ...,
    "DistributionLoggingConfig",
    "DistributionOrderedCacheBehavior",
    "DistributionOrderedCacheBehaviorForwardedValues",
    ...,
    ...,
    "DistributionOrderedCacheBehaviorGrpcConfig",
    ...,
    "DistributionOrigin",
    "DistributionOriginCustomHeader",
    "DistributionOriginCustomOriginConfig",
    "DistributionOriginGroup",
    "DistributionOriginGroupFailoverCriteria",
    "DistributionOriginGroupMember",
    "DistributionOriginOriginShield",
    "DistributionOriginS3OriginConfig",
    "DistributionOriginVpcOriginConfig",
    "DistributionRestrictions",
    "DistributionRestrictionsGeoRestriction",
    "DistributionTenantCustomizations",
    "DistributionTenantCustomizationsCertificate",
    "DistributionTenantCustomizationsGeoRestriction",
    "DistributionTenantCustomizationsWebAcl",
    "DistributionTenantDomain",
    "DistributionTenantManagedCertificateRequest",
    "DistributionTenantParameter",
    "DistributionTenantTimeouts",
    "DistributionTrustedKeyGroup",
    "DistributionTrustedKeyGroupItem",
    "DistributionTrustedSigner",
    "DistributionTrustedSignerItem",
    "DistributionViewerCertificate",
    "DistributionViewerMtlsConfig",
    "DistributionViewerMtlsConfigTrustStoreConfig",
    "FieldLevelEncryptionConfigContentTypeProfileConfig",
    ...,
    ...,
    "FieldLevelEncryptionConfigQueryArgProfileConfig",
    ...,
    ...,
    "FieldLevelEncryptionProfileEncryptionEntities",
    "FieldLevelEncryptionProfileEncryptionEntitiesItem",
    ...,
    "KeyValueStoreTimeouts",
    "KeyvaluestoreKeysExclusiveResourceKeyValuePair",
    "MonitoringSubscriptionMonitoringSubscription",
    ...,
    "MultitenantDistributionActiveTrustedKeyGroup",
    "MultitenantDistributionActiveTrustedKeyGroupItem",
    "MultitenantDistributionCacheBehavior",
    "MultitenantDistributionCacheBehaviorAllowedMethods",
    ...,
    ...,
    ...,
    "MultitenantDistributionCustomErrorResponse",
    "MultitenantDistributionDefaultCacheBehavior",
    ...,
    ...,
    ...,
    ...,
    "MultitenantDistributionOrigin",
    "MultitenantDistributionOriginCustomHeader",
    "MultitenantDistributionOriginCustomOriginConfig",
    "MultitenantDistributionOriginGroup",
    "MultitenantDistributionOriginGroupFailoverCriteria",
    "MultitenantDistributionOriginGroupMember",
    "MultitenantDistributionOriginOriginShield",
    "MultitenantDistributionOriginVpcOriginConfig",
    "MultitenantDistributionRestrictions",
    "MultitenantDistributionRestrictionsGeoRestriction",
    "MultitenantDistributionTenantConfig",
    ...,
    ...,
    ...,
    "MultitenantDistributionTimeouts",
    "MultitenantDistributionViewerCertificate",
    "OriginRequestPolicyCookiesConfig",
    "OriginRequestPolicyCookiesConfigCookies",
    "OriginRequestPolicyHeadersConfig",
    "OriginRequestPolicyHeadersConfigHeaders",
    "OriginRequestPolicyQueryStringsConfig",
    "OriginRequestPolicyQueryStringsConfigQueryStrings",
    "RealtimeLogConfigEndpoint",
    "RealtimeLogConfigEndpointKinesisStreamConfig",
    "ResponseHeadersPolicyCorsConfig",
    ...,
    ...,
    ...,
    ...,
    "ResponseHeadersPolicyCustomHeadersConfig",
    "ResponseHeadersPolicyCustomHeadersConfigItem",
    "ResponseHeadersPolicyRemoveHeadersConfig",
    "ResponseHeadersPolicyRemoveHeadersConfigItem",
    "ResponseHeadersPolicySecurityHeadersConfig",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ResponseHeadersPolicyServerTimingHeadersConfig",
    "TrustStoreCaCertificatesBundleSource",
    ...,
    "TrustStoreTimeouts",
    "VpcOriginTimeouts",
    "VpcOriginVpcOriginEndpointConfig",
    "VpcOriginVpcOriginEndpointConfigOriginSslProtocols",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetDistributionTenantCustomizationResult",
    ...,
    ...,
    "GetDistributionTenantCustomizationWebAclResult",
    "GetDistributionTenantDomainResult",
    ...,
    "GetDistributionTenantParameterResult",
    "GetOriginRequestPolicyCookiesConfigResult",
    "GetOriginRequestPolicyCookiesConfigCookieResult",
    "GetOriginRequestPolicyHeadersConfigResult",
    "GetOriginRequestPolicyHeadersConfigHeaderResult",
    "GetOriginRequestPolicyQueryStringsConfigResult",
    ...,
    "GetRealtimeLogConfigEndpointResult",
    ...,
    "GetResponseHeadersPolicyCorsConfigResult",
    ...,
    ...,
    ...,
    ...,
    "GetResponseHeadersPolicyCustomHeadersConfigResult",
    ...,
    "GetResponseHeadersPolicyRemoveHeadersConfigResult",
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

@pulumi.output_type
class AnycastIpListTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CachePolicyParametersInCacheKeyAndForwardedToOrigin(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cookies_config: outputs.CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig,
        headers_config: outputs.CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig,
        query_strings_config: outputs.CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig,
        enable_accept_encoding_brotli: Optional[_builtins.bool] = ...,
        enable_accept_encoding_gzip: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cookiesConfig")
    def cookies_config(
        self,
    ) -> outputs.CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig: ...
    @_builtins.property
    @pulumi.getter(name="headersConfig")
    def headers_config(
        self,
    ) -> outputs.CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig: ...
    @_builtins.property
    @pulumi.getter(name="queryStringsConfig")
    def query_strings_config(
        self,
    ) -> (
        outputs.CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAcceptEncodingBrotli")
    def enable_accept_encoding_brotli(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableAcceptEncodingGzip")
    def enable_accept_encoding_gzip(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cookie_behavior: _builtins.str,
        cookies: Optional[
            outputs.CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cookieBehavior")
    def cookie_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cookies(
        self,
    ) -> Optional[
        outputs.CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies
    ]: ...

@pulumi.output_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookies(dict):
    def __init__(
        __self__, *, items: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        header_behavior: Optional[_builtins.str] = ...,
        headers: Optional[
            outputs.CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerBehavior")
    def header_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        outputs.CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders
    ]: ...

@pulumi.output_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaders(dict):
    def __init__(
        __self__, *, items: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        query_string_behavior: _builtins.str,
        query_strings: Optional[
            outputs.CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryStringBehavior")
    def query_string_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(
        self,
    ) -> Optional[
        outputs.CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings
    ]: ...

@pulumi.output_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStrings(
    dict
):
    def __init__(
        __self__, *, items: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ConnectionFunctionConnectionFunctionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        comment: _builtins.str,
        runtime: _builtins.str,
        key_value_store_association: Optional[
            outputs.ConnectionFunctionConnectionFunctionConfigKeyValueStoreAssociation
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyValueStoreAssociation")
    def key_value_store_association(
        self,
    ) -> Optional[
        outputs.ConnectionFunctionConnectionFunctionConfigKeyValueStoreAssociation
    ]: ...

@pulumi.output_type
class ConnectionFunctionConnectionFunctionConfigKeyValueStoreAssociation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, key_value_store_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyValueStoreArn")
    def key_value_store_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionGroupTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContinuousDeploymentPolicyStagingDistributionDnsNames(dict):
    def __init__(
        __self__,
        *,
        quantity: _builtins.int,
        items: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def quantity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ContinuousDeploymentPolicyTrafficConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        single_header_config: Optional[
            outputs.ContinuousDeploymentPolicyTrafficConfigSingleHeaderConfig
        ] = ...,
        single_weight_config: Optional[
            outputs.ContinuousDeploymentPolicyTrafficConfigSingleWeightConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="singleHeaderConfig")
    def single_header_config(
        self,
    ) -> Optional[
        outputs.ContinuousDeploymentPolicyTrafficConfigSingleHeaderConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="singleWeightConfig")
    def single_weight_config(
        self,
    ) -> Optional[
        outputs.ContinuousDeploymentPolicyTrafficConfigSingleWeightConfig
    ]: ...

@pulumi.output_type
class ContinuousDeploymentPolicyTrafficConfigSingleHeaderConfig(dict):
    def __init__(__self__, *, header: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def header(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ContinuousDeploymentPolicyTrafficConfigSingleWeightConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        weight: _builtins.float,
        session_stickiness_config: Optional[
            outputs.ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigSessionStickinessConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="sessionStickinessConfig")
    def session_stickiness_config(
        self,
    ) -> Optional[
        outputs.ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigSessionStickinessConfig
    ]: ...

@pulumi.output_type
class ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigSessionStickinessConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, idle_ttl: _builtins.int, maximum_ttl: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleTtl")
    def idle_ttl(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maximumTtl")
    def maximum_ttl(self) -> _builtins.int: ...

@pulumi.output_type
class DistributionConnectionFunctionAssociation(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class DistributionCustomErrorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_code: _builtins.int,
        error_caching_min_ttl: Optional[_builtins.int] = ...,
        response_code: Optional[_builtins.int] = ...,
        response_page_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="errorCachingMinTtl")
    def error_caching_min_ttl(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="responsePagePath")
    def response_page_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionDefaultCacheBehavior(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_methods: Sequence[_builtins.str],
        cached_methods: Sequence[_builtins.str],
        target_origin_id: _builtins.str,
        viewer_protocol_policy: _builtins.str,
        cache_policy_id: Optional[_builtins.str] = ...,
        compress: Optional[_builtins.bool] = ...,
        default_ttl: Optional[_builtins.int] = ...,
        field_level_encryption_id: Optional[_builtins.str] = ...,
        forwarded_values: Optional[
            outputs.DistributionDefaultCacheBehaviorForwardedValues
        ] = ...,
        function_associations: Optional[
            Sequence[outputs.DistributionDefaultCacheBehaviorFunctionAssociation]
        ] = ...,
        grpc_config: Optional[outputs.DistributionDefaultCacheBehaviorGrpcConfig] = ...,
        lambda_function_associations: Optional[
            Sequence[outputs.DistributionDefaultCacheBehaviorLambdaFunctionAssociation]
        ] = ...,
        max_ttl: Optional[_builtins.int] = ...,
        min_ttl: Optional[_builtins.int] = ...,
        origin_request_policy_id: Optional[_builtins.str] = ...,
        realtime_log_config_arn: Optional[_builtins.str] = ...,
        response_headers_policy_id: Optional[_builtins.str] = ...,
        smooth_streaming: Optional[_builtins.bool] = ...,
        trusted_key_groups: Optional[Sequence[_builtins.str]] = ...,
        trusted_signers: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cachedMethods")
    def cached_methods(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetOriginId")
    def target_origin_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="viewerProtocolPolicy")
    def viewer_protocol_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cachePolicyId")
    def cache_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def compress(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="fieldLevelEncryptionId")
    def field_level_encryption_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forwardedValues")
    def forwarded_values(
        self,
    ) -> Optional[outputs.DistributionDefaultCacheBehaviorForwardedValues]: ...
    @_builtins.property
    @pulumi.getter(name="functionAssociations")
    def function_associations(
        self,
    ) -> Optional[
        Sequence[outputs.DistributionDefaultCacheBehaviorFunctionAssociation]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="grpcConfig")
    def grpc_config(
        self,
    ) -> Optional[outputs.DistributionDefaultCacheBehaviorGrpcConfig]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionAssociations")
    def lambda_function_associations(
        self,
    ) -> Optional[
        Sequence[outputs.DistributionDefaultCacheBehaviorLambdaFunctionAssociation]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minTtl")
    def min_ttl(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="originRequestPolicyId")
    def origin_request_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="realtimeLogConfigArn")
    def realtime_log_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responseHeadersPolicyId")
    def response_headers_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="smoothStreaming")
    def smooth_streaming(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="trustedKeyGroups")
    def trusted_key_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trustedSigners")
    def trusted_signers(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DistributionDefaultCacheBehaviorForwardedValues(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cookies: outputs.DistributionDefaultCacheBehaviorForwardedValuesCookies,
        query_string: _builtins.bool,
        headers: Optional[Sequence[_builtins.str]] = ...,
        query_string_cache_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cookies(
        self,
    ) -> outputs.DistributionDefaultCacheBehaviorForwardedValuesCookies: ...
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="queryStringCacheKeys")
    def query_string_cache_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DistributionDefaultCacheBehaviorForwardedValuesCookies(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        forward: _builtins.str,
        whitelisted_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def forward(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="whitelistedNames")
    def whitelisted_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DistributionDefaultCacheBehaviorFunctionAssociation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, event_type: _builtins.str, function_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> _builtins.str: ...

@pulumi.output_type
class DistributionDefaultCacheBehaviorGrpcConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DistributionDefaultCacheBehaviorLambdaFunctionAssociation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_type: _builtins.str,
        lambda_arn: _builtins.str,
        include_body: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeBody")
    def include_body(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DistributionLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: Optional[_builtins.str] = ...,
        include_cookies: Optional[_builtins.bool] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includeCookies")
    def include_cookies(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionOrderedCacheBehavior(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_methods: Sequence[_builtins.str],
        cached_methods: Sequence[_builtins.str],
        path_pattern: _builtins.str,
        target_origin_id: _builtins.str,
        viewer_protocol_policy: _builtins.str,
        cache_policy_id: Optional[_builtins.str] = ...,
        compress: Optional[_builtins.bool] = ...,
        default_ttl: Optional[_builtins.int] = ...,
        field_level_encryption_id: Optional[_builtins.str] = ...,
        forwarded_values: Optional[
            outputs.DistributionOrderedCacheBehaviorForwardedValues
        ] = ...,
        function_associations: Optional[
            Sequence[outputs.DistributionOrderedCacheBehaviorFunctionAssociation]
        ] = ...,
        grpc_config: Optional[outputs.DistributionOrderedCacheBehaviorGrpcConfig] = ...,
        lambda_function_associations: Optional[
            Sequence[outputs.DistributionOrderedCacheBehaviorLambdaFunctionAssociation]
        ] = ...,
        max_ttl: Optional[_builtins.int] = ...,
        min_ttl: Optional[_builtins.int] = ...,
        origin_request_policy_id: Optional[_builtins.str] = ...,
        realtime_log_config_arn: Optional[_builtins.str] = ...,
        response_headers_policy_id: Optional[_builtins.str] = ...,
        smooth_streaming: Optional[_builtins.bool] = ...,
        trusted_key_groups: Optional[Sequence[_builtins.str]] = ...,
        trusted_signers: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cachedMethods")
    def cached_methods(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pathPattern")
    def path_pattern(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetOriginId")
    def target_origin_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="viewerProtocolPolicy")
    def viewer_protocol_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cachePolicyId")
    def cache_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def compress(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="fieldLevelEncryptionId")
    def field_level_encryption_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forwardedValues")
    def forwarded_values(
        self,
    ) -> Optional[outputs.DistributionOrderedCacheBehaviorForwardedValues]: ...
    @_builtins.property
    @pulumi.getter(name="functionAssociations")
    def function_associations(
        self,
    ) -> Optional[
        Sequence[outputs.DistributionOrderedCacheBehaviorFunctionAssociation]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="grpcConfig")
    def grpc_config(
        self,
    ) -> Optional[outputs.DistributionOrderedCacheBehaviorGrpcConfig]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionAssociations")
    def lambda_function_associations(
        self,
    ) -> Optional[
        Sequence[outputs.DistributionOrderedCacheBehaviorLambdaFunctionAssociation]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minTtl")
    def min_ttl(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="originRequestPolicyId")
    def origin_request_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="realtimeLogConfigArn")
    def realtime_log_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responseHeadersPolicyId")
    def response_headers_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="smoothStreaming")
    def smooth_streaming(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="trustedKeyGroups")
    def trusted_key_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trustedSigners")
    def trusted_signers(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DistributionOrderedCacheBehaviorForwardedValues(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cookies: outputs.DistributionOrderedCacheBehaviorForwardedValuesCookies,
        query_string: _builtins.bool,
        headers: Optional[Sequence[_builtins.str]] = ...,
        query_string_cache_keys: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cookies(
        self,
    ) -> outputs.DistributionOrderedCacheBehaviorForwardedValuesCookies: ...
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="queryStringCacheKeys")
    def query_string_cache_keys(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DistributionOrderedCacheBehaviorForwardedValuesCookies(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        forward: _builtins.str,
        whitelisted_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def forward(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="whitelistedNames")
    def whitelisted_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DistributionOrderedCacheBehaviorFunctionAssociation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, event_type: _builtins.str, function_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> _builtins.str: ...

@pulumi.output_type
class DistributionOrderedCacheBehaviorGrpcConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DistributionOrderedCacheBehaviorLambdaFunctionAssociation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_type: _builtins.str,
        lambda_arn: _builtins.str,
        include_body: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeBody")
    def include_body(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DistributionOrigin(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_name: _builtins.str,
        origin_id: _builtins.str,
        connection_attempts: Optional[_builtins.int] = ...,
        connection_timeout: Optional[_builtins.int] = ...,
        custom_headers: Optional[
            Sequence[outputs.DistributionOriginCustomHeader]
        ] = ...,
        custom_origin_config: Optional[
            outputs.DistributionOriginCustomOriginConfig
        ] = ...,
        origin_access_control_id: Optional[_builtins.str] = ...,
        origin_path: Optional[_builtins.str] = ...,
        origin_shield: Optional[outputs.DistributionOriginOriginShield] = ...,
        response_completion_timeout: Optional[_builtins.int] = ...,
        s3_origin_config: Optional[outputs.DistributionOriginS3OriginConfig] = ...,
        vpc_origin_config: Optional[outputs.DistributionOriginVpcOriginConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="originId")
    def origin_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionAttempts")
    def connection_attempts(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="connectionTimeout")
    def connection_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(
        self,
    ) -> Optional[Sequence[outputs.DistributionOriginCustomHeader]]: ...
    @_builtins.property
    @pulumi.getter(name="customOriginConfig")
    def custom_origin_config(
        self,
    ) -> Optional[outputs.DistributionOriginCustomOriginConfig]: ...
    @_builtins.property
    @pulumi.getter(name="originAccessControlId")
    def origin_access_control_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originShield")
    def origin_shield(self) -> Optional[outputs.DistributionOriginOriginShield]: ...
    @_builtins.property
    @pulumi.getter(name="responseCompletionTimeout")
    def response_completion_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="s3OriginConfig")
    def s3_origin_config(
        self,
    ) -> Optional[outputs.DistributionOriginS3OriginConfig]: ...
    @_builtins.property
    @pulumi.getter(name="vpcOriginConfig")
    def vpc_origin_config(
        self,
    ) -> Optional[outputs.DistributionOriginVpcOriginConfig]: ...

@pulumi.output_type
class DistributionOriginCustomHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class DistributionOriginCustomOriginConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        http_port: _builtins.int,
        https_port: _builtins.int,
        origin_protocol_policy: _builtins.str,
        origin_ssl_protocols: Sequence[_builtins.str],
        ip_address_type: Optional[_builtins.str] = ...,
        origin_keepalive_timeout: Optional[_builtins.int] = ...,
        origin_read_timeout: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="originProtocolPolicy")
    def origin_protocol_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="originSslProtocols")
    def origin_ssl_protocols(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originKeepaliveTimeout")
    def origin_keepalive_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="originReadTimeout")
    def origin_read_timeout(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DistributionOriginGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        failover_criteria: outputs.DistributionOriginGroupFailoverCriteria,
        members: Sequence[outputs.DistributionOriginGroupMember],
        origin_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failoverCriteria")
    def failover_criteria(self) -> outputs.DistributionOriginGroupFailoverCriteria: ...
    @_builtins.property
    @pulumi.getter
    def members(self) -> Sequence[outputs.DistributionOriginGroupMember]: ...
    @_builtins.property
    @pulumi.getter(name="originId")
    def origin_id(self) -> _builtins.str: ...

@pulumi.output_type
class DistributionOriginGroupFailoverCriteria(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, status_codes: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="statusCodes")
    def status_codes(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class DistributionOriginGroupMember(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, origin_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="originId")
    def origin_id(self) -> _builtins.str: ...

@pulumi.output_type
class DistributionOriginOriginShield(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        origin_shield_region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="originShieldRegion")
    def origin_shield_region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionOriginS3OriginConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, origin_access_identity: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="originAccessIdentity")
    def origin_access_identity(self) -> _builtins.str: ...

@pulumi.output_type
class DistributionOriginVpcOriginConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        vpc_origin_id: _builtins.str,
        origin_keepalive_timeout: Optional[_builtins.int] = ...,
        origin_read_timeout: Optional[_builtins.int] = ...,
        owner_account_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcOriginId")
    def vpc_origin_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="originKeepaliveTimeout")
    def origin_keepalive_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="originReadTimeout")
    def origin_read_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionRestrictions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, geo_restriction: outputs.DistributionRestrictionsGeoRestriction
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="geoRestriction")
    def geo_restriction(self) -> outputs.DistributionRestrictionsGeoRestriction: ...

@pulumi.output_type
class DistributionRestrictionsGeoRestriction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        restriction_type: _builtins.str,
        locations: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="restrictionType")
    def restriction_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DistributionTenantCustomizations(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate: Optional[
            outputs.DistributionTenantCustomizationsCertificate
        ] = ...,
        geo_restriction: Optional[
            outputs.DistributionTenantCustomizationsGeoRestriction
        ] = ...,
        web_acl: Optional[outputs.DistributionTenantCustomizationsWebAcl] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificate(
        self,
    ) -> Optional[outputs.DistributionTenantCustomizationsCertificate]: ...
    @_builtins.property
    @pulumi.getter(name="geoRestriction")
    def geo_restriction(
        self,
    ) -> Optional[outputs.DistributionTenantCustomizationsGeoRestriction]: ...
    @_builtins.property
    @pulumi.getter(name="webAcl")
    def web_acl(self) -> Optional[outputs.DistributionTenantCustomizationsWebAcl]: ...

@pulumi.output_type
class DistributionTenantCustomizationsCertificate(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionTenantCustomizationsGeoRestriction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        locations: Optional[Sequence[_builtins.str]] = ...,
        restriction_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="restrictionType")
    def restriction_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionTenantCustomizationsWebAcl(dict):
    def __init__(
        __self__,
        *,
        action: Optional[_builtins.str] = ...,
        arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionTenantDomain(dict):
    def __init__(
        __self__, *, domain: _builtins.str, status: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionTenantManagedCertificateRequest(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_transparency_logging_preference: Optional[_builtins.str] = ...,
        primary_domain_name: Optional[_builtins.str] = ...,
        validation_token_host: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateTransparencyLoggingPreference")
    def certificate_transparency_logging_preference(
        self,
    ) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryDomainName")
    def primary_domain_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validationTokenHost")
    def validation_token_host(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionTenantParameter(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class DistributionTenantTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionTrustedKeyGroup(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        items: Optional[Sequence[outputs.DistributionTrustedKeyGroupItem]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[outputs.DistributionTrustedKeyGroupItem]]: ...

@pulumi.output_type
class DistributionTrustedKeyGroupItem(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_group_id: Optional[_builtins.str] = ...,
        key_pair_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyGroupId")
    def key_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyPairIds")
    def key_pair_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DistributionTrustedSigner(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        items: Optional[Sequence[outputs.DistributionTrustedSignerItem]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[outputs.DistributionTrustedSignerItem]]: ...

@pulumi.output_type
class DistributionTrustedSignerItem(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aws_account_number: Optional[_builtins.str] = ...,
        key_pair_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountNumber")
    def aws_account_number(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyPairIds")
    def key_pair_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DistributionViewerCertificate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        acm_certificate_arn: Optional[_builtins.str] = ...,
        cloudfront_default_certificate: Optional[_builtins.bool] = ...,
        iam_certificate_id: Optional[_builtins.str] = ...,
        minimum_protocol_version: Optional[_builtins.str] = ...,
        ssl_support_method: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acmCertificateArn")
    def acm_certificate_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudfrontDefaultCertificate")
    def cloudfront_default_certificate(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="iamCertificateId")
    def iam_certificate_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minimumProtocolVersion")
    def minimum_protocol_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslSupportMethod")
    def ssl_support_method(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DistributionViewerMtlsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mode: Optional[_builtins.str] = ...,
        trust_store_config: Optional[
            outputs.DistributionViewerMtlsConfigTrustStoreConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trustStoreConfig")
    def trust_store_config(
        self,
    ) -> Optional[outputs.DistributionViewerMtlsConfigTrustStoreConfig]: ...

@pulumi.output_type
class DistributionViewerMtlsConfigTrustStoreConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        trust_store_id: _builtins.str,
        advertise_trust_store_ca_names: Optional[_builtins.bool] = ...,
        ignore_certificate_expiry: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="trustStoreId")
    def trust_store_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="advertiseTrustStoreCaNames")
    def advertise_trust_store_ca_names(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreCertificateExpiry")
    def ignore_certificate_expiry(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FieldLevelEncryptionConfigContentTypeProfileConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        content_type_profiles: outputs.FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles,
        forward_when_content_type_is_unknown: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentTypeProfiles")
    def content_type_profiles(
        self,
    ) -> (
        outputs.FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles
    ): ...
    @_builtins.property
    @pulumi.getter(name="forwardWhenContentTypeIsUnknown")
    def forward_when_content_type_is_unknown(self) -> _builtins.bool: ...

@pulumi.output_type
class FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles(dict):
    def __init__(
        __self__,
        *,
        items: Sequence[
            outputs.FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItem
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Sequence[
        outputs.FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItem
    ]: ...

@pulumi.output_type
class FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItem(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        content_type: _builtins.str,
        format: _builtins.str,
        profile_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FieldLevelEncryptionConfigQueryArgProfileConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        forward_when_query_arg_profile_is_unknown: _builtins.bool,
        query_arg_profiles: Optional[
            outputs.FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="forwardWhenQueryArgProfileIsUnknown")
    def forward_when_query_arg_profile_is_unknown(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="queryArgProfiles")
    def query_arg_profiles(
        self,
    ) -> Optional[
        outputs.FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles
    ]: ...

@pulumi.output_type
class FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles(dict):
    def __init__(
        __self__,
        *,
        items: Optional[
            Sequence[
                outputs.FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItem
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        Sequence[
            outputs.FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItem
        ]
    ]: ...

@pulumi.output_type
class FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItem(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, profile_id: _builtins.str, query_arg: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryArg")
    def query_arg(self) -> _builtins.str: ...

@pulumi.output_type
class FieldLevelEncryptionProfileEncryptionEntities(dict):
    def __init__(
        __self__,
        *,
        items: Optional[
            Sequence[outputs.FieldLevelEncryptionProfileEncryptionEntitiesItem]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        Sequence[outputs.FieldLevelEncryptionProfileEncryptionEntitiesItem]
    ]: ...

@pulumi.output_type
class FieldLevelEncryptionProfileEncryptionEntitiesItem(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        field_patterns: outputs.FieldLevelEncryptionProfileEncryptionEntitiesItemFieldPatterns,
        provider_id: _builtins.str,
        public_key_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldPatterns")
    def field_patterns(
        self,
    ) -> outputs.FieldLevelEncryptionProfileEncryptionEntitiesItemFieldPatterns: ...
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicKeyId")
    def public_key_id(self) -> _builtins.str: ...

@pulumi.output_type
class FieldLevelEncryptionProfileEncryptionEntitiesItemFieldPatterns(dict):
    def __init__(
        __self__, *, items: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class KeyValueStoreTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KeyvaluestoreKeysExclusiveResourceKeyValuePair(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class MonitoringSubscriptionMonitoringSubscription(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        realtime_metrics_subscription_config: outputs.MonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="realtimeMetricsSubscriptionConfig")
    def realtime_metrics_subscription_config(
        self,
    ) -> outputs.MonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig: ...

@pulumi.output_type
class MonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, realtime_metrics_subscription_status: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="realtimeMetricsSubscriptionStatus")
    def realtime_metrics_subscription_status(self) -> _builtins.str: ...

@pulumi.output_type
class MultitenantDistributionActiveTrustedKeyGroup(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        items: Optional[
            Sequence[outputs.MultitenantDistributionActiveTrustedKeyGroupItem]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        Sequence[outputs.MultitenantDistributionActiveTrustedKeyGroupItem]
    ]: ...

@pulumi.output_type
class MultitenantDistributionActiveTrustedKeyGroupItem(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_group_id: Optional[_builtins.str] = ...,
        key_pair_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyGroupId")
    def key_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyPairIds")
    def key_pair_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class MultitenantDistributionCacheBehavior(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_methods: outputs.MultitenantDistributionCacheBehaviorAllowedMethods,
        path_pattern: _builtins.str,
        target_origin_id: _builtins.str,
        viewer_protocol_policy: _builtins.str,
        cache_policy_id: Optional[_builtins.str] = ...,
        compress: Optional[_builtins.bool] = ...,
        field_level_encryption_id: Optional[_builtins.str] = ...,
        function_associations: Optional[
            Sequence[outputs.MultitenantDistributionCacheBehaviorFunctionAssociation]
        ] = ...,
        lambda_function_associations: Optional[
            Sequence[
                outputs.MultitenantDistributionCacheBehaviorLambdaFunctionAssociation
            ]
        ] = ...,
        origin_request_policy_id: Optional[_builtins.str] = ...,
        realtime_log_config_arn: Optional[_builtins.str] = ...,
        response_headers_policy_id: Optional[_builtins.str] = ...,
        trusted_key_groups: Optional[
            outputs.MultitenantDistributionCacheBehaviorTrustedKeyGroups
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(
        self,
    ) -> outputs.MultitenantDistributionCacheBehaviorAllowedMethods: ...
    @_builtins.property
    @pulumi.getter(name="pathPattern")
    def path_pattern(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetOriginId")
    def target_origin_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="viewerProtocolPolicy")
    def viewer_protocol_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cachePolicyId")
    def cache_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def compress(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="fieldLevelEncryptionId")
    def field_level_encryption_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="functionAssociations")
    def function_associations(
        self,
    ) -> Optional[
        Sequence[outputs.MultitenantDistributionCacheBehaviorFunctionAssociation]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionAssociations")
    def lambda_function_associations(
        self,
    ) -> Optional[
        Sequence[outputs.MultitenantDistributionCacheBehaviorLambdaFunctionAssociation]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="originRequestPolicyId")
    def origin_request_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="realtimeLogConfigArn")
    def realtime_log_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responseHeadersPolicyId")
    def response_headers_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trustedKeyGroups")
    def trusted_key_groups(
        self,
    ) -> Optional[outputs.MultitenantDistributionCacheBehaviorTrustedKeyGroups]: ...

@pulumi.output_type
class MultitenantDistributionCacheBehaviorAllowedMethods(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cached_methods: Sequence[_builtins.str],
        items: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachedMethods")
    def cached_methods(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class MultitenantDistributionCacheBehaviorFunctionAssociation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, event_type: _builtins.str, function_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> _builtins.str: ...

@pulumi.output_type
class MultitenantDistributionCacheBehaviorLambdaFunctionAssociation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_type: _builtins.str,
        lambda_function_arn: _builtins.str,
        include_body: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeBody")
    def include_body(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MultitenantDistributionCacheBehaviorTrustedKeyGroups(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        items: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class MultitenantDistributionCustomErrorResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_code: _builtins.int,
        error_caching_min_ttl: Optional[_builtins.int] = ...,
        response_code: Optional[_builtins.str] = ...,
        response_page_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="errorCachingMinTtl")
    def error_caching_min_ttl(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responsePagePath")
    def response_page_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MultitenantDistributionDefaultCacheBehavior(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_methods: outputs.MultitenantDistributionDefaultCacheBehaviorAllowedMethods,
        target_origin_id: _builtins.str,
        viewer_protocol_policy: _builtins.str,
        cache_policy_id: Optional[_builtins.str] = ...,
        compress: Optional[_builtins.bool] = ...,
        field_level_encryption_id: Optional[_builtins.str] = ...,
        function_associations: Optional[
            Sequence[
                outputs.MultitenantDistributionDefaultCacheBehaviorFunctionAssociation
            ]
        ] = ...,
        lambda_function_associations: Optional[
            Sequence[
                outputs.MultitenantDistributionDefaultCacheBehaviorLambdaFunctionAssociation
            ]
        ] = ...,
        origin_request_policy_id: Optional[_builtins.str] = ...,
        realtime_log_config_arn: Optional[_builtins.str] = ...,
        response_headers_policy_id: Optional[_builtins.str] = ...,
        trusted_key_groups: Optional[
            outputs.MultitenantDistributionDefaultCacheBehaviorTrustedKeyGroups
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(
        self,
    ) -> outputs.MultitenantDistributionDefaultCacheBehaviorAllowedMethods: ...
    @_builtins.property
    @pulumi.getter(name="targetOriginId")
    def target_origin_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="viewerProtocolPolicy")
    def viewer_protocol_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cachePolicyId")
    def cache_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def compress(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="fieldLevelEncryptionId")
    def field_level_encryption_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="functionAssociations")
    def function_associations(
        self,
    ) -> Optional[
        Sequence[outputs.MultitenantDistributionDefaultCacheBehaviorFunctionAssociation]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionAssociations")
    def lambda_function_associations(
        self,
    ) -> Optional[
        Sequence[
            outputs.MultitenantDistributionDefaultCacheBehaviorLambdaFunctionAssociation
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="originRequestPolicyId")
    def origin_request_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="realtimeLogConfigArn")
    def realtime_log_config_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responseHeadersPolicyId")
    def response_headers_policy_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trustedKeyGroups")
    def trusted_key_groups(
        self,
    ) -> Optional[
        outputs.MultitenantDistributionDefaultCacheBehaviorTrustedKeyGroups
    ]: ...

@pulumi.output_type
class MultitenantDistributionDefaultCacheBehaviorAllowedMethods(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cached_methods: Sequence[_builtins.str],
        items: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cachedMethods")
    def cached_methods(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class MultitenantDistributionDefaultCacheBehaviorFunctionAssociation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, event_type: _builtins.str, function_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> _builtins.str: ...

@pulumi.output_type
class MultitenantDistributionDefaultCacheBehaviorLambdaFunctionAssociation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event_type: _builtins.str,
        lambda_function_arn: _builtins.str,
        include_body: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeBody")
    def include_body(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MultitenantDistributionDefaultCacheBehaviorTrustedKeyGroups(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        items: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class MultitenantDistributionOrigin(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_name: _builtins.str,
        id: _builtins.str,
        connection_attempts: Optional[_builtins.int] = ...,
        connection_timeout: Optional[_builtins.int] = ...,
        custom_headers: Optional[
            Sequence[outputs.MultitenantDistributionOriginCustomHeader]
        ] = ...,
        custom_origin_configs: Optional[
            Sequence[outputs.MultitenantDistributionOriginCustomOriginConfig]
        ] = ...,
        origin_access_control_id: Optional[_builtins.str] = ...,
        origin_path: Optional[_builtins.str] = ...,
        origin_shields: Optional[
            Sequence[outputs.MultitenantDistributionOriginOriginShield]
        ] = ...,
        response_completion_timeout: Optional[_builtins.int] = ...,
        vpc_origin_configs: Optional[
            Sequence[outputs.MultitenantDistributionOriginVpcOriginConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionAttempts")
    def connection_attempts(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="connectionTimeout")
    def connection_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(
        self,
    ) -> Optional[Sequence[outputs.MultitenantDistributionOriginCustomHeader]]: ...
    @_builtins.property
    @pulumi.getter(name="customOriginConfigs")
    def custom_origin_configs(
        self,
    ) -> Optional[
        Sequence[outputs.MultitenantDistributionOriginCustomOriginConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="originAccessControlId")
    def origin_access_control_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originShields")
    def origin_shields(
        self,
    ) -> Optional[Sequence[outputs.MultitenantDistributionOriginOriginShield]]: ...
    @_builtins.property
    @pulumi.getter(name="responseCompletionTimeout")
    def response_completion_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="vpcOriginConfigs")
    def vpc_origin_configs(
        self,
    ) -> Optional[Sequence[outputs.MultitenantDistributionOriginVpcOriginConfig]]: ...

@pulumi.output_type
class MultitenantDistributionOriginCustomHeader(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, header_name: _builtins.str, header_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> _builtins.str: ...

@pulumi.output_type
class MultitenantDistributionOriginCustomOriginConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        http_port: _builtins.int,
        https_port: _builtins.int,
        origin_protocol_policy: _builtins.str,
        origin_ssl_protocols: Sequence[_builtins.str],
        ip_address_type: Optional[_builtins.str] = ...,
        origin_keepalive_timeout: Optional[_builtins.int] = ...,
        origin_read_timeout: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="originProtocolPolicy")
    def origin_protocol_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="originSslProtocols")
    def origin_ssl_protocols(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originKeepaliveTimeout")
    def origin_keepalive_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="originReadTimeout")
    def origin_read_timeout(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class MultitenantDistributionOriginGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        failover_criteria: outputs.MultitenantDistributionOriginGroupFailoverCriteria,
        id: _builtins.str,
        members: Sequence[outputs.MultitenantDistributionOriginGroupMember],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failoverCriteria")
    def failover_criteria(
        self,
    ) -> outputs.MultitenantDistributionOriginGroupFailoverCriteria: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def members(self) -> Sequence[outputs.MultitenantDistributionOriginGroupMember]: ...

@pulumi.output_type
class MultitenantDistributionOriginGroupFailoverCriteria(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, status_codes: Sequence[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="statusCodes")
    def status_codes(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class MultitenantDistributionOriginGroupMember(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, origin_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="originId")
    def origin_id(self) -> _builtins.str: ...

@pulumi.output_type
class MultitenantDistributionOriginOriginShield(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        origin_shield_region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="originShieldRegion")
    def origin_shield_region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MultitenantDistributionOriginVpcOriginConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        vpc_origin_id: _builtins.str,
        origin_keepalive_timeout: Optional[_builtins.int] = ...,
        origin_read_timeout: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcOriginId")
    def vpc_origin_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="originKeepaliveTimeout")
    def origin_keepalive_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="originReadTimeout")
    def origin_read_timeout(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class MultitenantDistributionRestrictions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        geo_restriction: outputs.MultitenantDistributionRestrictionsGeoRestriction,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="geoRestriction")
    def geo_restriction(
        self,
    ) -> outputs.MultitenantDistributionRestrictionsGeoRestriction: ...

@pulumi.output_type
class MultitenantDistributionRestrictionsGeoRestriction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        restriction_type: _builtins.str,
        items: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="restrictionType")
    def restriction_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class MultitenantDistributionTenantConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        parameter_definitions: Optional[
            Sequence[outputs.MultitenantDistributionTenantConfigParameterDefinition]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="parameterDefinitions")
    def parameter_definitions(
        self,
    ) -> Optional[
        Sequence[outputs.MultitenantDistributionTenantConfigParameterDefinition]
    ]: ...

@pulumi.output_type
class MultitenantDistributionTenantConfigParameterDefinition(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        definitions: Optional[
            Sequence[
                outputs.MultitenantDistributionTenantConfigParameterDefinitionDefinition
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def definitions(
        self,
    ) -> Optional[
        Sequence[
            outputs.MultitenantDistributionTenantConfigParameterDefinitionDefinition
        ]
    ]: ...

@pulumi.output_type
class MultitenantDistributionTenantConfigParameterDefinitionDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        string_schemas: Optional[
            Sequence[
                outputs.MultitenantDistributionTenantConfigParameterDefinitionDefinitionStringSchema
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stringSchemas")
    def string_schemas(
        self,
    ) -> Optional[
        Sequence[
            outputs.MultitenantDistributionTenantConfigParameterDefinitionDefinitionStringSchema
        ]
    ]: ...

@pulumi.output_type
class MultitenantDistributionTenantConfigParameterDefinitionDefinitionStringSchema(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        required: _builtins.bool,
        comment: Optional[_builtins.str] = ...,
        default_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MultitenantDistributionTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MultitenantDistributionViewerCertificate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        acm_certificate_arn: Optional[_builtins.str] = ...,
        cloudfront_default_certificate: Optional[_builtins.bool] = ...,
        minimum_protocol_version: Optional[_builtins.str] = ...,
        ssl_support_method: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acmCertificateArn")
    def acm_certificate_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudfrontDefaultCertificate")
    def cloudfront_default_certificate(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="minimumProtocolVersion")
    def minimum_protocol_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslSupportMethod")
    def ssl_support_method(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OriginRequestPolicyCookiesConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cookie_behavior: _builtins.str,
        cookies: Optional[outputs.OriginRequestPolicyCookiesConfigCookies] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cookieBehavior")
    def cookie_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.OriginRequestPolicyCookiesConfigCookies]: ...

@pulumi.output_type
class OriginRequestPolicyCookiesConfigCookies(dict):
    def __init__(
        __self__, *, items: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OriginRequestPolicyHeadersConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        header_behavior: Optional[_builtins.str] = ...,
        headers: Optional[outputs.OriginRequestPolicyHeadersConfigHeaders] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerBehavior")
    def header_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[outputs.OriginRequestPolicyHeadersConfigHeaders]: ...

@pulumi.output_type
class OriginRequestPolicyHeadersConfigHeaders(dict):
    def __init__(
        __self__, *, items: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OriginRequestPolicyQueryStringsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        query_string_behavior: _builtins.str,
        query_strings: Optional[
            outputs.OriginRequestPolicyQueryStringsConfigQueryStrings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryStringBehavior")
    def query_string_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(
        self,
    ) -> Optional[outputs.OriginRequestPolicyQueryStringsConfigQueryStrings]: ...

@pulumi.output_type
class OriginRequestPolicyQueryStringsConfigQueryStrings(dict):
    def __init__(
        __self__, *, items: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RealtimeLogConfigEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kinesis_stream_config: outputs.RealtimeLogConfigEndpointKinesisStreamConfig,
        stream_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kinesisStreamConfig")
    def kinesis_stream_config(
        self,
    ) -> outputs.RealtimeLogConfigEndpointKinesisStreamConfig: ...
    @_builtins.property
    @pulumi.getter(name="streamType")
    def stream_type(self) -> _builtins.str: ...

@pulumi.output_type
class RealtimeLogConfigEndpointKinesisStreamConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, role_arn: _builtins.str, stream_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> _builtins.str: ...

@pulumi.output_type
class ResponseHeadersPolicyCorsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_control_allow_credentials: _builtins.bool,
        access_control_allow_headers: outputs.ResponseHeadersPolicyCorsConfigAccessControlAllowHeaders,
        access_control_allow_methods: outputs.ResponseHeadersPolicyCorsConfigAccessControlAllowMethods,
        access_control_allow_origins: outputs.ResponseHeadersPolicyCorsConfigAccessControlAllowOrigins,
        origin_override: _builtins.bool,
        access_control_expose_headers: Optional[
            outputs.ResponseHeadersPolicyCorsConfigAccessControlExposeHeaders
        ] = ...,
        access_control_max_age_sec: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessControlAllowCredentials")
    def access_control_allow_credentials(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="accessControlAllowHeaders")
    def access_control_allow_headers(
        self,
    ) -> outputs.ResponseHeadersPolicyCorsConfigAccessControlAllowHeaders: ...
    @_builtins.property
    @pulumi.getter(name="accessControlAllowMethods")
    def access_control_allow_methods(
        self,
    ) -> outputs.ResponseHeadersPolicyCorsConfigAccessControlAllowMethods: ...
    @_builtins.property
    @pulumi.getter(name="accessControlAllowOrigins")
    def access_control_allow_origins(
        self,
    ) -> outputs.ResponseHeadersPolicyCorsConfigAccessControlAllowOrigins: ...
    @_builtins.property
    @pulumi.getter(name="originOverride")
    def origin_override(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="accessControlExposeHeaders")
    def access_control_expose_headers(
        self,
    ) -> Optional[
        outputs.ResponseHeadersPolicyCorsConfigAccessControlExposeHeaders
    ]: ...
    @_builtins.property
    @pulumi.getter(name="accessControlMaxAgeSec")
    def access_control_max_age_sec(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ResponseHeadersPolicyCorsConfigAccessControlAllowHeaders(dict):
    def __init__(
        __self__, *, items: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ResponseHeadersPolicyCorsConfigAccessControlAllowMethods(dict):
    def __init__(
        __self__, *, items: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ResponseHeadersPolicyCorsConfigAccessControlAllowOrigins(dict):
    def __init__(
        __self__, *, items: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ResponseHeadersPolicyCorsConfigAccessControlExposeHeaders(dict):
    def __init__(
        __self__, *, items: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ResponseHeadersPolicyCustomHeadersConfig(dict):
    def __init__(
        __self__,
        *,
        items: Optional[
            Sequence[outputs.ResponseHeadersPolicyCustomHeadersConfigItem]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[Sequence[outputs.ResponseHeadersPolicyCustomHeadersConfigItem]]: ...

@pulumi.output_type
class ResponseHeadersPolicyCustomHeadersConfigItem(dict):
    def __init__(
        __self__,
        *,
        header: _builtins.str,
        override: _builtins.bool,
        value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def header(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ResponseHeadersPolicyRemoveHeadersConfig(dict):
    def __init__(
        __self__,
        *,
        items: Optional[
            Sequence[outputs.ResponseHeadersPolicyRemoveHeadersConfigItem]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[Sequence[outputs.ResponseHeadersPolicyRemoveHeadersConfigItem]]: ...

@pulumi.output_type
class ResponseHeadersPolicyRemoveHeadersConfigItem(dict):
    def __init__(__self__, *, header: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def header(self) -> _builtins.str: ...

@pulumi.output_type
class ResponseHeadersPolicySecurityHeadersConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        content_security_policy: Optional[
            outputs.ResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy
        ] = ...,
        content_type_options: Optional[
            outputs.ResponseHeadersPolicySecurityHeadersConfigContentTypeOptions
        ] = ...,
        frame_options: Optional[
            outputs.ResponseHeadersPolicySecurityHeadersConfigFrameOptions
        ] = ...,
        referrer_policy: Optional[
            outputs.ResponseHeadersPolicySecurityHeadersConfigReferrerPolicy
        ] = ...,
        strict_transport_security: Optional[
            outputs.ResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity
        ] = ...,
        xss_protection: Optional[
            outputs.ResponseHeadersPolicySecurityHeadersConfigXssProtection
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentSecurityPolicy")
    def content_security_policy(
        self,
    ) -> Optional[
        outputs.ResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy
    ]: ...
    @_builtins.property
    @pulumi.getter(name="contentTypeOptions")
    def content_type_options(
        self,
    ) -> Optional[
        outputs.ResponseHeadersPolicySecurityHeadersConfigContentTypeOptions
    ]: ...
    @_builtins.property
    @pulumi.getter(name="frameOptions")
    def frame_options(
        self,
    ) -> Optional[outputs.ResponseHeadersPolicySecurityHeadersConfigFrameOptions]: ...
    @_builtins.property
    @pulumi.getter(name="referrerPolicy")
    def referrer_policy(
        self,
    ) -> Optional[outputs.ResponseHeadersPolicySecurityHeadersConfigReferrerPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="strictTransportSecurity")
    def strict_transport_security(
        self,
    ) -> Optional[
        outputs.ResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity
    ]: ...
    @_builtins.property
    @pulumi.getter(name="xssProtection")
    def xss_protection(
        self,
    ) -> Optional[outputs.ResponseHeadersPolicySecurityHeadersConfigXssProtection]: ...

@pulumi.output_type
class ResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, content_security_policy: _builtins.str, override: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentSecurityPolicy")
    def content_security_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...

@pulumi.output_type
class ResponseHeadersPolicySecurityHeadersConfigContentTypeOptions(dict):
    def __init__(__self__, *, override: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...

@pulumi.output_type
class ResponseHeadersPolicySecurityHeadersConfigFrameOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, frame_option: _builtins.str, override: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="frameOption")
    def frame_option(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...

@pulumi.output_type
class ResponseHeadersPolicySecurityHeadersConfigReferrerPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, override: _builtins.bool, referrer_policy: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="referrerPolicy")
    def referrer_policy(self) -> _builtins.str: ...

@pulumi.output_type
class ResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_control_max_age_sec: _builtins.int,
        override: _builtins.bool,
        include_subdomains: Optional[_builtins.bool] = ...,
        preload: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessControlMaxAgeSec")
    def access_control_max_age_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="includeSubdomains")
    def include_subdomains(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def preload(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ResponseHeadersPolicySecurityHeadersConfigXssProtection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        override: _builtins.bool,
        protection: _builtins.bool,
        mode_block: Optional[_builtins.bool] = ...,
        report_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="modeBlock")
    def mode_block(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="reportUri")
    def report_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResponseHeadersPolicyServerTimingHeadersConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enabled: _builtins.bool, sampling_rate: _builtins.float
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> _builtins.float: ...

@pulumi.output_type
class TrustStoreCaCertificatesBundleSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ca_certificates_bundle_s3_location: outputs.TrustStoreCaCertificatesBundleSourceCaCertificatesBundleS3Location,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleS3Location")
    def ca_certificates_bundle_s3_location(
        self,
    ) -> outputs.TrustStoreCaCertificatesBundleSourceCaCertificatesBundleS3Location: ...

@pulumi.output_type
class TrustStoreCaCertificatesBundleSourceCaCertificatesBundleS3Location(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        key: _builtins.str,
        region: _builtins.str,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrustStoreTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VpcOriginTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VpcOriginVpcOriginEndpointConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        http_port: _builtins.int,
        https_port: _builtins.int,
        name: _builtins.str,
        origin_protocol_policy: _builtins.str,
        origin_ssl_protocols: outputs.VpcOriginVpcOriginEndpointConfigOriginSslProtocols,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="originProtocolPolicy")
    def origin_protocol_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="originSslProtocols")
    def origin_ssl_protocols(
        self,
    ) -> outputs.VpcOriginVpcOriginEndpointConfigOriginSslProtocols: ...

@pulumi.output_type
class VpcOriginVpcOriginEndpointConfigOriginSslProtocols(dict):
    def __init__(
        __self__, *, items: Sequence[_builtins.str], quantity: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def quantity(self) -> _builtins.int: ...

@pulumi.output_type
class GetCachePolicyParametersInCacheKeyAndForwardedToOriginResult(dict):
    def __init__(
        __self__,
        *,
        cookies_configs: Sequence[
            outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigResult
        ],
        enable_accept_encoding_brotli: _builtins.bool,
        enable_accept_encoding_gzip: _builtins.bool,
        headers_configs: Sequence[
            outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigResult
        ],
        query_strings_configs: Sequence[
            outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cookiesConfigs")
    def cookies_configs(
        self,
    ) -> Sequence[
        outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableAcceptEncodingBrotli")
    def enable_accept_encoding_brotli(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableAcceptEncodingGzip")
    def enable_accept_encoding_gzip(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="headersConfigs")
    def headers_configs(
        self,
    ) -> Sequence[
        outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="queryStringsConfigs")
    def query_strings_configs(
        self,
    ) -> Sequence[
        outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigResult
    ]: ...

@pulumi.output_type
class GetCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigResult(dict):
    def __init__(
        __self__,
        *,
        cookie_behavior: _builtins.str,
        cookies: Sequence[
            outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookieResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cookieBehavior")
    def cookie_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cookies(
        self,
    ) -> Sequence[
        outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookieResult
    ]: ...

@pulumi.output_type
class GetCachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookieResult(
    dict
):
    def __init__(__self__, *, items: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigResult(dict):
    def __init__(
        __self__,
        *,
        header_behavior: _builtins.str,
        headers: Sequence[
            outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaderResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerBehavior")
    def header_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Sequence[
        outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaderResult
    ]: ...

@pulumi.output_type
class GetCachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeaderResult(
    dict
):
    def __init__(__self__, *, items: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigResult(
    dict
):
    def __init__(
        __self__,
        *,
        query_string_behavior: _builtins.str,
        query_strings: Sequence[
            outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryStringBehavior")
    def query_string_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(
        self,
    ) -> Sequence[
        outputs.GetCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringResult
    ]: ...

@pulumi.output_type
class GetCachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringResult(
    dict
):
    def __init__(__self__, *, items: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetDistributionTenantCustomizationResult(dict):
    def __init__(
        __self__,
        *,
        certificates: Sequence[
            outputs.GetDistributionTenantCustomizationCertificateResult
        ],
        geo_restrictions: Sequence[
            outputs.GetDistributionTenantCustomizationGeoRestrictionResult
        ],
        web_acls: Sequence[outputs.GetDistributionTenantCustomizationWebAclResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> Sequence[outputs.GetDistributionTenantCustomizationCertificateResult]: ...
    @_builtins.property
    @pulumi.getter(name="geoRestrictions")
    def geo_restrictions(
        self,
    ) -> Sequence[outputs.GetDistributionTenantCustomizationGeoRestrictionResult]: ...
    @_builtins.property
    @pulumi.getter(name="webAcls")
    def web_acls(
        self,
    ) -> Sequence[outputs.GetDistributionTenantCustomizationWebAclResult]: ...

@pulumi.output_type
class GetDistributionTenantCustomizationCertificateResult(dict):
    def __init__(__self__, *, arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetDistributionTenantCustomizationGeoRestrictionResult(dict):
    def __init__(
        __self__, *, locations: Sequence[_builtins.str], restriction_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restrictionType")
    def restriction_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetDistributionTenantCustomizationWebAclResult(dict):
    def __init__(__self__, *, action: _builtins.str, arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetDistributionTenantDomainResult(dict):
    def __init__(__self__, *, domain: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetDistributionTenantManagedCertificateRequestResult(dict):
    def __init__(
        __self__,
        *,
        certificate_transparency_logging_preference: _builtins.str,
        primary_domain_name: _builtins.str,
        validation_token_host: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateTransparencyLoggingPreference")
    def certificate_transparency_logging_preference(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryDomainName")
    def primary_domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="validationTokenHost")
    def validation_token_host(self) -> _builtins.str: ...

@pulumi.output_type
class GetDistributionTenantParameterResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetOriginRequestPolicyCookiesConfigResult(dict):
    def __init__(
        __self__,
        *,
        cookie_behavior: _builtins.str,
        cookies: Sequence[outputs.GetOriginRequestPolicyCookiesConfigCookieResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cookieBehavior")
    def cookie_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cookies(
        self,
    ) -> Sequence[outputs.GetOriginRequestPolicyCookiesConfigCookieResult]: ...

@pulumi.output_type
class GetOriginRequestPolicyCookiesConfigCookieResult(dict):
    def __init__(__self__, *, items: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetOriginRequestPolicyHeadersConfigResult(dict):
    def __init__(
        __self__,
        *,
        header_behavior: _builtins.str,
        headers: Sequence[outputs.GetOriginRequestPolicyHeadersConfigHeaderResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerBehavior")
    def header_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Sequence[outputs.GetOriginRequestPolicyHeadersConfigHeaderResult]: ...

@pulumi.output_type
class GetOriginRequestPolicyHeadersConfigHeaderResult(dict):
    def __init__(__self__, *, items: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetOriginRequestPolicyQueryStringsConfigResult(dict):
    def __init__(
        __self__,
        *,
        query_string_behavior: _builtins.str,
        query_strings: Sequence[
            outputs.GetOriginRequestPolicyQueryStringsConfigQueryStringResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryStringBehavior")
    def query_string_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(
        self,
    ) -> Sequence[
        outputs.GetOriginRequestPolicyQueryStringsConfigQueryStringResult
    ]: ...

@pulumi.output_type
class GetOriginRequestPolicyQueryStringsConfigQueryStringResult(dict):
    def __init__(__self__, *, items: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetRealtimeLogConfigEndpointResult(dict):
    def __init__(
        __self__,
        *,
        kinesis_stream_configs: Sequence[
            outputs.GetRealtimeLogConfigEndpointKinesisStreamConfigResult
        ],
        stream_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kinesisStreamConfigs")
    def kinesis_stream_configs(
        self,
    ) -> Sequence[outputs.GetRealtimeLogConfigEndpointKinesisStreamConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="streamType")
    def stream_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetRealtimeLogConfigEndpointKinesisStreamConfigResult(dict):
    def __init__(
        __self__, *, role_arn: _builtins.str, stream_arn: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetResponseHeadersPolicyCorsConfigResult(dict):
    def __init__(
        __self__,
        *,
        access_control_allow_credentials: _builtins.bool,
        access_control_allow_headers: Sequence[
            outputs.GetResponseHeadersPolicyCorsConfigAccessControlAllowHeaderResult
        ],
        access_control_allow_methods: Sequence[
            outputs.GetResponseHeadersPolicyCorsConfigAccessControlAllowMethodResult
        ],
        access_control_allow_origins: Sequence[
            outputs.GetResponseHeadersPolicyCorsConfigAccessControlAllowOriginResult
        ],
        access_control_expose_headers: Sequence[
            outputs.GetResponseHeadersPolicyCorsConfigAccessControlExposeHeaderResult
        ],
        access_control_max_age_sec: _builtins.int,
        origin_override: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessControlAllowCredentials")
    def access_control_allow_credentials(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="accessControlAllowHeaders")
    def access_control_allow_headers(
        self,
    ) -> Sequence[
        outputs.GetResponseHeadersPolicyCorsConfigAccessControlAllowHeaderResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="accessControlAllowMethods")
    def access_control_allow_methods(
        self,
    ) -> Sequence[
        outputs.GetResponseHeadersPolicyCorsConfigAccessControlAllowMethodResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="accessControlAllowOrigins")
    def access_control_allow_origins(
        self,
    ) -> Sequence[
        outputs.GetResponseHeadersPolicyCorsConfigAccessControlAllowOriginResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="accessControlExposeHeaders")
    def access_control_expose_headers(
        self,
    ) -> Sequence[
        outputs.GetResponseHeadersPolicyCorsConfigAccessControlExposeHeaderResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="accessControlMaxAgeSec")
    def access_control_max_age_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="originOverride")
    def origin_override(self) -> _builtins.bool: ...

@pulumi.output_type
class GetResponseHeadersPolicyCorsConfigAccessControlAllowHeaderResult(dict):
    def __init__(__self__, *, items: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetResponseHeadersPolicyCorsConfigAccessControlAllowMethodResult(dict):
    def __init__(__self__, *, items: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetResponseHeadersPolicyCorsConfigAccessControlAllowOriginResult(dict):
    def __init__(__self__, *, items: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetResponseHeadersPolicyCorsConfigAccessControlExposeHeaderResult(dict):
    def __init__(__self__, *, items: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetResponseHeadersPolicyCustomHeadersConfigResult(dict):
    def __init__(
        __self__,
        *,
        items: Sequence[outputs.GetResponseHeadersPolicyCustomHeadersConfigItemResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Sequence[outputs.GetResponseHeadersPolicyCustomHeadersConfigItemResult]: ...

@pulumi.output_type
class GetResponseHeadersPolicyCustomHeadersConfigItemResult(dict):
    def __init__(
        __self__,
        *,
        header: _builtins.str,
        override: _builtins.bool,
        value: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def header(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetResponseHeadersPolicyRemoveHeadersConfigResult(dict):
    def __init__(
        __self__,
        *,
        items: Sequence[outputs.GetResponseHeadersPolicyRemoveHeadersConfigItemResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Sequence[outputs.GetResponseHeadersPolicyRemoveHeadersConfigItemResult]: ...

@pulumi.output_type
class GetResponseHeadersPolicyRemoveHeadersConfigItemResult(dict):
    def __init__(__self__, *, header: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def header(self) -> _builtins.str: ...

@pulumi.output_type
class GetResponseHeadersPolicySecurityHeadersConfigResult(dict):
    def __init__(
        __self__,
        *,
        content_security_policies: Sequence[
            outputs.GetResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyResult
        ],
        content_type_options: Sequence[
            outputs.GetResponseHeadersPolicySecurityHeadersConfigContentTypeOptionResult
        ],
        frame_options: Sequence[
            outputs.GetResponseHeadersPolicySecurityHeadersConfigFrameOptionResult
        ],
        referrer_policies: Sequence[
            outputs.GetResponseHeadersPolicySecurityHeadersConfigReferrerPolicyResult
        ],
        strict_transport_securities: Sequence[
            outputs.GetResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityResult
        ],
        xss_protections: Sequence[
            outputs.GetResponseHeadersPolicySecurityHeadersConfigXssProtectionResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentSecurityPolicies")
    def content_security_policies(
        self,
    ) -> Sequence[
        outputs.GetResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="contentTypeOptions")
    def content_type_options(
        self,
    ) -> Sequence[
        outputs.GetResponseHeadersPolicySecurityHeadersConfigContentTypeOptionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="frameOptions")
    def frame_options(
        self,
    ) -> Sequence[
        outputs.GetResponseHeadersPolicySecurityHeadersConfigFrameOptionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="referrerPolicies")
    def referrer_policies(
        self,
    ) -> Sequence[
        outputs.GetResponseHeadersPolicySecurityHeadersConfigReferrerPolicyResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="strictTransportSecurities")
    def strict_transport_securities(
        self,
    ) -> Sequence[
        outputs.GetResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="xssProtections")
    def xss_protections(
        self,
    ) -> Sequence[
        outputs.GetResponseHeadersPolicySecurityHeadersConfigXssProtectionResult
    ]: ...

@pulumi.output_type
class GetResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyResult(dict):
    def __init__(
        __self__, *, content_security_policy: _builtins.str, override: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentSecurityPolicy")
    def content_security_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...

@pulumi.output_type
class GetResponseHeadersPolicySecurityHeadersConfigContentTypeOptionResult(dict):
    def __init__(__self__, *, override: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...

@pulumi.output_type
class GetResponseHeadersPolicySecurityHeadersConfigFrameOptionResult(dict):
    def __init__(
        __self__, *, frame_option: _builtins.str, override: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="frameOption")
    def frame_option(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...

@pulumi.output_type
class GetResponseHeadersPolicySecurityHeadersConfigReferrerPolicyResult(dict):
    def __init__(
        __self__, *, override: _builtins.bool, referrer_policy: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="referrerPolicy")
    def referrer_policy(self) -> _builtins.str: ...

@pulumi.output_type
class GetResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityResult(dict):
    def __init__(
        __self__,
        *,
        access_control_max_age_sec: _builtins.int,
        include_subdomains: _builtins.bool,
        override: _builtins.bool,
        preload: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessControlMaxAgeSec")
    def access_control_max_age_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="includeSubdomains")
    def include_subdomains(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def preload(self) -> _builtins.bool: ...

@pulumi.output_type
class GetResponseHeadersPolicySecurityHeadersConfigXssProtectionResult(dict):
    def __init__(
        __self__,
        *,
        mode_block: _builtins.bool,
        override: _builtins.bool,
        protection: _builtins.bool,
        report_uri: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modeBlock")
    def mode_block(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def override(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def protection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="reportUri")
    def report_uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetResponseHeadersPolicyServerTimingHeadersConfigResult(dict):
    def __init__(
        __self__, *, enabled: _builtins.bool, sampling_rate: _builtins.float
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> _builtins.float: ...
