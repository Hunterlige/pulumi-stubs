import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SearchResult", "AwaitableSearchResult", "search", "search_output"]

@pulumi.output_type
class SearchResult:
    def __init__(
        __self__,
        id=...,
        query_string=...,
        region=...,
        resource_counts=...,
        resources=...,
        view_arn=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceCounts")
    def resource_counts(self) -> Sequence[outputs.SearchResourceCountResult]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Sequence[outputs.SearchResourceResult]: ...
    @_builtins.property
    @pulumi.getter(name="viewArn")
    def view_arn(self) -> _builtins.str: ...

class AwaitableSearchResult(SearchResult):
    def __await__(self): ...

def search(
    query_string: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    view_arn: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableSearchResult: ...
def search_output(
    query_string: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    view_arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[SearchResult]: ...
