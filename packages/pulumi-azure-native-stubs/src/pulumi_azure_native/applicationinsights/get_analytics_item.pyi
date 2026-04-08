import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAnalyticsItemResult",
    "AwaitableGetAnalyticsItemResult",
    "get_analytics_item",
    "get_analytics_item_output",
]

@pulumi.output_type
class GetAnalyticsItemResult:
    def __init__(
        __self__,
        azure_api_version=...,
        content=...,
        id=...,
        name=...,
        properties=...,
        scope=...,
        time_created=...,
        time_modified=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> outputs.ApplicationInsightsComponentAnalyticsItemPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetAnalyticsItemResult(GetAnalyticsItemResult):
    def __await__(self): ...

def get_analytics_item(
    id: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    scope_path: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAnalyticsItemResult: ...
def get_analytics_item_output(
    id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    scope_path: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAnalyticsItemResult]: ...
