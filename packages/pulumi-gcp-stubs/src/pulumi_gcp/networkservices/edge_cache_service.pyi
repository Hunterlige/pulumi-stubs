import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EdgeCacheServiceArgs", "EdgeCacheService"]

@pulumi.input_type
class EdgeCacheServiceArgs:
    def __init__(
        __self__,
        *,
        routing: pulumi.Input[EdgeCacheServiceRoutingArgs],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_http2: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_quic: Optional[pulumi.Input[_builtins.bool]] = ...,
        edge_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_ssl_certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        log_config: Optional[pulumi.Input[EdgeCacheServiceLogConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        require_tls: Optional[pulumi.Input[_builtins.bool]] = ...,
        ssl_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def routing(self) -> pulumi.Input[EdgeCacheServiceRoutingArgs]: ...
    @routing.setter
    def routing(self, value: pulumi.Input[EdgeCacheServiceRoutingArgs]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableHttp2")
    def disable_http2(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_http2.setter
    def disable_http2(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="disableQuic")
    def disable_quic(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_quic.setter
    def disable_quic(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="edgeSecurityPolicy")
    def edge_security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edge_security_policy.setter
    def edge_security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="edgeSslCertificates")
    def edge_ssl_certificates(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @edge_ssl_certificates.setter
    def edge_ssl_certificates(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[EdgeCacheServiceLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self, value: Optional[pulumi.Input[EdgeCacheServiceLogConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requireTls")
    def require_tls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_tls.setter
    def require_tls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_policy.setter
    def ssl_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _EdgeCacheServiceState:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_http2: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_quic: Optional[pulumi.Input[_builtins.bool]] = ...,
        edge_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_ssl_certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        ipv4_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ipv6_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        log_config: Optional[pulumi.Input[EdgeCacheServiceLogConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        require_tls: Optional[pulumi.Input[_builtins.bool]] = ...,
        routing: Optional[pulumi.Input[EdgeCacheServiceRoutingArgs]] = ...,
        ssl_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableHttp2")
    def disable_http2(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_http2.setter
    def disable_http2(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="disableQuic")
    def disable_quic(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_quic.setter
    def disable_quic(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="edgeSecurityPolicy")
    def edge_security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edge_security_policy.setter
    def edge_security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="edgeSslCertificates")
    def edge_ssl_certificates(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @edge_ssl_certificates.setter
    def edge_ssl_certificates(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ipv4_addresses.setter
    def ipv4_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ipv6_addresses.setter
    def ipv6_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[EdgeCacheServiceLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self, value: Optional[pulumi.Input[EdgeCacheServiceLogConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requireTls")
    def require_tls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_tls.setter
    def require_tls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def routing(self) -> Optional[pulumi.Input[EdgeCacheServiceRoutingArgs]]: ...
    @routing.setter
    def routing(self, value: Optional[pulumi.Input[EdgeCacheServiceRoutingArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_policy.setter
    def ssl_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class EdgeCacheService(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_http2: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_quic: Optional[pulumi.Input[_builtins.bool]] = ...,
        edge_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_ssl_certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        log_config: Optional[
            pulumi.Input[
                Union[EdgeCacheServiceLogConfigArgs, EdgeCacheServiceLogConfigArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        require_tls: Optional[pulumi.Input[_builtins.bool]] = ...,
        routing: Optional[
            pulumi.Input[
                Union[EdgeCacheServiceRoutingArgs, EdgeCacheServiceRoutingArgsDict]
            ]
        ] = ...,
        ssl_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: EdgeCacheServiceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_http2: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_quic: Optional[pulumi.Input[_builtins.bool]] = ...,
        edge_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        edge_ssl_certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        ipv4_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ipv6_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        log_config: Optional[
            pulumi.Input[
                Union[EdgeCacheServiceLogConfigArgs, EdgeCacheServiceLogConfigArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        require_tls: Optional[pulumi.Input[_builtins.bool]] = ...,
        routing: Optional[
            pulumi.Input[
                Union[EdgeCacheServiceRoutingArgs, EdgeCacheServiceRoutingArgsDict]
            ]
        ] = ...,
        ssl_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> EdgeCacheService: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="disableHttp2")
    def disable_http2(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="disableQuic")
    def disable_quic(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="edgeSecurityPolicy")
    def edge_security_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="edgeSslCertificates")
    def edge_ssl_certificates(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(
        self,
    ) -> pulumi.Output[Optional[outputs.EdgeCacheServiceLogConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requireTls")
    def require_tls(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def routing(self) -> pulumi.Output[outputs.EdgeCacheServiceRouting]: ...
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
