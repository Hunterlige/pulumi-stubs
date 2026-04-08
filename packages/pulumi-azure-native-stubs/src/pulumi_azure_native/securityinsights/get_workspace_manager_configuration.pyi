import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkspaceManagerConfigurationResult",
    "AwaitableGetWorkspaceManagerConfigurationResult",
    "get_workspace_manager_configuration",
    "get_workspace_manager_configuration_output",
]

@pulumi.output_type
class GetWorkspaceManagerConfigurationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        etag=...,
        id=...,
        mode=...,
        name=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetWorkspaceManagerConfigurationResult(
    GetWorkspaceManagerConfigurationResult
):
    def __await__(self): ...

def get_workspace_manager_configuration(
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_manager_configuration_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkspaceManagerConfigurationResult: ...
def get_workspace_manager_configuration_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_manager_configuration_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkspaceManagerConfigurationResult]: ...
