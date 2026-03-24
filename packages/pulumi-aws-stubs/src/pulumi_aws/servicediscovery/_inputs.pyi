import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ServiceDnsConfigArgs",
    "ServiceDnsConfigArgsDict",
    "ServiceDnsConfigDnsRecordArgs",
    "ServiceDnsConfigDnsRecordArgsDict",
    "ServiceHealthCheckConfigArgs",
    "ServiceHealthCheckConfigArgsDict",
    "ServiceHealthCheckCustomConfigArgs",
    "ServiceHealthCheckCustomConfigArgsDict",
]

class ServiceDnsConfigArgsDict(TypedDict):
    dns_records: pulumi.Input[Sequence[pulumi.Input[ServiceDnsConfigDnsRecordArgsDict]]]
    namespace_id: pulumi.Input[_builtins.str]
    routing_policy: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServiceDnsConfigArgs:
    def __init__(
        __self__,
        *,
        dns_records: pulumi.Input[
            Sequence[pulumi.Input[ServiceDnsConfigDnsRecordArgs]]
        ],
        namespace_id: pulumi.Input[_builtins.str],
        routing_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsRecords")
    def dns_records(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ServiceDnsConfigDnsRecordArgs]]]: ...
    @dns_records.setter
    def dns_records(
        self, value: pulumi.Input[Sequence[pulumi.Input[ServiceDnsConfigDnsRecordArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Input[_builtins.str]: ...
    @namespace_id.setter
    def namespace_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="routingPolicy")
    def routing_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_policy.setter
    def routing_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceDnsConfigDnsRecordArgsDict(TypedDict):
    ttl: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ServiceDnsConfigDnsRecordArgs:
    def __init__(
        __self__, *, ttl: pulumi.Input[_builtins.int], type: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> pulumi.Input[_builtins.int]: ...
    @ttl.setter
    def ttl(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ServiceHealthCheckConfigArgsDict(TypedDict):
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    resource_path: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ServiceHealthCheckConfigArgs:
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_path: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourcePath")
    def resource_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_path.setter
    def resource_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceHealthCheckCustomConfigArgsDict(TypedDict):
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ServiceHealthCheckCustomConfigArgs:
    def __init__(
        __self__, *, failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    @_utilities.deprecated(...)
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
