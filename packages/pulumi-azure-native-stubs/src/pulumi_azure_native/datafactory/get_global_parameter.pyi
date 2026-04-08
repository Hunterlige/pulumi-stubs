import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGlobalParameterResult",
    "AwaitableGetGlobalParameterResult",
    "get_global_parameter",
    "get_global_parameter_output",
]

@pulumi.output_type
class GetGlobalParameterResult:
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
    def properties(
        self,
    ) -> Mapping[str, outputs.GlobalParameterSpecificationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetGlobalParameterResult(GetGlobalParameterResult):
    def __await__(self): ...

def get_global_parameter(
    factory_name: Optional[_builtins.str] = ...,
    global_parameter_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGlobalParameterResult: ...
def get_global_parameter_output(
    factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
    global_parameter_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGlobalParameterResult]: ...
