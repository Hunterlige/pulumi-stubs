import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkspaceManagerConfigurationArgs", "WorkspaceManagerConfiguration"]

@pulumi.input_type
class WorkspaceManagerConfigurationArgs:
    def __init__(
        __self__,
        *,
        mode: pulumi.Input[Union[_builtins.str, Mode]],
        resource_group_name: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        workspace_manager_configuration_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[Union[_builtins.str, Mode]]: ...
    @mode.setter
    def mode(self, value: pulumi.Input[Union[_builtins.str, Mode]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceManagerConfigurationName")
    def workspace_manager_configuration_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_manager_configuration_name.setter
    def workspace_manager_configuration_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class WorkspaceManagerConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        mode: Optional[pulumi.Input[Union[_builtins.str, Mode]]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_manager_configuration_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkspaceManagerConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WorkspaceManagerConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
