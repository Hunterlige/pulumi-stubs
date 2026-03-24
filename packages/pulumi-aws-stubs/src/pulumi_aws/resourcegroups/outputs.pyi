import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GroupConfiguration", "GroupConfigurationParameter", "GroupResourceQuery"]

@pulumi.output_type
class GroupConfiguration(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        parameters: Optional[Sequence[outputs.GroupConfigurationParameter]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.GroupConfigurationParameter]]: ...

@pulumi.output_type
class GroupConfigurationParameter(dict):
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
class GroupResourceQuery(dict):
    def __init__(
        __self__, *, query: _builtins.str, type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
