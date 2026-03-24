import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AgentGatewayAgentGatewayCard",
    "AgentGatewayGoogleManaged",
    "AgentGatewayNetworkConfig",
    "AgentGatewayNetworkConfigEgress",
    "AgentGatewaySelfManaged",
    "EdgeCacheKeysetPublicKey",
    "EdgeCacheKeysetValidationSharedKey",
    "EdgeCacheOriginAwsV4Authentication",
    "EdgeCacheOriginFlexShielding",
    "EdgeCacheOriginOriginOverrideAction",
    "EdgeCacheOriginOriginOverrideActionHeaderAction",
    ...,
    "EdgeCacheOriginOriginOverrideActionUrlRewrite",
    "EdgeCacheOriginOriginRedirect",
    "EdgeCacheOriginTimeout",
    "EdgeCacheServiceLogConfig",
    "EdgeCacheServiceRouting",
    "EdgeCacheServiceRoutingHostRule",
    "EdgeCacheServiceRoutingPathMatcher",
    "EdgeCacheServiceRoutingPathMatcherRouteRule",
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
    "EndpointPolicyEndpointMatcher",
    "EndpointPolicyEndpointMatcherMetadataLabelMatcher",
    ...,
    "EndpointPolicyTrafficPortSelector",
    "GrpcRouteRule",
    "GrpcRouteRuleAction",
    "GrpcRouteRuleActionDestination",
    "GrpcRouteRuleActionFaultInjectionPolicy",
    "GrpcRouteRuleActionFaultInjectionPolicyAbort",
    "GrpcRouteRuleActionFaultInjectionPolicyDelay",
    "GrpcRouteRuleActionRetryPolicy",
    "GrpcRouteRuleMatch",
    "GrpcRouteRuleMatchHeader",
    "GrpcRouteRuleMatchMethod",
    "HttpRouteRule",
    "HttpRouteRuleAction",
    "HttpRouteRuleActionCorsPolicy",
    "HttpRouteRuleActionDestination",
    "HttpRouteRuleActionFaultInjectionPolicy",
    "HttpRouteRuleActionFaultInjectionPolicyAbort",
    "HttpRouteRuleActionFaultInjectionPolicyDelay",
    "HttpRouteRuleActionRedirect",
    "HttpRouteRuleActionRequestHeaderModifier",
    "HttpRouteRuleActionRequestMirrorPolicy",
    "HttpRouteRuleActionRequestMirrorPolicyDestination",
    "HttpRouteRuleActionResponseHeaderModifier",
    "HttpRouteRuleActionRetryPolicy",
    "HttpRouteRuleActionUrlRewrite",
    "HttpRouteRuleMatch",
    "HttpRouteRuleMatchHeader",
    "HttpRouteRuleMatchHeaderRangeMatch",
    "HttpRouteRuleMatchQueryParameter",
    "LbEdgeExtensionExtensionChain",
    "LbEdgeExtensionExtensionChainExtension",
    "LbEdgeExtensionExtensionChainMatchCondition",
    "LbRouteExtensionExtensionChain",
    "LbRouteExtensionExtensionChainExtension",
    "LbRouteExtensionExtensionChainMatchCondition",
    "LbTrafficExtensionExtensionChain",
    "LbTrafficExtensionExtensionChainExtension",
    "LbTrafficExtensionExtensionChainMatchCondition",
    "MulticastConsumerAssociationState",
    "MulticastDomainActivationState",
    "MulticastDomainActivationTrafficSpec",
    "MulticastDomainConnectionConfig",
    "MulticastDomainGroupState",
    "MulticastDomainState",
    "MulticastDomainUllMulticastDomain",
    "MulticastGroupConsumerActivationLogConfig",
    "MulticastGroupConsumerActivationState",
    "MulticastGroupProducerActivationState",
    "MulticastGroupRangeActivationLogConfig",
    "MulticastGroupRangeActivationState",
    "MulticastGroupRangeLogConfig",
    "MulticastGroupRangeState",
    "MulticastProducerAssociationState",
    "ServiceLbPoliciesAutoCapacityDrain",
    "ServiceLbPoliciesFailoverConfig",
    "ServiceLbPoliciesIsolationConfig",
    "TcpRouteRule",
    "TcpRouteRuleAction",
    "TcpRouteRuleActionDestination",
    "TcpRouteRuleMatch",
    "TlsRouteRule",
    "TlsRouteRuleAction",
    "TlsRouteRuleActionDestination",
    "TlsRouteRuleMatch",
    "WasmPluginLogConfig",
    "WasmPluginUsedBy",
    "WasmPluginVersion",
]

@pulumi.output_type
class AgentGatewayAgentGatewayCard(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mtls_endpoint: Optional[_builtins.str] = ...,
        root_certificates: Optional[Sequence[_builtins.str]] = ...,
        service_extensions_service_account: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mtlsEndpoint")
    def mtls_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rootCertificates")
    def root_certificates(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceExtensionsServiceAccount")
    def service_extensions_service_account(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AgentGatewayGoogleManaged(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, governed_access_path: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="governedAccessPath")
    def governed_access_path(self) -> _builtins.str: ...

@pulumi.output_type
class AgentGatewayNetworkConfig(dict):
    def __init__(
        __self__, *, egress: outputs.AgentGatewayNetworkConfigEgress
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def egress(self) -> outputs.AgentGatewayNetworkConfigEgress: ...

@pulumi.output_type
class AgentGatewayNetworkConfigEgress(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, network_attachment: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> _builtins.str: ...

@pulumi.output_type
class AgentGatewaySelfManaged(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, resource_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> _builtins.str: ...

@pulumi.output_type
class EdgeCacheKeysetPublicKey(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        managed: Optional[_builtins.bool] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def managed(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EdgeCacheKeysetValidationSharedKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class EdgeCacheOriginAwsV4Authentication(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_key_id: _builtins.str,
        origin_region: _builtins.str,
        secret_access_key_version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="originRegion")
    def origin_region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretAccessKeyVersion")
    def secret_access_key_version(self) -> _builtins.str: ...

@pulumi.output_type
class EdgeCacheOriginFlexShielding(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, flex_shielding_regions: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="flexShieldingRegions")
    def flex_shielding_regions(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EdgeCacheOriginOriginOverrideAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        header_action: Optional[
            outputs.EdgeCacheOriginOriginOverrideActionHeaderAction
        ] = ...,
        url_rewrite: Optional[
            outputs.EdgeCacheOriginOriginOverrideActionUrlRewrite
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerAction")
    def header_action(
        self,
    ) -> Optional[outputs.EdgeCacheOriginOriginOverrideActionHeaderAction]: ...
    @_builtins.property
    @pulumi.getter(name="urlRewrite")
    def url_rewrite(
        self,
    ) -> Optional[outputs.EdgeCacheOriginOriginOverrideActionUrlRewrite]: ...

@pulumi.output_type
class EdgeCacheOriginOriginOverrideActionHeaderAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        request_headers_to_adds: Optional[
            Sequence[
                outputs.EdgeCacheOriginOriginOverrideActionHeaderActionRequestHeadersToAdd
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requestHeadersToAdds")
    def request_headers_to_adds(
        self,
    ) -> Optional[
        Sequence[
            outputs.EdgeCacheOriginOriginOverrideActionHeaderActionRequestHeadersToAdd
        ]
    ]: ...

@pulumi.output_type
class EdgeCacheOriginOriginOverrideActionHeaderActionRequestHeadersToAdd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        header_name: _builtins.str,
        header_value: _builtins.str,
        replace: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def replace(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class EdgeCacheOriginOriginOverrideActionUrlRewrite(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, host_rewrite: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostRewrite")
    def host_rewrite(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EdgeCacheOriginOriginRedirect(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, redirect_conditions: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="redirectConditions")
    def redirect_conditions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EdgeCacheOriginTimeout(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connect_timeout: Optional[_builtins.str] = ...,
        max_attempts_timeout: Optional[_builtins.str] = ...,
        read_timeout: Optional[_builtins.str] = ...,
        response_timeout: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectTimeout")
    def connect_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxAttemptsTimeout")
    def max_attempts_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="readTimeout")
    def read_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responseTimeout")
    def response_timeout(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EdgeCacheServiceLogConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable: Optional[_builtins.bool] = ...,
        sample_rate: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="sampleRate")
    def sample_rate(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class EdgeCacheServiceRouting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_rules: Sequence[outputs.EdgeCacheServiceRoutingHostRule],
        path_matchers: Sequence[outputs.EdgeCacheServiceRoutingPathMatcher],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostRules")
    def host_rules(self) -> Sequence[outputs.EdgeCacheServiceRoutingHostRule]: ...
    @_builtins.property
    @pulumi.getter(name="pathMatchers")
    def path_matchers(self) -> Sequence[outputs.EdgeCacheServiceRoutingPathMatcher]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingHostRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hosts: Sequence[_builtins.str],
        path_matcher: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pathMatcher")
    def path_matcher(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcher(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        route_rules: Sequence[outputs.EdgeCacheServiceRoutingPathMatcherRouteRule],
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routeRules")
    def route_rules(
        self,
    ) -> Sequence[outputs.EdgeCacheServiceRoutingPathMatcherRouteRule]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        match_rules: Sequence[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRule
        ],
        priority: _builtins.str,
        description: Optional[_builtins.str] = ...,
        header_action: Optional[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderAction
        ] = ...,
        origin: Optional[_builtins.str] = ...,
        route_action: Optional[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteAction
        ] = ...,
        route_methods: Optional[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteMethods
        ] = ...,
        url_redirect: Optional[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleUrlRedirect
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchRules")
    def match_rules(
        self,
    ) -> Sequence[outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRule]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="headerAction")
    def header_action(
        self,
    ) -> Optional[outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderAction]: ...
    @_builtins.property
    @pulumi.getter
    def origin(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routeAction")
    def route_action(
        self,
    ) -> Optional[outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteAction]: ...
    @_builtins.property
    @pulumi.getter(name="routeMethods")
    def route_methods(
        self,
    ) -> Optional[outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteMethods]: ...
    @_builtins.property
    @pulumi.getter(name="urlRedirect")
    def url_redirect(
        self,
    ) -> Optional[outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleUrlRedirect]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        request_header_to_adds: Optional[
            Sequence[
                outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToAdd
            ]
        ] = ...,
        request_header_to_removes: Optional[
            Sequence[
                outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToRemove
            ]
        ] = ...,
        response_header_to_adds: Optional[
            Sequence[
                outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToAdd
            ]
        ] = ...,
        response_header_to_removes: Optional[
            Sequence[
                outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToRemove
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderToAdds")
    def request_header_to_adds(
        self,
    ) -> Optional[
        Sequence[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToAdd
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderToRemoves")
    def request_header_to_removes(
        self,
    ) -> Optional[
        Sequence[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToRemove
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="responseHeaderToAdds")
    def response_header_to_adds(
        self,
    ) -> Optional[
        Sequence[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToAdd
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="responseHeaderToRemoves")
    def response_header_to_removes(
        self,
    ) -> Optional[
        Sequence[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToRemove
        ]
    ]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToAdd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        header_name: _builtins.str,
        header_value: _builtins.str,
        replace: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def replace(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionRequestHeaderToRemove(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, header_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToAdd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        header_name: _builtins.str,
        header_value: _builtins.str,
        replace: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def replace(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleHeaderActionResponseHeaderToRemove(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, header_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        full_path_match: Optional[_builtins.str] = ...,
        header_matches: Optional[
            Sequence[
                outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleHeaderMatch
            ]
        ] = ...,
        ignore_case: Optional[_builtins.bool] = ...,
        path_template_match: Optional[_builtins.str] = ...,
        prefix_match: Optional[_builtins.str] = ...,
        query_parameter_matches: Optional[
            Sequence[
                outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleQueryParameterMatch
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fullPathMatch")
    def full_path_match(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="headerMatches")
    def header_matches(
        self,
    ) -> Optional[
        Sequence[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleHeaderMatch
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="pathTemplateMatch")
    def path_template_match(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryParameterMatches")
    def query_parameter_matches(
        self,
    ) -> Optional[
        Sequence[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleQueryParameterMatch
        ]
    ]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleHeaderMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        header_name: _builtins.str,
        exact_match: Optional[_builtins.str] = ...,
        invert_match: Optional[_builtins.bool] = ...,
        prefix_match: Optional[_builtins.str] = ...,
        present_match: Optional[_builtins.bool] = ...,
        suffix_match: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="invertMatch")
    def invert_match(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="presentMatch")
    def present_match(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="suffixMatch")
    def suffix_match(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleMatchRuleQueryParameterMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        exact_match: Optional[_builtins.str] = ...,
        present_match: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="presentMatch")
    def present_match(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cdn_policy: Optional[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicy
        ] = ...,
        compression_mode: Optional[_builtins.str] = ...,
        cors_policy: Optional[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCorsPolicy
        ] = ...,
        url_rewrite: Optional[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionUrlRewrite
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicy")
    def cdn_policy(
        self,
    ) -> Optional[
        outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicy
    ]: ...
    @_builtins.property
    @pulumi.getter(name="compressionMode")
    def compression_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="corsPolicy")
    def cors_policy(
        self,
    ) -> Optional[
        outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCorsPolicy
    ]: ...
    @_builtins.property
    @pulumi.getter(name="urlRewrite")
    def url_rewrite(
        self,
    ) -> Optional[
        outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionUrlRewrite
    ]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        add_signatures: Optional[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyAddSignatures
        ] = ...,
        cache_key_policy: Optional[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyCacheKeyPolicy
        ] = ...,
        cache_mode: Optional[_builtins.str] = ...,
        client_ttl: Optional[_builtins.str] = ...,
        default_ttl: Optional[_builtins.str] = ...,
        max_ttl: Optional[_builtins.str] = ...,
        negative_caching: Optional[_builtins.bool] = ...,
        negative_caching_policy: Optional[Mapping[str, _builtins.str]] = ...,
        signed_request_keyset: Optional[_builtins.str] = ...,
        signed_request_maximum_expiration_ttl: Optional[_builtins.str] = ...,
        signed_request_mode: Optional[_builtins.str] = ...,
        signed_token_options: Optional[
            outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicySignedTokenOptions
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addSignatures")
    def add_signatures(
        self,
    ) -> Optional[
        outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyAddSignatures
    ]: ...
    @_builtins.property
    @pulumi.getter(name="cacheKeyPolicy")
    def cache_key_policy(
        self,
    ) -> Optional[
        outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyCacheKeyPolicy
    ]: ...
    @_builtins.property
    @pulumi.getter(name="cacheMode")
    def cache_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientTtl")
    def client_ttl(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxTtl")
    def max_ttl(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="negativeCaching")
    def negative_caching(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="negativeCachingPolicy")
    def negative_caching_policy(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="signedRequestKeyset")
    def signed_request_keyset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="signedRequestMaximumExpirationTtl")
    def signed_request_maximum_expiration_ttl(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="signedRequestMode")
    def signed_request_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="signedTokenOptions")
    def signed_token_options(
        self,
    ) -> Optional[
        outputs.EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicySignedTokenOptions
    ]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyAddSignatures(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: _builtins.str,
        copied_parameters: Optional[Sequence[_builtins.str]] = ...,
        keyset: Optional[_builtins.str] = ...,
        token_query_parameter: Optional[_builtins.str] = ...,
        token_ttl: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="copiedParameters")
    def copied_parameters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def keyset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenQueryParameter")
    def token_query_parameter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenTtl")
    def token_ttl(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicyCacheKeyPolicy(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exclude_host: Optional[_builtins.bool] = ...,
        exclude_query_string: Optional[_builtins.bool] = ...,
        excluded_query_parameters: Optional[Sequence[_builtins.str]] = ...,
        include_protocol: Optional[_builtins.bool] = ...,
        included_cookie_names: Optional[Sequence[_builtins.str]] = ...,
        included_header_names: Optional[Sequence[_builtins.str]] = ...,
        included_query_parameters: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludeHost")
    def exclude_host(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="excludeQueryString")
    def exclude_query_string(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="excludedQueryParameters")
    def excluded_query_parameters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includeProtocol")
    def include_protocol(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="includedCookieNames")
    def included_cookie_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includedHeaderNames")
    def included_header_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="includedQueryParameters")
    def included_query_parameters(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCdnPolicySignedTokenOptions(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_signature_algorithms: Optional[Sequence[_builtins.str]] = ...,
        token_query_parameter: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSignatureAlgorithms")
    def allowed_signature_algorithms(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tokenQueryParameter")
    def token_query_parameter(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionCorsPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_age: _builtins.str,
        allow_credentials: Optional[_builtins.bool] = ...,
        allow_headers: Optional[Sequence[_builtins.str]] = ...,
        allow_methods: Optional[Sequence[_builtins.str]] = ...,
        allow_origins: Optional[Sequence[_builtins.str]] = ...,
        disabled: Optional[_builtins.bool] = ...,
        expose_headers: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowHeaders")
    def allow_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowMethods")
    def allow_methods(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowOrigins")
    def allow_origins(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteActionUrlRewrite(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_rewrite: Optional[_builtins.str] = ...,
        path_prefix_rewrite: Optional[_builtins.str] = ...,
        path_template_rewrite: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostRewrite")
    def host_rewrite(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pathPrefixRewrite")
    def path_prefix_rewrite(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pathTemplateRewrite")
    def path_template_rewrite(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleRouteMethods(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allowed_methods: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EdgeCacheServiceRoutingPathMatcherRouteRuleUrlRedirect(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_redirect: Optional[_builtins.str] = ...,
        https_redirect: Optional[_builtins.bool] = ...,
        path_redirect: Optional[_builtins.str] = ...,
        prefix_redirect: Optional[_builtins.str] = ...,
        redirect_response_code: Optional[_builtins.str] = ...,
        strip_query: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostRedirect")
    def host_redirect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpsRedirect")
    def https_redirect(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="pathRedirect")
    def path_redirect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="prefixRedirect")
    def prefix_redirect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectResponseCode")
    def redirect_response_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stripQuery")
    def strip_query(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class EndpointPolicyEndpointMatcher(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metadata_label_matcher: outputs.EndpointPolicyEndpointMatcherMetadataLabelMatcher,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataLabelMatcher")
    def metadata_label_matcher(
        self,
    ) -> outputs.EndpointPolicyEndpointMatcherMetadataLabelMatcher: ...

@pulumi.output_type
class EndpointPolicyEndpointMatcherMetadataLabelMatcher(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metadata_label_match_criteria: _builtins.str,
        metadata_labels: Optional[
            Sequence[
                outputs.EndpointPolicyEndpointMatcherMetadataLabelMatcherMetadataLabel
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metadataLabelMatchCriteria")
    def metadata_label_match_criteria(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metadataLabels")
    def metadata_labels(
        self,
    ) -> Optional[
        Sequence[outputs.EndpointPolicyEndpointMatcherMetadataLabelMatcherMetadataLabel]
    ]: ...

@pulumi.output_type
class EndpointPolicyEndpointMatcherMetadataLabelMatcherMetadataLabel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, label_name: _builtins.str, label_value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="labelName")
    def label_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="labelValue")
    def label_value(self) -> _builtins.str: ...

@pulumi.output_type
class EndpointPolicyTrafficPortSelector(dict):
    def __init__(__self__, *, ports: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GrpcRouteRule(dict):
    def __init__(
        __self__,
        *,
        action: Optional[outputs.GrpcRouteRuleAction] = ...,
        matches: Optional[Sequence[outputs.GrpcRouteRuleMatch]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[outputs.GrpcRouteRuleAction]: ...
    @_builtins.property
    @pulumi.getter
    def matches(self) -> Optional[Sequence[outputs.GrpcRouteRuleMatch]]: ...

@pulumi.output_type
class GrpcRouteRuleAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destinations: Optional[Sequence[outputs.GrpcRouteRuleActionDestination]] = ...,
        fault_injection_policy: Optional[
            outputs.GrpcRouteRuleActionFaultInjectionPolicy
        ] = ...,
        retry_policy: Optional[outputs.GrpcRouteRuleActionRetryPolicy] = ...,
        timeout: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[Sequence[outputs.GrpcRouteRuleActionDestination]]: ...
    @_builtins.property
    @pulumi.getter(name="faultInjectionPolicy")
    def fault_injection_policy(
        self,
    ) -> Optional[outputs.GrpcRouteRuleActionFaultInjectionPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[outputs.GrpcRouteRuleActionRetryPolicy]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GrpcRouteRuleActionDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_name: Optional[_builtins.str] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GrpcRouteRuleActionFaultInjectionPolicy(dict):
    def __init__(
        __self__,
        *,
        abort: Optional[outputs.GrpcRouteRuleActionFaultInjectionPolicyAbort] = ...,
        delay: Optional[outputs.GrpcRouteRuleActionFaultInjectionPolicyDelay] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def abort(
        self,
    ) -> Optional[outputs.GrpcRouteRuleActionFaultInjectionPolicyAbort]: ...
    @_builtins.property
    @pulumi.getter
    def delay(
        self,
    ) -> Optional[outputs.GrpcRouteRuleActionFaultInjectionPolicyDelay]: ...

@pulumi.output_type
class GrpcRouteRuleActionFaultInjectionPolicyAbort(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        http_status: Optional[_builtins.int] = ...,
        percentage: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpStatus")
    def http_status(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GrpcRouteRuleActionFaultInjectionPolicyDelay(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fixed_delay: Optional[_builtins.str] = ...,
        percentage: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedDelay")
    def fixed_delay(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GrpcRouteRuleActionRetryPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        num_retries: Optional[_builtins.int] = ...,
        retry_conditions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="retryConditions")
    def retry_conditions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GrpcRouteRuleMatch(dict):
    def __init__(
        __self__,
        *,
        headers: Optional[Sequence[outputs.GrpcRouteRuleMatchHeader]] = ...,
        method: Optional[outputs.GrpcRouteRuleMatchMethod] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.GrpcRouteRuleMatchHeader]]: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.GrpcRouteRuleMatchMethod]: ...

@pulumi.output_type
class GrpcRouteRuleMatchHeader(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        value: _builtins.str,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GrpcRouteRuleMatchMethod(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        grpc_method: _builtins.str,
        grpc_service: _builtins.str,
        case_sensitive: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="grpcMethod")
    def grpc_method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="grpcService")
    def grpc_service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="caseSensitive")
    def case_sensitive(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class HttpRouteRule(dict):
    def __init__(
        __self__,
        *,
        action: Optional[outputs.HttpRouteRuleAction] = ...,
        matches: Optional[Sequence[outputs.HttpRouteRuleMatch]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[outputs.HttpRouteRuleAction]: ...
    @_builtins.property
    @pulumi.getter
    def matches(self) -> Optional[Sequence[outputs.HttpRouteRuleMatch]]: ...

@pulumi.output_type
class HttpRouteRuleAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cors_policy: Optional[outputs.HttpRouteRuleActionCorsPolicy] = ...,
        destinations: Optional[Sequence[outputs.HttpRouteRuleActionDestination]] = ...,
        fault_injection_policy: Optional[
            outputs.HttpRouteRuleActionFaultInjectionPolicy
        ] = ...,
        redirect: Optional[outputs.HttpRouteRuleActionRedirect] = ...,
        request_header_modifier: Optional[
            outputs.HttpRouteRuleActionRequestHeaderModifier
        ] = ...,
        request_mirror_policy: Optional[
            outputs.HttpRouteRuleActionRequestMirrorPolicy
        ] = ...,
        response_header_modifier: Optional[
            outputs.HttpRouteRuleActionResponseHeaderModifier
        ] = ...,
        retry_policy: Optional[outputs.HttpRouteRuleActionRetryPolicy] = ...,
        timeout: Optional[_builtins.str] = ...,
        url_rewrite: Optional[outputs.HttpRouteRuleActionUrlRewrite] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="corsPolicy")
    def cors_policy(self) -> Optional[outputs.HttpRouteRuleActionCorsPolicy]: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[Sequence[outputs.HttpRouteRuleActionDestination]]: ...
    @_builtins.property
    @pulumi.getter(name="faultInjectionPolicy")
    def fault_injection_policy(
        self,
    ) -> Optional[outputs.HttpRouteRuleActionFaultInjectionPolicy]: ...
    @_builtins.property
    @pulumi.getter
    def redirect(self) -> Optional[outputs.HttpRouteRuleActionRedirect]: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderModifier")
    def request_header_modifier(
        self,
    ) -> Optional[outputs.HttpRouteRuleActionRequestHeaderModifier]: ...
    @_builtins.property
    @pulumi.getter(name="requestMirrorPolicy")
    def request_mirror_policy(
        self,
    ) -> Optional[outputs.HttpRouteRuleActionRequestMirrorPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="responseHeaderModifier")
    def response_header_modifier(
        self,
    ) -> Optional[outputs.HttpRouteRuleActionResponseHeaderModifier]: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[outputs.HttpRouteRuleActionRetryPolicy]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="urlRewrite")
    def url_rewrite(self) -> Optional[outputs.HttpRouteRuleActionUrlRewrite]: ...

@pulumi.output_type
class HttpRouteRuleActionCorsPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_credentials: Optional[_builtins.bool] = ...,
        allow_headers: Optional[Sequence[_builtins.str]] = ...,
        allow_methods: Optional[Sequence[_builtins.str]] = ...,
        allow_origin_regexes: Optional[Sequence[_builtins.str]] = ...,
        allow_origins: Optional[Sequence[_builtins.str]] = ...,
        disabled: Optional[_builtins.bool] = ...,
        expose_headers: Optional[Sequence[_builtins.str]] = ...,
        max_age: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowHeaders")
    def allow_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowMethods")
    def allow_methods(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowOriginRegexes")
    def allow_origin_regexes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowOrigins")
    def allow_origins(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HttpRouteRuleActionDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_name: Optional[_builtins.str] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class HttpRouteRuleActionFaultInjectionPolicy(dict):
    def __init__(
        __self__,
        *,
        abort: Optional[outputs.HttpRouteRuleActionFaultInjectionPolicyAbort] = ...,
        delay: Optional[outputs.HttpRouteRuleActionFaultInjectionPolicyDelay] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def abort(
        self,
    ) -> Optional[outputs.HttpRouteRuleActionFaultInjectionPolicyAbort]: ...
    @_builtins.property
    @pulumi.getter
    def delay(
        self,
    ) -> Optional[outputs.HttpRouteRuleActionFaultInjectionPolicyDelay]: ...

@pulumi.output_type
class HttpRouteRuleActionFaultInjectionPolicyAbort(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        http_status: Optional[_builtins.int] = ...,
        percentage: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpStatus")
    def http_status(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class HttpRouteRuleActionFaultInjectionPolicyDelay(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        fixed_delay: Optional[_builtins.str] = ...,
        percentage: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedDelay")
    def fixed_delay(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class HttpRouteRuleActionRedirect(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_redirect: Optional[_builtins.str] = ...,
        https_redirect: Optional[_builtins.bool] = ...,
        path_redirect: Optional[_builtins.str] = ...,
        port_redirect: Optional[_builtins.int] = ...,
        prefix_rewrite: Optional[_builtins.str] = ...,
        response_code: Optional[_builtins.str] = ...,
        strip_query: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostRedirect")
    def host_redirect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpsRedirect")
    def https_redirect(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="pathRedirect")
    def path_redirect(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="portRedirect")
    def port_redirect(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="prefixRewrite")
    def prefix_rewrite(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stripQuery")
    def strip_query(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class HttpRouteRuleActionRequestHeaderModifier(dict):
    def __init__(
        __self__,
        *,
        add: Optional[Mapping[str, _builtins.str]] = ...,
        removes: Optional[Sequence[_builtins.str]] = ...,
        set: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def add(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def removes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def set(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class HttpRouteRuleActionRequestMirrorPolicy(dict):
    def __init__(
        __self__,
        *,
        destination: Optional[
            outputs.HttpRouteRuleActionRequestMirrorPolicyDestination
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> Optional[outputs.HttpRouteRuleActionRequestMirrorPolicyDestination]: ...

@pulumi.output_type
class HttpRouteRuleActionRequestMirrorPolicyDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_name: Optional[_builtins.str] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class HttpRouteRuleActionResponseHeaderModifier(dict):
    def __init__(
        __self__,
        *,
        add: Optional[Mapping[str, _builtins.str]] = ...,
        removes: Optional[Sequence[_builtins.str]] = ...,
        set: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def add(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def removes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def set(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class HttpRouteRuleActionRetryPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        num_retries: Optional[_builtins.int] = ...,
        per_try_timeout: Optional[_builtins.str] = ...,
        retry_conditions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="numRetries")
    def num_retries(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="perTryTimeout")
    def per_try_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retryConditions")
    def retry_conditions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class HttpRouteRuleActionUrlRewrite(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_rewrite: Optional[_builtins.str] = ...,
        path_prefix_rewrite: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostRewrite")
    def host_rewrite(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pathPrefixRewrite")
    def path_prefix_rewrite(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HttpRouteRuleMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        full_path_match: Optional[_builtins.str] = ...,
        headers: Optional[Sequence[outputs.HttpRouteRuleMatchHeader]] = ...,
        ignore_case: Optional[_builtins.bool] = ...,
        prefix_match: Optional[_builtins.str] = ...,
        query_parameters: Optional[
            Sequence[outputs.HttpRouteRuleMatchQueryParameter]
        ] = ...,
        regex_match: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fullPathMatch")
    def full_path_match(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.HttpRouteRuleMatchHeader]]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[Sequence[outputs.HttpRouteRuleMatchQueryParameter]]: ...
    @_builtins.property
    @pulumi.getter(name="regexMatch")
    def regex_match(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HttpRouteRuleMatchHeader(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exact_match: Optional[_builtins.str] = ...,
        header: Optional[_builtins.str] = ...,
        invert_match: Optional[_builtins.bool] = ...,
        prefix_match: Optional[_builtins.str] = ...,
        present_match: Optional[_builtins.bool] = ...,
        range_match: Optional[outputs.HttpRouteRuleMatchHeaderRangeMatch] = ...,
        regex_match: Optional[_builtins.str] = ...,
        suffix_match: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="invertMatch")
    def invert_match(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="presentMatch")
    def present_match(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="rangeMatch")
    def range_match(self) -> Optional[outputs.HttpRouteRuleMatchHeaderRangeMatch]: ...
    @_builtins.property
    @pulumi.getter(name="regexMatch")
    def regex_match(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="suffixMatch")
    def suffix_match(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HttpRouteRuleMatchHeaderRangeMatch(dict):
    def __init__(__self__, *, end: _builtins.int, start: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class HttpRouteRuleMatchQueryParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        exact_match: Optional[_builtins.str] = ...,
        present_match: Optional[_builtins.bool] = ...,
        query_parameter: Optional[_builtins.str] = ...,
        regex_match: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="presentMatch")
    def present_match(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="queryParameter")
    def query_parameter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regexMatch")
    def regex_match(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LbEdgeExtensionExtensionChain(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        extensions: Sequence[outputs.LbEdgeExtensionExtensionChainExtension],
        match_condition: outputs.LbEdgeExtensionExtensionChainMatchCondition,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> Sequence[outputs.LbEdgeExtensionExtensionChainExtension]: ...
    @_builtins.property
    @pulumi.getter(name="matchCondition")
    def match_condition(
        self,
    ) -> outputs.LbEdgeExtensionExtensionChainMatchCondition: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class LbEdgeExtensionExtensionChainExtension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        service: _builtins.str,
        fail_open: Optional[_builtins.bool] = ...,
        forward_headers: Optional[Sequence[_builtins.str]] = ...,
        supported_events: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="forwardHeaders")
    def forward_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="supportedEvents")
    def supported_events(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class LbEdgeExtensionExtensionChainMatchCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, cel_expression: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="celExpression")
    def cel_expression(self) -> _builtins.str: ...

@pulumi.output_type
class LbRouteExtensionExtensionChain(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        extensions: Sequence[outputs.LbRouteExtensionExtensionChainExtension],
        match_condition: outputs.LbRouteExtensionExtensionChainMatchCondition,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> Sequence[outputs.LbRouteExtensionExtensionChainExtension]: ...
    @_builtins.property
    @pulumi.getter(name="matchCondition")
    def match_condition(
        self,
    ) -> outputs.LbRouteExtensionExtensionChainMatchCondition: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class LbRouteExtensionExtensionChainExtension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        service: _builtins.str,
        authority: Optional[_builtins.str] = ...,
        fail_open: Optional[_builtins.bool] = ...,
        forward_headers: Optional[Sequence[_builtins.str]] = ...,
        metadata: Optional[Mapping[str, _builtins.str]] = ...,
        observability_mode: Optional[_builtins.bool] = ...,
        request_body_send_mode: Optional[_builtins.str] = ...,
        supported_events: Optional[Sequence[_builtins.str]] = ...,
        timeout: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="forwardHeaders")
    def forward_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="observabilityMode")
    def observability_mode(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="requestBodySendMode")
    def request_body_send_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportedEvents")
    def supported_events(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LbRouteExtensionExtensionChainMatchCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, cel_expression: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="celExpression")
    def cel_expression(self) -> _builtins.str: ...

@pulumi.output_type
class LbTrafficExtensionExtensionChain(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        extensions: Sequence[outputs.LbTrafficExtensionExtensionChainExtension],
        match_condition: outputs.LbTrafficExtensionExtensionChainMatchCondition,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> Sequence[outputs.LbTrafficExtensionExtensionChainExtension]: ...
    @_builtins.property
    @pulumi.getter(name="matchCondition")
    def match_condition(
        self,
    ) -> outputs.LbTrafficExtensionExtensionChainMatchCondition: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class LbTrafficExtensionExtensionChainExtension(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        service: _builtins.str,
        authority: Optional[_builtins.str] = ...,
        fail_open: Optional[_builtins.bool] = ...,
        forward_headers: Optional[Sequence[_builtins.str]] = ...,
        metadata: Optional[Mapping[str, _builtins.str]] = ...,
        supported_events: Optional[Sequence[_builtins.str]] = ...,
        timeout: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="forwardHeaders")
    def forward_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="supportedEvents")
    def supported_events(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LbTrafficExtensionExtensionChainMatchCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, cel_expression: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="celExpression")
    def cel_expression(self) -> _builtins.str: ...

@pulumi.output_type
class MulticastConsumerAssociationState(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MulticastDomainActivationState(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MulticastDomainActivationTrafficSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aggr_egress_pps: Optional[_builtins.str] = ...,
        aggr_ingress_pps: Optional[_builtins.str] = ...,
        avg_packet_size: Optional[_builtins.int] = ...,
        max_per_group_ingress_pps: Optional[_builtins.str] = ...,
        max_per_group_subscribers: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggrEgressPps")
    def aggr_egress_pps(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="aggrIngressPps")
    def aggr_ingress_pps(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="avgPacketSize")
    def avg_packet_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxPerGroupIngressPps")
    def max_per_group_ingress_pps(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxPerGroupSubscribers")
    def max_per_group_subscribers(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MulticastDomainConnectionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_type: _builtins.str,
        ncc_hub: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nccHub")
    def ncc_hub(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MulticastDomainGroupState(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MulticastDomainState(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MulticastDomainUllMulticastDomain(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, preconfigured_ull_domain: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preconfiguredUllDomain")
    def preconfigured_ull_domain(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MulticastGroupConsumerActivationLogConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MulticastGroupConsumerActivationState(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MulticastGroupProducerActivationState(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MulticastGroupRangeActivationLogConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MulticastGroupRangeActivationState(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MulticastGroupRangeLogConfig(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MulticastGroupRangeState(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MulticastProducerAssociationState(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceLbPoliciesAutoCapacityDrain(dict):
    def __init__(__self__, *, enable: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ServiceLbPoliciesFailoverConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, failover_health_threshold: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failoverHealthThreshold")
    def failover_health_threshold(self) -> _builtins.int: ...

@pulumi.output_type
class ServiceLbPoliciesIsolationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        isolation_granularity: Optional[_builtins.str] = ...,
        isolation_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isolationGranularity")
    def isolation_granularity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isolationMode")
    def isolation_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TcpRouteRule(dict):
    def __init__(
        __self__,
        *,
        action: outputs.TcpRouteRuleAction,
        matches: Optional[Sequence[outputs.TcpRouteRuleMatch]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.TcpRouteRuleAction: ...
    @_builtins.property
    @pulumi.getter
    def matches(self) -> Optional[Sequence[outputs.TcpRouteRuleMatch]]: ...

@pulumi.output_type
class TcpRouteRuleAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destinations: Optional[Sequence[outputs.TcpRouteRuleActionDestination]] = ...,
        idle_timeout: Optional[_builtins.str] = ...,
        original_destination: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[Sequence[outputs.TcpRouteRuleActionDestination]]: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originalDestination")
    def original_destination(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class TcpRouteRuleActionDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_name: Optional[_builtins.str] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TcpRouteRuleMatch(dict):
    def __init__(__self__, *, address: _builtins.str, port: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str: ...

@pulumi.output_type
class TlsRouteRule(dict):
    def __init__(
        __self__,
        *,
        action: outputs.TlsRouteRuleAction,
        matches: Sequence[outputs.TlsRouteRuleMatch],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.TlsRouteRuleAction: ...
    @_builtins.property
    @pulumi.getter
    def matches(self) -> Sequence[outputs.TlsRouteRuleMatch]: ...

@pulumi.output_type
class TlsRouteRuleAction(dict):
    def __init__(
        __self__,
        *,
        destinations: Optional[Sequence[outputs.TlsRouteRuleActionDestination]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[Sequence[outputs.TlsRouteRuleActionDestination]]: ...

@pulumi.output_type
class TlsRouteRuleActionDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_name: Optional[_builtins.str] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TlsRouteRuleMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        alpns: Optional[Sequence[_builtins.str]] = ...,
        sni_hosts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alpns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sniHosts")
    def sni_hosts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class WasmPluginLogConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable: Optional[_builtins.bool] = ...,
        min_log_level: Optional[_builtins.str] = ...,
        sample_rate: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="minLogLevel")
    def min_log_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sampleRate")
    def sample_rate(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class WasmPluginUsedBy(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WasmPluginVersion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        version_name: _builtins.str,
        create_time: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        image_digest: Optional[_builtins.str] = ...,
        image_uri: Optional[_builtins.str] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        plugin_config_data: Optional[_builtins.str] = ...,
        plugin_config_digest: Optional[_builtins.str] = ...,
        plugin_config_uri: Optional[_builtins.str] = ...,
        update_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="versionName")
    def version_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageDigest")
    def image_digest(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pluginConfigData")
    def plugin_config_data(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pluginConfigDigest")
    def plugin_config_digest(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pluginConfigUri")
    def plugin_config_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]: ...
