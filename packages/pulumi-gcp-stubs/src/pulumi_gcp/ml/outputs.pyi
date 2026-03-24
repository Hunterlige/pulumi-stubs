import builtins as _builtins
import sys
import pulumi

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["EngineModelDefaultVersion"]

@pulumi.output_type
class EngineModelDefaultVersion(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
