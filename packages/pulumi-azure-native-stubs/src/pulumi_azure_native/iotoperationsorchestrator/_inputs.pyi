import builtins as _builtins
import sys
import pulumi
from typing import Any, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BindingPropertiesArgs",
    "BindingPropertiesArgsDict",
    "ComponentPropertiesArgs",
    "ComponentPropertiesArgsDict",
    "ExtendedLocationArgs",
    "ExtendedLocationArgsDict",
    "ReconciliationPolicyArgs",
    "ReconciliationPolicyArgsDict",
    "TargetSelectorPropertiesArgs",
    "TargetSelectorPropertiesArgsDict",
    "TopologiesPropertiesArgs",
    "TopologiesPropertiesArgsDict",
]

class BindingPropertiesArgsDict(TypedDict):
    config: Any
    provider: pulumi.Input[_builtins.str]
    role: pulumi.Input[_builtins.str]

@pulumi.input_type
class BindingPropertiesArgs:
    def __init__(
        __self__,
        *,
        config: Any,
        provider: pulumi.Input[_builtins.str],
        role: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Any: ...
    @config.setter
    def config(self, value: Any): ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> pulumi.Input[_builtins.str]: ...
    @provider.setter
    def provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]: ...
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): ...

class ComponentPropertiesArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    dependencies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    properties: NotRequired[Any]

@pulumi.input_type
class ComponentPropertiesArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        dependencies: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        properties: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dependencies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dependencies.setter
    def dependencies(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Any]: ...
    @properties.setter
    def properties(self, value: Optional[Any]): ...

class ExtendedLocationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ExtendedLocationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ReconciliationPolicyArgsDict(TypedDict):
    type: pulumi.Input[Union[_builtins.str, ReconciliationPolicies]]
    interval: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReconciliationPolicyArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, ReconciliationPolicies]],
        interval: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ReconciliationPolicies]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ReconciliationPolicies]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TargetSelectorPropertiesArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TargetSelectorPropertiesArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TopologiesPropertiesArgsDict(TypedDict):
    bindings: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BindingPropertiesArgsDict]]]
    ]

@pulumi.input_type
class TopologiesPropertiesArgs:
    def __init__(
        __self__,
        *,
        bindings: Optional[
            pulumi.Input[Sequence[pulumi.Input[BindingPropertiesArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bindings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BindingPropertiesArgs]]]]: ...
    @bindings.setter
    def bindings(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[BindingPropertiesArgs]]]],
    ): ...
