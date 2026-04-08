import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetContentTypeResult",
    "AwaitableGetContentTypeResult",
    "get_content_type",
    "get_content_type_output",
]

@pulumi.output_type
class GetContentTypeResult:
    def __init__(
        __self__,
        azure_api_version=...,
        description=...,
        id=...,
        name=...,
        schema=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

class AwaitableGetContentTypeResult(GetContentTypeResult):
    def __await__(self): ...

def get_content_type(
    content_type_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetContentTypeResult: ...
def get_content_type_output(
    content_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetContentTypeResult]: ...
