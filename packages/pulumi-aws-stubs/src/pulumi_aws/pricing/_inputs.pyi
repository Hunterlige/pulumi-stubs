import builtins as _builtins
import sys
import pulumi
from typing import TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetProductFilterArgs", "GetProductFilterArgsDict"]

class GetProductFilterArgsDict(TypedDict):
    field: _builtins.str
    value: _builtins.str

@pulumi.input_type
class GetProductFilterArgs:
    def __init__(__self__, *, field: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> _builtins.str: ...
    @field.setter
    def field(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @value.setter
    def value(self, value: _builtins.str): ...
