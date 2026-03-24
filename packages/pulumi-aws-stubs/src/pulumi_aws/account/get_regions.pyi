import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegionsResult",
    "AwaitableGetRegionsResult",
    "get_regions",
    "get_regions_output",
]

@pulumi.output_type
class GetRegionsResult:
    def __init__(
        __self__, account_id=..., id=..., region_opt_status_contains=..., regions=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regionOptStatusContains")
    def region_opt_status_contains(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Sequence[outputs.GetRegionsRegionResult]: ...

class AwaitableGetRegionsResult(GetRegionsResult):
    def __await__(self): ...

def get_regions(
    account_id: Optional[_builtins.str] = ...,
    region_opt_status_contains: Optional[Sequence[_builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegionsResult: ...
def get_regions_output(
    account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region_opt_status_contains: Optional[
        pulumi.Input[Optional[Sequence[_builtins.str]]]
    ] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegionsResult]: ...
