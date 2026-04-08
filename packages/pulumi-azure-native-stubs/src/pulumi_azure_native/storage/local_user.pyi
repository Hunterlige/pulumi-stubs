import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LocalUserArgs", "LocalUser"]

@pulumi.input_type
class LocalUserArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        allow_acl_authorization: Optional[pulumi.Input[_builtins.bool]] = ...,
        extended_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        group_id: Optional[pulumi.Input[_builtins.int]] = ...,
        has_shared_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        has_ssh_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        has_ssh_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        home_directory: Optional[pulumi.Input[_builtins.str]] = ...,
        is_nf_sv3_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        permission_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[PermissionScopeArgs]]]
        ] = ...,
        ssh_authorized_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]
        ] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="allowAclAuthorization")
    def allow_acl_authorization(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_acl_authorization.setter
    def allow_acl_authorization(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedGroups")
    def extended_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @extended_groups.setter
    def extended_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="hasSharedKey")
    def has_shared_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @has_shared_key.setter
    def has_shared_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="hasSshKey")
    def has_ssh_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @has_ssh_key.setter
    def has_ssh_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="hasSshPassword")
    def has_ssh_password(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @has_ssh_password.setter
    def has_ssh_password(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @home_directory.setter
    def home_directory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isNFSv3Enabled")
    def is_nf_sv3_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_nf_sv3_enabled.setter
    def is_nf_sv3_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="permissionScopes")
    def permission_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PermissionScopeArgs]]]]: ...
    @permission_scopes.setter
    def permission_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PermissionScopeArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sshAuthorizedKeys")
    def ssh_authorized_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]]: ...
    @ssh_authorized_keys.setter
    def ssh_authorized_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SshPublicKeyArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:storage:LocalUser")
class LocalUser(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        allow_acl_authorization: Optional[pulumi.Input[_builtins.bool]] = ...,
        extended_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        group_id: Optional[pulumi.Input[_builtins.int]] = ...,
        has_shared_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        has_ssh_key: Optional[pulumi.Input[_builtins.bool]] = ...,
        has_ssh_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        home_directory: Optional[pulumi.Input[_builtins.str]] = ...,
        is_nf_sv3_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        permission_scopes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[PermissionScopeArgs, PermissionScopeArgsDict]]
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        ssh_authorized_keys: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[SshPublicKeyArgs, SshPublicKeyArgsDict]]]
            ]
        ] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LocalUserArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> LocalUser: ...
    @_builtins.property
    @pulumi.getter(name="allowAclAuthorization")
    def allow_acl_authorization(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extendedGroups")
    def extended_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.int]]]: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="hasSharedKey")
    def has_shared_key(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="hasSshKey")
    def has_ssh_key(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="hasSshPassword")
    def has_ssh_password(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isNFSv3Enabled")
    def is_nf_sv3_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permissionScopes")
    def permission_scopes(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PermissionScopeResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def sid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sshAuthorizedKeys")
    def ssh_authorized_keys(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.SshPublicKeyResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[_builtins.int]: ...
