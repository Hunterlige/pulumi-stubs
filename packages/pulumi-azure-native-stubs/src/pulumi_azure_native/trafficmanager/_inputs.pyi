import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DnsConfigArgs",
    "DnsConfigArgsDict",
    "EndpointPropertiesCustomHeadersItemArgs",
    "EndpointPropertiesCustomHeadersItemArgsDict",
    "EndpointPropertiesSubnetsItemArgs",
    "EndpointPropertiesSubnetsItemArgsDict",
    "EndpointArgs",
    "EndpointArgsDict",
    "MonitorConfigCustomHeadersItemArgs",
    "MonitorConfigCustomHeadersItemArgsDict",
    "MonitorConfigExpectedStatusCodeRangesItemArgs",
    "MonitorConfigExpectedStatusCodeRangesItemArgsDict",
    "MonitorConfigArgs",
    "MonitorConfigArgsDict",
]

class DnsConfigArgsDict(TypedDict):
    relative_name: NotRequired[pulumi.Input[_builtins.str]]
    ttl: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class DnsConfigArgs:
    def __init__(
        __self__,
        *,
        relative_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ttl: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="relativeName")
    def relative_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @relative_name.setter
    def relative_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class EndpointPropertiesCustomHeadersItemArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EndpointPropertiesCustomHeadersItemArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EndpointPropertiesSubnetsItemArgsDict(TypedDict):
    first: NotRequired[pulumi.Input[_builtins.str]]
    last: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class EndpointPropertiesSubnetsItemArgs:
    def __init__(
        __self__,
        *,
        first: Optional[pulumi.Input[_builtins.str]] = ...,
        last: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def first(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @first.setter
    def first(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def last(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last.setter
    def last(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class EndpointArgsDict(TypedDict):
    always_serve: NotRequired[pulumi.Input[Union[_builtins.str, AlwaysServe]]]
    custom_headers: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[EndpointPropertiesCustomHeadersItemArgsDict]]
        ]
    ]
    endpoint_location: NotRequired[pulumi.Input[_builtins.str]]
    endpoint_monitor_status: NotRequired[
        pulumi.Input[Union[_builtins.str, EndpointMonitorStatus]]
    ]
    endpoint_status: NotRequired[pulumi.Input[Union[_builtins.str, EndpointStatus]]]
    geo_mapping: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    min_child_endpoints: NotRequired[pulumi.Input[_builtins.float]]
    min_child_endpoints_i_pv4: NotRequired[pulumi.Input[_builtins.float]]
    min_child_endpoints_i_pv6: NotRequired[pulumi.Input[_builtins.float]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    priority: NotRequired[pulumi.Input[_builtins.float]]
    subnets: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesSubnetsItemArgsDict]]]
    ]
    target: NotRequired[pulumi.Input[_builtins.str]]
    target_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class EndpointArgs:
    def __init__(
        __self__,
        *,
        always_serve: Optional[pulumi.Input[Union[_builtins.str, AlwaysServe]]] = ...,
        custom_headers: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EndpointPropertiesCustomHeadersItemArgs]]
            ]
        ] = ...,
        endpoint_location: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_monitor_status: Optional[
            pulumi.Input[Union[_builtins.str, EndpointMonitorStatus]]
        ] = ...,
        endpoint_status: Optional[
            pulumi.Input[Union[_builtins.str, EndpointStatus]]
        ] = ...,
        geo_mapping: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        min_child_endpoints: Optional[pulumi.Input[_builtins.float]] = ...,
        min_child_endpoints_i_pv4: Optional[pulumi.Input[_builtins.float]] = ...,
        min_child_endpoints_i_pv6: Optional[pulumi.Input[_builtins.float]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.float]] = ...,
        subnets: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesSubnetsItemArgs]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        target_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        weight: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alwaysServe")
    def always_serve(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AlwaysServe]]]: ...
    @always_serve.setter
    def always_serve(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AlwaysServe]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesCustomHeadersItemArgs]]]
    ]: ...
    @custom_headers.setter
    def custom_headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[EndpointPropertiesCustomHeadersItemArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointLocation")
    def endpoint_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_location.setter
    def endpoint_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointMonitorStatus")
    def endpoint_monitor_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EndpointMonitorStatus]]]: ...
    @endpoint_monitor_status.setter
    def endpoint_monitor_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EndpointMonitorStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointStatus")
    def endpoint_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EndpointStatus]]]: ...
    @endpoint_status.setter
    def endpoint_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EndpointStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="geoMapping")
    def geo_mapping(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @geo_mapping.setter
    def geo_mapping(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minChildEndpoints")
    def min_child_endpoints(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min_child_endpoints.setter
    def min_child_endpoints(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="minChildEndpointsIPv4")
    def min_child_endpoints_i_pv4(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min_child_endpoints_i_pv4.setter
    def min_child_endpoints_i_pv4(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minChildEndpointsIPv6")
    def min_child_endpoints_i_pv6(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min_child_endpoints_i_pv6.setter
    def min_child_endpoints_i_pv6(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def subnets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesSubnetsItemArgs]]]
    ]: ...
    @subnets.setter
    def subnets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesSubnetsItemArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_resource_id.setter
    def target_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class MonitorConfigCustomHeadersItemArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MonitorConfigCustomHeadersItemArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MonitorConfigExpectedStatusCodeRangesItemArgsDict(TypedDict):
    max: NotRequired[pulumi.Input[_builtins.int]]
    min: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class MonitorConfigExpectedStatusCodeRangesItemArgs:
    def __init__(
        __self__,
        *,
        max: Optional[pulumi.Input[_builtins.int]] = ...,
        min: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max.setter
    def max(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min.setter
    def min(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class MonitorConfigArgsDict(TypedDict):
    custom_headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[MonitorConfigCustomHeadersItemArgsDict]]]
    ]
    expected_status_code_ranges: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[MonitorConfigExpectedStatusCodeRangesItemArgsDict]]
        ]
    ]
    interval_in_seconds: NotRequired[pulumi.Input[_builtins.float]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.float]]
    profile_monitor_status: NotRequired[
        pulumi.Input[Union[_builtins.str, ProfileMonitorStatus]]
    ]
    protocol: NotRequired[pulumi.Input[Union[_builtins.str, MonitorProtocol]]]
    timeout_in_seconds: NotRequired[pulumi.Input[_builtins.float]]
    tolerated_number_of_failures: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class MonitorConfigArgs:
    def __init__(
        __self__,
        *,
        custom_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[MonitorConfigCustomHeadersItemArgs]]]
        ] = ...,
        expected_status_code_ranges: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MonitorConfigExpectedStatusCodeRangesItemArgs]]
            ]
        ] = ...,
        interval_in_seconds: Optional[pulumi.Input[_builtins.float]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.float]] = ...,
        profile_monitor_status: Optional[
            pulumi.Input[Union[_builtins.str, ProfileMonitorStatus]]
        ] = ...,
        protocol: Optional[pulumi.Input[Union[_builtins.str, MonitorProtocol]]] = ...,
        timeout_in_seconds: Optional[pulumi.Input[_builtins.float]] = ...,
        tolerated_number_of_failures: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MonitorConfigCustomHeadersItemArgs]]]
    ]: ...
    @custom_headers.setter
    def custom_headers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MonitorConfigCustomHeadersItemArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="expectedStatusCodeRanges")
    def expected_status_code_ranges(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[MonitorConfigExpectedStatusCodeRangesItemArgs]]
        ]
    ]: ...
    @expected_status_code_ranges.setter
    def expected_status_code_ranges(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[MonitorConfigExpectedStatusCodeRangesItemArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="intervalInSeconds")
    def interval_in_seconds(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @interval_in_seconds.setter
    def interval_in_seconds(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="profileMonitorStatus")
    def profile_monitor_status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProfileMonitorStatus]]]: ...
    @profile_monitor_status.setter
    def profile_monitor_status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ProfileMonitorStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MonitorProtocol]]]: ...
    @protocol.setter
    def protocol(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MonitorProtocol]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="toleratedNumberOfFailures")
    def tolerated_number_of_failures(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @tolerated_number_of_failures.setter
    def tolerated_number_of_failures(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
