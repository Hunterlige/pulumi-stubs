import builtins as _builtins
import sys
import pulumi

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WebResourceSite"]

@pulumi.output_type
class WebResourceSite(dict):
    def __init__(
        __self__, *, identifier: _builtins.str, type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
