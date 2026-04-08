import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTagApiLinkResult",
    "AwaitableGetTagApiLinkResult",
    "get_tag_api_link",
    "get_tag_api_link_output",
]

@pulumi.output_type
class GetTagApiLinkResult:
    def __init__(
        __self__, api_id=..., azure_api_version=..., id=..., name=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> _builtins.str: ...
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
    def type(self) -> _builtins.str: ...

class AwaitableGetTagApiLinkResult(GetTagApiLinkResult):
    def __await__(self): ...

def get_tag_api_link(
    api_link_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    tag_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTagApiLinkResult: ...
def get_tag_api_link_output(
    api_link_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    tag_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTagApiLinkResult]: ...
