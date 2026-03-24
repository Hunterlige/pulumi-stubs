import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GroupConfigurationArgs",
    "GroupConfigurationArgsDict",
    "GroupConfigurationParameterArgs",
    "GroupConfigurationParameterArgsDict",
    "GroupResourceQueryArgs",
    "GroupResourceQueryArgsDict",
]

class GroupConfigurationArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[GroupConfigurationParameterArgsDict]]]
    ]
    ...

@pulumi.input_type
class GroupConfigurationArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[GroupConfigurationParameterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[GroupConfigurationParameterArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[GroupConfigurationParameterArgs]]]
        ],
    ): ...

class GroupConfigurationParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class GroupConfigurationParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class GroupResourceQueryArgsDict(TypedDict):
    query: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GroupResourceQueryArgs:
    def __init__(
        __self__,
        *,
        query: pulumi.Input[_builtins.str],
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Input[_builtins.str]: ...
    @query.setter
    def query(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
