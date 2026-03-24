import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetMultiRegionAccessPointsResult",
    "AwaitableGetMultiRegionAccessPointsResult",
    "get_multi_region_access_points",
    "get_multi_region_access_points_output",
]

@pulumi.output_type
class GetMultiRegionAccessPointsResult:
    def __init__(
        __self__, access_points=..., account_id=..., id=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPoints")
    def access_points(
        self,
    ) -> Sequence[outputs.GetMultiRegionAccessPointsAccessPointResult]: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetMultiRegionAccessPointsResult(GetMultiRegionAccessPointsResult):
    def __await__(self): ...

def get_multi_region_access_points(
    account_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetMultiRegionAccessPointsResult: ...
def get_multi_region_access_points_output(
    account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetMultiRegionAccessPointsResult]: ...
