import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GroupMembershipArgs", "GroupMembership"]

@pulumi.input_type
class GroupMembershipArgs:
    def __init__(
        __self__,
        *,
        group: pulumi.Input[_builtins.str],
        roles: pulumi.Input[Sequence[pulumi.Input[GroupMembershipRoleArgs]]],
        create_ignore_already_exists: Optional[pulumi.Input[_builtins.bool]] = ...,
        member_key: Optional[pulumi.Input[GroupMembershipMemberKeyArgs]] = ...,
        preferred_member_key: Optional[
            pulumi.Input[GroupMembershipPreferredMemberKeyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> pulumi.Input[_builtins.str]: ...
    @group.setter
    def group(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[GroupMembershipRoleArgs]]]: ...
    @roles.setter
    def roles(
        self, value: pulumi.Input[Sequence[pulumi.Input[GroupMembershipRoleArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createIgnoreAlreadyExists")
    def create_ignore_already_exists(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_ignore_already_exists.setter
    def create_ignore_already_exists(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="memberKey")
    def member_key(self) -> Optional[pulumi.Input[GroupMembershipMemberKeyArgs]]: ...
    @member_key.setter
    def member_key(
        self, value: Optional[pulumi.Input[GroupMembershipMemberKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preferredMemberKey")
    def preferred_member_key(
        self,
    ) -> Optional[pulumi.Input[GroupMembershipPreferredMemberKeyArgs]]: ...
    @preferred_member_key.setter
    def preferred_member_key(
        self, value: Optional[pulumi.Input[GroupMembershipPreferredMemberKeyArgs]]
    ): ...

@pulumi.input_type
class _GroupMembershipState:
    def __init__(
        __self__,
        *,
        create_ignore_already_exists: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        member_key: Optional[pulumi.Input[GroupMembershipMemberKeyArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_member_key: Optional[
            pulumi.Input[GroupMembershipPreferredMemberKeyArgs]
        ] = ...,
        roles: Optional[
            pulumi.Input[Sequence[pulumi.Input[GroupMembershipRoleArgs]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createIgnoreAlreadyExists")
    def create_ignore_already_exists(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_ignore_already_exists.setter
    def create_ignore_already_exists(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group.setter
    def group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memberKey")
    def member_key(self) -> Optional[pulumi.Input[GroupMembershipMemberKeyArgs]]: ...
    @member_key.setter
    def member_key(
        self, value: Optional[pulumi.Input[GroupMembershipMemberKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredMemberKey")
    def preferred_member_key(
        self,
    ) -> Optional[pulumi.Input[GroupMembershipPreferredMemberKeyArgs]]: ...
    @preferred_member_key.setter
    def preferred_member_key(
        self, value: Optional[pulumi.Input[GroupMembershipPreferredMemberKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[GroupMembershipRoleArgs]]]]: ...
    @roles.setter
    def roles(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[GroupMembershipRoleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:cloudidentity/groupMembership:GroupMembership")
class GroupMembership(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_ignore_already_exists: Optional[pulumi.Input[_builtins.bool]] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        member_key: Optional[
            pulumi.Input[
                Union[GroupMembershipMemberKeyArgs, GroupMembershipMemberKeyArgsDict]
            ]
        ] = ...,
        preferred_member_key: Optional[
            pulumi.Input[
                Union[
                    GroupMembershipPreferredMemberKeyArgs,
                    GroupMembershipPreferredMemberKeyArgsDict,
                ]
            ]
        ] = ...,
        roles: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[GroupMembershipRoleArgs, GroupMembershipRoleArgsDict]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GroupMembershipArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_ignore_already_exists: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        group: Optional[pulumi.Input[_builtins.str]] = ...,
        member_key: Optional[
            pulumi.Input[
                Union[GroupMembershipMemberKeyArgs, GroupMembershipMemberKeyArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        preferred_member_key: Optional[
            pulumi.Input[
                Union[
                    GroupMembershipPreferredMemberKeyArgs,
                    GroupMembershipPreferredMemberKeyArgsDict,
                ]
            ]
        ] = ...,
        roles: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[GroupMembershipRoleArgs, GroupMembershipRoleArgsDict]
                    ]
                ]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> GroupMembership: ...
    @_builtins.property
    @pulumi.getter(name="createIgnoreAlreadyExists")
    def create_ignore_already_exists(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memberKey")
    def member_key(self) -> pulumi.Output[outputs.GroupMembershipMemberKey]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preferredMemberKey")
    def preferred_member_key(
        self,
    ) -> pulumi.Output[outputs.GroupMembershipPreferredMemberKey]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Sequence[outputs.GroupMembershipRole]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
