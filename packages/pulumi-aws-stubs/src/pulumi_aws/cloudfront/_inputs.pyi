

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AnycastIpListTimeoutsArgs', 'AnycastIpListTimeoutsArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'ConnectionFunctionConnectionFunctionConfigArgs', 'ConnectionFunctionConnectionFunctionConfigArgsDict', ..., ..., 'ConnectionGroupTimeoutsArgs', 'ConnectionGroupTimeoutsArgsDict', ..., ..., 'ContinuousDeploymentPolicyTrafficConfigArgs', 'ContinuousDeploymentPolicyTrafficConfigArgsDict', ..., ..., ..., ..., ..., ..., 'DistributionConnectionFunctionAssociationArgs', 'DistributionConnectionFunctionAssociationArgsDict', 'DistributionCustomErrorResponseArgs', 'DistributionCustomErrorResponseArgsDict', 'DistributionDefaultCacheBehaviorArgs', 'DistributionDefaultCacheBehaviorArgsDict', ..., ..., ..., ..., ..., ..., 'DistributionDefaultCacheBehaviorGrpcConfigArgs', 'DistributionDefaultCacheBehaviorGrpcConfigArgsDict', ..., ..., 'DistributionLoggingConfigArgs', 'DistributionLoggingConfigArgsDict', 'DistributionOrderedCacheBehaviorArgs', 'DistributionOrderedCacheBehaviorArgsDict', ..., ..., ..., ..., ..., ..., 'DistributionOrderedCacheBehaviorGrpcConfigArgs', 'DistributionOrderedCacheBehaviorGrpcConfigArgsDict', ..., ..., 'DistributionOriginArgs', 'DistributionOriginArgsDict', 'DistributionOriginCustomHeaderArgs', 'DistributionOriginCustomHeaderArgsDict', 'DistributionOriginCustomOriginConfigArgs', 'DistributionOriginCustomOriginConfigArgsDict', 'DistributionOriginGroupArgs', 'DistributionOriginGroupArgsDict', 'DistributionOriginGroupFailoverCriteriaArgs', 'DistributionOriginGroupFailoverCriteriaArgsDict', 'DistributionOriginGroupMemberArgs', 'DistributionOriginGroupMemberArgsDict', 'DistributionOriginOriginShieldArgs', 'DistributionOriginOriginShieldArgsDict', 'DistributionOriginS3OriginConfigArgs', 'DistributionOriginS3OriginConfigArgsDict', 'DistributionOriginVpcOriginConfigArgs', 'DistributionOriginVpcOriginConfigArgsDict', 'DistributionRestrictionsArgs', 'DistributionRestrictionsArgsDict', 'DistributionRestrictionsGeoRestrictionArgs', 'DistributionRestrictionsGeoRestrictionArgsDict', 'DistributionTenantCustomizationsArgs', 'DistributionTenantCustomizationsArgsDict', 'DistributionTenantCustomizationsCertificateArgs', ..., 'DistributionTenantCustomizationsGeoRestrictionArgs', ..., 'DistributionTenantCustomizationsWebAclArgs', 'DistributionTenantCustomizationsWebAclArgsDict', 'DistributionTenantDomainArgs', 'DistributionTenantDomainArgsDict', 'DistributionTenantManagedCertificateRequestArgs', ..., 'DistributionTenantParameterArgs', 'DistributionTenantParameterArgsDict', 'DistributionTenantTimeoutsArgs', 'DistributionTenantTimeoutsArgsDict', 'DistributionTrustedKeyGroupArgs', 'DistributionTrustedKeyGroupArgsDict', 'DistributionTrustedKeyGroupItemArgs', 'DistributionTrustedKeyGroupItemArgsDict', 'DistributionTrustedSignerArgs', 'DistributionTrustedSignerArgsDict', 'DistributionTrustedSignerItemArgs', 'DistributionTrustedSignerItemArgsDict', 'DistributionViewerCertificateArgs', 'DistributionViewerCertificateArgsDict', 'DistributionViewerMtlsConfigArgs', 'DistributionViewerMtlsConfigArgsDict', 'DistributionViewerMtlsConfigTrustStoreConfigArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FieldLevelEncryptionProfileEncryptionEntitiesArgs', ..., ..., ..., ..., ..., 'KeyValueStoreTimeoutsArgs', 'KeyValueStoreTimeoutsArgsDict', 'KeyvaluestoreKeysExclusiveResourceKeyValuePairArgs', ..., 'MonitoringSubscriptionMonitoringSubscriptionArgs', ..., ..., ..., 'MultitenantDistributionActiveTrustedKeyGroupArgs', ..., ..., ..., 'MultitenantDistributionCacheBehaviorArgs', 'MultitenantDistributionCacheBehaviorArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'MultitenantDistributionCustomErrorResponseArgs', 'MultitenantDistributionCustomErrorResponseArgsDict', 'MultitenantDistributionDefaultCacheBehaviorArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'MultitenantDistributionOriginArgs', 'MultitenantDistributionOriginArgsDict', 'MultitenantDistributionOriginCustomHeaderArgs', 'MultitenantDistributionOriginCustomHeaderArgsDict', ..., ..., 'MultitenantDistributionOriginGroupArgs', 'MultitenantDistributionOriginGroupArgsDict', ..., ..., 'MultitenantDistributionOriginGroupMemberArgs', 'MultitenantDistributionOriginGroupMemberArgsDict', 'MultitenantDistributionOriginOriginShieldArgs', 'MultitenantDistributionOriginOriginShieldArgsDict', 'MultitenantDistributionOriginVpcOriginConfigArgs', ..., 'MultitenantDistributionRestrictionsArgs', 'MultitenantDistributionRestrictionsArgsDict', ..., ..., 'MultitenantDistributionTenantConfigArgs', 'MultitenantDistributionTenantConfigArgsDict', ..., ..., ..., ..., ..., ..., 'MultitenantDistributionTimeoutsArgs', 'MultitenantDistributionTimeoutsArgsDict', 'MultitenantDistributionViewerCertificateArgs', 'MultitenantDistributionViewerCertificateArgsDict', 'OriginRequestPolicyCookiesConfigArgs', 'OriginRequestPolicyCookiesConfigArgsDict', 'OriginRequestPolicyCookiesConfigCookiesArgs', 'OriginRequestPolicyCookiesConfigCookiesArgsDict', 'OriginRequestPolicyHeadersConfigArgs', 'OriginRequestPolicyHeadersConfigArgsDict', 'OriginRequestPolicyHeadersConfigHeadersArgs', 'OriginRequestPolicyHeadersConfigHeadersArgsDict', 'OriginRequestPolicyQueryStringsConfigArgs', 'OriginRequestPolicyQueryStringsConfigArgsDict', ..., ..., 'RealtimeLogConfigEndpointArgs', 'RealtimeLogConfigEndpointArgsDict', 'RealtimeLogConfigEndpointKinesisStreamConfigArgs', ..., 'ResponseHeadersPolicyCorsConfigArgs', 'ResponseHeadersPolicyCorsConfigArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'ResponseHeadersPolicyCustomHeadersConfigArgs', 'ResponseHeadersPolicyCustomHeadersConfigArgsDict', 'ResponseHeadersPolicyCustomHeadersConfigItemArgs', ..., 'ResponseHeadersPolicyRemoveHeadersConfigArgs', 'ResponseHeadersPolicyRemoveHeadersConfigArgsDict', 'ResponseHeadersPolicyRemoveHeadersConfigItemArgs', ..., 'ResponseHeadersPolicySecurityHeadersConfigArgs', 'ResponseHeadersPolicySecurityHeadersConfigArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'ResponseHeadersPolicyServerTimingHeadersConfigArgs', ..., 'TrustStoreCaCertificatesBundleSourceArgs', 'TrustStoreCaCertificatesBundleSourceArgsDict', ..., ..., 'TrustStoreTimeoutsArgs', 'TrustStoreTimeoutsArgsDict', 'VpcOriginTimeoutsArgs', 'VpcOriginTimeoutsArgsDict', 'VpcOriginVpcOriginEndpointConfigArgs', 'VpcOriginVpcOriginEndpointConfigArgsDict', ..., ...]
class AnycastIpListTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AnycastIpListTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CachePolicyParametersInCacheKeyAndForwardedToOriginArgsDict(TypedDict):
    cookies_config: pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigArgsDict]
    headers_config: pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigArgsDict]
    query_strings_config: pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigArgsDict]
    enable_accept_encoding_brotli: NotRequired[pulumi.Input[_builtins.bool]]
    enable_accept_encoding_gzip: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginArgs:
    def __init__(__self__, *, cookies_config: pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigArgs], headers_config: pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigArgs], query_strings_config: pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigArgs], enable_accept_encoding_brotli: Optional[pulumi.Input[_builtins.bool]] = ..., enable_accept_encoding_gzip: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookiesConfig")
    def cookies_config(self) -> pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigArgs]:
        
        ...
    
    @cookies_config.setter
    def cookies_config(self, value: pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headersConfig")
    def headers_config(self) -> pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigArgs]:
        
        ...
    
    @headers_config.setter
    def headers_config(self, value: pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringsConfig")
    def query_strings_config(self) -> pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigArgs]:
        
        ...
    
    @query_strings_config.setter
    def query_strings_config(self, value: pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceptEncodingBrotli")
    def enable_accept_encoding_brotli(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_accept_encoding_brotli.setter
    def enable_accept_encoding_brotli(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAcceptEncodingGzip")
    def enable_accept_encoding_gzip(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_accept_encoding_gzip.setter
    def enable_accept_encoding_gzip(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigArgsDict(TypedDict):
    cookie_behavior: pulumi.Input[_builtins.str]
    cookies: NotRequired[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookiesArgsDict]]


@pulumi.input_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigArgs:
    def __init__(__self__, *, cookie_behavior: pulumi.Input[_builtins.str], cookies: Optional[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookieBehavior")
    def cookie_behavior(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cookie_behavior.setter
    def cookie_behavior(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookiesArgs]]:
        
        ...
    
    @cookies.setter
    def cookies(self, value: Optional[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookiesArgs]]): # -> None:
        ...
    


class CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookiesArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginCookiesConfigCookiesArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigArgsDict(TypedDict):
    header_behavior: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeadersArgsDict]]


@pulumi.input_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigArgs:
    def __init__(__self__, *, header_behavior: Optional[pulumi.Input[_builtins.str]] = ..., headers: Optional[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeadersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerBehavior")
    def header_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @header_behavior.setter
    def header_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeadersArgs]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeadersArgs]]): # -> None:
        ...
    


class CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeadersArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginHeadersConfigHeadersArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigArgsDict(TypedDict):
    query_string_behavior: pulumi.Input[_builtins.str]
    query_strings: NotRequired[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringsArgsDict]]


@pulumi.input_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigArgs:
    def __init__(__self__, *, query_string_behavior: pulumi.Input[_builtins.str], query_strings: Optional[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringBehavior")
    def query_string_behavior(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @query_string_behavior.setter
    def query_string_behavior(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(self) -> Optional[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringsArgs]]:
        
        ...
    
    @query_strings.setter
    def query_strings(self, value: Optional[pulumi.Input[CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringsArgs]]): # -> None:
        ...
    


class CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringsArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CachePolicyParametersInCacheKeyAndForwardedToOriginQueryStringsConfigQueryStringsArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ConnectionFunctionConnectionFunctionConfigArgsDict(TypedDict):
    comment: pulumi.Input[_builtins.str]
    runtime: pulumi.Input[_builtins.str]
    key_value_store_association: NotRequired[pulumi.Input[ConnectionFunctionConnectionFunctionConfigKeyValueStoreAssociationArgsDict]]


@pulumi.input_type
class ConnectionFunctionConnectionFunctionConfigArgs:
    def __init__(__self__, *, comment: pulumi.Input[_builtins.str], runtime: pulumi.Input[_builtins.str], key_value_store_association: Optional[pulumi.Input[ConnectionFunctionConnectionFunctionConfigKeyValueStoreAssociationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @comment.setter
    def comment(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @runtime.setter
    def runtime(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyValueStoreAssociation")
    def key_value_store_association(self) -> Optional[pulumi.Input[ConnectionFunctionConnectionFunctionConfigKeyValueStoreAssociationArgs]]:
        
        ...
    
    @key_value_store_association.setter
    def key_value_store_association(self, value: Optional[pulumi.Input[ConnectionFunctionConnectionFunctionConfigKeyValueStoreAssociationArgs]]): # -> None:
        ...
    


class ConnectionFunctionConnectionFunctionConfigKeyValueStoreAssociationArgsDict(TypedDict):
    key_value_store_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectionFunctionConnectionFunctionConfigKeyValueStoreAssociationArgs:
    def __init__(__self__, *, key_value_store_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyValueStoreArn")
    def key_value_store_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_value_store_arn.setter
    def key_value_store_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectionGroupTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionGroupTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContinuousDeploymentPolicyStagingDistributionDnsNamesArgsDict(TypedDict):
    quantity: pulumi.Input[_builtins.int]
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ContinuousDeploymentPolicyStagingDistributionDnsNamesArgs:
    def __init__(__self__, *, quantity: pulumi.Input[_builtins.int], items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def quantity(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @quantity.setter
    def quantity(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ContinuousDeploymentPolicyTrafficConfigArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    single_header_config: NotRequired[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigSingleHeaderConfigArgsDict]]
    single_weight_config: NotRequired[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigArgsDict]]


@pulumi.input_type
class ContinuousDeploymentPolicyTrafficConfigArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], single_header_config: Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigSingleHeaderConfigArgs]] = ..., single_weight_config: Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeaderConfig")
    def single_header_config(self) -> Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigSingleHeaderConfigArgs]]:
        
        ...
    
    @single_header_config.setter
    def single_header_config(self, value: Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigSingleHeaderConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleWeightConfig")
    def single_weight_config(self) -> Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigArgs]]:
        
        ...
    
    @single_weight_config.setter
    def single_weight_config(self, value: Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigArgs]]): # -> None:
        ...
    


class ContinuousDeploymentPolicyTrafficConfigSingleHeaderConfigArgsDict(TypedDict):
    header: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class ContinuousDeploymentPolicyTrafficConfigSingleHeaderConfigArgs:
    def __init__(__self__, *, header: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @header.setter
    def header(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigArgsDict(TypedDict):
    weight: pulumi.Input[_builtins.float]
    session_stickiness_config: NotRequired[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigSessionStickinessConfigArgsDict]]


@pulumi.input_type
class ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigArgs:
    def __init__(__self__, *, weight: pulumi.Input[_builtins.float], session_stickiness_config: Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigSessionStickinessConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @weight.setter
    def weight(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionStickinessConfig")
    def session_stickiness_config(self) -> Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigSessionStickinessConfigArgs]]:
        
        ...
    
    @session_stickiness_config.setter
    def session_stickiness_config(self, value: Optional[pulumi.Input[ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigSessionStickinessConfigArgs]]): # -> None:
        ...
    


class ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigSessionStickinessConfigArgsDict(TypedDict):
    idle_ttl: pulumi.Input[_builtins.int]
    maximum_ttl: pulumi.Input[_builtins.int]


@pulumi.input_type
class ContinuousDeploymentPolicyTrafficConfigSingleWeightConfigSessionStickinessConfigArgs:
    def __init__(__self__, *, idle_ttl: pulumi.Input[_builtins.int], maximum_ttl: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleTtl")
    def idle_ttl(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @idle_ttl.setter
    def idle_ttl(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumTtl")
    def maximum_ttl(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @maximum_ttl.setter
    def maximum_ttl(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class DistributionConnectionFunctionAssociationArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]


@pulumi.input_type
class DistributionConnectionFunctionAssociationArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DistributionCustomErrorResponseArgsDict(TypedDict):
    error_code: pulumi.Input[_builtins.int]
    error_caching_min_ttl: NotRequired[pulumi.Input[_builtins.int]]
    response_code: NotRequired[pulumi.Input[_builtins.int]]
    response_page_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionCustomErrorResponseArgs:
    def __init__(__self__, *, error_code: pulumi.Input[_builtins.int], error_caching_min_ttl: Optional[pulumi.Input[_builtins.int]] = ..., response_code: Optional[pulumi.Input[_builtins.int]] = ..., response_page_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @error_code.setter
    def error_code(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCachingMinTtl")
    def error_caching_min_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @error_caching_min_ttl.setter
    def error_caching_min_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @response_code.setter
    def response_code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responsePagePath")
    def response_page_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @response_page_path.setter
    def response_page_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionDefaultCacheBehaviorArgsDict(TypedDict):
    allowed_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    cached_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    target_origin_id: pulumi.Input[_builtins.str]
    viewer_protocol_policy: pulumi.Input[_builtins.str]
    cache_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    compress: NotRequired[pulumi.Input[_builtins.bool]]
    default_ttl: NotRequired[pulumi.Input[_builtins.int]]
    field_level_encryption_id: NotRequired[pulumi.Input[_builtins.str]]
    forwarded_values: NotRequired[pulumi.Input[DistributionDefaultCacheBehaviorForwardedValuesArgsDict]]
    function_associations: NotRequired[pulumi.Input[Sequence[pulumi.Input[DistributionDefaultCacheBehaviorFunctionAssociationArgsDict]]]]
    grpc_config: NotRequired[pulumi.Input[DistributionDefaultCacheBehaviorGrpcConfigArgsDict]]
    lambda_function_associations: NotRequired[pulumi.Input[Sequence[pulumi.Input[DistributionDefaultCacheBehaviorLambdaFunctionAssociationArgsDict]]]]
    max_ttl: NotRequired[pulumi.Input[_builtins.int]]
    min_ttl: NotRequired[pulumi.Input[_builtins.int]]
    origin_request_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    realtime_log_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    response_headers_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    smooth_streaming: NotRequired[pulumi.Input[_builtins.bool]]
    trusted_key_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    trusted_signers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DistributionDefaultCacheBehaviorArgs:
    def __init__(__self__, *, allowed_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], cached_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], target_origin_id: pulumi.Input[_builtins.str], viewer_protocol_policy: pulumi.Input[_builtins.str], cache_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., compress: Optional[pulumi.Input[_builtins.bool]] = ..., default_ttl: Optional[pulumi.Input[_builtins.int]] = ..., field_level_encryption_id: Optional[pulumi.Input[_builtins.str]] = ..., forwarded_values: Optional[pulumi.Input[DistributionDefaultCacheBehaviorForwardedValuesArgs]] = ..., function_associations: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionDefaultCacheBehaviorFunctionAssociationArgs]]]] = ..., grpc_config: Optional[pulumi.Input[DistributionDefaultCacheBehaviorGrpcConfigArgs]] = ..., lambda_function_associations: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionDefaultCacheBehaviorLambdaFunctionAssociationArgs]]]] = ..., max_ttl: Optional[pulumi.Input[_builtins.int]] = ..., min_ttl: Optional[pulumi.Input[_builtins.int]] = ..., origin_request_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., realtime_log_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., response_headers_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., smooth_streaming: Optional[pulumi.Input[_builtins.bool]] = ..., trusted_key_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., trusted_signers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_methods.setter
    def allowed_methods(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachedMethods")
    def cached_methods(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @cached_methods.setter
    def cached_methods(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetOriginId")
    def target_origin_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_origin_id.setter
    def target_origin_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewerProtocolPolicy")
    def viewer_protocol_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @viewer_protocol_policy.setter
    def viewer_protocol_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachePolicyId")
    def cache_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_policy_id.setter
    def cache_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def compress(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @compress.setter
    def compress(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldLevelEncryptionId")
    def field_level_encryption_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @field_level_encryption_id.setter
    def field_level_encryption_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedValues")
    def forwarded_values(self) -> Optional[pulumi.Input[DistributionDefaultCacheBehaviorForwardedValuesArgs]]:
        
        ...
    
    @forwarded_values.setter
    def forwarded_values(self, value: Optional[pulumi.Input[DistributionDefaultCacheBehaviorForwardedValuesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAssociations")
    def function_associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionDefaultCacheBehaviorFunctionAssociationArgs]]]]:
        
        ...
    
    @function_associations.setter
    def function_associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionDefaultCacheBehaviorFunctionAssociationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcConfig")
    def grpc_config(self) -> Optional[pulumi.Input[DistributionDefaultCacheBehaviorGrpcConfigArgs]]:
        
        ...
    
    @grpc_config.setter
    def grpc_config(self, value: Optional[pulumi.Input[DistributionDefaultCacheBehaviorGrpcConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionAssociations")
    def lambda_function_associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionDefaultCacheBehaviorLambdaFunctionAssociationArgs]]]]:
        
        ...
    
    @lambda_function_associations.setter
    def lambda_function_associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionDefaultCacheBehaviorLambdaFunctionAssociationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_ttl.setter
    def max_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTtl")
    def min_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_ttl.setter
    def min_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originRequestPolicyId")
    def origin_request_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_request_policy_id.setter
    def origin_request_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="realtimeLogConfigArn")
    def realtime_log_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @realtime_log_config_arn.setter
    def realtime_log_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeadersPolicyId")
    def response_headers_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @response_headers_policy_id.setter
    def response_headers_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smoothStreaming")
    def smooth_streaming(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @smooth_streaming.setter
    def smooth_streaming(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedKeyGroups")
    def trusted_key_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @trusted_key_groups.setter
    def trusted_key_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedSigners")
    def trusted_signers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @trusted_signers.setter
    def trusted_signers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DistributionDefaultCacheBehaviorForwardedValuesArgsDict(TypedDict):
    cookies: pulumi.Input[DistributionDefaultCacheBehaviorForwardedValuesCookiesArgsDict]
    query_string: pulumi.Input[_builtins.bool]
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    query_string_cache_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DistributionDefaultCacheBehaviorForwardedValuesArgs:
    def __init__(__self__, *, cookies: pulumi.Input[DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs], query_string: pulumi.Input[_builtins.bool], headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., query_string_cache_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> pulumi.Input[DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs]:
        
        ...
    
    @cookies.setter
    def cookies(self, value: pulumi.Input[DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @query_string.setter
    def query_string(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringCacheKeys")
    def query_string_cache_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @query_string_cache_keys.setter
    def query_string_cache_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DistributionDefaultCacheBehaviorForwardedValuesCookiesArgsDict(TypedDict):
    forward: pulumi.Input[_builtins.str]
    whitelisted_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs:
    def __init__(__self__, *, forward: pulumi.Input[_builtins.str], whitelisted_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def forward(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @forward.setter
    def forward(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="whitelistedNames")
    def whitelisted_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @whitelisted_names.setter
    def whitelisted_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DistributionDefaultCacheBehaviorFunctionAssociationArgsDict(TypedDict):
    event_type: pulumi.Input[_builtins.str]
    function_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class DistributionDefaultCacheBehaviorFunctionAssociationArgs:
    def __init__(__self__, *, event_type: pulumi.Input[_builtins.str], function_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @function_arn.setter
    def function_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DistributionDefaultCacheBehaviorGrpcConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DistributionDefaultCacheBehaviorGrpcConfigArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DistributionDefaultCacheBehaviorLambdaFunctionAssociationArgsDict(TypedDict):
    event_type: pulumi.Input[_builtins.str]
    lambda_arn: pulumi.Input[_builtins.str]
    include_body: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DistributionDefaultCacheBehaviorLambdaFunctionAssociationArgs:
    def __init__(__self__, *, event_type: pulumi.Input[_builtins.str], lambda_arn: pulumi.Input[_builtins.str], include_body: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @lambda_arn.setter
    def lambda_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeBody")
    def include_body(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_body.setter
    def include_body(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DistributionLoggingConfigArgsDict(TypedDict):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    include_cookies: NotRequired[pulumi.Input[_builtins.bool]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionLoggingConfigArgs:
    def __init__(__self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ..., include_cookies: Optional[pulumi.Input[_builtins.bool]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeCookies")
    def include_cookies(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_cookies.setter
    def include_cookies(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionOrderedCacheBehaviorArgsDict(TypedDict):
    allowed_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    cached_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    path_pattern: pulumi.Input[_builtins.str]
    target_origin_id: pulumi.Input[_builtins.str]
    viewer_protocol_policy: pulumi.Input[_builtins.str]
    cache_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    compress: NotRequired[pulumi.Input[_builtins.bool]]
    default_ttl: NotRequired[pulumi.Input[_builtins.int]]
    field_level_encryption_id: NotRequired[pulumi.Input[_builtins.str]]
    forwarded_values: NotRequired[pulumi.Input[DistributionOrderedCacheBehaviorForwardedValuesArgsDict]]
    function_associations: NotRequired[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorFunctionAssociationArgsDict]]]]
    grpc_config: NotRequired[pulumi.Input[DistributionOrderedCacheBehaviorGrpcConfigArgsDict]]
    lambda_function_associations: NotRequired[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorLambdaFunctionAssociationArgsDict]]]]
    max_ttl: NotRequired[pulumi.Input[_builtins.int]]
    min_ttl: NotRequired[pulumi.Input[_builtins.int]]
    origin_request_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    realtime_log_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    response_headers_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    smooth_streaming: NotRequired[pulumi.Input[_builtins.bool]]
    trusted_key_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    trusted_signers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DistributionOrderedCacheBehaviorArgs:
    def __init__(__self__, *, allowed_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], cached_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], path_pattern: pulumi.Input[_builtins.str], target_origin_id: pulumi.Input[_builtins.str], viewer_protocol_policy: pulumi.Input[_builtins.str], cache_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., compress: Optional[pulumi.Input[_builtins.bool]] = ..., default_ttl: Optional[pulumi.Input[_builtins.int]] = ..., field_level_encryption_id: Optional[pulumi.Input[_builtins.str]] = ..., forwarded_values: Optional[pulumi.Input[DistributionOrderedCacheBehaviorForwardedValuesArgs]] = ..., function_associations: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorFunctionAssociationArgs]]]] = ..., grpc_config: Optional[pulumi.Input[DistributionOrderedCacheBehaviorGrpcConfigArgs]] = ..., lambda_function_associations: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorLambdaFunctionAssociationArgs]]]] = ..., max_ttl: Optional[pulumi.Input[_builtins.int]] = ..., min_ttl: Optional[pulumi.Input[_builtins.int]] = ..., origin_request_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., realtime_log_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., response_headers_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., smooth_streaming: Optional[pulumi.Input[_builtins.bool]] = ..., trusted_key_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., trusted_signers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_methods.setter
    def allowed_methods(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachedMethods")
    def cached_methods(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @cached_methods.setter
    def cached_methods(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathPattern")
    def path_pattern(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path_pattern.setter
    def path_pattern(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetOriginId")
    def target_origin_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_origin_id.setter
    def target_origin_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewerProtocolPolicy")
    def viewer_protocol_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @viewer_protocol_policy.setter
    def viewer_protocol_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachePolicyId")
    def cache_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_policy_id.setter
    def cache_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def compress(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @compress.setter
    def compress(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldLevelEncryptionId")
    def field_level_encryption_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @field_level_encryption_id.setter
    def field_level_encryption_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedValues")
    def forwarded_values(self) -> Optional[pulumi.Input[DistributionOrderedCacheBehaviorForwardedValuesArgs]]:
        
        ...
    
    @forwarded_values.setter
    def forwarded_values(self, value: Optional[pulumi.Input[DistributionOrderedCacheBehaviorForwardedValuesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAssociations")
    def function_associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorFunctionAssociationArgs]]]]:
        
        ...
    
    @function_associations.setter
    def function_associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorFunctionAssociationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcConfig")
    def grpc_config(self) -> Optional[pulumi.Input[DistributionOrderedCacheBehaviorGrpcConfigArgs]]:
        
        ...
    
    @grpc_config.setter
    def grpc_config(self, value: Optional[pulumi.Input[DistributionOrderedCacheBehaviorGrpcConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionAssociations")
    def lambda_function_associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorLambdaFunctionAssociationArgs]]]]:
        
        ...
    
    @lambda_function_associations.setter
    def lambda_function_associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOrderedCacheBehaviorLambdaFunctionAssociationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_ttl.setter
    def max_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTtl")
    def min_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_ttl.setter
    def min_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originRequestPolicyId")
    def origin_request_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_request_policy_id.setter
    def origin_request_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="realtimeLogConfigArn")
    def realtime_log_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @realtime_log_config_arn.setter
    def realtime_log_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeadersPolicyId")
    def response_headers_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @response_headers_policy_id.setter
    def response_headers_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smoothStreaming")
    def smooth_streaming(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @smooth_streaming.setter
    def smooth_streaming(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedKeyGroups")
    def trusted_key_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @trusted_key_groups.setter
    def trusted_key_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedSigners")
    def trusted_signers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @trusted_signers.setter
    def trusted_signers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DistributionOrderedCacheBehaviorForwardedValuesArgsDict(TypedDict):
    cookies: pulumi.Input[DistributionOrderedCacheBehaviorForwardedValuesCookiesArgsDict]
    query_string: pulumi.Input[_builtins.bool]
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    query_string_cache_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DistributionOrderedCacheBehaviorForwardedValuesArgs:
    def __init__(__self__, *, cookies: pulumi.Input[DistributionOrderedCacheBehaviorForwardedValuesCookiesArgs], query_string: pulumi.Input[_builtins.bool], headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., query_string_cache_keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> pulumi.Input[DistributionOrderedCacheBehaviorForwardedValuesCookiesArgs]:
        
        ...
    
    @cookies.setter
    def cookies(self, value: pulumi.Input[DistributionOrderedCacheBehaviorForwardedValuesCookiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @query_string.setter
    def query_string(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringCacheKeys")
    def query_string_cache_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @query_string_cache_keys.setter
    def query_string_cache_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DistributionOrderedCacheBehaviorForwardedValuesCookiesArgsDict(TypedDict):
    forward: pulumi.Input[_builtins.str]
    whitelisted_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DistributionOrderedCacheBehaviorForwardedValuesCookiesArgs:
    def __init__(__self__, *, forward: pulumi.Input[_builtins.str], whitelisted_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def forward(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @forward.setter
    def forward(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="whitelistedNames")
    def whitelisted_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @whitelisted_names.setter
    def whitelisted_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DistributionOrderedCacheBehaviorFunctionAssociationArgsDict(TypedDict):
    event_type: pulumi.Input[_builtins.str]
    function_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class DistributionOrderedCacheBehaviorFunctionAssociationArgs:
    def __init__(__self__, *, event_type: pulumi.Input[_builtins.str], function_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @function_arn.setter
    def function_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DistributionOrderedCacheBehaviorGrpcConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DistributionOrderedCacheBehaviorGrpcConfigArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DistributionOrderedCacheBehaviorLambdaFunctionAssociationArgsDict(TypedDict):
    event_type: pulumi.Input[_builtins.str]
    lambda_arn: pulumi.Input[_builtins.str]
    include_body: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DistributionOrderedCacheBehaviorLambdaFunctionAssociationArgs:
    def __init__(__self__, *, event_type: pulumi.Input[_builtins.str], lambda_arn: pulumi.Input[_builtins.str], include_body: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @lambda_arn.setter
    def lambda_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeBody")
    def include_body(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_body.setter
    def include_body(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DistributionOriginArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    origin_id: pulumi.Input[_builtins.str]
    connection_attempts: NotRequired[pulumi.Input[_builtins.int]]
    connection_timeout: NotRequired[pulumi.Input[_builtins.int]]
    custom_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[DistributionOriginCustomHeaderArgsDict]]]]
    custom_origin_config: NotRequired[pulumi.Input[DistributionOriginCustomOriginConfigArgsDict]]
    origin_access_control_id: NotRequired[pulumi.Input[_builtins.str]]
    origin_path: NotRequired[pulumi.Input[_builtins.str]]
    origin_shield: NotRequired[pulumi.Input[DistributionOriginOriginShieldArgsDict]]
    response_completion_timeout: NotRequired[pulumi.Input[_builtins.int]]
    s3_origin_config: NotRequired[pulumi.Input[DistributionOriginS3OriginConfigArgsDict]]
    vpc_origin_config: NotRequired[pulumi.Input[DistributionOriginVpcOriginConfigArgsDict]]


@pulumi.input_type
class DistributionOriginArgs:
    def __init__(__self__, *, domain_name: pulumi.Input[_builtins.str], origin_id: pulumi.Input[_builtins.str], connection_attempts: Optional[pulumi.Input[_builtins.int]] = ..., connection_timeout: Optional[pulumi.Input[_builtins.int]] = ..., custom_headers: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOriginCustomHeaderArgs]]]] = ..., custom_origin_config: Optional[pulumi.Input[DistributionOriginCustomOriginConfigArgs]] = ..., origin_access_control_id: Optional[pulumi.Input[_builtins.str]] = ..., origin_path: Optional[pulumi.Input[_builtins.str]] = ..., origin_shield: Optional[pulumi.Input[DistributionOriginOriginShieldArgs]] = ..., response_completion_timeout: Optional[pulumi.Input[_builtins.int]] = ..., s3_origin_config: Optional[pulumi.Input[DistributionOriginS3OriginConfigArgs]] = ..., vpc_origin_config: Optional[pulumi.Input[DistributionOriginVpcOriginConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originId")
    def origin_id(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @origin_id.setter
    def origin_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionAttempts")
    def connection_attempts(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @connection_attempts.setter
    def connection_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTimeout")
    def connection_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @connection_timeout.setter
    def connection_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOriginCustomHeaderArgs]]]]:
        
        ...
    
    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionOriginCustomHeaderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customOriginConfig")
    def custom_origin_config(self) -> Optional[pulumi.Input[DistributionOriginCustomOriginConfigArgs]]:
        
        ...
    
    @custom_origin_config.setter
    def custom_origin_config(self, value: Optional[pulumi.Input[DistributionOriginCustomOriginConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originAccessControlId")
    def origin_access_control_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_access_control_id.setter
    def origin_access_control_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_path.setter
    def origin_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originShield")
    def origin_shield(self) -> Optional[pulumi.Input[DistributionOriginOriginShieldArgs]]:
        
        ...
    
    @origin_shield.setter
    def origin_shield(self, value: Optional[pulumi.Input[DistributionOriginOriginShieldArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCompletionTimeout")
    def response_completion_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @response_completion_timeout.setter
    def response_completion_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3OriginConfig")
    def s3_origin_config(self) -> Optional[pulumi.Input[DistributionOriginS3OriginConfigArgs]]:
        
        ...
    
    @s3_origin_config.setter
    def s3_origin_config(self, value: Optional[pulumi.Input[DistributionOriginS3OriginConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOriginConfig")
    def vpc_origin_config(self) -> Optional[pulumi.Input[DistributionOriginVpcOriginConfigArgs]]:
        
        ...
    
    @vpc_origin_config.setter
    def vpc_origin_config(self, value: Optional[pulumi.Input[DistributionOriginVpcOriginConfigArgs]]): # -> None:
        ...
    


class DistributionOriginCustomHeaderArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class DistributionOriginCustomHeaderArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
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
    def value(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DistributionOriginCustomOriginConfigArgsDict(TypedDict):
    http_port: pulumi.Input[_builtins.int]
    https_port: pulumi.Input[_builtins.int]
    origin_protocol_policy: pulumi.Input[_builtins.str]
    origin_ssl_protocols: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ip_address_type: NotRequired[pulumi.Input[_builtins.str]]
    origin_keepalive_timeout: NotRequired[pulumi.Input[_builtins.int]]
    origin_read_timeout: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DistributionOriginCustomOriginConfigArgs:
    def __init__(__self__, *, http_port: pulumi.Input[_builtins.int], https_port: pulumi.Input[_builtins.int], origin_protocol_policy: pulumi.Input[_builtins.str], origin_ssl_protocols: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., origin_keepalive_timeout: Optional[pulumi.Input[_builtins.int]] = ..., origin_read_timeout: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @http_port.setter
    def http_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @https_port.setter
    def https_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originProtocolPolicy")
    def origin_protocol_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @origin_protocol_policy.setter
    def origin_protocol_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originSslProtocols")
    def origin_ssl_protocols(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @origin_ssl_protocols.setter
    def origin_ssl_protocols(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originKeepaliveTimeout")
    def origin_keepalive_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @origin_keepalive_timeout.setter
    def origin_keepalive_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originReadTimeout")
    def origin_read_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @origin_read_timeout.setter
    def origin_read_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DistributionOriginGroupArgsDict(TypedDict):
    failover_criteria: pulumi.Input[DistributionOriginGroupFailoverCriteriaArgsDict]
    members: pulumi.Input[Sequence[pulumi.Input[DistributionOriginGroupMemberArgsDict]]]
    origin_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class DistributionOriginGroupArgs:
    def __init__(__self__, *, failover_criteria: pulumi.Input[DistributionOriginGroupFailoverCriteriaArgs], members: pulumi.Input[Sequence[pulumi.Input[DistributionOriginGroupMemberArgs]]], origin_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverCriteria")
    def failover_criteria(self) -> pulumi.Input[DistributionOriginGroupFailoverCriteriaArgs]:
        
        ...
    
    @failover_criteria.setter
    def failover_criteria(self, value: pulumi.Input[DistributionOriginGroupFailoverCriteriaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Input[Sequence[pulumi.Input[DistributionOriginGroupMemberArgs]]]:
        
        ...
    
    @members.setter
    def members(self, value: pulumi.Input[Sequence[pulumi.Input[DistributionOriginGroupMemberArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originId")
    def origin_id(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @origin_id.setter
    def origin_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DistributionOriginGroupFailoverCriteriaArgsDict(TypedDict):
    status_codes: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]


@pulumi.input_type
class DistributionOriginGroupFailoverCriteriaArgs:
    def __init__(__self__, *, status_codes: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCodes")
    def status_codes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]:
        
        ...
    
    @status_codes.setter
    def status_codes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): # -> None:
        ...
    


class DistributionOriginGroupMemberArgsDict(TypedDict):
    origin_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class DistributionOriginGroupMemberArgs:
    def __init__(__self__, *, origin_id: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originId")
    def origin_id(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @origin_id.setter
    def origin_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DistributionOriginOriginShieldArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    origin_shield_region: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionOriginOriginShieldArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], origin_shield_region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originShieldRegion")
    def origin_shield_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_shield_region.setter
    def origin_shield_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionOriginS3OriginConfigArgsDict(TypedDict):
    origin_access_identity: pulumi.Input[_builtins.str]


@pulumi.input_type
class DistributionOriginS3OriginConfigArgs:
    def __init__(__self__, *, origin_access_identity: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originAccessIdentity")
    def origin_access_identity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @origin_access_identity.setter
    def origin_access_identity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DistributionOriginVpcOriginConfigArgsDict(TypedDict):
    vpc_origin_id: pulumi.Input[_builtins.str]
    origin_keepalive_timeout: NotRequired[pulumi.Input[_builtins.int]]
    origin_read_timeout: NotRequired[pulumi.Input[_builtins.int]]
    owner_account_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionOriginVpcOriginConfigArgs:
    def __init__(__self__, *, vpc_origin_id: pulumi.Input[_builtins.str], origin_keepalive_timeout: Optional[pulumi.Input[_builtins.int]] = ..., origin_read_timeout: Optional[pulumi.Input[_builtins.int]] = ..., owner_account_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOriginId")
    def vpc_origin_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_origin_id.setter
    def vpc_origin_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originKeepaliveTimeout")
    def origin_keepalive_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @origin_keepalive_timeout.setter
    def origin_keepalive_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originReadTimeout")
    def origin_read_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @origin_read_timeout.setter
    def origin_read_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAccountId")
    def owner_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_account_id.setter
    def owner_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionRestrictionsArgsDict(TypedDict):
    geo_restriction: pulumi.Input[DistributionRestrictionsGeoRestrictionArgsDict]


@pulumi.input_type
class DistributionRestrictionsArgs:
    def __init__(__self__, *, geo_restriction: pulumi.Input[DistributionRestrictionsGeoRestrictionArgs]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoRestriction")
    def geo_restriction(self) -> pulumi.Input[DistributionRestrictionsGeoRestrictionArgs]:
        ...
    
    @geo_restriction.setter
    def geo_restriction(self, value: pulumi.Input[DistributionRestrictionsGeoRestrictionArgs]): # -> None:
        ...
    


class DistributionRestrictionsGeoRestrictionArgsDict(TypedDict):
    restriction_type: pulumi.Input[_builtins.str]
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DistributionRestrictionsGeoRestrictionArgs:
    def __init__(__self__, *, restriction_type: pulumi.Input[_builtins.str], locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictionType")
    def restriction_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @restriction_type.setter
    def restriction_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DistributionTenantCustomizationsArgsDict(TypedDict):
    certificate: NotRequired[pulumi.Input[DistributionTenantCustomizationsCertificateArgsDict]]
    geo_restriction: NotRequired[pulumi.Input[DistributionTenantCustomizationsGeoRestrictionArgsDict]]
    web_acl: NotRequired[pulumi.Input[DistributionTenantCustomizationsWebAclArgsDict]]


@pulumi.input_type
class DistributionTenantCustomizationsArgs:
    def __init__(__self__, *, certificate: Optional[pulumi.Input[DistributionTenantCustomizationsCertificateArgs]] = ..., geo_restriction: Optional[pulumi.Input[DistributionTenantCustomizationsGeoRestrictionArgs]] = ..., web_acl: Optional[pulumi.Input[DistributionTenantCustomizationsWebAclArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[DistributionTenantCustomizationsCertificateArgs]]:
        
        ...
    
    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[DistributionTenantCustomizationsCertificateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoRestriction")
    def geo_restriction(self) -> Optional[pulumi.Input[DistributionTenantCustomizationsGeoRestrictionArgs]]:
        
        ...
    
    @geo_restriction.setter
    def geo_restriction(self, value: Optional[pulumi.Input[DistributionTenantCustomizationsGeoRestrictionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAcl")
    def web_acl(self) -> Optional[pulumi.Input[DistributionTenantCustomizationsWebAclArgs]]:
        
        ...
    
    @web_acl.setter
    def web_acl(self, value: Optional[pulumi.Input[DistributionTenantCustomizationsWebAclArgs]]): # -> None:
        ...
    


class DistributionTenantCustomizationsCertificateArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionTenantCustomizationsCertificateArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionTenantCustomizationsGeoRestrictionArgsDict(TypedDict):
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    restriction_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionTenantCustomizationsGeoRestrictionArgs:
    def __init__(__self__, *, locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., restriction_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictionType")
    def restriction_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restriction_type.setter
    def restriction_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionTenantCustomizationsWebAclArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[_builtins.str]]
    arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionTenantCustomizationsWebAclArgs:
    def __init__(__self__, *, action: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionTenantDomainArgsDict(TypedDict):
    domain: pulumi.Input[_builtins.str]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionTenantDomainArgs:
    def __init__(__self__, *, domain: pulumi.Input[_builtins.str], status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionTenantManagedCertificateRequestArgsDict(TypedDict):
    certificate_transparency_logging_preference: NotRequired[pulumi.Input[_builtins.str]]
    primary_domain_name: NotRequired[pulumi.Input[_builtins.str]]
    validation_token_host: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionTenantManagedCertificateRequestArgs:
    def __init__(__self__, *, certificate_transparency_logging_preference: Optional[pulumi.Input[_builtins.str]] = ..., primary_domain_name: Optional[pulumi.Input[_builtins.str]] = ..., validation_token_host: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateTransparencyLoggingPreference")
    def certificate_transparency_logging_preference(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_transparency_logging_preference.setter
    def certificate_transparency_logging_preference(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryDomainName")
    def primary_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_domain_name.setter
    def primary_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationTokenHost")
    def validation_token_host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @validation_token_host.setter
    def validation_token_host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionTenantParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class DistributionTenantParameterArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
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
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DistributionTenantTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionTenantTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionTrustedKeyGroupArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedKeyGroupItemArgsDict]]]]


@pulumi.input_type
class DistributionTrustedKeyGroupArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., items: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedKeyGroupItemArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedKeyGroupItemArgs]]]]:
        
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedKeyGroupItemArgs]]]]): # -> None:
        ...
    


class DistributionTrustedKeyGroupItemArgsDict(TypedDict):
    key_group_id: NotRequired[pulumi.Input[_builtins.str]]
    key_pair_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DistributionTrustedKeyGroupItemArgs:
    def __init__(__self__, *, key_group_id: Optional[pulumi.Input[_builtins.str]] = ..., key_pair_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyGroupId")
    def key_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_group_id.setter
    def key_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPairIds")
    def key_pair_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @key_pair_ids.setter
    def key_pair_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DistributionTrustedSignerArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedSignerItemArgsDict]]]]


@pulumi.input_type
class DistributionTrustedSignerArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., items: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedSignerItemArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedSignerItemArgs]]]]:
        
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DistributionTrustedSignerItemArgs]]]]): # -> None:
        ...
    


class DistributionTrustedSignerItemArgsDict(TypedDict):
    aws_account_number: NotRequired[pulumi.Input[_builtins.str]]
    key_pair_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DistributionTrustedSignerItemArgs:
    def __init__(__self__, *, aws_account_number: Optional[pulumi.Input[_builtins.str]] = ..., key_pair_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountNumber")
    def aws_account_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_number.setter
    def aws_account_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPairIds")
    def key_pair_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @key_pair_ids.setter
    def key_pair_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DistributionViewerCertificateArgsDict(TypedDict):
    acm_certificate_arn: NotRequired[pulumi.Input[_builtins.str]]
    cloudfront_default_certificate: NotRequired[pulumi.Input[_builtins.bool]]
    iam_certificate_id: NotRequired[pulumi.Input[_builtins.str]]
    minimum_protocol_version: NotRequired[pulumi.Input[_builtins.str]]
    ssl_support_method: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionViewerCertificateArgs:
    def __init__(__self__, *, acm_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., cloudfront_default_certificate: Optional[pulumi.Input[_builtins.bool]] = ..., iam_certificate_id: Optional[pulumi.Input[_builtins.str]] = ..., minimum_protocol_version: Optional[pulumi.Input[_builtins.str]] = ..., ssl_support_method: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acmCertificateArn")
    def acm_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acm_certificate_arn.setter
    def acm_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudfrontDefaultCertificate")
    def cloudfront_default_certificate(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cloudfront_default_certificate.setter
    def cloudfront_default_certificate(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamCertificateId")
    def iam_certificate_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_certificate_id.setter
    def iam_certificate_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumProtocolVersion")
    def minimum_protocol_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @minimum_protocol_version.setter
    def minimum_protocol_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslSupportMethod")
    def ssl_support_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssl_support_method.setter
    def ssl_support_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionViewerMtlsConfigArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[_builtins.str]]
    trust_store_config: NotRequired[pulumi.Input[DistributionViewerMtlsConfigTrustStoreConfigArgsDict]]


@pulumi.input_type
class DistributionViewerMtlsConfigArgs:
    def __init__(__self__, *, mode: Optional[pulumi.Input[_builtins.str]] = ..., trust_store_config: Optional[pulumi.Input[DistributionViewerMtlsConfigTrustStoreConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustStoreConfig")
    def trust_store_config(self) -> Optional[pulumi.Input[DistributionViewerMtlsConfigTrustStoreConfigArgs]]:
        
        ...
    
    @trust_store_config.setter
    def trust_store_config(self, value: Optional[pulumi.Input[DistributionViewerMtlsConfigTrustStoreConfigArgs]]): # -> None:
        ...
    


class DistributionViewerMtlsConfigTrustStoreConfigArgsDict(TypedDict):
    trust_store_id: pulumi.Input[_builtins.str]
    advertise_trust_store_ca_names: NotRequired[pulumi.Input[_builtins.bool]]
    ignore_certificate_expiry: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DistributionViewerMtlsConfigTrustStoreConfigArgs:
    def __init__(__self__, *, trust_store_id: pulumi.Input[_builtins.str], advertise_trust_store_ca_names: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_certificate_expiry: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustStoreId")
    def trust_store_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @trust_store_id.setter
    def trust_store_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advertiseTrustStoreCaNames")
    def advertise_trust_store_ca_names(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @advertise_trust_store_ca_names.setter
    def advertise_trust_store_ca_names(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCertificateExpiry")
    def ignore_certificate_expiry(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_certificate_expiry.setter
    def ignore_certificate_expiry(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FieldLevelEncryptionConfigContentTypeProfileConfigArgsDict(TypedDict):
    content_type_profiles: pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesArgsDict]
    forward_when_content_type_is_unknown: pulumi.Input[_builtins.bool]


@pulumi.input_type
class FieldLevelEncryptionConfigContentTypeProfileConfigArgs:
    def __init__(__self__, *, content_type_profiles: pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesArgs], forward_when_content_type_is_unknown: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentTypeProfiles")
    def content_type_profiles(self) -> pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesArgs]:
        
        ...
    
    @content_type_profiles.setter
    def content_type_profiles(self, value: pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardWhenContentTypeIsUnknown")
    def forward_when_content_type_is_unknown(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @forward_when_content_type_is_unknown.setter
    def forward_when_content_type_is_unknown(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesArgsDict(TypedDict):
    items: pulumi.Input[Sequence[pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemArgsDict]]]


@pulumi.input_type
class FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesArgs:
    def __init__(__self__, *, items: pulumi.Input[Sequence[pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemArgs]]]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> pulumi.Input[Sequence[pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemArgs]]]:
        ...
    
    @items.setter
    def items(self, value: pulumi.Input[Sequence[pulumi.Input[FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemArgs]]]): # -> None:
        ...
    


class FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemArgsDict(TypedDict):
    content_type: pulumi.Input[_builtins.str]
    format: pulumi.Input[_builtins.str]
    profile_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemArgs:
    def __init__(__self__, *, content_type: pulumi.Input[_builtins.str], format: pulumi.Input[_builtins.str], profile_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @profile_id.setter
    def profile_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FieldLevelEncryptionConfigQueryArgProfileConfigArgsDict(TypedDict):
    forward_when_query_arg_profile_is_unknown: pulumi.Input[_builtins.bool]
    query_arg_profiles: NotRequired[pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesArgsDict]]


@pulumi.input_type
class FieldLevelEncryptionConfigQueryArgProfileConfigArgs:
    def __init__(__self__, *, forward_when_query_arg_profile_is_unknown: pulumi.Input[_builtins.bool], query_arg_profiles: Optional[pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardWhenQueryArgProfileIsUnknown")
    def forward_when_query_arg_profile_is_unknown(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @forward_when_query_arg_profile_is_unknown.setter
    def forward_when_query_arg_profile_is_unknown(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryArgProfiles")
    def query_arg_profiles(self) -> Optional[pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesArgs]]:
        
        ...
    
    @query_arg_profiles.setter
    def query_arg_profiles(self, value: Optional[pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesArgs]]): # -> None:
        ...
    


class FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemArgsDict]]]]


@pulumi.input_type
class FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemArgs]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemArgs]]]]): # -> None:
        ...
    


class FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemArgsDict(TypedDict):
    profile_id: pulumi.Input[_builtins.str]
    query_arg: pulumi.Input[_builtins.str]


@pulumi.input_type
class FieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemArgs:
    def __init__(__self__, *, profile_id: pulumi.Input[_builtins.str], query_arg: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @profile_id.setter
    def profile_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryArg")
    def query_arg(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @query_arg.setter
    def query_arg(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FieldLevelEncryptionProfileEncryptionEntitiesArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesItemArgsDict]]]]


@pulumi.input_type
class FieldLevelEncryptionProfileEncryptionEntitiesArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesItemArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesItemArgs]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesItemArgs]]]]): # -> None:
        ...
    


class FieldLevelEncryptionProfileEncryptionEntitiesItemArgsDict(TypedDict):
    field_patterns: pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesItemFieldPatternsArgsDict]
    provider_id: pulumi.Input[_builtins.str]
    public_key_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class FieldLevelEncryptionProfileEncryptionEntitiesItemArgs:
    def __init__(__self__, *, field_patterns: pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesItemFieldPatternsArgs], provider_id: pulumi.Input[_builtins.str], public_key_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldPatterns")
    def field_patterns(self) -> pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesItemFieldPatternsArgs]:
        
        ...
    
    @field_patterns.setter
    def field_patterns(self, value: pulumi.Input[FieldLevelEncryptionProfileEncryptionEntitiesItemFieldPatternsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @provider_id.setter
    def provider_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeyId")
    def public_key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @public_key_id.setter
    def public_key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FieldLevelEncryptionProfileEncryptionEntitiesItemFieldPatternsArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FieldLevelEncryptionProfileEncryptionEntitiesItemFieldPatternsArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class KeyValueStoreTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyValueStoreTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class KeyvaluestoreKeysExclusiveResourceKeyValuePairArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class KeyvaluestoreKeysExclusiveResourceKeyValuePairArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MonitoringSubscriptionMonitoringSubscriptionArgsDict(TypedDict):
    realtime_metrics_subscription_config: pulumi.Input[MonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfigArgsDict]


@pulumi.input_type
class MonitoringSubscriptionMonitoringSubscriptionArgs:
    def __init__(__self__, *, realtime_metrics_subscription_config: pulumi.Input[MonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfigArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="realtimeMetricsSubscriptionConfig")
    def realtime_metrics_subscription_config(self) -> pulumi.Input[MonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfigArgs]:
        
        ...
    
    @realtime_metrics_subscription_config.setter
    def realtime_metrics_subscription_config(self, value: pulumi.Input[MonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfigArgs]): # -> None:
        ...
    


class MonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfigArgsDict(TypedDict):
    realtime_metrics_subscription_status: pulumi.Input[_builtins.str]


@pulumi.input_type
class MonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfigArgs:
    def __init__(__self__, *, realtime_metrics_subscription_status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="realtimeMetricsSubscriptionStatus")
    def realtime_metrics_subscription_status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @realtime_metrics_subscription_status.setter
    def realtime_metrics_subscription_status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MultitenantDistributionActiveTrustedKeyGroupArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionActiveTrustedKeyGroupItemArgsDict]]]]


@pulumi.input_type
class MultitenantDistributionActiveTrustedKeyGroupArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., items: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionActiveTrustedKeyGroupItemArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionActiveTrustedKeyGroupItemArgs]]]]:
        
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionActiveTrustedKeyGroupItemArgs]]]]): # -> None:
        ...
    


class MultitenantDistributionActiveTrustedKeyGroupItemArgsDict(TypedDict):
    key_group_id: NotRequired[pulumi.Input[_builtins.str]]
    key_pair_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class MultitenantDistributionActiveTrustedKeyGroupItemArgs:
    def __init__(__self__, *, key_group_id: Optional[pulumi.Input[_builtins.str]] = ..., key_pair_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyGroupId")
    def key_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_group_id.setter
    def key_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPairIds")
    def key_pair_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @key_pair_ids.setter
    def key_pair_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MultitenantDistributionCacheBehaviorArgsDict(TypedDict):
    allowed_methods: pulumi.Input[MultitenantDistributionCacheBehaviorAllowedMethodsArgsDict]
    path_pattern: pulumi.Input[_builtins.str]
    target_origin_id: pulumi.Input[_builtins.str]
    viewer_protocol_policy: pulumi.Input[_builtins.str]
    cache_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    compress: NotRequired[pulumi.Input[_builtins.bool]]
    field_level_encryption_id: NotRequired[pulumi.Input[_builtins.str]]
    function_associations: NotRequired[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorFunctionAssociationArgsDict]]]]
    lambda_function_associations: NotRequired[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorLambdaFunctionAssociationArgsDict]]]]
    origin_request_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    realtime_log_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    response_headers_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    trusted_key_groups: NotRequired[pulumi.Input[MultitenantDistributionCacheBehaviorTrustedKeyGroupsArgsDict]]


@pulumi.input_type
class MultitenantDistributionCacheBehaviorArgs:
    def __init__(__self__, *, allowed_methods: pulumi.Input[MultitenantDistributionCacheBehaviorAllowedMethodsArgs], path_pattern: pulumi.Input[_builtins.str], target_origin_id: pulumi.Input[_builtins.str], viewer_protocol_policy: pulumi.Input[_builtins.str], cache_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., compress: Optional[pulumi.Input[_builtins.bool]] = ..., field_level_encryption_id: Optional[pulumi.Input[_builtins.str]] = ..., function_associations: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorFunctionAssociationArgs]]]] = ..., lambda_function_associations: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorLambdaFunctionAssociationArgs]]]] = ..., origin_request_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., realtime_log_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., response_headers_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., trusted_key_groups: Optional[pulumi.Input[MultitenantDistributionCacheBehaviorTrustedKeyGroupsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> pulumi.Input[MultitenantDistributionCacheBehaviorAllowedMethodsArgs]:
        
        ...
    
    @allowed_methods.setter
    def allowed_methods(self, value: pulumi.Input[MultitenantDistributionCacheBehaviorAllowedMethodsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathPattern")
    def path_pattern(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path_pattern.setter
    def path_pattern(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetOriginId")
    def target_origin_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_origin_id.setter
    def target_origin_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewerProtocolPolicy")
    def viewer_protocol_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @viewer_protocol_policy.setter
    def viewer_protocol_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachePolicyId")
    def cache_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_policy_id.setter
    def cache_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def compress(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @compress.setter
    def compress(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldLevelEncryptionId")
    def field_level_encryption_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @field_level_encryption_id.setter
    def field_level_encryption_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAssociations")
    def function_associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorFunctionAssociationArgs]]]]:
        
        ...
    
    @function_associations.setter
    def function_associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorFunctionAssociationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionAssociations")
    def lambda_function_associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorLambdaFunctionAssociationArgs]]]]:
        
        ...
    
    @lambda_function_associations.setter
    def lambda_function_associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionCacheBehaviorLambdaFunctionAssociationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originRequestPolicyId")
    def origin_request_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_request_policy_id.setter
    def origin_request_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="realtimeLogConfigArn")
    def realtime_log_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @realtime_log_config_arn.setter
    def realtime_log_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeadersPolicyId")
    def response_headers_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @response_headers_policy_id.setter
    def response_headers_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedKeyGroups")
    def trusted_key_groups(self) -> Optional[pulumi.Input[MultitenantDistributionCacheBehaviorTrustedKeyGroupsArgs]]:
        
        ...
    
    @trusted_key_groups.setter
    def trusted_key_groups(self, value: Optional[pulumi.Input[MultitenantDistributionCacheBehaviorTrustedKeyGroupsArgs]]): # -> None:
        ...
    


class MultitenantDistributionCacheBehaviorAllowedMethodsArgsDict(TypedDict):
    cached_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    items: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class MultitenantDistributionCacheBehaviorAllowedMethodsArgs:
    def __init__(__self__, *, cached_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], items: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachedMethods")
    def cached_methods(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @cached_methods.setter
    def cached_methods(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        ...
    
    @items.setter
    def items(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class MultitenantDistributionCacheBehaviorFunctionAssociationArgsDict(TypedDict):
    event_type: pulumi.Input[_builtins.str]
    function_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class MultitenantDistributionCacheBehaviorFunctionAssociationArgs:
    def __init__(__self__, *, event_type: pulumi.Input[_builtins.str], function_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @function_arn.setter
    def function_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MultitenantDistributionCacheBehaviorLambdaFunctionAssociationArgsDict(TypedDict):
    event_type: pulumi.Input[_builtins.str]
    lambda_function_arn: pulumi.Input[_builtins.str]
    include_body: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class MultitenantDistributionCacheBehaviorLambdaFunctionAssociationArgs:
    def __init__(__self__, *, event_type: pulumi.Input[_builtins.str], lambda_function_arn: pulumi.Input[_builtins.str], include_body: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @lambda_function_arn.setter
    def lambda_function_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeBody")
    def include_body(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_body.setter
    def include_body(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class MultitenantDistributionCacheBehaviorTrustedKeyGroupsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class MultitenantDistributionCacheBehaviorTrustedKeyGroupsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MultitenantDistributionCustomErrorResponseArgsDict(TypedDict):
    error_code: pulumi.Input[_builtins.int]
    error_caching_min_ttl: NotRequired[pulumi.Input[_builtins.int]]
    response_code: NotRequired[pulumi.Input[_builtins.str]]
    response_page_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MultitenantDistributionCustomErrorResponseArgs:
    def __init__(__self__, *, error_code: pulumi.Input[_builtins.int], error_caching_min_ttl: Optional[pulumi.Input[_builtins.int]] = ..., response_code: Optional[pulumi.Input[_builtins.str]] = ..., response_page_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @error_code.setter
    def error_code(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCachingMinTtl")
    def error_caching_min_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @error_caching_min_ttl.setter
    def error_caching_min_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @response_code.setter
    def response_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responsePagePath")
    def response_page_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @response_page_path.setter
    def response_page_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MultitenantDistributionDefaultCacheBehaviorArgsDict(TypedDict):
    allowed_methods: pulumi.Input[MultitenantDistributionDefaultCacheBehaviorAllowedMethodsArgsDict]
    target_origin_id: pulumi.Input[_builtins.str]
    viewer_protocol_policy: pulumi.Input[_builtins.str]
    cache_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    compress: NotRequired[pulumi.Input[_builtins.bool]]
    field_level_encryption_id: NotRequired[pulumi.Input[_builtins.str]]
    function_associations: NotRequired[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorFunctionAssociationArgsDict]]]]
    lambda_function_associations: NotRequired[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorLambdaFunctionAssociationArgsDict]]]]
    origin_request_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    realtime_log_config_arn: NotRequired[pulumi.Input[_builtins.str]]
    response_headers_policy_id: NotRequired[pulumi.Input[_builtins.str]]
    trusted_key_groups: NotRequired[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorTrustedKeyGroupsArgsDict]]


@pulumi.input_type
class MultitenantDistributionDefaultCacheBehaviorArgs:
    def __init__(__self__, *, allowed_methods: pulumi.Input[MultitenantDistributionDefaultCacheBehaviorAllowedMethodsArgs], target_origin_id: pulumi.Input[_builtins.str], viewer_protocol_policy: pulumi.Input[_builtins.str], cache_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., compress: Optional[pulumi.Input[_builtins.bool]] = ..., field_level_encryption_id: Optional[pulumi.Input[_builtins.str]] = ..., function_associations: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorFunctionAssociationArgs]]]] = ..., lambda_function_associations: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorLambdaFunctionAssociationArgs]]]] = ..., origin_request_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., realtime_log_config_arn: Optional[pulumi.Input[_builtins.str]] = ..., response_headers_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., trusted_key_groups: Optional[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorTrustedKeyGroupsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> pulumi.Input[MultitenantDistributionDefaultCacheBehaviorAllowedMethodsArgs]:
        
        ...
    
    @allowed_methods.setter
    def allowed_methods(self, value: pulumi.Input[MultitenantDistributionDefaultCacheBehaviorAllowedMethodsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetOriginId")
    def target_origin_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_origin_id.setter
    def target_origin_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewerProtocolPolicy")
    def viewer_protocol_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @viewer_protocol_policy.setter
    def viewer_protocol_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachePolicyId")
    def cache_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_policy_id.setter
    def cache_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def compress(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @compress.setter
    def compress(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldLevelEncryptionId")
    def field_level_encryption_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @field_level_encryption_id.setter
    def field_level_encryption_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAssociations")
    def function_associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorFunctionAssociationArgs]]]]:
        
        ...
    
    @function_associations.setter
    def function_associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorFunctionAssociationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionAssociations")
    def lambda_function_associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorLambdaFunctionAssociationArgs]]]]:
        
        ...
    
    @lambda_function_associations.setter
    def lambda_function_associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorLambdaFunctionAssociationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originRequestPolicyId")
    def origin_request_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_request_policy_id.setter
    def origin_request_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="realtimeLogConfigArn")
    def realtime_log_config_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @realtime_log_config_arn.setter
    def realtime_log_config_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeadersPolicyId")
    def response_headers_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @response_headers_policy_id.setter
    def response_headers_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedKeyGroups")
    def trusted_key_groups(self) -> Optional[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorTrustedKeyGroupsArgs]]:
        
        ...
    
    @trusted_key_groups.setter
    def trusted_key_groups(self, value: Optional[pulumi.Input[MultitenantDistributionDefaultCacheBehaviorTrustedKeyGroupsArgs]]): # -> None:
        ...
    


class MultitenantDistributionDefaultCacheBehaviorAllowedMethodsArgsDict(TypedDict):
    cached_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    items: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class MultitenantDistributionDefaultCacheBehaviorAllowedMethodsArgs:
    def __init__(__self__, *, cached_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], items: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachedMethods")
    def cached_methods(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @cached_methods.setter
    def cached_methods(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        ...
    
    @items.setter
    def items(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class MultitenantDistributionDefaultCacheBehaviorFunctionAssociationArgsDict(TypedDict):
    event_type: pulumi.Input[_builtins.str]
    function_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class MultitenantDistributionDefaultCacheBehaviorFunctionAssociationArgs:
    def __init__(__self__, *, event_type: pulumi.Input[_builtins.str], function_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @function_arn.setter
    def function_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MultitenantDistributionDefaultCacheBehaviorLambdaFunctionAssociationArgsDict(TypedDict):
    event_type: pulumi.Input[_builtins.str]
    lambda_function_arn: pulumi.Input[_builtins.str]
    include_body: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class MultitenantDistributionDefaultCacheBehaviorLambdaFunctionAssociationArgs:
    def __init__(__self__, *, event_type: pulumi.Input[_builtins.str], lambda_function_arn: pulumi.Input[_builtins.str], include_body: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @lambda_function_arn.setter
    def lambda_function_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeBody")
    def include_body(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_body.setter
    def include_body(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class MultitenantDistributionDefaultCacheBehaviorTrustedKeyGroupsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class MultitenantDistributionDefaultCacheBehaviorTrustedKeyGroupsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MultitenantDistributionOriginArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    connection_attempts: NotRequired[pulumi.Input[_builtins.int]]
    connection_timeout: NotRequired[pulumi.Input[_builtins.int]]
    custom_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginCustomHeaderArgsDict]]]]
    custom_origin_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginCustomOriginConfigArgsDict]]]]
    origin_access_control_id: NotRequired[pulumi.Input[_builtins.str]]
    origin_path: NotRequired[pulumi.Input[_builtins.str]]
    origin_shields: NotRequired[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginOriginShieldArgsDict]]]]
    response_completion_timeout: NotRequired[pulumi.Input[_builtins.int]]
    vpc_origin_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginVpcOriginConfigArgsDict]]]]


@pulumi.input_type
class MultitenantDistributionOriginArgs:
    def __init__(__self__, *, domain_name: pulumi.Input[_builtins.str], id: pulumi.Input[_builtins.str], connection_attempts: Optional[pulumi.Input[_builtins.int]] = ..., connection_timeout: Optional[pulumi.Input[_builtins.int]] = ..., custom_headers: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginCustomHeaderArgs]]]] = ..., custom_origin_configs: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginCustomOriginConfigArgs]]]] = ..., origin_access_control_id: Optional[pulumi.Input[_builtins.str]] = ..., origin_path: Optional[pulumi.Input[_builtins.str]] = ..., origin_shields: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginOriginShieldArgs]]]] = ..., response_completion_timeout: Optional[pulumi.Input[_builtins.int]] = ..., vpc_origin_configs: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginVpcOriginConfigArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionAttempts")
    def connection_attempts(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @connection_attempts.setter
    def connection_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTimeout")
    def connection_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @connection_timeout.setter
    def connection_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginCustomHeaderArgs]]]]:
        
        ...
    
    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginCustomHeaderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customOriginConfigs")
    def custom_origin_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginCustomOriginConfigArgs]]]]:
        
        ...
    
    @custom_origin_configs.setter
    def custom_origin_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginCustomOriginConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originAccessControlId")
    def origin_access_control_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_access_control_id.setter
    def origin_access_control_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_path.setter
    def origin_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originShields")
    def origin_shields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginOriginShieldArgs]]]]:
        
        ...
    
    @origin_shields.setter
    def origin_shields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginOriginShieldArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCompletionTimeout")
    def response_completion_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @response_completion_timeout.setter
    def response_completion_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOriginConfigs")
    def vpc_origin_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginVpcOriginConfigArgs]]]]:
        
        ...
    
    @vpc_origin_configs.setter
    def vpc_origin_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginVpcOriginConfigArgs]]]]): # -> None:
        ...
    


class MultitenantDistributionOriginCustomHeaderArgsDict(TypedDict):
    header_name: pulumi.Input[_builtins.str]
    header_value: pulumi.Input[_builtins.str]


@pulumi.input_type
class MultitenantDistributionOriginCustomHeaderArgs:
    def __init__(__self__, *, header_name: pulumi.Input[_builtins.str], header_value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @header_name.setter
    def header_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @header_value.setter
    def header_value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MultitenantDistributionOriginCustomOriginConfigArgsDict(TypedDict):
    http_port: pulumi.Input[_builtins.int]
    https_port: pulumi.Input[_builtins.int]
    origin_protocol_policy: pulumi.Input[_builtins.str]
    origin_ssl_protocols: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ip_address_type: NotRequired[pulumi.Input[_builtins.str]]
    origin_keepalive_timeout: NotRequired[pulumi.Input[_builtins.int]]
    origin_read_timeout: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class MultitenantDistributionOriginCustomOriginConfigArgs:
    def __init__(__self__, *, http_port: pulumi.Input[_builtins.int], https_port: pulumi.Input[_builtins.int], origin_protocol_policy: pulumi.Input[_builtins.str], origin_ssl_protocols: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., origin_keepalive_timeout: Optional[pulumi.Input[_builtins.int]] = ..., origin_read_timeout: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @http_port.setter
    def http_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @https_port.setter
    def https_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originProtocolPolicy")
    def origin_protocol_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @origin_protocol_policy.setter
    def origin_protocol_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originSslProtocols")
    def origin_ssl_protocols(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @origin_ssl_protocols.setter
    def origin_ssl_protocols(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originKeepaliveTimeout")
    def origin_keepalive_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @origin_keepalive_timeout.setter
    def origin_keepalive_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originReadTimeout")
    def origin_read_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @origin_read_timeout.setter
    def origin_read_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class MultitenantDistributionOriginGroupArgsDict(TypedDict):
    failover_criteria: pulumi.Input[MultitenantDistributionOriginGroupFailoverCriteriaArgsDict]
    id: pulumi.Input[_builtins.str]
    members: pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginGroupMemberArgsDict]]]


@pulumi.input_type
class MultitenantDistributionOriginGroupArgs:
    def __init__(__self__, *, failover_criteria: pulumi.Input[MultitenantDistributionOriginGroupFailoverCriteriaArgs], id: pulumi.Input[_builtins.str], members: pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginGroupMemberArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverCriteria")
    def failover_criteria(self) -> pulumi.Input[MultitenantDistributionOriginGroupFailoverCriteriaArgs]:
        
        ...
    
    @failover_criteria.setter
    def failover_criteria(self, value: pulumi.Input[MultitenantDistributionOriginGroupFailoverCriteriaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginGroupMemberArgs]]]:
        
        ...
    
    @members.setter
    def members(self, value: pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionOriginGroupMemberArgs]]]): # -> None:
        ...
    


class MultitenantDistributionOriginGroupFailoverCriteriaArgsDict(TypedDict):
    status_codes: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]


@pulumi.input_type
class MultitenantDistributionOriginGroupFailoverCriteriaArgs:
    def __init__(__self__, *, status_codes: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCodes")
    def status_codes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]:
        
        ...
    
    @status_codes.setter
    def status_codes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): # -> None:
        ...
    


class MultitenantDistributionOriginGroupMemberArgsDict(TypedDict):
    origin_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class MultitenantDistributionOriginGroupMemberArgs:
    def __init__(__self__, *, origin_id: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originId")
    def origin_id(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @origin_id.setter
    def origin_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MultitenantDistributionOriginOriginShieldArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    origin_shield_region: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MultitenantDistributionOriginOriginShieldArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], origin_shield_region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originShieldRegion")
    def origin_shield_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @origin_shield_region.setter
    def origin_shield_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MultitenantDistributionOriginVpcOriginConfigArgsDict(TypedDict):
    vpc_origin_id: pulumi.Input[_builtins.str]
    origin_keepalive_timeout: NotRequired[pulumi.Input[_builtins.int]]
    origin_read_timeout: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class MultitenantDistributionOriginVpcOriginConfigArgs:
    def __init__(__self__, *, vpc_origin_id: pulumi.Input[_builtins.str], origin_keepalive_timeout: Optional[pulumi.Input[_builtins.int]] = ..., origin_read_timeout: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcOriginId")
    def vpc_origin_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_origin_id.setter
    def vpc_origin_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originKeepaliveTimeout")
    def origin_keepalive_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @origin_keepalive_timeout.setter
    def origin_keepalive_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originReadTimeout")
    def origin_read_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @origin_read_timeout.setter
    def origin_read_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class MultitenantDistributionRestrictionsArgsDict(TypedDict):
    geo_restriction: pulumi.Input[MultitenantDistributionRestrictionsGeoRestrictionArgsDict]


@pulumi.input_type
class MultitenantDistributionRestrictionsArgs:
    def __init__(__self__, *, geo_restriction: pulumi.Input[MultitenantDistributionRestrictionsGeoRestrictionArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoRestriction")
    def geo_restriction(self) -> pulumi.Input[MultitenantDistributionRestrictionsGeoRestrictionArgs]:
        
        ...
    
    @geo_restriction.setter
    def geo_restriction(self, value: pulumi.Input[MultitenantDistributionRestrictionsGeoRestrictionArgs]): # -> None:
        ...
    


class MultitenantDistributionRestrictionsGeoRestrictionArgsDict(TypedDict):
    restriction_type: pulumi.Input[_builtins.str]
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class MultitenantDistributionRestrictionsGeoRestrictionArgs:
    def __init__(__self__, *, restriction_type: pulumi.Input[_builtins.str], items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictionType")
    def restriction_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @restriction_type.setter
    def restriction_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MultitenantDistributionTenantConfigArgsDict(TypedDict):
    parameter_definitions: NotRequired[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionTenantConfigParameterDefinitionArgsDict]]]]


@pulumi.input_type
class MultitenantDistributionTenantConfigArgs:
    def __init__(__self__, *, parameter_definitions: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionTenantConfigParameterDefinitionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterDefinitions")
    def parameter_definitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionTenantConfigParameterDefinitionArgs]]]]:
        
        ...
    
    @parameter_definitions.setter
    def parameter_definitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionTenantConfigParameterDefinitionArgs]]]]): # -> None:
        ...
    


class MultitenantDistributionTenantConfigParameterDefinitionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    definitions: NotRequired[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionTenantConfigParameterDefinitionDefinitionArgsDict]]]]


@pulumi.input_type
class MultitenantDistributionTenantConfigParameterDefinitionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], definitions: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionTenantConfigParameterDefinitionDefinitionArgs]]]] = ...) -> None:
        
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
    def definitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionTenantConfigParameterDefinitionDefinitionArgs]]]]:
        
        ...
    
    @definitions.setter
    def definitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionTenantConfigParameterDefinitionDefinitionArgs]]]]): # -> None:
        ...
    


class MultitenantDistributionTenantConfigParameterDefinitionDefinitionArgsDict(TypedDict):
    string_schemas: NotRequired[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionTenantConfigParameterDefinitionDefinitionStringSchemaArgsDict]]]]


@pulumi.input_type
class MultitenantDistributionTenantConfigParameterDefinitionDefinitionArgs:
    def __init__(__self__, *, string_schemas: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionTenantConfigParameterDefinitionDefinitionStringSchemaArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringSchemas")
    def string_schemas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionTenantConfigParameterDefinitionDefinitionStringSchemaArgs]]]]:
        
        ...
    
    @string_schemas.setter
    def string_schemas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MultitenantDistributionTenantConfigParameterDefinitionDefinitionStringSchemaArgs]]]]): # -> None:
        ...
    


class MultitenantDistributionTenantConfigParameterDefinitionDefinitionStringSchemaArgsDict(TypedDict):
    required: pulumi.Input[_builtins.bool]
    comment: NotRequired[pulumi.Input[_builtins.str]]
    default_value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MultitenantDistributionTenantConfigParameterDefinitionDefinitionStringSchemaArgs:
    def __init__(__self__, *, required: pulumi.Input[_builtins.bool], comment: Optional[pulumi.Input[_builtins.str]] = ..., default_value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @required.setter
    def required(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MultitenantDistributionTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MultitenantDistributionTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MultitenantDistributionViewerCertificateArgsDict(TypedDict):
    acm_certificate_arn: NotRequired[pulumi.Input[_builtins.str]]
    cloudfront_default_certificate: NotRequired[pulumi.Input[_builtins.bool]]
    minimum_protocol_version: NotRequired[pulumi.Input[_builtins.str]]
    ssl_support_method: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MultitenantDistributionViewerCertificateArgs:
    def __init__(__self__, *, acm_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., cloudfront_default_certificate: Optional[pulumi.Input[_builtins.bool]] = ..., minimum_protocol_version: Optional[pulumi.Input[_builtins.str]] = ..., ssl_support_method: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acmCertificateArn")
    def acm_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acm_certificate_arn.setter
    def acm_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudfrontDefaultCertificate")
    def cloudfront_default_certificate(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @cloudfront_default_certificate.setter
    def cloudfront_default_certificate(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumProtocolVersion")
    def minimum_protocol_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @minimum_protocol_version.setter
    def minimum_protocol_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslSupportMethod")
    def ssl_support_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssl_support_method.setter
    def ssl_support_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OriginRequestPolicyCookiesConfigArgsDict(TypedDict):
    cookie_behavior: pulumi.Input[_builtins.str]
    cookies: NotRequired[pulumi.Input[OriginRequestPolicyCookiesConfigCookiesArgsDict]]


@pulumi.input_type
class OriginRequestPolicyCookiesConfigArgs:
    def __init__(__self__, *, cookie_behavior: pulumi.Input[_builtins.str], cookies: Optional[pulumi.Input[OriginRequestPolicyCookiesConfigCookiesArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookieBehavior")
    def cookie_behavior(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @cookie_behavior.setter
    def cookie_behavior(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[pulumi.Input[OriginRequestPolicyCookiesConfigCookiesArgs]]:
        ...
    
    @cookies.setter
    def cookies(self, value: Optional[pulumi.Input[OriginRequestPolicyCookiesConfigCookiesArgs]]): # -> None:
        ...
    


class OriginRequestPolicyCookiesConfigCookiesArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class OriginRequestPolicyCookiesConfigCookiesArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class OriginRequestPolicyHeadersConfigArgsDict(TypedDict):
    header_behavior: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[pulumi.Input[OriginRequestPolicyHeadersConfigHeadersArgsDict]]


@pulumi.input_type
class OriginRequestPolicyHeadersConfigArgs:
    def __init__(__self__, *, header_behavior: Optional[pulumi.Input[_builtins.str]] = ..., headers: Optional[pulumi.Input[OriginRequestPolicyHeadersConfigHeadersArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerBehavior")
    def header_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @header_behavior.setter
    def header_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[OriginRequestPolicyHeadersConfigHeadersArgs]]:
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[OriginRequestPolicyHeadersConfigHeadersArgs]]): # -> None:
        ...
    


class OriginRequestPolicyHeadersConfigHeadersArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class OriginRequestPolicyHeadersConfigHeadersArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class OriginRequestPolicyQueryStringsConfigArgsDict(TypedDict):
    query_string_behavior: pulumi.Input[_builtins.str]
    query_strings: NotRequired[pulumi.Input[OriginRequestPolicyQueryStringsConfigQueryStringsArgsDict]]


@pulumi.input_type
class OriginRequestPolicyQueryStringsConfigArgs:
    def __init__(__self__, *, query_string_behavior: pulumi.Input[_builtins.str], query_strings: Optional[pulumi.Input[OriginRequestPolicyQueryStringsConfigQueryStringsArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringBehavior")
    def query_string_behavior(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @query_string_behavior.setter
    def query_string_behavior(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStrings")
    def query_strings(self) -> Optional[pulumi.Input[OriginRequestPolicyQueryStringsConfigQueryStringsArgs]]:
        ...
    
    @query_strings.setter
    def query_strings(self, value: Optional[pulumi.Input[OriginRequestPolicyQueryStringsConfigQueryStringsArgs]]): # -> None:
        ...
    


class OriginRequestPolicyQueryStringsConfigQueryStringsArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class OriginRequestPolicyQueryStringsConfigQueryStringsArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RealtimeLogConfigEndpointArgsDict(TypedDict):
    kinesis_stream_config: pulumi.Input[RealtimeLogConfigEndpointKinesisStreamConfigArgsDict]
    stream_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class RealtimeLogConfigEndpointArgs:
    def __init__(__self__, *, kinesis_stream_config: pulumi.Input[RealtimeLogConfigEndpointKinesisStreamConfigArgs], stream_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisStreamConfig")
    def kinesis_stream_config(self) -> pulumi.Input[RealtimeLogConfigEndpointKinesisStreamConfigArgs]:
        
        ...
    
    @kinesis_stream_config.setter
    def kinesis_stream_config(self, value: pulumi.Input[RealtimeLogConfigEndpointKinesisStreamConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamType")
    def stream_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @stream_type.setter
    def stream_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RealtimeLogConfigEndpointKinesisStreamConfigArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    stream_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class RealtimeLogConfigEndpointKinesisStreamConfigArgs:
    def __init__(__self__, *, role_arn: pulumi.Input[_builtins.str], stream_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @stream_arn.setter
    def stream_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ResponseHeadersPolicyCorsConfigArgsDict(TypedDict):
    access_control_allow_credentials: pulumi.Input[_builtins.bool]
    access_control_allow_headers: pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlAllowHeadersArgsDict]
    access_control_allow_methods: pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlAllowMethodsArgsDict]
    access_control_allow_origins: pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlAllowOriginsArgsDict]
    origin_override: pulumi.Input[_builtins.bool]
    access_control_expose_headers: NotRequired[pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlExposeHeadersArgsDict]]
    access_control_max_age_sec: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ResponseHeadersPolicyCorsConfigArgs:
    def __init__(__self__, *, access_control_allow_credentials: pulumi.Input[_builtins.bool], access_control_allow_headers: pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlAllowHeadersArgs], access_control_allow_methods: pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlAllowMethodsArgs], access_control_allow_origins: pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlAllowOriginsArgs], origin_override: pulumi.Input[_builtins.bool], access_control_expose_headers: Optional[pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlExposeHeadersArgs]] = ..., access_control_max_age_sec: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlAllowCredentials")
    def access_control_allow_credentials(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @access_control_allow_credentials.setter
    def access_control_allow_credentials(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlAllowHeaders")
    def access_control_allow_headers(self) -> pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlAllowHeadersArgs]:
        
        ...
    
    @access_control_allow_headers.setter
    def access_control_allow_headers(self, value: pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlAllowHeadersArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlAllowMethods")
    def access_control_allow_methods(self) -> pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlAllowMethodsArgs]:
        
        ...
    
    @access_control_allow_methods.setter
    def access_control_allow_methods(self, value: pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlAllowMethodsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlAllowOrigins")
    def access_control_allow_origins(self) -> pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlAllowOriginsArgs]:
        
        ...
    
    @access_control_allow_origins.setter
    def access_control_allow_origins(self, value: pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlAllowOriginsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originOverride")
    def origin_override(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @origin_override.setter
    def origin_override(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlExposeHeaders")
    def access_control_expose_headers(self) -> Optional[pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlExposeHeadersArgs]]:
        
        ...
    
    @access_control_expose_headers.setter
    def access_control_expose_headers(self, value: Optional[pulumi.Input[ResponseHeadersPolicyCorsConfigAccessControlExposeHeadersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlMaxAgeSec")
    def access_control_max_age_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @access_control_max_age_sec.setter
    def access_control_max_age_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ResponseHeadersPolicyCorsConfigAccessControlAllowHeadersArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ResponseHeadersPolicyCorsConfigAccessControlAllowHeadersArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ResponseHeadersPolicyCorsConfigAccessControlAllowMethodsArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ResponseHeadersPolicyCorsConfigAccessControlAllowMethodsArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ResponseHeadersPolicyCorsConfigAccessControlAllowOriginsArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ResponseHeadersPolicyCorsConfigAccessControlAllowOriginsArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ResponseHeadersPolicyCorsConfigAccessControlExposeHeadersArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ResponseHeadersPolicyCorsConfigAccessControlExposeHeadersArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ResponseHeadersPolicyCustomHeadersConfigArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[ResponseHeadersPolicyCustomHeadersConfigItemArgsDict]]]]


@pulumi.input_type
class ResponseHeadersPolicyCustomHeadersConfigArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[ResponseHeadersPolicyCustomHeadersConfigItemArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResponseHeadersPolicyCustomHeadersConfigItemArgs]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResponseHeadersPolicyCustomHeadersConfigItemArgs]]]]): # -> None:
        ...
    


class ResponseHeadersPolicyCustomHeadersConfigItemArgsDict(TypedDict):
    header: pulumi.Input[_builtins.str]
    override: pulumi.Input[_builtins.bool]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class ResponseHeadersPolicyCustomHeadersConfigItemArgs:
    def __init__(__self__, *, header: pulumi.Input[_builtins.str], override: pulumi.Input[_builtins.bool], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @header.setter
    def header(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def override(self) -> pulumi.Input[_builtins.bool]:
        ...
    
    @override.setter
    def override(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ResponseHeadersPolicyRemoveHeadersConfigArgsDict(TypedDict):
    items: NotRequired[pulumi.Input[Sequence[pulumi.Input[ResponseHeadersPolicyRemoveHeadersConfigItemArgsDict]]]]


@pulumi.input_type
class ResponseHeadersPolicyRemoveHeadersConfigArgs:
    def __init__(__self__, *, items: Optional[pulumi.Input[Sequence[pulumi.Input[ResponseHeadersPolicyRemoveHeadersConfigItemArgs]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResponseHeadersPolicyRemoveHeadersConfigItemArgs]]]]:
        ...
    
    @items.setter
    def items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResponseHeadersPolicyRemoveHeadersConfigItemArgs]]]]): # -> None:
        ...
    


class ResponseHeadersPolicyRemoveHeadersConfigItemArgsDict(TypedDict):
    header: pulumi.Input[_builtins.str]


@pulumi.input_type
class ResponseHeadersPolicyRemoveHeadersConfigItemArgs:
    def __init__(__self__, *, header: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @header.setter
    def header(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ResponseHeadersPolicySecurityHeadersConfigArgsDict(TypedDict):
    content_security_policy: NotRequired[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyArgsDict]]
    content_type_options: NotRequired[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigContentTypeOptionsArgsDict]]
    frame_options: NotRequired[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigFrameOptionsArgsDict]]
    referrer_policy: NotRequired[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigReferrerPolicyArgsDict]]
    strict_transport_security: NotRequired[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityArgsDict]]
    xss_protection: NotRequired[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigXssProtectionArgsDict]]


@pulumi.input_type
class ResponseHeadersPolicySecurityHeadersConfigArgs:
    def __init__(__self__, *, content_security_policy: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyArgs]] = ..., content_type_options: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigContentTypeOptionsArgs]] = ..., frame_options: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigFrameOptionsArgs]] = ..., referrer_policy: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigReferrerPolicyArgs]] = ..., strict_transport_security: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityArgs]] = ..., xss_protection: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigXssProtectionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentSecurityPolicy")
    def content_security_policy(self) -> Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyArgs]]:
        
        ...
    
    @content_security_policy.setter
    def content_security_policy(self, value: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentTypeOptions")
    def content_type_options(self) -> Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigContentTypeOptionsArgs]]:
        
        ...
    
    @content_type_options.setter
    def content_type_options(self, value: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigContentTypeOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="frameOptions")
    def frame_options(self) -> Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigFrameOptionsArgs]]:
        
        ...
    
    @frame_options.setter
    def frame_options(self, value: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigFrameOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="referrerPolicy")
    def referrer_policy(self) -> Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigReferrerPolicyArgs]]:
        
        ...
    
    @referrer_policy.setter
    def referrer_policy(self, value: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigReferrerPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="strictTransportSecurity")
    def strict_transport_security(self) -> Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityArgs]]:
        
        ...
    
    @strict_transport_security.setter
    def strict_transport_security(self, value: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xssProtection")
    def xss_protection(self) -> Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigXssProtectionArgs]]:
        
        ...
    
    @xss_protection.setter
    def xss_protection(self, value: Optional[pulumi.Input[ResponseHeadersPolicySecurityHeadersConfigXssProtectionArgs]]): # -> None:
        ...
    


class ResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyArgsDict(TypedDict):
    content_security_policy: pulumi.Input[_builtins.str]
    override: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ResponseHeadersPolicySecurityHeadersConfigContentSecurityPolicyArgs:
    def __init__(__self__, *, content_security_policy: pulumi.Input[_builtins.str], override: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentSecurityPolicy")
    def content_security_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @content_security_policy.setter
    def content_security_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def override(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @override.setter
    def override(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ResponseHeadersPolicySecurityHeadersConfigContentTypeOptionsArgsDict(TypedDict):
    override: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ResponseHeadersPolicySecurityHeadersConfigContentTypeOptionsArgs:
    def __init__(__self__, *, override: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def override(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @override.setter
    def override(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ResponseHeadersPolicySecurityHeadersConfigFrameOptionsArgsDict(TypedDict):
    frame_option: pulumi.Input[_builtins.str]
    override: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ResponseHeadersPolicySecurityHeadersConfigFrameOptionsArgs:
    def __init__(__self__, *, frame_option: pulumi.Input[_builtins.str], override: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frameOption")
    def frame_option(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @frame_option.setter
    def frame_option(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def override(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @override.setter
    def override(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ResponseHeadersPolicySecurityHeadersConfigReferrerPolicyArgsDict(TypedDict):
    override: pulumi.Input[_builtins.bool]
    referrer_policy: pulumi.Input[_builtins.str]


@pulumi.input_type
class ResponseHeadersPolicySecurityHeadersConfigReferrerPolicyArgs:
    def __init__(__self__, *, override: pulumi.Input[_builtins.bool], referrer_policy: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def override(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @override.setter
    def override(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="referrerPolicy")
    def referrer_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @referrer_policy.setter
    def referrer_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityArgsDict(TypedDict):
    access_control_max_age_sec: pulumi.Input[_builtins.int]
    override: pulumi.Input[_builtins.bool]
    include_subdomains: NotRequired[pulumi.Input[_builtins.bool]]
    preload: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ResponseHeadersPolicySecurityHeadersConfigStrictTransportSecurityArgs:
    def __init__(__self__, *, access_control_max_age_sec: pulumi.Input[_builtins.int], override: pulumi.Input[_builtins.bool], include_subdomains: Optional[pulumi.Input[_builtins.bool]] = ..., preload: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlMaxAgeSec")
    def access_control_max_age_sec(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @access_control_max_age_sec.setter
    def access_control_max_age_sec(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def override(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @override.setter
    def override(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeSubdomains")
    def include_subdomains(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_subdomains.setter
    def include_subdomains(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def preload(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @preload.setter
    def preload(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ResponseHeadersPolicySecurityHeadersConfigXssProtectionArgsDict(TypedDict):
    override: pulumi.Input[_builtins.bool]
    protection: pulumi.Input[_builtins.bool]
    mode_block: NotRequired[pulumi.Input[_builtins.bool]]
    report_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResponseHeadersPolicySecurityHeadersConfigXssProtectionArgs:
    def __init__(__self__, *, override: pulumi.Input[_builtins.bool], protection: pulumi.Input[_builtins.bool], mode_block: Optional[pulumi.Input[_builtins.bool]] = ..., report_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def override(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @override.setter
    def override(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protection(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @protection.setter
    def protection(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modeBlock")
    def mode_block(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @mode_block.setter
    def mode_block(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportUri")
    def report_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @report_uri.setter
    def report_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResponseHeadersPolicyServerTimingHeadersConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    sampling_rate: pulumi.Input[_builtins.float]


@pulumi.input_type
class ResponseHeadersPolicyServerTimingHeadersConfigArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], sampling_rate: pulumi.Input[_builtins.float]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @sampling_rate.setter
    def sampling_rate(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    


class TrustStoreCaCertificatesBundleSourceArgsDict(TypedDict):
    ca_certificates_bundle_s3_location: pulumi.Input[TrustStoreCaCertificatesBundleSourceCaCertificatesBundleS3LocationArgsDict]


@pulumi.input_type
class TrustStoreCaCertificatesBundleSourceArgs:
    def __init__(__self__, *, ca_certificates_bundle_s3_location: pulumi.Input[TrustStoreCaCertificatesBundleSourceCaCertificatesBundleS3LocationArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleS3Location")
    def ca_certificates_bundle_s3_location(self) -> pulumi.Input[TrustStoreCaCertificatesBundleSourceCaCertificatesBundleS3LocationArgs]:
        
        ...
    
    @ca_certificates_bundle_s3_location.setter
    def ca_certificates_bundle_s3_location(self, value: pulumi.Input[TrustStoreCaCertificatesBundleSourceCaCertificatesBundleS3LocationArgs]): # -> None:
        ...
    


class TrustStoreCaCertificatesBundleSourceCaCertificatesBundleS3LocationArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    region: pulumi.Input[_builtins.str]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TrustStoreCaCertificatesBundleSourceCaCertificatesBundleS3LocationArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], key: pulumi.Input[_builtins.str], region: pulumi.Input[_builtins.str], version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TrustStoreTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TrustStoreTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpcOriginTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VpcOriginTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VpcOriginVpcOriginEndpointConfigArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    http_port: pulumi.Input[_builtins.int]
    https_port: pulumi.Input[_builtins.int]
    name: pulumi.Input[_builtins.str]
    origin_protocol_policy: pulumi.Input[_builtins.str]
    origin_ssl_protocols: pulumi.Input[VpcOriginVpcOriginEndpointConfigOriginSslProtocolsArgsDict]


@pulumi.input_type
class VpcOriginVpcOriginEndpointConfigArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str], http_port: pulumi.Input[_builtins.int], https_port: pulumi.Input[_builtins.int], name: pulumi.Input[_builtins.str], origin_protocol_policy: pulumi.Input[_builtins.str], origin_ssl_protocols: pulumi.Input[VpcOriginVpcOriginEndpointConfigOriginSslProtocolsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @http_port.setter
    def http_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @https_port.setter
    def https_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originProtocolPolicy")
    def origin_protocol_policy(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @origin_protocol_policy.setter
    def origin_protocol_policy(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originSslProtocols")
    def origin_ssl_protocols(self) -> pulumi.Input[VpcOriginVpcOriginEndpointConfigOriginSslProtocolsArgs]:
        
        ...
    
    @origin_ssl_protocols.setter
    def origin_ssl_protocols(self, value: pulumi.Input[VpcOriginVpcOriginEndpointConfigOriginSslProtocolsArgs]): # -> None:
        ...
    


class VpcOriginVpcOriginEndpointConfigOriginSslProtocolsArgsDict(TypedDict):
    items: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    quantity: pulumi.Input[_builtins.int]


@pulumi.input_type
class VpcOriginVpcOriginEndpointConfigOriginSslProtocolsArgs:
    def __init__(__self__, *, items: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], quantity: pulumi.Input[_builtins.int]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        ...
    
    @items.setter
    def items(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def quantity(self) -> pulumi.Input[_builtins.int]:
        ...
    
    @quantity.setter
    def quantity(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


