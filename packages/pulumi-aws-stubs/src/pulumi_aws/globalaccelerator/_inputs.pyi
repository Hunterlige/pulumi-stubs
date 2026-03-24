import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AcceleratorAttributesArgs",
    "AcceleratorAttributesArgsDict",
    "AcceleratorIpSetArgs",
    "AcceleratorIpSetArgsDict",
    "CrossAccountAttachmentResourceArgs",
    "CrossAccountAttachmentResourceArgsDict",
    "CustomRoutingAcceleratorAttributesArgs",
    "CustomRoutingAcceleratorAttributesArgsDict",
    "CustomRoutingAcceleratorIpSetArgs",
    "CustomRoutingAcceleratorIpSetArgsDict",
    ...,
    ...,
    ...,
    ...,
    "CustomRoutingListenerPortRangeArgs",
    "CustomRoutingListenerPortRangeArgsDict",
    "EndpointGroupEndpointConfigurationArgs",
    "EndpointGroupEndpointConfigurationArgsDict",
    "EndpointGroupPortOverrideArgs",
    "EndpointGroupPortOverrideArgsDict",
    "ListenerPortRangeArgs",
    "ListenerPortRangeArgsDict",
]

class AcceleratorAttributesArgsDict(TypedDict):
    flow_logs_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    flow_logs_s3_bucket: NotRequired[pulumi.Input[_builtins.str]]
    flow_logs_s3_prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AcceleratorAttributesArgs:
    def __init__(
        __self__,
        *,
        flow_logs_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        flow_logs_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        flow_logs_s3_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsEnabled")
    def flow_logs_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @flow_logs_enabled.setter
    def flow_logs_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="flowLogsS3Bucket")
    def flow_logs_s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flow_logs_s3_bucket.setter
    def flow_logs_s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="flowLogsS3Prefix")
    def flow_logs_s3_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flow_logs_s3_prefix.setter
    def flow_logs_s3_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AcceleratorIpSetArgsDict(TypedDict):
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ip_family: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AcceleratorIpSetArgs:
    def __init__(
        __self__,
        *,
        ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ip_family: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_addresses.setter
    def ip_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipFamily")
    def ip_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_family.setter
    def ip_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CrossAccountAttachmentResourceArgsDict(TypedDict):
    cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CrossAccountAttachmentResourceArgs:
    def __init__(
        __self__,
        *,
        cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_id.setter
    def endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomRoutingAcceleratorAttributesArgsDict(TypedDict):
    flow_logs_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    flow_logs_s3_bucket: NotRequired[pulumi.Input[_builtins.str]]
    flow_logs_s3_prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CustomRoutingAcceleratorAttributesArgs:
    def __init__(
        __self__,
        *,
        flow_logs_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        flow_logs_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        flow_logs_s3_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="flowLogsEnabled")
    def flow_logs_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @flow_logs_enabled.setter
    def flow_logs_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="flowLogsS3Bucket")
    def flow_logs_s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flow_logs_s3_bucket.setter
    def flow_logs_s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="flowLogsS3Prefix")
    def flow_logs_s3_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flow_logs_s3_prefix.setter
    def flow_logs_s3_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomRoutingAcceleratorIpSetArgsDict(TypedDict):
    ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ip_family: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CustomRoutingAcceleratorIpSetArgs:
    def __init__(
        __self__,
        *,
        ip_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        ip_family: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @ip_addresses.setter
    def ip_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipFamily")
    def ip_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_family.setter
    def ip_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomRoutingEndpointGroupDestinationConfigurationArgsDict(TypedDict):
    from_port: pulumi.Input[_builtins.int]
    protocols: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    to_port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class CustomRoutingEndpointGroupDestinationConfigurationArgs:
    def __init__(
        __self__,
        *,
        from_port: pulumi.Input[_builtins.int],
        protocols: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        to_port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]: ...
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @protocols.setter
    def protocols(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]: ...
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): ...

class CustomRoutingEndpointGroupEndpointConfigurationArgsDict(TypedDict):
    endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CustomRoutingEndpointGroupEndpointConfigurationArgs:
    def __init__(
        __self__, *, endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_id.setter
    def endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CustomRoutingListenerPortRangeArgsDict(TypedDict):
    from_port: NotRequired[pulumi.Input[_builtins.int]]
    to_port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class CustomRoutingListenerPortRangeArgs:
    def __init__(
        __self__,
        *,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @from_port.setter
    def from_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class EndpointGroupEndpointConfigurationArgsDict(TypedDict):
    attachment_arn: NotRequired[pulumi.Input[_builtins.str]]
    client_ip_preservation_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class EndpointGroupEndpointConfigurationArgs:
    def __init__(
        __self__,
        *,
        attachment_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        client_ip_preservation_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        weight: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachmentArn")
    def attachment_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attachment_arn.setter
    def attachment_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientIpPreservationEnabled")
    def client_ip_preservation_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @client_ip_preservation_enabled.setter
    def client_ip_preservation_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_id.setter
    def endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class EndpointGroupPortOverrideArgsDict(TypedDict):
    endpoint_port: pulumi.Input[_builtins.int]
    listener_port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class EndpointGroupPortOverrideArgs:
    def __init__(
        __self__,
        *,
        endpoint_port: pulumi.Input[_builtins.int],
        listener_port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointPort")
    def endpoint_port(self) -> pulumi.Input[_builtins.int]: ...
    @endpoint_port.setter
    def endpoint_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="listenerPort")
    def listener_port(self) -> pulumi.Input[_builtins.int]: ...
    @listener_port.setter
    def listener_port(self, value: pulumi.Input[_builtins.int]): ...

class ListenerPortRangeArgsDict(TypedDict):
    from_port: NotRequired[pulumi.Input[_builtins.int]]
    to_port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ListenerPortRangeArgs:
    def __init__(
        __self__,
        *,
        from_port: Optional[pulumi.Input[_builtins.int]] = ...,
        to_port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @from_port.setter
    def from_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @to_port.setter
    def to_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
