import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLaunchPathsResult",
    "AwaitableGetLaunchPathsResult",
    "get_launch_paths",
    "get_launch_paths_output",
]

@pulumi.output_type
class GetLaunchPathsResult:
    def __init__(
        __self__, accept_language=..., id=..., product_id=..., region=..., summaries=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def summaries(self) -> Sequence[outputs.GetLaunchPathsSummaryResult]: ...

class AwaitableGetLaunchPathsResult(GetLaunchPathsResult):
    def __await__(self): ...

def get_launch_paths(
    accept_language: Optional[_builtins.str] = ...,
    product_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLaunchPathsResult: ...
def get_launch_paths_output(
    accept_language: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    product_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLaunchPathsResult]: ...
