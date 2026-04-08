import builtins as _builtins
import sys
import pulumi
from typing import Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetConnectionFilterArgs", "GetConnectionFilterArgsDict"]

class GetConnectionFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]

@pulumi.input_type
class GetConnectionFilterArgs:
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @name.setter
    def name(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...
    @values.setter
    def values(self, value: Sequence[_builtins.str]): ...
