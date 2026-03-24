import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetExportResult",
    "AwaitableGetExportResult",
    "get_export",
    "get_export_output",
]

@pulumi.output_type
class GetExportResult:
    def __init__(
        __self__,
        api_id=...,
        body=...,
        export_version=...,
        id=...,
        include_extensions=...,
        output_type=...,
        region=...,
        specification=...,
        stage_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="exportVersion")
    def export_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includeExtensions")
    def include_extensions(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def specification(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> Optional[_builtins.str]: ...

class AwaitableGetExportResult(GetExportResult):
    def __await__(self): ...

def get_export(
    api_id: Optional[_builtins.str] = ...,
    export_version: Optional[_builtins.str] = ...,
    include_extensions: Optional[_builtins.bool] = ...,
    output_type: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    specification: Optional[_builtins.str] = ...,
    stage_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetExportResult: ...
def get_export_output(
    api_id: Optional[pulumi.Input[_builtins.str]] = ...,
    export_version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    include_extensions: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    output_type: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    specification: Optional[pulumi.Input[_builtins.str]] = ...,
    stage_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetExportResult]: ...
