import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPlaywrightWorkspaceResult",
    "AwaitableGetPlaywrightWorkspaceResult",
    "get_playwright_workspace",
    "get_playwright_workspace_output",
]

@pulumi.output_type
class GetPlaywrightWorkspaceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        dataplane_uri=...,
        id=...,
        local_auth=...,
        location=...,
        name=...,
        provisioning_state=...,
        regional_affinity=...,
        system_data=...,
        tags=...,
        type=...,
        workspace_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataplaneUri")
    def dataplane_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localAuth")
    def local_auth(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regionalAffinity")
    def regional_affinity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> _builtins.str: ...

class AwaitableGetPlaywrightWorkspaceResult(GetPlaywrightWorkspaceResult):
    def __await__(self): ...

def get_playwright_workspace(
    playwright_workspace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPlaywrightWorkspaceResult: ...
def get_playwright_workspace_output(
    playwright_workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPlaywrightWorkspaceResult]: ...
