import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkspacesResult",
    "AwaitableGetWorkspacesResult",
    "get_workspaces",
    "get_workspaces_output",
]

@pulumi.output_type
class GetWorkspacesResult:
    def __init__(
        __self__,
        alias_prefix=...,
        aliases=...,
        arns=...,
        id=...,
        region=...,
        workspace_ids=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aliasPrefix")
    def alias_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def aliases(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workspaceIds")
    def workspace_ids(self) -> Sequence[_builtins.str]: ...

class AwaitableGetWorkspacesResult(GetWorkspacesResult):
    def __await__(self): ...

def get_workspaces(
    alias_prefix: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkspacesResult: ...
def get_workspaces_output(
    alias_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkspacesResult]: ...
