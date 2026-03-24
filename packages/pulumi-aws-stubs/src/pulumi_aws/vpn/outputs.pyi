import builtins as _builtins
import sys
import pulumi
from typing import Sequence

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConnectionFilterResult",
    "GetConnectionRouteResult",
    "GetConnectionVgwTelemetryResult",
]

@pulumi.output_type
class GetConnectionFilterResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetConnectionRouteResult(dict):
    def __init__(
        __self__,
        *,
        destination_cidr_block: _builtins.str,
        source: _builtins.str,
        state: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationCidrBlock")
    def destination_cidr_block(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class GetConnectionVgwTelemetryResult(dict):
    def __init__(
        __self__,
        *,
        accepted_route_count: _builtins.int,
        last_status_change: _builtins.str,
        outside_ip_address: _builtins.str,
        status: _builtins.str,
        status_message: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptedRouteCount")
    def accepted_route_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="lastStatusChange")
    def last_status_change(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outsideIpAddress")
    def outside_ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str: ...
