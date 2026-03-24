import builtins as _builtins
import sys
import pulumi
from typing import TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EngineModelDefaultVersionArgs", "EngineModelDefaultVersionArgsDict"]

class EngineModelDefaultVersionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class EngineModelDefaultVersionArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
