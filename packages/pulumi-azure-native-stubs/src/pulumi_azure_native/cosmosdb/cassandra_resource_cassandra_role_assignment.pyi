import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CassandraResourceCassandraRoleAssignmentArgs",
    "CassandraResourceCassandraRoleAssignment",
]

@pulumi.input_type
class CassandraResourceCassandraRoleAssignmentArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_assignment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleAssignmentId")
    def role_assignment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_assignment_id.setter
    def role_assignment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_definition_id.setter
    def role_definition_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class CassandraResourceCassandraRoleAssignment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        role_assignment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CassandraResourceCassandraRoleAssignmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> CassandraResourceCassandraRoleAssignment: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
