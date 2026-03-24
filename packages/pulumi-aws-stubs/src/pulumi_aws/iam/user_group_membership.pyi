import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UserGroupMembershipArgs", "UserGroupMembership"]

@pulumi.input_type
class UserGroupMembershipArgs:
    def __init__(
        __self__,
        *,
        groups: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        user: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def groups(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @groups.setter
    def groups(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Input[_builtins.str]: ...
    @user.setter
    def user(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _UserGroupMembershipState:
    def __init__(
        __self__,
        *,
        groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @groups.setter
    def groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:iam/userGroupMembership:UserGroupMembership")
class UserGroupMembership(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UserGroupMembershipArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> UserGroupMembership: ...
    @_builtins.property
    @pulumi.getter
    def groups(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Output[_builtins.str]: ...
