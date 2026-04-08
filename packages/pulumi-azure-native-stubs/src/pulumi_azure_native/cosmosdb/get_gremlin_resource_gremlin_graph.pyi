import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGremlinResourceGremlinGraphResult",
    "AwaitableGetGremlinResourceGremlinGraphResult",
    "get_gremlin_resource_gremlin_graph",
    "get_gremlin_resource_gremlin_graph_output",
]

@pulumi.output_type
class GetGremlinResourceGremlinGraphResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        options=...,
        resource=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[outputs.GremlinGraphGetPropertiesResponseOptions]: ...
    @_builtins.property
    @pulumi.getter
    def resource(
        self,
    ) -> Optional[outputs.GremlinGraphGetPropertiesResponseResource]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetGremlinResourceGremlinGraphResult(
    GetGremlinResourceGremlinGraphResult
):
    def __await__(self): ...

def get_gremlin_resource_gremlin_graph(
    account_name: Optional[_builtins.str] = ...,
    database_name: Optional[_builtins.str] = ...,
    graph_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGremlinResourceGremlinGraphResult: ...
def get_gremlin_resource_gremlin_graph_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    database_name: Optional[pulumi.Input[_builtins.str]] = ...,
    graph_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGremlinResourceGremlinGraphResult]: ...
