import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTagAtScopeResult",
    "AwaitableGetTagAtScopeResult",
    "get_tag_at_scope",
    "get_tag_at_scope_output",
]

@pulumi.output_type
class GetTagAtScopeResult:
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
    def properties(self) -> outputs.TagsResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetTagAtScopeResult(GetTagAtScopeResult):
    def __await__(self): ...

def get_tag_at_scope(
    scope: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetTagAtScopeResult: ...
def get_tag_at_scope_output(
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTagAtScopeResult]: ...
