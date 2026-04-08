import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkspaceManagerMemberArgs", "WorkspaceManagerMember"]

@pulumi.input_type
class WorkspaceManagerMemberArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        target_workspace_resource_id: pulumi.Input[_builtins.str],
        target_workspace_tenant_id: pulumi.Input[_builtins.str],
        workspace_name: pulumi.Input[_builtins.str],
        workspace_manager_member_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetWorkspaceResourceId")
    def target_workspace_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_workspace_resource_id.setter
    def target_workspace_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetWorkspaceTenantId")
    def target_workspace_tenant_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_workspace_tenant_id.setter
    def target_workspace_tenant_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceManagerMemberName")
    def workspace_manager_member_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_manager_member_name.setter
    def workspace_manager_member_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class WorkspaceManagerMember(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_workspace_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        target_workspace_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_manager_member_name: Optional[pulumi.Input[_builtins.str]] = ...,
        workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkspaceManagerMemberArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> WorkspaceManagerMember: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="targetWorkspaceResourceId")
    def target_workspace_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetWorkspaceTenantId")
    def target_workspace_tenant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
