import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DeploymentLabelArgs",
    "DeploymentLabelArgsDict",
    "DeploymentTargetArgs",
    "DeploymentTargetArgsDict",
    "DeploymentTargetConfigArgs",
    "DeploymentTargetConfigArgsDict",
    "DeploymentTargetImportArgs",
    "DeploymentTargetImportArgsDict",
]

class DeploymentLabelArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DeploymentLabelArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentTargetArgsDict(TypedDict):
    config: pulumi.Input[DeploymentTargetConfigArgsDict]
    imports: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DeploymentTargetImportArgsDict]]]
    ]
    ...

@pulumi.input_type
class DeploymentTargetArgs:
    def __init__(
        __self__,
        *,
        config: pulumi.Input[DeploymentTargetConfigArgs],
        imports: Optional[
            pulumi.Input[Sequence[pulumi.Input[DeploymentTargetImportArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Input[DeploymentTargetConfigArgs]: ...
    @config.setter
    def config(self, value: pulumi.Input[DeploymentTargetConfigArgs]): ...
    @_builtins.property
    @pulumi.getter
    def imports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeploymentTargetImportArgs]]]]: ...
    @imports.setter
    def imports(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DeploymentTargetImportArgs]]]
        ],
    ): ...

class DeploymentTargetConfigArgsDict(TypedDict):
    content: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DeploymentTargetConfigArgs:
    def __init__(__self__, *, content: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Input[_builtins.str]: ...
    @content.setter
    def content(self, value: pulumi.Input[_builtins.str]): ...

class DeploymentTargetImportArgsDict(TypedDict):
    content: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DeploymentTargetImportArgs:
    def __init__(
        __self__,
        *,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
