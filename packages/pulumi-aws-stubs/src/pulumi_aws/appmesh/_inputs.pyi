import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GatewayRouteSpecArgs",
    "GatewayRouteSpecArgsDict",
    "GatewayRouteSpecGrpcRouteArgs",
    "GatewayRouteSpecGrpcRouteArgsDict",
    "GatewayRouteSpecGrpcRouteActionArgs",
    "GatewayRouteSpecGrpcRouteActionArgsDict",
    "GatewayRouteSpecGrpcRouteActionTargetArgs",
    "GatewayRouteSpecGrpcRouteActionTargetArgsDict",
    ...,
    ...,
    "GatewayRouteSpecGrpcRouteMatchArgs",
    "GatewayRouteSpecGrpcRouteMatchArgsDict",
    "GatewayRouteSpecHttp2RouteArgs",
    "GatewayRouteSpecHttp2RouteArgsDict",
    "GatewayRouteSpecHttp2RouteActionArgs",
    "GatewayRouteSpecHttp2RouteActionArgsDict",
    "GatewayRouteSpecHttp2RouteActionRewriteArgs",
    "GatewayRouteSpecHttp2RouteActionRewriteArgsDict",
    ...,
    ...,
    "GatewayRouteSpecHttp2RouteActionRewritePathArgs",
    ...,
    "GatewayRouteSpecHttp2RouteActionRewritePrefixArgs",
    ...,
    "GatewayRouteSpecHttp2RouteActionTargetArgs",
    "GatewayRouteSpecHttp2RouteActionTargetArgsDict",
    ...,
    ...,
    "GatewayRouteSpecHttp2RouteMatchArgs",
    "GatewayRouteSpecHttp2RouteMatchArgsDict",
    "GatewayRouteSpecHttp2RouteMatchHeaderArgs",
    "GatewayRouteSpecHttp2RouteMatchHeaderArgsDict",
    "GatewayRouteSpecHttp2RouteMatchHeaderMatchArgs",
    "GatewayRouteSpecHttp2RouteMatchHeaderMatchArgsDict",
    ...,
    ...,
    "GatewayRouteSpecHttp2RouteMatchHostnameArgs",
    "GatewayRouteSpecHttp2RouteMatchHostnameArgsDict",
    "GatewayRouteSpecHttp2RouteMatchPathArgs",
    "GatewayRouteSpecHttp2RouteMatchPathArgsDict",
    "GatewayRouteSpecHttp2RouteMatchQueryParameterArgs",
    ...,
    ...,
    ...,
    "GatewayRouteSpecHttpRouteArgs",
    "GatewayRouteSpecHttpRouteArgsDict",
    "GatewayRouteSpecHttpRouteActionArgs",
    "GatewayRouteSpecHttpRouteActionArgsDict",
    "GatewayRouteSpecHttpRouteActionRewriteArgs",
    "GatewayRouteSpecHttpRouteActionRewriteArgsDict",
    "GatewayRouteSpecHttpRouteActionRewriteHostnameArgs",
    ...,
    "GatewayRouteSpecHttpRouteActionRewritePathArgs",
    "GatewayRouteSpecHttpRouteActionRewritePathArgsDict",
    "GatewayRouteSpecHttpRouteActionRewritePrefixArgs",
    ...,
    "GatewayRouteSpecHttpRouteActionTargetArgs",
    "GatewayRouteSpecHttpRouteActionTargetArgsDict",
    ...,
    ...,
    "GatewayRouteSpecHttpRouteMatchArgs",
    "GatewayRouteSpecHttpRouteMatchArgsDict",
    "GatewayRouteSpecHttpRouteMatchHeaderArgs",
    "GatewayRouteSpecHttpRouteMatchHeaderArgsDict",
    "GatewayRouteSpecHttpRouteMatchHeaderMatchArgs",
    "GatewayRouteSpecHttpRouteMatchHeaderMatchArgsDict",
    "GatewayRouteSpecHttpRouteMatchHeaderMatchRangeArgs",
    ...,
    "GatewayRouteSpecHttpRouteMatchHostnameArgs",
    "GatewayRouteSpecHttpRouteMatchHostnameArgsDict",
    "GatewayRouteSpecHttpRouteMatchPathArgs",
    "GatewayRouteSpecHttpRouteMatchPathArgsDict",
    "GatewayRouteSpecHttpRouteMatchQueryParameterArgs",
    ...,
    ...,
    ...,
    "MeshSpecArgs",
    "MeshSpecArgsDict",
    "MeshSpecEgressFilterArgs",
    "MeshSpecEgressFilterArgsDict",
    "MeshSpecServiceDiscoveryArgs",
    "MeshSpecServiceDiscoveryArgsDict",
    "RouteSpecArgs",
    "RouteSpecArgsDict",
    "RouteSpecGrpcRouteArgs",
    "RouteSpecGrpcRouteArgsDict",
    "RouteSpecGrpcRouteActionArgs",
    "RouteSpecGrpcRouteActionArgsDict",
    "RouteSpecGrpcRouteActionWeightedTargetArgs",
    "RouteSpecGrpcRouteActionWeightedTargetArgsDict",
    "RouteSpecGrpcRouteMatchArgs",
    "RouteSpecGrpcRouteMatchArgsDict",
    "RouteSpecGrpcRouteMatchMetadataArgs",
    "RouteSpecGrpcRouteMatchMetadataArgsDict",
    "RouteSpecGrpcRouteMatchMetadataMatchArgs",
    "RouteSpecGrpcRouteMatchMetadataMatchArgsDict",
    "RouteSpecGrpcRouteMatchMetadataMatchRangeArgs",
    "RouteSpecGrpcRouteMatchMetadataMatchRangeArgsDict",
    "RouteSpecGrpcRouteRetryPolicyArgs",
    "RouteSpecGrpcRouteRetryPolicyArgsDict",
    "RouteSpecGrpcRouteRetryPolicyPerRetryTimeoutArgs",
    ...,
    "RouteSpecGrpcRouteTimeoutArgs",
    "RouteSpecGrpcRouteTimeoutArgsDict",
    "RouteSpecGrpcRouteTimeoutIdleArgs",
    "RouteSpecGrpcRouteTimeoutIdleArgsDict",
    "RouteSpecGrpcRouteTimeoutPerRequestArgs",
    "RouteSpecGrpcRouteTimeoutPerRequestArgsDict",
    "RouteSpecHttp2RouteArgs",
    "RouteSpecHttp2RouteArgsDict",
    "RouteSpecHttp2RouteActionArgs",
    "RouteSpecHttp2RouteActionArgsDict",
    "RouteSpecHttp2RouteActionWeightedTargetArgs",
    "RouteSpecHttp2RouteActionWeightedTargetArgsDict",
    "RouteSpecHttp2RouteMatchArgs",
    "RouteSpecHttp2RouteMatchArgsDict",
    "RouteSpecHttp2RouteMatchHeaderArgs",
    "RouteSpecHttp2RouteMatchHeaderArgsDict",
    "RouteSpecHttp2RouteMatchHeaderMatchArgs",
    "RouteSpecHttp2RouteMatchHeaderMatchArgsDict",
    "RouteSpecHttp2RouteMatchHeaderMatchRangeArgs",
    "RouteSpecHttp2RouteMatchHeaderMatchRangeArgsDict",
    "RouteSpecHttp2RouteMatchPathArgs",
    "RouteSpecHttp2RouteMatchPathArgsDict",
    "RouteSpecHttp2RouteMatchQueryParameterArgs",
    "RouteSpecHttp2RouteMatchQueryParameterArgsDict",
    "RouteSpecHttp2RouteMatchQueryParameterMatchArgs",
    ...,
    "RouteSpecHttp2RouteRetryPolicyArgs",
    "RouteSpecHttp2RouteRetryPolicyArgsDict",
    "RouteSpecHttp2RouteRetryPolicyPerRetryTimeoutArgs",
    ...,
    "RouteSpecHttp2RouteTimeoutArgs",
    "RouteSpecHttp2RouteTimeoutArgsDict",
    "RouteSpecHttp2RouteTimeoutIdleArgs",
    "RouteSpecHttp2RouteTimeoutIdleArgsDict",
    "RouteSpecHttp2RouteTimeoutPerRequestArgs",
    "RouteSpecHttp2RouteTimeoutPerRequestArgsDict",
    "RouteSpecHttpRouteArgs",
    "RouteSpecHttpRouteArgsDict",
    "RouteSpecHttpRouteActionArgs",
    "RouteSpecHttpRouteActionArgsDict",
    "RouteSpecHttpRouteActionWeightedTargetArgs",
    "RouteSpecHttpRouteActionWeightedTargetArgsDict",
    "RouteSpecHttpRouteMatchArgs",
    "RouteSpecHttpRouteMatchArgsDict",
    "RouteSpecHttpRouteMatchHeaderArgs",
    "RouteSpecHttpRouteMatchHeaderArgsDict",
    "RouteSpecHttpRouteMatchHeaderMatchArgs",
    "RouteSpecHttpRouteMatchHeaderMatchArgsDict",
    "RouteSpecHttpRouteMatchHeaderMatchRangeArgs",
    "RouteSpecHttpRouteMatchHeaderMatchRangeArgsDict",
    "RouteSpecHttpRouteMatchPathArgs",
    "RouteSpecHttpRouteMatchPathArgsDict",
    "RouteSpecHttpRouteMatchQueryParameterArgs",
    "RouteSpecHttpRouteMatchQueryParameterArgsDict",
    "RouteSpecHttpRouteMatchQueryParameterMatchArgs",
    "RouteSpecHttpRouteMatchQueryParameterMatchArgsDict",
    "RouteSpecHttpRouteRetryPolicyArgs",
    "RouteSpecHttpRouteRetryPolicyArgsDict",
    "RouteSpecHttpRouteRetryPolicyPerRetryTimeoutArgs",
    ...,
    "RouteSpecHttpRouteTimeoutArgs",
    "RouteSpecHttpRouteTimeoutArgsDict",
    "RouteSpecHttpRouteTimeoutIdleArgs",
    "RouteSpecHttpRouteTimeoutIdleArgsDict",
    "RouteSpecHttpRouteTimeoutPerRequestArgs",
    "RouteSpecHttpRouteTimeoutPerRequestArgsDict",
    "RouteSpecTcpRouteArgs",
    "RouteSpecTcpRouteArgsDict",
    "RouteSpecTcpRouteActionArgs",
    "RouteSpecTcpRouteActionArgsDict",
    "RouteSpecTcpRouteActionWeightedTargetArgs",
    "RouteSpecTcpRouteActionWeightedTargetArgsDict",
    "RouteSpecTcpRouteMatchArgs",
    "RouteSpecTcpRouteMatchArgsDict",
    "RouteSpecTcpRouteTimeoutArgs",
    "RouteSpecTcpRouteTimeoutArgsDict",
    "RouteSpecTcpRouteTimeoutIdleArgs",
    "RouteSpecTcpRouteTimeoutIdleArgsDict",
    "VirtualGatewaySpecArgs",
    "VirtualGatewaySpecArgsDict",
    "VirtualGatewaySpecBackendDefaultsArgs",
    "VirtualGatewaySpecBackendDefaultsArgsDict",
    "VirtualGatewaySpecBackendDefaultsClientPolicyArgs",
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
    "VirtualGatewaySpecListenerArgs",
    "VirtualGatewaySpecListenerArgsDict",
    "VirtualGatewaySpecListenerConnectionPoolArgs",
    "VirtualGatewaySpecListenerConnectionPoolArgsDict",
    "VirtualGatewaySpecListenerConnectionPoolGrpcArgs",
    ...,
    "VirtualGatewaySpecListenerConnectionPoolHttp2Args",
    ...,
    "VirtualGatewaySpecListenerConnectionPoolHttpArgs",
    ...,
    "VirtualGatewaySpecListenerHealthCheckArgs",
    "VirtualGatewaySpecListenerHealthCheckArgsDict",
    "VirtualGatewaySpecListenerPortMappingArgs",
    "VirtualGatewaySpecListenerPortMappingArgsDict",
    "VirtualGatewaySpecListenerTlsArgs",
    "VirtualGatewaySpecListenerTlsArgsDict",
    "VirtualGatewaySpecListenerTlsCertificateArgs",
    "VirtualGatewaySpecListenerTlsCertificateArgsDict",
    "VirtualGatewaySpecListenerTlsCertificateAcmArgs",
    ...,
    "VirtualGatewaySpecListenerTlsCertificateFileArgs",
    ...,
    "VirtualGatewaySpecListenerTlsCertificateSdsArgs",
    ...,
    "VirtualGatewaySpecListenerTlsValidationArgs",
    "VirtualGatewaySpecListenerTlsValidationArgsDict",
    ...,
    ...,
    ...,
    ...,
    "VirtualGatewaySpecListenerTlsValidationTrustArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "VirtualGatewaySpecLoggingArgs",
    "VirtualGatewaySpecLoggingArgsDict",
    "VirtualGatewaySpecLoggingAccessLogArgs",
    "VirtualGatewaySpecLoggingAccessLogArgsDict",
    "VirtualGatewaySpecLoggingAccessLogFileArgs",
    "VirtualGatewaySpecLoggingAccessLogFileArgsDict",
    "VirtualGatewaySpecLoggingAccessLogFileFormatArgs",
    ...,
    ...,
    ...,
    "VirtualNodeSpecArgs",
    "VirtualNodeSpecArgsDict",
    "VirtualNodeSpecBackendArgs",
    "VirtualNodeSpecBackendArgsDict",
    "VirtualNodeSpecBackendDefaultsArgs",
    "VirtualNodeSpecBackendDefaultsArgsDict",
    "VirtualNodeSpecBackendDefaultsClientPolicyArgs",
    "VirtualNodeSpecBackendDefaultsClientPolicyArgsDict",
    "VirtualNodeSpecBackendDefaultsClientPolicyTlsArgs",
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
    "VirtualNodeSpecBackendVirtualServiceArgs",
    "VirtualNodeSpecBackendVirtualServiceArgsDict",
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
    "VirtualNodeSpecListenerArgs",
    "VirtualNodeSpecListenerArgsDict",
    "VirtualNodeSpecListenerConnectionPoolArgs",
    "VirtualNodeSpecListenerConnectionPoolArgsDict",
    "VirtualNodeSpecListenerConnectionPoolGrpcArgs",
    "VirtualNodeSpecListenerConnectionPoolGrpcArgsDict",
    "VirtualNodeSpecListenerConnectionPoolHttp2Args",
    "VirtualNodeSpecListenerConnectionPoolHttp2ArgsDict",
    "VirtualNodeSpecListenerConnectionPoolHttpArgs",
    "VirtualNodeSpecListenerConnectionPoolHttpArgsDict",
    "VirtualNodeSpecListenerConnectionPoolTcpArgs",
    "VirtualNodeSpecListenerConnectionPoolTcpArgsDict",
    "VirtualNodeSpecListenerHealthCheckArgs",
    "VirtualNodeSpecListenerHealthCheckArgsDict",
    "VirtualNodeSpecListenerOutlierDetectionArgs",
    "VirtualNodeSpecListenerOutlierDetectionArgsDict",
    ...,
    ...,
    ...,
    ...,
    "VirtualNodeSpecListenerPortMappingArgs",
    "VirtualNodeSpecListenerPortMappingArgsDict",
    "VirtualNodeSpecListenerTimeoutArgs",
    "VirtualNodeSpecListenerTimeoutArgsDict",
    "VirtualNodeSpecListenerTimeoutGrpcArgs",
    "VirtualNodeSpecListenerTimeoutGrpcArgsDict",
    "VirtualNodeSpecListenerTimeoutGrpcIdleArgs",
    "VirtualNodeSpecListenerTimeoutGrpcIdleArgsDict",
    "VirtualNodeSpecListenerTimeoutGrpcPerRequestArgs",
    ...,
    "VirtualNodeSpecListenerTimeoutHttp2Args",
    "VirtualNodeSpecListenerTimeoutHttp2ArgsDict",
    "VirtualNodeSpecListenerTimeoutHttp2IdleArgs",
    "VirtualNodeSpecListenerTimeoutHttp2IdleArgsDict",
    "VirtualNodeSpecListenerTimeoutHttp2PerRequestArgs",
    ...,
    "VirtualNodeSpecListenerTimeoutHttpArgs",
    "VirtualNodeSpecListenerTimeoutHttpArgsDict",
    "VirtualNodeSpecListenerTimeoutHttpIdleArgs",
    "VirtualNodeSpecListenerTimeoutHttpIdleArgsDict",
    "VirtualNodeSpecListenerTimeoutHttpPerRequestArgs",
    ...,
    "VirtualNodeSpecListenerTimeoutTcpArgs",
    "VirtualNodeSpecListenerTimeoutTcpArgsDict",
    "VirtualNodeSpecListenerTimeoutTcpIdleArgs",
    "VirtualNodeSpecListenerTimeoutTcpIdleArgsDict",
    "VirtualNodeSpecListenerTlsArgs",
    "VirtualNodeSpecListenerTlsArgsDict",
    "VirtualNodeSpecListenerTlsCertificateArgs",
    "VirtualNodeSpecListenerTlsCertificateArgsDict",
    "VirtualNodeSpecListenerTlsCertificateAcmArgs",
    "VirtualNodeSpecListenerTlsCertificateAcmArgsDict",
    "VirtualNodeSpecListenerTlsCertificateFileArgs",
    "VirtualNodeSpecListenerTlsCertificateFileArgsDict",
    "VirtualNodeSpecListenerTlsCertificateSdsArgs",
    "VirtualNodeSpecListenerTlsCertificateSdsArgsDict",
    "VirtualNodeSpecListenerTlsValidationArgs",
    "VirtualNodeSpecListenerTlsValidationArgsDict",
    ...,
    ...,
    ...,
    ...,
    "VirtualNodeSpecListenerTlsValidationTrustArgs",
    "VirtualNodeSpecListenerTlsValidationTrustArgsDict",
    "VirtualNodeSpecListenerTlsValidationTrustFileArgs",
    ...,
    "VirtualNodeSpecListenerTlsValidationTrustSdsArgs",
    ...,
    "VirtualNodeSpecLoggingArgs",
    "VirtualNodeSpecLoggingArgsDict",
    "VirtualNodeSpecLoggingAccessLogArgs",
    "VirtualNodeSpecLoggingAccessLogArgsDict",
    "VirtualNodeSpecLoggingAccessLogFileArgs",
    "VirtualNodeSpecLoggingAccessLogFileArgsDict",
    "VirtualNodeSpecLoggingAccessLogFileFormatArgs",
    "VirtualNodeSpecLoggingAccessLogFileFormatArgsDict",
    "VirtualNodeSpecLoggingAccessLogFileFormatJsonArgs",
    ...,
    "VirtualNodeSpecServiceDiscoveryArgs",
    "VirtualNodeSpecServiceDiscoveryArgsDict",
    "VirtualNodeSpecServiceDiscoveryAwsCloudMapArgs",
    "VirtualNodeSpecServiceDiscoveryAwsCloudMapArgsDict",
    "VirtualNodeSpecServiceDiscoveryDnsArgs",
    "VirtualNodeSpecServiceDiscoveryDnsArgsDict",
    "VirtualRouterSpecArgs",
    "VirtualRouterSpecArgsDict",
    "VirtualRouterSpecListenerArgs",
    "VirtualRouterSpecListenerArgsDict",
    "VirtualRouterSpecListenerPortMappingArgs",
    "VirtualRouterSpecListenerPortMappingArgsDict",
    "VirtualServiceSpecArgs",
    "VirtualServiceSpecArgsDict",
    "VirtualServiceSpecProviderArgs",
    "VirtualServiceSpecProviderArgsDict",
    "VirtualServiceSpecProviderVirtualNodeArgs",
    "VirtualServiceSpecProviderVirtualNodeArgsDict",
    "VirtualServiceSpecProviderVirtualRouterArgs",
    "VirtualServiceSpecProviderVirtualRouterArgsDict",
]

class GatewayRouteSpecArgsDict(TypedDict):
    grpc_route: NotRequired[pulumi.Input[GatewayRouteSpecGrpcRouteArgsDict]]
    http2_route: NotRequired[pulumi.Input[GatewayRouteSpecHttp2RouteArgsDict]]
    http_route: NotRequired[pulumi.Input[GatewayRouteSpecHttpRouteArgsDict]]
    priority: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GatewayRouteSpecArgs:
    def __init__(
        __self__,
        *,
        grpc_route: Optional[pulumi.Input[GatewayRouteSpecGrpcRouteArgs]] = ...,
        http2_route: Optional[pulumi.Input[GatewayRouteSpecHttp2RouteArgs]] = ...,
        http_route: Optional[pulumi.Input[GatewayRouteSpecHttpRouteArgs]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="grpcRoute")
    def grpc_route(self) -> Optional[pulumi.Input[GatewayRouteSpecGrpcRouteArgs]]: ...
    @grpc_route.setter
    def grpc_route(
        self, value: Optional[pulumi.Input[GatewayRouteSpecGrpcRouteArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="http2Route")
    def http2_route(self) -> Optional[pulumi.Input[GatewayRouteSpecHttp2RouteArgs]]: ...
    @http2_route.setter
    def http2_route(
        self, value: Optional[pulumi.Input[GatewayRouteSpecHttp2RouteArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpRoute")
    def http_route(self) -> Optional[pulumi.Input[GatewayRouteSpecHttpRouteArgs]]: ...
    @http_route.setter
    def http_route(
        self, value: Optional[pulumi.Input[GatewayRouteSpecHttpRouteArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GatewayRouteSpecGrpcRouteArgsDict(TypedDict):
    action: pulumi.Input[GatewayRouteSpecGrpcRouteActionArgsDict]
    match: pulumi.Input[GatewayRouteSpecGrpcRouteMatchArgsDict]

@pulumi.input_type
class GatewayRouteSpecGrpcRouteArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[GatewayRouteSpecGrpcRouteActionArgs],
        match: pulumi.Input[GatewayRouteSpecGrpcRouteMatchArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[GatewayRouteSpecGrpcRouteActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[GatewayRouteSpecGrpcRouteActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Input[GatewayRouteSpecGrpcRouteMatchArgs]: ...
    @match.setter
    def match(self, value: pulumi.Input[GatewayRouteSpecGrpcRouteMatchArgs]): ...

class GatewayRouteSpecGrpcRouteActionArgsDict(TypedDict):
    target: pulumi.Input[GatewayRouteSpecGrpcRouteActionTargetArgsDict]

@pulumi.input_type
class GatewayRouteSpecGrpcRouteActionArgs:
    def __init__(
        __self__, *, target: pulumi.Input[GatewayRouteSpecGrpcRouteActionTargetArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[GatewayRouteSpecGrpcRouteActionTargetArgs]: ...
    @target.setter
    def target(
        self, value: pulumi.Input[GatewayRouteSpecGrpcRouteActionTargetArgs]
    ): ...

class GatewayRouteSpecGrpcRouteActionTargetArgsDict(TypedDict):
    virtual_service: pulumi.Input[
        GatewayRouteSpecGrpcRouteActionTargetVirtualServiceArgsDict
    ]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GatewayRouteSpecGrpcRouteActionTargetArgs:
    def __init__(
        __self__,
        *,
        virtual_service: pulumi.Input[
            GatewayRouteSpecGrpcRouteActionTargetVirtualServiceArgs
        ],
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualService")
    def virtual_service(
        self,
    ) -> pulumi.Input[GatewayRouteSpecGrpcRouteActionTargetVirtualServiceArgs]: ...
    @virtual_service.setter
    def virtual_service(
        self,
        value: pulumi.Input[GatewayRouteSpecGrpcRouteActionTargetVirtualServiceArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GatewayRouteSpecGrpcRouteActionTargetVirtualServiceArgsDict(TypedDict):
    virtual_service_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class GatewayRouteSpecGrpcRouteActionTargetVirtualServiceArgs:
    def __init__(
        __self__, *, virtual_service_name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualServiceName")
    def virtual_service_name(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_service_name.setter
    def virtual_service_name(self, value: pulumi.Input[_builtins.str]): ...

class GatewayRouteSpecGrpcRouteMatchArgsDict(TypedDict):
    service_name: pulumi.Input[_builtins.str]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GatewayRouteSpecGrpcRouteMatchArgs:
    def __init__(
        __self__,
        *,
        service_name: pulumi.Input[_builtins.str],
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GatewayRouteSpecHttp2RouteArgsDict(TypedDict):
    action: pulumi.Input[GatewayRouteSpecHttp2RouteActionArgsDict]
    match: pulumi.Input[GatewayRouteSpecHttp2RouteMatchArgsDict]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[GatewayRouteSpecHttp2RouteActionArgs],
        match: pulumi.Input[GatewayRouteSpecHttp2RouteMatchArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[GatewayRouteSpecHttp2RouteActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[GatewayRouteSpecHttp2RouteActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Input[GatewayRouteSpecHttp2RouteMatchArgs]: ...
    @match.setter
    def match(self, value: pulumi.Input[GatewayRouteSpecHttp2RouteMatchArgs]): ...

class GatewayRouteSpecHttp2RouteActionArgsDict(TypedDict):
    target: pulumi.Input[GatewayRouteSpecHttp2RouteActionTargetArgsDict]
    rewrite: NotRequired[pulumi.Input[GatewayRouteSpecHttp2RouteActionRewriteArgsDict]]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteActionArgs:
    def __init__(
        __self__,
        *,
        target: pulumi.Input[GatewayRouteSpecHttp2RouteActionTargetArgs],
        rewrite: Optional[
            pulumi.Input[GatewayRouteSpecHttp2RouteActionRewriteArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[GatewayRouteSpecHttp2RouteActionTargetArgs]: ...
    @target.setter
    def target(
        self, value: pulumi.Input[GatewayRouteSpecHttp2RouteActionTargetArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def rewrite(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttp2RouteActionRewriteArgs]]: ...
    @rewrite.setter
    def rewrite(
        self, value: Optional[pulumi.Input[GatewayRouteSpecHttp2RouteActionRewriteArgs]]
    ): ...

class GatewayRouteSpecHttp2RouteActionRewriteArgsDict(TypedDict):
    hostname: NotRequired[
        pulumi.Input[GatewayRouteSpecHttp2RouteActionRewriteHostnameArgsDict]
    ]
    path: NotRequired[pulumi.Input[GatewayRouteSpecHttp2RouteActionRewritePathArgsDict]]
    prefix: NotRequired[
        pulumi.Input[GatewayRouteSpecHttp2RouteActionRewritePrefixArgsDict]
    ]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteActionRewriteArgs:
    def __init__(
        __self__,
        *,
        hostname: Optional[
            pulumi.Input[GatewayRouteSpecHttp2RouteActionRewriteHostnameArgs]
        ] = ...,
        path: Optional[
            pulumi.Input[GatewayRouteSpecHttp2RouteActionRewritePathArgs]
        ] = ...,
        prefix: Optional[
            pulumi.Input[GatewayRouteSpecHttp2RouteActionRewritePrefixArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(
        self,
    ) -> Optional[
        pulumi.Input[GatewayRouteSpecHttp2RouteActionRewriteHostnameArgs]
    ]: ...
    @hostname.setter
    def hostname(
        self,
        value: Optional[
            pulumi.Input[GatewayRouteSpecHttp2RouteActionRewriteHostnameArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttp2RouteActionRewritePathArgs]]: ...
    @path.setter
    def path(
        self,
        value: Optional[pulumi.Input[GatewayRouteSpecHttp2RouteActionRewritePathArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def prefix(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttp2RouteActionRewritePrefixArgs]]: ...
    @prefix.setter
    def prefix(
        self,
        value: Optional[
            pulumi.Input[GatewayRouteSpecHttp2RouteActionRewritePrefixArgs]
        ],
    ): ...

class GatewayRouteSpecHttp2RouteActionRewriteHostnameArgsDict(TypedDict):
    default_target_hostname: pulumi.Input[_builtins.str]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteActionRewriteHostnameArgs:
    def __init__(
        __self__, *, default_target_hostname: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultTargetHostname")
    def default_target_hostname(self) -> pulumi.Input[_builtins.str]: ...
    @default_target_hostname.setter
    def default_target_hostname(self, value: pulumi.Input[_builtins.str]): ...

class GatewayRouteSpecHttp2RouteActionRewritePathArgsDict(TypedDict):
    exact: pulumi.Input[_builtins.str]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteActionRewritePathArgs:
    def __init__(__self__, *, exact: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> pulumi.Input[_builtins.str]: ...
    @exact.setter
    def exact(self, value: pulumi.Input[_builtins.str]): ...

class GatewayRouteSpecHttp2RouteActionRewritePrefixArgsDict(TypedDict):
    default_prefix: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteActionRewritePrefixArgs:
    def __init__(
        __self__,
        *,
        default_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultPrefix")
    def default_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_prefix.setter
    def default_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GatewayRouteSpecHttp2RouteActionTargetArgsDict(TypedDict):
    virtual_service: pulumi.Input[
        GatewayRouteSpecHttp2RouteActionTargetVirtualServiceArgsDict
    ]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteActionTargetArgs:
    def __init__(
        __self__,
        *,
        virtual_service: pulumi.Input[
            GatewayRouteSpecHttp2RouteActionTargetVirtualServiceArgs
        ],
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualService")
    def virtual_service(
        self,
    ) -> pulumi.Input[GatewayRouteSpecHttp2RouteActionTargetVirtualServiceArgs]: ...
    @virtual_service.setter
    def virtual_service(
        self,
        value: pulumi.Input[GatewayRouteSpecHttp2RouteActionTargetVirtualServiceArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GatewayRouteSpecHttp2RouteActionTargetVirtualServiceArgsDict(TypedDict):
    virtual_service_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteActionTargetVirtualServiceArgs:
    def __init__(
        __self__, *, virtual_service_name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualServiceName")
    def virtual_service_name(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_service_name.setter
    def virtual_service_name(self, value: pulumi.Input[_builtins.str]): ...

class GatewayRouteSpecHttp2RouteMatchArgsDict(TypedDict):
    headers: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[GatewayRouteSpecHttp2RouteMatchHeaderArgsDict]]
        ]
    ]
    hostname: NotRequired[pulumi.Input[GatewayRouteSpecHttp2RouteMatchHostnameArgsDict]]
    path: NotRequired[pulumi.Input[GatewayRouteSpecHttp2RouteMatchPathArgsDict]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    query_parameters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[GatewayRouteSpecHttp2RouteMatchQueryParameterArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteMatchArgs:
    def __init__(
        __self__,
        *,
        headers: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GatewayRouteSpecHttp2RouteMatchHeaderArgs]]
            ]
        ] = ...,
        hostname: Optional[
            pulumi.Input[GatewayRouteSpecHttp2RouteMatchHostnameArgs]
        ] = ...,
        path: Optional[pulumi.Input[GatewayRouteSpecHttp2RouteMatchPathArgs]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        query_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[GatewayRouteSpecHttp2RouteMatchQueryParameterArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GatewayRouteSpecHttp2RouteMatchHeaderArgs]]]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GatewayRouteSpecHttp2RouteMatchHeaderArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def hostname(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttp2RouteMatchHostnameArgs]]: ...
    @hostname.setter
    def hostname(
        self, value: Optional[pulumi.Input[GatewayRouteSpecHttp2RouteMatchHostnameArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttp2RouteMatchPathArgs]]: ...
    @path.setter
    def path(
        self, value: Optional[pulumi.Input[GatewayRouteSpecHttp2RouteMatchPathArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[GatewayRouteSpecHttp2RouteMatchQueryParameterArgs]]
        ]
    ]: ...
    @query_parameters.setter
    def query_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[GatewayRouteSpecHttp2RouteMatchQueryParameterArgs]
                ]
            ]
        ],
    ): ...

class GatewayRouteSpecHttp2RouteMatchHeaderArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    invert: NotRequired[pulumi.Input[_builtins.bool]]
    match: NotRequired[pulumi.Input[GatewayRouteSpecHttp2RouteMatchHeaderMatchArgsDict]]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteMatchHeaderArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        invert: Optional[pulumi.Input[_builtins.bool]] = ...,
        match: Optional[
            pulumi.Input[GatewayRouteSpecHttp2RouteMatchHeaderMatchArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert.setter
    def invert(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttp2RouteMatchHeaderMatchArgs]]: ...
    @match.setter
    def match(
        self,
        value: Optional[pulumi.Input[GatewayRouteSpecHttp2RouteMatchHeaderMatchArgs]],
    ): ...

class GatewayRouteSpecHttp2RouteMatchHeaderMatchArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    range: NotRequired[
        pulumi.Input[GatewayRouteSpecHttp2RouteMatchHeaderMatchRangeArgsDict]
    ]
    regex: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteMatchHeaderMatchArgs:
    def __init__(
        __self__,
        *,
        exact: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        range: Optional[
            pulumi.Input[GatewayRouteSpecHttp2RouteMatchHeaderMatchRangeArgs]
        ] = ...,
        regex: Optional[pulumi.Input[_builtins.str]] = ...,
        suffix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def range(
        self,
    ) -> Optional[
        pulumi.Input[GatewayRouteSpecHttp2RouteMatchHeaderMatchRangeArgs]
    ]: ...
    @range.setter
    def range(
        self,
        value: Optional[
            pulumi.Input[GatewayRouteSpecHttp2RouteMatchHeaderMatchRangeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex.setter
    def regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GatewayRouteSpecHttp2RouteMatchHeaderMatchRangeArgsDict(TypedDict):
    end: pulumi.Input[_builtins.int]
    start: pulumi.Input[_builtins.int]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteMatchHeaderMatchRangeArgs:
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

class GatewayRouteSpecHttp2RouteMatchHostnameArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteMatchHostnameArgs:
    def __init__(
        __self__,
        *,
        exact: Optional[pulumi.Input[_builtins.str]] = ...,
        suffix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GatewayRouteSpecHttp2RouteMatchPathArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]
    regex: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteMatchPathArgs:
    def __init__(
        __self__,
        *,
        exact: Optional[pulumi.Input[_builtins.str]] = ...,
        regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex.setter
    def regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GatewayRouteSpecHttp2RouteMatchQueryParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    match: NotRequired[
        pulumi.Input[GatewayRouteSpecHttp2RouteMatchQueryParameterMatchArgsDict]
    ]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteMatchQueryParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        match: Optional[
            pulumi.Input[GatewayRouteSpecHttp2RouteMatchQueryParameterMatchArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[
        pulumi.Input[GatewayRouteSpecHttp2RouteMatchQueryParameterMatchArgs]
    ]: ...
    @match.setter
    def match(
        self,
        value: Optional[
            pulumi.Input[GatewayRouteSpecHttp2RouteMatchQueryParameterMatchArgs]
        ],
    ): ...

class GatewayRouteSpecHttp2RouteMatchQueryParameterMatchArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayRouteSpecHttp2RouteMatchQueryParameterMatchArgs:
    def __init__(
        __self__, *, exact: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GatewayRouteSpecHttpRouteArgsDict(TypedDict):
    action: pulumi.Input[GatewayRouteSpecHttpRouteActionArgsDict]
    match: pulumi.Input[GatewayRouteSpecHttpRouteMatchArgsDict]

@pulumi.input_type
class GatewayRouteSpecHttpRouteArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[GatewayRouteSpecHttpRouteActionArgs],
        match: pulumi.Input[GatewayRouteSpecHttpRouteMatchArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[GatewayRouteSpecHttpRouteActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[GatewayRouteSpecHttpRouteActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Input[GatewayRouteSpecHttpRouteMatchArgs]: ...
    @match.setter
    def match(self, value: pulumi.Input[GatewayRouteSpecHttpRouteMatchArgs]): ...

class GatewayRouteSpecHttpRouteActionArgsDict(TypedDict):
    target: pulumi.Input[GatewayRouteSpecHttpRouteActionTargetArgsDict]
    rewrite: NotRequired[pulumi.Input[GatewayRouteSpecHttpRouteActionRewriteArgsDict]]

@pulumi.input_type
class GatewayRouteSpecHttpRouteActionArgs:
    def __init__(
        __self__,
        *,
        target: pulumi.Input[GatewayRouteSpecHttpRouteActionTargetArgs],
        rewrite: Optional[
            pulumi.Input[GatewayRouteSpecHttpRouteActionRewriteArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[GatewayRouteSpecHttpRouteActionTargetArgs]: ...
    @target.setter
    def target(
        self, value: pulumi.Input[GatewayRouteSpecHttpRouteActionTargetArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def rewrite(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttpRouteActionRewriteArgs]]: ...
    @rewrite.setter
    def rewrite(
        self, value: Optional[pulumi.Input[GatewayRouteSpecHttpRouteActionRewriteArgs]]
    ): ...

class GatewayRouteSpecHttpRouteActionRewriteArgsDict(TypedDict):
    hostname: NotRequired[
        pulumi.Input[GatewayRouteSpecHttpRouteActionRewriteHostnameArgsDict]
    ]
    path: NotRequired[pulumi.Input[GatewayRouteSpecHttpRouteActionRewritePathArgsDict]]
    prefix: NotRequired[
        pulumi.Input[GatewayRouteSpecHttpRouteActionRewritePrefixArgsDict]
    ]

@pulumi.input_type
class GatewayRouteSpecHttpRouteActionRewriteArgs:
    def __init__(
        __self__,
        *,
        hostname: Optional[
            pulumi.Input[GatewayRouteSpecHttpRouteActionRewriteHostnameArgs]
        ] = ...,
        path: Optional[
            pulumi.Input[GatewayRouteSpecHttpRouteActionRewritePathArgs]
        ] = ...,
        prefix: Optional[
            pulumi.Input[GatewayRouteSpecHttpRouteActionRewritePrefixArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttpRouteActionRewriteHostnameArgs]]: ...
    @hostname.setter
    def hostname(
        self,
        value: Optional[
            pulumi.Input[GatewayRouteSpecHttpRouteActionRewriteHostnameArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttpRouteActionRewritePathArgs]]: ...
    @path.setter
    def path(
        self,
        value: Optional[pulumi.Input[GatewayRouteSpecHttpRouteActionRewritePathArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def prefix(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttpRouteActionRewritePrefixArgs]]: ...
    @prefix.setter
    def prefix(
        self,
        value: Optional[pulumi.Input[GatewayRouteSpecHttpRouteActionRewritePrefixArgs]],
    ): ...

class GatewayRouteSpecHttpRouteActionRewriteHostnameArgsDict(TypedDict):
    default_target_hostname: pulumi.Input[_builtins.str]

@pulumi.input_type
class GatewayRouteSpecHttpRouteActionRewriteHostnameArgs:
    def __init__(
        __self__, *, default_target_hostname: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultTargetHostname")
    def default_target_hostname(self) -> pulumi.Input[_builtins.str]: ...
    @default_target_hostname.setter
    def default_target_hostname(self, value: pulumi.Input[_builtins.str]): ...

class GatewayRouteSpecHttpRouteActionRewritePathArgsDict(TypedDict):
    exact: pulumi.Input[_builtins.str]

@pulumi.input_type
class GatewayRouteSpecHttpRouteActionRewritePathArgs:
    def __init__(__self__, *, exact: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> pulumi.Input[_builtins.str]: ...
    @exact.setter
    def exact(self, value: pulumi.Input[_builtins.str]): ...

class GatewayRouteSpecHttpRouteActionRewritePrefixArgsDict(TypedDict):
    default_prefix: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayRouteSpecHttpRouteActionRewritePrefixArgs:
    def __init__(
        __self__,
        *,
        default_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultPrefix")
    def default_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_prefix.setter
    def default_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GatewayRouteSpecHttpRouteActionTargetArgsDict(TypedDict):
    virtual_service: pulumi.Input[
        GatewayRouteSpecHttpRouteActionTargetVirtualServiceArgsDict
    ]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GatewayRouteSpecHttpRouteActionTargetArgs:
    def __init__(
        __self__,
        *,
        virtual_service: pulumi.Input[
            GatewayRouteSpecHttpRouteActionTargetVirtualServiceArgs
        ],
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualService")
    def virtual_service(
        self,
    ) -> pulumi.Input[GatewayRouteSpecHttpRouteActionTargetVirtualServiceArgs]: ...
    @virtual_service.setter
    def virtual_service(
        self,
        value: pulumi.Input[GatewayRouteSpecHttpRouteActionTargetVirtualServiceArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class GatewayRouteSpecHttpRouteActionTargetVirtualServiceArgsDict(TypedDict):
    virtual_service_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class GatewayRouteSpecHttpRouteActionTargetVirtualServiceArgs:
    def __init__(
        __self__, *, virtual_service_name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualServiceName")
    def virtual_service_name(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_service_name.setter
    def virtual_service_name(self, value: pulumi.Input[_builtins.str]): ...

class GatewayRouteSpecHttpRouteMatchArgsDict(TypedDict):
    headers: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[GatewayRouteSpecHttpRouteMatchHeaderArgsDict]]
        ]
    ]
    hostname: NotRequired[pulumi.Input[GatewayRouteSpecHttpRouteMatchHostnameArgsDict]]
    path: NotRequired[pulumi.Input[GatewayRouteSpecHttpRouteMatchPathArgsDict]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    query_parameters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[GatewayRouteSpecHttpRouteMatchQueryParameterArgsDict]]
        ]
    ]

@pulumi.input_type
class GatewayRouteSpecHttpRouteMatchArgs:
    def __init__(
        __self__,
        *,
        headers: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GatewayRouteSpecHttpRouteMatchHeaderArgs]]
            ]
        ] = ...,
        hostname: Optional[
            pulumi.Input[GatewayRouteSpecHttpRouteMatchHostnameArgs]
        ] = ...,
        path: Optional[pulumi.Input[GatewayRouteSpecHttpRouteMatchPathArgs]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        query_parameters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GatewayRouteSpecHttpRouteMatchQueryParameterArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GatewayRouteSpecHttpRouteMatchHeaderArgs]]]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GatewayRouteSpecHttpRouteMatchHeaderArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def hostname(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttpRouteMatchHostnameArgs]]: ...
    @hostname.setter
    def hostname(
        self, value: Optional[pulumi.Input[GatewayRouteSpecHttpRouteMatchHostnameArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttpRouteMatchPathArgs]]: ...
    @path.setter
    def path(
        self, value: Optional[pulumi.Input[GatewayRouteSpecHttpRouteMatchPathArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[GatewayRouteSpecHttpRouteMatchQueryParameterArgs]]
        ]
    ]: ...
    @query_parameters.setter
    def query_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[GatewayRouteSpecHttpRouteMatchQueryParameterArgs]]
            ]
        ],
    ): ...

class GatewayRouteSpecHttpRouteMatchHeaderArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    invert: NotRequired[pulumi.Input[_builtins.bool]]
    match: NotRequired[pulumi.Input[GatewayRouteSpecHttpRouteMatchHeaderMatchArgsDict]]

@pulumi.input_type
class GatewayRouteSpecHttpRouteMatchHeaderArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        invert: Optional[pulumi.Input[_builtins.bool]] = ...,
        match: Optional[
            pulumi.Input[GatewayRouteSpecHttpRouteMatchHeaderMatchArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert.setter
    def invert(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttpRouteMatchHeaderMatchArgs]]: ...
    @match.setter
    def match(
        self,
        value: Optional[pulumi.Input[GatewayRouteSpecHttpRouteMatchHeaderMatchArgs]],
    ): ...

class GatewayRouteSpecHttpRouteMatchHeaderMatchArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    range: NotRequired[
        pulumi.Input[GatewayRouteSpecHttpRouteMatchHeaderMatchRangeArgsDict]
    ]
    regex: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayRouteSpecHttpRouteMatchHeaderMatchArgs:
    def __init__(
        __self__,
        *,
        exact: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        range: Optional[
            pulumi.Input[GatewayRouteSpecHttpRouteMatchHeaderMatchRangeArgs]
        ] = ...,
        regex: Optional[pulumi.Input[_builtins.str]] = ...,
        suffix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def range(
        self,
    ) -> Optional[pulumi.Input[GatewayRouteSpecHttpRouteMatchHeaderMatchRangeArgs]]: ...
    @range.setter
    def range(
        self,
        value: Optional[
            pulumi.Input[GatewayRouteSpecHttpRouteMatchHeaderMatchRangeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex.setter
    def regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GatewayRouteSpecHttpRouteMatchHeaderMatchRangeArgsDict(TypedDict):
    end: pulumi.Input[_builtins.int]
    start: pulumi.Input[_builtins.int]

@pulumi.input_type
class GatewayRouteSpecHttpRouteMatchHeaderMatchRangeArgs:
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

class GatewayRouteSpecHttpRouteMatchHostnameArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayRouteSpecHttpRouteMatchHostnameArgs:
    def __init__(
        __self__,
        *,
        exact: Optional[pulumi.Input[_builtins.str]] = ...,
        suffix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GatewayRouteSpecHttpRouteMatchPathArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]
    regex: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayRouteSpecHttpRouteMatchPathArgs:
    def __init__(
        __self__,
        *,
        exact: Optional[pulumi.Input[_builtins.str]] = ...,
        regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex.setter
    def regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GatewayRouteSpecHttpRouteMatchQueryParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    match: NotRequired[
        pulumi.Input[GatewayRouteSpecHttpRouteMatchQueryParameterMatchArgsDict]
    ]

@pulumi.input_type
class GatewayRouteSpecHttpRouteMatchQueryParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        match: Optional[
            pulumi.Input[GatewayRouteSpecHttpRouteMatchQueryParameterMatchArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[
        pulumi.Input[GatewayRouteSpecHttpRouteMatchQueryParameterMatchArgs]
    ]: ...
    @match.setter
    def match(
        self,
        value: Optional[
            pulumi.Input[GatewayRouteSpecHttpRouteMatchQueryParameterMatchArgs]
        ],
    ): ...

class GatewayRouteSpecHttpRouteMatchQueryParameterMatchArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GatewayRouteSpecHttpRouteMatchQueryParameterMatchArgs:
    def __init__(
        __self__, *, exact: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MeshSpecArgsDict(TypedDict):
    egress_filter: NotRequired[pulumi.Input[MeshSpecEgressFilterArgsDict]]
    service_discovery: NotRequired[pulumi.Input[MeshSpecServiceDiscoveryArgsDict]]

@pulumi.input_type
class MeshSpecArgs:
    def __init__(
        __self__,
        *,
        egress_filter: Optional[pulumi.Input[MeshSpecEgressFilterArgs]] = ...,
        service_discovery: Optional[pulumi.Input[MeshSpecServiceDiscoveryArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressFilter")
    def egress_filter(self) -> Optional[pulumi.Input[MeshSpecEgressFilterArgs]]: ...
    @egress_filter.setter
    def egress_filter(
        self, value: Optional[pulumi.Input[MeshSpecEgressFilterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceDiscovery")
    def service_discovery(
        self,
    ) -> Optional[pulumi.Input[MeshSpecServiceDiscoveryArgs]]: ...
    @service_discovery.setter
    def service_discovery(
        self, value: Optional[pulumi.Input[MeshSpecServiceDiscoveryArgs]]
    ): ...

class MeshSpecEgressFilterArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MeshSpecEgressFilterArgs:
    def __init__(
        __self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MeshSpecServiceDiscoveryArgsDict(TypedDict):
    ip_preference: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MeshSpecServiceDiscoveryArgs:
    def __init__(
        __self__, *, ip_preference: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipPreference")
    def ip_preference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_preference.setter
    def ip_preference(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RouteSpecArgsDict(TypedDict):
    grpc_route: NotRequired[pulumi.Input[RouteSpecGrpcRouteArgsDict]]
    http2_route: NotRequired[pulumi.Input[RouteSpecHttp2RouteArgsDict]]
    http_route: NotRequired[pulumi.Input[RouteSpecHttpRouteArgsDict]]
    priority: NotRequired[pulumi.Input[_builtins.int]]
    tcp_route: NotRequired[pulumi.Input[RouteSpecTcpRouteArgsDict]]

@pulumi.input_type
class RouteSpecArgs:
    def __init__(
        __self__,
        *,
        grpc_route: Optional[pulumi.Input[RouteSpecGrpcRouteArgs]] = ...,
        http2_route: Optional[pulumi.Input[RouteSpecHttp2RouteArgs]] = ...,
        http_route: Optional[pulumi.Input[RouteSpecHttpRouteArgs]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        tcp_route: Optional[pulumi.Input[RouteSpecTcpRouteArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="grpcRoute")
    def grpc_route(self) -> Optional[pulumi.Input[RouteSpecGrpcRouteArgs]]: ...
    @grpc_route.setter
    def grpc_route(self, value: Optional[pulumi.Input[RouteSpecGrpcRouteArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="http2Route")
    def http2_route(self) -> Optional[pulumi.Input[RouteSpecHttp2RouteArgs]]: ...
    @http2_route.setter
    def http2_route(self, value: Optional[pulumi.Input[RouteSpecHttp2RouteArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="httpRoute")
    def http_route(self) -> Optional[pulumi.Input[RouteSpecHttpRouteArgs]]: ...
    @http_route.setter
    def http_route(self, value: Optional[pulumi.Input[RouteSpecHttpRouteArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tcpRoute")
    def tcp_route(self) -> Optional[pulumi.Input[RouteSpecTcpRouteArgs]]: ...
    @tcp_route.setter
    def tcp_route(self, value: Optional[pulumi.Input[RouteSpecTcpRouteArgs]]): ...

class RouteSpecGrpcRouteArgsDict(TypedDict):
    action: pulumi.Input[RouteSpecGrpcRouteActionArgsDict]
    match: NotRequired[pulumi.Input[RouteSpecGrpcRouteMatchArgsDict]]
    retry_policy: NotRequired[pulumi.Input[RouteSpecGrpcRouteRetryPolicyArgsDict]]
    timeout: NotRequired[pulumi.Input[RouteSpecGrpcRouteTimeoutArgsDict]]

@pulumi.input_type
class RouteSpecGrpcRouteArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[RouteSpecGrpcRouteActionArgs],
        match: Optional[pulumi.Input[RouteSpecGrpcRouteMatchArgs]] = ...,
        retry_policy: Optional[pulumi.Input[RouteSpecGrpcRouteRetryPolicyArgs]] = ...,
        timeout: Optional[pulumi.Input[RouteSpecGrpcRouteTimeoutArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[RouteSpecGrpcRouteActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[RouteSpecGrpcRouteActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[pulumi.Input[RouteSpecGrpcRouteMatchArgs]]: ...
    @match.setter
    def match(self, value: Optional[pulumi.Input[RouteSpecGrpcRouteMatchArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(
        self,
    ) -> Optional[pulumi.Input[RouteSpecGrpcRouteRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(
        self, value: Optional[pulumi.Input[RouteSpecGrpcRouteRetryPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[RouteSpecGrpcRouteTimeoutArgs]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[RouteSpecGrpcRouteTimeoutArgs]]): ...

class RouteSpecGrpcRouteActionArgsDict(TypedDict):
    weighted_targets: pulumi.Input[
        Sequence[pulumi.Input[RouteSpecGrpcRouteActionWeightedTargetArgsDict]]
    ]

@pulumi.input_type
class RouteSpecGrpcRouteActionArgs:
    def __init__(
        __self__,
        *,
        weighted_targets: pulumi.Input[
            Sequence[pulumi.Input[RouteSpecGrpcRouteActionWeightedTargetArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weightedTargets")
    def weighted_targets(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[RouteSpecGrpcRouteActionWeightedTargetArgs]]
    ]: ...
    @weighted_targets.setter
    def weighted_targets(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[RouteSpecGrpcRouteActionWeightedTargetArgs]]
        ],
    ): ...

class RouteSpecGrpcRouteActionWeightedTargetArgsDict(TypedDict):
    virtual_node: pulumi.Input[_builtins.str]
    weight: pulumi.Input[_builtins.int]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RouteSpecGrpcRouteActionWeightedTargetArgs:
    def __init__(
        __self__,
        *,
        virtual_node: pulumi.Input[_builtins.str],
        weight: pulumi.Input[_builtins.int],
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_node.setter
    def virtual_node(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Input[_builtins.int]: ...
    @weight.setter
    def weight(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RouteSpecGrpcRouteMatchArgsDict(TypedDict):
    metadatas: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RouteSpecGrpcRouteMatchMetadataArgsDict]]]
    ]
    method_name: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    service_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RouteSpecGrpcRouteMatchArgs:
    def __init__(
        __self__,
        *,
        metadatas: Optional[
            pulumi.Input[Sequence[pulumi.Input[RouteSpecGrpcRouteMatchMetadataArgs]]]
        ] = ...,
        method_name: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadatas(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RouteSpecGrpcRouteMatchMetadataArgs]]]
    ]: ...
    @metadatas.setter
    def metadatas(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RouteSpecGrpcRouteMatchMetadataArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="methodName")
    def method_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method_name.setter
    def method_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RouteSpecGrpcRouteMatchMetadataArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    invert: NotRequired[pulumi.Input[_builtins.bool]]
    match: NotRequired[pulumi.Input[RouteSpecGrpcRouteMatchMetadataMatchArgsDict]]

@pulumi.input_type
class RouteSpecGrpcRouteMatchMetadataArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        invert: Optional[pulumi.Input[_builtins.bool]] = ...,
        match: Optional[pulumi.Input[RouteSpecGrpcRouteMatchMetadataMatchArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert.setter
    def invert(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[pulumi.Input[RouteSpecGrpcRouteMatchMetadataMatchArgs]]: ...
    @match.setter
    def match(
        self, value: Optional[pulumi.Input[RouteSpecGrpcRouteMatchMetadataMatchArgs]]
    ): ...

class RouteSpecGrpcRouteMatchMetadataMatchArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    range: NotRequired[pulumi.Input[RouteSpecGrpcRouteMatchMetadataMatchRangeArgsDict]]
    regex: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RouteSpecGrpcRouteMatchMetadataMatchArgs:
    def __init__(
        __self__,
        *,
        exact: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        range: Optional[
            pulumi.Input[RouteSpecGrpcRouteMatchMetadataMatchRangeArgs]
        ] = ...,
        regex: Optional[pulumi.Input[_builtins.str]] = ...,
        suffix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def range(
        self,
    ) -> Optional[pulumi.Input[RouteSpecGrpcRouteMatchMetadataMatchRangeArgs]]: ...
    @range.setter
    def range(
        self,
        value: Optional[pulumi.Input[RouteSpecGrpcRouteMatchMetadataMatchRangeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex.setter
    def regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RouteSpecGrpcRouteMatchMetadataMatchRangeArgsDict(TypedDict):
    end: pulumi.Input[_builtins.int]
    start: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecGrpcRouteMatchMetadataMatchRangeArgs:
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

class RouteSpecGrpcRouteRetryPolicyArgsDict(TypedDict):
    max_retries: pulumi.Input[_builtins.int]
    per_retry_timeout: pulumi.Input[
        RouteSpecGrpcRouteRetryPolicyPerRetryTimeoutArgsDict
    ]
    grpc_retry_events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    http_retry_events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tcp_retry_events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RouteSpecGrpcRouteRetryPolicyArgs:
    def __init__(
        __self__,
        *,
        max_retries: pulumi.Input[_builtins.int],
        per_retry_timeout: pulumi.Input[
            RouteSpecGrpcRouteRetryPolicyPerRetryTimeoutArgs
        ],
        grpc_retry_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        http_retry_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tcp_retry_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> pulumi.Input[_builtins.int]: ...
    @max_retries.setter
    def max_retries(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="perRetryTimeout")
    def per_retry_timeout(
        self,
    ) -> pulumi.Input[RouteSpecGrpcRouteRetryPolicyPerRetryTimeoutArgs]: ...
    @per_retry_timeout.setter
    def per_retry_timeout(
        self, value: pulumi.Input[RouteSpecGrpcRouteRetryPolicyPerRetryTimeoutArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="grpcRetryEvents")
    def grpc_retry_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @grpc_retry_events.setter
    def grpc_retry_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpRetryEvents")
    def http_retry_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @http_retry_events.setter
    def http_retry_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tcpRetryEvents")
    def tcp_retry_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tcp_retry_events.setter
    def tcp_retry_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RouteSpecGrpcRouteRetryPolicyPerRetryTimeoutArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecGrpcRouteRetryPolicyPerRetryTimeoutArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class RouteSpecGrpcRouteTimeoutArgsDict(TypedDict):
    idle: NotRequired[pulumi.Input[RouteSpecGrpcRouteTimeoutIdleArgsDict]]
    per_request: NotRequired[pulumi.Input[RouteSpecGrpcRouteTimeoutPerRequestArgsDict]]

@pulumi.input_type
class RouteSpecGrpcRouteTimeoutArgs:
    def __init__(
        __self__,
        *,
        idle: Optional[pulumi.Input[RouteSpecGrpcRouteTimeoutIdleArgs]] = ...,
        per_request: Optional[
            pulumi.Input[RouteSpecGrpcRouteTimeoutPerRequestArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(self) -> Optional[pulumi.Input[RouteSpecGrpcRouteTimeoutIdleArgs]]: ...
    @idle.setter
    def idle(
        self, value: Optional[pulumi.Input[RouteSpecGrpcRouteTimeoutIdleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="perRequest")
    def per_request(
        self,
    ) -> Optional[pulumi.Input[RouteSpecGrpcRouteTimeoutPerRequestArgs]]: ...
    @per_request.setter
    def per_request(
        self, value: Optional[pulumi.Input[RouteSpecGrpcRouteTimeoutPerRequestArgs]]
    ): ...

class RouteSpecGrpcRouteTimeoutIdleArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecGrpcRouteTimeoutIdleArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class RouteSpecGrpcRouteTimeoutPerRequestArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecGrpcRouteTimeoutPerRequestArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class RouteSpecHttp2RouteArgsDict(TypedDict):
    action: pulumi.Input[RouteSpecHttp2RouteActionArgsDict]
    match: pulumi.Input[RouteSpecHttp2RouteMatchArgsDict]
    retry_policy: NotRequired[pulumi.Input[RouteSpecHttp2RouteRetryPolicyArgsDict]]
    timeout: NotRequired[pulumi.Input[RouteSpecHttp2RouteTimeoutArgsDict]]

@pulumi.input_type
class RouteSpecHttp2RouteArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[RouteSpecHttp2RouteActionArgs],
        match: pulumi.Input[RouteSpecHttp2RouteMatchArgs],
        retry_policy: Optional[pulumi.Input[RouteSpecHttp2RouteRetryPolicyArgs]] = ...,
        timeout: Optional[pulumi.Input[RouteSpecHttp2RouteTimeoutArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[RouteSpecHttp2RouteActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[RouteSpecHttp2RouteActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Input[RouteSpecHttp2RouteMatchArgs]: ...
    @match.setter
    def match(self, value: pulumi.Input[RouteSpecHttp2RouteMatchArgs]): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(
        self,
    ) -> Optional[pulumi.Input[RouteSpecHttp2RouteRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(
        self, value: Optional[pulumi.Input[RouteSpecHttp2RouteRetryPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[RouteSpecHttp2RouteTimeoutArgs]]: ...
    @timeout.setter
    def timeout(
        self, value: Optional[pulumi.Input[RouteSpecHttp2RouteTimeoutArgs]]
    ): ...

class RouteSpecHttp2RouteActionArgsDict(TypedDict):
    weighted_targets: pulumi.Input[
        Sequence[pulumi.Input[RouteSpecHttp2RouteActionWeightedTargetArgsDict]]
    ]

@pulumi.input_type
class RouteSpecHttp2RouteActionArgs:
    def __init__(
        __self__,
        *,
        weighted_targets: pulumi.Input[
            Sequence[pulumi.Input[RouteSpecHttp2RouteActionWeightedTargetArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weightedTargets")
    def weighted_targets(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[RouteSpecHttp2RouteActionWeightedTargetArgs]]
    ]: ...
    @weighted_targets.setter
    def weighted_targets(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[RouteSpecHttp2RouteActionWeightedTargetArgs]]
        ],
    ): ...

class RouteSpecHttp2RouteActionWeightedTargetArgsDict(TypedDict):
    virtual_node: pulumi.Input[_builtins.str]
    weight: pulumi.Input[_builtins.int]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RouteSpecHttp2RouteActionWeightedTargetArgs:
    def __init__(
        __self__,
        *,
        virtual_node: pulumi.Input[_builtins.str],
        weight: pulumi.Input[_builtins.int],
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_node.setter
    def virtual_node(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Input[_builtins.int]: ...
    @weight.setter
    def weight(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RouteSpecHttp2RouteMatchArgsDict(TypedDict):
    headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RouteSpecHttp2RouteMatchHeaderArgsDict]]]
    ]
    method: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[RouteSpecHttp2RouteMatchPathArgsDict]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    query_parameters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[RouteSpecHttp2RouteMatchQueryParameterArgsDict]]
        ]
    ]
    scheme: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RouteSpecHttp2RouteMatchArgs:
    def __init__(
        __self__,
        *,
        headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[RouteSpecHttp2RouteMatchHeaderArgs]]]
        ] = ...,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[RouteSpecHttp2RouteMatchPathArgs]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        query_parameters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RouteSpecHttp2RouteMatchQueryParameterArgs]]
            ]
        ] = ...,
        scheme: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RouteSpecHttp2RouteMatchHeaderArgs]]]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RouteSpecHttp2RouteMatchHeaderArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[RouteSpecHttp2RouteMatchPathArgs]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[RouteSpecHttp2RouteMatchPathArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RouteSpecHttp2RouteMatchQueryParameterArgs]]]
    ]: ...
    @query_parameters.setter
    def query_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RouteSpecHttp2RouteMatchQueryParameterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scheme.setter
    def scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RouteSpecHttp2RouteMatchHeaderArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    invert: NotRequired[pulumi.Input[_builtins.bool]]
    match: NotRequired[pulumi.Input[RouteSpecHttp2RouteMatchHeaderMatchArgsDict]]

@pulumi.input_type
class RouteSpecHttp2RouteMatchHeaderArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        invert: Optional[pulumi.Input[_builtins.bool]] = ...,
        match: Optional[pulumi.Input[RouteSpecHttp2RouteMatchHeaderMatchArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert.setter
    def invert(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[pulumi.Input[RouteSpecHttp2RouteMatchHeaderMatchArgs]]: ...
    @match.setter
    def match(
        self, value: Optional[pulumi.Input[RouteSpecHttp2RouteMatchHeaderMatchArgs]]
    ): ...

class RouteSpecHttp2RouteMatchHeaderMatchArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    range: NotRequired[pulumi.Input[RouteSpecHttp2RouteMatchHeaderMatchRangeArgsDict]]
    regex: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RouteSpecHttp2RouteMatchHeaderMatchArgs:
    def __init__(
        __self__,
        *,
        exact: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        range: Optional[
            pulumi.Input[RouteSpecHttp2RouteMatchHeaderMatchRangeArgs]
        ] = ...,
        regex: Optional[pulumi.Input[_builtins.str]] = ...,
        suffix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def range(
        self,
    ) -> Optional[pulumi.Input[RouteSpecHttp2RouteMatchHeaderMatchRangeArgs]]: ...
    @range.setter
    def range(
        self,
        value: Optional[pulumi.Input[RouteSpecHttp2RouteMatchHeaderMatchRangeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex.setter
    def regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RouteSpecHttp2RouteMatchHeaderMatchRangeArgsDict(TypedDict):
    end: pulumi.Input[_builtins.int]
    start: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecHttp2RouteMatchHeaderMatchRangeArgs:
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

class RouteSpecHttp2RouteMatchPathArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]
    regex: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RouteSpecHttp2RouteMatchPathArgs:
    def __init__(
        __self__,
        *,
        exact: Optional[pulumi.Input[_builtins.str]] = ...,
        regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex.setter
    def regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RouteSpecHttp2RouteMatchQueryParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    match: NotRequired[
        pulumi.Input[RouteSpecHttp2RouteMatchQueryParameterMatchArgsDict]
    ]

@pulumi.input_type
class RouteSpecHttp2RouteMatchQueryParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        match: Optional[
            pulumi.Input[RouteSpecHttp2RouteMatchQueryParameterMatchArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[pulumi.Input[RouteSpecHttp2RouteMatchQueryParameterMatchArgs]]: ...
    @match.setter
    def match(
        self,
        value: Optional[pulumi.Input[RouteSpecHttp2RouteMatchQueryParameterMatchArgs]],
    ): ...

class RouteSpecHttp2RouteMatchQueryParameterMatchArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RouteSpecHttp2RouteMatchQueryParameterMatchArgs:
    def __init__(
        __self__, *, exact: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RouteSpecHttp2RouteRetryPolicyArgsDict(TypedDict):
    max_retries: pulumi.Input[_builtins.int]
    per_retry_timeout: pulumi.Input[
        RouteSpecHttp2RouteRetryPolicyPerRetryTimeoutArgsDict
    ]
    http_retry_events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tcp_retry_events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RouteSpecHttp2RouteRetryPolicyArgs:
    def __init__(
        __self__,
        *,
        max_retries: pulumi.Input[_builtins.int],
        per_retry_timeout: pulumi.Input[
            RouteSpecHttp2RouteRetryPolicyPerRetryTimeoutArgs
        ],
        http_retry_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tcp_retry_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> pulumi.Input[_builtins.int]: ...
    @max_retries.setter
    def max_retries(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="perRetryTimeout")
    def per_retry_timeout(
        self,
    ) -> pulumi.Input[RouteSpecHttp2RouteRetryPolicyPerRetryTimeoutArgs]: ...
    @per_retry_timeout.setter
    def per_retry_timeout(
        self, value: pulumi.Input[RouteSpecHttp2RouteRetryPolicyPerRetryTimeoutArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpRetryEvents")
    def http_retry_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @http_retry_events.setter
    def http_retry_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tcpRetryEvents")
    def tcp_retry_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tcp_retry_events.setter
    def tcp_retry_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RouteSpecHttp2RouteRetryPolicyPerRetryTimeoutArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecHttp2RouteRetryPolicyPerRetryTimeoutArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class RouteSpecHttp2RouteTimeoutArgsDict(TypedDict):
    idle: NotRequired[pulumi.Input[RouteSpecHttp2RouteTimeoutIdleArgsDict]]
    per_request: NotRequired[pulumi.Input[RouteSpecHttp2RouteTimeoutPerRequestArgsDict]]

@pulumi.input_type
class RouteSpecHttp2RouteTimeoutArgs:
    def __init__(
        __self__,
        *,
        idle: Optional[pulumi.Input[RouteSpecHttp2RouteTimeoutIdleArgs]] = ...,
        per_request: Optional[
            pulumi.Input[RouteSpecHttp2RouteTimeoutPerRequestArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(self) -> Optional[pulumi.Input[RouteSpecHttp2RouteTimeoutIdleArgs]]: ...
    @idle.setter
    def idle(
        self, value: Optional[pulumi.Input[RouteSpecHttp2RouteTimeoutIdleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="perRequest")
    def per_request(
        self,
    ) -> Optional[pulumi.Input[RouteSpecHttp2RouteTimeoutPerRequestArgs]]: ...
    @per_request.setter
    def per_request(
        self, value: Optional[pulumi.Input[RouteSpecHttp2RouteTimeoutPerRequestArgs]]
    ): ...

class RouteSpecHttp2RouteTimeoutIdleArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecHttp2RouteTimeoutIdleArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class RouteSpecHttp2RouteTimeoutPerRequestArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecHttp2RouteTimeoutPerRequestArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class RouteSpecHttpRouteArgsDict(TypedDict):
    action: pulumi.Input[RouteSpecHttpRouteActionArgsDict]
    match: pulumi.Input[RouteSpecHttpRouteMatchArgsDict]
    retry_policy: NotRequired[pulumi.Input[RouteSpecHttpRouteRetryPolicyArgsDict]]
    timeout: NotRequired[pulumi.Input[RouteSpecHttpRouteTimeoutArgsDict]]

@pulumi.input_type
class RouteSpecHttpRouteArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[RouteSpecHttpRouteActionArgs],
        match: pulumi.Input[RouteSpecHttpRouteMatchArgs],
        retry_policy: Optional[pulumi.Input[RouteSpecHttpRouteRetryPolicyArgs]] = ...,
        timeout: Optional[pulumi.Input[RouteSpecHttpRouteTimeoutArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[RouteSpecHttpRouteActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[RouteSpecHttpRouteActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Input[RouteSpecHttpRouteMatchArgs]: ...
    @match.setter
    def match(self, value: pulumi.Input[RouteSpecHttpRouteMatchArgs]): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(
        self,
    ) -> Optional[pulumi.Input[RouteSpecHttpRouteRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(
        self, value: Optional[pulumi.Input[RouteSpecHttpRouteRetryPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[RouteSpecHttpRouteTimeoutArgs]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[RouteSpecHttpRouteTimeoutArgs]]): ...

class RouteSpecHttpRouteActionArgsDict(TypedDict):
    weighted_targets: pulumi.Input[
        Sequence[pulumi.Input[RouteSpecHttpRouteActionWeightedTargetArgsDict]]
    ]

@pulumi.input_type
class RouteSpecHttpRouteActionArgs:
    def __init__(
        __self__,
        *,
        weighted_targets: pulumi.Input[
            Sequence[pulumi.Input[RouteSpecHttpRouteActionWeightedTargetArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weightedTargets")
    def weighted_targets(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[RouteSpecHttpRouteActionWeightedTargetArgs]]
    ]: ...
    @weighted_targets.setter
    def weighted_targets(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[RouteSpecHttpRouteActionWeightedTargetArgs]]
        ],
    ): ...

class RouteSpecHttpRouteActionWeightedTargetArgsDict(TypedDict):
    virtual_node: pulumi.Input[_builtins.str]
    weight: pulumi.Input[_builtins.int]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RouteSpecHttpRouteActionWeightedTargetArgs:
    def __init__(
        __self__,
        *,
        virtual_node: pulumi.Input[_builtins.str],
        weight: pulumi.Input[_builtins.int],
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_node.setter
    def virtual_node(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Input[_builtins.int]: ...
    @weight.setter
    def weight(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RouteSpecHttpRouteMatchArgsDict(TypedDict):
    headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[RouteSpecHttpRouteMatchHeaderArgsDict]]]
    ]
    method: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[RouteSpecHttpRouteMatchPathArgsDict]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    query_parameters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[RouteSpecHttpRouteMatchQueryParameterArgsDict]]
        ]
    ]
    scheme: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RouteSpecHttpRouteMatchArgs:
    def __init__(
        __self__,
        *,
        headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[RouteSpecHttpRouteMatchHeaderArgs]]]
        ] = ...,
        method: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[RouteSpecHttpRouteMatchPathArgs]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        query_parameters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RouteSpecHttpRouteMatchQueryParameterArgs]]
            ]
        ] = ...,
        scheme: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RouteSpecHttpRouteMatchHeaderArgs]]]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RouteSpecHttpRouteMatchHeaderArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @method.setter
    def method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[RouteSpecHttpRouteMatchPathArgs]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[RouteSpecHttpRouteMatchPathArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RouteSpecHttpRouteMatchQueryParameterArgs]]]
    ]: ...
    @query_parameters.setter
    def query_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RouteSpecHttpRouteMatchQueryParameterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scheme.setter
    def scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RouteSpecHttpRouteMatchHeaderArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    invert: NotRequired[pulumi.Input[_builtins.bool]]
    match: NotRequired[pulumi.Input[RouteSpecHttpRouteMatchHeaderMatchArgsDict]]

@pulumi.input_type
class RouteSpecHttpRouteMatchHeaderArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        invert: Optional[pulumi.Input[_builtins.bool]] = ...,
        match: Optional[pulumi.Input[RouteSpecHttpRouteMatchHeaderMatchArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert.setter
    def invert(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[pulumi.Input[RouteSpecHttpRouteMatchHeaderMatchArgs]]: ...
    @match.setter
    def match(
        self, value: Optional[pulumi.Input[RouteSpecHttpRouteMatchHeaderMatchArgs]]
    ): ...

class RouteSpecHttpRouteMatchHeaderMatchArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    range: NotRequired[pulumi.Input[RouteSpecHttpRouteMatchHeaderMatchRangeArgsDict]]
    regex: NotRequired[pulumi.Input[_builtins.str]]
    suffix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RouteSpecHttpRouteMatchHeaderMatchArgs:
    def __init__(
        __self__,
        *,
        exact: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        range: Optional[
            pulumi.Input[RouteSpecHttpRouteMatchHeaderMatchRangeArgs]
        ] = ...,
        regex: Optional[pulumi.Input[_builtins.str]] = ...,
        suffix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def range(
        self,
    ) -> Optional[pulumi.Input[RouteSpecHttpRouteMatchHeaderMatchRangeArgs]]: ...
    @range.setter
    def range(
        self, value: Optional[pulumi.Input[RouteSpecHttpRouteMatchHeaderMatchRangeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex.setter
    def regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @suffix.setter
    def suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RouteSpecHttpRouteMatchHeaderMatchRangeArgsDict(TypedDict):
    end: pulumi.Input[_builtins.int]
    start: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecHttpRouteMatchHeaderMatchRangeArgs:
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

class RouteSpecHttpRouteMatchPathArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]
    regex: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RouteSpecHttpRouteMatchPathArgs:
    def __init__(
        __self__,
        *,
        exact: Optional[pulumi.Input[_builtins.str]] = ...,
        regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex.setter
    def regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RouteSpecHttpRouteMatchQueryParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    match: NotRequired[pulumi.Input[RouteSpecHttpRouteMatchQueryParameterMatchArgsDict]]

@pulumi.input_type
class RouteSpecHttpRouteMatchQueryParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        match: Optional[
            pulumi.Input[RouteSpecHttpRouteMatchQueryParameterMatchArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[pulumi.Input[RouteSpecHttpRouteMatchQueryParameterMatchArgs]]: ...
    @match.setter
    def match(
        self,
        value: Optional[pulumi.Input[RouteSpecHttpRouteMatchQueryParameterMatchArgs]],
    ): ...

class RouteSpecHttpRouteMatchQueryParameterMatchArgsDict(TypedDict):
    exact: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RouteSpecHttpRouteMatchQueryParameterMatchArgs:
    def __init__(
        __self__, *, exact: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exact.setter
    def exact(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RouteSpecHttpRouteRetryPolicyArgsDict(TypedDict):
    max_retries: pulumi.Input[_builtins.int]
    per_retry_timeout: pulumi.Input[
        RouteSpecHttpRouteRetryPolicyPerRetryTimeoutArgsDict
    ]
    http_retry_events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tcp_retry_events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RouteSpecHttpRouteRetryPolicyArgs:
    def __init__(
        __self__,
        *,
        max_retries: pulumi.Input[_builtins.int],
        per_retry_timeout: pulumi.Input[
            RouteSpecHttpRouteRetryPolicyPerRetryTimeoutArgs
        ],
        http_retry_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tcp_retry_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> pulumi.Input[_builtins.int]: ...
    @max_retries.setter
    def max_retries(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="perRetryTimeout")
    def per_retry_timeout(
        self,
    ) -> pulumi.Input[RouteSpecHttpRouteRetryPolicyPerRetryTimeoutArgs]: ...
    @per_retry_timeout.setter
    def per_retry_timeout(
        self, value: pulumi.Input[RouteSpecHttpRouteRetryPolicyPerRetryTimeoutArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpRetryEvents")
    def http_retry_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @http_retry_events.setter
    def http_retry_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tcpRetryEvents")
    def tcp_retry_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tcp_retry_events.setter
    def tcp_retry_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RouteSpecHttpRouteRetryPolicyPerRetryTimeoutArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecHttpRouteRetryPolicyPerRetryTimeoutArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class RouteSpecHttpRouteTimeoutArgsDict(TypedDict):
    idle: NotRequired[pulumi.Input[RouteSpecHttpRouteTimeoutIdleArgsDict]]
    per_request: NotRequired[pulumi.Input[RouteSpecHttpRouteTimeoutPerRequestArgsDict]]

@pulumi.input_type
class RouteSpecHttpRouteTimeoutArgs:
    def __init__(
        __self__,
        *,
        idle: Optional[pulumi.Input[RouteSpecHttpRouteTimeoutIdleArgs]] = ...,
        per_request: Optional[
            pulumi.Input[RouteSpecHttpRouteTimeoutPerRequestArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(self) -> Optional[pulumi.Input[RouteSpecHttpRouteTimeoutIdleArgs]]: ...
    @idle.setter
    def idle(
        self, value: Optional[pulumi.Input[RouteSpecHttpRouteTimeoutIdleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="perRequest")
    def per_request(
        self,
    ) -> Optional[pulumi.Input[RouteSpecHttpRouteTimeoutPerRequestArgs]]: ...
    @per_request.setter
    def per_request(
        self, value: Optional[pulumi.Input[RouteSpecHttpRouteTimeoutPerRequestArgs]]
    ): ...

class RouteSpecHttpRouteTimeoutIdleArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecHttpRouteTimeoutIdleArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class RouteSpecHttpRouteTimeoutPerRequestArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecHttpRouteTimeoutPerRequestArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class RouteSpecTcpRouteArgsDict(TypedDict):
    action: pulumi.Input[RouteSpecTcpRouteActionArgsDict]
    match: NotRequired[pulumi.Input[RouteSpecTcpRouteMatchArgsDict]]
    timeout: NotRequired[pulumi.Input[RouteSpecTcpRouteTimeoutArgsDict]]

@pulumi.input_type
class RouteSpecTcpRouteArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[RouteSpecTcpRouteActionArgs],
        match: Optional[pulumi.Input[RouteSpecTcpRouteMatchArgs]] = ...,
        timeout: Optional[pulumi.Input[RouteSpecTcpRouteTimeoutArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[RouteSpecTcpRouteActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[RouteSpecTcpRouteActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[pulumi.Input[RouteSpecTcpRouteMatchArgs]]: ...
    @match.setter
    def match(self, value: Optional[pulumi.Input[RouteSpecTcpRouteMatchArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[RouteSpecTcpRouteTimeoutArgs]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[RouteSpecTcpRouteTimeoutArgs]]): ...

class RouteSpecTcpRouteActionArgsDict(TypedDict):
    weighted_targets: pulumi.Input[
        Sequence[pulumi.Input[RouteSpecTcpRouteActionWeightedTargetArgsDict]]
    ]

@pulumi.input_type
class RouteSpecTcpRouteActionArgs:
    def __init__(
        __self__,
        *,
        weighted_targets: pulumi.Input[
            Sequence[pulumi.Input[RouteSpecTcpRouteActionWeightedTargetArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weightedTargets")
    def weighted_targets(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[RouteSpecTcpRouteActionWeightedTargetArgs]]
    ]: ...
    @weighted_targets.setter
    def weighted_targets(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[RouteSpecTcpRouteActionWeightedTargetArgs]]
        ],
    ): ...

class RouteSpecTcpRouteActionWeightedTargetArgsDict(TypedDict):
    virtual_node: pulumi.Input[_builtins.str]
    weight: pulumi.Input[_builtins.int]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RouteSpecTcpRouteActionWeightedTargetArgs:
    def __init__(
        __self__,
        *,
        virtual_node: pulumi.Input[_builtins.str],
        weight: pulumi.Input[_builtins.int],
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_node.setter
    def virtual_node(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Input[_builtins.int]: ...
    @weight.setter
    def weight(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RouteSpecTcpRouteMatchArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RouteSpecTcpRouteMatchArgs:
    def __init__(
        __self__, *, port: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RouteSpecTcpRouteTimeoutArgsDict(TypedDict):
    idle: NotRequired[pulumi.Input[RouteSpecTcpRouteTimeoutIdleArgsDict]]

@pulumi.input_type
class RouteSpecTcpRouteTimeoutArgs:
    def __init__(
        __self__,
        *,
        idle: Optional[pulumi.Input[RouteSpecTcpRouteTimeoutIdleArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(self) -> Optional[pulumi.Input[RouteSpecTcpRouteTimeoutIdleArgs]]: ...
    @idle.setter
    def idle(self, value: Optional[pulumi.Input[RouteSpecTcpRouteTimeoutIdleArgs]]): ...

class RouteSpecTcpRouteTimeoutIdleArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class RouteSpecTcpRouteTimeoutIdleArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class VirtualGatewaySpecArgsDict(TypedDict):
    listeners: pulumi.Input[Sequence[pulumi.Input[VirtualGatewaySpecListenerArgsDict]]]
    backend_defaults: NotRequired[
        pulumi.Input[VirtualGatewaySpecBackendDefaultsArgsDict]
    ]
    logging: NotRequired[pulumi.Input[VirtualGatewaySpecLoggingArgsDict]]

@pulumi.input_type
class VirtualGatewaySpecArgs:
    def __init__(
        __self__,
        *,
        listeners: pulumi.Input[Sequence[pulumi.Input[VirtualGatewaySpecListenerArgs]]],
        backend_defaults: Optional[
            pulumi.Input[VirtualGatewaySpecBackendDefaultsArgs]
        ] = ...,
        logging: Optional[pulumi.Input[VirtualGatewaySpecLoggingArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def listeners(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[VirtualGatewaySpecListenerArgs]]]: ...
    @listeners.setter
    def listeners(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[VirtualGatewaySpecListenerArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="backendDefaults")
    def backend_defaults(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecBackendDefaultsArgs]]: ...
    @backend_defaults.setter
    def backend_defaults(
        self, value: Optional[pulumi.Input[VirtualGatewaySpecBackendDefaultsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input[VirtualGatewaySpecLoggingArgs]]: ...
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[VirtualGatewaySpecLoggingArgs]]): ...

class VirtualGatewaySpecBackendDefaultsArgsDict(TypedDict):
    client_policy: NotRequired[
        pulumi.Input[VirtualGatewaySpecBackendDefaultsClientPolicyArgsDict]
    ]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsArgs:
    def __init__(
        __self__,
        *,
        client_policy: Optional[
            pulumi.Input[VirtualGatewaySpecBackendDefaultsClientPolicyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientPolicy")
    def client_policy(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecBackendDefaultsClientPolicyArgs]]: ...
    @client_policy.setter
    def client_policy(
        self,
        value: Optional[
            pulumi.Input[VirtualGatewaySpecBackendDefaultsClientPolicyArgs]
        ],
    ): ...

class VirtualGatewaySpecBackendDefaultsClientPolicyArgsDict(TypedDict):
    tls: NotRequired[
        pulumi.Input[VirtualGatewaySpecBackendDefaultsClientPolicyTlsArgsDict]
    ]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsClientPolicyArgs:
    def __init__(
        __self__,
        *,
        tls: Optional[
            pulumi.Input[VirtualGatewaySpecBackendDefaultsClientPolicyTlsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tls(
        self,
    ) -> Optional[
        pulumi.Input[VirtualGatewaySpecBackendDefaultsClientPolicyTlsArgs]
    ]: ...
    @tls.setter
    def tls(
        self,
        value: Optional[
            pulumi.Input[VirtualGatewaySpecBackendDefaultsClientPolicyTlsArgs]
        ],
    ): ...

class VirtualGatewaySpecBackendDefaultsClientPolicyTlsArgsDict(TypedDict):
    validation: pulumi.Input[
        VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationArgsDict
    ]
    certificate: NotRequired[
        pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateArgsDict
        ]
    ]
    enforce: NotRequired[pulumi.Input[_builtins.bool]]
    ports: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsArgs:
    def __init__(
        __self__,
        *,
        validation: pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationArgs
        ],
        certificate: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateArgs
            ]
        ] = ...,
        enforce: Optional[pulumi.Input[_builtins.bool]] = ...,
        ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> pulumi.Input[
        VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationArgs
    ]: ...
    @validation.setter
    def validation(
        self,
        value: pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def certificate(
        self,
    ) -> Optional[
        pulumi.Input[VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateArgs]
    ]: ...
    @certificate.setter
    def certificate(
        self,
        value: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enforce.setter
    def enforce(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def ports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @ports.setter
    def ports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateArgsDict(TypedDict):
    file: NotRequired[
        pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFileArgsDict
        ]
    ]
    sds: NotRequired[
        pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSdsArgsDict
        ]
    ]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateArgs:
    def __init__(
        __self__,
        *,
        file: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFileArgs
            ]
        ] = ...,
        sds: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSdsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        pulumi.Input[VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSdsArgs]
    ]: ...
    @sds.setter
    def sds(
        self,
        value: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSdsArgs
            ]
        ],
    ): ...

class VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFileArgsDict(
    TypedDict
):
    certificate_chain: pulumi.Input[_builtins.str]
    private_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFileArgs:
    def __init__(
        __self__,
        *,
        certificate_chain: pulumi.Input[_builtins.str],
        private_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[_builtins.str]: ...
    @private_key.setter
    def private_key(self, value: pulumi.Input[_builtins.str]): ...

class VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSdsArgsDict(TypedDict):
    secret_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSdsArgs:
    def __init__(__self__, *, secret_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): ...

class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationArgsDict(TypedDict):
    trust: pulumi.Input[
        VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustArgsDict
    ]
    subject_alternative_names: NotRequired[
        pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesArgsDict
        ]
    ]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationArgs:
    def __init__(
        __self__,
        *,
        trust: pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustArgs
        ],
        subject_alternative_names: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trust(
        self,
    ) -> pulumi.Input[
        VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustArgs
    ]: ...
    @trust.setter
    def trust(
        self,
        value: pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesArgs
        ]
    ]: ...
    @subject_alternative_names.setter
    def subject_alternative_names(
        self,
        value: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesArgs
            ]
        ],
    ): ...

class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesArgsDict(
    TypedDict
):
    match: pulumi.Input[
        VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchArgsDict
    ]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesArgs:
    def __init__(
        __self__,
        *,
        match: pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> pulumi.Input[
        VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchArgs
    ]: ...
    @match.setter
    def match(
        self,
        value: pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchArgs
        ],
    ): ...

class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchArgsDict(
    TypedDict
):
    exacts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchArgs:
    def __init__(
        __self__, *, exacts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @exacts.setter
    def exacts(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustArgsDict(
    TypedDict
):
    acm: NotRequired[
        pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcmArgsDict
        ]
    ]
    file: NotRequired[
        pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFileArgsDict
        ]
    ]
    sds: NotRequired[
        pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSdsArgsDict
        ]
    ]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustArgs:
    def __init__(
        __self__,
        *,
        acm: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcmArgs
            ]
        ] = ...,
        file: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFileArgs
            ]
        ] = ...,
        sds: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSdsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acm(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcmArgs
        ]
    ]: ...
    @acm.setter
    def acm(
        self,
        value: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcmArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSdsArgs
        ]
    ]: ...
    @sds.setter
    def sds(
        self,
        value: Optional[
            pulumi.Input[
                VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSdsArgs
            ]
        ],
    ): ...

class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcmArgsDict(
    TypedDict
):
    certificate_authority_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcmArgs:
    def __init__(
        __self__,
        *,
        certificate_authority_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArns")
    def certificate_authority_arns(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @certificate_authority_arns.setter
    def certificate_authority_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFileArgsDict(
    TypedDict
):
    certificate_chain: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFileArgs:
    def __init__(
        __self__, *, certificate_chain: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: pulumi.Input[_builtins.str]): ...

class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSdsArgsDict(
    TypedDict
):
    secret_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSdsArgs:
    def __init__(__self__, *, secret_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): ...

class VirtualGatewaySpecListenerArgsDict(TypedDict):
    port_mapping: pulumi.Input[VirtualGatewaySpecListenerPortMappingArgsDict]
    connection_pool: NotRequired[
        pulumi.Input[VirtualGatewaySpecListenerConnectionPoolArgsDict]
    ]
    health_check: NotRequired[
        pulumi.Input[VirtualGatewaySpecListenerHealthCheckArgsDict]
    ]
    tls: NotRequired[pulumi.Input[VirtualGatewaySpecListenerTlsArgsDict]]

@pulumi.input_type
class VirtualGatewaySpecListenerArgs:
    def __init__(
        __self__,
        *,
        port_mapping: pulumi.Input[VirtualGatewaySpecListenerPortMappingArgs],
        connection_pool: Optional[
            pulumi.Input[VirtualGatewaySpecListenerConnectionPoolArgs]
        ] = ...,
        health_check: Optional[
            pulumi.Input[VirtualGatewaySpecListenerHealthCheckArgs]
        ] = ...,
        tls: Optional[pulumi.Input[VirtualGatewaySpecListenerTlsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="portMapping")
    def port_mapping(
        self,
    ) -> pulumi.Input[VirtualGatewaySpecListenerPortMappingArgs]: ...
    @port_mapping.setter
    def port_mapping(
        self, value: pulumi.Input[VirtualGatewaySpecListenerPortMappingArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionPool")
    def connection_pool(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecListenerConnectionPoolArgs]]: ...
    @connection_pool.setter
    def connection_pool(
        self,
        value: Optional[pulumi.Input[VirtualGatewaySpecListenerConnectionPoolArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecListenerHealthCheckArgs]]: ...
    @health_check.setter
    def health_check(
        self, value: Optional[pulumi.Input[VirtualGatewaySpecListenerHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[pulumi.Input[VirtualGatewaySpecListenerTlsArgs]]: ...
    @tls.setter
    def tls(self, value: Optional[pulumi.Input[VirtualGatewaySpecListenerTlsArgs]]): ...

class VirtualGatewaySpecListenerConnectionPoolArgsDict(TypedDict):
    grpc: NotRequired[
        pulumi.Input[VirtualGatewaySpecListenerConnectionPoolGrpcArgsDict]
    ]
    http: NotRequired[
        pulumi.Input[VirtualGatewaySpecListenerConnectionPoolHttpArgsDict]
    ]
    http2: NotRequired[
        pulumi.Input[VirtualGatewaySpecListenerConnectionPoolHttp2ArgsDict]
    ]

@pulumi.input_type
class VirtualGatewaySpecListenerConnectionPoolArgs:
    def __init__(
        __self__,
        *,
        grpc: Optional[
            pulumi.Input[VirtualGatewaySpecListenerConnectionPoolGrpcArgs]
        ] = ...,
        http: Optional[
            pulumi.Input[VirtualGatewaySpecListenerConnectionPoolHttpArgs]
        ] = ...,
        http2: Optional[
            pulumi.Input[VirtualGatewaySpecListenerConnectionPoolHttp2Args]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecListenerConnectionPoolGrpcArgs]]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[pulumi.Input[VirtualGatewaySpecListenerConnectionPoolGrpcArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def http(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecListenerConnectionPoolHttpArgs]]: ...
    @http.setter
    def http(
        self,
        value: Optional[pulumi.Input[VirtualGatewaySpecListenerConnectionPoolHttpArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def http2(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecListenerConnectionPoolHttp2Args]]: ...
    @http2.setter
    def http2(
        self,
        value: Optional[
            pulumi.Input[VirtualGatewaySpecListenerConnectionPoolHttp2Args]
        ],
    ): ...

class VirtualGatewaySpecListenerConnectionPoolGrpcArgsDict(TypedDict):
    max_requests: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualGatewaySpecListenerConnectionPoolGrpcArgs:
    def __init__(__self__, *, max_requests: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequests")
    def max_requests(self) -> pulumi.Input[_builtins.int]: ...
    @max_requests.setter
    def max_requests(self, value: pulumi.Input[_builtins.int]): ...

class VirtualGatewaySpecListenerConnectionPoolHttp2ArgsDict(TypedDict):
    max_requests: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualGatewaySpecListenerConnectionPoolHttp2Args:
    def __init__(__self__, *, max_requests: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequests")
    def max_requests(self) -> pulumi.Input[_builtins.int]: ...
    @max_requests.setter
    def max_requests(self, value: pulumi.Input[_builtins.int]): ...

class VirtualGatewaySpecListenerConnectionPoolHttpArgsDict(TypedDict):
    max_connections: pulumi.Input[_builtins.int]
    max_pending_requests: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class VirtualGatewaySpecListenerConnectionPoolHttpArgs:
    def __init__(
        __self__,
        *,
        max_connections: pulumi.Input[_builtins.int],
        max_pending_requests: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> pulumi.Input[_builtins.int]: ...
    @max_connections.setter
    def max_connections(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maxPendingRequests")
    def max_pending_requests(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pending_requests.setter
    def max_pending_requests(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class VirtualGatewaySpecListenerHealthCheckArgsDict(TypedDict):
    healthy_threshold: pulumi.Input[_builtins.int]
    interval_millis: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]
    timeout_millis: pulumi.Input[_builtins.int]
    unhealthy_threshold: pulumi.Input[_builtins.int]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class VirtualGatewaySpecListenerHealthCheckArgs:
    def __init__(
        __self__,
        *,
        healthy_threshold: pulumi.Input[_builtins.int],
        interval_millis: pulumi.Input[_builtins.int],
        protocol: pulumi.Input[_builtins.str],
        timeout_millis: pulumi.Input[_builtins.int],
        unhealthy_threshold: pulumi.Input[_builtins.int],
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> pulumi.Input[_builtins.int]: ...
    @healthy_threshold.setter
    def healthy_threshold(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="intervalMillis")
    def interval_millis(self) -> pulumi.Input[_builtins.int]: ...
    @interval_millis.setter
    def interval_millis(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMillis")
    def timeout_millis(self) -> pulumi.Input[_builtins.int]: ...
    @timeout_millis.setter
    def timeout_millis(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> pulumi.Input[_builtins.int]: ...
    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class VirtualGatewaySpecListenerPortMappingArgsDict(TypedDict):
    port: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualGatewaySpecListenerPortMappingArgs:
    def __init__(
        __self__,
        *,
        port: pulumi.Input[_builtins.int],
        protocol: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): ...

class VirtualGatewaySpecListenerTlsArgsDict(TypedDict):
    certificate: pulumi.Input[VirtualGatewaySpecListenerTlsCertificateArgsDict]
    mode: pulumi.Input[_builtins.str]
    validation: NotRequired[
        pulumi.Input[VirtualGatewaySpecListenerTlsValidationArgsDict]
    ]

@pulumi.input_type
class VirtualGatewaySpecListenerTlsArgs:
    def __init__(
        __self__,
        *,
        certificate: pulumi.Input[VirtualGatewaySpecListenerTlsCertificateArgs],
        mode: pulumi.Input[_builtins.str],
        validation: Optional[
            pulumi.Input[VirtualGatewaySpecListenerTlsValidationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificate(
        self,
    ) -> pulumi.Input[VirtualGatewaySpecListenerTlsCertificateArgs]: ...
    @certificate.setter
    def certificate(
        self, value: pulumi.Input[VirtualGatewaySpecListenerTlsCertificateArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecListenerTlsValidationArgs]]: ...
    @validation.setter
    def validation(
        self, value: Optional[pulumi.Input[VirtualGatewaySpecListenerTlsValidationArgs]]
    ): ...

class VirtualGatewaySpecListenerTlsCertificateArgsDict(TypedDict):
    acm: NotRequired[pulumi.Input[VirtualGatewaySpecListenerTlsCertificateAcmArgsDict]]
    file: NotRequired[
        pulumi.Input[VirtualGatewaySpecListenerTlsCertificateFileArgsDict]
    ]
    sds: NotRequired[pulumi.Input[VirtualGatewaySpecListenerTlsCertificateSdsArgsDict]]

@pulumi.input_type
class VirtualGatewaySpecListenerTlsCertificateArgs:
    def __init__(
        __self__,
        *,
        acm: Optional[
            pulumi.Input[VirtualGatewaySpecListenerTlsCertificateAcmArgs]
        ] = ...,
        file: Optional[
            pulumi.Input[VirtualGatewaySpecListenerTlsCertificateFileArgs]
        ] = ...,
        sds: Optional[
            pulumi.Input[VirtualGatewaySpecListenerTlsCertificateSdsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acm(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecListenerTlsCertificateAcmArgs]]: ...
    @acm.setter
    def acm(
        self,
        value: Optional[pulumi.Input[VirtualGatewaySpecListenerTlsCertificateAcmArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecListenerTlsCertificateFileArgs]]: ...
    @file.setter
    def file(
        self,
        value: Optional[pulumi.Input[VirtualGatewaySpecListenerTlsCertificateFileArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecListenerTlsCertificateSdsArgs]]: ...
    @sds.setter
    def sds(
        self,
        value: Optional[pulumi.Input[VirtualGatewaySpecListenerTlsCertificateSdsArgs]],
    ): ...

class VirtualGatewaySpecListenerTlsCertificateAcmArgsDict(TypedDict):
    certificate_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualGatewaySpecListenerTlsCertificateAcmArgs:
    def __init__(__self__, *, certificate_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: pulumi.Input[_builtins.str]): ...

class VirtualGatewaySpecListenerTlsCertificateFileArgsDict(TypedDict):
    certificate_chain: pulumi.Input[_builtins.str]
    private_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualGatewaySpecListenerTlsCertificateFileArgs:
    def __init__(
        __self__,
        *,
        certificate_chain: pulumi.Input[_builtins.str],
        private_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[_builtins.str]: ...
    @private_key.setter
    def private_key(self, value: pulumi.Input[_builtins.str]): ...

class VirtualGatewaySpecListenerTlsCertificateSdsArgsDict(TypedDict):
    secret_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualGatewaySpecListenerTlsCertificateSdsArgs:
    def __init__(__self__, *, secret_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): ...

class VirtualGatewaySpecListenerTlsValidationArgsDict(TypedDict):
    trust: pulumi.Input[VirtualGatewaySpecListenerTlsValidationTrustArgsDict]
    subject_alternative_names: NotRequired[
        pulumi.Input[
            VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesArgsDict
        ]
    ]

@pulumi.input_type
class VirtualGatewaySpecListenerTlsValidationArgs:
    def __init__(
        __self__,
        *,
        trust: pulumi.Input[VirtualGatewaySpecListenerTlsValidationTrustArgs],
        subject_alternative_names: Optional[
            pulumi.Input[
                VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trust(
        self,
    ) -> pulumi.Input[VirtualGatewaySpecListenerTlsValidationTrustArgs]: ...
    @trust.setter
    def trust(
        self, value: pulumi.Input[VirtualGatewaySpecListenerTlsValidationTrustArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Optional[
        pulumi.Input[VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesArgs]
    ]: ...
    @subject_alternative_names.setter
    def subject_alternative_names(
        self,
        value: Optional[
            pulumi.Input[
                VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesArgs
            ]
        ],
    ): ...

class VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesArgsDict(TypedDict):
    match: pulumi.Input[
        VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatchArgsDict
    ]

@pulumi.input_type
class VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesArgs:
    def __init__(
        __self__,
        *,
        match: pulumi.Input[
            VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatchArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> pulumi.Input[
        VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatchArgs
    ]: ...
    @match.setter
    def match(
        self,
        value: pulumi.Input[
            VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatchArgs
        ],
    ): ...

class VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatchArgsDict(
    TypedDict
):
    exacts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatchArgs:
    def __init__(
        __self__, *, exacts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @exacts.setter
    def exacts(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class VirtualGatewaySpecListenerTlsValidationTrustArgsDict(TypedDict):
    file: NotRequired[
        pulumi.Input[VirtualGatewaySpecListenerTlsValidationTrustFileArgsDict]
    ]
    sds: NotRequired[
        pulumi.Input[VirtualGatewaySpecListenerTlsValidationTrustSdsArgsDict]
    ]

@pulumi.input_type
class VirtualGatewaySpecListenerTlsValidationTrustArgs:
    def __init__(
        __self__,
        *,
        file: Optional[
            pulumi.Input[VirtualGatewaySpecListenerTlsValidationTrustFileArgs]
        ] = ...,
        sds: Optional[
            pulumi.Input[VirtualGatewaySpecListenerTlsValidationTrustSdsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[VirtualGatewaySpecListenerTlsValidationTrustFileArgs]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[VirtualGatewaySpecListenerTlsValidationTrustFileArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        pulumi.Input[VirtualGatewaySpecListenerTlsValidationTrustSdsArgs]
    ]: ...
    @sds.setter
    def sds(
        self,
        value: Optional[
            pulumi.Input[VirtualGatewaySpecListenerTlsValidationTrustSdsArgs]
        ],
    ): ...

class VirtualGatewaySpecListenerTlsValidationTrustFileArgsDict(TypedDict):
    certificate_chain: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualGatewaySpecListenerTlsValidationTrustFileArgs:
    def __init__(
        __self__, *, certificate_chain: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: pulumi.Input[_builtins.str]): ...

class VirtualGatewaySpecListenerTlsValidationTrustSdsArgsDict(TypedDict):
    secret_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualGatewaySpecListenerTlsValidationTrustSdsArgs:
    def __init__(__self__, *, secret_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): ...

class VirtualGatewaySpecLoggingArgsDict(TypedDict):
    access_log: NotRequired[pulumi.Input[VirtualGatewaySpecLoggingAccessLogArgsDict]]

@pulumi.input_type
class VirtualGatewaySpecLoggingArgs:
    def __init__(
        __self__,
        *,
        access_log: Optional[
            pulumi.Input[VirtualGatewaySpecLoggingAccessLogArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLog")
    def access_log(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecLoggingAccessLogArgs]]: ...
    @access_log.setter
    def access_log(
        self, value: Optional[pulumi.Input[VirtualGatewaySpecLoggingAccessLogArgs]]
    ): ...

class VirtualGatewaySpecLoggingAccessLogArgsDict(TypedDict):
    file: NotRequired[pulumi.Input[VirtualGatewaySpecLoggingAccessLogFileArgsDict]]

@pulumi.input_type
class VirtualGatewaySpecLoggingAccessLogArgs:
    def __init__(
        __self__,
        *,
        file: Optional[pulumi.Input[VirtualGatewaySpecLoggingAccessLogFileArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecLoggingAccessLogFileArgs]]: ...
    @file.setter
    def file(
        self, value: Optional[pulumi.Input[VirtualGatewaySpecLoggingAccessLogFileArgs]]
    ): ...

class VirtualGatewaySpecLoggingAccessLogFileArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    format: NotRequired[
        pulumi.Input[VirtualGatewaySpecLoggingAccessLogFileFormatArgsDict]
    ]

@pulumi.input_type
class VirtualGatewaySpecLoggingAccessLogFileArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        format: Optional[
            pulumi.Input[VirtualGatewaySpecLoggingAccessLogFileFormatArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def format(
        self,
    ) -> Optional[pulumi.Input[VirtualGatewaySpecLoggingAccessLogFileFormatArgs]]: ...
    @format.setter
    def format(
        self,
        value: Optional[pulumi.Input[VirtualGatewaySpecLoggingAccessLogFileFormatArgs]],
    ): ...

class VirtualGatewaySpecLoggingAccessLogFileFormatArgsDict(TypedDict):
    jsons: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[VirtualGatewaySpecLoggingAccessLogFileFormatJsonArgsDict]
            ]
        ]
    ]
    text: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualGatewaySpecLoggingAccessLogFileFormatArgs:
    def __init__(
        __self__,
        *,
        jsons: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[VirtualGatewaySpecLoggingAccessLogFileFormatJsonArgs]
                ]
            ]
        ] = ...,
        text: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def jsons(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VirtualGatewaySpecLoggingAccessLogFileFormatJsonArgs]]
        ]
    ]: ...
    @jsons.setter
    def jsons(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[VirtualGatewaySpecLoggingAccessLogFileFormatJsonArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualGatewaySpecLoggingAccessLogFileFormatJsonArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualGatewaySpecLoggingAccessLogFileFormatJsonArgs:
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

class VirtualNodeSpecArgsDict(TypedDict):
    backend_defaults: NotRequired[pulumi.Input[VirtualNodeSpecBackendDefaultsArgsDict]]
    backends: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VirtualNodeSpecBackendArgsDict]]]
    ]
    listeners: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VirtualNodeSpecListenerArgsDict]]]
    ]
    logging: NotRequired[pulumi.Input[VirtualNodeSpecLoggingArgsDict]]
    service_discovery: NotRequired[
        pulumi.Input[VirtualNodeSpecServiceDiscoveryArgsDict]
    ]

@pulumi.input_type
class VirtualNodeSpecArgs:
    def __init__(
        __self__,
        *,
        backend_defaults: Optional[
            pulumi.Input[VirtualNodeSpecBackendDefaultsArgs]
        ] = ...,
        backends: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNodeSpecBackendArgs]]]
        ] = ...,
        listeners: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNodeSpecListenerArgs]]]
        ] = ...,
        logging: Optional[pulumi.Input[VirtualNodeSpecLoggingArgs]] = ...,
        service_discovery: Optional[
            pulumi.Input[VirtualNodeSpecServiceDiscoveryArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendDefaults")
    def backend_defaults(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecBackendDefaultsArgs]]: ...
    @backend_defaults.setter
    def backend_defaults(
        self, value: Optional[pulumi.Input[VirtualNodeSpecBackendDefaultsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def backends(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualNodeSpecBackendArgs]]]]: ...
    @backends.setter
    def backends(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNodeSpecBackendArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def listeners(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VirtualNodeSpecListenerArgs]]]
    ]: ...
    @listeners.setter
    def listeners(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNodeSpecListenerArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input[VirtualNodeSpecLoggingArgs]]: ...
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[VirtualNodeSpecLoggingArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDiscovery")
    def service_discovery(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecServiceDiscoveryArgs]]: ...
    @service_discovery.setter
    def service_discovery(
        self, value: Optional[pulumi.Input[VirtualNodeSpecServiceDiscoveryArgs]]
    ): ...

class VirtualNodeSpecBackendArgsDict(TypedDict):
    virtual_service: pulumi.Input[VirtualNodeSpecBackendVirtualServiceArgsDict]

@pulumi.input_type
class VirtualNodeSpecBackendArgs:
    def __init__(
        __self__,
        *,
        virtual_service: pulumi.Input[VirtualNodeSpecBackendVirtualServiceArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualService")
    def virtual_service(
        self,
    ) -> pulumi.Input[VirtualNodeSpecBackendVirtualServiceArgs]: ...
    @virtual_service.setter
    def virtual_service(
        self, value: pulumi.Input[VirtualNodeSpecBackendVirtualServiceArgs]
    ): ...

class VirtualNodeSpecBackendDefaultsArgsDict(TypedDict):
    client_policy: NotRequired[
        pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyArgsDict]
    ]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsArgs:
    def __init__(
        __self__,
        *,
        client_policy: Optional[
            pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientPolicy")
    def client_policy(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyArgs]]: ...
    @client_policy.setter
    def client_policy(
        self,
        value: Optional[pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyArgs]],
    ): ...

class VirtualNodeSpecBackendDefaultsClientPolicyArgsDict(TypedDict):
    tls: NotRequired[
        pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyTlsArgsDict]
    ]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsClientPolicyArgs:
    def __init__(
        __self__,
        *,
        tls: Optional[
            pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyTlsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tls(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyTlsArgs]]: ...
    @tls.setter
    def tls(
        self,
        value: Optional[
            pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyTlsArgs]
        ],
    ): ...

class VirtualNodeSpecBackendDefaultsClientPolicyTlsArgsDict(TypedDict):
    validation: pulumi.Input[
        VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationArgsDict
    ]
    certificate: NotRequired[
        pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateArgsDict]
    ]
    enforce: NotRequired[pulumi.Input[_builtins.bool]]
    ports: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsArgs:
    def __init__(
        __self__,
        *,
        validation: pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationArgs
        ],
        certificate: Optional[
            pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateArgs]
        ] = ...,
        enforce: Optional[pulumi.Input[_builtins.bool]] = ...,
        ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationArgs]: ...
    @validation.setter
    def validation(
        self,
        value: pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def certificate(
        self,
    ) -> Optional[
        pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateArgs]
    ]: ...
    @certificate.setter
    def certificate(
        self,
        value: Optional[
            pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enforce.setter
    def enforce(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def ports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @ports.setter
    def ports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateArgsDict(TypedDict):
    file: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileArgsDict
        ]
    ]
    sds: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsArgsDict
        ]
    ]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateArgs:
    def __init__(
        __self__,
        *,
        file: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileArgs
            ]
        ] = ...,
        sds: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileArgs]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        pulumi.Input[VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsArgs]
    ]: ...
    @sds.setter
    def sds(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsArgs
            ]
        ],
    ): ...

class VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileArgsDict(TypedDict):
    certificate_chain: pulumi.Input[_builtins.str]
    private_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileArgs:
    def __init__(
        __self__,
        *,
        certificate_chain: pulumi.Input[_builtins.str],
        private_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[_builtins.str]: ...
    @private_key.setter
    def private_key(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsArgsDict(TypedDict):
    secret_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsArgs:
    def __init__(__self__, *, secret_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationArgsDict(TypedDict):
    trust: pulumi.Input[
        VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustArgsDict
    ]
    subject_alternative_names: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesArgsDict
        ]
    ]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationArgs:
    def __init__(
        __self__,
        *,
        trust: pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustArgs
        ],
        subject_alternative_names: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trust(
        self,
    ) -> pulumi.Input[
        VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustArgs
    ]: ...
    @trust.setter
    def trust(
        self,
        value: pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesArgs
        ]
    ]: ...
    @subject_alternative_names.setter
    def subject_alternative_names(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesArgs
            ]
        ],
    ): ...

class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesArgsDict(
    TypedDict
):
    match: pulumi.Input[
        VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchArgsDict
    ]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesArgs:
    def __init__(
        __self__,
        *,
        match: pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> pulumi.Input[
        VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchArgs
    ]: ...
    @match.setter
    def match(
        self,
        value: pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchArgs
        ],
    ): ...

class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchArgsDict(
    TypedDict
):
    exacts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchArgs:
    def __init__(
        __self__, *, exacts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @exacts.setter
    def exacts(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustArgsDict(TypedDict):
    acm: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmArgsDict
        ]
    ]
    file: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileArgsDict
        ]
    ]
    sds: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsArgsDict
        ]
    ]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustArgs:
    def __init__(
        __self__,
        *,
        acm: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmArgs
            ]
        ] = ...,
        file: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileArgs
            ]
        ] = ...,
        sds: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acm(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmArgs
        ]
    ]: ...
    @acm.setter
    def acm(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsArgs
        ]
    ]: ...
    @sds.setter
    def sds(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsArgs
            ]
        ],
    ): ...

class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmArgsDict(
    TypedDict
):
    certificate_authority_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmArgs:
    def __init__(
        __self__,
        *,
        certificate_authority_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArns")
    def certificate_authority_arns(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @certificate_authority_arns.setter
    def certificate_authority_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileArgsDict(
    TypedDict
):
    certificate_chain: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileArgs:
    def __init__(
        __self__, *, certificate_chain: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsArgsDict(
    TypedDict
):
    secret_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsArgs:
    def __init__(__self__, *, secret_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecBackendVirtualServiceArgsDict(TypedDict):
    virtual_service_name: pulumi.Input[_builtins.str]
    client_policy: NotRequired[
        pulumi.Input[VirtualNodeSpecBackendVirtualServiceClientPolicyArgsDict]
    ]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceArgs:
    def __init__(
        __self__,
        *,
        virtual_service_name: pulumi.Input[_builtins.str],
        client_policy: Optional[
            pulumi.Input[VirtualNodeSpecBackendVirtualServiceClientPolicyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualServiceName")
    def virtual_service_name(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_service_name.setter
    def virtual_service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientPolicy")
    def client_policy(
        self,
    ) -> Optional[
        pulumi.Input[VirtualNodeSpecBackendVirtualServiceClientPolicyArgs]
    ]: ...
    @client_policy.setter
    def client_policy(
        self,
        value: Optional[
            pulumi.Input[VirtualNodeSpecBackendVirtualServiceClientPolicyArgs]
        ],
    ): ...

class VirtualNodeSpecBackendVirtualServiceClientPolicyArgsDict(TypedDict):
    tls: NotRequired[
        pulumi.Input[VirtualNodeSpecBackendVirtualServiceClientPolicyTlsArgsDict]
    ]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyArgs:
    def __init__(
        __self__,
        *,
        tls: Optional[
            pulumi.Input[VirtualNodeSpecBackendVirtualServiceClientPolicyTlsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tls(
        self,
    ) -> Optional[
        pulumi.Input[VirtualNodeSpecBackendVirtualServiceClientPolicyTlsArgs]
    ]: ...
    @tls.setter
    def tls(
        self,
        value: Optional[
            pulumi.Input[VirtualNodeSpecBackendVirtualServiceClientPolicyTlsArgs]
        ],
    ): ...

class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsArgsDict(TypedDict):
    validation: pulumi.Input[
        VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationArgsDict
    ]
    certificate: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateArgsDict
        ]
    ]
    enforce: NotRequired[pulumi.Input[_builtins.bool]]
    ports: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsArgs:
    def __init__(
        __self__,
        *,
        validation: pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationArgs
        ],
        certificate: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateArgs
            ]
        ] = ...,
        enforce: Optional[pulumi.Input[_builtins.bool]] = ...,
        ports: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> pulumi.Input[
        VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationArgs
    ]: ...
    @validation.setter
    def validation(
        self,
        value: pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def certificate(
        self,
    ) -> Optional[
        pulumi.Input[VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateArgs]
    ]: ...
    @certificate.setter
    def certificate(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enforce.setter
    def enforce(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def ports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @ports.setter
    def ports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateArgsDict(TypedDict):
    file: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileArgsDict
        ]
    ]
    sds: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsArgsDict
        ]
    ]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateArgs:
    def __init__(
        __self__,
        *,
        file: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileArgs
            ]
        ] = ...,
        sds: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsArgs
        ]
    ]: ...
    @sds.setter
    def sds(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsArgs
            ]
        ],
    ): ...

class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileArgsDict(
    TypedDict
):
    certificate_chain: pulumi.Input[_builtins.str]
    private_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileArgs:
    def __init__(
        __self__,
        *,
        certificate_chain: pulumi.Input[_builtins.str],
        private_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[_builtins.str]: ...
    @private_key.setter
    def private_key(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsArgsDict(
    TypedDict
):
    secret_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsArgs:
    def __init__(__self__, *, secret_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationArgsDict(TypedDict):
    trust: pulumi.Input[
        VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustArgsDict
    ]
    subject_alternative_names: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesArgsDict
        ]
    ]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationArgs:
    def __init__(
        __self__,
        *,
        trust: pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustArgs
        ],
        subject_alternative_names: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trust(
        self,
    ) -> pulumi.Input[
        VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustArgs
    ]: ...
    @trust.setter
    def trust(
        self,
        value: pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesArgs
        ]
    ]: ...
    @subject_alternative_names.setter
    def subject_alternative_names(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesArgs
            ]
        ],
    ): ...

class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesArgsDict(
    TypedDict
):
    match: pulumi.Input[
        VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchArgsDict
    ]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesArgs:
    def __init__(
        __self__,
        *,
        match: pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> pulumi.Input[
        VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchArgs
    ]: ...
    @match.setter
    def match(
        self,
        value: pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchArgs
        ],
    ): ...

class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchArgsDict(
    TypedDict
):
    exacts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchArgs:
    def __init__(
        __self__, *, exacts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @exacts.setter
    def exacts(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustArgsDict(
    TypedDict
):
    acm: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmArgsDict
        ]
    ]
    file: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileArgsDict
        ]
    ]
    sds: NotRequired[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsArgsDict
        ]
    ]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustArgs:
    def __init__(
        __self__,
        *,
        acm: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmArgs
            ]
        ] = ...,
        file: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileArgs
            ]
        ] = ...,
        sds: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acm(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmArgs
        ]
    ]: ...
    @acm.setter
    def acm(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileArgs
        ]
    ]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        pulumi.Input[
            VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsArgs
        ]
    ]: ...
    @sds.setter
    def sds(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsArgs
            ]
        ],
    ): ...

class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmArgsDict(
    TypedDict
):
    certificate_authority_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmArgs:
    def __init__(
        __self__,
        *,
        certificate_authority_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArns")
    def certificate_authority_arns(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @certificate_authority_arns.setter
    def certificate_authority_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileArgsDict(
    TypedDict
):
    certificate_chain: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileArgs:
    def __init__(
        __self__, *, certificate_chain: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsArgsDict(
    TypedDict
):
    secret_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsArgs:
    def __init__(__self__, *, secret_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecListenerArgsDict(TypedDict):
    port_mapping: pulumi.Input[VirtualNodeSpecListenerPortMappingArgsDict]
    connection_pool: NotRequired[
        pulumi.Input[VirtualNodeSpecListenerConnectionPoolArgsDict]
    ]
    health_check: NotRequired[pulumi.Input[VirtualNodeSpecListenerHealthCheckArgsDict]]
    outlier_detection: NotRequired[
        pulumi.Input[VirtualNodeSpecListenerOutlierDetectionArgsDict]
    ]
    timeout: NotRequired[pulumi.Input[VirtualNodeSpecListenerTimeoutArgsDict]]
    tls: NotRequired[pulumi.Input[VirtualNodeSpecListenerTlsArgsDict]]

@pulumi.input_type
class VirtualNodeSpecListenerArgs:
    def __init__(
        __self__,
        *,
        port_mapping: pulumi.Input[VirtualNodeSpecListenerPortMappingArgs],
        connection_pool: Optional[
            pulumi.Input[VirtualNodeSpecListenerConnectionPoolArgs]
        ] = ...,
        health_check: Optional[
            pulumi.Input[VirtualNodeSpecListenerHealthCheckArgs]
        ] = ...,
        outlier_detection: Optional[
            pulumi.Input[VirtualNodeSpecListenerOutlierDetectionArgs]
        ] = ...,
        timeout: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutArgs]] = ...,
        tls: Optional[pulumi.Input[VirtualNodeSpecListenerTlsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="portMapping")
    def port_mapping(self) -> pulumi.Input[VirtualNodeSpecListenerPortMappingArgs]: ...
    @port_mapping.setter
    def port_mapping(
        self, value: pulumi.Input[VirtualNodeSpecListenerPortMappingArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionPool")
    def connection_pool(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerConnectionPoolArgs]]: ...
    @connection_pool.setter
    def connection_pool(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerConnectionPoolArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerHealthCheckArgs]]: ...
    @health_check.setter
    def health_check(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outlierDetection")
    def outlier_detection(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerOutlierDetectionArgs]]: ...
    @outlier_detection.setter
    def outlier_detection(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerOutlierDetectionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutArgs]]: ...
    @timeout.setter
    def timeout(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[pulumi.Input[VirtualNodeSpecListenerTlsArgs]]: ...
    @tls.setter
    def tls(self, value: Optional[pulumi.Input[VirtualNodeSpecListenerTlsArgs]]): ...

class VirtualNodeSpecListenerConnectionPoolArgsDict(TypedDict):
    grpc: NotRequired[pulumi.Input[VirtualNodeSpecListenerConnectionPoolGrpcArgsDict]]
    http2s: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[VirtualNodeSpecListenerConnectionPoolHttp2ArgsDict]]
        ]
    ]
    https: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[VirtualNodeSpecListenerConnectionPoolHttpArgsDict]]
        ]
    ]
    tcps: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[VirtualNodeSpecListenerConnectionPoolTcpArgsDict]]
        ]
    ]

@pulumi.input_type
class VirtualNodeSpecListenerConnectionPoolArgs:
    def __init__(
        __self__,
        *,
        grpc: Optional[
            pulumi.Input[VirtualNodeSpecListenerConnectionPoolGrpcArgs]
        ] = ...,
        http2s: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VirtualNodeSpecListenerConnectionPoolHttp2Args]]
            ]
        ] = ...,
        https: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VirtualNodeSpecListenerConnectionPoolHttpArgs]]
            ]
        ] = ...,
        tcps: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VirtualNodeSpecListenerConnectionPoolTcpArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerConnectionPoolGrpcArgs]]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[pulumi.Input[VirtualNodeSpecListenerConnectionPoolGrpcArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def http2s(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VirtualNodeSpecListenerConnectionPoolHttp2Args]]
        ]
    ]: ...
    @http2s.setter
    def http2s(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VirtualNodeSpecListenerConnectionPoolHttp2Args]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def https(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VirtualNodeSpecListenerConnectionPoolHttpArgs]]
        ]
    ]: ...
    @https.setter
    def https(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VirtualNodeSpecListenerConnectionPoolHttpArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tcps(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VirtualNodeSpecListenerConnectionPoolTcpArgs]]
        ]
    ]: ...
    @tcps.setter
    def tcps(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[VirtualNodeSpecListenerConnectionPoolTcpArgs]]
            ]
        ],
    ): ...

class VirtualNodeSpecListenerConnectionPoolGrpcArgsDict(TypedDict):
    max_requests: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerConnectionPoolGrpcArgs:
    def __init__(__self__, *, max_requests: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequests")
    def max_requests(self) -> pulumi.Input[_builtins.int]: ...
    @max_requests.setter
    def max_requests(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerConnectionPoolHttp2ArgsDict(TypedDict):
    max_requests: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerConnectionPoolHttp2Args:
    def __init__(__self__, *, max_requests: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequests")
    def max_requests(self) -> pulumi.Input[_builtins.int]: ...
    @max_requests.setter
    def max_requests(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerConnectionPoolHttpArgsDict(TypedDict):
    max_connections: pulumi.Input[_builtins.int]
    max_pending_requests: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class VirtualNodeSpecListenerConnectionPoolHttpArgs:
    def __init__(
        __self__,
        *,
        max_connections: pulumi.Input[_builtins.int],
        max_pending_requests: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> pulumi.Input[_builtins.int]: ...
    @max_connections.setter
    def max_connections(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maxPendingRequests")
    def max_pending_requests(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_pending_requests.setter
    def max_pending_requests(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class VirtualNodeSpecListenerConnectionPoolTcpArgsDict(TypedDict):
    max_connections: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerConnectionPoolTcpArgs:
    def __init__(__self__, *, max_connections: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> pulumi.Input[_builtins.int]: ...
    @max_connections.setter
    def max_connections(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerHealthCheckArgsDict(TypedDict):
    healthy_threshold: pulumi.Input[_builtins.int]
    interval_millis: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]
    timeout_millis: pulumi.Input[_builtins.int]
    unhealthy_threshold: pulumi.Input[_builtins.int]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class VirtualNodeSpecListenerHealthCheckArgs:
    def __init__(
        __self__,
        *,
        healthy_threshold: pulumi.Input[_builtins.int],
        interval_millis: pulumi.Input[_builtins.int],
        protocol: pulumi.Input[_builtins.str],
        timeout_millis: pulumi.Input[_builtins.int],
        unhealthy_threshold: pulumi.Input[_builtins.int],
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> pulumi.Input[_builtins.int]: ...
    @healthy_threshold.setter
    def healthy_threshold(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="intervalMillis")
    def interval_millis(self) -> pulumi.Input[_builtins.int]: ...
    @interval_millis.setter
    def interval_millis(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutMillis")
    def timeout_millis(self) -> pulumi.Input[_builtins.int]: ...
    @timeout_millis.setter
    def timeout_millis(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> pulumi.Input[_builtins.int]: ...
    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class VirtualNodeSpecListenerOutlierDetectionArgsDict(TypedDict):
    base_ejection_duration: pulumi.Input[
        VirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationArgsDict
    ]
    interval: pulumi.Input[VirtualNodeSpecListenerOutlierDetectionIntervalArgsDict]
    max_ejection_percent: pulumi.Input[_builtins.int]
    max_server_errors: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerOutlierDetectionArgs:
    def __init__(
        __self__,
        *,
        base_ejection_duration: pulumi.Input[
            VirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationArgs
        ],
        interval: pulumi.Input[VirtualNodeSpecListenerOutlierDetectionIntervalArgs],
        max_ejection_percent: pulumi.Input[_builtins.int],
        max_server_errors: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseEjectionDuration")
    def base_ejection_duration(
        self,
    ) -> pulumi.Input[
        VirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationArgs
    ]: ...
    @base_ejection_duration.setter
    def base_ejection_duration(
        self,
        value: pulumi.Input[
            VirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def interval(
        self,
    ) -> pulumi.Input[VirtualNodeSpecListenerOutlierDetectionIntervalArgs]: ...
    @interval.setter
    def interval(
        self, value: pulumi.Input[VirtualNodeSpecListenerOutlierDetectionIntervalArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxEjectionPercent")
    def max_ejection_percent(self) -> pulumi.Input[_builtins.int]: ...
    @max_ejection_percent.setter
    def max_ejection_percent(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maxServerErrors")
    def max_server_errors(self) -> pulumi.Input[_builtins.int]: ...
    @max_server_errors.setter
    def max_server_errors(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerOutlierDetectionIntervalArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerOutlierDetectionIntervalArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerPortMappingArgsDict(TypedDict):
    port: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecListenerPortMappingArgs:
    def __init__(
        __self__,
        *,
        port: pulumi.Input[_builtins.int],
        protocol: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecListenerTimeoutArgsDict(TypedDict):
    grpc: NotRequired[pulumi.Input[VirtualNodeSpecListenerTimeoutGrpcArgsDict]]
    http: NotRequired[pulumi.Input[VirtualNodeSpecListenerTimeoutHttpArgsDict]]
    http2: NotRequired[pulumi.Input[VirtualNodeSpecListenerTimeoutHttp2ArgsDict]]
    tcp: NotRequired[pulumi.Input[VirtualNodeSpecListenerTimeoutTcpArgsDict]]

@pulumi.input_type
class VirtualNodeSpecListenerTimeoutArgs:
    def __init__(
        __self__,
        *,
        grpc: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutGrpcArgs]] = ...,
        http: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttpArgs]] = ...,
        http2: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttp2Args]] = ...,
        tcp: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutTcpArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutGrpcArgs]]: ...
    @grpc.setter
    def grpc(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutGrpcArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def http(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttpArgs]]: ...
    @http.setter
    def http(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttpArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def http2(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttp2Args]]: ...
    @http2.setter
    def http2(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttp2Args]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tcp(self) -> Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutTcpArgs]]: ...
    @tcp.setter
    def tcp(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutTcpArgs]]
    ): ...

class VirtualNodeSpecListenerTimeoutGrpcArgsDict(TypedDict):
    idle: NotRequired[pulumi.Input[VirtualNodeSpecListenerTimeoutGrpcIdleArgsDict]]
    per_request: NotRequired[
        pulumi.Input[VirtualNodeSpecListenerTimeoutGrpcPerRequestArgsDict]
    ]

@pulumi.input_type
class VirtualNodeSpecListenerTimeoutGrpcArgs:
    def __init__(
        __self__,
        *,
        idle: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutGrpcIdleArgs]] = ...,
        per_request: Optional[
            pulumi.Input[VirtualNodeSpecListenerTimeoutGrpcPerRequestArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutGrpcIdleArgs]]: ...
    @idle.setter
    def idle(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutGrpcIdleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="perRequest")
    def per_request(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutGrpcPerRequestArgs]]: ...
    @per_request.setter
    def per_request(
        self,
        value: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutGrpcPerRequestArgs]],
    ): ...

class VirtualNodeSpecListenerTimeoutGrpcIdleArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerTimeoutGrpcIdleArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerTimeoutGrpcPerRequestArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerTimeoutGrpcPerRequestArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerTimeoutHttp2ArgsDict(TypedDict):
    idle: NotRequired[pulumi.Input[VirtualNodeSpecListenerTimeoutHttp2IdleArgsDict]]
    per_request: NotRequired[
        pulumi.Input[VirtualNodeSpecListenerTimeoutHttp2PerRequestArgsDict]
    ]

@pulumi.input_type
class VirtualNodeSpecListenerTimeoutHttp2Args:
    def __init__(
        __self__,
        *,
        idle: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttp2IdleArgs]] = ...,
        per_request: Optional[
            pulumi.Input[VirtualNodeSpecListenerTimeoutHttp2PerRequestArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttp2IdleArgs]]: ...
    @idle.setter
    def idle(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttp2IdleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="perRequest")
    def per_request(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttp2PerRequestArgs]]: ...
    @per_request.setter
    def per_request(
        self,
        value: Optional[
            pulumi.Input[VirtualNodeSpecListenerTimeoutHttp2PerRequestArgs]
        ],
    ): ...

class VirtualNodeSpecListenerTimeoutHttp2IdleArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerTimeoutHttp2IdleArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerTimeoutHttp2PerRequestArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerTimeoutHttp2PerRequestArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerTimeoutHttpArgsDict(TypedDict):
    idle: NotRequired[pulumi.Input[VirtualNodeSpecListenerTimeoutHttpIdleArgsDict]]
    per_request: NotRequired[
        pulumi.Input[VirtualNodeSpecListenerTimeoutHttpPerRequestArgsDict]
    ]

@pulumi.input_type
class VirtualNodeSpecListenerTimeoutHttpArgs:
    def __init__(
        __self__,
        *,
        idle: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttpIdleArgs]] = ...,
        per_request: Optional[
            pulumi.Input[VirtualNodeSpecListenerTimeoutHttpPerRequestArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttpIdleArgs]]: ...
    @idle.setter
    def idle(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttpIdleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="perRequest")
    def per_request(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttpPerRequestArgs]]: ...
    @per_request.setter
    def per_request(
        self,
        value: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutHttpPerRequestArgs]],
    ): ...

class VirtualNodeSpecListenerTimeoutHttpIdleArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerTimeoutHttpIdleArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerTimeoutHttpPerRequestArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerTimeoutHttpPerRequestArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerTimeoutTcpArgsDict(TypedDict):
    idle: NotRequired[pulumi.Input[VirtualNodeSpecListenerTimeoutTcpIdleArgsDict]]

@pulumi.input_type
class VirtualNodeSpecListenerTimeoutTcpArgs:
    def __init__(
        __self__,
        *,
        idle: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutTcpIdleArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutTcpIdleArgs]]: ...
    @idle.setter
    def idle(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerTimeoutTcpIdleArgs]]
    ): ...

class VirtualNodeSpecListenerTimeoutTcpIdleArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class VirtualNodeSpecListenerTimeoutTcpIdleArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class VirtualNodeSpecListenerTlsArgsDict(TypedDict):
    certificate: pulumi.Input[VirtualNodeSpecListenerTlsCertificateArgsDict]
    mode: pulumi.Input[_builtins.str]
    validation: NotRequired[pulumi.Input[VirtualNodeSpecListenerTlsValidationArgsDict]]

@pulumi.input_type
class VirtualNodeSpecListenerTlsArgs:
    def __init__(
        __self__,
        *,
        certificate: pulumi.Input[VirtualNodeSpecListenerTlsCertificateArgs],
        mode: pulumi.Input[_builtins.str],
        validation: Optional[
            pulumi.Input[VirtualNodeSpecListenerTlsValidationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificate(
        self,
    ) -> pulumi.Input[VirtualNodeSpecListenerTlsCertificateArgs]: ...
    @certificate.setter
    def certificate(
        self, value: pulumi.Input[VirtualNodeSpecListenerTlsCertificateArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTlsValidationArgs]]: ...
    @validation.setter
    def validation(
        self, value: Optional[pulumi.Input[VirtualNodeSpecListenerTlsValidationArgs]]
    ): ...

class VirtualNodeSpecListenerTlsCertificateArgsDict(TypedDict):
    acm: NotRequired[pulumi.Input[VirtualNodeSpecListenerTlsCertificateAcmArgsDict]]
    file: NotRequired[pulumi.Input[VirtualNodeSpecListenerTlsCertificateFileArgsDict]]
    sds: NotRequired[pulumi.Input[VirtualNodeSpecListenerTlsCertificateSdsArgsDict]]

@pulumi.input_type
class VirtualNodeSpecListenerTlsCertificateArgs:
    def __init__(
        __self__,
        *,
        acm: Optional[pulumi.Input[VirtualNodeSpecListenerTlsCertificateAcmArgs]] = ...,
        file: Optional[
            pulumi.Input[VirtualNodeSpecListenerTlsCertificateFileArgs]
        ] = ...,
        sds: Optional[pulumi.Input[VirtualNodeSpecListenerTlsCertificateSdsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acm(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTlsCertificateAcmArgs]]: ...
    @acm.setter
    def acm(
        self,
        value: Optional[pulumi.Input[VirtualNodeSpecListenerTlsCertificateAcmArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTlsCertificateFileArgs]]: ...
    @file.setter
    def file(
        self,
        value: Optional[pulumi.Input[VirtualNodeSpecListenerTlsCertificateFileArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTlsCertificateSdsArgs]]: ...
    @sds.setter
    def sds(
        self,
        value: Optional[pulumi.Input[VirtualNodeSpecListenerTlsCertificateSdsArgs]],
    ): ...

class VirtualNodeSpecListenerTlsCertificateAcmArgsDict(TypedDict):
    certificate_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecListenerTlsCertificateAcmArgs:
    def __init__(__self__, *, certificate_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecListenerTlsCertificateFileArgsDict(TypedDict):
    certificate_chain: pulumi.Input[_builtins.str]
    private_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecListenerTlsCertificateFileArgs:
    def __init__(
        __self__,
        *,
        certificate_chain: pulumi.Input[_builtins.str],
        private_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[_builtins.str]: ...
    @private_key.setter
    def private_key(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecListenerTlsCertificateSdsArgsDict(TypedDict):
    secret_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecListenerTlsCertificateSdsArgs:
    def __init__(__self__, *, secret_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecListenerTlsValidationArgsDict(TypedDict):
    trust: pulumi.Input[VirtualNodeSpecListenerTlsValidationTrustArgsDict]
    subject_alternative_names: NotRequired[
        pulumi.Input[
            VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesArgsDict
        ]
    ]

@pulumi.input_type
class VirtualNodeSpecListenerTlsValidationArgs:
    def __init__(
        __self__,
        *,
        trust: pulumi.Input[VirtualNodeSpecListenerTlsValidationTrustArgs],
        subject_alternative_names: Optional[
            pulumi.Input[
                VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trust(self) -> pulumi.Input[VirtualNodeSpecListenerTlsValidationTrustArgs]: ...
    @trust.setter
    def trust(
        self, value: pulumi.Input[VirtualNodeSpecListenerTlsValidationTrustArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Optional[
        pulumi.Input[VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesArgs]
    ]: ...
    @subject_alternative_names.setter
    def subject_alternative_names(
        self,
        value: Optional[
            pulumi.Input[
                VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesArgs
            ]
        ],
    ): ...

class VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesArgsDict(TypedDict):
    match: pulumi.Input[
        VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchArgsDict
    ]

@pulumi.input_type
class VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesArgs:
    def __init__(
        __self__,
        *,
        match: pulumi.Input[
            VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> pulumi.Input[
        VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchArgs
    ]: ...
    @match.setter
    def match(
        self,
        value: pulumi.Input[
            VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchArgs
        ],
    ): ...

class VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchArgsDict(
    TypedDict
):
    exacts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchArgs:
    def __init__(
        __self__, *, exacts: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @exacts.setter
    def exacts(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class VirtualNodeSpecListenerTlsValidationTrustArgsDict(TypedDict):
    file: NotRequired[
        pulumi.Input[VirtualNodeSpecListenerTlsValidationTrustFileArgsDict]
    ]
    sds: NotRequired[pulumi.Input[VirtualNodeSpecListenerTlsValidationTrustSdsArgsDict]]

@pulumi.input_type
class VirtualNodeSpecListenerTlsValidationTrustArgs:
    def __init__(
        __self__,
        *,
        file: Optional[
            pulumi.Input[VirtualNodeSpecListenerTlsValidationTrustFileArgs]
        ] = ...,
        sds: Optional[
            pulumi.Input[VirtualNodeSpecListenerTlsValidationTrustSdsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTlsValidationTrustFileArgs]]: ...
    @file.setter
    def file(
        self,
        value: Optional[
            pulumi.Input[VirtualNodeSpecListenerTlsValidationTrustFileArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecListenerTlsValidationTrustSdsArgs]]: ...
    @sds.setter
    def sds(
        self,
        value: Optional[pulumi.Input[VirtualNodeSpecListenerTlsValidationTrustSdsArgs]],
    ): ...

class VirtualNodeSpecListenerTlsValidationTrustFileArgsDict(TypedDict):
    certificate_chain: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecListenerTlsValidationTrustFileArgs:
    def __init__(
        __self__, *, certificate_chain: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Input[_builtins.str]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecListenerTlsValidationTrustSdsArgsDict(TypedDict):
    secret_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecListenerTlsValidationTrustSdsArgs:
    def __init__(__self__, *, secret_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): ...

class VirtualNodeSpecLoggingArgsDict(TypedDict):
    access_log: NotRequired[pulumi.Input[VirtualNodeSpecLoggingAccessLogArgsDict]]

@pulumi.input_type
class VirtualNodeSpecLoggingArgs:
    def __init__(
        __self__,
        *,
        access_log: Optional[pulumi.Input[VirtualNodeSpecLoggingAccessLogArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLog")
    def access_log(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecLoggingAccessLogArgs]]: ...
    @access_log.setter
    def access_log(
        self, value: Optional[pulumi.Input[VirtualNodeSpecLoggingAccessLogArgs]]
    ): ...

class VirtualNodeSpecLoggingAccessLogArgsDict(TypedDict):
    file: NotRequired[pulumi.Input[VirtualNodeSpecLoggingAccessLogFileArgsDict]]

@pulumi.input_type
class VirtualNodeSpecLoggingAccessLogArgs:
    def __init__(
        __self__,
        *,
        file: Optional[pulumi.Input[VirtualNodeSpecLoggingAccessLogFileArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecLoggingAccessLogFileArgs]]: ...
    @file.setter
    def file(
        self, value: Optional[pulumi.Input[VirtualNodeSpecLoggingAccessLogFileArgs]]
    ): ...

class VirtualNodeSpecLoggingAccessLogFileArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    format: NotRequired[pulumi.Input[VirtualNodeSpecLoggingAccessLogFileFormatArgsDict]]

@pulumi.input_type
class VirtualNodeSpecLoggingAccessLogFileArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        format: Optional[
            pulumi.Input[VirtualNodeSpecLoggingAccessLogFileFormatArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def format(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecLoggingAccessLogFileFormatArgs]]: ...
    @format.setter
    def format(
        self,
        value: Optional[pulumi.Input[VirtualNodeSpecLoggingAccessLogFileFormatArgs]],
    ): ...

class VirtualNodeSpecLoggingAccessLogFileFormatArgsDict(TypedDict):
    jsons: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[VirtualNodeSpecLoggingAccessLogFileFormatJsonArgsDict]
            ]
        ]
    ]
    text: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNodeSpecLoggingAccessLogFileFormatArgs:
    def __init__(
        __self__,
        *,
        jsons: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[VirtualNodeSpecLoggingAccessLogFileFormatJsonArgs]
                ]
            ]
        ] = ...,
        text: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def jsons(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[VirtualNodeSpecLoggingAccessLogFileFormatJsonArgs]]
        ]
    ]: ...
    @jsons.setter
    def jsons(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[VirtualNodeSpecLoggingAccessLogFileFormatJsonArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNodeSpecLoggingAccessLogFileFormatJsonArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualNodeSpecLoggingAccessLogFileFormatJsonArgs:
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

class VirtualNodeSpecServiceDiscoveryArgsDict(TypedDict):
    aws_cloud_map: NotRequired[
        pulumi.Input[VirtualNodeSpecServiceDiscoveryAwsCloudMapArgsDict]
    ]
    dns: NotRequired[pulumi.Input[VirtualNodeSpecServiceDiscoveryDnsArgsDict]]

@pulumi.input_type
class VirtualNodeSpecServiceDiscoveryArgs:
    def __init__(
        __self__,
        *,
        aws_cloud_map: Optional[
            pulumi.Input[VirtualNodeSpecServiceDiscoveryAwsCloudMapArgs]
        ] = ...,
        dns: Optional[pulumi.Input[VirtualNodeSpecServiceDiscoveryDnsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsCloudMap")
    def aws_cloud_map(
        self,
    ) -> Optional[pulumi.Input[VirtualNodeSpecServiceDiscoveryAwsCloudMapArgs]]: ...
    @aws_cloud_map.setter
    def aws_cloud_map(
        self,
        value: Optional[pulumi.Input[VirtualNodeSpecServiceDiscoveryAwsCloudMapArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dns(self) -> Optional[pulumi.Input[VirtualNodeSpecServiceDiscoveryDnsArgs]]: ...
    @dns.setter
    def dns(
        self, value: Optional[pulumi.Input[VirtualNodeSpecServiceDiscoveryDnsArgs]]
    ): ...

class VirtualNodeSpecServiceDiscoveryAwsCloudMapArgsDict(TypedDict):
    namespace_name: pulumi.Input[_builtins.str]
    service_name: pulumi.Input[_builtins.str]
    attributes: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class VirtualNodeSpecServiceDiscoveryAwsCloudMapArgs:
    def __init__(
        __self__,
        *,
        namespace_name: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
        attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]: ...
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def attributes(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @attributes.setter
    def attributes(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class VirtualNodeSpecServiceDiscoveryDnsArgsDict(TypedDict):
    hostname: pulumi.Input[_builtins.str]
    ip_preference: NotRequired[pulumi.Input[_builtins.str]]
    response_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class VirtualNodeSpecServiceDiscoveryDnsArgs:
    def __init__(
        __self__,
        *,
        hostname: pulumi.Input[_builtins.str],
        ip_preference: Optional[pulumi.Input[_builtins.str]] = ...,
        response_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[_builtins.str]: ...
    @hostname.setter
    def hostname(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipPreference")
    def ip_preference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_preference.setter
    def ip_preference(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="responseType")
    def response_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @response_type.setter
    def response_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualRouterSpecArgsDict(TypedDict):
    listeners: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VirtualRouterSpecListenerArgsDict]]]
    ]

@pulumi.input_type
class VirtualRouterSpecArgs:
    def __init__(
        __self__,
        *,
        listeners: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualRouterSpecListenerArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def listeners(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VirtualRouterSpecListenerArgs]]]
    ]: ...
    @listeners.setter
    def listeners(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualRouterSpecListenerArgs]]]
        ],
    ): ...

class VirtualRouterSpecListenerArgsDict(TypedDict):
    port_mapping: pulumi.Input[VirtualRouterSpecListenerPortMappingArgsDict]

@pulumi.input_type
class VirtualRouterSpecListenerArgs:
    def __init__(
        __self__,
        *,
        port_mapping: pulumi.Input[VirtualRouterSpecListenerPortMappingArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="portMapping")
    def port_mapping(
        self,
    ) -> pulumi.Input[VirtualRouterSpecListenerPortMappingArgs]: ...
    @port_mapping.setter
    def port_mapping(
        self, value: pulumi.Input[VirtualRouterSpecListenerPortMappingArgs]
    ): ...

class VirtualRouterSpecListenerPortMappingArgsDict(TypedDict):
    port: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualRouterSpecListenerPortMappingArgs:
    def __init__(
        __self__,
        *,
        port: pulumi.Input[_builtins.int],
        protocol: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): ...

class VirtualServiceSpecArgsDict(TypedDict):
    provider: NotRequired[pulumi.Input[VirtualServiceSpecProviderArgsDict]]

@pulumi.input_type
class VirtualServiceSpecArgs:
    def __init__(
        __self__,
        *,
        provider: Optional[pulumi.Input[VirtualServiceSpecProviderArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> Optional[pulumi.Input[VirtualServiceSpecProviderArgs]]: ...
    @provider.setter
    def provider(
        self, value: Optional[pulumi.Input[VirtualServiceSpecProviderArgs]]
    ): ...

class VirtualServiceSpecProviderArgsDict(TypedDict):
    virtual_node: NotRequired[
        pulumi.Input[VirtualServiceSpecProviderVirtualNodeArgsDict]
    ]
    virtual_router: NotRequired[
        pulumi.Input[VirtualServiceSpecProviderVirtualRouterArgsDict]
    ]

@pulumi.input_type
class VirtualServiceSpecProviderArgs:
    def __init__(
        __self__,
        *,
        virtual_node: Optional[
            pulumi.Input[VirtualServiceSpecProviderVirtualNodeArgs]
        ] = ...,
        virtual_router: Optional[
            pulumi.Input[VirtualServiceSpecProviderVirtualRouterArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(
        self,
    ) -> Optional[pulumi.Input[VirtualServiceSpecProviderVirtualNodeArgs]]: ...
    @virtual_node.setter
    def virtual_node(
        self, value: Optional[pulumi.Input[VirtualServiceSpecProviderVirtualNodeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualRouter")
    def virtual_router(
        self,
    ) -> Optional[pulumi.Input[VirtualServiceSpecProviderVirtualRouterArgs]]: ...
    @virtual_router.setter
    def virtual_router(
        self, value: Optional[pulumi.Input[VirtualServiceSpecProviderVirtualRouterArgs]]
    ): ...

class VirtualServiceSpecProviderVirtualNodeArgsDict(TypedDict):
    virtual_node_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualServiceSpecProviderVirtualNodeArgs:
    def __init__(
        __self__, *, virtual_node_name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNodeName")
    def virtual_node_name(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_node_name.setter
    def virtual_node_name(self, value: pulumi.Input[_builtins.str]): ...

class VirtualServiceSpecProviderVirtualRouterArgsDict(TypedDict):
    virtual_router_name: pulumi.Input[_builtins.str]

@pulumi.input_type
class VirtualServiceSpecProviderVirtualRouterArgs:
    def __init__(
        __self__, *, virtual_router_name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualRouterName")
    def virtual_router_name(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_router_name.setter
    def virtual_router_name(self, value: pulumi.Input[_builtins.str]): ...
