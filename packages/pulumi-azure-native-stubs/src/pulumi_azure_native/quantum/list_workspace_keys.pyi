import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListWorkspaceKeysResult",
    "AwaitableListWorkspaceKeysResult",
    "list_workspace_keys",
    "list_workspace_keys_output",
]

@pulumi.output_type
class ListWorkspaceKeysResult:
    def __init__(
        __self__,
        api_key_enabled=...,
        primary_connection_string=...,
        primary_key=...,
        secondary_connection_string=...,
        secondary_key=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyEnabled")
    def api_key_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="primaryConnectionString")
    def primary_connection_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[outputs.ApiKeyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryConnectionString")
    def secondary_connection_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[outputs.ApiKeyResponse]: ...

class AwaitableListWorkspaceKeysResult(ListWorkspaceKeysResult):
    def __await__(self): ...

def list_workspace_keys(
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListWorkspaceKeysResult: ...
def list_workspace_keys_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListWorkspaceKeysResult]: ...
