import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AFDDomainHttpsCustomizedCipherSuiteSetResponse",
    "AFDDomainHttpsParametersResponse",
    "ActivatedResourceReferenceResponse",
    "AfdRouteCacheConfigurationResponse",
    "AgentPathResponse",
    ...,
    "CacheConfigurationResponse",
    "CacheExpirationActionParametersResponse",
    "CacheKeyQueryStringActionParametersResponse",
    "CdnCertificateSourceParametersResponse",
    "CdnEndpointResponse",
    "CdnManagedHttpsParametersResponse",
    "ClientPortMatchConditionParametersResponse",
    "CompressionSettingsResponse",
    "CookiesMatchConditionParametersResponse",
    "CustomRuleListResponse",
    "CustomRuleResponse",
    "CustomerCertificateParametersResponse",
    "DeepCreatedCustomDomainResponse",
    "DeepCreatedOriginGroupResponse",
    "DeepCreatedOriginResponse",
    "DeliveryRuleCacheExpirationActionResponse",
    "DeliveryRuleCacheKeyQueryStringActionResponse",
    "DeliveryRuleClientPortConditionResponse",
    "DeliveryRuleCookiesConditionResponse",
    "DeliveryRuleHostNameConditionResponse",
    "DeliveryRuleHttpVersionConditionResponse",
    "DeliveryRuleIsDeviceConditionResponse",
    "DeliveryRulePostArgsConditionResponse",
    "DeliveryRuleQueryStringConditionResponse",
    "DeliveryRuleRemoteAddressConditionResponse",
    "DeliveryRuleRequestBodyConditionResponse",
    "DeliveryRuleRequestHeaderActionResponse",
    "DeliveryRuleRequestHeaderConditionResponse",
    "DeliveryRuleRequestMethodConditionResponse",
    "DeliveryRuleRequestSchemeConditionResponse",
    "DeliveryRuleRequestUriConditionResponse",
    "DeliveryRuleResponse",
    "DeliveryRuleResponseHeaderActionResponse",
    ...,
    "DeliveryRuleServerPortConditionResponse",
    "DeliveryRuleSocketAddrConditionResponse",
    "DeliveryRuleSslProtocolConditionResponse",
    "DeliveryRuleUrlFileExtensionConditionResponse",
    "DeliveryRuleUrlFileNameConditionResponse",
    "DeliveryRuleUrlPathConditionResponse",
    "DomainValidationPropertiesResponse",
    "EdgeActionAttachmentResponse",
    ...,
    ...,
    "GeoFilterResponse",
    "HeaderActionParametersResponse",
    "HealthProbeParametersResponse",
    "HostNameMatchConditionParametersResponse",
    "HttpErrorRangeParametersResponse",
    "HttpVersionMatchConditionParametersResponse",
    "IsDeviceMatchConditionParametersResponse",
    "KeyVaultCertificateSourceParametersResponse",
    "KeyVaultSigningKeyParametersResponse",
    "LoadBalancingSettingsParametersResponse",
    "ManagedCertificateParametersResponse",
    "ManagedRuleGroupOverrideResponse",
    "ManagedRuleOverrideResponse",
    "ManagedRuleSetListResponse",
    "ManagedRuleSetResponse",
    "ManagedServiceIdentityResponse",
    "MatchConditionResponse",
    "OriginAuthenticationPropertiesResponse",
    "OriginGroupOverrideActionParametersResponse",
    "OriginGroupOverrideActionResponse",
    "OriginGroupOverrideResponse",
    "PolicySettingsResponse",
    "PostArgsMatchConditionParametersResponse",
    "ProfileLogScrubbingResponse",
    "ProfileScrubbingRulesResponse",
    "QueryStringMatchConditionParametersResponse",
    "RateLimitRuleListResponse",
    "RateLimitRuleResponse",
    "RemoteAddressMatchConditionParametersResponse",
    "RequestBodyMatchConditionParametersResponse",
    "RequestHeaderMatchConditionParametersResponse",
    "RequestMethodMatchConditionParametersResponse",
    "RequestSchemeMatchConditionParametersResponse",
    "RequestUriMatchConditionParametersResponse",
    "ResourceReferenceResponse",
    ...,
    "RouteConfigurationOverrideActionParametersResponse",
    ...,
    ...,
    "ServerPortMatchConditionParametersResponse",
    "SharedPrivateLinkResourcePropertiesResponse",
    "SkuResponse",
    "SkuTypeResponse",
    "SocketAddrMatchConditionParametersResponse",
    "SslProtocolMatchConditionParametersResponse",
    "SystemDataResponse",
    "TargetEndpointResponse",
    "UrlFileExtensionMatchConditionParametersResponse",
    "UrlFileNameMatchConditionParametersResponse",
    "UrlPathMatchConditionParametersResponse",
    "UrlRedirectActionParametersResponse",
    "UrlRedirectActionResponse",
    "UrlRewriteActionParametersResponse",
    "UrlRewriteActionResponse",
    "UrlSigningActionParametersResponse",
    "UrlSigningActionResponse",
    "UrlSigningKeyParametersResponse",
    "UrlSigningKeyResponse",
    "UrlSigningParamIdentifierResponse",
    "UserAssignedIdentityResponse",
    "UserManagedHttpsParametersResponse",
]

@pulumi.output_type
class AFDDomainHttpsCustomizedCipherSuiteSetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cipher_suite_set_for_tls12: Optional[Sequence[_builtins.str]] = ...,
        cipher_suite_set_for_tls13: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cipherSuiteSetForTls12")
    def cipher_suite_set_for_tls12(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cipherSuiteSetForTls13")
    def cipher_suite_set_for_tls13(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AFDDomainHttpsParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_type: _builtins.str,
        cipher_suite_set_type: Optional[_builtins.str] = ...,
        customized_cipher_suite_set: Optional[
            outputs.AFDDomainHttpsCustomizedCipherSuiteSetResponse
        ] = ...,
        minimum_tls_version: Optional[_builtins.str] = ...,
        secret: Optional[outputs.ResourceReferenceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateType")
    def certificate_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cipherSuiteSetType")
    def cipher_suite_set_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customizedCipherSuiteSet")
    def customized_cipher_suite_set(
        self,
    ) -> Optional[outputs.AFDDomainHttpsCustomizedCipherSuiteSetResponse]: ...
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[outputs.ResourceReferenceResponse]: ...

@pulumi.output_type
class ActivatedResourceReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, is_active: _builtins.bool, id: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isActive")
    def is_active(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AfdRouteCacheConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compression_settings: Optional[outputs.CompressionSettingsResponse] = ...,
        query_parameters: Optional[_builtins.str] = ...,
        query_string_caching_behavior: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="compressionSettings")
    def compression_settings(self) -> Optional[outputs.CompressionSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryStringCachingBehavior")
    def query_string_caching_behavior(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentPathResponse(dict):
    def __init__(__self__, *, path: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AzureFirstPartyManagedCertificateParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_authority: _builtins.str,
        expiration_date: _builtins.str,
        secret_source: outputs.ResourceReferenceResponse,
        subject: _builtins.str,
        thumbprint: _builtins.str,
        type: _builtins.str,
        subject_alternative_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretSource")
    def secret_source(self) -> outputs.ResourceReferenceResponse: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CacheConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cache_behavior: Optional[_builtins.str] = ...,
        cache_duration: Optional[_builtins.str] = ...,
        is_compression_enabled: Optional[_builtins.str] = ...,
        query_parameters: Optional[_builtins.str] = ...,
        query_string_caching_behavior: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheBehavior")
    def cache_behavior(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cacheDuration")
    def cache_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isCompressionEnabled")
    def is_compression_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryStringCachingBehavior")
    def query_string_caching_behavior(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CacheExpirationActionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cache_behavior: _builtins.str,
        cache_type: _builtins.str,
        type_name: _builtins.str,
        cache_duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheBehavior")
    def cache_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cacheType")
    def cache_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cacheDuration")
    def cache_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CacheKeyQueryStringActionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        query_string_behavior: _builtins.str,
        type_name: _builtins.str,
        query_parameters: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="queryStringBehavior")
    def query_string_behavior(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CdnCertificateSourceParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_type: _builtins.str, type_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateType")
    def certificate_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...

@pulumi.output_type
class CdnEndpointResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CdnManagedHttpsParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_source: _builtins.str,
        certificate_source_parameters: outputs.CdnCertificateSourceParametersResponse,
        protocol_type: _builtins.str,
        minimum_tls_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateSource")
    def certificate_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateSourceParameters")
    def certificate_source_parameters(
        self,
    ) -> outputs.CdnCertificateSourceParametersResponse: ...
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClientPortMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CompressionSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        content_types_to_compress: Optional[Sequence[_builtins.str]] = ...,
        is_compression_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentTypesToCompress")
    def content_types_to_compress(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isCompressionEnabled")
    def is_compression_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CookiesMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        selector: Optional[_builtins.str] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CustomRuleListResponse(dict):
    def __init__(
        __self__, *, rules: Optional[Sequence[outputs.CustomRuleResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.CustomRuleResponse]]: ...

@pulumi.output_type
class CustomRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        match_conditions: Sequence[outputs.MatchConditionResponse],
        name: _builtins.str,
        priority: _builtins.int,
        enabled_state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchConditions")
    def match_conditions(self) -> Sequence[outputs.MatchConditionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomerCertificateParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_authority: _builtins.str,
        expiration_date: _builtins.str,
        secret_source: outputs.ResourceReferenceResponse,
        subject: _builtins.str,
        subject_alternative_names: Sequence[_builtins.str],
        thumbprint: _builtins.str,
        type: _builtins.str,
        secret_version: Optional[_builtins.str] = ...,
        use_latest_version: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretSource")
    def secret_source(self) -> outputs.ResourceReferenceResponse: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useLatestVersion")
    def use_latest_version(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DeepCreatedCustomDomainResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_name: _builtins.str,
        name: _builtins.str,
        validation_data: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="validationData")
    def validation_data(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeepCreatedOriginGroupResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        origins: Sequence[outputs.ResourceReferenceResponse],
        health_probe_settings: Optional[outputs.HealthProbeParametersResponse] = ...,
        response_based_origin_error_detection_settings: Optional[
            outputs.ResponseBasedOriginErrorDetectionParametersResponse
        ] = ...,
        traffic_restoration_time_to_healed_or_new_endpoints_in_minutes: Optional[
            _builtins.int
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def origins(self) -> Sequence[outputs.ResourceReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(
        self,
    ) -> Optional[outputs.HealthProbeParametersResponse]: ...
    @_builtins.property
    @pulumi.getter(name="responseBasedOriginErrorDetectionSettings")
    def response_based_origin_error_detection_settings(
        self,
    ) -> Optional[outputs.ResponseBasedOriginErrorDetectionParametersResponse]: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def traffic_restoration_time_to_healed_or_new_endpoints_in_minutes(
        self,
    ) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DeepCreatedOriginResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_name: _builtins.str,
        name: _builtins.str,
        private_endpoint_status: _builtins.str,
        enabled: Optional[_builtins.bool] = ...,
        http_port: Optional[_builtins.int] = ...,
        https_port: Optional[_builtins.int] = ...,
        origin_host_header: Optional[_builtins.str] = ...,
        priority: Optional[_builtins.int] = ...,
        private_link_alias: Optional[_builtins.str] = ...,
        private_link_approval_message: Optional[_builtins.str] = ...,
        private_link_location: Optional[_builtins.str] = ...,
        private_link_resource_id: Optional[_builtins.str] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointStatus")
    def private_endpoint_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkAlias")
    def private_link_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkApprovalMessage")
    def private_link_approval_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkLocation")
    def private_link_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DeliveryRuleCacheExpirationActionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.CacheExpirationActionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.CacheExpirationActionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleCacheKeyQueryStringActionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.CacheKeyQueryStringActionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.CacheKeyQueryStringActionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleClientPortConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.ClientPortMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.ClientPortMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleCookiesConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.CookiesMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.CookiesMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleHostNameConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.HostNameMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.HostNameMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleHttpVersionConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.HttpVersionMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.HttpVersionMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleIsDeviceConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.IsDeviceMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.IsDeviceMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRulePostArgsConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.PostArgsMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.PostArgsMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleQueryStringConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.QueryStringMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.QueryStringMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleRemoteAddressConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.RemoteAddressMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.RemoteAddressMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleRequestBodyConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.RequestBodyMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.RequestBodyMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleRequestHeaderActionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.HeaderActionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.HeaderActionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleRequestHeaderConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.RequestHeaderMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.RequestHeaderMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleRequestMethodConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.RequestMethodMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.RequestMethodMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleRequestSchemeConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.RequestSchemeMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.RequestSchemeMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleRequestUriConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.RequestUriMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.RequestUriMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleResponse(dict):
    def __init__(
        __self__,
        *,
        actions: Sequence[Any],
        order: _builtins.int,
        conditions: Optional[Sequence[Any]] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[Any]: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[Any]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeliveryRuleResponseHeaderActionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.HeaderActionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.HeaderActionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleRouteConfigurationOverrideActionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.RouteConfigurationOverrideActionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> outputs.RouteConfigurationOverrideActionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleServerPortConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.ServerPortMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.ServerPortMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleSocketAddrConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.SocketAddrMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.SocketAddrMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleSslProtocolConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.SslProtocolMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.SslProtocolMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleUrlFileExtensionConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.UrlFileExtensionMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> outputs.UrlFileExtensionMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleUrlFileNameConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.UrlFileNameMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.UrlFileNameMatchConditionParametersResponse: ...

@pulumi.output_type
class DeliveryRuleUrlPathConditionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.UrlPathMatchConditionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.UrlPathMatchConditionParametersResponse: ...

@pulumi.output_type
class DomainValidationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, expiration_date: _builtins.str, validation_token: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="validationToken")
    def validation_token(self) -> _builtins.str: ...

@pulumi.output_type
class EdgeActionAttachmentResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, attached_resource_id: _builtins.str, id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachedResourceId")
    def attached_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class EndpointPropertiesUpdateParametersDeliveryPolicyResponse(dict):
    def __init__(
        __self__,
        *,
        rules: Sequence[outputs.DeliveryRuleResponse],
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.DeliveryRuleResponse]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLinkResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GeoFilterResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        country_codes: Sequence[_builtins.str],
        relative_path: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="countryCodes")
    def country_codes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> _builtins.str: ...

@pulumi.output_type
class HeaderActionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        header_action: _builtins.str,
        header_name: _builtins.str,
        type_name: _builtins.str,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerAction")
    def header_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HealthProbeParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        probe_interval_in_seconds: Optional[_builtins.int] = ...,
        probe_path: Optional[_builtins.str] = ...,
        probe_protocol: Optional[_builtins.str] = ...,
        probe_request_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="probeIntervalInSeconds")
    def probe_interval_in_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="probePath")
    def probe_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="probeProtocol")
    def probe_protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="probeRequestType")
    def probe_request_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HostNameMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class HttpErrorRangeParametersResponse(dict):
    def __init__(
        __self__,
        *,
        begin: Optional[_builtins.int] = ...,
        end: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def begin(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class HttpVersionMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class IsDeviceMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class KeyVaultCertificateSourceParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delete_rule: _builtins.str,
        resource_group_name: _builtins.str,
        secret_name: _builtins.str,
        subscription_id: _builtins.str,
        type_name: _builtins.str,
        update_rule: _builtins.str,
        vault_name: _builtins.str,
        secret_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deleteRule")
    def delete_rule(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updateRule")
    def update_rule(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KeyVaultSigningKeyParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_group_name: _builtins.str,
        secret_name: _builtins.str,
        secret_version: _builtins.str,
        subscription_id: _builtins.str,
        type_name: _builtins.str,
        vault_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> _builtins.str: ...

@pulumi.output_type
class LoadBalancingSettingsParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_latency_in_milliseconds: Optional[_builtins.int] = ...,
        sample_size: Optional[_builtins.int] = ...,
        successful_samples_required: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalLatencyInMilliseconds")
    def additional_latency_in_milliseconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sampleSize")
    def sample_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="successfulSamplesRequired")
    def successful_samples_required(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ManagedCertificateParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        expiration_date: _builtins.str,
        subject: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ManagedRuleGroupOverrideResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rule_group_name: _builtins.str,
        rules: Optional[Sequence[outputs.ManagedRuleOverrideResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleGroupName")
    def rule_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.ManagedRuleOverrideResponse]]: ...

@pulumi.output_type
class ManagedRuleOverrideResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rule_id: _builtins.str,
        action: Optional[_builtins.str] = ...,
        enabled_state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagedRuleSetListResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        managed_rule_sets: Optional[Sequence[outputs.ManagedRuleSetResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedRuleSets")
    def managed_rule_sets(
        self,
    ) -> Optional[Sequence[outputs.ManagedRuleSetResponse]]: ...

@pulumi.output_type
class ManagedRuleSetResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rule_set_type: _builtins.str,
        rule_set_version: _builtins.str,
        anomaly_score: Optional[_builtins.int] = ...,
        rule_group_overrides: Optional[
            Sequence[outputs.ManagedRuleGroupOverrideResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleSetType")
    def rule_set_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleSetVersion")
    def rule_set_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="anomalyScore")
    def anomaly_score(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ruleGroupOverrides")
    def rule_group_overrides(
        self,
    ) -> Optional[Sequence[outputs.ManagedRuleGroupOverrideResponse]]: ...

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
class MatchConditionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        match_value: Sequence[_builtins.str],
        match_variable: _builtins.str,
        operator: _builtins.str,
        negate_condition: Optional[_builtins.bool] = ...,
        selector: Optional[_builtins.str] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchValue")
    def match_value(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="matchVariable")
    def match_variable(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OriginAuthenticationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        scope: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
        user_assigned_identity: Optional[outputs.ResourceReferenceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[outputs.ResourceReferenceResponse]: ...

@pulumi.output_type
class OriginGroupOverrideActionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        origin_group: outputs.ResourceReferenceResponse,
        type_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="originGroup")
    def origin_group(self) -> outputs.ResourceReferenceResponse: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...

@pulumi.output_type
class OriginGroupOverrideActionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.OriginGroupOverrideActionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.OriginGroupOverrideActionParametersResponse: ...

@pulumi.output_type
class OriginGroupOverrideResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        forwarding_protocol: Optional[_builtins.str] = ...,
        origin_group: Optional[outputs.ResourceReferenceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="forwardingProtocol")
    def forwarding_protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originGroup")
    def origin_group(self) -> Optional[outputs.ResourceReferenceResponse]: ...

@pulumi.output_type
class PolicySettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_custom_block_response_body: Optional[_builtins.str] = ...,
        default_custom_block_response_status_code: Optional[_builtins.float] = ...,
        default_redirect_url: Optional[_builtins.str] = ...,
        enabled_state: Optional[_builtins.str] = ...,
        mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultCustomBlockResponseBody")
    def default_custom_block_response_body(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultCustomBlockResponseStatusCode")
    def default_custom_block_response_status_code(
        self,
    ) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="defaultRedirectUrl")
    def default_redirect_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PostArgsMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        selector: Optional[_builtins.str] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ProfileLogScrubbingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        scrubbing_rules: Optional[
            Sequence[outputs.ProfileScrubbingRulesResponse]
        ] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scrubbingRules")
    def scrubbing_rules(
        self,
    ) -> Optional[Sequence[outputs.ProfileScrubbingRulesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProfileScrubbingRulesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        match_variable: _builtins.str,
        selector_match_operator: _builtins.str,
        selector: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchVariable")
    def match_variable(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selectorMatchOperator")
    def selector_match_operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class QueryStringMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RateLimitRuleListResponse(dict):
    def __init__(
        __self__, *, rules: Optional[Sequence[outputs.RateLimitRuleResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.RateLimitRuleResponse]]: ...

@pulumi.output_type
class RateLimitRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        match_conditions: Sequence[outputs.MatchConditionResponse],
        name: _builtins.str,
        priority: _builtins.int,
        rate_limit_duration_in_minutes: _builtins.int,
        rate_limit_threshold: _builtins.int,
        enabled_state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchConditions")
    def match_conditions(self) -> Sequence[outputs.MatchConditionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="rateLimitDurationInMinutes")
    def rate_limit_duration_in_minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="rateLimitThreshold")
    def rate_limit_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RemoteAddressMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RequestBodyMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RequestHeaderMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        selector: Optional[_builtins.str] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RequestMethodMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RequestSchemeMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RequestUriMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ResourceReferenceResponse(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResponseBasedOriginErrorDetectionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        http_error_ranges: Optional[
            Sequence[outputs.HttpErrorRangeParametersResponse]
        ] = ...,
        response_based_detected_error_types: Optional[_builtins.str] = ...,
        response_based_failover_threshold_percentage: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpErrorRanges")
    def http_error_ranges(
        self,
    ) -> Optional[Sequence[outputs.HttpErrorRangeParametersResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="responseBasedDetectedErrorTypes")
    def response_based_detected_error_types(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responseBasedFailoverThresholdPercentage")
    def response_based_failover_threshold_percentage(
        self,
    ) -> Optional[_builtins.int]: ...

@pulumi.output_type
class RouteConfigurationOverrideActionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type_name: _builtins.str,
        cache_configuration: Optional[outputs.CacheConfigurationResponse] = ...,
        origin_group_override: Optional[outputs.OriginGroupOverrideResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cacheConfiguration")
    def cache_configuration(self) -> Optional[outputs.CacheConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="originGroupOverride")
    def origin_group_override(
        self,
    ) -> Optional[outputs.OriginGroupOverrideResponse]: ...

@pulumi.output_type
class SecurityPolicyWebApplicationFirewallAssociationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domains: Optional[Sequence[outputs.ActivatedResourceReferenceResponse]] = ...,
        patterns_to_match: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domains(
        self,
    ) -> Optional[Sequence[outputs.ActivatedResourceReferenceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="patternsToMatch")
    def patterns_to_match(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SecurityPolicyWebApplicationFirewallParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        associations: Optional[
            Sequence[outputs.SecurityPolicyWebApplicationFirewallAssociationResponse]
        ] = ...,
        waf_policy: Optional[outputs.ResourceReferenceResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def associations(
        self,
    ) -> Optional[
        Sequence[outputs.SecurityPolicyWebApplicationFirewallAssociationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="wafPolicy")
    def waf_policy(self) -> Optional[outputs.ResourceReferenceResponse]: ...

@pulumi.output_type
class ServerPortMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SharedPrivateLinkResourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_id: Optional[_builtins.str] = ...,
        private_link: Optional[outputs.ResourceReferenceResponse] = ...,
        private_link_location: Optional[_builtins.str] = ...,
        request_message: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLink")
    def private_link(self) -> Optional[outputs.ResourceReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkLocation")
    def private_link_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SkuResponse(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SkuTypeResponse(dict):
    def __init__(__self__, *, name: _builtins.str, tier: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str: ...

@pulumi.output_type
class SocketAddrMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SslProtocolMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

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
class TargetEndpointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ports: Optional[Sequence[_builtins.int]] = ...,
        target_fqdn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[Sequence[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="targetFqdn")
    def target_fqdn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UrlFileExtensionMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class UrlFileNameMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class UrlPathMatchConditionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operator: _builtins.str,
        type_name: _builtins.str,
        match_values: Optional[Sequence[_builtins.str]] = ...,
        negate_condition: Optional[_builtins.bool] = ...,
        transforms: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class UrlRedirectActionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        redirect_type: _builtins.str,
        type_name: _builtins.str,
        custom_fragment: Optional[_builtins.str] = ...,
        custom_hostname: Optional[_builtins.str] = ...,
        custom_path: Optional[_builtins.str] = ...,
        custom_query_string: Optional[_builtins.str] = ...,
        destination_protocol: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="redirectType")
    def redirect_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customFragment")
    def custom_fragment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customHostname")
    def custom_hostname(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customPath")
    def custom_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customQueryString")
    def custom_query_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationProtocol")
    def destination_protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UrlRedirectActionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.UrlRedirectActionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.UrlRedirectActionParametersResponse: ...

@pulumi.output_type
class UrlRewriteActionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: _builtins.str,
        source_pattern: _builtins.str,
        type_name: _builtins.str,
        preserve_unmatched_path: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourcePattern")
    def source_pattern(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preserveUnmatchedPath")
    def preserve_unmatched_path(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class UrlRewriteActionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.UrlRewriteActionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.UrlRewriteActionParametersResponse: ...

@pulumi.output_type
class UrlSigningActionParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type_name: _builtins.str,
        algorithm: Optional[_builtins.str] = ...,
        parameter_name_override: Optional[
            Sequence[outputs.UrlSigningParamIdentifierResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parameterNameOverride")
    def parameter_name_override(
        self,
    ) -> Optional[Sequence[outputs.UrlSigningParamIdentifierResponse]]: ...

@pulumi.output_type
class UrlSigningActionResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        parameters: outputs.UrlSigningActionParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> outputs.UrlSigningActionParametersResponse: ...

@pulumi.output_type
class UrlSigningKeyParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_id: _builtins.str,
        secret_source: outputs.ResourceReferenceResponse,
        secret_version: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretSource")
    def secret_source(self) -> outputs.ResourceReferenceResponse: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class UrlSigningKeyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_id: _builtins.str,
        key_source_parameters: outputs.KeyVaultSigningKeyParametersResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keySourceParameters")
    def key_source_parameters(self) -> outputs.KeyVaultSigningKeyParametersResponse: ...

@pulumi.output_type
class UrlSigningParamIdentifierResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, param_indicator: _builtins.str, param_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="paramIndicator")
    def param_indicator(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="paramName")
    def param_name(self) -> _builtins.str: ...

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

@pulumi.output_type
class UserManagedHttpsParametersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_source: _builtins.str,
        certificate_source_parameters: outputs.KeyVaultCertificateSourceParametersResponse,
        protocol_type: _builtins.str,
        minimum_tls_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateSource")
    def certificate_source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateSourceParameters")
    def certificate_source_parameters(
        self,
    ) -> outputs.KeyVaultCertificateSourceParametersResponse: ...
    @_builtins.property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> Optional[_builtins.str]: ...
