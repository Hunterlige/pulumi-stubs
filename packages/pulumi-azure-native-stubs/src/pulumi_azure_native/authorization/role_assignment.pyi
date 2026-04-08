import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RoleAssignmentArgs", "RoleAssignment"]

@pulumi.input_type
class RoleAssignmentArgs:
    def __init__(
        __self__,
        *,
        principal_id: pulumi.Input[_builtins.str],
        role_definition_id: pulumi.Input[_builtins.str],
        scope: pulumi.Input[_builtins.str],
        condition: Optional[pulumi.Input[_builtins.str]] = ...,
        condition_version: Optional[pulumi.Input[_builtins.str]] = ...,
        delegated_managed_identity_resource_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_type: Optional[
            pulumi.Input[Union[_builtins.str, PrincipalType]]
        ] = ...,
        role_assignment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[_builtins.str]: ...
    @principal_id.setter
    def principal_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Input[_builtins.str]: ...
    @role_definition_id.setter
    def role_definition_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="conditionVersion")
    def condition_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @condition_version.setter
    def condition_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="delegatedManagedIdentityResourceId")
    def delegated_managed_identity_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delegated_managed_identity_resource_id.setter
    def delegated_managed_identity_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrincipalType]]]: ...
    @principal_type.setter
    def principal_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PrincipalType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleAssignmentName")
    def role_assignment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_assignment_name.setter
    def role_assignment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:authorization:RoleAssignment")
class RoleAssignment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        condition: Optional[pulumi.Input[_builtins.str]] = ...,
        condition_version: Optional[pulumi.Input[_builtins.str]] = ...,
        delegated_managed_identity_resource_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_type: Optional[
            pulumi.Input[Union[_builtins.str, PrincipalType]]
        ] = ...,
        role_assignment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RoleAssignmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> RoleAssignment: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="conditionVersion")
    def condition_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="delegatedManagedIdentityResourceId")
    def delegated_managed_identity_resource_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedOn")
    def updated_on(self) -> pulumi.Output[_builtins.str]: ...
