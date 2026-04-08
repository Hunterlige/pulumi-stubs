import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CustomRPActionRouteDefinitionArgs",
    "CustomRPActionRouteDefinitionArgsDict",
    "CustomRPResourceTypeRouteDefinitionArgs",
    "CustomRPResourceTypeRouteDefinitionArgsDict",
    "CustomRPValidationsArgs",
    "CustomRPValidationsArgsDict",
]

class CustomRPActionRouteDefinitionArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    routing_type: NotRequired[pulumi.Input[Union[_builtins.str, ActionRouting]]]

@pulumi.input_type
class CustomRPActionRouteDefinitionArgs:
    def __init__(
        __self__,
        *,
        endpoint: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        routing_type: Optional[pulumi.Input[Union[_builtins.str, ActionRouting]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="routingType")
    def routing_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ActionRouting]]]: ...
    @routing_type.setter
    def routing_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ActionRouting]]]
    ): ...

class CustomRPResourceTypeRouteDefinitionArgsDict(TypedDict):
    endpoint: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    routing_type: NotRequired[pulumi.Input[Union[_builtins.str, ResourceTypeRouting]]]

@pulumi.input_type
class CustomRPResourceTypeRouteDefinitionArgs:
    def __init__(
        __self__,
        *,
        endpoint: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        routing_type: Optional[
            pulumi.Input[Union[_builtins.str, ResourceTypeRouting]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="routingType")
    def routing_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceTypeRouting]]]: ...
    @routing_type.setter
    def routing_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceTypeRouting]]]
    ): ...

class CustomRPValidationsArgsDict(TypedDict):
    specification: pulumi.Input[_builtins.str]
    validation_type: NotRequired[pulumi.Input[Union[_builtins.str, ValidationType]]]

@pulumi.input_type
class CustomRPValidationsArgs:
    def __init__(
        __self__,
        *,
        specification: pulumi.Input[_builtins.str],
        validation_type: Optional[
            pulumi.Input[Union[_builtins.str, ValidationType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def specification(self) -> pulumi.Input[_builtins.str]: ...
    @specification.setter
    def specification(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="validationType")
    def validation_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ValidationType]]]: ...
    @validation_type.setter
    def validation_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ValidationType]]]
    ): ...
