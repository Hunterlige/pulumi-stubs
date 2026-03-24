import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "LoadBalancerAccessLogs",
    "LoadBalancerHealthCheck",
    "LoadBalancerListener",
    "LoadBalancerPolicyPolicyAttribute",
    "SslNegotiationPolicyAttribute",
    "GetLoadBalancerAccessLogsResult",
    "GetLoadBalancerHealthCheckResult",
    "GetLoadBalancerListenerResult",
]

@pulumi.output_type
class LoadBalancerAccessLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        bucket_prefix: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
        interval: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class LoadBalancerHealthCheck(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        healthy_threshold: _builtins.int,
        interval: _builtins.int,
        target: _builtins.str,
        timeout: _builtins.int,
        unhealthy_threshold: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> _builtins.int: ...

@pulumi.output_type
class LoadBalancerListener(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_port: _builtins.int,
        instance_protocol: _builtins.str,
        lb_port: _builtins.int,
        lb_protocol: _builtins.str,
        ssl_certificate_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instancePort")
    def instance_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="instanceProtocol")
    def instance_protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lbPort")
    def lb_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="lbProtocol")
    def lb_protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sslCertificateId")
    def ssl_certificate_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LoadBalancerPolicyPolicyAttribute(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SslNegotiationPolicyAttribute(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetLoadBalancerAccessLogsResult(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        bucket_prefix: _builtins.str,
        enabled: _builtins.bool,
        interval: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.int: ...

@pulumi.output_type
class GetLoadBalancerHealthCheckResult(dict):
    def __init__(
        __self__,
        *,
        healthy_threshold: _builtins.int,
        interval: _builtins.int,
        target: _builtins.str,
        timeout: _builtins.int,
        unhealthy_threshold: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> _builtins.int: ...

@pulumi.output_type
class GetLoadBalancerListenerResult(dict):
    def __init__(
        __self__,
        *,
        instance_port: _builtins.int,
        instance_protocol: _builtins.str,
        lb_port: _builtins.int,
        lb_protocol: _builtins.str,
        ssl_certificate_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instancePort")
    def instance_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="instanceProtocol")
    def instance_protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lbPort")
    def lb_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="lbProtocol")
    def lb_protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sslCertificateId")
    def ssl_certificate_id(self) -> _builtins.str: ...
