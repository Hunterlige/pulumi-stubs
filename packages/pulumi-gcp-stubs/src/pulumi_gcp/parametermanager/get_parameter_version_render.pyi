import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetParameterVersionRenderResult",
    "AwaitableGetParameterVersionRenderResult",
    "get_parameter_version_render",
    "get_parameter_version_render_output",
]

@pulumi.output_type
class GetParameterVersionRenderResult:
    def __init__(
        __self__,
        disabled=...,
        id=...,
        name=...,
        parameter=...,
        parameter_data=...,
        parameter_version_id=...,
        project=...,
        rendered_parameter_data=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterData")
    def parameter_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterVersionId")
    def parameter_version_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="renderedParameterData")
    def rendered_parameter_data(self) -> _builtins.str: ...

class AwaitableGetParameterVersionRenderResult(GetParameterVersionRenderResult):
    def __await__(self): ...

def get_parameter_version_render(
    parameter: Optional[_builtins.str] = ...,
    parameter_version_id: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetParameterVersionRenderResult: ...
def get_parameter_version_render_output(
    parameter: Optional[pulumi.Input[_builtins.str]] = ...,
    parameter_version_id: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetParameterVersionRenderResult]: ...
