

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AFDDomainHttpsCustomizedCipherSuiteSetArgs', 'AFDDomainHttpsCustomizedCipherSuiteSetArgsDict', 'AFDDomainHttpsParametersArgs', 'AFDDomainHttpsParametersArgsDict', 'ActivatedResourceReferenceArgs', 'ActivatedResourceReferenceArgsDict', 'AfdRouteCacheConfigurationArgs', 'AfdRouteCacheConfigurationArgsDict', 'AgentPathArgs', 'AgentPathArgsDict', 'AzureFirstPartyManagedCertificateParametersArgs', ..., 'CacheConfigurationArgs', 'CacheConfigurationArgsDict', 'CacheExpirationActionParametersArgs', 'CacheExpirationActionParametersArgsDict', 'CacheKeyQueryStringActionParametersArgs', 'CacheKeyQueryStringActionParametersArgsDict', 'ClientPortMatchConditionParametersArgs', 'ClientPortMatchConditionParametersArgsDict', 'CompressionSettingsArgs', 'CompressionSettingsArgsDict', 'CookiesMatchConditionParametersArgs', 'CookiesMatchConditionParametersArgsDict', 'CustomRuleListArgs', 'CustomRuleListArgsDict', 'CustomRuleArgs', 'CustomRuleArgsDict', 'CustomerCertificateParametersArgs', 'CustomerCertificateParametersArgsDict', 'DeepCreatedOriginGroupArgs', 'DeepCreatedOriginGroupArgsDict', 'DeepCreatedOriginArgs', 'DeepCreatedOriginArgsDict', 'DeliveryRuleCacheExpirationActionArgs', 'DeliveryRuleCacheExpirationActionArgsDict', 'DeliveryRuleCacheKeyQueryStringActionArgs', 'DeliveryRuleCacheKeyQueryStringActionArgsDict', 'DeliveryRuleClientPortConditionArgs', 'DeliveryRuleClientPortConditionArgsDict', 'DeliveryRuleCookiesConditionArgs', 'DeliveryRuleCookiesConditionArgsDict', 'DeliveryRuleHostNameConditionArgs', 'DeliveryRuleHostNameConditionArgsDict', 'DeliveryRuleHttpVersionConditionArgs', 'DeliveryRuleHttpVersionConditionArgsDict', 'DeliveryRuleIsDeviceConditionArgs', 'DeliveryRuleIsDeviceConditionArgsDict', 'DeliveryRulePostArgsConditionArgs', 'DeliveryRulePostArgsConditionArgsDict', 'DeliveryRuleQueryStringConditionArgs', 'DeliveryRuleQueryStringConditionArgsDict', 'DeliveryRuleRemoteAddressConditionArgs', 'DeliveryRuleRemoteAddressConditionArgsDict', 'DeliveryRuleRequestBodyConditionArgs', 'DeliveryRuleRequestBodyConditionArgsDict', 'DeliveryRuleRequestHeaderActionArgs', 'DeliveryRuleRequestHeaderActionArgsDict', 'DeliveryRuleRequestHeaderConditionArgs', 'DeliveryRuleRequestHeaderConditionArgsDict', 'DeliveryRuleRequestMethodConditionArgs', 'DeliveryRuleRequestMethodConditionArgsDict', 'DeliveryRuleRequestSchemeConditionArgs', 'DeliveryRuleRequestSchemeConditionArgsDict', 'DeliveryRuleRequestUriConditionArgs', 'DeliveryRuleRequestUriConditionArgsDict', 'DeliveryRuleResponseHeaderActionArgs', 'DeliveryRuleResponseHeaderActionArgsDict', 'DeliveryRuleRouteConfigurationOverrideActionArgs', ..., 'DeliveryRuleServerPortConditionArgs', 'DeliveryRuleServerPortConditionArgsDict', 'DeliveryRuleSocketAddrConditionArgs', 'DeliveryRuleSocketAddrConditionArgsDict', 'DeliveryRuleSslProtocolConditionArgs', 'DeliveryRuleSslProtocolConditionArgsDict', 'DeliveryRuleUrlFileExtensionConditionArgs', 'DeliveryRuleUrlFileExtensionConditionArgsDict', 'DeliveryRuleUrlFileNameConditionArgs', 'DeliveryRuleUrlFileNameConditionArgsDict', 'DeliveryRuleUrlPathConditionArgs', 'DeliveryRuleUrlPathConditionArgsDict', 'DeliveryRuleArgs', 'DeliveryRuleArgsDict', ..., ..., ..., ..., 'GeoFilterArgs', 'GeoFilterArgsDict', 'HeaderActionParametersArgs', 'HeaderActionParametersArgsDict', 'HealthProbeParametersArgs', 'HealthProbeParametersArgsDict', 'HostNameMatchConditionParametersArgs', 'HostNameMatchConditionParametersArgsDict', 'HttpErrorRangeParametersArgs', 'HttpErrorRangeParametersArgsDict', 'HttpVersionMatchConditionParametersArgs', 'HttpVersionMatchConditionParametersArgsDict', 'IsDeviceMatchConditionParametersArgs', 'IsDeviceMatchConditionParametersArgsDict', 'KeyVaultSigningKeyParametersArgs', 'KeyVaultSigningKeyParametersArgsDict', 'LoadBalancingSettingsParametersArgs', 'LoadBalancingSettingsParametersArgsDict', 'ManagedCertificateParametersArgs', 'ManagedCertificateParametersArgsDict', 'ManagedRuleGroupOverrideArgs', 'ManagedRuleGroupOverrideArgsDict', 'ManagedRuleOverrideArgs', 'ManagedRuleOverrideArgsDict', 'ManagedRuleSetListArgs', 'ManagedRuleSetListArgsDict', 'ManagedRuleSetArgs', 'ManagedRuleSetArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'MatchConditionArgs', 'MatchConditionArgsDict', 'OriginAuthenticationPropertiesArgs', 'OriginAuthenticationPropertiesArgsDict', 'OriginGroupOverrideActionParametersArgs', 'OriginGroupOverrideActionParametersArgsDict', 'OriginGroupOverrideActionArgs', 'OriginGroupOverrideActionArgsDict', 'OriginGroupOverrideArgs', 'OriginGroupOverrideArgsDict', 'PolicySettingsArgs', 'PolicySettingsArgsDict', 'PostArgsMatchConditionParametersArgs', 'PostArgsMatchConditionParametersArgsDict', 'ProfileLogScrubbingArgs', 'ProfileLogScrubbingArgsDict', 'ProfileScrubbingRulesArgs', 'ProfileScrubbingRulesArgsDict', 'QueryStringMatchConditionParametersArgs', 'QueryStringMatchConditionParametersArgsDict', 'RateLimitRuleListArgs', 'RateLimitRuleListArgsDict', 'RateLimitRuleArgs', 'RateLimitRuleArgsDict', 'RemoteAddressMatchConditionParametersArgs', 'RemoteAddressMatchConditionParametersArgsDict', 'RequestBodyMatchConditionParametersArgs', 'RequestBodyMatchConditionParametersArgsDict', 'RequestHeaderMatchConditionParametersArgs', 'RequestHeaderMatchConditionParametersArgsDict', 'RequestMethodMatchConditionParametersArgs', 'RequestMethodMatchConditionParametersArgsDict', 'RequestSchemeMatchConditionParametersArgs', 'RequestSchemeMatchConditionParametersArgsDict', 'RequestUriMatchConditionParametersArgs', 'RequestUriMatchConditionParametersArgsDict', 'ResourceReferenceArgs', 'ResourceReferenceArgsDict', 'ResponseBasedOriginErrorDetectionParametersArgs', ..., 'RouteConfigurationOverrideActionParametersArgs', 'RouteConfigurationOverrideActionParametersArgsDict', ..., ..., 'SecurityPolicyWebApplicationFirewallParametersArgs', ..., 'ServerPortMatchConditionParametersArgs', 'ServerPortMatchConditionParametersArgsDict', 'SharedPrivateLinkResourcePropertiesArgs', 'SharedPrivateLinkResourcePropertiesArgsDict', 'SkuTypeArgs', 'SkuTypeArgsDict', 'SkuArgs', 'SkuArgsDict', 'SocketAddrMatchConditionParametersArgs', 'SocketAddrMatchConditionParametersArgsDict', 'SslProtocolMatchConditionParametersArgs', 'SslProtocolMatchConditionParametersArgsDict', 'TargetEndpointArgs', 'TargetEndpointArgsDict', 'UrlFileExtensionMatchConditionParametersArgs', 'UrlFileExtensionMatchConditionParametersArgsDict', 'UrlFileNameMatchConditionParametersArgs', 'UrlFileNameMatchConditionParametersArgsDict', 'UrlPathMatchConditionParametersArgs', 'UrlPathMatchConditionParametersArgsDict', 'UrlRedirectActionParametersArgs', 'UrlRedirectActionParametersArgsDict', 'UrlRedirectActionArgs', 'UrlRedirectActionArgsDict', 'UrlRewriteActionParametersArgs', 'UrlRewriteActionParametersArgsDict', 'UrlRewriteActionArgs', 'UrlRewriteActionArgsDict', 'UrlSigningActionParametersArgs', 'UrlSigningActionParametersArgsDict', 'UrlSigningActionArgs', 'UrlSigningActionArgsDict', 'UrlSigningKeyParametersArgs', 'UrlSigningKeyParametersArgsDict', 'UrlSigningKeyArgs', 'UrlSigningKeyArgsDict', 'UrlSigningParamIdentifierArgs', 'UrlSigningParamIdentifierArgsDict']
class AFDDomainHttpsCustomizedCipherSuiteSetArgsDict(TypedDict):
    
    cipher_suite_set_for_tls12: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AfdCustomizedCipherSuiteForTls12]]]]]
    cipher_suite_set_for_tls13: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AfdCustomizedCipherSuiteForTls13]]]]]


@pulumi.input_type
class AFDDomainHttpsCustomizedCipherSuiteSetArgs:
    def __init__(__self__, *, cipher_suite_set_for_tls12: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AfdCustomizedCipherSuiteForTls12]]]]] = ..., cipher_suite_set_for_tls13: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AfdCustomizedCipherSuiteForTls13]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cipherSuiteSetForTls12")
    def cipher_suite_set_for_tls12(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AfdCustomizedCipherSuiteForTls12]]]]]:
        
        ...
    
    @cipher_suite_set_for_tls12.setter
    def cipher_suite_set_for_tls12(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AfdCustomizedCipherSuiteForTls12]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cipherSuiteSetForTls13")
    def cipher_suite_set_for_tls13(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AfdCustomizedCipherSuiteForTls13]]]]]:
        
        ...
    
    @cipher_suite_set_for_tls13.setter
    def cipher_suite_set_for_tls13(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AfdCustomizedCipherSuiteForTls13]]]]]): # -> None:
        ...
    


class AFDDomainHttpsParametersArgsDict(TypedDict):
    
    certificate_type: pulumi.Input[Union[_builtins.str, AfdCertificateType]]
    cipher_suite_set_type: NotRequired[pulumi.Input[Union[_builtins.str, AfdCipherSuiteSetType]]]
    customized_cipher_suite_set: NotRequired[pulumi.Input[AFDDomainHttpsCustomizedCipherSuiteSetArgsDict]]
    minimum_tls_version: NotRequired[pulumi.Input[AfdMinimumTlsVersion]]
    secret: NotRequired[pulumi.Input[ResourceReferenceArgsDict]]


@pulumi.input_type
class AFDDomainHttpsParametersArgs:
    def __init__(__self__, *, certificate_type: pulumi.Input[Union[_builtins.str, AfdCertificateType]], cipher_suite_set_type: Optional[pulumi.Input[Union[_builtins.str, AfdCipherSuiteSetType]]] = ..., customized_cipher_suite_set: Optional[pulumi.Input[AFDDomainHttpsCustomizedCipherSuiteSetArgs]] = ..., minimum_tls_version: Optional[pulumi.Input[AfdMinimumTlsVersion]] = ..., secret: Optional[pulumi.Input[ResourceReferenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateType")
    def certificate_type(self) -> pulumi.Input[Union[_builtins.str, AfdCertificateType]]:
        
        ...
    
    @certificate_type.setter
    def certificate_type(self, value: pulumi.Input[Union[_builtins.str, AfdCertificateType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cipherSuiteSetType")
    def cipher_suite_set_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AfdCipherSuiteSetType]]]:
        
        ...
    
    @cipher_suite_set_type.setter
    def cipher_suite_set_type(self, value: Optional[pulumi.Input[Union[_builtins.str, AfdCipherSuiteSetType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customizedCipherSuiteSet")
    def customized_cipher_suite_set(self) -> Optional[pulumi.Input[AFDDomainHttpsCustomizedCipherSuiteSetArgs]]:
        
        ...
    
    @customized_cipher_suite_set.setter
    def customized_cipher_suite_set(self, value: Optional[pulumi.Input[AFDDomainHttpsCustomizedCipherSuiteSetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> Optional[pulumi.Input[AfdMinimumTlsVersion]]:
        
        ...
    
    @minimum_tls_version.setter
    def minimum_tls_version(self, value: Optional[pulumi.Input[AfdMinimumTlsVersion]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]:
        
        ...
    
    @secret.setter
    def secret(self, value: Optional[pulumi.Input[ResourceReferenceArgs]]): # -> None:
        ...
    


class ActivatedResourceReferenceArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ActivatedResourceReferenceArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AfdRouteCacheConfigurationArgsDict(TypedDict):
    
    compression_settings: NotRequired[pulumi.Input[CompressionSettingsArgsDict]]
    query_parameters: NotRequired[pulumi.Input[_builtins.str]]
    query_string_caching_behavior: NotRequired[pulumi.Input[Union[_builtins.str, AfdQueryStringCachingBehavior]]]


@pulumi.input_type
class AfdRouteCacheConfigurationArgs:
    def __init__(__self__, *, compression_settings: Optional[pulumi.Input[CompressionSettingsArgs]] = ..., query_parameters: Optional[pulumi.Input[_builtins.str]] = ..., query_string_caching_behavior: Optional[pulumi.Input[Union[_builtins.str, AfdQueryStringCachingBehavior]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressionSettings")
    def compression_settings(self) -> Optional[pulumi.Input[CompressionSettingsArgs]]:
        
        ...
    
    @compression_settings.setter
    def compression_settings(self, value: Optional[pulumi.Input[CompressionSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query_parameters.setter
    def query_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringCachingBehavior")
    def query_string_caching_behavior(self) -> Optional[pulumi.Input[Union[_builtins.str, AfdQueryStringCachingBehavior]]]:
        
        ...
    
    @query_string_caching_behavior.setter
    def query_string_caching_behavior(self, value: Optional[pulumi.Input[Union[_builtins.str, AfdQueryStringCachingBehavior]]]): # -> None:
        ...
    


class AgentPathArgsDict(TypedDict):
    
    path: pulumi.Input[_builtins.str]
    type: pulumi.Input[Union[_builtins.str, AgentPathType]]


@pulumi.input_type
class AgentPathArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str], type: pulumi.Input[Union[_builtins.str, AgentPathType]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, AgentPathType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, AgentPathType]]): # -> None:
        ...
    


class AzureFirstPartyManagedCertificateParametersArgsDict(TypedDict):
    
    type: pulumi.Input[_builtins.str]
    subject_alternative_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AzureFirstPartyManagedCertificateParametersArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], subject_alternative_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subject_alternative_names.setter
    def subject_alternative_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CacheConfigurationArgsDict(TypedDict):
    
    cache_behavior: NotRequired[pulumi.Input[Union[_builtins.str, RuleCacheBehavior]]]
    cache_duration: NotRequired[pulumi.Input[_builtins.str]]
    is_compression_enabled: NotRequired[pulumi.Input[Union[_builtins.str, RuleIsCompressionEnabled]]]
    query_parameters: NotRequired[pulumi.Input[_builtins.str]]
    query_string_caching_behavior: NotRequired[pulumi.Input[Union[_builtins.str, RuleQueryStringCachingBehavior]]]


@pulumi.input_type
class CacheConfigurationArgs:
    def __init__(__self__, *, cache_behavior: Optional[pulumi.Input[Union[_builtins.str, RuleCacheBehavior]]] = ..., cache_duration: Optional[pulumi.Input[_builtins.str]] = ..., is_compression_enabled: Optional[pulumi.Input[Union[_builtins.str, RuleIsCompressionEnabled]]] = ..., query_parameters: Optional[pulumi.Input[_builtins.str]] = ..., query_string_caching_behavior: Optional[pulumi.Input[Union[_builtins.str, RuleQueryStringCachingBehavior]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheBehavior")
    def cache_behavior(self) -> Optional[pulumi.Input[Union[_builtins.str, RuleCacheBehavior]]]:
        
        ...
    
    @cache_behavior.setter
    def cache_behavior(self, value: Optional[pulumi.Input[Union[_builtins.str, RuleCacheBehavior]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheDuration")
    def cache_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_duration.setter
    def cache_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCompressionEnabled")
    def is_compression_enabled(self) -> Optional[pulumi.Input[Union[_builtins.str, RuleIsCompressionEnabled]]]:
        
        ...
    
    @is_compression_enabled.setter
    def is_compression_enabled(self, value: Optional[pulumi.Input[Union[_builtins.str, RuleIsCompressionEnabled]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query_parameters.setter
    def query_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringCachingBehavior")
    def query_string_caching_behavior(self) -> Optional[pulumi.Input[Union[_builtins.str, RuleQueryStringCachingBehavior]]]:
        
        ...
    
    @query_string_caching_behavior.setter
    def query_string_caching_behavior(self, value: Optional[pulumi.Input[Union[_builtins.str, RuleQueryStringCachingBehavior]]]): # -> None:
        ...
    


class CacheExpirationActionParametersArgsDict(TypedDict):
    
    cache_behavior: pulumi.Input[Union[_builtins.str, CacheBehavior]]
    cache_type: pulumi.Input[Union[_builtins.str, CacheType]]
    type_name: pulumi.Input[_builtins.str]
    cache_duration: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CacheExpirationActionParametersArgs:
    def __init__(__self__, *, cache_behavior: pulumi.Input[Union[_builtins.str, CacheBehavior]], cache_type: pulumi.Input[Union[_builtins.str, CacheType]], type_name: pulumi.Input[_builtins.str], cache_duration: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheBehavior")
    def cache_behavior(self) -> pulumi.Input[Union[_builtins.str, CacheBehavior]]:
        
        ...
    
    @cache_behavior.setter
    def cache_behavior(self, value: pulumi.Input[Union[_builtins.str, CacheBehavior]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheType")
    def cache_type(self) -> pulumi.Input[Union[_builtins.str, CacheType]]:
        
        ...
    
    @cache_type.setter
    def cache_type(self, value: pulumi.Input[Union[_builtins.str, CacheType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheDuration")
    def cache_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_duration.setter
    def cache_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CacheKeyQueryStringActionParametersArgsDict(TypedDict):
    
    query_string_behavior: pulumi.Input[Union[_builtins.str, QueryStringBehavior]]
    type_name: pulumi.Input[_builtins.str]
    query_parameters: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CacheKeyQueryStringActionParametersArgs:
    def __init__(__self__, *, query_string_behavior: pulumi.Input[Union[_builtins.str, QueryStringBehavior]], type_name: pulumi.Input[_builtins.str], query_parameters: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringBehavior")
    def query_string_behavior(self) -> pulumi.Input[Union[_builtins.str, QueryStringBehavior]]:
        
        ...
    
    @query_string_behavior.setter
    def query_string_behavior(self, value: pulumi.Input[Union[_builtins.str, QueryStringBehavior]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @query_parameters.setter
    def query_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ClientPortMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, ClientPortOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class ClientPortMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, ClientPortOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, ClientPortOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, ClientPortOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class CompressionSettingsArgsDict(TypedDict):
    
    content_types_to_compress: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    is_compression_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CompressionSettingsArgs:
    def __init__(__self__, *, content_types_to_compress: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., is_compression_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentTypesToCompress")
    def content_types_to_compress(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @content_types_to_compress.setter
    def content_types_to_compress(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCompressionEnabled")
    def is_compression_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_compression_enabled.setter
    def is_compression_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CookiesMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, CookiesOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    selector: NotRequired[pulumi.Input[_builtins.str]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class CookiesMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, CookiesOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., selector: Optional[pulumi.Input[_builtins.str]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, CookiesOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, CookiesOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @selector.setter
    def selector(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class CustomRuleListArgsDict(TypedDict):
    
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[CustomRuleArgsDict]]]]


@pulumi.input_type
class CustomRuleListArgs:
    def __init__(__self__, *, rules: Optional[pulumi.Input[Sequence[pulumi.Input[CustomRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomRuleArgs]]]]): # -> None:
        ...
    


class CustomRuleArgsDict(TypedDict):
    
    action: pulumi.Input[Union[_builtins.str, ActionType]]
    match_conditions: pulumi.Input[Sequence[pulumi.Input[MatchConditionArgsDict]]]
    name: pulumi.Input[_builtins.str]
    priority: pulumi.Input[_builtins.int]
    enabled_state: NotRequired[pulumi.Input[Union[_builtins.str, CustomRuleEnabledState]]]


@pulumi.input_type
class CustomRuleArgs:
    def __init__(__self__, *, action: pulumi.Input[Union[_builtins.str, ActionType]], match_conditions: pulumi.Input[Sequence[pulumi.Input[MatchConditionArgs]]], name: pulumi.Input[_builtins.str], priority: pulumi.Input[_builtins.int], enabled_state: Optional[pulumi.Input[Union[_builtins.str, CustomRuleEnabledState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[Union[_builtins.str, ActionType]]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[Union[_builtins.str, ActionType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchConditions")
    def match_conditions(self) -> pulumi.Input[Sequence[pulumi.Input[MatchConditionArgs]]]:
        
        ...
    
    @match_conditions.setter
    def match_conditions(self, value: pulumi.Input[Sequence[pulumi.Input[MatchConditionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[pulumi.Input[Union[_builtins.str, CustomRuleEnabledState]]]:
        
        ...
    
    @enabled_state.setter
    def enabled_state(self, value: Optional[pulumi.Input[Union[_builtins.str, CustomRuleEnabledState]]]): # -> None:
        ...
    


class CustomerCertificateParametersArgsDict(TypedDict):
    
    secret_source: pulumi.Input[ResourceReferenceArgsDict]
    type: pulumi.Input[_builtins.str]
    secret_version: NotRequired[pulumi.Input[_builtins.str]]
    use_latest_version: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CustomerCertificateParametersArgs:
    def __init__(__self__, *, secret_source: pulumi.Input[ResourceReferenceArgs], type: pulumi.Input[_builtins.str], secret_version: Optional[pulumi.Input[_builtins.str]] = ..., use_latest_version: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretSource")
    def secret_source(self) -> pulumi.Input[ResourceReferenceArgs]:
        
        ...
    
    @secret_source.setter
    def secret_source(self, value: pulumi.Input[ResourceReferenceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_version.setter
    def secret_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useLatestVersion")
    def use_latest_version(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_latest_version.setter
    def use_latest_version(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DeepCreatedOriginGroupArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    origins: pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgsDict]]]
    health_probe_settings: NotRequired[pulumi.Input[HealthProbeParametersArgsDict]]
    response_based_origin_error_detection_settings: NotRequired[pulumi.Input[ResponseBasedOriginErrorDetectionParametersArgsDict]]
    traffic_restoration_time_to_healed_or_new_endpoints_in_minutes: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DeepCreatedOriginGroupArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], origins: pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]], health_probe_settings: Optional[pulumi.Input[HealthProbeParametersArgs]] = ..., response_based_origin_error_detection_settings: Optional[pulumi.Input[ResponseBasedOriginErrorDetectionParametersArgs]] = ..., traffic_restoration_time_to_healed_or_new_endpoints_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origins(self) -> pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]:
        
        ...
    
    @origins.setter
    def origins(self, value: pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> Optional[pulumi.Input[HealthProbeParametersArgs]]:
        
        ...
    
    @health_probe_settings.setter
    def health_probe_settings(self, value: Optional[pulumi.Input[HealthProbeParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseBasedOriginErrorDetectionSettings")
    def response_based_origin_error_detection_settings(self) -> Optional[pulumi.Input[ResponseBasedOriginErrorDetectionParametersArgs]]:
        
        ...
    
    @response_based_origin_error_detection_settings.setter
    def response_based_origin_error_detection_settings(self, value: Optional[pulumi.Input[ResponseBasedOriginErrorDetectionParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name=...)
    def traffic_restoration_time_to_healed_or_new_endpoints_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @traffic_restoration_time_to_healed_or_new_endpoints_in_minutes.setter
    def traffic_restoration_time_to_healed_or_new_endpoints_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DeepCreatedOriginArgsDict(TypedDict):
    
    host_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    http_port: NotRequired[pulumi.Input[_builtins.int]]
    https_port: NotRequired[pulumi.Input[_builtins.int]]
    origin_host_header: NotRequired[pulumi.Input[_builtins.str]]
    priority: NotRequired[pulumi.Input[_builtins.int]]
    private_link_alias: NotRequired[pulumi.Input[_builtins.str]]
    private_link_approval_message: NotRequired[pulumi.Input[_builtins.str]]
    private_link_location: NotRequired[pulumi.Input[_builtins.str]]
    private_link_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DeepCreatedOriginArgs:
    def __init__(__self__, *, host_name: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], enabled: Optional[pulumi.Input[_builtins.bool]] = ..., http_port: Optional[pulumi.Input[_builtins.int]] = ..., https_port: Optional[pulumi.Input[_builtins.int]] = ..., origin_host_header: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., private_link_alias: Optional[pulumi.Input[_builtins.str]] = ..., private_link_approval_message: Optional[pulumi.Input[_builtins.str]] = ..., private_link_location: Optional[pulumi.Input[_builtins.str]] = ..., private_link_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., weight: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host_name.setter
    def host_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_port.setter
    def http_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @https_port.setter
    def https_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_host_header.setter
    def origin_host_header(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkAlias")
    def private_link_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_link_alias.setter
    def private_link_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkApprovalMessage")
    def private_link_approval_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_link_approval_message.setter
    def private_link_approval_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkLocation")
    def private_link_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_link_location.setter
    def private_link_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_link_resource_id.setter
    def private_link_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DeliveryRuleCacheExpirationActionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[CacheExpirationActionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleCacheExpirationActionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[CacheExpirationActionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[CacheExpirationActionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[CacheExpirationActionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleCacheKeyQueryStringActionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[CacheKeyQueryStringActionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleCacheKeyQueryStringActionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[CacheKeyQueryStringActionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[CacheKeyQueryStringActionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[CacheKeyQueryStringActionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleClientPortConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[ClientPortMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleClientPortConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[ClientPortMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[ClientPortMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[ClientPortMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleCookiesConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[CookiesMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleCookiesConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[CookiesMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[CookiesMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[CookiesMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleHostNameConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[HostNameMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleHostNameConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[HostNameMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[HostNameMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[HostNameMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleHttpVersionConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[HttpVersionMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleHttpVersionConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[HttpVersionMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[HttpVersionMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[HttpVersionMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleIsDeviceConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[IsDeviceMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleIsDeviceConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[IsDeviceMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[IsDeviceMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[IsDeviceMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRulePostArgsConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[PostArgsMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRulePostArgsConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[PostArgsMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[PostArgsMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[PostArgsMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleQueryStringConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[QueryStringMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleQueryStringConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[QueryStringMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[QueryStringMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[QueryStringMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleRemoteAddressConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[RemoteAddressMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleRemoteAddressConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[RemoteAddressMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[RemoteAddressMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[RemoteAddressMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleRequestBodyConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[RequestBodyMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleRequestBodyConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[RequestBodyMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[RequestBodyMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[RequestBodyMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleRequestHeaderActionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[HeaderActionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleRequestHeaderActionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[HeaderActionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[HeaderActionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[HeaderActionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleRequestHeaderConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[RequestHeaderMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleRequestHeaderConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[RequestHeaderMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[RequestHeaderMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[RequestHeaderMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleRequestMethodConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[RequestMethodMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleRequestMethodConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[RequestMethodMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[RequestMethodMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[RequestMethodMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleRequestSchemeConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[RequestSchemeMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleRequestSchemeConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[RequestSchemeMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[RequestSchemeMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[RequestSchemeMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleRequestUriConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[RequestUriMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleRequestUriConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[RequestUriMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[RequestUriMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[RequestUriMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleResponseHeaderActionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[HeaderActionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleResponseHeaderActionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[HeaderActionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[HeaderActionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[HeaderActionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleRouteConfigurationOverrideActionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[RouteConfigurationOverrideActionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleRouteConfigurationOverrideActionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[RouteConfigurationOverrideActionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[RouteConfigurationOverrideActionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[RouteConfigurationOverrideActionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleServerPortConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[ServerPortMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleServerPortConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[ServerPortMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[ServerPortMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[ServerPortMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleSocketAddrConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[SocketAddrMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleSocketAddrConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[SocketAddrMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[SocketAddrMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[SocketAddrMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleSslProtocolConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[SslProtocolMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleSslProtocolConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[SslProtocolMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[SslProtocolMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[SslProtocolMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleUrlFileExtensionConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[UrlFileExtensionMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleUrlFileExtensionConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[UrlFileExtensionMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[UrlFileExtensionMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[UrlFileExtensionMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleUrlFileNameConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[UrlFileNameMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleUrlFileNameConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[UrlFileNameMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[UrlFileNameMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[UrlFileNameMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleUrlPathConditionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[UrlPathMatchConditionParametersArgsDict]


@pulumi.input_type
class DeliveryRuleUrlPathConditionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[UrlPathMatchConditionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[UrlPathMatchConditionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[UrlPathMatchConditionParametersArgs]): # -> None:
        ...
    


class DeliveryRuleArgsDict(TypedDict):
    
    actions: pulumi.Input[Sequence[pulumi.Input[Union[DeliveryRuleCacheExpirationActionArgsDict, DeliveryRuleCacheKeyQueryStringActionArgsDict, DeliveryRuleRequestHeaderActionArgsDict, DeliveryRuleResponseHeaderActionArgsDict, DeliveryRuleRouteConfigurationOverrideActionArgsDict, OriginGroupOverrideActionArgsDict, UrlRedirectActionArgsDict, UrlRewriteActionArgsDict, UrlSigningActionArgsDict]]]]
    order: pulumi.Input[_builtins.int]
    conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[DeliveryRuleClientPortConditionArgsDict, DeliveryRuleCookiesConditionArgsDict, DeliveryRuleHostNameConditionArgsDict, DeliveryRuleHttpVersionConditionArgsDict, DeliveryRuleIsDeviceConditionArgsDict, DeliveryRulePostArgsConditionArgsDict, DeliveryRuleQueryStringConditionArgsDict, DeliveryRuleRemoteAddressConditionArgsDict, DeliveryRuleRequestBodyConditionArgsDict, DeliveryRuleRequestHeaderConditionArgsDict, DeliveryRuleRequestMethodConditionArgsDict, DeliveryRuleRequestSchemeConditionArgsDict, DeliveryRuleRequestUriConditionArgsDict, DeliveryRuleServerPortConditionArgsDict, DeliveryRuleSocketAddrConditionArgsDict, DeliveryRuleSslProtocolConditionArgsDict, DeliveryRuleUrlFileExtensionConditionArgsDict, DeliveryRuleUrlFileNameConditionArgsDict, DeliveryRuleUrlPathConditionArgsDict]]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DeliveryRuleArgs:
    def __init__(__self__, *, actions: pulumi.Input[Sequence[pulumi.Input[Union[DeliveryRuleCacheExpirationActionArgs, DeliveryRuleCacheKeyQueryStringActionArgs, DeliveryRuleRequestHeaderActionArgs, DeliveryRuleResponseHeaderActionArgs, DeliveryRuleRouteConfigurationOverrideActionArgs, OriginGroupOverrideActionArgs, UrlRedirectActionArgs, UrlRewriteActionArgs, UrlSigningActionArgs]]]], order: pulumi.Input[_builtins.int], conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeliveryRuleClientPortConditionArgs, DeliveryRuleCookiesConditionArgs, DeliveryRuleHostNameConditionArgs, DeliveryRuleHttpVersionConditionArgs, DeliveryRuleIsDeviceConditionArgs, DeliveryRulePostArgsConditionArgs, DeliveryRuleQueryStringConditionArgs, DeliveryRuleRemoteAddressConditionArgs, DeliveryRuleRequestBodyConditionArgs, DeliveryRuleRequestHeaderConditionArgs, DeliveryRuleRequestMethodConditionArgs, DeliveryRuleRequestSchemeConditionArgs, DeliveryRuleRequestUriConditionArgs, DeliveryRuleServerPortConditionArgs, DeliveryRuleSocketAddrConditionArgs, DeliveryRuleSslProtocolConditionArgs, DeliveryRuleUrlFileExtensionConditionArgs, DeliveryRuleUrlFileNameConditionArgs, DeliveryRuleUrlPathConditionArgs]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[Union[DeliveryRuleCacheExpirationActionArgs, DeliveryRuleCacheKeyQueryStringActionArgs, DeliveryRuleRequestHeaderActionArgs, DeliveryRuleResponseHeaderActionArgs, DeliveryRuleRouteConfigurationOverrideActionArgs, OriginGroupOverrideActionArgs, UrlRedirectActionArgs, UrlRewriteActionArgs, UrlSigningActionArgs]]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[Union[DeliveryRuleCacheExpirationActionArgs, DeliveryRuleCacheKeyQueryStringActionArgs, DeliveryRuleRequestHeaderActionArgs, DeliveryRuleResponseHeaderActionArgs, DeliveryRuleRouteConfigurationOverrideActionArgs, OriginGroupOverrideActionArgs, UrlRedirectActionArgs, UrlRewriteActionArgs, UrlSigningActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @order.setter
    def order(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeliveryRuleClientPortConditionArgs, DeliveryRuleCookiesConditionArgs, DeliveryRuleHostNameConditionArgs, DeliveryRuleHttpVersionConditionArgs, DeliveryRuleIsDeviceConditionArgs, DeliveryRulePostArgsConditionArgs, DeliveryRuleQueryStringConditionArgs, DeliveryRuleRemoteAddressConditionArgs, DeliveryRuleRequestBodyConditionArgs, DeliveryRuleRequestHeaderConditionArgs, DeliveryRuleRequestMethodConditionArgs, DeliveryRuleRequestSchemeConditionArgs, DeliveryRuleRequestUriConditionArgs, DeliveryRuleServerPortConditionArgs, DeliveryRuleSocketAddrConditionArgs, DeliveryRuleSslProtocolConditionArgs, DeliveryRuleUrlFileExtensionConditionArgs, DeliveryRuleUrlFileNameConditionArgs, DeliveryRuleUrlPathConditionArgs]]]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DeliveryRuleClientPortConditionArgs, DeliveryRuleCookiesConditionArgs, DeliveryRuleHostNameConditionArgs, DeliveryRuleHttpVersionConditionArgs, DeliveryRuleIsDeviceConditionArgs, DeliveryRulePostArgsConditionArgs, DeliveryRuleQueryStringConditionArgs, DeliveryRuleRemoteAddressConditionArgs, DeliveryRuleRequestBodyConditionArgs, DeliveryRuleRequestHeaderConditionArgs, DeliveryRuleRequestMethodConditionArgs, DeliveryRuleRequestSchemeConditionArgs, DeliveryRuleRequestUriConditionArgs, DeliveryRuleServerPortConditionArgs, DeliveryRuleSocketAddrConditionArgs, DeliveryRuleSslProtocolConditionArgs, DeliveryRuleUrlFileExtensionConditionArgs, DeliveryRuleUrlFileNameConditionArgs, DeliveryRuleUrlPathConditionArgs]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointPropertiesUpdateParametersDeliveryPolicyArgsDict(TypedDict):
    
    rules: pulumi.Input[Sequence[pulumi.Input[DeliveryRuleArgsDict]]]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointPropertiesUpdateParametersDeliveryPolicyArgs:
    def __init__(__self__, *, rules: pulumi.Input[Sequence[pulumi.Input[DeliveryRuleArgs]]], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input[DeliveryRuleArgs]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input[DeliveryRuleArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLinkArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLinkArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GeoFilterArgsDict(TypedDict):
    
    action: pulumi.Input[GeoFilterActions]
    country_codes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    relative_path: pulumi.Input[_builtins.str]


@pulumi.input_type
class GeoFilterArgs:
    def __init__(__self__, *, action: pulumi.Input[GeoFilterActions], country_codes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], relative_path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[GeoFilterActions]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[GeoFilterActions]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCodes")
    def country_codes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @country_codes.setter
    def country_codes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @relative_path.setter
    def relative_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class HeaderActionParametersArgsDict(TypedDict):
    
    header_action: pulumi.Input[Union[_builtins.str, HeaderAction]]
    header_name: pulumi.Input[_builtins.str]
    type_name: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HeaderActionParametersArgs:
    def __init__(__self__, *, header_action: pulumi.Input[Union[_builtins.str, HeaderAction]], header_name: pulumi.Input[_builtins.str], type_name: pulumi.Input[_builtins.str], value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerAction")
    def header_action(self) -> pulumi.Input[Union[_builtins.str, HeaderAction]]:
        
        ...
    
    @header_action.setter
    def header_action(self, value: pulumi.Input[Union[_builtins.str, HeaderAction]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @header_name.setter
    def header_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HealthProbeParametersArgsDict(TypedDict):
    
    probe_interval_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    probe_path: NotRequired[pulumi.Input[_builtins.str]]
    probe_protocol: NotRequired[pulumi.Input[ProbeProtocol]]
    probe_request_type: NotRequired[pulumi.Input[HealthProbeRequestType]]


@pulumi.input_type
class HealthProbeParametersArgs:
    def __init__(__self__, *, probe_interval_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., probe_path: Optional[pulumi.Input[_builtins.str]] = ..., probe_protocol: Optional[pulumi.Input[ProbeProtocol]] = ..., probe_request_type: Optional[pulumi.Input[HealthProbeRequestType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="probeIntervalInSeconds")
    def probe_interval_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @probe_interval_in_seconds.setter
    def probe_interval_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="probePath")
    def probe_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @probe_path.setter
    def probe_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="probeProtocol")
    def probe_protocol(self) -> Optional[pulumi.Input[ProbeProtocol]]:
        
        ...
    
    @probe_protocol.setter
    def probe_protocol(self, value: Optional[pulumi.Input[ProbeProtocol]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="probeRequestType")
    def probe_request_type(self) -> Optional[pulumi.Input[HealthProbeRequestType]]:
        
        ...
    
    @probe_request_type.setter
    def probe_request_type(self, value: Optional[pulumi.Input[HealthProbeRequestType]]): # -> None:
        ...
    


class HostNameMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, HostNameOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class HostNameMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, HostNameOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, HostNameOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, HostNameOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class HttpErrorRangeParametersArgsDict(TypedDict):
    
    begin: NotRequired[pulumi.Input[_builtins.int]]
    end: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class HttpErrorRangeParametersArgs:
    def __init__(__self__, *, begin: Optional[pulumi.Input[_builtins.int]] = ..., end: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def begin(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @begin.setter
    def begin(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class HttpVersionMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, HttpVersionOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class HttpVersionMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, HttpVersionOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, HttpVersionOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, HttpVersionOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class IsDeviceMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, IsDeviceOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, IsDeviceMatchValue]]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class IsDeviceMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, IsDeviceOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, IsDeviceMatchValue]]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, IsDeviceOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, IsDeviceOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, IsDeviceMatchValue]]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, IsDeviceMatchValue]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class KeyVaultSigningKeyParametersArgsDict(TypedDict):
    
    resource_group_name: pulumi.Input[_builtins.str]
    secret_name: pulumi.Input[_builtins.str]
    secret_version: pulumi.Input[_builtins.str]
    subscription_id: pulumi.Input[_builtins.str]
    type_name: pulumi.Input[Union[_builtins.str, KeyVaultSigningKeyParametersType]]
    vault_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class KeyVaultSigningKeyParametersArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], secret_name: pulumi.Input[_builtins.str], secret_version: pulumi.Input[_builtins.str], subscription_id: pulumi.Input[_builtins.str], type_name: pulumi.Input[Union[_builtins.str, KeyVaultSigningKeyParametersType]], vault_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subscription_id.setter
    def subscription_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[Union[_builtins.str, KeyVaultSigningKeyParametersType]]:
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[Union[_builtins.str, KeyVaultSigningKeyParametersType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vault_name.setter
    def vault_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class LoadBalancingSettingsParametersArgsDict(TypedDict):
    
    additional_latency_in_milliseconds: NotRequired[pulumi.Input[_builtins.int]]
    sample_size: NotRequired[pulumi.Input[_builtins.int]]
    successful_samples_required: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LoadBalancingSettingsParametersArgs:
    def __init__(__self__, *, additional_latency_in_milliseconds: Optional[pulumi.Input[_builtins.int]] = ..., sample_size: Optional[pulumi.Input[_builtins.int]] = ..., successful_samples_required: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalLatencyInMilliseconds")
    def additional_latency_in_milliseconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @additional_latency_in_milliseconds.setter
    def additional_latency_in_milliseconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleSize")
    def sample_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @sample_size.setter
    def sample_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="successfulSamplesRequired")
    def successful_samples_required(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @successful_samples_required.setter
    def successful_samples_required(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ManagedCertificateParametersArgsDict(TypedDict):
    
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ManagedCertificateParametersArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ManagedRuleGroupOverrideArgsDict(TypedDict):
    
    rule_group_name: pulumi.Input[_builtins.str]
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[ManagedRuleOverrideArgsDict]]]]


@pulumi.input_type
class ManagedRuleGroupOverrideArgs:
    def __init__(__self__, *, rule_group_name: pulumi.Input[_builtins.str], rules: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleOverrideArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleGroupName")
    def rule_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_group_name.setter
    def rule_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleOverrideArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleOverrideArgs]]]]): # -> None:
        ...
    


class ManagedRuleOverrideArgsDict(TypedDict):
    
    rule_id: pulumi.Input[_builtins.str]
    action: NotRequired[pulumi.Input[Union[_builtins.str, ActionType]]]
    enabled_state: NotRequired[pulumi.Input[Union[_builtins.str, ManagedRuleEnabledState]]]


@pulumi.input_type
class ManagedRuleOverrideArgs:
    def __init__(__self__, *, rule_id: pulumi.Input[_builtins.str], action: Optional[pulumi.Input[Union[_builtins.str, ActionType]]] = ..., enabled_state: Optional[pulumi.Input[Union[_builtins.str, ManagedRuleEnabledState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_id.setter
    def rule_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union[_builtins.str, ActionType]]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[Union[_builtins.str, ActionType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedRuleEnabledState]]]:
        
        ...
    
    @enabled_state.setter
    def enabled_state(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedRuleEnabledState]]]): # -> None:
        ...
    


class ManagedRuleSetListArgsDict(TypedDict):
    
    managed_rule_sets: NotRequired[pulumi.Input[Sequence[pulumi.Input[ManagedRuleSetArgsDict]]]]


@pulumi.input_type
class ManagedRuleSetListArgs:
    def __init__(__self__, *, managed_rule_sets: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleSetArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedRuleSets")
    def managed_rule_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleSetArgs]]]]:
        
        ...
    
    @managed_rule_sets.setter
    def managed_rule_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleSetArgs]]]]): # -> None:
        ...
    


class ManagedRuleSetArgsDict(TypedDict):
    
    rule_set_type: pulumi.Input[_builtins.str]
    rule_set_version: pulumi.Input[_builtins.str]
    anomaly_score: NotRequired[pulumi.Input[_builtins.int]]
    rule_group_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[ManagedRuleGroupOverrideArgsDict]]]]


@pulumi.input_type
class ManagedRuleSetArgs:
    def __init__(__self__, *, rule_set_type: pulumi.Input[_builtins.str], rule_set_version: pulumi.Input[_builtins.str], anomaly_score: Optional[pulumi.Input[_builtins.int]] = ..., rule_group_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleGroupOverrideArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleSetType")
    def rule_set_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_set_type.setter
    def rule_set_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleSetVersion")
    def rule_set_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_set_version.setter
    def rule_set_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="anomalyScore")
    def anomaly_score(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @anomaly_score.setter
    def anomaly_score(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleGroupOverrides")
    def rule_group_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleGroupOverrideArgs]]]]:
        
        ...
    
    @rule_group_overrides.setter
    def rule_group_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedRuleGroupOverrideArgs]]]]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MatchConditionArgsDict(TypedDict):
    
    match_value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    match_variable: pulumi.Input[Union[_builtins.str, WafMatchVariable]]
    operator: pulumi.Input[Union[_builtins.str, Operator]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    selector: NotRequired[pulumi.Input[_builtins.str]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, TransformType]]]]]


@pulumi.input_type
class MatchConditionArgs:
    def __init__(__self__, *, match_value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], match_variable: pulumi.Input[Union[_builtins.str, WafMatchVariable]], operator: pulumi.Input[Union[_builtins.str, Operator]], negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., selector: Optional[pulumi.Input[_builtins.str]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, TransformType]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValue")
    def match_value(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @match_value.setter
    def match_value(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchVariable")
    def match_variable(self) -> pulumi.Input[Union[_builtins.str, WafMatchVariable]]:
        
        ...
    
    @match_variable.setter
    def match_variable(self, value: pulumi.Input[Union[_builtins.str, WafMatchVariable]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, Operator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, Operator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @selector.setter
    def selector(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, TransformType]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, TransformType]]]]]): # -> None:
        ...
    


class OriginAuthenticationPropertiesArgsDict(TypedDict):
    
    scope: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, OriginAuthenticationType]]]
    user_assigned_identity: NotRequired[pulumi.Input[ResourceReferenceArgsDict]]


@pulumi.input_type
class OriginAuthenticationPropertiesArgs:
    def __init__(__self__, *, scope: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, OriginAuthenticationType]]] = ..., user_assigned_identity: Optional[pulumi.Input[ResourceReferenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, OriginAuthenticationType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, OriginAuthenticationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]:
        
        ...
    
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[ResourceReferenceArgs]]): # -> None:
        ...
    


class OriginGroupOverrideActionParametersArgsDict(TypedDict):
    
    origin_group: pulumi.Input[ResourceReferenceArgsDict]
    type_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class OriginGroupOverrideActionParametersArgs:
    def __init__(__self__, *, origin_group: pulumi.Input[ResourceReferenceArgs], type_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originGroup")
    def origin_group(self) -> pulumi.Input[ResourceReferenceArgs]:
        
        ...
    
    @origin_group.setter
    def origin_group(self, value: pulumi.Input[ResourceReferenceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class OriginGroupOverrideActionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[OriginGroupOverrideActionParametersArgsDict]


@pulumi.input_type
class OriginGroupOverrideActionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[OriginGroupOverrideActionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[OriginGroupOverrideActionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[OriginGroupOverrideActionParametersArgs]): # -> None:
        ...
    


class OriginGroupOverrideArgsDict(TypedDict):
    
    forwarding_protocol: NotRequired[pulumi.Input[Union[_builtins.str, ForwardingProtocol]]]
    origin_group: NotRequired[pulumi.Input[ResourceReferenceArgsDict]]


@pulumi.input_type
class OriginGroupOverrideArgs:
    def __init__(__self__, *, forwarding_protocol: Optional[pulumi.Input[Union[_builtins.str, ForwardingProtocol]]] = ..., origin_group: Optional[pulumi.Input[ResourceReferenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingProtocol")
    def forwarding_protocol(self) -> Optional[pulumi.Input[Union[_builtins.str, ForwardingProtocol]]]:
        
        ...
    
    @forwarding_protocol.setter
    def forwarding_protocol(self, value: Optional[pulumi.Input[Union[_builtins.str, ForwardingProtocol]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originGroup")
    def origin_group(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]:
        
        ...
    
    @origin_group.setter
    def origin_group(self, value: Optional[pulumi.Input[ResourceReferenceArgs]]): # -> None:
        ...
    


class PolicySettingsArgsDict(TypedDict):
    
    default_custom_block_response_body: NotRequired[pulumi.Input[_builtins.str]]
    default_custom_block_response_status_code: NotRequired[pulumi.Input[_builtins.float]]
    default_redirect_url: NotRequired[pulumi.Input[_builtins.str]]
    enabled_state: NotRequired[pulumi.Input[Union[_builtins.str, PolicyEnabledState]]]
    mode: NotRequired[pulumi.Input[Union[_builtins.str, PolicyMode]]]


@pulumi.input_type
class PolicySettingsArgs:
    def __init__(__self__, *, default_custom_block_response_body: Optional[pulumi.Input[_builtins.str]] = ..., default_custom_block_response_status_code: Optional[pulumi.Input[_builtins.float]] = ..., default_redirect_url: Optional[pulumi.Input[_builtins.str]] = ..., enabled_state: Optional[pulumi.Input[Union[_builtins.str, PolicyEnabledState]]] = ..., mode: Optional[pulumi.Input[Union[_builtins.str, PolicyMode]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCustomBlockResponseBody")
    def default_custom_block_response_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_custom_block_response_body.setter
    def default_custom_block_response_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCustomBlockResponseStatusCode")
    def default_custom_block_response_status_code(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @default_custom_block_response_status_code.setter
    def default_custom_block_response_status_code(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRedirectUrl")
    def default_redirect_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_redirect_url.setter
    def default_redirect_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyEnabledState]]]:
        
        ...
    
    @enabled_state.setter
    def enabled_state(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyEnabledState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyMode]]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyMode]]]): # -> None:
        ...
    


class PostArgsMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, PostArgsOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    selector: NotRequired[pulumi.Input[_builtins.str]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class PostArgsMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, PostArgsOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., selector: Optional[pulumi.Input[_builtins.str]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, PostArgsOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, PostArgsOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @selector.setter
    def selector(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class ProfileLogScrubbingArgsDict(TypedDict):
    
    scrubbing_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[ProfileScrubbingRulesArgsDict]]]]
    state: NotRequired[pulumi.Input[Union[_builtins.str, ProfileScrubbingState]]]


@pulumi.input_type
class ProfileLogScrubbingArgs:
    def __init__(__self__, *, scrubbing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[ProfileScrubbingRulesArgs]]]] = ..., state: Optional[pulumi.Input[Union[_builtins.str, ProfileScrubbingState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scrubbingRules")
    def scrubbing_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProfileScrubbingRulesArgs]]]]:
        
        ...
    
    @scrubbing_rules.setter
    def scrubbing_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ProfileScrubbingRulesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, ProfileScrubbingState]]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, ProfileScrubbingState]]]): # -> None:
        ...
    


class ProfileScrubbingRulesArgsDict(TypedDict):
    
    match_variable: pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchVariable]]
    selector_match_operator: pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchOperator]]
    selector: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryState]]]


@pulumi.input_type
class ProfileScrubbingRulesArgs:
    def __init__(__self__, *, match_variable: pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchVariable]], selector_match_operator: pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchOperator]], selector: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchVariable")
    def match_variable(self) -> pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchVariable]]:
        
        ...
    
    @match_variable.setter
    def match_variable(self, value: pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchVariable]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectorMatchOperator")
    def selector_match_operator(self) -> pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchOperator]]:
        
        ...
    
    @selector_match_operator.setter
    def selector_match_operator(self, value: pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryMatchOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @selector.setter
    def selector(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryState]]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, ScrubbingRuleEntryState]]]): # -> None:
        ...
    


class QueryStringMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, QueryStringOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class QueryStringMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, QueryStringOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, QueryStringOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, QueryStringOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class RateLimitRuleListArgsDict(TypedDict):
    
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[RateLimitRuleArgsDict]]]]


@pulumi.input_type
class RateLimitRuleListArgs:
    def __init__(__self__, *, rules: Optional[pulumi.Input[Sequence[pulumi.Input[RateLimitRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RateLimitRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RateLimitRuleArgs]]]]): # -> None:
        ...
    


class RateLimitRuleArgsDict(TypedDict):
    
    action: pulumi.Input[Union[_builtins.str, ActionType]]
    match_conditions: pulumi.Input[Sequence[pulumi.Input[MatchConditionArgsDict]]]
    name: pulumi.Input[_builtins.str]
    priority: pulumi.Input[_builtins.int]
    rate_limit_duration_in_minutes: pulumi.Input[_builtins.int]
    rate_limit_threshold: pulumi.Input[_builtins.int]
    enabled_state: NotRequired[pulumi.Input[Union[_builtins.str, CustomRuleEnabledState]]]


@pulumi.input_type
class RateLimitRuleArgs:
    def __init__(__self__, *, action: pulumi.Input[Union[_builtins.str, ActionType]], match_conditions: pulumi.Input[Sequence[pulumi.Input[MatchConditionArgs]]], name: pulumi.Input[_builtins.str], priority: pulumi.Input[_builtins.int], rate_limit_duration_in_minutes: pulumi.Input[_builtins.int], rate_limit_threshold: pulumi.Input[_builtins.int], enabled_state: Optional[pulumi.Input[Union[_builtins.str, CustomRuleEnabledState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[Union[_builtins.str, ActionType]]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[Union[_builtins.str, ActionType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchConditions")
    def match_conditions(self) -> pulumi.Input[Sequence[pulumi.Input[MatchConditionArgs]]]:
        
        ...
    
    @match_conditions.setter
    def match_conditions(self, value: pulumi.Input[Sequence[pulumi.Input[MatchConditionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateLimitDurationInMinutes")
    def rate_limit_duration_in_minutes(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @rate_limit_duration_in_minutes.setter
    def rate_limit_duration_in_minutes(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateLimitThreshold")
    def rate_limit_threshold(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @rate_limit_threshold.setter
    def rate_limit_threshold(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[pulumi.Input[Union[_builtins.str, CustomRuleEnabledState]]]:
        
        ...
    
    @enabled_state.setter
    def enabled_state(self, value: Optional[pulumi.Input[Union[_builtins.str, CustomRuleEnabledState]]]): # -> None:
        ...
    


class RemoteAddressMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, RemoteAddressOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class RemoteAddressMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, RemoteAddressOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, RemoteAddressOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, RemoteAddressOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class RequestBodyMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, RequestBodyOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class RequestBodyMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, RequestBodyOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, RequestBodyOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, RequestBodyOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class RequestHeaderMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, RequestHeaderOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    selector: NotRequired[pulumi.Input[_builtins.str]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class RequestHeaderMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, RequestHeaderOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., selector: Optional[pulumi.Input[_builtins.str]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, RequestHeaderOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, RequestHeaderOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def selector(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @selector.setter
    def selector(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class RequestMethodMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, RequestMethodOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RequestMethodMatchValue]]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class RequestMethodMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, RequestMethodOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RequestMethodMatchValue]]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, RequestMethodOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, RequestMethodOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RequestMethodMatchValue]]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RequestMethodMatchValue]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class RequestSchemeMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, RequestSchemeMatchConditionParametersOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RequestSchemeMatchValue]]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class RequestSchemeMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, RequestSchemeMatchConditionParametersOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RequestSchemeMatchValue]]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, RequestSchemeMatchConditionParametersOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, RequestSchemeMatchConditionParametersOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RequestSchemeMatchValue]]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, RequestSchemeMatchValue]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class RequestUriMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, RequestUriOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class RequestUriMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, RequestUriOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, RequestUriOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, RequestUriOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class ResourceReferenceArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourceReferenceArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResponseBasedOriginErrorDetectionParametersArgsDict(TypedDict):
    
    http_error_ranges: NotRequired[pulumi.Input[Sequence[pulumi.Input[HttpErrorRangeParametersArgsDict]]]]
    response_based_detected_error_types: NotRequired[pulumi.Input[ResponseBasedDetectedErrorTypes]]
    response_based_failover_threshold_percentage: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ResponseBasedOriginErrorDetectionParametersArgs:
    def __init__(__self__, *, http_error_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[HttpErrorRangeParametersArgs]]]] = ..., response_based_detected_error_types: Optional[pulumi.Input[ResponseBasedDetectedErrorTypes]] = ..., response_based_failover_threshold_percentage: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpErrorRanges")
    def http_error_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HttpErrorRangeParametersArgs]]]]:
        
        ...
    
    @http_error_ranges.setter
    def http_error_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HttpErrorRangeParametersArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseBasedDetectedErrorTypes")
    def response_based_detected_error_types(self) -> Optional[pulumi.Input[ResponseBasedDetectedErrorTypes]]:
        
        ...
    
    @response_based_detected_error_types.setter
    def response_based_detected_error_types(self, value: Optional[pulumi.Input[ResponseBasedDetectedErrorTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseBasedFailoverThresholdPercentage")
    def response_based_failover_threshold_percentage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @response_based_failover_threshold_percentage.setter
    def response_based_failover_threshold_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class RouteConfigurationOverrideActionParametersArgsDict(TypedDict):
    
    type_name: pulumi.Input[_builtins.str]
    cache_configuration: NotRequired[pulumi.Input[CacheConfigurationArgsDict]]
    origin_group_override: NotRequired[pulumi.Input[OriginGroupOverrideArgsDict]]


@pulumi.input_type
class RouteConfigurationOverrideActionParametersArgs:
    def __init__(__self__, *, type_name: pulumi.Input[_builtins.str], cache_configuration: Optional[pulumi.Input[CacheConfigurationArgs]] = ..., origin_group_override: Optional[pulumi.Input[OriginGroupOverrideArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheConfiguration")
    def cache_configuration(self) -> Optional[pulumi.Input[CacheConfigurationArgs]]:
        
        ...
    
    @cache_configuration.setter
    def cache_configuration(self, value: Optional[pulumi.Input[CacheConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originGroupOverride")
    def origin_group_override(self) -> Optional[pulumi.Input[OriginGroupOverrideArgs]]:
        
        ...
    
    @origin_group_override.setter
    def origin_group_override(self, value: Optional[pulumi.Input[OriginGroupOverrideArgs]]): # -> None:
        ...
    


class SecurityPolicyWebApplicationFirewallAssociationArgsDict(TypedDict):
    
    domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[ActivatedResourceReferenceArgsDict]]]]
    patterns_to_match: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SecurityPolicyWebApplicationFirewallAssociationArgs:
    def __init__(__self__, *, domains: Optional[pulumi.Input[Sequence[pulumi.Input[ActivatedResourceReferenceArgs]]]] = ..., patterns_to_match: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ActivatedResourceReferenceArgs]]]]:
        
        ...
    
    @domains.setter
    def domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ActivatedResourceReferenceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="patternsToMatch")
    def patterns_to_match(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @patterns_to_match.setter
    def patterns_to_match(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SecurityPolicyWebApplicationFirewallParametersArgsDict(TypedDict):
    
    type: pulumi.Input[_builtins.str]
    associations: NotRequired[pulumi.Input[Sequence[pulumi.Input[SecurityPolicyWebApplicationFirewallAssociationArgsDict]]]]
    waf_policy: NotRequired[pulumi.Input[ResourceReferenceArgsDict]]


@pulumi.input_type
class SecurityPolicyWebApplicationFirewallParametersArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], associations: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityPolicyWebApplicationFirewallAssociationArgs]]]] = ..., waf_policy: Optional[pulumi.Input[ResourceReferenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityPolicyWebApplicationFirewallAssociationArgs]]]]:
        
        ...
    
    @associations.setter
    def associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityPolicyWebApplicationFirewallAssociationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="wafPolicy")
    def waf_policy(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]:
        
        ...
    
    @waf_policy.setter
    def waf_policy(self, value: Optional[pulumi.Input[ResourceReferenceArgs]]): # -> None:
        ...
    


class ServerPortMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, ServerPortOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class ServerPortMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, ServerPortOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, ServerPortOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, ServerPortOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class SharedPrivateLinkResourcePropertiesArgsDict(TypedDict):
    
    group_id: NotRequired[pulumi.Input[_builtins.str]]
    private_link: NotRequired[pulumi.Input[ResourceReferenceArgsDict]]
    private_link_location: NotRequired[pulumi.Input[_builtins.str]]
    request_message: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[SharedPrivateLinkResourceStatus]]


@pulumi.input_type
class SharedPrivateLinkResourcePropertiesArgs:
    def __init__(__self__, *, group_id: Optional[pulumi.Input[_builtins.str]] = ..., private_link: Optional[pulumi.Input[ResourceReferenceArgs]] = ..., private_link_location: Optional[pulumi.Input[_builtins.str]] = ..., request_message: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[SharedPrivateLinkResourceStatus]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLink")
    def private_link(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]:
        
        ...
    
    @private_link.setter
    def private_link(self, value: Optional[pulumi.Input[ResourceReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkLocation")
    def private_link_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_link_location.setter
    def private_link_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_message.setter
    def request_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[SharedPrivateLinkResourceStatus]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[SharedPrivateLinkResourceStatus]]): # -> None:
        ...
    


class SkuTypeArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    tier: pulumi.Input[_builtins.str]


@pulumi.input_type
class SkuTypeArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], tier: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tier.setter
    def tier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SkuArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[Union[_builtins.str, SkuName]]]


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[Union[_builtins.str, SkuName]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, SkuName]]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, SkuName]]]): # -> None:
        ...
    


class SocketAddrMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, SocketAddrOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class SocketAddrMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, SocketAddrOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, SocketAddrOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, SocketAddrOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class SslProtocolMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, SslProtocolOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SslProtocol]]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class SslProtocolMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, SslProtocolOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SslProtocol]]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, SslProtocolOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, SslProtocolOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SslProtocol]]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, SslProtocol]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class TargetEndpointArgsDict(TypedDict):
    
    ports: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    target_fqdn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TargetEndpointArgs:
    def __init__(__self__, *, ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., target_fqdn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @ports.setter
    def ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFqdn")
    def target_fqdn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_fqdn.setter
    def target_fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class UrlFileExtensionMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, UrlFileExtensionOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class UrlFileExtensionMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, UrlFileExtensionOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, UrlFileExtensionOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, UrlFileExtensionOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class UrlFileNameMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, UrlFileNameOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class UrlFileNameMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, UrlFileNameOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, UrlFileNameOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, UrlFileNameOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class UrlPathMatchConditionParametersArgsDict(TypedDict):
    
    operator: pulumi.Input[Union[_builtins.str, UrlPathOperator]]
    type_name: pulumi.Input[_builtins.str]
    match_values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    negate_condition: NotRequired[pulumi.Input[_builtins.bool]]
    transforms: NotRequired[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]


@pulumi.input_type
class UrlPathMatchConditionParametersArgs:
    def __init__(__self__, *, operator: pulumi.Input[Union[_builtins.str, UrlPathOperator]], type_name: pulumi.Input[_builtins.str], match_values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate_condition: Optional[pulumi.Input[_builtins.bool]] = ..., transforms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, UrlPathOperator]]:
        
        ...
    
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, UrlPathOperator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchValues")
    def match_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @match_values.setter
    def match_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="negateCondition")
    def negate_condition(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate_condition.setter
    def negate_condition(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]:
        
        ...
    
    @transforms.setter
    def transforms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Transform]]]]]): # -> None:
        ...
    


class UrlRedirectActionParametersArgsDict(TypedDict):
    
    redirect_type: pulumi.Input[Union[_builtins.str, RedirectType]]
    type_name: pulumi.Input[_builtins.str]
    custom_fragment: NotRequired[pulumi.Input[_builtins.str]]
    custom_hostname: NotRequired[pulumi.Input[_builtins.str]]
    custom_path: NotRequired[pulumi.Input[_builtins.str]]
    custom_query_string: NotRequired[pulumi.Input[_builtins.str]]
    destination_protocol: NotRequired[pulumi.Input[Union[_builtins.str, DestinationProtocol]]]


@pulumi.input_type
class UrlRedirectActionParametersArgs:
    def __init__(__self__, *, redirect_type: pulumi.Input[Union[_builtins.str, RedirectType]], type_name: pulumi.Input[_builtins.str], custom_fragment: Optional[pulumi.Input[_builtins.str]] = ..., custom_hostname: Optional[pulumi.Input[_builtins.str]] = ..., custom_path: Optional[pulumi.Input[_builtins.str]] = ..., custom_query_string: Optional[pulumi.Input[_builtins.str]] = ..., destination_protocol: Optional[pulumi.Input[Union[_builtins.str, DestinationProtocol]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectType")
    def redirect_type(self) -> pulumi.Input[Union[_builtins.str, RedirectType]]:
        
        ...
    
    @redirect_type.setter
    def redirect_type(self, value: pulumi.Input[Union[_builtins.str, RedirectType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customFragment")
    def custom_fragment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_fragment.setter
    def custom_fragment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHostname")
    def custom_hostname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_hostname.setter
    def custom_hostname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPath")
    def custom_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_path.setter
    def custom_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customQueryString")
    def custom_query_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_query_string.setter
    def custom_query_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationProtocol")
    def destination_protocol(self) -> Optional[pulumi.Input[Union[_builtins.str, DestinationProtocol]]]:
        
        ...
    
    @destination_protocol.setter
    def destination_protocol(self, value: Optional[pulumi.Input[Union[_builtins.str, DestinationProtocol]]]): # -> None:
        ...
    


class UrlRedirectActionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[UrlRedirectActionParametersArgsDict]


@pulumi.input_type
class UrlRedirectActionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[UrlRedirectActionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[UrlRedirectActionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[UrlRedirectActionParametersArgs]): # -> None:
        ...
    


class UrlRewriteActionParametersArgsDict(TypedDict):
    
    destination: pulumi.Input[_builtins.str]
    source_pattern: pulumi.Input[_builtins.str]
    type_name: pulumi.Input[_builtins.str]
    preserve_unmatched_path: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class UrlRewriteActionParametersArgs:
    def __init__(__self__, *, destination: pulumi.Input[_builtins.str], source_pattern: pulumi.Input[_builtins.str], type_name: pulumi.Input[_builtins.str], preserve_unmatched_path: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePattern")
    def source_pattern(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_pattern.setter
    def source_pattern(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveUnmatchedPath")
    def preserve_unmatched_path(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @preserve_unmatched_path.setter
    def preserve_unmatched_path(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class UrlRewriteActionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[UrlRewriteActionParametersArgsDict]


@pulumi.input_type
class UrlRewriteActionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[UrlRewriteActionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[UrlRewriteActionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[UrlRewriteActionParametersArgs]): # -> None:
        ...
    


class UrlSigningActionParametersArgsDict(TypedDict):
    
    type_name: pulumi.Input[_builtins.str]
    algorithm: NotRequired[pulumi.Input[Union[_builtins.str, Algorithm]]]
    parameter_name_override: NotRequired[pulumi.Input[Sequence[pulumi.Input[UrlSigningParamIdentifierArgsDict]]]]


@pulumi.input_type
class UrlSigningActionParametersArgs:
    def __init__(__self__, *, type_name: pulumi.Input[_builtins.str], algorithm: Optional[pulumi.Input[Union[_builtins.str, Algorithm]]] = ..., parameter_name_override: Optional[pulumi.Input[Sequence[pulumi.Input[UrlSigningParamIdentifierArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input[Union[_builtins.str, Algorithm]]]:
        
        ...
    
    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input[Union[_builtins.str, Algorithm]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterNameOverride")
    def parameter_name_override(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UrlSigningParamIdentifierArgs]]]]:
        
        ...
    
    @parameter_name_override.setter
    def parameter_name_override(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UrlSigningParamIdentifierArgs]]]]): # -> None:
        ...
    


class UrlSigningActionArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    parameters: pulumi.Input[UrlSigningActionParametersArgsDict]


@pulumi.input_type
class UrlSigningActionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], parameters: pulumi.Input[UrlSigningActionParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[UrlSigningActionParametersArgs]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[UrlSigningActionParametersArgs]): # -> None:
        ...
    


class UrlSigningKeyParametersArgsDict(TypedDict):
    
    key_id: pulumi.Input[_builtins.str]
    secret_source: pulumi.Input[ResourceReferenceArgsDict]
    secret_version: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class UrlSigningKeyParametersArgs:
    def __init__(__self__, *, key_id: pulumi.Input[_builtins.str], secret_source: pulumi.Input[ResourceReferenceArgs], secret_version: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_id.setter
    def key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretSource")
    def secret_source(self) -> pulumi.Input[ResourceReferenceArgs]:
        
        ...
    
    @secret_source.setter
    def secret_source(self, value: pulumi.Input[ResourceReferenceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class UrlSigningKeyArgsDict(TypedDict):
    
    key_id: pulumi.Input[_builtins.str]
    key_source_parameters: pulumi.Input[KeyVaultSigningKeyParametersArgsDict]


@pulumi.input_type
class UrlSigningKeyArgs:
    def __init__(__self__, *, key_id: pulumi.Input[_builtins.str], key_source_parameters: pulumi.Input[KeyVaultSigningKeyParametersArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_id.setter
    def key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySourceParameters")
    def key_source_parameters(self) -> pulumi.Input[KeyVaultSigningKeyParametersArgs]:
        
        ...
    
    @key_source_parameters.setter
    def key_source_parameters(self, value: pulumi.Input[KeyVaultSigningKeyParametersArgs]): # -> None:
        ...
    


class UrlSigningParamIdentifierArgsDict(TypedDict):
    
    param_indicator: pulumi.Input[Union[_builtins.str, ParamIndicator]]
    param_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class UrlSigningParamIdentifierArgs:
    def __init__(__self__, *, param_indicator: pulumi.Input[Union[_builtins.str, ParamIndicator]], param_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="paramIndicator")
    def param_indicator(self) -> pulumi.Input[Union[_builtins.str, ParamIndicator]]:
        
        ...
    
    @param_indicator.setter
    def param_indicator(self, value: pulumi.Input[Union[_builtins.str, ParamIndicator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="paramName")
    def param_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @param_name.setter
    def param_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


