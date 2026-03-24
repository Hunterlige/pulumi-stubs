import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAssetsResult",
    "AwaitableGetAssetsResult",
    "get_assets",
    "get_assets_output",
]

@pulumi.output_type
class GetAssetsResult:
    def __init__(
        __self__,
        arn=...,
        asset_ids=...,
        host_id_filters=...,
        id=...,
        region=...,
        status_id_filters=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="assetIds")
    def asset_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostIdFilters")
    def host_id_filters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusIdFilters")
    def status_id_filters(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableGetAssetsResult(GetAssetsResult):
    def __await__(self): ...

def get_assets(
    arn: Optional[_builtins.str] = ...,
    host_id_filters: Optional[Sequence[_builtins.str]] = ...,
    region: Optional[_builtins.str] = ...,
    status_id_filters: Optional[Sequence[_builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAssetsResult: ...
def get_assets_output(
    arn: Optional[pulumi.Input[_builtins.str]] = ...,
    host_id_filters: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    status_id_filters: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAssetsResult]: ...
