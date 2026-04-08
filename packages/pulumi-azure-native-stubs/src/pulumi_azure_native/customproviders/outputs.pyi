import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CustomRPActionRouteDefinitionResponse",
    "CustomRPResourceTypeRouteDefinitionResponse",
    "CustomRPValidationsResponse",
]

@pulumi.output_type
class CustomRPActionRouteDefinitionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint: _builtins.str,
        name: _builtins.str,
        routing_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routingType")
    def routing_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomRPResourceTypeRouteDefinitionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint: _builtins.str,
        name: _builtins.str,
        routing_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="routingType")
    def routing_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomRPValidationsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        specification: _builtins.str,
        validation_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def specification(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="validationType")
    def validation_type(self) -> Optional[_builtins.str]: ...
