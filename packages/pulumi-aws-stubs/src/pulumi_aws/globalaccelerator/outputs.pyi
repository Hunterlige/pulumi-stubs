import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AcceleratorAttributes",
    "AcceleratorIpSet",
    "CrossAccountAttachmentResource",
    "CustomRoutingAcceleratorAttributes",
    "CustomRoutingAcceleratorIpSet",
    "CustomRoutingEndpointGroupDestinationConfiguration",
    "CustomRoutingEndpointGroupEndpointConfiguration",
    "CustomRoutingListenerPortRange",
    "EndpointGroupEndpointConfiguration",
    "EndpointGroupPortOverride",
    "ListenerPortRange",
    "GetAcceleratorAttributeResult",
    "GetAcceleratorIpSetResult",
    "GetCustomRoutingAcceleratorAttributeResult",
    "GetCustomRoutingAcceleratorIpSetResult",
]

@pulumi.output_type
class AcceleratorAttributes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        flow_logs_enabled: Optional[_builtins.bool] = ...,
        flow_logs_s3_bucket: Optional[_builtins.str] = ...,
        flow_logs_s3_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsEnabled")
    def flow_logs_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsS3Bucket")
    def flow_logs_s3_bucket(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsS3Prefix")
    def flow_logs_s3_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AcceleratorIpSet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
        ip_family: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipFamily")
    def ip_family(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CrossAccountAttachmentResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cidr_block: Optional[_builtins.str] = ...,
        endpoint_id: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomRoutingAcceleratorAttributes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        flow_logs_enabled: Optional[_builtins.bool] = ...,
        flow_logs_s3_bucket: Optional[_builtins.str] = ...,
        flow_logs_s3_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsEnabled")
    def flow_logs_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsS3Bucket")
    def flow_logs_s3_bucket(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsS3Prefix")
    def flow_logs_s3_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomRoutingAcceleratorIpSet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
        ip_family: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipFamily")
    def ip_family(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomRoutingEndpointGroupDestinationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        from_port: _builtins.int,
        protocols: Sequence[_builtins.str],
        to_port: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int: ...

@pulumi.output_type
class CustomRoutingEndpointGroupEndpointConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, endpoint_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomRoutingListenerPortRange(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        from_port: Optional[_builtins.int] = ...,
        to_port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EndpointGroupEndpointConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        attachment_arn: Optional[_builtins.str] = ...,
        client_ip_preservation_enabled: Optional[_builtins.bool] = ...,
        endpoint_id: Optional[_builtins.str] = ...,
        weight: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachmentArn")
    def attachment_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientIpPreservationEnabled")
    def client_ip_preservation_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class EndpointGroupPortOverride(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, endpoint_port: _builtins.int, listener_port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointPort")
    def endpoint_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="listenerPort")
    def listener_port(self) -> _builtins.int: ...

@pulumi.output_type
class ListenerPortRange(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        from_port: Optional[_builtins.int] = ...,
        to_port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GetAcceleratorAttributeResult(dict):
    def __init__(
        __self__,
        *,
        flow_logs_enabled: _builtins.bool,
        flow_logs_s3_bucket: _builtins.str,
        flow_logs_s3_prefix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsEnabled")
    def flow_logs_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsS3Bucket")
    def flow_logs_s3_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsS3Prefix")
    def flow_logs_s3_prefix(self) -> _builtins.str: ...

@pulumi.output_type
class GetAcceleratorIpSetResult(dict):
    def __init__(
        __self__, *, ip_addresses: Sequence[_builtins.str], ip_family: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipFamily")
    def ip_family(self) -> _builtins.str: ...

@pulumi.output_type
class GetCustomRoutingAcceleratorAttributeResult(dict):
    def __init__(
        __self__,
        *,
        flow_logs_enabled: _builtins.bool,
        flow_logs_s3_bucket: _builtins.str,
        flow_logs_s3_prefix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsEnabled")
    def flow_logs_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsS3Bucket")
    def flow_logs_s3_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsS3Prefix")
    def flow_logs_s3_prefix(self) -> _builtins.str: ...

@pulumi.output_type
class GetCustomRoutingAcceleratorIpSetResult(dict):
    def __init__(
        __self__, *, ip_addresses: Sequence[_builtins.str], ip_family: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipFamily")
    def ip_family(self) -> _builtins.str: ...
