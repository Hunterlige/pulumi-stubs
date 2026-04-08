import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkspaceApiReleaseResult",
    "AwaitableGetWorkspaceApiReleaseResult",
    "get_workspace_api_release",
    "get_workspace_api_release_output",
]

@pulumi.output_type
class GetWorkspaceApiReleaseResult:
    def __init__(
        __self__,
        api_id=...,
        azure_api_version=...,
        created_date_time=...,
        id=...,
        name=...,
        notes=...,
        type=...,
        updated_date_time=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedDateTime")
    def updated_date_time(self) -> _builtins.str: ...

class AwaitableGetWorkspaceApiReleaseResult(GetWorkspaceApiReleaseResult):
    def __await__(self): ...

def get_workspace_api_release(
    api_id: Optional[_builtins.str] = ...,
    release_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    workspace_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkspaceApiReleaseResult: ...
def get_workspace_api_release_output(
    api_id: Optional[pulumi.Input[_builtins.str]] = ...,
    release_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkspaceApiReleaseResult]: ...
