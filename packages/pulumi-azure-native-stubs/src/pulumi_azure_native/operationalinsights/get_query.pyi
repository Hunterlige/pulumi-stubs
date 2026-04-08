import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetQueryResult", "AwaitableGetQueryResult", "get_query", "get_query_output"]

@pulumi.output_type
class GetQueryResult:
    def __init__(
        __self__,
        author=...,
        azure_api_version=...,
        body=...,
        description=...,
        display_name=...,
        id=...,
        name=...,
        properties=...,
        related=...,
        system_data=...,
        tags=...,
        time_created=...,
        time_modified=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def author(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def related(
        self,
    ) -> Optional[outputs.LogAnalyticsQueryPackQueryPropertiesResponseRelated]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetQueryResult(GetQueryResult):
    def __await__(self): ...

def get_query(
    id: Optional[_builtins.str] = ...,
    query_pack_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetQueryResult: ...
def get_query_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    query_pack_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetQueryResult]: ...
