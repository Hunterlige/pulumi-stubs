import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GatewayRouteSpec",
    "GatewayRouteSpecGrpcRoute",
    "GatewayRouteSpecGrpcRouteAction",
    "GatewayRouteSpecGrpcRouteActionTarget",
    ...,
    "GatewayRouteSpecGrpcRouteMatch",
    "GatewayRouteSpecHttp2Route",
    "GatewayRouteSpecHttp2RouteAction",
    "GatewayRouteSpecHttp2RouteActionRewrite",
    "GatewayRouteSpecHttp2RouteActionRewriteHostname",
    "GatewayRouteSpecHttp2RouteActionRewritePath",
    "GatewayRouteSpecHttp2RouteActionRewritePrefix",
    "GatewayRouteSpecHttp2RouteActionTarget",
    ...,
    "GatewayRouteSpecHttp2RouteMatch",
    "GatewayRouteSpecHttp2RouteMatchHeader",
    "GatewayRouteSpecHttp2RouteMatchHeaderMatch",
    "GatewayRouteSpecHttp2RouteMatchHeaderMatchRange",
    "GatewayRouteSpecHttp2RouteMatchHostname",
    "GatewayRouteSpecHttp2RouteMatchPath",
    "GatewayRouteSpecHttp2RouteMatchQueryParameter",
    "GatewayRouteSpecHttp2RouteMatchQueryParameterMatch",
    "GatewayRouteSpecHttpRoute",
    "GatewayRouteSpecHttpRouteAction",
    "GatewayRouteSpecHttpRouteActionRewrite",
    "GatewayRouteSpecHttpRouteActionRewriteHostname",
    "GatewayRouteSpecHttpRouteActionRewritePath",
    "GatewayRouteSpecHttpRouteActionRewritePrefix",
    "GatewayRouteSpecHttpRouteActionTarget",
    ...,
    "GatewayRouteSpecHttpRouteMatch",
    "GatewayRouteSpecHttpRouteMatchHeader",
    "GatewayRouteSpecHttpRouteMatchHeaderMatch",
    "GatewayRouteSpecHttpRouteMatchHeaderMatchRange",
    "GatewayRouteSpecHttpRouteMatchHostname",
    "GatewayRouteSpecHttpRouteMatchPath",
    "GatewayRouteSpecHttpRouteMatchQueryParameter",
    "GatewayRouteSpecHttpRouteMatchQueryParameterMatch",
    "MeshSpec",
    "MeshSpecEgressFilter",
    "MeshSpecServiceDiscovery",
    "RouteSpec",
    "RouteSpecGrpcRoute",
    "RouteSpecGrpcRouteAction",
    "RouteSpecGrpcRouteActionWeightedTarget",
    "RouteSpecGrpcRouteMatch",
    "RouteSpecGrpcRouteMatchMetadata",
    "RouteSpecGrpcRouteMatchMetadataMatch",
    "RouteSpecGrpcRouteMatchMetadataMatchRange",
    "RouteSpecGrpcRouteRetryPolicy",
    "RouteSpecGrpcRouteRetryPolicyPerRetryTimeout",
    "RouteSpecGrpcRouteTimeout",
    "RouteSpecGrpcRouteTimeoutIdle",
    "RouteSpecGrpcRouteTimeoutPerRequest",
    "RouteSpecHttp2Route",
    "RouteSpecHttp2RouteAction",
    "RouteSpecHttp2RouteActionWeightedTarget",
    "RouteSpecHttp2RouteMatch",
    "RouteSpecHttp2RouteMatchHeader",
    "RouteSpecHttp2RouteMatchHeaderMatch",
    "RouteSpecHttp2RouteMatchHeaderMatchRange",
    "RouteSpecHttp2RouteMatchPath",
    "RouteSpecHttp2RouteMatchQueryParameter",
    "RouteSpecHttp2RouteMatchQueryParameterMatch",
    "RouteSpecHttp2RouteRetryPolicy",
    "RouteSpecHttp2RouteRetryPolicyPerRetryTimeout",
    "RouteSpecHttp2RouteTimeout",
    "RouteSpecHttp2RouteTimeoutIdle",
    "RouteSpecHttp2RouteTimeoutPerRequest",
    "RouteSpecHttpRoute",
    "RouteSpecHttpRouteAction",
    "RouteSpecHttpRouteActionWeightedTarget",
    "RouteSpecHttpRouteMatch",
    "RouteSpecHttpRouteMatchHeader",
    "RouteSpecHttpRouteMatchHeaderMatch",
    "RouteSpecHttpRouteMatchHeaderMatchRange",
    "RouteSpecHttpRouteMatchPath",
    "RouteSpecHttpRouteMatchQueryParameter",
    "RouteSpecHttpRouteMatchQueryParameterMatch",
    "RouteSpecHttpRouteRetryPolicy",
    "RouteSpecHttpRouteRetryPolicyPerRetryTimeout",
    "RouteSpecHttpRouteTimeout",
    "RouteSpecHttpRouteTimeoutIdle",
    "RouteSpecHttpRouteTimeoutPerRequest",
    "RouteSpecTcpRoute",
    "RouteSpecTcpRouteAction",
    "RouteSpecTcpRouteActionWeightedTarget",
    "RouteSpecTcpRouteMatch",
    "RouteSpecTcpRouteTimeout",
    "RouteSpecTcpRouteTimeoutIdle",
    "VirtualGatewaySpec",
    "VirtualGatewaySpecBackendDefaults",
    "VirtualGatewaySpecBackendDefaultsClientPolicy",
    "VirtualGatewaySpecBackendDefaultsClientPolicyTls",
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
    "VirtualGatewaySpecListener",
    "VirtualGatewaySpecListenerConnectionPool",
    "VirtualGatewaySpecListenerConnectionPoolGrpc",
    "VirtualGatewaySpecListenerConnectionPoolHttp2",
    "VirtualGatewaySpecListenerConnectionPoolHttp",
    "VirtualGatewaySpecListenerHealthCheck",
    "VirtualGatewaySpecListenerPortMapping",
    "VirtualGatewaySpecListenerTls",
    "VirtualGatewaySpecListenerTlsCertificate",
    "VirtualGatewaySpecListenerTlsCertificateAcm",
    "VirtualGatewaySpecListenerTlsCertificateFile",
    "VirtualGatewaySpecListenerTlsCertificateSds",
    "VirtualGatewaySpecListenerTlsValidation",
    ...,
    ...,
    "VirtualGatewaySpecListenerTlsValidationTrust",
    "VirtualGatewaySpecListenerTlsValidationTrustFile",
    "VirtualGatewaySpecListenerTlsValidationTrustSds",
    "VirtualGatewaySpecLogging",
    "VirtualGatewaySpecLoggingAccessLog",
    "VirtualGatewaySpecLoggingAccessLogFile",
    "VirtualGatewaySpecLoggingAccessLogFileFormat",
    "VirtualGatewaySpecLoggingAccessLogFileFormatJson",
    "VirtualNodeSpec",
    "VirtualNodeSpecBackend",
    "VirtualNodeSpecBackendDefaults",
    "VirtualNodeSpecBackendDefaultsClientPolicy",
    "VirtualNodeSpecBackendDefaultsClientPolicyTls",
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
    "VirtualNodeSpecBackendVirtualService",
    "VirtualNodeSpecBackendVirtualServiceClientPolicy",
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
    "VirtualNodeSpecListener",
    "VirtualNodeSpecListenerConnectionPool",
    "VirtualNodeSpecListenerConnectionPoolGrpc",
    "VirtualNodeSpecListenerConnectionPoolHttp2",
    "VirtualNodeSpecListenerConnectionPoolHttp",
    "VirtualNodeSpecListenerConnectionPoolTcp",
    "VirtualNodeSpecListenerHealthCheck",
    "VirtualNodeSpecListenerOutlierDetection",
    ...,
    "VirtualNodeSpecListenerOutlierDetectionInterval",
    "VirtualNodeSpecListenerPortMapping",
    "VirtualNodeSpecListenerTimeout",
    "VirtualNodeSpecListenerTimeoutGrpc",
    "VirtualNodeSpecListenerTimeoutGrpcIdle",
    "VirtualNodeSpecListenerTimeoutGrpcPerRequest",
    "VirtualNodeSpecListenerTimeoutHttp2",
    "VirtualNodeSpecListenerTimeoutHttp2Idle",
    "VirtualNodeSpecListenerTimeoutHttp2PerRequest",
    "VirtualNodeSpecListenerTimeoutHttp",
    "VirtualNodeSpecListenerTimeoutHttpIdle",
    "VirtualNodeSpecListenerTimeoutHttpPerRequest",
    "VirtualNodeSpecListenerTimeoutTcp",
    "VirtualNodeSpecListenerTimeoutTcpIdle",
    "VirtualNodeSpecListenerTls",
    "VirtualNodeSpecListenerTlsCertificate",
    "VirtualNodeSpecListenerTlsCertificateAcm",
    "VirtualNodeSpecListenerTlsCertificateFile",
    "VirtualNodeSpecListenerTlsCertificateSds",
    "VirtualNodeSpecListenerTlsValidation",
    ...,
    ...,
    "VirtualNodeSpecListenerTlsValidationTrust",
    "VirtualNodeSpecListenerTlsValidationTrustFile",
    "VirtualNodeSpecListenerTlsValidationTrustSds",
    "VirtualNodeSpecLogging",
    "VirtualNodeSpecLoggingAccessLog",
    "VirtualNodeSpecLoggingAccessLogFile",
    "VirtualNodeSpecLoggingAccessLogFileFormat",
    "VirtualNodeSpecLoggingAccessLogFileFormatJson",
    "VirtualNodeSpecServiceDiscovery",
    "VirtualNodeSpecServiceDiscoveryAwsCloudMap",
    "VirtualNodeSpecServiceDiscoveryDns",
    "VirtualRouterSpec",
    "VirtualRouterSpecListener",
    "VirtualRouterSpecListenerPortMapping",
    "VirtualServiceSpec",
    "VirtualServiceSpecProvider",
    "VirtualServiceSpecProviderVirtualNode",
    "VirtualServiceSpecProviderVirtualRouter",
    "GetGatewayRouteSpecResult",
    "GetGatewayRouteSpecGrpcRouteResult",
    "GetGatewayRouteSpecGrpcRouteActionResult",
    "GetGatewayRouteSpecGrpcRouteActionTargetResult",
    ...,
    "GetGatewayRouteSpecGrpcRouteMatchResult",
    "GetGatewayRouteSpecHttp2RouteResult",
    "GetGatewayRouteSpecHttp2RouteActionResult",
    "GetGatewayRouteSpecHttp2RouteActionRewriteResult",
    ...,
    ...,
    ...,
    "GetGatewayRouteSpecHttp2RouteActionTargetResult",
    ...,
    "GetGatewayRouteSpecHttp2RouteMatchResult",
    "GetGatewayRouteSpecHttp2RouteMatchHeaderResult",
    ...,
    ...,
    "GetGatewayRouteSpecHttp2RouteMatchHostnameResult",
    "GetGatewayRouteSpecHttp2RouteMatchPathResult",
    ...,
    ...,
    "GetGatewayRouteSpecHttpRouteResult",
    "GetGatewayRouteSpecHttpRouteActionResult",
    "GetGatewayRouteSpecHttpRouteActionRewriteResult",
    ...,
    ...,
    ...,
    "GetGatewayRouteSpecHttpRouteActionTargetResult",
    ...,
    "GetGatewayRouteSpecHttpRouteMatchResult",
    "GetGatewayRouteSpecHttpRouteMatchHeaderResult",
    "GetGatewayRouteSpecHttpRouteMatchHeaderMatchResult",
    ...,
    "GetGatewayRouteSpecHttpRouteMatchHostnameResult",
    "GetGatewayRouteSpecHttpRouteMatchPathResult",
    ...,
    ...,
    "GetMeshSpecResult",
    "GetMeshSpecEgressFilterResult",
    "GetMeshSpecServiceDiscoveryResult",
    "GetRouteSpecResult",
    "GetRouteSpecGrpcRouteResult",
    "GetRouteSpecGrpcRouteActionResult",
    "GetRouteSpecGrpcRouteActionWeightedTargetResult",
    "GetRouteSpecGrpcRouteMatchResult",
    "GetRouteSpecGrpcRouteMatchMetadataResult",
    "GetRouteSpecGrpcRouteMatchMetadataMatchResult",
    "GetRouteSpecGrpcRouteMatchMetadataMatchRangeResult",
    "GetRouteSpecGrpcRouteRetryPolicyResult",
    ...,
    "GetRouteSpecGrpcRouteTimeoutResult",
    "GetRouteSpecGrpcRouteTimeoutIdleResult",
    "GetRouteSpecGrpcRouteTimeoutPerRequestResult",
    "GetRouteSpecHttp2RouteResult",
    "GetRouteSpecHttp2RouteActionResult",
    "GetRouteSpecHttp2RouteActionWeightedTargetResult",
    "GetRouteSpecHttp2RouteMatchResult",
    "GetRouteSpecHttp2RouteMatchHeaderResult",
    "GetRouteSpecHttp2RouteMatchHeaderMatchResult",
    "GetRouteSpecHttp2RouteMatchHeaderMatchRangeResult",
    "GetRouteSpecHttp2RouteMatchPathResult",
    "GetRouteSpecHttp2RouteMatchQueryParameterResult",
    ...,
    "GetRouteSpecHttp2RouteRetryPolicyResult",
    ...,
    "GetRouteSpecHttp2RouteTimeoutResult",
    "GetRouteSpecHttp2RouteTimeoutIdleResult",
    "GetRouteSpecHttp2RouteTimeoutPerRequestResult",
    "GetRouteSpecHttpRouteResult",
    "GetRouteSpecHttpRouteActionResult",
    "GetRouteSpecHttpRouteActionWeightedTargetResult",
    "GetRouteSpecHttpRouteMatchResult",
    "GetRouteSpecHttpRouteMatchHeaderResult",
    "GetRouteSpecHttpRouteMatchHeaderMatchResult",
    "GetRouteSpecHttpRouteMatchHeaderMatchRangeResult",
    "GetRouteSpecHttpRouteMatchPathResult",
    "GetRouteSpecHttpRouteMatchQueryParameterResult",
    ...,
    "GetRouteSpecHttpRouteRetryPolicyResult",
    ...,
    "GetRouteSpecHttpRouteTimeoutResult",
    "GetRouteSpecHttpRouteTimeoutIdleResult",
    "GetRouteSpecHttpRouteTimeoutPerRequestResult",
    "GetRouteSpecTcpRouteResult",
    "GetRouteSpecTcpRouteActionResult",
    "GetRouteSpecTcpRouteActionWeightedTargetResult",
    "GetRouteSpecTcpRouteMatchResult",
    "GetRouteSpecTcpRouteTimeoutResult",
    "GetRouteSpecTcpRouteTimeoutIdleResult",
    "GetVirtualGatewaySpecResult",
    "GetVirtualGatewaySpecBackendDefaultResult",
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
    "GetVirtualGatewaySpecListenerResult",
    "GetVirtualGatewaySpecListenerConnectionPoolResult",
    ...,
    ...,
    ...,
    "GetVirtualGatewaySpecListenerHealthCheckResult",
    "GetVirtualGatewaySpecListenerPortMappingResult",
    "GetVirtualGatewaySpecListenerTlResult",
    "GetVirtualGatewaySpecListenerTlCertificateResult",
    ...,
    ...,
    "GetVirtualGatewaySpecListenerTlCertificateSdResult",
    "GetVirtualGatewaySpecListenerTlValidationResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetVirtualGatewaySpecLoggingResult",
    "GetVirtualGatewaySpecLoggingAccessLogResult",
    "GetVirtualGatewaySpecLoggingAccessLogFileResult",
    ...,
    ...,
    "GetVirtualNodeSpecResult",
    "GetVirtualNodeSpecBackendResult",
    "GetVirtualNodeSpecBackendDefaultResult",
    "GetVirtualNodeSpecBackendDefaultClientPolicyResult",
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
    "GetVirtualNodeSpecBackendVirtualServiceResult",
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
    "GetVirtualNodeSpecListenerResult",
    "GetVirtualNodeSpecListenerConnectionPoolResult",
    "GetVirtualNodeSpecListenerConnectionPoolGrpcResult",
    ...,
    "GetVirtualNodeSpecListenerConnectionPoolHttpResult",
    "GetVirtualNodeSpecListenerConnectionPoolTcpResult",
    "GetVirtualNodeSpecListenerHealthCheckResult",
    "GetVirtualNodeSpecListenerOutlierDetectionResult",
    ...,
    ...,
    "GetVirtualNodeSpecListenerPortMappingResult",
    "GetVirtualNodeSpecListenerTimeoutResult",
    "GetVirtualNodeSpecListenerTimeoutGrpcResult",
    "GetVirtualNodeSpecListenerTimeoutGrpcIdleResult",
    ...,
    "GetVirtualNodeSpecListenerTimeoutHttp2Result",
    "GetVirtualNodeSpecListenerTimeoutHttp2IdleResult",
    ...,
    "GetVirtualNodeSpecListenerTimeoutHttpResult",
    "GetVirtualNodeSpecListenerTimeoutHttpIdleResult",
    ...,
    "GetVirtualNodeSpecListenerTimeoutTcpResult",
    "GetVirtualNodeSpecListenerTimeoutTcpIdleResult",
    "GetVirtualNodeSpecListenerTlResult",
    "GetVirtualNodeSpecListenerTlCertificateResult",
    "GetVirtualNodeSpecListenerTlCertificateAcmResult",
    "GetVirtualNodeSpecListenerTlCertificateFileResult",
    "GetVirtualNodeSpecListenerTlCertificateSdResult",
    "GetVirtualNodeSpecListenerTlValidationResult",
    ...,
    ...,
    "GetVirtualNodeSpecListenerTlValidationTrustResult",
    ...,
    ...,
    "GetVirtualNodeSpecLoggingResult",
    "GetVirtualNodeSpecLoggingAccessLogResult",
    "GetVirtualNodeSpecLoggingAccessLogFileResult",
    "GetVirtualNodeSpecLoggingAccessLogFileFormatResult",
    ...,
    "GetVirtualNodeSpecServiceDiscoveryResult",
    ...,
    "GetVirtualNodeSpecServiceDiscoveryDnResult",
    "GetVirtualRouterSpecResult",
    "GetVirtualRouterSpecListenerResult",
    "GetVirtualRouterSpecListenerPortMappingResult",
    "GetVirtualServiceSpecResult",
    "GetVirtualServiceSpecProviderResult",
    "GetVirtualServiceSpecProviderVirtualNodeResult",
    "GetVirtualServiceSpecProviderVirtualRouterResult",
]

@pulumi.output_type
class GatewayRouteSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        grpc_route: Optional[outputs.GatewayRouteSpecGrpcRoute] = ...,
        http2_route: Optional[outputs.GatewayRouteSpecHttp2Route] = ...,
        http_route: Optional[outputs.GatewayRouteSpecHttpRoute] = ...,
        priority: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="grpcRoute")
    def grpc_route(self) -> Optional[outputs.GatewayRouteSpecGrpcRoute]: ...
    @_builtins.property
    @pulumi.getter(name="http2Route")
    def http2_route(self) -> Optional[outputs.GatewayRouteSpecHttp2Route]: ...
    @_builtins.property
    @pulumi.getter(name="httpRoute")
    def http_route(self) -> Optional[outputs.GatewayRouteSpecHttpRoute]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GatewayRouteSpecGrpcRoute(dict):
    def __init__(
        __self__,
        *,
        action: outputs.GatewayRouteSpecGrpcRouteAction,
        match: outputs.GatewayRouteSpecGrpcRouteMatch,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.GatewayRouteSpecGrpcRouteAction: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> outputs.GatewayRouteSpecGrpcRouteMatch: ...

@pulumi.output_type
class GatewayRouteSpecGrpcRouteAction(dict):
    def __init__(
        __self__, *, target: outputs.GatewayRouteSpecGrpcRouteActionTarget
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> outputs.GatewayRouteSpecGrpcRouteActionTarget: ...

@pulumi.output_type
class GatewayRouteSpecGrpcRouteActionTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        virtual_service: outputs.GatewayRouteSpecGrpcRouteActionTargetVirtualService,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualService")
    def virtual_service(
        self,
    ) -> outputs.GatewayRouteSpecGrpcRouteActionTargetVirtualService: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GatewayRouteSpecGrpcRouteActionTargetVirtualService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, virtual_service_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualServiceName")
    def virtual_service_name(self) -> _builtins.str: ...

@pulumi.output_type
class GatewayRouteSpecGrpcRouteMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, service_name: _builtins.str, port: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GatewayRouteSpecHttp2Route(dict):
    def __init__(
        __self__,
        *,
        action: outputs.GatewayRouteSpecHttp2RouteAction,
        match: outputs.GatewayRouteSpecHttp2RouteMatch,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.GatewayRouteSpecHttp2RouteAction: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> outputs.GatewayRouteSpecHttp2RouteMatch: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteAction(dict):
    def __init__(
        __self__,
        *,
        target: outputs.GatewayRouteSpecHttp2RouteActionTarget,
        rewrite: Optional[outputs.GatewayRouteSpecHttp2RouteActionRewrite] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> outputs.GatewayRouteSpecHttp2RouteActionTarget: ...
    @_builtins.property
    @pulumi.getter
    def rewrite(self) -> Optional[outputs.GatewayRouteSpecHttp2RouteActionRewrite]: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteActionRewrite(dict):
    def __init__(
        __self__,
        *,
        hostname: Optional[
            outputs.GatewayRouteSpecHttp2RouteActionRewriteHostname
        ] = ...,
        path: Optional[outputs.GatewayRouteSpecHttp2RouteActionRewritePath] = ...,
        prefix: Optional[outputs.GatewayRouteSpecHttp2RouteActionRewritePrefix] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(
        self,
    ) -> Optional[outputs.GatewayRouteSpecHttp2RouteActionRewriteHostname]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[outputs.GatewayRouteSpecHttp2RouteActionRewritePath]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(
        self,
    ) -> Optional[outputs.GatewayRouteSpecHttp2RouteActionRewritePrefix]: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteActionRewriteHostname(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, default_target_hostname: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultTargetHostname")
    def default_target_hostname(self) -> _builtins.str: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteActionRewritePath(dict):
    def __init__(__self__, *, exact: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteActionRewritePrefix(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_prefix: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultPrefix")
    def default_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteActionTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        virtual_service: outputs.GatewayRouteSpecHttp2RouteActionTargetVirtualService,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualService")
    def virtual_service(
        self,
    ) -> outputs.GatewayRouteSpecHttp2RouteActionTargetVirtualService: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteActionTargetVirtualService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, virtual_service_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualServiceName")
    def virtual_service_name(self) -> _builtins.str: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        headers: Optional[
            Sequence[outputs.GatewayRouteSpecHttp2RouteMatchHeader]
        ] = ...,
        hostname: Optional[outputs.GatewayRouteSpecHttp2RouteMatchHostname] = ...,
        path: Optional[outputs.GatewayRouteSpecHttp2RouteMatchPath] = ...,
        port: Optional[_builtins.int] = ...,
        prefix: Optional[_builtins.str] = ...,
        query_parameters: Optional[
            Sequence[outputs.GatewayRouteSpecHttp2RouteMatchQueryParameter]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[Sequence[outputs.GatewayRouteSpecHttp2RouteMatchHeader]]: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[outputs.GatewayRouteSpecHttp2RouteMatchHostname]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[outputs.GatewayRouteSpecHttp2RouteMatchPath]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[Sequence[outputs.GatewayRouteSpecHttp2RouteMatchQueryParameter]]: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteMatchHeader(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        invert: Optional[_builtins.bool] = ...,
        match: Optional[outputs.GatewayRouteSpecHttp2RouteMatchHeaderMatch] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[outputs.GatewayRouteSpecHttp2RouteMatchHeaderMatch]: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteMatchHeaderMatch(dict):
    def __init__(
        __self__,
        *,
        exact: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
        range: Optional[outputs.GatewayRouteSpecHttp2RouteMatchHeaderMatchRange] = ...,
        regex: Optional[_builtins.str] = ...,
        suffix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def range(
        self,
    ) -> Optional[outputs.GatewayRouteSpecHttp2RouteMatchHeaderMatchRange]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteMatchHeaderMatchRange(dict):
    def __init__(__self__, *, end: _builtins.int, start: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteMatchHostname(dict):
    def __init__(
        __self__,
        *,
        exact: Optional[_builtins.str] = ...,
        suffix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteMatchPath(dict):
    def __init__(
        __self__,
        *,
        exact: Optional[_builtins.str] = ...,
        regex: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteMatchQueryParameter(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        match: Optional[
            outputs.GatewayRouteSpecHttp2RouteMatchQueryParameterMatch
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[outputs.GatewayRouteSpecHttp2RouteMatchQueryParameterMatch]: ...

@pulumi.output_type
class GatewayRouteSpecHttp2RouteMatchQueryParameterMatch(dict):
    def __init__(__self__, *, exact: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayRouteSpecHttpRoute(dict):
    def __init__(
        __self__,
        *,
        action: outputs.GatewayRouteSpecHttpRouteAction,
        match: outputs.GatewayRouteSpecHttpRouteMatch,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.GatewayRouteSpecHttpRouteAction: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> outputs.GatewayRouteSpecHttpRouteMatch: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteAction(dict):
    def __init__(
        __self__,
        *,
        target: outputs.GatewayRouteSpecHttpRouteActionTarget,
        rewrite: Optional[outputs.GatewayRouteSpecHttpRouteActionRewrite] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> outputs.GatewayRouteSpecHttpRouteActionTarget: ...
    @_builtins.property
    @pulumi.getter
    def rewrite(self) -> Optional[outputs.GatewayRouteSpecHttpRouteActionRewrite]: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteActionRewrite(dict):
    def __init__(
        __self__,
        *,
        hostname: Optional[
            outputs.GatewayRouteSpecHttpRouteActionRewriteHostname
        ] = ...,
        path: Optional[outputs.GatewayRouteSpecHttpRouteActionRewritePath] = ...,
        prefix: Optional[outputs.GatewayRouteSpecHttpRouteActionRewritePrefix] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(
        self,
    ) -> Optional[outputs.GatewayRouteSpecHttpRouteActionRewriteHostname]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[outputs.GatewayRouteSpecHttpRouteActionRewritePath]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(
        self,
    ) -> Optional[outputs.GatewayRouteSpecHttpRouteActionRewritePrefix]: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteActionRewriteHostname(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, default_target_hostname: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultTargetHostname")
    def default_target_hostname(self) -> _builtins.str: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteActionRewritePath(dict):
    def __init__(__self__, *, exact: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteActionRewritePrefix(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_prefix: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultPrefix")
    def default_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteActionTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        virtual_service: outputs.GatewayRouteSpecHttpRouteActionTargetVirtualService,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualService")
    def virtual_service(
        self,
    ) -> outputs.GatewayRouteSpecHttpRouteActionTargetVirtualService: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteActionTargetVirtualService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, virtual_service_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualServiceName")
    def virtual_service_name(self) -> _builtins.str: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        headers: Optional[Sequence[outputs.GatewayRouteSpecHttpRouteMatchHeader]] = ...,
        hostname: Optional[outputs.GatewayRouteSpecHttpRouteMatchHostname] = ...,
        path: Optional[outputs.GatewayRouteSpecHttpRouteMatchPath] = ...,
        port: Optional[_builtins.int] = ...,
        prefix: Optional[_builtins.str] = ...,
        query_parameters: Optional[
            Sequence[outputs.GatewayRouteSpecHttpRouteMatchQueryParameter]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[Sequence[outputs.GatewayRouteSpecHttpRouteMatchHeader]]: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> Optional[outputs.GatewayRouteSpecHttpRouteMatchHostname]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[outputs.GatewayRouteSpecHttpRouteMatchPath]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[Sequence[outputs.GatewayRouteSpecHttpRouteMatchQueryParameter]]: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteMatchHeader(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        invert: Optional[_builtins.bool] = ...,
        match: Optional[outputs.GatewayRouteSpecHttpRouteMatchHeaderMatch] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[outputs.GatewayRouteSpecHttpRouteMatchHeaderMatch]: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteMatchHeaderMatch(dict):
    def __init__(
        __self__,
        *,
        exact: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
        range: Optional[outputs.GatewayRouteSpecHttpRouteMatchHeaderMatchRange] = ...,
        regex: Optional[_builtins.str] = ...,
        suffix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def range(
        self,
    ) -> Optional[outputs.GatewayRouteSpecHttpRouteMatchHeaderMatchRange]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteMatchHeaderMatchRange(dict):
    def __init__(__self__, *, end: _builtins.int, start: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteMatchHostname(dict):
    def __init__(
        __self__,
        *,
        exact: Optional[_builtins.str] = ...,
        suffix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteMatchPath(dict):
    def __init__(
        __self__,
        *,
        exact: Optional[_builtins.str] = ...,
        regex: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteMatchQueryParameter(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        match: Optional[
            outputs.GatewayRouteSpecHttpRouteMatchQueryParameterMatch
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[outputs.GatewayRouteSpecHttpRouteMatchQueryParameterMatch]: ...

@pulumi.output_type
class GatewayRouteSpecHttpRouteMatchQueryParameterMatch(dict):
    def __init__(__self__, *, exact: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MeshSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        egress_filter: Optional[outputs.MeshSpecEgressFilter] = ...,
        service_discovery: Optional[outputs.MeshSpecServiceDiscovery] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressFilter")
    def egress_filter(self) -> Optional[outputs.MeshSpecEgressFilter]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDiscovery")
    def service_discovery(self) -> Optional[outputs.MeshSpecServiceDiscovery]: ...

@pulumi.output_type
class MeshSpecEgressFilter(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MeshSpecServiceDiscovery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, ip_preference: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipPreference")
    def ip_preference(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RouteSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        grpc_route: Optional[outputs.RouteSpecGrpcRoute] = ...,
        http2_route: Optional[outputs.RouteSpecHttp2Route] = ...,
        http_route: Optional[outputs.RouteSpecHttpRoute] = ...,
        priority: Optional[_builtins.int] = ...,
        tcp_route: Optional[outputs.RouteSpecTcpRoute] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="grpcRoute")
    def grpc_route(self) -> Optional[outputs.RouteSpecGrpcRoute]: ...
    @_builtins.property
    @pulumi.getter(name="http2Route")
    def http2_route(self) -> Optional[outputs.RouteSpecHttp2Route]: ...
    @_builtins.property
    @pulumi.getter(name="httpRoute")
    def http_route(self) -> Optional[outputs.RouteSpecHttpRoute]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tcpRoute")
    def tcp_route(self) -> Optional[outputs.RouteSpecTcpRoute]: ...

@pulumi.output_type
class RouteSpecGrpcRoute(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: outputs.RouteSpecGrpcRouteAction,
        match: Optional[outputs.RouteSpecGrpcRouteMatch] = ...,
        retry_policy: Optional[outputs.RouteSpecGrpcRouteRetryPolicy] = ...,
        timeout: Optional[outputs.RouteSpecGrpcRouteTimeout] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.RouteSpecGrpcRouteAction: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[outputs.RouteSpecGrpcRouteMatch]: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[outputs.RouteSpecGrpcRouteRetryPolicy]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[outputs.RouteSpecGrpcRouteTimeout]: ...

@pulumi.output_type
class RouteSpecGrpcRouteAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        weighted_targets: Sequence[outputs.RouteSpecGrpcRouteActionWeightedTarget],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weightedTargets")
    def weighted_targets(
        self,
    ) -> Sequence[outputs.RouteSpecGrpcRouteActionWeightedTarget]: ...

@pulumi.output_type
class RouteSpecGrpcRouteActionWeightedTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        virtual_node: _builtins.str,
        weight: _builtins.int,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class RouteSpecGrpcRouteMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metadatas: Optional[Sequence[outputs.RouteSpecGrpcRouteMatchMetadata]] = ...,
        method_name: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        prefix: Optional[_builtins.str] = ...,
        service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadatas(
        self,
    ) -> Optional[Sequence[outputs.RouteSpecGrpcRouteMatchMetadata]]: ...
    @_builtins.property
    @pulumi.getter(name="methodName")
    def method_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RouteSpecGrpcRouteMatchMetadata(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        invert: Optional[_builtins.bool] = ...,
        match: Optional[outputs.RouteSpecGrpcRouteMatchMetadataMatch] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[outputs.RouteSpecGrpcRouteMatchMetadataMatch]: ...

@pulumi.output_type
class RouteSpecGrpcRouteMatchMetadataMatch(dict):
    def __init__(
        __self__,
        *,
        exact: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
        range: Optional[outputs.RouteSpecGrpcRouteMatchMetadataMatchRange] = ...,
        regex: Optional[_builtins.str] = ...,
        suffix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def range(self) -> Optional[outputs.RouteSpecGrpcRouteMatchMetadataMatchRange]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RouteSpecGrpcRouteMatchMetadataMatchRange(dict):
    def __init__(__self__, *, end: _builtins.int, start: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class RouteSpecGrpcRouteRetryPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_retries: _builtins.int,
        per_retry_timeout: outputs.RouteSpecGrpcRouteRetryPolicyPerRetryTimeout,
        grpc_retry_events: Optional[Sequence[_builtins.str]] = ...,
        http_retry_events: Optional[Sequence[_builtins.str]] = ...,
        tcp_retry_events: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="perRetryTimeout")
    def per_retry_timeout(
        self,
    ) -> outputs.RouteSpecGrpcRouteRetryPolicyPerRetryTimeout: ...
    @_builtins.property
    @pulumi.getter(name="grpcRetryEvents")
    def grpc_retry_events(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="httpRetryEvents")
    def http_retry_events(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tcpRetryEvents")
    def tcp_retry_events(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RouteSpecGrpcRouteRetryPolicyPerRetryTimeout(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class RouteSpecGrpcRouteTimeout(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle: Optional[outputs.RouteSpecGrpcRouteTimeoutIdle] = ...,
        per_request: Optional[outputs.RouteSpecGrpcRouteTimeoutPerRequest] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(self) -> Optional[outputs.RouteSpecGrpcRouteTimeoutIdle]: ...
    @_builtins.property
    @pulumi.getter(name="perRequest")
    def per_request(self) -> Optional[outputs.RouteSpecGrpcRouteTimeoutPerRequest]: ...

@pulumi.output_type
class RouteSpecGrpcRouteTimeoutIdle(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class RouteSpecGrpcRouteTimeoutPerRequest(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class RouteSpecHttp2Route(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: outputs.RouteSpecHttp2RouteAction,
        match: outputs.RouteSpecHttp2RouteMatch,
        retry_policy: Optional[outputs.RouteSpecHttp2RouteRetryPolicy] = ...,
        timeout: Optional[outputs.RouteSpecHttp2RouteTimeout] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.RouteSpecHttp2RouteAction: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> outputs.RouteSpecHttp2RouteMatch: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[outputs.RouteSpecHttp2RouteRetryPolicy]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[outputs.RouteSpecHttp2RouteTimeout]: ...

@pulumi.output_type
class RouteSpecHttp2RouteAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        weighted_targets: Sequence[outputs.RouteSpecHttp2RouteActionWeightedTarget],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weightedTargets")
    def weighted_targets(
        self,
    ) -> Sequence[outputs.RouteSpecHttp2RouteActionWeightedTarget]: ...

@pulumi.output_type
class RouteSpecHttp2RouteActionWeightedTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        virtual_node: _builtins.str,
        weight: _builtins.int,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class RouteSpecHttp2RouteMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        headers: Optional[Sequence[outputs.RouteSpecHttp2RouteMatchHeader]] = ...,
        method: Optional[_builtins.str] = ...,
        path: Optional[outputs.RouteSpecHttp2RouteMatchPath] = ...,
        port: Optional[_builtins.int] = ...,
        prefix: Optional[_builtins.str] = ...,
        query_parameters: Optional[
            Sequence[outputs.RouteSpecHttp2RouteMatchQueryParameter]
        ] = ...,
        scheme: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RouteSpecHttp2RouteMatchHeader]]: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[outputs.RouteSpecHttp2RouteMatchPath]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[Sequence[outputs.RouteSpecHttp2RouteMatchQueryParameter]]: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RouteSpecHttp2RouteMatchHeader(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        invert: Optional[_builtins.bool] = ...,
        match: Optional[outputs.RouteSpecHttp2RouteMatchHeaderMatch] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[outputs.RouteSpecHttp2RouteMatchHeaderMatch]: ...

@pulumi.output_type
class RouteSpecHttp2RouteMatchHeaderMatch(dict):
    def __init__(
        __self__,
        *,
        exact: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
        range: Optional[outputs.RouteSpecHttp2RouteMatchHeaderMatchRange] = ...,
        regex: Optional[_builtins.str] = ...,
        suffix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def range(self) -> Optional[outputs.RouteSpecHttp2RouteMatchHeaderMatchRange]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RouteSpecHttp2RouteMatchHeaderMatchRange(dict):
    def __init__(__self__, *, end: _builtins.int, start: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class RouteSpecHttp2RouteMatchPath(dict):
    def __init__(
        __self__,
        *,
        exact: Optional[_builtins.str] = ...,
        regex: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RouteSpecHttp2RouteMatchQueryParameter(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        match: Optional[outputs.RouteSpecHttp2RouteMatchQueryParameterMatch] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> Optional[outputs.RouteSpecHttp2RouteMatchQueryParameterMatch]: ...

@pulumi.output_type
class RouteSpecHttp2RouteMatchQueryParameterMatch(dict):
    def __init__(__self__, *, exact: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RouteSpecHttp2RouteRetryPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_retries: _builtins.int,
        per_retry_timeout: outputs.RouteSpecHttp2RouteRetryPolicyPerRetryTimeout,
        http_retry_events: Optional[Sequence[_builtins.str]] = ...,
        tcp_retry_events: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="perRetryTimeout")
    def per_retry_timeout(
        self,
    ) -> outputs.RouteSpecHttp2RouteRetryPolicyPerRetryTimeout: ...
    @_builtins.property
    @pulumi.getter(name="httpRetryEvents")
    def http_retry_events(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tcpRetryEvents")
    def tcp_retry_events(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RouteSpecHttp2RouteRetryPolicyPerRetryTimeout(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class RouteSpecHttp2RouteTimeout(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle: Optional[outputs.RouteSpecHttp2RouteTimeoutIdle] = ...,
        per_request: Optional[outputs.RouteSpecHttp2RouteTimeoutPerRequest] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(self) -> Optional[outputs.RouteSpecHttp2RouteTimeoutIdle]: ...
    @_builtins.property
    @pulumi.getter(name="perRequest")
    def per_request(self) -> Optional[outputs.RouteSpecHttp2RouteTimeoutPerRequest]: ...

@pulumi.output_type
class RouteSpecHttp2RouteTimeoutIdle(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class RouteSpecHttp2RouteTimeoutPerRequest(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class RouteSpecHttpRoute(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: outputs.RouteSpecHttpRouteAction,
        match: outputs.RouteSpecHttpRouteMatch,
        retry_policy: Optional[outputs.RouteSpecHttpRouteRetryPolicy] = ...,
        timeout: Optional[outputs.RouteSpecHttpRouteTimeout] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.RouteSpecHttpRouteAction: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> outputs.RouteSpecHttpRouteMatch: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[outputs.RouteSpecHttpRouteRetryPolicy]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[outputs.RouteSpecHttpRouteTimeout]: ...

@pulumi.output_type
class RouteSpecHttpRouteAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        weighted_targets: Sequence[outputs.RouteSpecHttpRouteActionWeightedTarget],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weightedTargets")
    def weighted_targets(
        self,
    ) -> Sequence[outputs.RouteSpecHttpRouteActionWeightedTarget]: ...

@pulumi.output_type
class RouteSpecHttpRouteActionWeightedTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        virtual_node: _builtins.str,
        weight: _builtins.int,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class RouteSpecHttpRouteMatch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        headers: Optional[Sequence[outputs.RouteSpecHttpRouteMatchHeader]] = ...,
        method: Optional[_builtins.str] = ...,
        path: Optional[outputs.RouteSpecHttpRouteMatchPath] = ...,
        port: Optional[_builtins.int] = ...,
        prefix: Optional[_builtins.str] = ...,
        query_parameters: Optional[
            Sequence[outputs.RouteSpecHttpRouteMatchQueryParameter]
        ] = ...,
        scheme: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RouteSpecHttpRouteMatchHeader]]: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[outputs.RouteSpecHttpRouteMatchPath]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Optional[Sequence[outputs.RouteSpecHttpRouteMatchQueryParameter]]: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RouteSpecHttpRouteMatchHeader(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        invert: Optional[_builtins.bool] = ...,
        match: Optional[outputs.RouteSpecHttpRouteMatchHeaderMatch] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[outputs.RouteSpecHttpRouteMatchHeaderMatch]: ...

@pulumi.output_type
class RouteSpecHttpRouteMatchHeaderMatch(dict):
    def __init__(
        __self__,
        *,
        exact: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
        range: Optional[outputs.RouteSpecHttpRouteMatchHeaderMatchRange] = ...,
        regex: Optional[_builtins.str] = ...,
        suffix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def range(self) -> Optional[outputs.RouteSpecHttpRouteMatchHeaderMatchRange]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RouteSpecHttpRouteMatchHeaderMatchRange(dict):
    def __init__(__self__, *, end: _builtins.int, start: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class RouteSpecHttpRouteMatchPath(dict):
    def __init__(
        __self__,
        *,
        exact: Optional[_builtins.str] = ...,
        regex: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RouteSpecHttpRouteMatchQueryParameter(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        match: Optional[outputs.RouteSpecHttpRouteMatchQueryParameterMatch] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[outputs.RouteSpecHttpRouteMatchQueryParameterMatch]: ...

@pulumi.output_type
class RouteSpecHttpRouteMatchQueryParameterMatch(dict):
    def __init__(__self__, *, exact: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RouteSpecHttpRouteRetryPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_retries: _builtins.int,
        per_retry_timeout: outputs.RouteSpecHttpRouteRetryPolicyPerRetryTimeout,
        http_retry_events: Optional[Sequence[_builtins.str]] = ...,
        tcp_retry_events: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="perRetryTimeout")
    def per_retry_timeout(
        self,
    ) -> outputs.RouteSpecHttpRouteRetryPolicyPerRetryTimeout: ...
    @_builtins.property
    @pulumi.getter(name="httpRetryEvents")
    def http_retry_events(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tcpRetryEvents")
    def tcp_retry_events(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RouteSpecHttpRouteRetryPolicyPerRetryTimeout(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class RouteSpecHttpRouteTimeout(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle: Optional[outputs.RouteSpecHttpRouteTimeoutIdle] = ...,
        per_request: Optional[outputs.RouteSpecHttpRouteTimeoutPerRequest] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(self) -> Optional[outputs.RouteSpecHttpRouteTimeoutIdle]: ...
    @_builtins.property
    @pulumi.getter(name="perRequest")
    def per_request(self) -> Optional[outputs.RouteSpecHttpRouteTimeoutPerRequest]: ...

@pulumi.output_type
class RouteSpecHttpRouteTimeoutIdle(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class RouteSpecHttpRouteTimeoutPerRequest(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class RouteSpecTcpRoute(dict):
    def __init__(
        __self__,
        *,
        action: outputs.RouteSpecTcpRouteAction,
        match: Optional[outputs.RouteSpecTcpRouteMatch] = ...,
        timeout: Optional[outputs.RouteSpecTcpRouteTimeout] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.RouteSpecTcpRouteAction: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[outputs.RouteSpecTcpRouteMatch]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[outputs.RouteSpecTcpRouteTimeout]: ...

@pulumi.output_type
class RouteSpecTcpRouteAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        weighted_targets: Sequence[outputs.RouteSpecTcpRouteActionWeightedTarget],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weightedTargets")
    def weighted_targets(
        self,
    ) -> Sequence[outputs.RouteSpecTcpRouteActionWeightedTarget]: ...

@pulumi.output_type
class RouteSpecTcpRouteActionWeightedTarget(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        virtual_node: _builtins.str,
        weight: _builtins.int,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class RouteSpecTcpRouteMatch(dict):
    def __init__(__self__, *, port: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class RouteSpecTcpRouteTimeout(dict):
    def __init__(
        __self__, *, idle: Optional[outputs.RouteSpecTcpRouteTimeoutIdle] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(self) -> Optional[outputs.RouteSpecTcpRouteTimeoutIdle]: ...

@pulumi.output_type
class RouteSpecTcpRouteTimeoutIdle(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualGatewaySpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        listeners: Sequence[outputs.VirtualGatewaySpecListener],
        backend_defaults: Optional[outputs.VirtualGatewaySpecBackendDefaults] = ...,
        logging: Optional[outputs.VirtualGatewaySpecLogging] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def listeners(self) -> Sequence[outputs.VirtualGatewaySpecListener]: ...
    @_builtins.property
    @pulumi.getter(name="backendDefaults")
    def backend_defaults(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecBackendDefaults]: ...
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[outputs.VirtualGatewaySpecLogging]: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaults(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_policy: Optional[
            outputs.VirtualGatewaySpecBackendDefaultsClientPolicy
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientPolicy")
    def client_policy(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecBackendDefaultsClientPolicy]: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaultsClientPolicy(dict):
    def __init__(
        __self__,
        *,
        tls: Optional[outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTls] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tls(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTls]: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTls(dict):
    def __init__(
        __self__,
        *,
        validation: outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation,
        certificate: Optional[
            outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate
        ] = ...,
        enforce: Optional[_builtins.bool] = ...,
        ports: Optional[Sequence[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation: ...
    @_builtins.property
    @pulumi.getter
    def certificate(
        self,
    ) -> Optional[
        outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate(dict):
    def __init__(
        __self__,
        *,
        file: Optional[
            outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile
        ] = ...,
        sds: Optional[
            outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds
    ]: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_chain: _builtins.str, private_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        trust: outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust,
        subject_alternative_names: Optional[
            outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trust(
        self,
    ) -> outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Optional[
        outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames
    ]: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames(
    dict
):
    def __init__(
        __self__,
        *,
        match: outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch(
    dict
):
    def __init__(__self__, *, exacts: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust(dict):
    def __init__(
        __self__,
        *,
        acm: Optional[
            outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm
        ] = ...,
        file: Optional[
            outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile
        ] = ...,
        sds: Optional[
            outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acm(
        self,
    ) -> Optional[
        outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm
    ]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        outputs.VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds
    ]: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_authority_arns: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, certificate_chain: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualGatewaySpecListener(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        port_mapping: outputs.VirtualGatewaySpecListenerPortMapping,
        connection_pool: Optional[
            outputs.VirtualGatewaySpecListenerConnectionPool
        ] = ...,
        health_check: Optional[outputs.VirtualGatewaySpecListenerHealthCheck] = ...,
        tls: Optional[outputs.VirtualGatewaySpecListenerTls] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="portMapping")
    def port_mapping(self) -> outputs.VirtualGatewaySpecListenerPortMapping: ...
    @_builtins.property
    @pulumi.getter(name="connectionPool")
    def connection_pool(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecListenerConnectionPool]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecListenerHealthCheck]: ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[outputs.VirtualGatewaySpecListenerTls]: ...

@pulumi.output_type
class VirtualGatewaySpecListenerConnectionPool(dict):
    def __init__(
        __self__,
        *,
        grpc: Optional[outputs.VirtualGatewaySpecListenerConnectionPoolGrpc] = ...,
        http: Optional[outputs.VirtualGatewaySpecListenerConnectionPoolHttp] = ...,
        http2: Optional[outputs.VirtualGatewaySpecListenerConnectionPoolHttp2] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecListenerConnectionPoolGrpc]: ...
    @_builtins.property
    @pulumi.getter
    def http(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecListenerConnectionPoolHttp]: ...
    @_builtins.property
    @pulumi.getter
    def http2(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecListenerConnectionPoolHttp2]: ...

@pulumi.output_type
class VirtualGatewaySpecListenerConnectionPoolGrpc(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_requests: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequests")
    def max_requests(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualGatewaySpecListenerConnectionPoolHttp2(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_requests: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequests")
    def max_requests(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualGatewaySpecListenerConnectionPoolHttp(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_connections: _builtins.int,
        max_pending_requests: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxPendingRequests")
    def max_pending_requests(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class VirtualGatewaySpecListenerHealthCheck(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        healthy_threshold: _builtins.int,
        interval_millis: _builtins.int,
        protocol: _builtins.str,
        timeout_millis: _builtins.int,
        unhealthy_threshold: _builtins.int,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="intervalMillis")
    def interval_millis(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMillis")
    def timeout_millis(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class VirtualGatewaySpecListenerPortMapping(dict):
    def __init__(__self__, *, port: _builtins.int, protocol: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualGatewaySpecListenerTls(dict):
    def __init__(
        __self__,
        *,
        certificate: outputs.VirtualGatewaySpecListenerTlsCertificate,
        mode: _builtins.str,
        validation: Optional[outputs.VirtualGatewaySpecListenerTlsValidation] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> outputs.VirtualGatewaySpecListenerTlsCertificate: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecListenerTlsValidation]: ...

@pulumi.output_type
class VirtualGatewaySpecListenerTlsCertificate(dict):
    def __init__(
        __self__,
        *,
        acm: Optional[outputs.VirtualGatewaySpecListenerTlsCertificateAcm] = ...,
        file: Optional[outputs.VirtualGatewaySpecListenerTlsCertificateFile] = ...,
        sds: Optional[outputs.VirtualGatewaySpecListenerTlsCertificateSds] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acm(self) -> Optional[outputs.VirtualGatewaySpecListenerTlsCertificateAcm]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecListenerTlsCertificateFile]: ...
    @_builtins.property
    @pulumi.getter
    def sds(self) -> Optional[outputs.VirtualGatewaySpecListenerTlsCertificateSds]: ...

@pulumi.output_type
class VirtualGatewaySpecListenerTlsCertificateAcm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, certificate_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualGatewaySpecListenerTlsCertificateFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_chain: _builtins.str, private_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualGatewaySpecListenerTlsCertificateSds(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualGatewaySpecListenerTlsValidation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        trust: outputs.VirtualGatewaySpecListenerTlsValidationTrust,
        subject_alternative_names: Optional[
            outputs.VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trust(self) -> outputs.VirtualGatewaySpecListenerTlsValidationTrust: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Optional[
        outputs.VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames
    ]: ...

@pulumi.output_type
class VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames(dict):
    def __init__(
        __self__,
        *,
        match: outputs.VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> (
        outputs.VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch
    ): ...

@pulumi.output_type
class VirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch(dict):
    def __init__(__self__, *, exacts: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class VirtualGatewaySpecListenerTlsValidationTrust(dict):
    def __init__(
        __self__,
        *,
        file: Optional[outputs.VirtualGatewaySpecListenerTlsValidationTrustFile] = ...,
        sds: Optional[outputs.VirtualGatewaySpecListenerTlsValidationTrustSds] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecListenerTlsValidationTrustFile]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecListenerTlsValidationTrustSds]: ...

@pulumi.output_type
class VirtualGatewaySpecListenerTlsValidationTrustFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, certificate_chain: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualGatewaySpecListenerTlsValidationTrustSds(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualGatewaySpecLogging(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_log: Optional[outputs.VirtualGatewaySpecLoggingAccessLog] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLog")
    def access_log(self) -> Optional[outputs.VirtualGatewaySpecLoggingAccessLog]: ...

@pulumi.output_type
class VirtualGatewaySpecLoggingAccessLog(dict):
    def __init__(
        __self__,
        *,
        file: Optional[outputs.VirtualGatewaySpecLoggingAccessLogFile] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(self) -> Optional[outputs.VirtualGatewaySpecLoggingAccessLogFile]: ...

@pulumi.output_type
class VirtualGatewaySpecLoggingAccessLogFile(dict):
    def __init__(
        __self__,
        *,
        path: _builtins.str,
        format: Optional[outputs.VirtualGatewaySpecLoggingAccessLogFileFormat] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(
        self,
    ) -> Optional[outputs.VirtualGatewaySpecLoggingAccessLogFileFormat]: ...

@pulumi.output_type
class VirtualGatewaySpecLoggingAccessLogFileFormat(dict):
    def __init__(
        __self__,
        *,
        jsons: Optional[
            Sequence[outputs.VirtualGatewaySpecLoggingAccessLogFileFormatJson]
        ] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def jsons(
        self,
    ) -> Optional[
        Sequence[outputs.VirtualGatewaySpecLoggingAccessLogFileFormatJson]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualGatewaySpecLoggingAccessLogFileFormatJson(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backend_defaults: Optional[outputs.VirtualNodeSpecBackendDefaults] = ...,
        backends: Optional[Sequence[outputs.VirtualNodeSpecBackend]] = ...,
        listeners: Optional[Sequence[outputs.VirtualNodeSpecListener]] = ...,
        logging: Optional[outputs.VirtualNodeSpecLogging] = ...,
        service_discovery: Optional[outputs.VirtualNodeSpecServiceDiscovery] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendDefaults")
    def backend_defaults(self) -> Optional[outputs.VirtualNodeSpecBackendDefaults]: ...
    @_builtins.property
    @pulumi.getter
    def backends(self) -> Optional[Sequence[outputs.VirtualNodeSpecBackend]]: ...
    @_builtins.property
    @pulumi.getter
    def listeners(self) -> Optional[Sequence[outputs.VirtualNodeSpecListener]]: ...
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[outputs.VirtualNodeSpecLogging]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDiscovery")
    def service_discovery(
        self,
    ) -> Optional[outputs.VirtualNodeSpecServiceDiscovery]: ...

@pulumi.output_type
class VirtualNodeSpecBackend(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, virtual_service: outputs.VirtualNodeSpecBackendVirtualService
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualService")
    def virtual_service(self) -> outputs.VirtualNodeSpecBackendVirtualService: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaults(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_policy: Optional[
            outputs.VirtualNodeSpecBackendDefaultsClientPolicy
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientPolicy")
    def client_policy(
        self,
    ) -> Optional[outputs.VirtualNodeSpecBackendDefaultsClientPolicy]: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaultsClientPolicy(dict):
    def __init__(
        __self__,
        *,
        tls: Optional[outputs.VirtualNodeSpecBackendDefaultsClientPolicyTls] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tls(
        self,
    ) -> Optional[outputs.VirtualNodeSpecBackendDefaultsClientPolicyTls]: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaultsClientPolicyTls(dict):
    def __init__(
        __self__,
        *,
        validation: outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidation,
        certificate: Optional[
            outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate
        ] = ...,
        enforce: Optional[_builtins.bool] = ...,
        ports: Optional[Sequence[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidation: ...
    @_builtins.property
    @pulumi.getter
    def certificate(
        self,
    ) -> Optional[outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate]: ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate(dict):
    def __init__(
        __self__,
        *,
        file: Optional[
            outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile
        ] = ...,
        sds: Optional[
            outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds
    ]: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_chain: _builtins.str, private_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        trust: outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust,
        subject_alternative_names: Optional[
            outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trust(
        self,
    ) -> outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames
    ]: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames(
    dict
):
    def __init__(
        __self__,
        *,
        match: outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch(
    dict
):
    def __init__(__self__, *, exacts: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust(dict):
    def __init__(
        __self__,
        *,
        acm: Optional[
            outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm
        ] = ...,
        file: Optional[
            outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile
        ] = ...,
        sds: Optional[
            outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acm(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm
    ]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds
    ]: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_authority_arns: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, certificate_chain: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        virtual_service_name: _builtins.str,
        client_policy: Optional[
            outputs.VirtualNodeSpecBackendVirtualServiceClientPolicy
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualServiceName")
    def virtual_service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientPolicy")
    def client_policy(
        self,
    ) -> Optional[outputs.VirtualNodeSpecBackendVirtualServiceClientPolicy]: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualServiceClientPolicy(dict):
    def __init__(
        __self__,
        *,
        tls: Optional[
            outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTls
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tls(
        self,
    ) -> Optional[outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTls]: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTls(dict):
    def __init__(
        __self__,
        *,
        validation: outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation,
        certificate: Optional[
            outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate
        ] = ...,
        enforce: Optional[_builtins.bool] = ...,
        ports: Optional[Sequence[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation: ...
    @_builtins.property
    @pulumi.getter
    def certificate(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate(dict):
    def __init__(
        __self__,
        *,
        file: Optional[
            outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile
        ] = ...,
        sds: Optional[
            outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds
    ]: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_chain: _builtins.str, private_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        trust: outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust,
        subject_alternative_names: Optional[
            outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trust(
        self,
    ) -> outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames
    ]: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames(
    dict
):
    def __init__(
        __self__,
        *,
        match: outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch(
    dict
):
    def __init__(__self__, *, exacts: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust(dict):
    def __init__(
        __self__,
        *,
        acm: Optional[
            outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm
        ] = ...,
        file: Optional[
            outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile
        ] = ...,
        sds: Optional[
            outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acm(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm
    ]: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds
    ]: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_authority_arns: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, certificate_chain: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecListener(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        port_mapping: outputs.VirtualNodeSpecListenerPortMapping,
        connection_pool: Optional[outputs.VirtualNodeSpecListenerConnectionPool] = ...,
        health_check: Optional[outputs.VirtualNodeSpecListenerHealthCheck] = ...,
        outlier_detection: Optional[
            outputs.VirtualNodeSpecListenerOutlierDetection
        ] = ...,
        timeout: Optional[outputs.VirtualNodeSpecListenerTimeout] = ...,
        tls: Optional[outputs.VirtualNodeSpecListenerTls] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="portMapping")
    def port_mapping(self) -> outputs.VirtualNodeSpecListenerPortMapping: ...
    @_builtins.property
    @pulumi.getter(name="connectionPool")
    def connection_pool(
        self,
    ) -> Optional[outputs.VirtualNodeSpecListenerConnectionPool]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[outputs.VirtualNodeSpecListenerHealthCheck]: ...
    @_builtins.property
    @pulumi.getter(name="outlierDetection")
    def outlier_detection(
        self,
    ) -> Optional[outputs.VirtualNodeSpecListenerOutlierDetection]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[outputs.VirtualNodeSpecListenerTimeout]: ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[outputs.VirtualNodeSpecListenerTls]: ...

@pulumi.output_type
class VirtualNodeSpecListenerConnectionPool(dict):
    def __init__(
        __self__,
        *,
        grpc: Optional[outputs.VirtualNodeSpecListenerConnectionPoolGrpc] = ...,
        http2s: Optional[
            Sequence[outputs.VirtualNodeSpecListenerConnectionPoolHttp2]
        ] = ...,
        https: Optional[
            Sequence[outputs.VirtualNodeSpecListenerConnectionPoolHttp]
        ] = ...,
        tcps: Optional[
            Sequence[outputs.VirtualNodeSpecListenerConnectionPoolTcp]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def grpc(self) -> Optional[outputs.VirtualNodeSpecListenerConnectionPoolGrpc]: ...
    @_builtins.property
    @pulumi.getter
    def http2s(
        self,
    ) -> Optional[Sequence[outputs.VirtualNodeSpecListenerConnectionPoolHttp2]]: ...
    @_builtins.property
    @pulumi.getter
    def https(
        self,
    ) -> Optional[Sequence[outputs.VirtualNodeSpecListenerConnectionPoolHttp]]: ...
    @_builtins.property
    @pulumi.getter
    def tcps(
        self,
    ) -> Optional[Sequence[outputs.VirtualNodeSpecListenerConnectionPoolTcp]]: ...

@pulumi.output_type
class VirtualNodeSpecListenerConnectionPoolGrpc(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_requests: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequests")
    def max_requests(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerConnectionPoolHttp2(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_requests: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequests")
    def max_requests(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerConnectionPoolHttp(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_connections: _builtins.int,
        max_pending_requests: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxPendingRequests")
    def max_pending_requests(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class VirtualNodeSpecListenerConnectionPoolTcp(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_connections: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerHealthCheck(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        healthy_threshold: _builtins.int,
        interval_millis: _builtins.int,
        protocol: _builtins.str,
        timeout_millis: _builtins.int,
        unhealthy_threshold: _builtins.int,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="intervalMillis")
    def interval_millis(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMillis")
    def timeout_millis(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class VirtualNodeSpecListenerOutlierDetection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        base_ejection_duration: outputs.VirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration,
        interval: outputs.VirtualNodeSpecListenerOutlierDetectionInterval,
        max_ejection_percent: _builtins.int,
        max_server_errors: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseEjectionDuration")
    def base_ejection_duration(
        self,
    ) -> outputs.VirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> outputs.VirtualNodeSpecListenerOutlierDetectionInterval: ...
    @_builtins.property
    @pulumi.getter(name="maxEjectionPercent")
    def max_ejection_percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxServerErrors")
    def max_server_errors(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerOutlierDetectionInterval(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerPortMapping(dict):
    def __init__(__self__, *, port: _builtins.int, protocol: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecListenerTimeout(dict):
    def __init__(
        __self__,
        *,
        grpc: Optional[outputs.VirtualNodeSpecListenerTimeoutGrpc] = ...,
        http: Optional[outputs.VirtualNodeSpecListenerTimeoutHttp] = ...,
        http2: Optional[outputs.VirtualNodeSpecListenerTimeoutHttp2] = ...,
        tcp: Optional[outputs.VirtualNodeSpecListenerTimeoutTcp] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def grpc(self) -> Optional[outputs.VirtualNodeSpecListenerTimeoutGrpc]: ...
    @_builtins.property
    @pulumi.getter
    def http(self) -> Optional[outputs.VirtualNodeSpecListenerTimeoutHttp]: ...
    @_builtins.property
    @pulumi.getter
    def http2(self) -> Optional[outputs.VirtualNodeSpecListenerTimeoutHttp2]: ...
    @_builtins.property
    @pulumi.getter
    def tcp(self) -> Optional[outputs.VirtualNodeSpecListenerTimeoutTcp]: ...

@pulumi.output_type
class VirtualNodeSpecListenerTimeoutGrpc(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle: Optional[outputs.VirtualNodeSpecListenerTimeoutGrpcIdle] = ...,
        per_request: Optional[
            outputs.VirtualNodeSpecListenerTimeoutGrpcPerRequest
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(self) -> Optional[outputs.VirtualNodeSpecListenerTimeoutGrpcIdle]: ...
    @_builtins.property
    @pulumi.getter(name="perRequest")
    def per_request(
        self,
    ) -> Optional[outputs.VirtualNodeSpecListenerTimeoutGrpcPerRequest]: ...

@pulumi.output_type
class VirtualNodeSpecListenerTimeoutGrpcIdle(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerTimeoutGrpcPerRequest(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerTimeoutHttp2(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle: Optional[outputs.VirtualNodeSpecListenerTimeoutHttp2Idle] = ...,
        per_request: Optional[
            outputs.VirtualNodeSpecListenerTimeoutHttp2PerRequest
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(self) -> Optional[outputs.VirtualNodeSpecListenerTimeoutHttp2Idle]: ...
    @_builtins.property
    @pulumi.getter(name="perRequest")
    def per_request(
        self,
    ) -> Optional[outputs.VirtualNodeSpecListenerTimeoutHttp2PerRequest]: ...

@pulumi.output_type
class VirtualNodeSpecListenerTimeoutHttp2Idle(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerTimeoutHttp2PerRequest(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerTimeoutHttp(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        idle: Optional[outputs.VirtualNodeSpecListenerTimeoutHttpIdle] = ...,
        per_request: Optional[
            outputs.VirtualNodeSpecListenerTimeoutHttpPerRequest
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(self) -> Optional[outputs.VirtualNodeSpecListenerTimeoutHttpIdle]: ...
    @_builtins.property
    @pulumi.getter(name="perRequest")
    def per_request(
        self,
    ) -> Optional[outputs.VirtualNodeSpecListenerTimeoutHttpPerRequest]: ...

@pulumi.output_type
class VirtualNodeSpecListenerTimeoutHttpIdle(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerTimeoutHttpPerRequest(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerTimeoutTcp(dict):
    def __init__(
        __self__, *, idle: Optional[outputs.VirtualNodeSpecListenerTimeoutTcpIdle] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idle(self) -> Optional[outputs.VirtualNodeSpecListenerTimeoutTcpIdle]: ...

@pulumi.output_type
class VirtualNodeSpecListenerTimeoutTcpIdle(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class VirtualNodeSpecListenerTls(dict):
    def __init__(
        __self__,
        *,
        certificate: outputs.VirtualNodeSpecListenerTlsCertificate,
        mode: _builtins.str,
        validation: Optional[outputs.VirtualNodeSpecListenerTlsValidation] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> outputs.VirtualNodeSpecListenerTlsCertificate: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def validation(self) -> Optional[outputs.VirtualNodeSpecListenerTlsValidation]: ...

@pulumi.output_type
class VirtualNodeSpecListenerTlsCertificate(dict):
    def __init__(
        __self__,
        *,
        acm: Optional[outputs.VirtualNodeSpecListenerTlsCertificateAcm] = ...,
        file: Optional[outputs.VirtualNodeSpecListenerTlsCertificateFile] = ...,
        sds: Optional[outputs.VirtualNodeSpecListenerTlsCertificateSds] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acm(self) -> Optional[outputs.VirtualNodeSpecListenerTlsCertificateAcm]: ...
    @_builtins.property
    @pulumi.getter
    def file(self) -> Optional[outputs.VirtualNodeSpecListenerTlsCertificateFile]: ...
    @_builtins.property
    @pulumi.getter
    def sds(self) -> Optional[outputs.VirtualNodeSpecListenerTlsCertificateSds]: ...

@pulumi.output_type
class VirtualNodeSpecListenerTlsCertificateAcm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, certificate_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecListenerTlsCertificateFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_chain: _builtins.str, private_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecListenerTlsCertificateSds(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecListenerTlsValidation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        trust: outputs.VirtualNodeSpecListenerTlsValidationTrust,
        subject_alternative_names: Optional[
            outputs.VirtualNodeSpecListenerTlsValidationSubjectAlternativeNames
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def trust(self) -> outputs.VirtualNodeSpecListenerTlsValidationTrust: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Optional[
        outputs.VirtualNodeSpecListenerTlsValidationSubjectAlternativeNames
    ]: ...

@pulumi.output_type
class VirtualNodeSpecListenerTlsValidationSubjectAlternativeNames(dict):
    def __init__(
        __self__,
        *,
        match: outputs.VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> outputs.VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch: ...

@pulumi.output_type
class VirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch(dict):
    def __init__(__self__, *, exacts: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class VirtualNodeSpecListenerTlsValidationTrust(dict):
    def __init__(
        __self__,
        *,
        file: Optional[outputs.VirtualNodeSpecListenerTlsValidationTrustFile] = ...,
        sds: Optional[outputs.VirtualNodeSpecListenerTlsValidationTrustSds] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(
        self,
    ) -> Optional[outputs.VirtualNodeSpecListenerTlsValidationTrustFile]: ...
    @_builtins.property
    @pulumi.getter
    def sds(self) -> Optional[outputs.VirtualNodeSpecListenerTlsValidationTrustSds]: ...

@pulumi.output_type
class VirtualNodeSpecListenerTlsValidationTrustFile(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, certificate_chain: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecListenerTlsValidationTrustSds(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecLogging(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, access_log: Optional[outputs.VirtualNodeSpecLoggingAccessLog] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLog")
    def access_log(self) -> Optional[outputs.VirtualNodeSpecLoggingAccessLog]: ...

@pulumi.output_type
class VirtualNodeSpecLoggingAccessLog(dict):
    def __init__(
        __self__, *, file: Optional[outputs.VirtualNodeSpecLoggingAccessLogFile] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def file(self) -> Optional[outputs.VirtualNodeSpecLoggingAccessLogFile]: ...

@pulumi.output_type
class VirtualNodeSpecLoggingAccessLogFile(dict):
    def __init__(
        __self__,
        *,
        path: _builtins.str,
        format: Optional[outputs.VirtualNodeSpecLoggingAccessLogFileFormat] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[outputs.VirtualNodeSpecLoggingAccessLogFileFormat]: ...

@pulumi.output_type
class VirtualNodeSpecLoggingAccessLogFileFormat(dict):
    def __init__(
        __self__,
        *,
        jsons: Optional[
            Sequence[outputs.VirtualNodeSpecLoggingAccessLogFileFormatJson]
        ] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def jsons(
        self,
    ) -> Optional[Sequence[outputs.VirtualNodeSpecLoggingAccessLogFileFormatJson]]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualNodeSpecLoggingAccessLogFileFormatJson(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualNodeSpecServiceDiscovery(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aws_cloud_map: Optional[
            outputs.VirtualNodeSpecServiceDiscoveryAwsCloudMap
        ] = ...,
        dns: Optional[outputs.VirtualNodeSpecServiceDiscoveryDns] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsCloudMap")
    def aws_cloud_map(
        self,
    ) -> Optional[outputs.VirtualNodeSpecServiceDiscoveryAwsCloudMap]: ...
    @_builtins.property
    @pulumi.getter
    def dns(self) -> Optional[outputs.VirtualNodeSpecServiceDiscoveryDns]: ...

@pulumi.output_type
class VirtualNodeSpecServiceDiscoveryAwsCloudMap(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        namespace_name: _builtins.str,
        service_name: _builtins.str,
        attributes: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class VirtualNodeSpecServiceDiscoveryDns(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hostname: _builtins.str,
        ip_preference: Optional[_builtins.str] = ...,
        response_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipPreference")
    def ip_preference(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="responseType")
    def response_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualRouterSpec(dict):
    def __init__(
        __self__,
        *,
        listeners: Optional[Sequence[outputs.VirtualRouterSpecListener]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def listeners(self) -> Optional[Sequence[outputs.VirtualRouterSpecListener]]: ...

@pulumi.output_type
class VirtualRouterSpecListener(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, port_mapping: outputs.VirtualRouterSpecListenerPortMapping
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="portMapping")
    def port_mapping(self) -> outputs.VirtualRouterSpecListenerPortMapping: ...

@pulumi.output_type
class VirtualRouterSpecListenerPortMapping(dict):
    def __init__(__self__, *, port: _builtins.int, protocol: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualServiceSpec(dict):
    def __init__(
        __self__, *, provider: Optional[outputs.VirtualServiceSpecProvider] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> Optional[outputs.VirtualServiceSpecProvider]: ...

@pulumi.output_type
class VirtualServiceSpecProvider(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        virtual_node: Optional[outputs.VirtualServiceSpecProviderVirtualNode] = ...,
        virtual_router: Optional[outputs.VirtualServiceSpecProviderVirtualRouter] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(
        self,
    ) -> Optional[outputs.VirtualServiceSpecProviderVirtualNode]: ...
    @_builtins.property
    @pulumi.getter(name="virtualRouter")
    def virtual_router(
        self,
    ) -> Optional[outputs.VirtualServiceSpecProviderVirtualRouter]: ...

@pulumi.output_type
class VirtualServiceSpecProviderVirtualNode(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, virtual_node_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNodeName")
    def virtual_node_name(self) -> _builtins.str: ...

@pulumi.output_type
class VirtualServiceSpecProviderVirtualRouter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, virtual_router_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualRouterName")
    def virtual_router_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecResult(dict):
    def __init__(
        __self__,
        *,
        grpc_routes: Sequence[outputs.GetGatewayRouteSpecGrpcRouteResult],
        http2_routes: Sequence[outputs.GetGatewayRouteSpecHttp2RouteResult],
        http_routes: Sequence[outputs.GetGatewayRouteSpecHttpRouteResult],
        priority: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="grpcRoutes")
    def grpc_routes(self) -> Sequence[outputs.GetGatewayRouteSpecGrpcRouteResult]: ...
    @_builtins.property
    @pulumi.getter(name="http2Routes")
    def http2_routes(self) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteResult]: ...
    @_builtins.property
    @pulumi.getter(name="httpRoutes")
    def http_routes(self) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteResult]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...

@pulumi.output_type
class GetGatewayRouteSpecGrpcRouteResult(dict):
    def __init__(
        __self__,
        *,
        actions: Sequence[outputs.GetGatewayRouteSpecGrpcRouteActionResult],
        matches: Sequence[outputs.GetGatewayRouteSpecGrpcRouteMatchResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.GetGatewayRouteSpecGrpcRouteActionResult]: ...
    @_builtins.property
    @pulumi.getter
    def matches(self) -> Sequence[outputs.GetGatewayRouteSpecGrpcRouteMatchResult]: ...

@pulumi.output_type
class GetGatewayRouteSpecGrpcRouteActionResult(dict):
    def __init__(
        __self__,
        *,
        targets: Sequence[outputs.GetGatewayRouteSpecGrpcRouteActionTargetResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecGrpcRouteActionTargetResult]: ...

@pulumi.output_type
class GetGatewayRouteSpecGrpcRouteActionTargetResult(dict):
    def __init__(
        __self__,
        *,
        port: _builtins.int,
        virtual_services: Sequence[
            outputs.GetGatewayRouteSpecGrpcRouteActionTargetVirtualServiceResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="virtualServices")
    def virtual_services(
        self,
    ) -> Sequence[
        outputs.GetGatewayRouteSpecGrpcRouteActionTargetVirtualServiceResult
    ]: ...

@pulumi.output_type
class GetGatewayRouteSpecGrpcRouteActionTargetVirtualServiceResult(dict):
    def __init__(__self__, *, virtual_service_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualServiceName")
    def virtual_service_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecGrpcRouteMatchResult(dict):
    def __init__(
        __self__, *, port: _builtins.int, service_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteResult(dict):
    def __init__(
        __self__,
        *,
        actions: Sequence[outputs.GetGatewayRouteSpecHttp2RouteActionResult],
        matches: Sequence[outputs.GetGatewayRouteSpecHttp2RouteMatchResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteActionResult]: ...
    @_builtins.property
    @pulumi.getter
    def matches(self) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteMatchResult]: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteActionResult(dict):
    def __init__(
        __self__,
        *,
        rewrites: Sequence[outputs.GetGatewayRouteSpecHttp2RouteActionRewriteResult],
        targets: Sequence[outputs.GetGatewayRouteSpecHttp2RouteActionTargetResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rewrites(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteActionRewriteResult]: ...
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteActionTargetResult]: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteActionRewriteResult(dict):
    def __init__(
        __self__,
        *,
        hostnames: Sequence[
            outputs.GetGatewayRouteSpecHttp2RouteActionRewriteHostnameResult
        ],
        paths: Sequence[outputs.GetGatewayRouteSpecHttp2RouteActionRewritePathResult],
        prefixes: Sequence[
            outputs.GetGatewayRouteSpecHttp2RouteActionRewritePrefixResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostnames(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteActionRewriteHostnameResult]: ...
    @_builtins.property
    @pulumi.getter
    def paths(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteActionRewritePathResult]: ...
    @_builtins.property
    @pulumi.getter
    def prefixes(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteActionRewritePrefixResult]: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteActionRewriteHostnameResult(dict):
    def __init__(__self__, *, default_target_hostname: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultTargetHostname")
    def default_target_hostname(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteActionRewritePathResult(dict):
    def __init__(__self__, *, exact: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteActionRewritePrefixResult(dict):
    def __init__(
        __self__, *, default_prefix: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultPrefix")
    def default_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteActionTargetResult(dict):
    def __init__(
        __self__,
        *,
        port: _builtins.int,
        virtual_services: Sequence[
            outputs.GetGatewayRouteSpecHttp2RouteActionTargetVirtualServiceResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="virtualServices")
    def virtual_services(
        self,
    ) -> Sequence[
        outputs.GetGatewayRouteSpecHttp2RouteActionTargetVirtualServiceResult
    ]: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteActionTargetVirtualServiceResult(dict):
    def __init__(__self__, *, virtual_service_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualServiceName")
    def virtual_service_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteMatchResult(dict):
    def __init__(
        __self__,
        *,
        headers: Sequence[outputs.GetGatewayRouteSpecHttp2RouteMatchHeaderResult],
        hostnames: Sequence[outputs.GetGatewayRouteSpecHttp2RouteMatchHostnameResult],
        paths: Sequence[outputs.GetGatewayRouteSpecHttp2RouteMatchPathResult],
        port: _builtins.int,
        prefix: _builtins.str,
        query_parameters: Sequence[
            outputs.GetGatewayRouteSpecHttp2RouteMatchQueryParameterResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteMatchHeaderResult]: ...
    @_builtins.property
    @pulumi.getter
    def hostnames(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteMatchHostnameResult]: ...
    @_builtins.property
    @pulumi.getter
    def paths(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteMatchPathResult]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteMatchQueryParameterResult]: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteMatchHeaderResult(dict):
    def __init__(
        __self__,
        *,
        invert: _builtins.bool,
        matches: Sequence[outputs.GetGatewayRouteSpecHttp2RouteMatchHeaderMatchResult],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteMatchHeaderMatchResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteMatchHeaderMatchResult(dict):
    def __init__(
        __self__,
        *,
        exact: _builtins.str,
        prefix: _builtins.str,
        ranges: Sequence[
            outputs.GetGatewayRouteSpecHttp2RouteMatchHeaderMatchRangeResult
        ],
        regex: _builtins.str,
        suffix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ranges(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttp2RouteMatchHeaderMatchRangeResult]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteMatchHeaderMatchRangeResult(dict):
    def __init__(__self__, *, end: _builtins.int, start: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteMatchHostnameResult(dict):
    def __init__(__self__, *, exact: _builtins.str, suffix: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteMatchPathResult(dict):
    def __init__(__self__, *, exact: _builtins.str, regex: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteMatchQueryParameterResult(dict):
    def __init__(
        __self__,
        *,
        matches: Sequence[
            outputs.GetGatewayRouteSpecHttp2RouteMatchQueryParameterMatchResult
        ],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[
        outputs.GetGatewayRouteSpecHttp2RouteMatchQueryParameterMatchResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttp2RouteMatchQueryParameterMatchResult(dict):
    def __init__(__self__, *, exact: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteResult(dict):
    def __init__(
        __self__,
        *,
        actions: Sequence[outputs.GetGatewayRouteSpecHttpRouteActionResult],
        matches: Sequence[outputs.GetGatewayRouteSpecHttpRouteMatchResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteActionResult]: ...
    @_builtins.property
    @pulumi.getter
    def matches(self) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteMatchResult]: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteActionResult(dict):
    def __init__(
        __self__,
        *,
        rewrites: Sequence[outputs.GetGatewayRouteSpecHttpRouteActionRewriteResult],
        targets: Sequence[outputs.GetGatewayRouteSpecHttpRouteActionTargetResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rewrites(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteActionRewriteResult]: ...
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteActionTargetResult]: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteActionRewriteResult(dict):
    def __init__(
        __self__,
        *,
        hostnames: Sequence[
            outputs.GetGatewayRouteSpecHttpRouteActionRewriteHostnameResult
        ],
        paths: Sequence[outputs.GetGatewayRouteSpecHttpRouteActionRewritePathResult],
        prefixes: Sequence[
            outputs.GetGatewayRouteSpecHttpRouteActionRewritePrefixResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostnames(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteActionRewriteHostnameResult]: ...
    @_builtins.property
    @pulumi.getter
    def paths(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteActionRewritePathResult]: ...
    @_builtins.property
    @pulumi.getter
    def prefixes(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteActionRewritePrefixResult]: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteActionRewriteHostnameResult(dict):
    def __init__(__self__, *, default_target_hostname: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultTargetHostname")
    def default_target_hostname(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteActionRewritePathResult(dict):
    def __init__(__self__, *, exact: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteActionRewritePrefixResult(dict):
    def __init__(
        __self__, *, default_prefix: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultPrefix")
    def default_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteActionTargetResult(dict):
    def __init__(
        __self__,
        *,
        port: _builtins.int,
        virtual_services: Sequence[
            outputs.GetGatewayRouteSpecHttpRouteActionTargetVirtualServiceResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="virtualServices")
    def virtual_services(
        self,
    ) -> Sequence[
        outputs.GetGatewayRouteSpecHttpRouteActionTargetVirtualServiceResult
    ]: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteActionTargetVirtualServiceResult(dict):
    def __init__(__self__, *, virtual_service_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualServiceName")
    def virtual_service_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteMatchResult(dict):
    def __init__(
        __self__,
        *,
        headers: Sequence[outputs.GetGatewayRouteSpecHttpRouteMatchHeaderResult],
        hostnames: Sequence[outputs.GetGatewayRouteSpecHttpRouteMatchHostnameResult],
        paths: Sequence[outputs.GetGatewayRouteSpecHttpRouteMatchPathResult],
        port: _builtins.int,
        prefix: _builtins.str,
        query_parameters: Sequence[
            outputs.GetGatewayRouteSpecHttpRouteMatchQueryParameterResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteMatchHeaderResult]: ...
    @_builtins.property
    @pulumi.getter
    def hostnames(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteMatchHostnameResult]: ...
    @_builtins.property
    @pulumi.getter
    def paths(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteMatchPathResult]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteMatchQueryParameterResult]: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteMatchHeaderResult(dict):
    def __init__(
        __self__,
        *,
        invert: _builtins.bool,
        matches: Sequence[outputs.GetGatewayRouteSpecHttpRouteMatchHeaderMatchResult],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteMatchHeaderMatchResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteMatchHeaderMatchResult(dict):
    def __init__(
        __self__,
        *,
        exact: _builtins.str,
        prefix: _builtins.str,
        ranges: Sequence[
            outputs.GetGatewayRouteSpecHttpRouteMatchHeaderMatchRangeResult
        ],
        regex: _builtins.str,
        suffix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ranges(
        self,
    ) -> Sequence[outputs.GetGatewayRouteSpecHttpRouteMatchHeaderMatchRangeResult]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteMatchHeaderMatchRangeResult(dict):
    def __init__(__self__, *, end: _builtins.int, start: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteMatchHostnameResult(dict):
    def __init__(__self__, *, exact: _builtins.str, suffix: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteMatchPathResult(dict):
    def __init__(__self__, *, exact: _builtins.str, regex: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteMatchQueryParameterResult(dict):
    def __init__(
        __self__,
        *,
        matches: Sequence[
            outputs.GetGatewayRouteSpecHttpRouteMatchQueryParameterMatchResult
        ],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[
        outputs.GetGatewayRouteSpecHttpRouteMatchQueryParameterMatchResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetGatewayRouteSpecHttpRouteMatchQueryParameterMatchResult(dict):
    def __init__(__self__, *, exact: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...

@pulumi.output_type
class GetMeshSpecResult(dict):
    def __init__(
        __self__,
        *,
        egress_filters: Sequence[outputs.GetMeshSpecEgressFilterResult],
        service_discoveries: Sequence[outputs.GetMeshSpecServiceDiscoveryResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="egressFilters")
    def egress_filters(self) -> Sequence[outputs.GetMeshSpecEgressFilterResult]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDiscoveries")
    def service_discoveries(
        self,
    ) -> Sequence[outputs.GetMeshSpecServiceDiscoveryResult]: ...

@pulumi.output_type
class GetMeshSpecEgressFilterResult(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetMeshSpecServiceDiscoveryResult(dict):
    def __init__(__self__, *, ip_preference: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipPreference")
    def ip_preference(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecResult(dict):
    def __init__(
        __self__,
        *,
        grpc_routes: Sequence[outputs.GetRouteSpecGrpcRouteResult],
        http2_routes: Sequence[outputs.GetRouteSpecHttp2RouteResult],
        http_routes: Sequence[outputs.GetRouteSpecHttpRouteResult],
        priority: _builtins.int,
        tcp_routes: Sequence[outputs.GetRouteSpecTcpRouteResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="grpcRoutes")
    def grpc_routes(self) -> Sequence[outputs.GetRouteSpecGrpcRouteResult]: ...
    @_builtins.property
    @pulumi.getter(name="http2Routes")
    def http2_routes(self) -> Sequence[outputs.GetRouteSpecHttp2RouteResult]: ...
    @_builtins.property
    @pulumi.getter(name="httpRoutes")
    def http_routes(self) -> Sequence[outputs.GetRouteSpecHttpRouteResult]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="tcpRoutes")
    def tcp_routes(self) -> Sequence[outputs.GetRouteSpecTcpRouteResult]: ...

@pulumi.output_type
class GetRouteSpecGrpcRouteResult(dict):
    def __init__(
        __self__,
        *,
        actions: Sequence[outputs.GetRouteSpecGrpcRouteActionResult],
        matches: Sequence[outputs.GetRouteSpecGrpcRouteMatchResult],
        retry_policies: Sequence[outputs.GetRouteSpecGrpcRouteRetryPolicyResult],
        timeouts: Sequence[outputs.GetRouteSpecGrpcRouteTimeoutResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.GetRouteSpecGrpcRouteActionResult]: ...
    @_builtins.property
    @pulumi.getter
    def matches(self) -> Sequence[outputs.GetRouteSpecGrpcRouteMatchResult]: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicies")
    def retry_policies(
        self,
    ) -> Sequence[outputs.GetRouteSpecGrpcRouteRetryPolicyResult]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Sequence[outputs.GetRouteSpecGrpcRouteTimeoutResult]: ...

@pulumi.output_type
class GetRouteSpecGrpcRouteActionResult(dict):
    def __init__(
        __self__,
        *,
        weighted_targets: Sequence[
            outputs.GetRouteSpecGrpcRouteActionWeightedTargetResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weightedTargets")
    def weighted_targets(
        self,
    ) -> Sequence[outputs.GetRouteSpecGrpcRouteActionWeightedTargetResult]: ...

@pulumi.output_type
class GetRouteSpecGrpcRouteActionWeightedTargetResult(dict):
    def __init__(
        __self__,
        *,
        port: _builtins.int,
        virtual_node: _builtins.str,
        weight: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecGrpcRouteMatchResult(dict):
    def __init__(
        __self__,
        *,
        metadatas: Sequence[outputs.GetRouteSpecGrpcRouteMatchMetadataResult],
        method_name: _builtins.str,
        port: _builtins.int,
        prefix: _builtins.str,
        service_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadatas(
        self,
    ) -> Sequence[outputs.GetRouteSpecGrpcRouteMatchMetadataResult]: ...
    @_builtins.property
    @pulumi.getter(name="methodName")
    def method_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecGrpcRouteMatchMetadataResult(dict):
    def __init__(
        __self__,
        *,
        invert: _builtins.bool,
        matches: Sequence[outputs.GetRouteSpecGrpcRouteMatchMetadataMatchResult],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[outputs.GetRouteSpecGrpcRouteMatchMetadataMatchResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecGrpcRouteMatchMetadataMatchResult(dict):
    def __init__(
        __self__,
        *,
        exact: _builtins.str,
        prefix: _builtins.str,
        ranges: Sequence[outputs.GetRouteSpecGrpcRouteMatchMetadataMatchRangeResult],
        regex: _builtins.str,
        suffix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ranges(
        self,
    ) -> Sequence[outputs.GetRouteSpecGrpcRouteMatchMetadataMatchRangeResult]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecGrpcRouteMatchMetadataMatchRangeResult(dict):
    def __init__(__self__, *, end: _builtins.int, start: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecGrpcRouteRetryPolicyResult(dict):
    def __init__(
        __self__,
        *,
        grpc_retry_events: Sequence[_builtins.str],
        http_retry_events: Sequence[_builtins.str],
        max_retries: _builtins.int,
        per_retry_timeouts: Sequence[
            outputs.GetRouteSpecGrpcRouteRetryPolicyPerRetryTimeoutResult
        ],
        tcp_retry_events: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="grpcRetryEvents")
    def grpc_retry_events(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpRetryEvents")
    def http_retry_events(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="perRetryTimeouts")
    def per_retry_timeouts(
        self,
    ) -> Sequence[outputs.GetRouteSpecGrpcRouteRetryPolicyPerRetryTimeoutResult]: ...
    @_builtins.property
    @pulumi.getter(name="tcpRetryEvents")
    def tcp_retry_events(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetRouteSpecGrpcRouteRetryPolicyPerRetryTimeoutResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecGrpcRouteTimeoutResult(dict):
    def __init__(
        __self__,
        *,
        idles: Sequence[outputs.GetRouteSpecGrpcRouteTimeoutIdleResult],
        per_requests: Sequence[outputs.GetRouteSpecGrpcRouteTimeoutPerRequestResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idles(self) -> Sequence[outputs.GetRouteSpecGrpcRouteTimeoutIdleResult]: ...
    @_builtins.property
    @pulumi.getter(name="perRequests")
    def per_requests(
        self,
    ) -> Sequence[outputs.GetRouteSpecGrpcRouteTimeoutPerRequestResult]: ...

@pulumi.output_type
class GetRouteSpecGrpcRouteTimeoutIdleResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecGrpcRouteTimeoutPerRequestResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteResult(dict):
    def __init__(
        __self__,
        *,
        actions: Sequence[outputs.GetRouteSpecHttp2RouteActionResult],
        matches: Sequence[outputs.GetRouteSpecHttp2RouteMatchResult],
        retry_policies: Sequence[outputs.GetRouteSpecHttp2RouteRetryPolicyResult],
        timeouts: Sequence[outputs.GetRouteSpecHttp2RouteTimeoutResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.GetRouteSpecHttp2RouteActionResult]: ...
    @_builtins.property
    @pulumi.getter
    def matches(self) -> Sequence[outputs.GetRouteSpecHttp2RouteMatchResult]: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicies")
    def retry_policies(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttp2RouteRetryPolicyResult]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Sequence[outputs.GetRouteSpecHttp2RouteTimeoutResult]: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteActionResult(dict):
    def __init__(
        __self__,
        *,
        weighted_targets: Sequence[
            outputs.GetRouteSpecHttp2RouteActionWeightedTargetResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weightedTargets")
    def weighted_targets(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttp2RouteActionWeightedTargetResult]: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteActionWeightedTargetResult(dict):
    def __init__(
        __self__,
        *,
        port: _builtins.int,
        virtual_node: _builtins.str,
        weight: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteMatchResult(dict):
    def __init__(
        __self__,
        *,
        headers: Sequence[outputs.GetRouteSpecHttp2RouteMatchHeaderResult],
        method: _builtins.str,
        paths: Sequence[outputs.GetRouteSpecHttp2RouteMatchPathResult],
        port: _builtins.int,
        prefix: _builtins.str,
        query_parameters: Sequence[
            outputs.GetRouteSpecHttp2RouteMatchQueryParameterResult
        ],
        scheme: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Sequence[outputs.GetRouteSpecHttp2RouteMatchHeaderResult]: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Sequence[outputs.GetRouteSpecHttp2RouteMatchPathResult]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttp2RouteMatchQueryParameterResult]: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteMatchHeaderResult(dict):
    def __init__(
        __self__,
        *,
        invert: _builtins.bool,
        matches: Sequence[outputs.GetRouteSpecHttp2RouteMatchHeaderMatchResult],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttp2RouteMatchHeaderMatchResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteMatchHeaderMatchResult(dict):
    def __init__(
        __self__,
        *,
        exact: _builtins.str,
        prefix: _builtins.str,
        ranges: Sequence[outputs.GetRouteSpecHttp2RouteMatchHeaderMatchRangeResult],
        regex: _builtins.str,
        suffix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ranges(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttp2RouteMatchHeaderMatchRangeResult]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteMatchHeaderMatchRangeResult(dict):
    def __init__(__self__, *, end: _builtins.int, start: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteMatchPathResult(dict):
    def __init__(__self__, *, exact: _builtins.str, regex: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteMatchQueryParameterResult(dict):
    def __init__(
        __self__,
        *,
        matches: Sequence[outputs.GetRouteSpecHttp2RouteMatchQueryParameterMatchResult],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttp2RouteMatchQueryParameterMatchResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteMatchQueryParameterMatchResult(dict):
    def __init__(__self__, *, exact: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteRetryPolicyResult(dict):
    def __init__(
        __self__,
        *,
        http_retry_events: Sequence[_builtins.str],
        max_retries: _builtins.int,
        per_retry_timeouts: Sequence[
            outputs.GetRouteSpecHttp2RouteRetryPolicyPerRetryTimeoutResult
        ],
        tcp_retry_events: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpRetryEvents")
    def http_retry_events(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="perRetryTimeouts")
    def per_retry_timeouts(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttp2RouteRetryPolicyPerRetryTimeoutResult]: ...
    @_builtins.property
    @pulumi.getter(name="tcpRetryEvents")
    def tcp_retry_events(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteRetryPolicyPerRetryTimeoutResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteTimeoutResult(dict):
    def __init__(
        __self__,
        *,
        idles: Sequence[outputs.GetRouteSpecHttp2RouteTimeoutIdleResult],
        per_requests: Sequence[outputs.GetRouteSpecHttp2RouteTimeoutPerRequestResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idles(self) -> Sequence[outputs.GetRouteSpecHttp2RouteTimeoutIdleResult]: ...
    @_builtins.property
    @pulumi.getter(name="perRequests")
    def per_requests(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttp2RouteTimeoutPerRequestResult]: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteTimeoutIdleResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecHttp2RouteTimeoutPerRequestResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecHttpRouteResult(dict):
    def __init__(
        __self__,
        *,
        actions: Sequence[outputs.GetRouteSpecHttpRouteActionResult],
        matches: Sequence[outputs.GetRouteSpecHttpRouteMatchResult],
        retry_policies: Sequence[outputs.GetRouteSpecHttpRouteRetryPolicyResult],
        timeouts: Sequence[outputs.GetRouteSpecHttpRouteTimeoutResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.GetRouteSpecHttpRouteActionResult]: ...
    @_builtins.property
    @pulumi.getter
    def matches(self) -> Sequence[outputs.GetRouteSpecHttpRouteMatchResult]: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicies")
    def retry_policies(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttpRouteRetryPolicyResult]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Sequence[outputs.GetRouteSpecHttpRouteTimeoutResult]: ...

@pulumi.output_type
class GetRouteSpecHttpRouteActionResult(dict):
    def __init__(
        __self__,
        *,
        weighted_targets: Sequence[
            outputs.GetRouteSpecHttpRouteActionWeightedTargetResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weightedTargets")
    def weighted_targets(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttpRouteActionWeightedTargetResult]: ...

@pulumi.output_type
class GetRouteSpecHttpRouteActionWeightedTargetResult(dict):
    def __init__(
        __self__,
        *,
        port: _builtins.int,
        virtual_node: _builtins.str,
        weight: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecHttpRouteMatchResult(dict):
    def __init__(
        __self__,
        *,
        headers: Sequence[outputs.GetRouteSpecHttpRouteMatchHeaderResult],
        method: _builtins.str,
        paths: Sequence[outputs.GetRouteSpecHttpRouteMatchPathResult],
        port: _builtins.int,
        prefix: _builtins.str,
        query_parameters: Sequence[
            outputs.GetRouteSpecHttpRouteMatchQueryParameterResult
        ],
        scheme: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Sequence[outputs.GetRouteSpecHttpRouteMatchHeaderResult]: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def paths(self) -> Sequence[outputs.GetRouteSpecHttpRouteMatchPathResult]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryParameters")
    def query_parameters(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttpRouteMatchQueryParameterResult]: ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecHttpRouteMatchHeaderResult(dict):
    def __init__(
        __self__,
        *,
        invert: _builtins.bool,
        matches: Sequence[outputs.GetRouteSpecHttpRouteMatchHeaderMatchResult],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def invert(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttpRouteMatchHeaderMatchResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecHttpRouteMatchHeaderMatchResult(dict):
    def __init__(
        __self__,
        *,
        exact: _builtins.str,
        prefix: _builtins.str,
        ranges: Sequence[outputs.GetRouteSpecHttpRouteMatchHeaderMatchRangeResult],
        regex: _builtins.str,
        suffix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ranges(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttpRouteMatchHeaderMatchRangeResult]: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecHttpRouteMatchHeaderMatchRangeResult(dict):
    def __init__(__self__, *, end: _builtins.int, start: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecHttpRouteMatchPathResult(dict):
    def __init__(__self__, *, exact: _builtins.str, regex: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecHttpRouteMatchQueryParameterResult(dict):
    def __init__(
        __self__,
        *,
        matches: Sequence[outputs.GetRouteSpecHttpRouteMatchQueryParameterMatchResult],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttpRouteMatchQueryParameterMatchResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecHttpRouteMatchQueryParameterMatchResult(dict):
    def __init__(__self__, *, exact: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exact(self) -> _builtins.str: ...

@pulumi.output_type
class GetRouteSpecHttpRouteRetryPolicyResult(dict):
    def __init__(
        __self__,
        *,
        http_retry_events: Sequence[_builtins.str],
        max_retries: _builtins.int,
        per_retry_timeouts: Sequence[
            outputs.GetRouteSpecHttpRouteRetryPolicyPerRetryTimeoutResult
        ],
        tcp_retry_events: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpRetryEvents")
    def http_retry_events(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="perRetryTimeouts")
    def per_retry_timeouts(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttpRouteRetryPolicyPerRetryTimeoutResult]: ...
    @_builtins.property
    @pulumi.getter(name="tcpRetryEvents")
    def tcp_retry_events(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetRouteSpecHttpRouteRetryPolicyPerRetryTimeoutResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecHttpRouteTimeoutResult(dict):
    def __init__(
        __self__,
        *,
        idles: Sequence[outputs.GetRouteSpecHttpRouteTimeoutIdleResult],
        per_requests: Sequence[outputs.GetRouteSpecHttpRouteTimeoutPerRequestResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idles(self) -> Sequence[outputs.GetRouteSpecHttpRouteTimeoutIdleResult]: ...
    @_builtins.property
    @pulumi.getter(name="perRequests")
    def per_requests(
        self,
    ) -> Sequence[outputs.GetRouteSpecHttpRouteTimeoutPerRequestResult]: ...

@pulumi.output_type
class GetRouteSpecHttpRouteTimeoutIdleResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecHttpRouteTimeoutPerRequestResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecTcpRouteResult(dict):
    def __init__(
        __self__,
        *,
        actions: Sequence[outputs.GetRouteSpecTcpRouteActionResult],
        matches: Sequence[outputs.GetRouteSpecTcpRouteMatchResult],
        timeouts: Sequence[outputs.GetRouteSpecTcpRouteTimeoutResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.GetRouteSpecTcpRouteActionResult]: ...
    @_builtins.property
    @pulumi.getter
    def matches(self) -> Sequence[outputs.GetRouteSpecTcpRouteMatchResult]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Sequence[outputs.GetRouteSpecTcpRouteTimeoutResult]: ...

@pulumi.output_type
class GetRouteSpecTcpRouteActionResult(dict):
    def __init__(
        __self__,
        *,
        weighted_targets: Sequence[
            outputs.GetRouteSpecTcpRouteActionWeightedTargetResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weightedTargets")
    def weighted_targets(
        self,
    ) -> Sequence[outputs.GetRouteSpecTcpRouteActionWeightedTargetResult]: ...

@pulumi.output_type
class GetRouteSpecTcpRouteActionWeightedTargetResult(dict):
    def __init__(
        __self__,
        *,
        port: _builtins.int,
        virtual_node: _builtins.str,
        weight: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="virtualNode")
    def virtual_node(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecTcpRouteMatchResult(dict):
    def __init__(__self__, *, port: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class GetRouteSpecTcpRouteTimeoutResult(dict):
    def __init__(
        __self__, *, idles: Sequence[outputs.GetRouteSpecTcpRouteTimeoutIdleResult]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idles(self) -> Sequence[outputs.GetRouteSpecTcpRouteTimeoutIdleResult]: ...

@pulumi.output_type
class GetRouteSpecTcpRouteTimeoutIdleResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualGatewaySpecResult(dict):
    def __init__(
        __self__,
        *,
        backend_defaults: Sequence[outputs.GetVirtualGatewaySpecBackendDefaultResult],
        listeners: Sequence[outputs.GetVirtualGatewaySpecListenerResult],
        loggings: Sequence[outputs.GetVirtualGatewaySpecLoggingResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendDefaults")
    def backend_defaults(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecBackendDefaultResult]: ...
    @_builtins.property
    @pulumi.getter
    def listeners(self) -> Sequence[outputs.GetVirtualGatewaySpecListenerResult]: ...
    @_builtins.property
    @pulumi.getter
    def loggings(self) -> Sequence[outputs.GetVirtualGatewaySpecLoggingResult]: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultResult(dict):
    def __init__(
        __self__,
        *,
        client_policies: Sequence[
            outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientPolicies")
    def client_policies(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyResult]: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultClientPolicyResult(dict):
    def __init__(
        __self__,
        *,
        tls: Sequence[outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tls(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlResult]: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultClientPolicyTlResult(dict):
    def __init__(
        __self__,
        *,
        certificates: Sequence[
            outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlCertificateResult
        ],
        enforce: _builtins.bool,
        ports: Sequence[_builtins.int],
        validations: Sequence[
            outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlCertificateResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def validations(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationResult
    ]: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultClientPolicyTlCertificateResult(dict):
    def __init__(
        __self__,
        *,
        files: Sequence[
            outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlCertificateFileResult
        ],
        sds: Sequence[
            outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlCertificateSdResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlCertificateFileResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlCertificateSdResult
    ]: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultClientPolicyTlCertificateFileResult(dict):
    def __init__(
        __self__, *, certificate_chain: _builtins.str, private_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultClientPolicyTlCertificateSdResult(dict):
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationResult(dict):
    def __init__(
        __self__,
        *,
        subject_alternative_names: Sequence[
            outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationSubjectAlternativeNameResult
        ],
        trusts: Sequence[
            outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationTrustResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationSubjectAlternativeNameResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def trusts(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationTrustResult
    ]: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationSubjectAlternativeNameResult(
    dict
):
    def __init__(
        __self__,
        *,
        matches: Sequence[
            outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationSubjectAlternativeNameMatchResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationSubjectAlternativeNameMatchResult
    ]: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationSubjectAlternativeNameMatchResult(
    dict
):
    def __init__(__self__, *, exacts: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationTrustResult(dict):
    def __init__(
        __self__,
        *,
        acms: Sequence[
            outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationTrustAcmResult
        ],
        files: Sequence[
            outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationTrustFileResult
        ],
        sds: Sequence[
            outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationTrustSdResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acms(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationTrustAcmResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationTrustFileResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationTrustSdResult
    ]: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationTrustAcmResult(dict):
    def __init__(
        __self__, *, certificate_authority_arns: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationTrustFileResult(dict):
    def __init__(__self__, *, certificate_chain: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualGatewaySpecBackendDefaultClientPolicyTlValidationTrustSdResult(dict):
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerResult(dict):
    def __init__(
        __self__,
        *,
        connection_pools: Sequence[
            outputs.GetVirtualGatewaySpecListenerConnectionPoolResult
        ],
        health_checks: Sequence[outputs.GetVirtualGatewaySpecListenerHealthCheckResult],
        port_mappings: Sequence[outputs.GetVirtualGatewaySpecListenerPortMappingResult],
        tls: Sequence[outputs.GetVirtualGatewaySpecListenerTlResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionPools")
    def connection_pools(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerConnectionPoolResult]: ...
    @_builtins.property
    @pulumi.getter(name="healthChecks")
    def health_checks(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerHealthCheckResult]: ...
    @_builtins.property
    @pulumi.getter(name="portMappings")
    def port_mappings(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerPortMappingResult]: ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Sequence[outputs.GetVirtualGatewaySpecListenerTlResult]: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerConnectionPoolResult(dict):
    def __init__(
        __self__,
        *,
        grpcs: Sequence[outputs.GetVirtualGatewaySpecListenerConnectionPoolGrpcResult],
        http2s: Sequence[
            outputs.GetVirtualGatewaySpecListenerConnectionPoolHttp2Result
        ],
        https: Sequence[outputs.GetVirtualGatewaySpecListenerConnectionPoolHttpResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def grpcs(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerConnectionPoolGrpcResult]: ...
    @_builtins.property
    @pulumi.getter
    def http2s(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerConnectionPoolHttp2Result]: ...
    @_builtins.property
    @pulumi.getter
    def https(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerConnectionPoolHttpResult]: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerConnectionPoolGrpcResult(dict):
    def __init__(__self__, *, max_requests: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequests")
    def max_requests(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerConnectionPoolHttp2Result(dict):
    def __init__(__self__, *, max_requests: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequests")
    def max_requests(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerConnectionPoolHttpResult(dict):
    def __init__(
        __self__, *, max_connections: _builtins.int, max_pending_requests: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxPendingRequests")
    def max_pending_requests(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerHealthCheckResult(dict):
    def __init__(
        __self__,
        *,
        healthy_threshold: _builtins.int,
        interval_millis: _builtins.int,
        path: _builtins.str,
        port: _builtins.int,
        protocol: _builtins.str,
        timeout_millis: _builtins.int,
        unhealthy_threshold: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="intervalMillis")
    def interval_millis(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMillis")
    def timeout_millis(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerPortMappingResult(dict):
    def __init__(__self__, *, port: _builtins.int, protocol: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerTlResult(dict):
    def __init__(
        __self__,
        *,
        certificates: Sequence[
            outputs.GetVirtualGatewaySpecListenerTlCertificateResult
        ],
        mode: _builtins.str,
        validations: Sequence[outputs.GetVirtualGatewaySpecListenerTlValidationResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerTlCertificateResult]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def validations(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerTlValidationResult]: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerTlCertificateResult(dict):
    def __init__(
        __self__,
        *,
        acms: Sequence[outputs.GetVirtualGatewaySpecListenerTlCertificateAcmResult],
        files: Sequence[outputs.GetVirtualGatewaySpecListenerTlCertificateFileResult],
        sds: Sequence[outputs.GetVirtualGatewaySpecListenerTlCertificateSdResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acms(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerTlCertificateAcmResult]: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerTlCertificateFileResult]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerTlCertificateSdResult]: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerTlCertificateAcmResult(dict):
    def __init__(__self__, *, certificate_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerTlCertificateFileResult(dict):
    def __init__(
        __self__, *, certificate_chain: _builtins.str, private_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerTlCertificateSdResult(dict):
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerTlValidationResult(dict):
    def __init__(
        __self__,
        *,
        subject_alternative_names: Sequence[
            outputs.GetVirtualGatewaySpecListenerTlValidationSubjectAlternativeNameResult
        ],
        trusts: Sequence[outputs.GetVirtualGatewaySpecListenerTlValidationTrustResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecListenerTlValidationSubjectAlternativeNameResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def trusts(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerTlValidationTrustResult]: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerTlValidationSubjectAlternativeNameResult(dict):
    def __init__(
        __self__,
        *,
        matches: Sequence[
            outputs.GetVirtualGatewaySpecListenerTlValidationSubjectAlternativeNameMatchResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecListenerTlValidationSubjectAlternativeNameMatchResult
    ]: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerTlValidationSubjectAlternativeNameMatchResult(dict):
    def __init__(__self__, *, exacts: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerTlValidationTrustResult(dict):
    def __init__(
        __self__,
        *,
        files: Sequence[
            outputs.GetVirtualGatewaySpecListenerTlValidationTrustFileResult
        ],
        sds: Sequence[outputs.GetVirtualGatewaySpecListenerTlValidationTrustSdResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerTlValidationTrustFileResult]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecListenerTlValidationTrustSdResult]: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerTlValidationTrustFileResult(dict):
    def __init__(__self__, *, certificate_chain: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualGatewaySpecListenerTlValidationTrustSdResult(dict):
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualGatewaySpecLoggingResult(dict):
    def __init__(
        __self__,
        *,
        access_logs: Sequence[outputs.GetVirtualGatewaySpecLoggingAccessLogResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLogs")
    def access_logs(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecLoggingAccessLogResult]: ...

@pulumi.output_type
class GetVirtualGatewaySpecLoggingAccessLogResult(dict):
    def __init__(
        __self__,
        *,
        files: Sequence[outputs.GetVirtualGatewaySpecLoggingAccessLogFileResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecLoggingAccessLogFileResult]: ...

@pulumi.output_type
class GetVirtualGatewaySpecLoggingAccessLogFileResult(dict):
    def __init__(
        __self__,
        *,
        formats: Sequence[
            outputs.GetVirtualGatewaySpecLoggingAccessLogFileFormatResult
        ],
        path: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def formats(
        self,
    ) -> Sequence[outputs.GetVirtualGatewaySpecLoggingAccessLogFileFormatResult]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualGatewaySpecLoggingAccessLogFileFormatResult(dict):
    def __init__(
        __self__,
        *,
        jsons: Sequence[
            outputs.GetVirtualGatewaySpecLoggingAccessLogFileFormatJsonResult
        ],
        text: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def jsons(
        self,
    ) -> Sequence[
        outputs.GetVirtualGatewaySpecLoggingAccessLogFileFormatJsonResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualGatewaySpecLoggingAccessLogFileFormatJsonResult(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecResult(dict):
    def __init__(
        __self__,
        *,
        backend_defaults: Sequence[outputs.GetVirtualNodeSpecBackendDefaultResult],
        backends: Sequence[outputs.GetVirtualNodeSpecBackendResult],
        listeners: Sequence[outputs.GetVirtualNodeSpecListenerResult],
        loggings: Sequence[outputs.GetVirtualNodeSpecLoggingResult],
        service_discoveries: Sequence[outputs.GetVirtualNodeSpecServiceDiscoveryResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendDefaults")
    def backend_defaults(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecBackendDefaultResult]: ...
    @_builtins.property
    @pulumi.getter
    def backends(self) -> Sequence[outputs.GetVirtualNodeSpecBackendResult]: ...
    @_builtins.property
    @pulumi.getter
    def listeners(self) -> Sequence[outputs.GetVirtualNodeSpecListenerResult]: ...
    @_builtins.property
    @pulumi.getter
    def loggings(self) -> Sequence[outputs.GetVirtualNodeSpecLoggingResult]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDiscoveries")
    def service_discoveries(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecServiceDiscoveryResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendResult(dict):
    def __init__(
        __self__,
        *,
        virtual_services: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualServices")
    def virtual_services(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecBackendVirtualServiceResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultResult(dict):
    def __init__(
        __self__,
        *,
        client_policies: Sequence[
            outputs.GetVirtualNodeSpecBackendDefaultClientPolicyResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientPolicies")
    def client_policies(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecBackendDefaultClientPolicyResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultClientPolicyResult(dict):
    def __init__(
        __self__,
        *,
        tls: Sequence[outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tls(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultClientPolicyTlResult(dict):
    def __init__(
        __self__,
        *,
        certificates: Sequence[
            outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlCertificateResult
        ],
        enforce: _builtins.bool,
        ports: Sequence[_builtins.int],
        validations: Sequence[
            outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlCertificateResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def validations(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationResult
    ]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultClientPolicyTlCertificateResult(dict):
    def __init__(
        __self__,
        *,
        files: Sequence[
            outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlCertificateFileResult
        ],
        sds: Sequence[
            outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlCertificateSdResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlCertificateFileResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlCertificateSdResult
    ]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultClientPolicyTlCertificateFileResult(dict):
    def __init__(
        __self__, *, certificate_chain: _builtins.str, private_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultClientPolicyTlCertificateSdResult(dict):
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationResult(dict):
    def __init__(
        __self__,
        *,
        subject_alternative_names: Sequence[
            outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationSubjectAlternativeNameResult
        ],
        trusts: Sequence[
            outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationTrustResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationSubjectAlternativeNameResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def trusts(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationTrustResult
    ]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationSubjectAlternativeNameResult(
    dict
):
    def __init__(
        __self__,
        *,
        matches: Sequence[
            outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationSubjectAlternativeNameMatchResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationSubjectAlternativeNameMatchResult
    ]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationSubjectAlternativeNameMatchResult(
    dict
):
    def __init__(__self__, *, exacts: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationTrustResult(dict):
    def __init__(
        __self__,
        *,
        acms: Sequence[
            outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationTrustAcmResult
        ],
        files: Sequence[
            outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationTrustFileResult
        ],
        sds: Sequence[
            outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationTrustSdResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acms(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationTrustAcmResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationTrustFileResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationTrustSdResult
    ]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationTrustAcmResult(dict):
    def __init__(
        __self__, *, certificate_authority_arns: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationTrustFileResult(dict):
    def __init__(__self__, *, certificate_chain: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendDefaultClientPolicyTlValidationTrustSdResult(dict):
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceResult(dict):
    def __init__(
        __self__,
        *,
        client_policies: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyResult
        ],
        virtual_service_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientPolicies")
    def client_policies(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="virtualServiceName")
    def virtual_service_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceClientPolicyResult(dict):
    def __init__(
        __self__,
        *,
        tls: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tls(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlResult
    ]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlResult(dict):
    def __init__(
        __self__,
        *,
        certificates: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlCertificateResult
        ],
        enforce: _builtins.bool,
        ports: Sequence[_builtins.int],
        validations: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlCertificateResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def validations(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationResult
    ]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlCertificateResult(dict):
    def __init__(
        __self__,
        *,
        files: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlCertificateFileResult
        ],
        sds: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlCertificateSdResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlCertificateFileResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlCertificateSdResult
    ]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlCertificateFileResult(dict):
    def __init__(
        __self__, *, certificate_chain: _builtins.str, private_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlCertificateSdResult(dict):
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationResult(dict):
    def __init__(
        __self__,
        *,
        subject_alternative_names: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationSubjectAlternativeNameResult
        ],
        trusts: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationTrustResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationSubjectAlternativeNameResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def trusts(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationTrustResult
    ]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationSubjectAlternativeNameResult(
    dict
):
    def __init__(
        __self__,
        *,
        matches: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationSubjectAlternativeNameMatchResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationSubjectAlternativeNameMatchResult
    ]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationSubjectAlternativeNameMatchResult(
    dict
):
    def __init__(__self__, *, exacts: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationTrustResult(dict):
    def __init__(
        __self__,
        *,
        acms: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationTrustAcmResult
        ],
        files: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationTrustFileResult
        ],
        sds: Sequence[
            outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationTrustSdResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acms(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationTrustAcmResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationTrustFileResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationTrustSdResult
    ]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationTrustAcmResult(
    dict
):
    def __init__(
        __self__, *, certificate_authority_arns: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationTrustFileResult(
    dict
):
    def __init__(__self__, *, certificate_chain: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecBackendVirtualServiceClientPolicyTlValidationTrustSdResult(
    dict
):
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerResult(dict):
    def __init__(
        __self__,
        *,
        connection_pools: Sequence[
            outputs.GetVirtualNodeSpecListenerConnectionPoolResult
        ],
        health_checks: Sequence[outputs.GetVirtualNodeSpecListenerHealthCheckResult],
        outlier_detections: Sequence[
            outputs.GetVirtualNodeSpecListenerOutlierDetectionResult
        ],
        port_mappings: Sequence[outputs.GetVirtualNodeSpecListenerPortMappingResult],
        timeouts: Sequence[outputs.GetVirtualNodeSpecListenerTimeoutResult],
        tls: Sequence[outputs.GetVirtualNodeSpecListenerTlResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionPools")
    def connection_pools(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerConnectionPoolResult]: ...
    @_builtins.property
    @pulumi.getter(name="healthChecks")
    def health_checks(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerHealthCheckResult]: ...
    @_builtins.property
    @pulumi.getter(name="outlierDetections")
    def outlier_detections(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerOutlierDetectionResult]: ...
    @_builtins.property
    @pulumi.getter(name="portMappings")
    def port_mappings(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerPortMappingResult]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Sequence[outputs.GetVirtualNodeSpecListenerTimeoutResult]: ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Sequence[outputs.GetVirtualNodeSpecListenerTlResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerConnectionPoolResult(dict):
    def __init__(
        __self__,
        *,
        grpcs: Sequence[outputs.GetVirtualNodeSpecListenerConnectionPoolGrpcResult],
        http2s: Sequence[outputs.GetVirtualNodeSpecListenerConnectionPoolHttp2Result],
        https: Sequence[outputs.GetVirtualNodeSpecListenerConnectionPoolHttpResult],
        tcps: Sequence[outputs.GetVirtualNodeSpecListenerConnectionPoolTcpResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def grpcs(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerConnectionPoolGrpcResult]: ...
    @_builtins.property
    @pulumi.getter
    def http2s(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerConnectionPoolHttp2Result]: ...
    @_builtins.property
    @pulumi.getter
    def https(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerConnectionPoolHttpResult]: ...
    @_builtins.property
    @pulumi.getter
    def tcps(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerConnectionPoolTcpResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerConnectionPoolGrpcResult(dict):
    def __init__(__self__, *, max_requests: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequests")
    def max_requests(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerConnectionPoolHttp2Result(dict):
    def __init__(__self__, *, max_requests: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRequests")
    def max_requests(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerConnectionPoolHttpResult(dict):
    def __init__(
        __self__, *, max_connections: _builtins.int, max_pending_requests: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxPendingRequests")
    def max_pending_requests(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerConnectionPoolTcpResult(dict):
    def __init__(__self__, *, max_connections: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerHealthCheckResult(dict):
    def __init__(
        __self__,
        *,
        healthy_threshold: _builtins.int,
        interval_millis: _builtins.int,
        path: _builtins.str,
        port: _builtins.int,
        protocol: _builtins.str,
        timeout_millis: _builtins.int,
        unhealthy_threshold: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="intervalMillis")
    def interval_millis(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutMillis")
    def timeout_millis(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerOutlierDetectionResult(dict):
    def __init__(
        __self__,
        *,
        base_ejection_durations: Sequence[
            outputs.GetVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationResult
        ],
        intervals: Sequence[
            outputs.GetVirtualNodeSpecListenerOutlierDetectionIntervalResult
        ],
        max_ejection_percent: _builtins.int,
        max_server_errors: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseEjectionDurations")
    def base_ejection_durations(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def intervals(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerOutlierDetectionIntervalResult]: ...
    @_builtins.property
    @pulumi.getter(name="maxEjectionPercent")
    def max_ejection_percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxServerErrors")
    def max_server_errors(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerOutlierDetectionIntervalResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerPortMappingResult(dict):
    def __init__(__self__, *, port: _builtins.int, protocol: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTimeoutResult(dict):
    def __init__(
        __self__,
        *,
        grpcs: Sequence[outputs.GetVirtualNodeSpecListenerTimeoutGrpcResult],
        http2s: Sequence[outputs.GetVirtualNodeSpecListenerTimeoutHttp2Result],
        https: Sequence[outputs.GetVirtualNodeSpecListenerTimeoutHttpResult],
        tcps: Sequence[outputs.GetVirtualNodeSpecListenerTimeoutTcpResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def grpcs(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTimeoutGrpcResult]: ...
    @_builtins.property
    @pulumi.getter
    def http2s(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTimeoutHttp2Result]: ...
    @_builtins.property
    @pulumi.getter
    def https(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTimeoutHttpResult]: ...
    @_builtins.property
    @pulumi.getter
    def tcps(self) -> Sequence[outputs.GetVirtualNodeSpecListenerTimeoutTcpResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTimeoutGrpcResult(dict):
    def __init__(
        __self__,
        *,
        idles: Sequence[outputs.GetVirtualNodeSpecListenerTimeoutGrpcIdleResult],
        per_requests: Sequence[
            outputs.GetVirtualNodeSpecListenerTimeoutGrpcPerRequestResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idles(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTimeoutGrpcIdleResult]: ...
    @_builtins.property
    @pulumi.getter(name="perRequests")
    def per_requests(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTimeoutGrpcPerRequestResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTimeoutGrpcIdleResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTimeoutGrpcPerRequestResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTimeoutHttp2Result(dict):
    def __init__(
        __self__,
        *,
        idles: Sequence[outputs.GetVirtualNodeSpecListenerTimeoutHttp2IdleResult],
        per_requests: Sequence[
            outputs.GetVirtualNodeSpecListenerTimeoutHttp2PerRequestResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idles(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTimeoutHttp2IdleResult]: ...
    @_builtins.property
    @pulumi.getter(name="perRequests")
    def per_requests(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTimeoutHttp2PerRequestResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTimeoutHttp2IdleResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTimeoutHttp2PerRequestResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTimeoutHttpResult(dict):
    def __init__(
        __self__,
        *,
        idles: Sequence[outputs.GetVirtualNodeSpecListenerTimeoutHttpIdleResult],
        per_requests: Sequence[
            outputs.GetVirtualNodeSpecListenerTimeoutHttpPerRequestResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idles(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTimeoutHttpIdleResult]: ...
    @_builtins.property
    @pulumi.getter(name="perRequests")
    def per_requests(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTimeoutHttpPerRequestResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTimeoutHttpIdleResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTimeoutHttpPerRequestResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTimeoutTcpResult(dict):
    def __init__(
        __self__,
        *,
        idles: Sequence[outputs.GetVirtualNodeSpecListenerTimeoutTcpIdleResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def idles(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTimeoutTcpIdleResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTimeoutTcpIdleResult(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTlResult(dict):
    def __init__(
        __self__,
        *,
        certificates: Sequence[outputs.GetVirtualNodeSpecListenerTlCertificateResult],
        mode: _builtins.str,
        validations: Sequence[outputs.GetVirtualNodeSpecListenerTlValidationResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTlCertificateResult]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def validations(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTlValidationResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTlCertificateResult(dict):
    def __init__(
        __self__,
        *,
        acms: Sequence[outputs.GetVirtualNodeSpecListenerTlCertificateAcmResult],
        files: Sequence[outputs.GetVirtualNodeSpecListenerTlCertificateFileResult],
        sds: Sequence[outputs.GetVirtualNodeSpecListenerTlCertificateSdResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acms(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTlCertificateAcmResult]: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTlCertificateFileResult]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTlCertificateSdResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTlCertificateAcmResult(dict):
    def __init__(__self__, *, certificate_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTlCertificateFileResult(dict):
    def __init__(
        __self__, *, certificate_chain: _builtins.str, private_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTlCertificateSdResult(dict):
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTlValidationResult(dict):
    def __init__(
        __self__,
        *,
        subject_alternative_names: Sequence[
            outputs.GetVirtualNodeSpecListenerTlValidationSubjectAlternativeNameResult
        ],
        trusts: Sequence[outputs.GetVirtualNodeSpecListenerTlValidationTrustResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecListenerTlValidationSubjectAlternativeNameResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def trusts(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTlValidationTrustResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTlValidationSubjectAlternativeNameResult(dict):
    def __init__(
        __self__,
        *,
        matches: Sequence[
            outputs.GetVirtualNodeSpecListenerTlValidationSubjectAlternativeNameMatchResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Sequence[
        outputs.GetVirtualNodeSpecListenerTlValidationSubjectAlternativeNameMatchResult
    ]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTlValidationSubjectAlternativeNameMatchResult(dict):
    def __init__(__self__, *, exacts: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def exacts(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTlValidationTrustResult(dict):
    def __init__(
        __self__,
        *,
        files: Sequence[outputs.GetVirtualNodeSpecListenerTlValidationTrustFileResult],
        sds: Sequence[outputs.GetVirtualNodeSpecListenerTlValidationTrustSdResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTlValidationTrustFileResult]: ...
    @_builtins.property
    @pulumi.getter
    def sds(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecListenerTlValidationTrustSdResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTlValidationTrustFileResult(dict):
    def __init__(__self__, *, certificate_chain: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecListenerTlValidationTrustSdResult(dict):
    def __init__(__self__, *, secret_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecLoggingResult(dict):
    def __init__(
        __self__,
        *,
        access_logs: Sequence[outputs.GetVirtualNodeSpecLoggingAccessLogResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessLogs")
    def access_logs(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecLoggingAccessLogResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecLoggingAccessLogResult(dict):
    def __init__(
        __self__,
        *,
        files: Sequence[outputs.GetVirtualNodeSpecLoggingAccessLogFileResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def files(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecLoggingAccessLogFileResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecLoggingAccessLogFileResult(dict):
    def __init__(
        __self__,
        *,
        formats: Sequence[outputs.GetVirtualNodeSpecLoggingAccessLogFileFormatResult],
        path: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def formats(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecLoggingAccessLogFileFormatResult]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecLoggingAccessLogFileFormatResult(dict):
    def __init__(
        __self__,
        *,
        jsons: Sequence[outputs.GetVirtualNodeSpecLoggingAccessLogFileFormatJsonResult],
        text: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def jsons(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecLoggingAccessLogFileFormatJsonResult]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecLoggingAccessLogFileFormatJsonResult(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecServiceDiscoveryResult(dict):
    def __init__(
        __self__,
        *,
        aws_cloud_maps: Sequence[
            outputs.GetVirtualNodeSpecServiceDiscoveryAwsCloudMapResult
        ],
        dns: Sequence[outputs.GetVirtualNodeSpecServiceDiscoveryDnResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsCloudMaps")
    def aws_cloud_maps(
        self,
    ) -> Sequence[outputs.GetVirtualNodeSpecServiceDiscoveryAwsCloudMapResult]: ...
    @_builtins.property
    @pulumi.getter
    def dns(self) -> Sequence[outputs.GetVirtualNodeSpecServiceDiscoveryDnResult]: ...

@pulumi.output_type
class GetVirtualNodeSpecServiceDiscoveryAwsCloudMapResult(dict):
    def __init__(
        __self__,
        *,
        attributes: Mapping[str, _builtins.str],
        namespace_name: _builtins.str,
        service_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualNodeSpecServiceDiscoveryDnResult(dict):
    def __init__(
        __self__,
        *,
        hostname: _builtins.str,
        ip_preference: _builtins.str,
        response_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipPreference")
    def ip_preference(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="responseType")
    def response_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualRouterSpecResult(dict):
    def __init__(
        __self__, *, listeners: Sequence[outputs.GetVirtualRouterSpecListenerResult]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def listeners(self) -> Sequence[outputs.GetVirtualRouterSpecListenerResult]: ...

@pulumi.output_type
class GetVirtualRouterSpecListenerResult(dict):
    def __init__(
        __self__,
        *,
        port_mappings: Sequence[outputs.GetVirtualRouterSpecListenerPortMappingResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="portMappings")
    def port_mappings(
        self,
    ) -> Sequence[outputs.GetVirtualRouterSpecListenerPortMappingResult]: ...

@pulumi.output_type
class GetVirtualRouterSpecListenerPortMappingResult(dict):
    def __init__(__self__, *, port: _builtins.int, protocol: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualServiceSpecResult(dict):
    def __init__(
        __self__, *, providers: Sequence[outputs.GetVirtualServiceSpecProviderResult]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def providers(self) -> Sequence[outputs.GetVirtualServiceSpecProviderResult]: ...

@pulumi.output_type
class GetVirtualServiceSpecProviderResult(dict):
    def __init__(
        __self__,
        *,
        virtual_nodes: Sequence[outputs.GetVirtualServiceSpecProviderVirtualNodeResult],
        virtual_routers: Sequence[
            outputs.GetVirtualServiceSpecProviderVirtualRouterResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNodes")
    def virtual_nodes(
        self,
    ) -> Sequence[outputs.GetVirtualServiceSpecProviderVirtualNodeResult]: ...
    @_builtins.property
    @pulumi.getter(name="virtualRouters")
    def virtual_routers(
        self,
    ) -> Sequence[outputs.GetVirtualServiceSpecProviderVirtualRouterResult]: ...

@pulumi.output_type
class GetVirtualServiceSpecProviderVirtualNodeResult(dict):
    def __init__(__self__, *, virtual_node_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNodeName")
    def virtual_node_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetVirtualServiceSpecProviderVirtualRouterResult(dict):
    def __init__(__self__, *, virtual_router_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualRouterName")
    def virtual_router_name(self) -> _builtins.str: ...
