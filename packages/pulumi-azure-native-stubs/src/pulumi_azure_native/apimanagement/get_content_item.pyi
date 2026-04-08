import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetContentItemResult",
    "AwaitableGetContentItemResult",
    "get_content_item",
    "get_content_item_output",
]

@pulumi.output_type
class GetContentItemResult:
    def __init__(
        __self__, azure_api_version=..., id=..., name=..., properties=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
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

class AwaitableGetContentItemResult(GetContentItemResult):
    def __await__(self): ...

def get_content_item(
    content_item_id: Optional[_builtins.str] = ...,
    content_type_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetContentItemResult: ...
def get_content_item_output(
    content_item_id: Optional[pulumi.Input[_builtins.str]] = ...,
    content_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetContentItemResult]: ...
