import builtins as _builtins
import sys
import pulumi

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetRegionsRegionResult"]

@pulumi.output_type
class GetRegionsRegionResult(dict):
    def __init__(
        __self__, *, region_name: _builtins.str, region_opt_status: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regionOptStatus")
    def region_opt_status(self) -> _builtins.str: ...
