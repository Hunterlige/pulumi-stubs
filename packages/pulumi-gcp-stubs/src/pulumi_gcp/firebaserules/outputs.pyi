import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RulesetMetadata", "RulesetSource", "RulesetSourceFile"]

@pulumi.output_type
class RulesetMetadata(dict):
    def __init__(
        __self__, *, services: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def services(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class RulesetSource(dict):
    def __init__(
        __self__,
        *,
        files: Sequence[outputs.RulesetSourceFile],
        language: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def files(self) -> Sequence[outputs.RulesetSourceFile]: ...
    @_builtins.property
    @pulumi.getter
    def language(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RulesetSourceFile(dict):
    def __init__(
        __self__,
        *,
        content: _builtins.str,
        name: _builtins.str,
        fingerprint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> Optional[_builtins.str]: ...
