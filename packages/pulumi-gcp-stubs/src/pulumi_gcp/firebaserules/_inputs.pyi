import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "RulesetMetadataArgs",
    "RulesetMetadataArgsDict",
    "RulesetSourceArgs",
    "RulesetSourceArgsDict",
    "RulesetSourceFileArgs",
    "RulesetSourceFileArgsDict",
]

class RulesetMetadataArgsDict(TypedDict):
    services: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RulesetMetadataArgs:
    def __init__(
        __self__,
        *,
        services: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @services.setter
    def services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RulesetSourceArgsDict(TypedDict):
    files: pulumi.Input[Sequence[pulumi.Input[RulesetSourceFileArgsDict]]]
    language: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RulesetSourceArgs:
    def __init__(
        __self__,
        *,
        files: pulumi.Input[Sequence[pulumi.Input[RulesetSourceFileArgs]]],
        language: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def files(self) -> pulumi.Input[Sequence[pulumi.Input[RulesetSourceFileArgs]]]: ...
    @files.setter
    def files(
        self, value: pulumi.Input[Sequence[pulumi.Input[RulesetSourceFileArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language.setter
    def language(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RulesetSourceFileArgsDict(TypedDict):
    content: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    fingerprint: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RulesetSourceFileArgs:
    def __init__(
        __self__,
        *,
        content: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Input[_builtins.str]: ...
    @content.setter
    def content(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
