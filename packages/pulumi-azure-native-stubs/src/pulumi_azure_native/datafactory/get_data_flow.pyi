import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDataFlowResult",
    "AwaitableGetDataFlowResult",
    "get_data_flow",
    "get_data_flow_output",
]

@pulumi.output_type
class GetDataFlowResult:
    def __init__(
        __self__,
        azure_api_version=...,
        etag=...,
        id=...,
        name=...,
        properties=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
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
    def type(self) -> _builtins.str: ...

class AwaitableGetDataFlowResult(GetDataFlowResult):
    def __await__(self): ...

def get_data_flow(
    data_flow_name: Optional[_builtins.str] = ...,
    factory_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDataFlowResult: ...
def get_data_flow_output(
    data_flow_name: Optional[pulumi.Input[_builtins.str]] = ...,
    factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDataFlowResult]: ...
