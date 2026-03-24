import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AgentGatewayAgentGatewayCardArgs",
    "AgentGatewayAgentGatewayCardArgsDict",
    "AgentGatewayGoogleManagedArgs",
    "AgentGatewayGoogleManagedArgsDict",
    "AgentGatewayNetworkConfigArgs",
    "AgentGatewayNetworkConfigArgsDict",
    "AgentGatewayNetworkConfigEgressArgs",
    "AgentGatewayNetworkConfigEgressArgsDict",
    "AgentGatewaySelfManagedArgs",
    "AgentGatewaySelfManagedArgsDict",
    "EdgeCacheKeysetPublicKeyArgs",
    "EdgeCacheKeysetPublicKeyArgsDict",
    "EdgeCacheKeysetValidationSharedKeyArgs",
    "EdgeCacheKeysetValidationSharedKeyArgsDict",
    "EdgeCacheOriginAwsV4AuthenticationArgs",
    "EdgeCacheOriginAwsV4AuthenticationArgsDict",
    "EdgeCacheOriginFlexShieldingArgs",
    "EdgeCacheOriginFlexShieldingArgsDict",
    "EdgeCacheOriginOriginOverrideActionArgs",
    "EdgeCacheOriginOriginOverrideActionArgsDict",
    ...,
    ...,
    ...,
    ...,
    "EdgeCacheOriginOriginOverrideActionUrlRewriteArgs",
    ...,
    "EdgeCacheOriginOriginRedirectArgs",
    "EdgeCacheOriginOriginRedirectArgsDict",
    "EdgeCacheOriginTimeoutArgs",
    "EdgeCacheOriginTimeoutArgsDict",
    "EdgeCacheServiceLogConfigArgs",
    "EdgeCacheServiceLogConfigArgsDict",
    "EdgeCacheServiceRoutingArgs",
    "EdgeCacheServiceRoutingArgsDict",
    "EdgeCacheServiceRoutingHostRuleArgs",
    "EdgeCacheServiceRoutingHostRuleArgsDict",
    "EdgeCacheServiceRoutingPathMatcherArgs",
    "EdgeCacheServiceRoutingPathMatcherArgsDict",
    "EdgeCacheServiceRoutingPathMatcherRouteRuleArgs",
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
    ...,
    "EndpointPolicyEndpointMatcherArgs",
    "EndpointPolicyEndpointMatcherArgsDict",
    ...,
    ...,
    ...,
    ...,
    "EndpointPolicyTrafficPortSelectorArgs",
    "EndpointPolicyTrafficPortSelectorArgsDict",
    "GrpcRouteRuleArgs",
    "GrpcRouteRuleArgsDict",
    "GrpcRouteRuleActionArgs",
    "GrpcRouteRuleActionArgsDict",
    "GrpcRouteRuleActionDestinationArgs",
    "GrpcRouteRuleActionDestinationArgsDict",
    "GrpcRouteRuleActionFaultInjectionPolicyArgs",
    "GrpcRouteRuleActionFaultInjectionPolicyArgsDict",
    "GrpcRouteRuleActionFaultInjectionPolicyAbortArgs",
    ...,
    "GrpcRouteRuleActionFaultInjectionPolicyDelayArgs",
    ...,
    "GrpcRouteRuleActionRetryPolicyArgs",
    "GrpcRouteRuleActionRetryPolicyArgsDict",
    "GrpcRouteRuleMatchArgs",
    "GrpcRouteRuleMatchArgsDict",
    "GrpcRouteRuleMatchHeaderArgs",
    "GrpcRouteRuleMatchHeaderArgsDict",
    "GrpcRouteRuleMatchMethodArgs",
    "GrpcRouteRuleMatchMethodArgsDict",
    "HttpRouteRuleArgs",
    "HttpRouteRuleArgsDict",
    "HttpRouteRuleActionArgs",
    "HttpRouteRuleActionArgsDict",
    "HttpRouteRuleActionCorsPolicyArgs",
    "HttpRouteRuleActionCorsPolicyArgsDict",
    "HttpRouteRuleActionDestinationArgs",
    "HttpRouteRuleActionDestinationArgsDict",
    "HttpRouteRuleActionFaultInjectionPolicyArgs",
    "HttpRouteRuleActionFaultInjectionPolicyArgsDict",
    "HttpRouteRuleActionFaultInjectionPolicyAbortArgs",
    ...,
    "HttpRouteRuleActionFaultInjectionPolicyDelayArgs",
    ...,
    "HttpRouteRuleActionRedirectArgs",
    "HttpRouteRuleActionRedirectArgsDict",
    "HttpRouteRuleActionRequestHeaderModifierArgs",
    "HttpRouteRuleActionRequestHeaderModifierArgsDict",
    "HttpRouteRuleActionRequestMirrorPolicyArgs",
    "HttpRouteRuleActionRequestMirrorPolicyArgsDict",
    ...,
    ...,
    "HttpRouteRuleActionResponseHeaderModifierArgs",
    "HttpRouteRuleActionResponseHeaderModifierArgsDict",
    "HttpRouteRuleActionRetryPolicyArgs",
    "HttpRouteRuleActionRetryPolicyArgsDict",
    "HttpRouteRuleActionUrlRewriteArgs",
    "HttpRouteRuleActionUrlRewriteArgsDict",
    "HttpRouteRuleMatchArgs",
    "HttpRouteRuleMatchArgsDict",
    "HttpRouteRuleMatchHeaderArgs",
    "HttpRouteRuleMatchHeaderArgsDict",
    "HttpRouteRuleMatchHeaderRangeMatchArgs",
    "HttpRouteRuleMatchHeaderRangeMatchArgsDict",
    "HttpRouteRuleMatchQueryParameterArgs",
    "HttpRouteRuleMatchQueryParameterArgsDict",
    "LbEdgeExtensionExtensionChainArgs",
    "LbEdgeExtensionExtensionChainArgsDict",
    "LbEdgeExtensionExtensionChainExtensionArgs",
    "LbEdgeExtensionExtensionChainExtensionArgsDict",
    "LbEdgeExtensionExtensionChainMatchConditionArgs",
    ...,
    "LbRouteExtensionExtensionChainArgs",
    "LbRouteExtensionExtensionChainArgsDict",
    "LbRouteExtensionExtensionChainExtensionArgs",
    "LbRouteExtensionExtensionChainExtensionArgsDict",
    "LbRouteExtensionExtensionChainMatchConditionArgs",
    ...,
    "LbTrafficExtensionExtensionChainArgs",
    "LbTrafficExtensionExtensionChainArgsDict",
    "LbTrafficExtensionExtensionChainExtensionArgs",
    "LbTrafficExtensionExtensionChainExtensionArgsDict",
    "LbTrafficExtensionExtensionChainMatchConditionArgs",
    ...,
    "MulticastConsumerAssociationStateArgs",
    "MulticastConsumerAssociationStateArgsDict",
    "MulticastDomainActivationStateArgs",
    "MulticastDomainActivationStateArgsDict",
    "MulticastDomainActivationTrafficSpecArgs",
    "MulticastDomainActivationTrafficSpecArgsDict",
    "MulticastDomainConnectionConfigArgs",
    "MulticastDomainConnectionConfigArgsDict",
    "MulticastDomainGroupStateArgs",
    "MulticastDomainGroupStateArgsDict",
    "MulticastDomainStateArgs",
    "MulticastDomainStateArgsDict",
    "MulticastDomainUllMulticastDomainArgs",
    "MulticastDomainUllMulticastDomainArgsDict",
    "MulticastGroupConsumerActivationLogConfigArgs",
    "MulticastGroupConsumerActivationLogConfigArgsDict",
    "MulticastGroupConsumerActivationStateArgs",
    "MulticastGroupConsumerActivationStateArgsDict",
    "MulticastGroupProducerActivationStateArgs",
    "MulticastGroupProducerActivationStateArgsDict",
    "MulticastGroupRangeActivationLogConfigArgs",
    "MulticastGroupRangeActivationLogConfigArgsDict",
    "MulticastGroupRangeActivationStateArgs",
    "MulticastGroupRangeActivationStateArgsDict",
    "MulticastGroupRangeLogConfigArgs",
    "MulticastGroupRangeLogConfigArgsDict",
    "MulticastGroupRangeStateArgs",
    "MulticastGroupRangeStateArgsDict",
    "MulticastProducerAssociationStateArgs",
    "MulticastProducerAssociationStateArgsDict",
    "ServiceLbPoliciesAutoCapacityDrainArgs",
    "ServiceLbPoliciesAutoCapacityDrainArgsDict",
    "ServiceLbPoliciesFailoverConfigArgs",
    "ServiceLbPoliciesFailoverConfigArgsDict",
    "ServiceLbPoliciesIsolationConfigArgs",
    "ServiceLbPoliciesIsolationConfigArgsDict",
    "TcpRouteRuleArgs",
    "TcpRouteRuleArgsDict",
    "TcpRouteRuleActionArgs",
    "TcpRouteRuleActionArgsDict",
    "TcpRouteRuleActionDestinationArgs",
    "TcpRouteRuleActionDestinationArgsDict",
    "TcpRouteRuleMatchArgs",
    "TcpRouteRuleMatchArgsDict",
    "TlsRouteRuleArgs",
    "TlsRouteRuleArgsDict",
    "TlsRouteRuleActionArgs",
    "TlsRouteRuleActionArgsDict",
    "TlsRouteRuleActionDestinationArgs",
    "TlsRouteRuleActionDestinationArgsDict",
    "TlsRouteRuleMatchArgs",
    "TlsRouteRuleMatchArgsDict",
    "WasmPluginLogConfigArgs",
    "WasmPluginLogConfigArgsDict",
    "WasmPluginUsedByArgs",
    "WasmPluginUsedByArgsDict",
    "WasmPluginVersionArgs",
    "WasmPluginVersionArgsDict",
]

class AgentGatewayAgentGatewayCardArgsDict(TypedDict):
    mtls_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    root_certificates: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    service_extensions_service_account: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AgentGatewayAgentGatewayCardArgs:
    def __init__(
        __self__,
        *,
        mtls_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        root_certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        service_extensions_service_account: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mtlsEndpoint")
    def mtls_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mtls_endpoint.setter
    def mtls_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootCertificates")
    def root_certificates(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @root_certificates.setter
    def root_certificates(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceExtensionsServiceAccount")
    def service_extensions_service_account(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_extensions_service_account.setter
    def service_extensions_service_account(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class AgentGatewayGoogleManagedArgsDict(TypedDict):
    governed_access_path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AgentGatewayGoogleManagedArgs:
    def __init__(
        __self__, *, governed_access_path: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="governedAccessPath")
    def governed_access_path(self) -> pulumi.Input[_builtins.str]: ...
    @governed_access_path.setter
    def governed_access_path(self, value: pulumi.Input[_builtins.str]): ...

class AgentGatewayNetworkConfigArgsDict(TypedDict):
    egress: pulumi.Input[AgentGatewayNetworkConfigEgressArgsDict]
    ...

@pulumi.input_type
class AgentGatewayNetworkConfigArgs:
    def __init__(
        __self__, *, egress: pulumi.Input[AgentGatewayNetworkConfigEgressArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def egress(self) -> pulumi.Input[AgentGatewayNetworkConfigEgressArgs]: ...
    @egress.setter
    def egress(self, value: pulumi.Input[AgentGatewayNetworkConfigEgressArgs]): ...

class AgentGatewayNetworkConfigEgressArgsDict(TypedDict):
    network_attachment: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AgentGatewayNetworkConfigEgressArgs:
    def __init__(
        __self__, *, network_attachment: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> pulumi.Input[_builtins.str]: ...
    @network_attachment.setter
    def network_attachment(self, value: pulumi.Input[_builtins.str]): ...

class AgentGatewaySelfManagedArgsDict(TypedDict):
    resource_uri: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AgentGatewaySelfManagedArgs:
    def __init__(__self__, *, resource_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[_builtins.str]: ...
    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[_builtins.str]): ...

class EdgeCacheKeysetPublicKeyArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    managed: NotRequired[pulumi.Input[_builtins.bool]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EdgeCacheKeysetPublicKeyArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        managed: Optional[pulumi.Input[_builtins.bool]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def managed(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @managed.setter
    def managed(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EdgeCacheKeysetValidationSharedKeyArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class EdgeCacheKeysetValidationSharedKeyArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class EdgeCacheOriginAwsV4AuthenticationArgsDict(TypedDict):
    access_key_id: pulumi.Input[_builtins.str]
    origin_region: pulumi.Input[_builtins.str]
    secret_access_key_version: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class EdgeCacheOriginAwsV4AuthenticationArgs:
    def __init__(
        __self__,
        *,
        access_key_id: pulumi.Input[_builtins.str],
        origin_region: pulumi.Input[_builtins.str],
        secret_access_key_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> pulumi.Input[_builtins.str]: ...
    @access_key_id.setter
    def access_key_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="originRegion")
    def origin_region(self) -> pulumi.Input[_builtins.str]: ...
    @origin_region.setter
    def origin_region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secretAccessKeyVersion")
    def secret_access_key_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_access_key_version.setter
    def secret_access_key_version(self, value: pulumi.Input[_builtins.str]): ...

class EdgeCacheOriginFlexShieldingArgsDict(TypedDict):
    flex_shielding_regions: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EdgeCacheOriginFlexShieldingArgs:
    def __init__(
        __self__, *, flex_shielding_regions: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="flexShieldingRegions")
    def flex_shielding_regions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flex_shielding_regions.setter
    def flex_shielding_regions(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EdgeCacheOriginOriginOverrideActionArgsDict(TypedDict):
    header_action: NotRequired[
        pulumi.Input[EdgeCacheOriginOriginOverrideActionHeaderActionArgsDict]
    ]
    url_rewrite: NotRequired[
        pulumi.Input[EdgeCacheOriginOriginOverrideActionUrlRewriteArgsDict]
    ]
    ...

@pulumi.input_type
class EdgeCacheOriginOriginOverrideActionArgs:
    def __init__(
        __self__,
        *,
        header_action: Optional[
            pulumi.Input[EdgeCacheOriginOriginOverrideActionHeaderActionArgs]
        ] = ...,
        url_rewrite: Optional[
            pulumi.Input[EdgeCacheOriginOriginOverrideActionUrlRewriteArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerAction")
    def header_action(
        self,
    ) -> Optional[
        pulumi.Input[EdgeCacheOriginOriginOverrideActionHeaderActionArgs]
    ]: ...
    @header_action.setter
    def header_action(
        self,
        value: Optional[
            pulumi.Input[EdgeCacheOriginOriginOverrideActionHeaderActionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="urlRewrite")
    def url_rewrite(
        self,
    ) -> Optional[pulumi.Input[EdgeCacheOriginOriginOverrideActionUrlRewriteArgs]]: ...
    @url_rewrite.setter
    def url_rewrite(
        self,
        value: Optional[
            pulumi.Input[EdgeCacheOriginOriginOverrideActionUrlRewriteArgs]
        ],
    ): ...

class EdgeCacheOriginOriginOverrideActionHeaderActionArgsDict(TypedDict):
    request_headers_to_adds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheOriginOriginOverrideActionHeaderActionRequestHeadersToAddArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class EdgeCacheOriginOriginOverrideActionHeaderActionArgs:
    def __init__(
        __self__,
        *,
        request_headers_to_adds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheOriginOriginOverrideActionHeaderActionRequestHeadersToAddArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requestHeadersToAdds")
    def request_headers_to_adds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheOriginOriginOverrideActionHeaderActionRequestHeadersToAddArgs
                ]
            ]
        ]
    ]: ...
    @request_headers_to_adds.setter
    def request_headers_to_adds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheOriginOriginOverrideActionHeaderActionRequestHeadersToAddArgs
                    ]
                ]
            ]
        ],
    ): ...

class EdgeCacheOriginOriginOverrideActionHeaderActionRequestHeadersToAddArgsDict(
    TypedDict
):
    header_name: pulumi.Input[_builtins.str]
    header_value: pulumi.Input[_builtins.str]
    replace: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class EdgeCacheOriginOriginOverrideActionHeaderActionRequestHeadersToAddArgs:
    def __init__(
        __self__,
        *,
        header_name: pulumi.Input[_builtins.str],
        header_value: pulumi.Input[_builtins.str],
        replace: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> pulumi.Input[_builtins.str]: ...
    @header_name.setter
    def header_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> pulumi.Input[_builtins.str]: ...
    @header_value.setter
    def header_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def replace(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @replace.setter
    def replace(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EdgeCacheOriginOriginOverrideActionUrlRewriteArgsDict(TypedDict):
    host_rewrite: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EdgeCacheOriginOriginOverrideActionUrlRewriteArgs:
    def __init__(
        __self__, *, host_rewrite: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostRewrite")
    def host_rewrite(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_rewrite.setter
    def host_rewrite(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EdgeCacheOriginOriginRedirectArgsDict(TypedDict):
    redirect_conditions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class EdgeCacheOriginOriginRedirectArgs:
    def __init__(
        __self__,
        *,
        redirect_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="redirectConditions")
    def redirect_conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @redirect_conditions.setter
    def redirect_conditions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class EdgeCacheOriginTimeoutArgsDict(TypedDict):
    connect_timeout: NotRequired[pulumi.Input[_builtins.str]]
    max_attempts_timeout: NotRequired[pulumi.Input[_builtins.str]]
    read_timeout: NotRequired[pulumi.Input[_builtins.str]]
    response_timeout: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EdgeCacheOriginTimeoutArgs:
    def __init__(
        __self__,
        *,
        connect_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        max_attempts_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        read_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        response_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectTimeout")
    def connect_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connect_timeout.setter
    def connect_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxAttemptsTimeout")
    def max_attempts_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_attempts_timeout.setter
    def max_attempts_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="readTimeout")
    def read_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @read_timeout.setter
    def read_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="responseTimeout")
    def response_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @response_timeout.setter
    def response_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EdgeCacheServiceLogConfigArgsDict(TypedDict):
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    sample_rate: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class EdgeCacheServiceLogConfigArgs:
    def __init__(
        __self__,
        *,
        enable: Optional[pulumi.Input[_builtins.bool]] = ...,
        sample_rate: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sampleRate")
    def sample_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @sample_rate.setter
    def sample_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class EdgeCacheServiceRoutingArgsDict(TypedDict):
    host_rules: pulumi.Input[
        Sequence[pulumi.Input[EdgeCacheServiceRoutingHostRuleArgsDict]]
    ]
    path_matchers: pulumi.Input[
        Sequence[pulumi.Input[EdgeCacheServiceRoutingPathMatcherArgsDict]]
    ]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingArgs:
    def __init__(
        __self__,
        *,
        host_rules: pulumi.Input[
            Sequence[pulumi.Input[EdgeCacheServiceRoutingHostRuleArgs]]
        ],
        path_matchers: pulumi.Input[
            Sequence[pulumi.Input[EdgeCacheServiceRoutingPathMatcherArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostRules")
    def host_rules(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[EdgeCacheServiceRoutingHostRuleArgs]]]: ...
    @host_rules.setter
    def host_rules(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[EdgeCacheServiceRoutingHostRuleArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pathMatchers")
    def path_matchers(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[EdgeCacheServiceRoutingPathMatcherArgs]]
    ]: ...
    @path_matchers.setter
    def path_matchers(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[EdgeCacheServiceRoutingPathMatcherArgs]]
        ],
    ): ...

class EdgeCacheServiceRoutingHostRuleArgsDict(TypedDict):
    hosts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    path_matcher: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingHostRuleArgs:
    def __init__(
        __self__,
        *,
        hosts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        path_matcher: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @hosts.setter
    def hosts(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="pathMatcher")
    def path_matcher(self) -> pulumi.Input[_builtins.str]: ...
    @path_matcher.setter
    def path_matcher(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EdgeCacheServiceRoutingPathMatcherArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    route_rules: pulumi.Input[
        Sequence[pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleArgsDict]]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        route_rules: pulumi.Input[
            Sequence[pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleArgs]]
        ],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="routeRules")
    def route_rules(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleArgs]]
    ]: ...
    @route_rules.setter
    def route_rules(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleArgsDict(TypedDict):
    match_rules: pulumi.Input[
        Sequence[
            pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleArgsDict]
        ]
    ]
    priority: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    header_action: NotRequired[
        pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionArgsDict]
    ]
    origin: NotRequired[pulumi.Input[_builtins.str]]
    route_action: NotRequired[
        pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionArgsDict]
    ]
    route_methods: NotRequired[
        pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleRouteMethodsArgsDict]
    ]
    url_redirect: NotRequired[
        pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleUrlRedirectArgsDict]
    ]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleArgs:
    def __init__(
        __self__,
        *,
        match_rules: pulumi.Input[
            Sequence[
                pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleArgs]
            ]
        ],
        priority: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        header_action: Optional[
            pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionArgs]
        ] = ...,
        origin: Optional[pulumi.Input[_builtins.str]] = ...,
        route_action: Optional[
            pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionArgs]
        ] = ...,
        route_methods: Optional[
            pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleRouteMethodsArgs]
        ] = ...,
        url_redirect: Optional[
            pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleUrlRedirectArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchRules")
    def match_rules(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleArgs]]
    ]: ...
    @match_rules.setter
    def match_rules(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.str]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="headerAction")
    def header_action(
        self,
    ) -> Optional[
        pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionArgs]
    ]: ...
    @header_action.setter
    def header_action(
        self,
        value: Optional[
            pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def origin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @origin.setter
    def origin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routeAction")
    def route_action(
        self,
    ) -> Optional[
        pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionArgs]
    ]: ...
    @route_action.setter
    def route_action(
        self,
        value: Optional[
            pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="routeMethods")
    def route_methods(
        self,
    ) -> Optional[
        pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleRouteMethodsArgs]
    ]: ...
    @route_methods.setter
    def route_methods(
        self,
        value: Optional[
            pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleRouteMethodsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="urlRedirect")
    def url_redirect(
        self,
    ) -> Optional[
        pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleUrlRedirectArgs]
    ]: ...
    @url_redirect.setter
    def url_redirect(
        self,
        value: Optional[
            pulumi.Input[EdgeCacheServiceRoutingPathMatcherRouteRuleUrlRedirectArgs]
        ],
    ): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionArgsDict(TypedDict):
    request_header_to_adds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToAddArgsDict
                ]
            ]
        ]
    ]
    request_header_to_removes: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToRemoveArgsDict
                ]
            ]
        ]
    ]
    response_header_to_adds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToAddArgsDict
                ]
            ]
        ]
    ]
    response_header_to_removes: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToRemoveArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionArgs:
    def __init__(
        __self__,
        *,
        request_header_to_adds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToAddArgs
                    ]
                ]
            ]
        ] = ...,
        request_header_to_removes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToRemoveArgs
                    ]
                ]
            ]
        ] = ...,
        response_header_to_adds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToAddArgs
                    ]
                ]
            ]
        ] = ...,
        response_header_to_removes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToRemoveArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderToAdds")
    def request_header_to_adds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToAddArgs
                ]
            ]
        ]
    ]: ...
    @request_header_to_adds.setter
    def request_header_to_adds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToAddArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderToRemoves")
    def request_header_to_removes(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToRemoveArgs
                ]
            ]
        ]
    ]: ...
    @request_header_to_removes.setter
    def request_header_to_removes(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToRemoveArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="responseHeaderToAdds")
    def response_header_to_adds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToAddArgs
                ]
            ]
        ]
    ]: ...
    @response_header_to_adds.setter
    def response_header_to_adds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToAddArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="responseHeaderToRemoves")
    def response_header_to_removes(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToRemoveArgs
                ]
            ]
        ]
    ]: ...
    @response_header_to_removes.setter
    def response_header_to_removes(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToRemoveArgs
                    ]
                ]
            ]
        ],
    ): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToAddArgsDict(
    TypedDict
):
    header_name: pulumi.Input[_builtins.str]
    header_value: pulumi.Input[_builtins.str]
    replace: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToAddArgs:
    def __init__(
        __self__,
        *,
        header_name: pulumi.Input[_builtins.str],
        header_value: pulumi.Input[_builtins.str],
        replace: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> pulumi.Input[_builtins.str]: ...
    @header_name.setter
    def header_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> pulumi.Input[_builtins.str]: ...
    @header_value.setter
    def header_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def replace(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @replace.setter
    def replace(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToRemoveArgsDict(
    TypedDict
):
    header_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToRemoveArgs:
    def __init__(__self__, *, header_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> pulumi.Input[_builtins.str]: ...
    @header_name.setter
    def header_name(self, value: pulumi.Input[_builtins.str]): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToAddArgsDict(
    TypedDict
):
    header_name: pulumi.Input[_builtins.str]
    header_value: pulumi.Input[_builtins.str]
    replace: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToAddArgs:
    def __init__(
        __self__,
        *,
        header_name: pulumi.Input[_builtins.str],
        header_value: pulumi.Input[_builtins.str],
        replace: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> pulumi.Input[_builtins.str]: ...
    @header_name.setter
    def header_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> pulumi.Input[_builtins.str]: ...
    @header_value.setter
    def header_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def replace(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @replace.setter
    def replace(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToRemoveArgsDict(
    TypedDict
):
    header_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToRemoveArgs:
    def __init__(__self__, *, header_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> pulumi.Input[_builtins.str]: ...
    @header_name.setter
    def header_name(self, value: pulumi.Input[_builtins.str]): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleArgsDict(TypedDict):
    full_path_match: NotRequired[pulumi.Input[_builtins.str]]
    header_matches: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleHeaderMatchArgsDict
                ]
            ]
        ]
    ]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    path_template_match: NotRequired[pulumi.Input[_builtins.str]]
    prefix_match: NotRequired[pulumi.Input[_builtins.str]]
    query_parameter_matches: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleQueryParameterMatchArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleArgs:
    def __init__(
        __self__,
        *,
        full_path_match: Optional[pulumi.Input[_builtins.str]] = ...,
        header_matches: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleHeaderMatchArgs
                    ]
                ]
            ]
        ] = ...,
        ignore_case: Optional[pulumi.Input[_builtins.bool]] = ...,
        path_template_match: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix_match: Optional[pulumi.Input[_builtins.str]] = ...,
        query_parameter_matches: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleQueryParameterMatchArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fullPathMatch")
    def full_path_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @full_path_match.setter
    def full_path_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="headerMatches")
    def header_matches(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleHeaderMatchArgs
                ]
            ]
        ]
    ]: ...
    @header_matches.setter
    def header_matches(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleHeaderMatchArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pathTemplateMatch")
    def path_template_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path_template_match.setter
    def path_template_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_match.setter
    def prefix_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryParameterMatches")
    def query_parameter_matches(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleQueryParameterMatchArgs
                ]
            ]
        ]
    ]: ...
    @query_parameter_matches.setter
    def query_parameter_matches(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleQueryParameterMatchArgs
                    ]
                ]
            ]
        ],
    ): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleHeaderMatchArgsDict(
    TypedDict
):
    header_name: pulumi.Input[_builtins.str]
    exact_match: NotRequired[pulumi.Input[_builtins.str]]
    invert_match: NotRequired[pulumi.Input[_builtins.bool]]
    prefix_match: NotRequired[pulumi.Input[_builtins.str]]
    present_match: NotRequired[pulumi.Input[_builtins.bool]]
    suffix_match: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleHeaderMatchArgs:
    def __init__(
        __self__,
        *,
        header_name: pulumi.Input[_builtins.str],
        exact_match: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        prefix_match: Optional[pulumi.Input[_builtins.str]] = ...,
        present_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        suffix_match: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> pulumi.Input[_builtins.str]: ...
    @header_name.setter
    def header_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact_match.setter
    def exact_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertMatch")
    def invert_match(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_match.setter
    def invert_match(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_match.setter
    def prefix_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="presentMatch")
    def present_match(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @present_match.setter
    def present_match(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="suffixMatch")
    def suffix_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suffix_match.setter
    def suffix_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleQueryParameterMatchArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    exact_match: NotRequired[pulumi.Input[_builtins.str]]
    present_match: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleQueryParameterMatchArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        exact_match: Optional[pulumi.Input[_builtins.str]] = ...,
        present_match: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact_match.setter
    def exact_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="presentMatch")
    def present_match(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @present_match.setter
    def present_match(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionArgsDict(TypedDict):
    cdn_policy: NotRequired[
        pulumi.Input[
            EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyArgsDict
        ]
    ]
    compression_mode: NotRequired[pulumi.Input[_builtins.str]]
    cors_policy: NotRequired[
        pulumi.Input[
            EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCorsPolicyArgsDict
        ]
    ]
    url_rewrite: NotRequired[
        pulumi.Input[
            EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionUrlRewriteArgsDict
        ]
    ]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionArgs:
    def __init__(
        __self__,
        *,
        cdn_policy: Optional[
            pulumi.Input[
                EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyArgs
            ]
        ] = ...,
        compression_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        cors_policy: Optional[
            pulumi.Input[
                EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCorsPolicyArgs
            ]
        ] = ...,
        url_rewrite: Optional[
            pulumi.Input[
                EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionUrlRewriteArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicy")
    def cdn_policy(
        self,
    ) -> Optional[
        pulumi.Input[
            EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyArgs
        ]
    ]: ...
    @cdn_policy.setter
    def cdn_policy(
        self,
        value: Optional[
            pulumi.Input[
                EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="compressionMode")
    def compression_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression_mode.setter
    def compression_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="corsPolicy")
    def cors_policy(
        self,
    ) -> Optional[
        pulumi.Input[
            EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCorsPolicyArgs
        ]
    ]: ...
    @cors_policy.setter
    def cors_policy(
        self,
        value: Optional[
            pulumi.Input[
                EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCorsPolicyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="urlRewrite")
    def url_rewrite(
        self,
    ) -> Optional[
        pulumi.Input[
            EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionUrlRewriteArgs
        ]
    ]: ...
    @url_rewrite.setter
    def url_rewrite(
        self,
        value: Optional[
            pulumi.Input[
                EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionUrlRewriteArgs
            ]
        ],
    ): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyArgsDict(
    TypedDict
):
    add_signatures: NotRequired[
        pulumi.Input[
            EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyAddSignaturesArgsDict
        ]
    ]
    cache_key_policy: NotRequired[
        pulumi.Input[
            EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyCacheKeyPolicyArgsDict
        ]
    ]
    cache_mode: NotRequired[pulumi.Input[_builtins.str]]
    client_ttl: NotRequired[pulumi.Input[_builtins.str]]
    default_ttl: NotRequired[pulumi.Input[_builtins.str]]
    max_ttl: NotRequired[pulumi.Input[_builtins.str]]
    negative_caching: NotRequired[pulumi.Input[_builtins.bool]]
    negative_caching_policy: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    signed_request_keyset: NotRequired[pulumi.Input[_builtins.str]]
    signed_request_maximum_expiration_ttl: NotRequired[pulumi.Input[_builtins.str]]
    signed_request_mode: NotRequired[pulumi.Input[_builtins.str]]
    signed_token_options: NotRequired[
        pulumi.Input[
            EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicySignedTokenOptionsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyArgs:
    def __init__(
        __self__,
        *,
        add_signatures: Optional[
            pulumi.Input[
                EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyAddSignaturesArgs
            ]
        ] = ...,
        cache_key_policy: Optional[
            pulumi.Input[
                EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyCacheKeyPolicyArgs
            ]
        ] = ...,
        cache_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        client_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        default_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        max_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        negative_caching: Optional[pulumi.Input[_builtins.bool]] = ...,
        negative_caching_policy: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        signed_request_keyset: Optional[pulumi.Input[_builtins.str]] = ...,
        signed_request_maximum_expiration_ttl: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        signed_request_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        signed_token_options: Optional[
            pulumi.Input[
                EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicySignedTokenOptionsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addSignatures")
    def add_signatures(
        self,
    ) -> Optional[
        pulumi.Input[
            EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyAddSignaturesArgs
        ]
    ]: ...
    @add_signatures.setter
    def add_signatures(
        self,
        value: Optional[
            pulumi.Input[
                EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyAddSignaturesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cacheKeyPolicy")
    def cache_key_policy(
        self,
    ) -> Optional[
        pulumi.Input[
            EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyCacheKeyPolicyArgs
        ]
    ]: ...
    @cache_key_policy.setter
    def cache_key_policy(
        self,
        value: Optional[
            pulumi.Input[
                EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyCacheKeyPolicyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cacheMode")
    def cache_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cache_mode.setter
    def cache_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientTtl")
    def client_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_ttl.setter
    def client_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_ttl.setter
    def max_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="negativeCaching")
    def negative_caching(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @negative_caching.setter
    def negative_caching(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="negativeCachingPolicy")
    def negative_caching_policy(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @negative_caching_policy.setter
    def negative_caching_policy(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signedRequestKeyset")
    def signed_request_keyset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signed_request_keyset.setter
    def signed_request_keyset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="signedRequestMaximumExpirationTtl")
    def signed_request_maximum_expiration_ttl(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signed_request_maximum_expiration_ttl.setter
    def signed_request_maximum_expiration_ttl(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signedRequestMode")
    def signed_request_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signed_request_mode.setter
    def signed_request_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="signedTokenOptions")
    def signed_token_options(
        self,
    ) -> Optional[
        pulumi.Input[
            EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicySignedTokenOptionsArgs
        ]
    ]: ...
    @signed_token_options.setter
    def signed_token_options(
        self,
        value: Optional[
            pulumi.Input[
                EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicySignedTokenOptionsArgs
            ]
        ],
    ): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyAddSignaturesArgsDict(
    TypedDict
):
    actions: pulumi.Input[_builtins.str]
    copied_parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    keyset: NotRequired[pulumi.Input[_builtins.str]]
    token_query_parameter: NotRequired[pulumi.Input[_builtins.str]]
    token_ttl: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyAddSignaturesArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[_builtins.str],
        copied_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        keyset: Optional[pulumi.Input[_builtins.str]] = ...,
        token_query_parameter: Optional[pulumi.Input[_builtins.str]] = ...,
        token_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[_builtins.str]: ...
    @actions.setter
    def actions(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="copiedParameters")
    def copied_parameters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @copied_parameters.setter
    def copied_parameters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def keyset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @keyset.setter
    def keyset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tokenQueryParameter")
    def token_query_parameter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_query_parameter.setter
    def token_query_parameter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tokenTtl")
    def token_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_ttl.setter
    def token_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyCacheKeyPolicyArgsDict(
    TypedDict
):
    exclude_host: NotRequired[pulumi.Input[_builtins.bool]]
    exclude_query_string: NotRequired[pulumi.Input[_builtins.bool]]
    excluded_query_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    include_protocol: NotRequired[pulumi.Input[_builtins.bool]]
    included_cookie_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    included_header_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    included_query_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyCacheKeyPolicyArgs:
    def __init__(
        __self__,
        *,
        exclude_host: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclude_query_string: Optional[pulumi.Input[_builtins.bool]] = ...,
        excluded_query_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_protocol: Optional[pulumi.Input[_builtins.bool]] = ...,
        included_cookie_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        included_header_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        included_query_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludeHost")
    def exclude_host(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @exclude_host.setter
    def exclude_host(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="excludeQueryString")
    def exclude_query_string(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @exclude_query_string.setter
    def exclude_query_string(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="excludedQueryParameters")
    def excluded_query_parameters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @excluded_query_parameters.setter
    def excluded_query_parameters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeProtocol")
    def include_protocol(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_protocol.setter
    def include_protocol(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includedCookieNames")
    def included_cookie_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_cookie_names.setter
    def included_cookie_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includedHeaderNames")
    def included_header_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_header_names.setter
    def included_header_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includedQueryParameters")
    def included_query_parameters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_query_parameters.setter
    def included_query_parameters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicySignedTokenOptionsArgsDict(
    TypedDict
):
    allowed_signature_algorithms: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    token_query_parameter: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicySignedTokenOptionsArgs:
    def __init__(
        __self__,
        *,
        allowed_signature_algorithms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        token_query_parameter: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSignatureAlgorithms")
    def allowed_signature_algorithms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_signature_algorithms.setter
    def allowed_signature_algorithms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenQueryParameter")
    def token_query_parameter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_query_parameter.setter
    def token_query_parameter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCorsPolicyArgsDict(
    TypedDict
):
    max_age: pulumi.Input[_builtins.str]
    allow_credentials: NotRequired[pulumi.Input[_builtins.bool]]
    allow_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allow_methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allow_origins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    expose_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCorsPolicyArgs:
    def __init__(
        __self__,
        *,
        max_age: pulumi.Input[_builtins.str],
        allow_credentials: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allow_methods: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allow_origins: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        expose_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> pulumi.Input[_builtins.str]: ...
    @max_age.setter
    def max_age(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_credentials.setter
    def allow_credentials(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowHeaders")
    def allow_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allow_headers.setter
    def allow_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowMethods")
    def allow_methods(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allow_methods.setter
    def allow_methods(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowOrigins")
    def allow_origins(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allow_origins.setter
    def allow_origins(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @expose_headers.setter
    def expose_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionUrlRewriteArgsDict(
    TypedDict
):
    host_rewrite: NotRequired[pulumi.Input[_builtins.str]]
    path_prefix_rewrite: NotRequired[pulumi.Input[_builtins.str]]
    path_template_rewrite: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionUrlRewriteArgs:
    def __init__(
        __self__,
        *,
        host_rewrite: Optional[pulumi.Input[_builtins.str]] = ...,
        path_prefix_rewrite: Optional[pulumi.Input[_builtins.str]] = ...,
        path_template_rewrite: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostRewrite")
    def host_rewrite(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_rewrite.setter
    def host_rewrite(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pathPrefixRewrite")
    def path_prefix_rewrite(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path_prefix_rewrite.setter
    def path_prefix_rewrite(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pathTemplateRewrite")
    def path_template_rewrite(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path_template_rewrite.setter
    def path_template_rewrite(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteMethodsArgsDict(TypedDict):
    allowed_methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteMethodsArgs:
    def __init__(
        __self__,
        *,
        allowed_methods: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_methods.setter
    def allowed_methods(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class EdgeCacheServiceRoutingPathMatcherRouteRuleUrlRedirectArgsDict(TypedDict):
    host_redirect: NotRequired[pulumi.Input[_builtins.str]]
    https_redirect: NotRequired[pulumi.Input[_builtins.bool]]
    path_redirect: NotRequired[pulumi.Input[_builtins.str]]
    prefix_redirect: NotRequired[pulumi.Input[_builtins.str]]
    redirect_response_code: NotRequired[pulumi.Input[_builtins.str]]
    strip_query: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleUrlRedirectArgs:
    def __init__(
        __self__,
        *,
        host_redirect: Optional[pulumi.Input[_builtins.str]] = ...,
        https_redirect: Optional[pulumi.Input[_builtins.bool]] = ...,
        path_redirect: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix_redirect: Optional[pulumi.Input[_builtins.str]] = ...,
        redirect_response_code: Optional[pulumi.Input[_builtins.str]] = ...,
        strip_query: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostRedirect")
    def host_redirect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_redirect.setter
    def host_redirect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpsRedirect")
    def https_redirect(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @https_redirect.setter
    def https_redirect(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pathRedirect")
    def path_redirect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path_redirect.setter
    def path_redirect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixRedirect")
    def prefix_redirect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_redirect.setter
    def prefix_redirect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="redirectResponseCode")
    def redirect_response_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redirect_response_code.setter
    def redirect_response_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stripQuery")
    def strip_query(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @strip_query.setter
    def strip_query(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EndpointPolicyEndpointMatcherArgsDict(TypedDict):
    metadata_label_matcher: pulumi.Input[
        EndpointPolicyEndpointMatcherMetadataLabelMatcherArgsDict
    ]
    ...

@pulumi.input_type
class EndpointPolicyEndpointMatcherArgs:
    def __init__(
        __self__,
        *,
        metadata_label_matcher: pulumi.Input[
            EndpointPolicyEndpointMatcherMetadataLabelMatcherArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataLabelMatcher")
    def metadata_label_matcher(
        self,
    ) -> pulumi.Input[EndpointPolicyEndpointMatcherMetadataLabelMatcherArgs]: ...
    @metadata_label_matcher.setter
    def metadata_label_matcher(
        self, value: pulumi.Input[EndpointPolicyEndpointMatcherMetadataLabelMatcherArgs]
    ): ...

class EndpointPolicyEndpointMatcherMetadataLabelMatcherArgsDict(TypedDict):
    metadata_label_match_criteria: pulumi.Input[_builtins.str]
    metadata_labels: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EndpointPolicyEndpointMatcherMetadataLabelMatcherMetadataLabelArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class EndpointPolicyEndpointMatcherMetadataLabelMatcherArgs:
    def __init__(
        __self__,
        *,
        metadata_label_match_criteria: pulumi.Input[_builtins.str],
        metadata_labels: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EndpointPolicyEndpointMatcherMetadataLabelMatcherMetadataLabelArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataLabelMatchCriteria")
    def metadata_label_match_criteria(self) -> pulumi.Input[_builtins.str]: ...
    @metadata_label_match_criteria.setter
    def metadata_label_match_criteria(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metadataLabels")
    def metadata_labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    EndpointPolicyEndpointMatcherMetadataLabelMatcherMetadataLabelArgs
                ]
            ]
        ]
    ]: ...
    @metadata_labels.setter
    def metadata_labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        EndpointPolicyEndpointMatcherMetadataLabelMatcherMetadataLabelArgs
                    ]
                ]
            ]
        ],
    ): ...

class EndpointPolicyEndpointMatcherMetadataLabelMatcherMetadataLabelArgsDict(TypedDict):
    label_name: pulumi.Input[_builtins.str]
    label_value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class EndpointPolicyEndpointMatcherMetadataLabelMatcherMetadataLabelArgs:
    def __init__(
        __self__,
        *,
        label_name: pulumi.Input[_builtins.str],
        label_value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labelName")
    def label_name(self) -> pulumi.Input[_builtins.str]: ...
    @label_name.setter
    def label_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="labelValue")
    def label_value(self) -> pulumi.Input[_builtins.str]: ...
    @label_value.setter
    def label_value(self, value: pulumi.Input[_builtins.str]): ...

class EndpointPolicyTrafficPortSelectorArgsDict(TypedDict):
    ports: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class EndpointPolicyTrafficPortSelectorArgs:
    def __init__(
        __self__, *, ports: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @ports.setter
    def ports(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class GrpcRouteRuleArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[GrpcRouteRuleActionArgsDict]]
    matches: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[GrpcRouteRuleMatchArgsDict]]]
    ]
    ...

@pulumi.input_type
class GrpcRouteRuleArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[GrpcRouteRuleActionArgs]] = ...,
        matches: Optional[
            pulumi.Input[Sequence[pulumi.Input[GrpcRouteRuleMatchArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[GrpcRouteRuleActionArgs]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[GrpcRouteRuleActionArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[GrpcRouteRuleMatchArgs]]]]: ...
    @matches.setter
    def matches(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[GrpcRouteRuleMatchArgs]]]],
    ): ...

class GrpcRouteRuleActionArgsDict(TypedDict):
    destinations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[GrpcRouteRuleActionDestinationArgsDict]]]
    ]
    fault_injection_policy: NotRequired[
        pulumi.Input[GrpcRouteRuleActionFaultInjectionPolicyArgsDict]
    ]
    retry_policy: NotRequired[pulumi.Input[GrpcRouteRuleActionRetryPolicyArgsDict]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GrpcRouteRuleActionArgs:
    def __init__(
        __self__,
        *,
        destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[GrpcRouteRuleActionDestinationArgs]]]
        ] = ...,
        fault_injection_policy: Optional[
            pulumi.Input[GrpcRouteRuleActionFaultInjectionPolicyArgs]
        ] = ...,
        retry_policy: Optional[pulumi.Input[GrpcRouteRuleActionRetryPolicyArgs]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GrpcRouteRuleActionDestinationArgs]]]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[GrpcRouteRuleActionDestinationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="faultInjectionPolicy")
    def fault_injection_policy(
        self,
    ) -> Optional[pulumi.Input[GrpcRouteRuleActionFaultInjectionPolicyArgs]]: ...
    @fault_injection_policy.setter
    def fault_injection_policy(
        self, value: Optional[pulumi.Input[GrpcRouteRuleActionFaultInjectionPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(
        self,
    ) -> Optional[pulumi.Input[GrpcRouteRuleActionRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(
        self, value: Optional[pulumi.Input[GrpcRouteRuleActionRetryPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GrpcRouteRuleActionDestinationArgsDict(TypedDict):
    service_name: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class GrpcRouteRuleActionDestinationArgs:
    def __init__(
        __self__,
        *,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GrpcRouteRuleActionFaultInjectionPolicyArgsDict(TypedDict):
    abort: NotRequired[
        pulumi.Input[GrpcRouteRuleActionFaultInjectionPolicyAbortArgsDict]
    ]
    delay: NotRequired[
        pulumi.Input[GrpcRouteRuleActionFaultInjectionPolicyDelayArgsDict]
    ]
    ...

@pulumi.input_type
class GrpcRouteRuleActionFaultInjectionPolicyArgs:
    def __init__(
        __self__,
        *,
        abort: Optional[
            pulumi.Input[GrpcRouteRuleActionFaultInjectionPolicyAbortArgs]
        ] = ...,
        delay: Optional[
            pulumi.Input[GrpcRouteRuleActionFaultInjectionPolicyDelayArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def abort(
        self,
    ) -> Optional[pulumi.Input[GrpcRouteRuleActionFaultInjectionPolicyAbortArgs]]: ...
    @abort.setter
    def abort(
        self,
        value: Optional[pulumi.Input[GrpcRouteRuleActionFaultInjectionPolicyAbortArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def delay(
        self,
    ) -> Optional[pulumi.Input[GrpcRouteRuleActionFaultInjectionPolicyDelayArgs]]: ...
    @delay.setter
    def delay(
        self,
        value: Optional[pulumi.Input[GrpcRouteRuleActionFaultInjectionPolicyDelayArgs]],
    ): ...

class GrpcRouteRuleActionFaultInjectionPolicyAbortArgsDict(TypedDict):
    http_status: NotRequired[pulumi.Input[_builtins.int]]
    percentage: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class GrpcRouteRuleActionFaultInjectionPolicyAbortArgs:
    def __init__(
        __self__,
        *,
        http_status: Optional[pulumi.Input[_builtins.int]] = ...,
        percentage: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpStatus")
    def http_status(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @http_status.setter
    def http_status(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percentage.setter
    def percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GrpcRouteRuleActionFaultInjectionPolicyDelayArgsDict(TypedDict):
    fixed_delay: NotRequired[pulumi.Input[_builtins.str]]
    percentage: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class GrpcRouteRuleActionFaultInjectionPolicyDelayArgs:
    def __init__(
        __self__,
        *,
        fixed_delay: Optional[pulumi.Input[_builtins.str]] = ...,
        percentage: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedDelay")
    def fixed_delay(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fixed_delay.setter
    def fixed_delay(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percentage.setter
    def percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GrpcRouteRuleActionRetryPolicyArgsDict(TypedDict):
    num_retries: NotRequired[pulumi.Input[_builtins.int]]
    retry_conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class GrpcRouteRuleActionRetryPolicyArgs:
    def __init__(
        __self__,
        *,
        num_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        retry_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_retries.setter
    def num_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="retryConditions")
    def retry_conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @retry_conditions.setter
    def retry_conditions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GrpcRouteRuleMatchArgsDict(TypedDict):
    headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[GrpcRouteRuleMatchHeaderArgsDict]]]
    ]
    method: NotRequired[pulumi.Input[GrpcRouteRuleMatchMethodArgsDict]]
    ...

@pulumi.input_type
class GrpcRouteRuleMatchArgs:
    def __init__(
        __self__,
        *,
        headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[GrpcRouteRuleMatchHeaderArgs]]]
        ] = ...,
        method: Optional[pulumi.Input[GrpcRouteRuleMatchMethodArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GrpcRouteRuleMatchHeaderArgs]]]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[GrpcRouteRuleMatchHeaderArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[GrpcRouteRuleMatchMethodArgs]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[GrpcRouteRuleMatchMethodArgs]]): ...

class GrpcRouteRuleMatchHeaderArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GrpcRouteRuleMatchHeaderArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        type: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GrpcRouteRuleMatchMethodArgsDict(TypedDict):
    grpc_method: pulumi.Input[_builtins.str]
    grpc_service: pulumi.Input[_builtins.str]
    case_sensitive: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class GrpcRouteRuleMatchMethodArgs:
    def __init__(
        __self__,
        *,
        grpc_method: pulumi.Input[_builtins.str],
        grpc_service: pulumi.Input[_builtins.str],
        case_sensitive: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="grpcMethod")
    def grpc_method(self) -> pulumi.Input[_builtins.str]: ...
    @grpc_method.setter
    def grpc_method(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="grpcService")
    def grpc_service(self) -> pulumi.Input[_builtins.str]: ...
    @grpc_service.setter
    def grpc_service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="caseSensitive")
    def case_sensitive(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @case_sensitive.setter
    def case_sensitive(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class HttpRouteRuleArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[HttpRouteRuleActionArgsDict]]
    matches: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleMatchArgsDict]]]
    ]
    ...

@pulumi.input_type
class HttpRouteRuleArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[HttpRouteRuleActionArgs]] = ...,
        matches: Optional[
            pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleMatchArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[HttpRouteRuleActionArgs]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[HttpRouteRuleActionArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleMatchArgs]]]]: ...
    @matches.setter
    def matches(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleMatchArgs]]]],
    ): ...

class HttpRouteRuleActionArgsDict(TypedDict):
    cors_policy: NotRequired[pulumi.Input[HttpRouteRuleActionCorsPolicyArgsDict]]
    destinations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleActionDestinationArgsDict]]]
    ]
    fault_injection_policy: NotRequired[
        pulumi.Input[HttpRouteRuleActionFaultInjectionPolicyArgsDict]
    ]
    redirect: NotRequired[pulumi.Input[HttpRouteRuleActionRedirectArgsDict]]
    request_header_modifier: NotRequired[
        pulumi.Input[HttpRouteRuleActionRequestHeaderModifierArgsDict]
    ]
    request_mirror_policy: NotRequired[
        pulumi.Input[HttpRouteRuleActionRequestMirrorPolicyArgsDict]
    ]
    response_header_modifier: NotRequired[
        pulumi.Input[HttpRouteRuleActionResponseHeaderModifierArgsDict]
    ]
    retry_policy: NotRequired[pulumi.Input[HttpRouteRuleActionRetryPolicyArgsDict]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    url_rewrite: NotRequired[pulumi.Input[HttpRouteRuleActionUrlRewriteArgsDict]]
    ...

@pulumi.input_type
class HttpRouteRuleActionArgs:
    def __init__(
        __self__,
        *,
        cors_policy: Optional[pulumi.Input[HttpRouteRuleActionCorsPolicyArgs]] = ...,
        destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleActionDestinationArgs]]]
        ] = ...,
        fault_injection_policy: Optional[
            pulumi.Input[HttpRouteRuleActionFaultInjectionPolicyArgs]
        ] = ...,
        redirect: Optional[pulumi.Input[HttpRouteRuleActionRedirectArgs]] = ...,
        request_header_modifier: Optional[
            pulumi.Input[HttpRouteRuleActionRequestHeaderModifierArgs]
        ] = ...,
        request_mirror_policy: Optional[
            pulumi.Input[HttpRouteRuleActionRequestMirrorPolicyArgs]
        ] = ...,
        response_header_modifier: Optional[
            pulumi.Input[HttpRouteRuleActionResponseHeaderModifierArgs]
        ] = ...,
        retry_policy: Optional[pulumi.Input[HttpRouteRuleActionRetryPolicyArgs]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        url_rewrite: Optional[pulumi.Input[HttpRouteRuleActionUrlRewriteArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="corsPolicy")
    def cors_policy(
        self,
    ) -> Optional[pulumi.Input[HttpRouteRuleActionCorsPolicyArgs]]: ...
    @cors_policy.setter
    def cors_policy(
        self, value: Optional[pulumi.Input[HttpRouteRuleActionCorsPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleActionDestinationArgs]]]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleActionDestinationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="faultInjectionPolicy")
    def fault_injection_policy(
        self,
    ) -> Optional[pulumi.Input[HttpRouteRuleActionFaultInjectionPolicyArgs]]: ...
    @fault_injection_policy.setter
    def fault_injection_policy(
        self, value: Optional[pulumi.Input[HttpRouteRuleActionFaultInjectionPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def redirect(self) -> Optional[pulumi.Input[HttpRouteRuleActionRedirectArgs]]: ...
    @redirect.setter
    def redirect(
        self, value: Optional[pulumi.Input[HttpRouteRuleActionRedirectArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderModifier")
    def request_header_modifier(
        self,
    ) -> Optional[pulumi.Input[HttpRouteRuleActionRequestHeaderModifierArgs]]: ...
    @request_header_modifier.setter
    def request_header_modifier(
        self,
        value: Optional[pulumi.Input[HttpRouteRuleActionRequestHeaderModifierArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requestMirrorPolicy")
    def request_mirror_policy(
        self,
    ) -> Optional[pulumi.Input[HttpRouteRuleActionRequestMirrorPolicyArgs]]: ...
    @request_mirror_policy.setter
    def request_mirror_policy(
        self, value: Optional[pulumi.Input[HttpRouteRuleActionRequestMirrorPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="responseHeaderModifier")
    def response_header_modifier(
        self,
    ) -> Optional[pulumi.Input[HttpRouteRuleActionResponseHeaderModifierArgs]]: ...
    @response_header_modifier.setter
    def response_header_modifier(
        self,
        value: Optional[pulumi.Input[HttpRouteRuleActionResponseHeaderModifierArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(
        self,
    ) -> Optional[pulumi.Input[HttpRouteRuleActionRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(
        self, value: Optional[pulumi.Input[HttpRouteRuleActionRetryPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="urlRewrite")
    def url_rewrite(
        self,
    ) -> Optional[pulumi.Input[HttpRouteRuleActionUrlRewriteArgs]]: ...
    @url_rewrite.setter
    def url_rewrite(
        self, value: Optional[pulumi.Input[HttpRouteRuleActionUrlRewriteArgs]]
    ): ...

class HttpRouteRuleActionCorsPolicyArgsDict(TypedDict):
    allow_credentials: NotRequired[pulumi.Input[_builtins.bool]]
    allow_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allow_methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allow_origin_regexes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    allow_origins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    expose_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_age: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HttpRouteRuleActionCorsPolicyArgs:
    def __init__(
        __self__,
        *,
        allow_credentials: Optional[pulumi.Input[_builtins.bool]] = ...,
        allow_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allow_methods: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allow_origin_regexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allow_origins: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        expose_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        max_age: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_credentials.setter
    def allow_credentials(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowHeaders")
    def allow_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allow_headers.setter
    def allow_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowMethods")
    def allow_methods(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allow_methods.setter
    def allow_methods(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowOriginRegexes")
    def allow_origin_regexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allow_origin_regexes.setter
    def allow_origin_regexes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowOrigins")
    def allow_origins(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allow_origins.setter
    def allow_origins(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @expose_headers.setter
    def expose_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_age.setter
    def max_age(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HttpRouteRuleActionDestinationArgsDict(TypedDict):
    service_name: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class HttpRouteRuleActionDestinationArgs:
    def __init__(
        __self__,
        *,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class HttpRouteRuleActionFaultInjectionPolicyArgsDict(TypedDict):
    abort: NotRequired[
        pulumi.Input[HttpRouteRuleActionFaultInjectionPolicyAbortArgsDict]
    ]
    delay: NotRequired[
        pulumi.Input[HttpRouteRuleActionFaultInjectionPolicyDelayArgsDict]
    ]
    ...

@pulumi.input_type
class HttpRouteRuleActionFaultInjectionPolicyArgs:
    def __init__(
        __self__,
        *,
        abort: Optional[
            pulumi.Input[HttpRouteRuleActionFaultInjectionPolicyAbortArgs]
        ] = ...,
        delay: Optional[
            pulumi.Input[HttpRouteRuleActionFaultInjectionPolicyDelayArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def abort(
        self,
    ) -> Optional[pulumi.Input[HttpRouteRuleActionFaultInjectionPolicyAbortArgs]]: ...
    @abort.setter
    def abort(
        self,
        value: Optional[pulumi.Input[HttpRouteRuleActionFaultInjectionPolicyAbortArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def delay(
        self,
    ) -> Optional[pulumi.Input[HttpRouteRuleActionFaultInjectionPolicyDelayArgs]]: ...
    @delay.setter
    def delay(
        self,
        value: Optional[pulumi.Input[HttpRouteRuleActionFaultInjectionPolicyDelayArgs]],
    ): ...

class HttpRouteRuleActionFaultInjectionPolicyAbortArgsDict(TypedDict):
    http_status: NotRequired[pulumi.Input[_builtins.int]]
    percentage: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class HttpRouteRuleActionFaultInjectionPolicyAbortArgs:
    def __init__(
        __self__,
        *,
        http_status: Optional[pulumi.Input[_builtins.int]] = ...,
        percentage: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpStatus")
    def http_status(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @http_status.setter
    def http_status(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percentage.setter
    def percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class HttpRouteRuleActionFaultInjectionPolicyDelayArgsDict(TypedDict):
    fixed_delay: NotRequired[pulumi.Input[_builtins.str]]
    percentage: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class HttpRouteRuleActionFaultInjectionPolicyDelayArgs:
    def __init__(
        __self__,
        *,
        fixed_delay: Optional[pulumi.Input[_builtins.str]] = ...,
        percentage: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedDelay")
    def fixed_delay(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fixed_delay.setter
    def fixed_delay(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percentage.setter
    def percentage(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class HttpRouteRuleActionRedirectArgsDict(TypedDict):
    host_redirect: NotRequired[pulumi.Input[_builtins.str]]
    https_redirect: NotRequired[pulumi.Input[_builtins.bool]]
    path_redirect: NotRequired[pulumi.Input[_builtins.str]]
    port_redirect: NotRequired[pulumi.Input[_builtins.int]]
    prefix_rewrite: NotRequired[pulumi.Input[_builtins.str]]
    response_code: NotRequired[pulumi.Input[_builtins.str]]
    strip_query: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class HttpRouteRuleActionRedirectArgs:
    def __init__(
        __self__,
        *,
        host_redirect: Optional[pulumi.Input[_builtins.str]] = ...,
        https_redirect: Optional[pulumi.Input[_builtins.bool]] = ...,
        path_redirect: Optional[pulumi.Input[_builtins.str]] = ...,
        port_redirect: Optional[pulumi.Input[_builtins.int]] = ...,
        prefix_rewrite: Optional[pulumi.Input[_builtins.str]] = ...,
        response_code: Optional[pulumi.Input[_builtins.str]] = ...,
        strip_query: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostRedirect")
    def host_redirect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_redirect.setter
    def host_redirect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpsRedirect")
    def https_redirect(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @https_redirect.setter
    def https_redirect(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pathRedirect")
    def path_redirect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path_redirect.setter
    def path_redirect(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="portRedirect")
    def port_redirect(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port_redirect.setter
    def port_redirect(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixRewrite")
    def prefix_rewrite(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_rewrite.setter
    def prefix_rewrite(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @response_code.setter
    def response_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stripQuery")
    def strip_query(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @strip_query.setter
    def strip_query(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class HttpRouteRuleActionRequestHeaderModifierArgsDict(TypedDict):
    add: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    removes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    set: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class HttpRouteRuleActionRequestHeaderModifierArgs:
    def __init__(
        __self__,
        *,
        add: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        removes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        set: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def add(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @add.setter
    def add(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def removes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @removes.setter
    def removes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def set(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @set.setter
    def set(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class HttpRouteRuleActionRequestMirrorPolicyArgsDict(TypedDict):
    destination: NotRequired[
        pulumi.Input[HttpRouteRuleActionRequestMirrorPolicyDestinationArgsDict]
    ]
    ...

@pulumi.input_type
class HttpRouteRuleActionRequestMirrorPolicyArgs:
    def __init__(
        __self__,
        *,
        destination: Optional[
            pulumi.Input[HttpRouteRuleActionRequestMirrorPolicyDestinationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> Optional[
        pulumi.Input[HttpRouteRuleActionRequestMirrorPolicyDestinationArgs]
    ]: ...
    @destination.setter
    def destination(
        self,
        value: Optional[
            pulumi.Input[HttpRouteRuleActionRequestMirrorPolicyDestinationArgs]
        ],
    ): ...

class HttpRouteRuleActionRequestMirrorPolicyDestinationArgsDict(TypedDict):
    service_name: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class HttpRouteRuleActionRequestMirrorPolicyDestinationArgs:
    def __init__(
        __self__,
        *,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class HttpRouteRuleActionResponseHeaderModifierArgsDict(TypedDict):
    add: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    removes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    set: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class HttpRouteRuleActionResponseHeaderModifierArgs:
    def __init__(
        __self__,
        *,
        add: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        removes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        set: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def add(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @add.setter
    def add(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def removes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @removes.setter
    def removes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def set(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @set.setter
    def set(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class HttpRouteRuleActionRetryPolicyArgsDict(TypedDict):
    num_retries: NotRequired[pulumi.Input[_builtins.int]]
    per_try_timeout: NotRequired[pulumi.Input[_builtins.str]]
    retry_conditions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class HttpRouteRuleActionRetryPolicyArgs:
    def __init__(
        __self__,
        *,
        num_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        per_try_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_retries.setter
    def num_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="perTryTimeout")
    def per_try_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @per_try_timeout.setter
    def per_try_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryConditions")
    def retry_conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @retry_conditions.setter
    def retry_conditions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class HttpRouteRuleActionUrlRewriteArgsDict(TypedDict):
    host_rewrite: NotRequired[pulumi.Input[_builtins.str]]
    path_prefix_rewrite: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HttpRouteRuleActionUrlRewriteArgs:
    def __init__(
        __self__,
        *,
        host_rewrite: Optional[pulumi.Input[_builtins.str]] = ...,
        path_prefix_rewrite: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostRewrite")
    def host_rewrite(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_rewrite.setter
    def host_rewrite(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pathPrefixRewrite")
    def path_prefix_rewrite(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path_prefix_rewrite.setter
    def path_prefix_rewrite(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HttpRouteRuleMatchArgsDict(TypedDict):
    full_path_match: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleMatchHeaderArgsDict]]]
    ]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    prefix_match: NotRequired[pulumi.Input[_builtins.str]]
    query_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleMatchQueryParameterArgsDict]]]
    ]
    regex_match: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HttpRouteRuleMatchArgs:
    def __init__(
        __self__,
        *,
        full_path_match: Optional[pulumi.Input[_builtins.str]] = ...,
        headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleMatchHeaderArgs]]]
        ] = ...,
        ignore_case: Optional[pulumi.Input[_builtins.bool]] = ...,
        prefix_match: Optional[pulumi.Input[_builtins.str]] = ...,
        query_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleMatchQueryParameterArgs]]]
        ] = ...,
        regex_match: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fullPathMatch")
    def full_path_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @full_path_match.setter
    def full_path_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleMatchHeaderArgs]]]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleMatchHeaderArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_match.setter
    def prefix_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleMatchQueryParameterArgs]]]
    ]: ...
    @query_parameters.setter
    def query_parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleMatchQueryParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="regexMatch")
    def regex_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex_match.setter
    def regex_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HttpRouteRuleMatchHeaderArgsDict(TypedDict):
    exact_match: NotRequired[pulumi.Input[_builtins.str]]
    header: NotRequired[pulumi.Input[_builtins.str]]
    invert_match: NotRequired[pulumi.Input[_builtins.bool]]
    prefix_match: NotRequired[pulumi.Input[_builtins.str]]
    present_match: NotRequired[pulumi.Input[_builtins.bool]]
    range_match: NotRequired[pulumi.Input[HttpRouteRuleMatchHeaderRangeMatchArgsDict]]
    regex_match: NotRequired[pulumi.Input[_builtins.str]]
    suffix_match: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HttpRouteRuleMatchHeaderArgs:
    def __init__(
        __self__,
        *,
        exact_match: Optional[pulumi.Input[_builtins.str]] = ...,
        header: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        prefix_match: Optional[pulumi.Input[_builtins.str]] = ...,
        present_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        range_match: Optional[
            pulumi.Input[HttpRouteRuleMatchHeaderRangeMatchArgs]
        ] = ...,
        regex_match: Optional[pulumi.Input[_builtins.str]] = ...,
        suffix_match: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact_match.setter
    def exact_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @header.setter
    def header(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertMatch")
    def invert_match(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_match.setter
    def invert_match(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_match.setter
    def prefix_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="presentMatch")
    def present_match(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @present_match.setter
    def present_match(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="rangeMatch")
    def range_match(
        self,
    ) -> Optional[pulumi.Input[HttpRouteRuleMatchHeaderRangeMatchArgs]]: ...
    @range_match.setter
    def range_match(
        self, value: Optional[pulumi.Input[HttpRouteRuleMatchHeaderRangeMatchArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="regexMatch")
    def regex_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex_match.setter
    def regex_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="suffixMatch")
    def suffix_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suffix_match.setter
    def suffix_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HttpRouteRuleMatchHeaderRangeMatchArgsDict(TypedDict):
    end: pulumi.Input[_builtins.int]
    start: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class HttpRouteRuleMatchHeaderRangeMatchArgs:
    def __init__(
        __self__,
        *,
        end: pulumi.Input[_builtins.int],
        start: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> pulumi.Input[_builtins.int]: ...
    @end.setter
    def end(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> pulumi.Input[_builtins.int]: ...
    @start.setter
    def start(self, value: pulumi.Input[_builtins.int]): ...

class HttpRouteRuleMatchQueryParameterArgsDict(TypedDict):
    exact_match: NotRequired[pulumi.Input[_builtins.str]]
    present_match: NotRequired[pulumi.Input[_builtins.bool]]
    query_parameter: NotRequired[pulumi.Input[_builtins.str]]
    regex_match: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HttpRouteRuleMatchQueryParameterArgs:
    def __init__(
        __self__,
        *,
        exact_match: Optional[pulumi.Input[_builtins.str]] = ...,
        present_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        query_parameter: Optional[pulumi.Input[_builtins.str]] = ...,
        regex_match: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact_match.setter
    def exact_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="presentMatch")
    def present_match(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @present_match.setter
    def present_match(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="queryParameter")
    def query_parameter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_parameter.setter
    def query_parameter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regexMatch")
    def regex_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex_match.setter
    def regex_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LbEdgeExtensionExtensionChainArgsDict(TypedDict):
    extensions: pulumi.Input[
        Sequence[pulumi.Input[LbEdgeExtensionExtensionChainExtensionArgsDict]]
    ]
    match_condition: pulumi.Input[LbEdgeExtensionExtensionChainMatchConditionArgsDict]
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class LbEdgeExtensionExtensionChainArgs:
    def __init__(
        __self__,
        *,
        extensions: pulumi.Input[
            Sequence[pulumi.Input[LbEdgeExtensionExtensionChainExtensionArgs]]
        ],
        match_condition: pulumi.Input[LbEdgeExtensionExtensionChainMatchConditionArgs],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[LbEdgeExtensionExtensionChainExtensionArgs]]
    ]: ...
    @extensions.setter
    def extensions(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[LbEdgeExtensionExtensionChainExtensionArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="matchCondition")
    def match_condition(
        self,
    ) -> pulumi.Input[LbEdgeExtensionExtensionChainMatchConditionArgs]: ...
    @match_condition.setter
    def match_condition(
        self, value: pulumi.Input[LbEdgeExtensionExtensionChainMatchConditionArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class LbEdgeExtensionExtensionChainExtensionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    service: pulumi.Input[_builtins.str]
    fail_open: NotRequired[pulumi.Input[_builtins.bool]]
    forward_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    supported_events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class LbEdgeExtensionExtensionChainExtensionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
        fail_open: Optional[pulumi.Input[_builtins.bool]] = ...,
        forward_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        supported_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_open.setter
    def fail_open(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="forwardHeaders")
    def forward_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @forward_headers.setter
    def forward_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="supportedEvents")
    def supported_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @supported_events.setter
    def supported_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class LbEdgeExtensionExtensionChainMatchConditionArgsDict(TypedDict):
    cel_expression: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class LbEdgeExtensionExtensionChainMatchConditionArgs:
    def __init__(__self__, *, cel_expression: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="celExpression")
    def cel_expression(self) -> pulumi.Input[_builtins.str]: ...
    @cel_expression.setter
    def cel_expression(self, value: pulumi.Input[_builtins.str]): ...

class LbRouteExtensionExtensionChainArgsDict(TypedDict):
    extensions: pulumi.Input[
        Sequence[pulumi.Input[LbRouteExtensionExtensionChainExtensionArgsDict]]
    ]
    match_condition: pulumi.Input[LbRouteExtensionExtensionChainMatchConditionArgsDict]
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class LbRouteExtensionExtensionChainArgs:
    def __init__(
        __self__,
        *,
        extensions: pulumi.Input[
            Sequence[pulumi.Input[LbRouteExtensionExtensionChainExtensionArgs]]
        ],
        match_condition: pulumi.Input[LbRouteExtensionExtensionChainMatchConditionArgs],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[LbRouteExtensionExtensionChainExtensionArgs]]
    ]: ...
    @extensions.setter
    def extensions(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[LbRouteExtensionExtensionChainExtensionArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="matchCondition")
    def match_condition(
        self,
    ) -> pulumi.Input[LbRouteExtensionExtensionChainMatchConditionArgs]: ...
    @match_condition.setter
    def match_condition(
        self, value: pulumi.Input[LbRouteExtensionExtensionChainMatchConditionArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class LbRouteExtensionExtensionChainExtensionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    service: pulumi.Input[_builtins.str]
    authority: NotRequired[pulumi.Input[_builtins.str]]
    fail_open: NotRequired[pulumi.Input[_builtins.bool]]
    forward_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    observability_mode: NotRequired[pulumi.Input[_builtins.bool]]
    request_body_send_mode: NotRequired[pulumi.Input[_builtins.str]]
    supported_events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class LbRouteExtensionExtensionChainExtensionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
        authority: Optional[pulumi.Input[_builtins.str]] = ...,
        fail_open: Optional[pulumi.Input[_builtins.bool]] = ...,
        forward_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        observability_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
        request_body_send_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        supported_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authority.setter
    def authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_open.setter
    def fail_open(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="forwardHeaders")
    def forward_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @forward_headers.setter
    def forward_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="observabilityMode")
    def observability_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @observability_mode.setter
    def observability_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requestBodySendMode")
    def request_body_send_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_body_send_mode.setter
    def request_body_send_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="supportedEvents")
    def supported_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @supported_events.setter
    def supported_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LbRouteExtensionExtensionChainMatchConditionArgsDict(TypedDict):
    cel_expression: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class LbRouteExtensionExtensionChainMatchConditionArgs:
    def __init__(__self__, *, cel_expression: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="celExpression")
    def cel_expression(self) -> pulumi.Input[_builtins.str]: ...
    @cel_expression.setter
    def cel_expression(self, value: pulumi.Input[_builtins.str]): ...

class LbTrafficExtensionExtensionChainArgsDict(TypedDict):
    extensions: pulumi.Input[
        Sequence[pulumi.Input[LbTrafficExtensionExtensionChainExtensionArgsDict]]
    ]
    match_condition: pulumi.Input[
        LbTrafficExtensionExtensionChainMatchConditionArgsDict
    ]
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class LbTrafficExtensionExtensionChainArgs:
    def __init__(
        __self__,
        *,
        extensions: pulumi.Input[
            Sequence[pulumi.Input[LbTrafficExtensionExtensionChainExtensionArgs]]
        ],
        match_condition: pulumi.Input[
            LbTrafficExtensionExtensionChainMatchConditionArgs
        ],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[LbTrafficExtensionExtensionChainExtensionArgs]]
    ]: ...
    @extensions.setter
    def extensions(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[LbTrafficExtensionExtensionChainExtensionArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="matchCondition")
    def match_condition(
        self,
    ) -> pulumi.Input[LbTrafficExtensionExtensionChainMatchConditionArgs]: ...
    @match_condition.setter
    def match_condition(
        self, value: pulumi.Input[LbTrafficExtensionExtensionChainMatchConditionArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class LbTrafficExtensionExtensionChainExtensionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    service: pulumi.Input[_builtins.str]
    authority: NotRequired[pulumi.Input[_builtins.str]]
    fail_open: NotRequired[pulumi.Input[_builtins.bool]]
    forward_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    supported_events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class LbTrafficExtensionExtensionChainExtensionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
        authority: Optional[pulumi.Input[_builtins.str]] = ...,
        fail_open: Optional[pulumi.Input[_builtins.bool]] = ...,
        forward_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        supported_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authority.setter
    def authority(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_open.setter
    def fail_open(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="forwardHeaders")
    def forward_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @forward_headers.setter
    def forward_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="supportedEvents")
    def supported_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @supported_events.setter
    def supported_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LbTrafficExtensionExtensionChainMatchConditionArgsDict(TypedDict):
    cel_expression: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class LbTrafficExtensionExtensionChainMatchConditionArgs:
    def __init__(__self__, *, cel_expression: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="celExpression")
    def cel_expression(self) -> pulumi.Input[_builtins.str]: ...
    @cel_expression.setter
    def cel_expression(self, value: pulumi.Input[_builtins.str]): ...

class MulticastConsumerAssociationStateArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MulticastConsumerAssociationStateArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MulticastDomainActivationStateArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MulticastDomainActivationStateArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MulticastDomainActivationTrafficSpecArgsDict(TypedDict):
    aggr_egress_pps: NotRequired[pulumi.Input[_builtins.str]]
    aggr_ingress_pps: NotRequired[pulumi.Input[_builtins.str]]
    avg_packet_size: NotRequired[pulumi.Input[_builtins.int]]
    max_per_group_ingress_pps: NotRequired[pulumi.Input[_builtins.str]]
    max_per_group_subscribers: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MulticastDomainActivationTrafficSpecArgs:
    def __init__(
        __self__,
        *,
        aggr_egress_pps: Optional[pulumi.Input[_builtins.str]] = ...,
        aggr_ingress_pps: Optional[pulumi.Input[_builtins.str]] = ...,
        avg_packet_size: Optional[pulumi.Input[_builtins.int]] = ...,
        max_per_group_ingress_pps: Optional[pulumi.Input[_builtins.str]] = ...,
        max_per_group_subscribers: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggrEgressPps")
    def aggr_egress_pps(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aggr_egress_pps.setter
    def aggr_egress_pps(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="aggrIngressPps")
    def aggr_ingress_pps(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aggr_ingress_pps.setter
    def aggr_ingress_pps(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="avgPacketSize")
    def avg_packet_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @avg_packet_size.setter
    def avg_packet_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxPerGroupIngressPps")
    def max_per_group_ingress_pps(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_per_group_ingress_pps.setter
    def max_per_group_ingress_pps(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxPerGroupSubscribers")
    def max_per_group_subscribers(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_per_group_subscribers.setter
    def max_per_group_subscribers(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class MulticastDomainConnectionConfigArgsDict(TypedDict):
    connection_type: pulumi.Input[_builtins.str]
    ncc_hub: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MulticastDomainConnectionConfigArgs:
    def __init__(
        __self__,
        *,
        connection_type: pulumi.Input[_builtins.str],
        ncc_hub: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> pulumi.Input[_builtins.str]: ...
    @connection_type.setter
    def connection_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nccHub")
    def ncc_hub(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ncc_hub.setter
    def ncc_hub(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MulticastDomainGroupStateArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MulticastDomainGroupStateArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MulticastDomainStateArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MulticastDomainStateArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MulticastDomainUllMulticastDomainArgsDict(TypedDict):
    preconfigured_ull_domain: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MulticastDomainUllMulticastDomainArgs:
    def __init__(
        __self__,
        *,
        preconfigured_ull_domain: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preconfiguredUllDomain")
    def preconfigured_ull_domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preconfigured_ull_domain.setter
    def preconfigured_ull_domain(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class MulticastGroupConsumerActivationLogConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class MulticastGroupConsumerActivationLogConfigArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class MulticastGroupConsumerActivationStateArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MulticastGroupConsumerActivationStateArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MulticastGroupProducerActivationStateArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MulticastGroupProducerActivationStateArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MulticastGroupRangeActivationLogConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class MulticastGroupRangeActivationLogConfigArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class MulticastGroupRangeActivationStateArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MulticastGroupRangeActivationStateArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MulticastGroupRangeLogConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class MulticastGroupRangeLogConfigArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class MulticastGroupRangeStateArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MulticastGroupRangeStateArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MulticastProducerAssociationStateArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MulticastProducerAssociationStateArgs:
    def __init__(
        __self__, *, state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceLbPoliciesAutoCapacityDrainArgsDict(TypedDict):
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class ServiceLbPoliciesAutoCapacityDrainArgs:
    def __init__(
        __self__, *, enable: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServiceLbPoliciesFailoverConfigArgsDict(TypedDict):
    failover_health_threshold: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class ServiceLbPoliciesFailoverConfigArgs:
    def __init__(
        __self__, *, failover_health_threshold: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failoverHealthThreshold")
    def failover_health_threshold(self) -> pulumi.Input[_builtins.int]: ...
    @failover_health_threshold.setter
    def failover_health_threshold(self, value: pulumi.Input[_builtins.int]): ...

class ServiceLbPoliciesIsolationConfigArgsDict(TypedDict):
    isolation_granularity: NotRequired[pulumi.Input[_builtins.str]]
    isolation_mode: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServiceLbPoliciesIsolationConfigArgs:
    def __init__(
        __self__,
        *,
        isolation_granularity: Optional[pulumi.Input[_builtins.str]] = ...,
        isolation_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isolationGranularity")
    def isolation_granularity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @isolation_granularity.setter
    def isolation_granularity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isolationMode")
    def isolation_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @isolation_mode.setter
    def isolation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TcpRouteRuleArgsDict(TypedDict):
    action: pulumi.Input[TcpRouteRuleActionArgsDict]
    matches: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TcpRouteRuleMatchArgsDict]]]
    ]
    ...

@pulumi.input_type
class TcpRouteRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[TcpRouteRuleActionArgs],
        matches: Optional[
            pulumi.Input[Sequence[pulumi.Input[TcpRouteRuleMatchArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[TcpRouteRuleActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[TcpRouteRuleActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TcpRouteRuleMatchArgs]]]]: ...
    @matches.setter
    def matches(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TcpRouteRuleMatchArgs]]]],
    ): ...

class TcpRouteRuleActionArgsDict(TypedDict):
    destinations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TcpRouteRuleActionDestinationArgsDict]]]
    ]
    idle_timeout: NotRequired[pulumi.Input[_builtins.str]]
    original_destination: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class TcpRouteRuleActionArgs:
    def __init__(
        __self__,
        *,
        destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[TcpRouteRuleActionDestinationArgs]]]
        ] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        original_destination: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TcpRouteRuleActionDestinationArgs]]]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TcpRouteRuleActionDestinationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idle_timeout.setter
    def idle_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="originalDestination")
    def original_destination(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @original_destination.setter
    def original_destination(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TcpRouteRuleActionDestinationArgsDict(TypedDict):
    service_name: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class TcpRouteRuleActionDestinationArgs:
    def __init__(
        __self__,
        *,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TcpRouteRuleMatchArgsDict(TypedDict):
    address: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TcpRouteRuleMatchArgs:
    def __init__(
        __self__,
        *,
        address: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Input[_builtins.str]: ...
    @address.setter
    def address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.str]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.str]): ...

class TlsRouteRuleArgsDict(TypedDict):
    action: pulumi.Input[TlsRouteRuleActionArgsDict]
    matches: pulumi.Input[Sequence[pulumi.Input[TlsRouteRuleMatchArgsDict]]]
    ...

@pulumi.input_type
class TlsRouteRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[TlsRouteRuleActionArgs],
        matches: pulumi.Input[Sequence[pulumi.Input[TlsRouteRuleMatchArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[TlsRouteRuleActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[TlsRouteRuleActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[TlsRouteRuleMatchArgs]]]: ...
    @matches.setter
    def matches(
        self, value: pulumi.Input[Sequence[pulumi.Input[TlsRouteRuleMatchArgs]]]
    ): ...

class TlsRouteRuleActionArgsDict(TypedDict):
    destinations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TlsRouteRuleActionDestinationArgsDict]]]
    ]
    ...

@pulumi.input_type
class TlsRouteRuleActionArgs:
    def __init__(
        __self__,
        *,
        destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[TlsRouteRuleActionDestinationArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TlsRouteRuleActionDestinationArgs]]]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TlsRouteRuleActionDestinationArgs]]]
        ],
    ): ...

class TlsRouteRuleActionDestinationArgsDict(TypedDict):
    service_name: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class TlsRouteRuleActionDestinationArgs:
    def __init__(
        __self__,
        *,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TlsRouteRuleMatchArgsDict(TypedDict):
    alpns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    sni_hosts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class TlsRouteRuleMatchArgs:
    def __init__(
        __self__,
        *,
        alpns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        sni_hosts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alpns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @alpns.setter
    def alpns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sniHosts")
    def sni_hosts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @sni_hosts.setter
    def sni_hosts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class WasmPluginLogConfigArgsDict(TypedDict):
    enable: NotRequired[pulumi.Input[_builtins.bool]]
    min_log_level: NotRequired[pulumi.Input[_builtins.str]]
    sample_rate: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class WasmPluginLogConfigArgs:
    def __init__(
        __self__,
        *,
        enable: Optional[pulumi.Input[_builtins.bool]] = ...,
        min_log_level: Optional[pulumi.Input[_builtins.str]] = ...,
        sample_rate: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable.setter
    def enable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="minLogLevel")
    def min_log_level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_log_level.setter
    def min_log_level(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sampleRate")
    def sample_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @sample_rate.setter
    def sample_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class WasmPluginUsedByArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class WasmPluginUsedByArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WasmPluginVersionArgsDict(TypedDict):
    version_name: pulumi.Input[_builtins.str]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    image_digest: NotRequired[pulumi.Input[_builtins.str]]
    image_uri: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    plugin_config_data: NotRequired[pulumi.Input[_builtins.str]]
    plugin_config_digest: NotRequired[pulumi.Input[_builtins.str]]
    plugin_config_uri: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class WasmPluginVersionArgs:
    def __init__(
        __self__,
        *,
        version_name: pulumi.Input[_builtins.str],
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        image_digest: Optional[pulumi.Input[_builtins.str]] = ...,
        image_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        plugin_config_data: Optional[pulumi.Input[_builtins.str]] = ...,
        plugin_config_digest: Optional[pulumi.Input[_builtins.str]] = ...,
        plugin_config_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> pulumi.Input[_builtins.str]: ...
    @version_name.setter
    def version_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageDigest")
    def image_digest(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_digest.setter
    def image_digest(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_uri.setter
    def image_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pluginConfigData")
    def plugin_config_data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plugin_config_data.setter
    def plugin_config_data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pluginConfigDigest")
    def plugin_config_digest(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plugin_config_digest.setter
    def plugin_config_digest(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pluginConfigUri")
    def plugin_config_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plugin_config_uri.setter
    def plugin_config_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
