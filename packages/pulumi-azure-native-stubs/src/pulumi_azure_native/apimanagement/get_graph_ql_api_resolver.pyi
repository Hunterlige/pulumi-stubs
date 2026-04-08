import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGraphQLApiResolverResult",
    "AwaitableGetGraphQLApiResolverResult",
    "get_graph_ql_api_resolver",
    "get_graph_ql_api_resolver_output",
]

@pulumi.output_type
class GetGraphQLApiResolverResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        display_name=...,
        id=...,
        name=...,
        path=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetGraphQLApiResolverResult(GetGraphQLApiResolverResult):
    def __await__(self): ...

def get_graph_ql_api_resolver(
    api_id: Optional[_builtins.str] = ...,
    resolver_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGraphQLApiResolverResult: ...
def get_graph_ql_api_resolver_output(
    api_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resolver_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGraphQLApiResolverResult]: ...
