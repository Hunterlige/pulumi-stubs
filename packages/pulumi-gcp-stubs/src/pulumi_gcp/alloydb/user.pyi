import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UserArgs", "User"]

@pulumi.input_type
class UserArgs:
    def __init__(
        __self__,
        *,
        cluster: pulumi.Input[_builtins.str],
        user_id: pulumi.Input[_builtins.str],
        user_type: pulumi.Input[_builtins.str],
        database_roles: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[_builtins.str]: ...
    @cluster.setter
    def cluster(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[_builtins.str]: ...
    @user_id.setter
    def user_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> pulumi.Input[_builtins.str]: ...
    @user_type.setter
    def user_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseRoles")
    def database_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @database_roles.setter
    def database_roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_wo.setter
    def password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_wo_version.setter
    def password_wo_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _UserState:
    def __init__(
        __self__,
        *,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        database_roles: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
        user_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseRoles")
    def database_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @database_roles.setter
    def database_roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_wo.setter
    def password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_wo_version.setter
    def password_wo_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_type.setter
    def user_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:alloydb/user:User")
class User(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        database_roles: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
        user_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UserArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        database_roles: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        password_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
        user_id: Optional[pulumi.Input[_builtins.str]] = ...,
        user_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> User: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databaseRoles")
    def database_roles(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="passwordWo")
    def password_wo(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="passwordWoVersion")
    def password_wo_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> pulumi.Output[_builtins.str]: ...
