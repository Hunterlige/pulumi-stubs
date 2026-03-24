import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetZonesResult", "AwaitableGetZonesResult", "get_zones", "get_zones_output"]

@pulumi.output_type
class GetZonesResult:
    def __init__(__self__, id=..., ids=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]: ...

class AwaitableGetZonesResult(GetZonesResult):
    def __await__(self): ...

def get_zones(
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetZonesResult: ...
def get_zones_output(
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetZonesResult]: ...
