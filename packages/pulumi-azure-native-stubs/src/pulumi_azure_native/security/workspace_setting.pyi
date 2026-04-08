import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkspaceSettingArgs", "WorkspaceSetting"]

@pulumi.input_type
class WorkspaceSettingArgs:
    def __init__(
        __self__,
        *,
        scope: pulumi.Input[_builtins.str],
        workspace_id: pulumi.Input[_builtins.str],
        workspace_setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceSettingName")
    def workspace_setting_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_setting_name.setter
    def workspace_setting_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:security:WorkspaceSetting")
class WorkspaceSetting(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_setting_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkspaceSettingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WorkspaceSetting: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[_builtins.str]: ...
