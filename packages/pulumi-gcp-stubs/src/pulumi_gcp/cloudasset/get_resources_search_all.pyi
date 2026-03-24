import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetResourcesSearchAllResult",
    "AwaitableGetResourcesSearchAllResult",
    "get_resources_search_all",
    "get_resources_search_all_output",
]

@pulumi.output_type
class GetResourcesSearchAllResult:
    def __init__(
        __self__, asset_types=..., id=..., query=..., results=..., scope=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assetTypes")
    def asset_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def results(self) -> Sequence[outputs.GetResourcesSearchAllResultResult]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...

class AwaitableGetResourcesSearchAllResult(GetResourcesSearchAllResult):
    def __await__(self): ...

def get_resources_search_all(
    asset_types: Optional[Sequence[_builtins.str]] = ...,
    query: Optional[_builtins.str] = ...,
    scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetResourcesSearchAllResult: ...
def get_resources_search_all_output(
    asset_types: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    query: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetResourcesSearchAllResult]: ...
