import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ServiceDnsConfig",
    "ServiceDnsConfigDnsRecord",
    "ServiceHealthCheckConfig",
    "ServiceHealthCheckCustomConfig",
    "GetServiceDnsConfigResult",
    "GetServiceDnsConfigDnsRecordResult",
    "GetServiceHealthCheckConfigResult",
    "GetServiceHealthCheckCustomConfigResult",
]

@pulumi.output_type
class ServiceDnsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_records: Sequence[outputs.ServiceDnsConfigDnsRecord],
        namespace_id: _builtins.str,
        routing_policy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsRecords")
    def dns_records(self) -> Sequence[outputs.ServiceDnsConfigDnsRecord]: ...
    @_builtins.property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routingPolicy")
    def routing_policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceDnsConfigDnsRecord(dict):
    def __init__(__self__, *, ttl: _builtins.int, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceHealthCheckConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[_builtins.int] = ...,
        resource_path: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="resourcePath")
    def resource_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceHealthCheckCustomConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, failure_threshold: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    @_utilities.deprecated(...)
    def failure_threshold(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GetServiceDnsConfigResult(dict):
    def __init__(
        __self__,
        *,
        dns_records: Sequence[outputs.GetServiceDnsConfigDnsRecordResult],
        namespace_id: _builtins.str,
        routing_policy: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsRecords")
    def dns_records(self) -> Sequence[outputs.GetServiceDnsConfigDnsRecordResult]: ...
    @_builtins.property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routingPolicy")
    def routing_policy(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceDnsConfigDnsRecordResult(dict):
    def __init__(__self__, *, ttl: _builtins.int, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceHealthCheckConfigResult(dict):
    def __init__(
        __self__,
        *,
        failure_threshold: _builtins.int,
        resource_path: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="resourcePath")
    def resource_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceHealthCheckCustomConfigResult(dict):
    def __init__(__self__, *, failure_threshold: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> _builtins.int: ...
