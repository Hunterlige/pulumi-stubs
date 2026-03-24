import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetTagsResult", "AwaitableGetTagsResult", "get_tags", "get_tags_output"]

@pulumi.output_type
class GetTagsResult:
    def __init__(
        __self__,
        filter=...,
        id=...,
        search_string=...,
        sort_bies=...,
        tag_key=...,
        tags=...,
        time_period=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[outputs.GetTagsFilterResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="searchString")
    def search_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sortBies")
    def sort_bies(self) -> Optional[Sequence[outputs.GetTagsSortByResult]]: ...
    @_builtins.property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> outputs.GetTagsTimePeriodResult: ...

class AwaitableGetTagsResult(GetTagsResult):
    def __await__(self): ...

def get_tags(
    filter: Optional[Union[GetTagsFilterArgs, GetTagsFilterArgsDict]] = ...,
    search_string: Optional[_builtins.str] = ...,
    sort_bies: Optional[
        Sequence[Union[GetTagsSortByArgs, GetTagsSortByArgsDict]]
    ] = ...,
    tag_key: Optional[_builtins.str] = ...,
    time_period: Optional[
        Union[GetTagsTimePeriodArgs, GetTagsTimePeriodArgsDict]
    ] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTagsResult: ...
def get_tags_output(
    filter: Optional[
        pulumi.Input[Optional[Union[GetTagsFilterArgs, GetTagsFilterArgsDict]]]
    ] = ...,
    search_string: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    sort_bies: Optional[
        pulumi.Input[
            Optional[Sequence[Union[GetTagsSortByArgs, GetTagsSortByArgsDict]]]
        ]
    ] = ...,
    tag_key: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    time_period: Optional[
        pulumi.Input[Union[GetTagsTimePeriodArgs, GetTagsTimePeriodArgsDict]]
    ] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTagsResult]: ...
