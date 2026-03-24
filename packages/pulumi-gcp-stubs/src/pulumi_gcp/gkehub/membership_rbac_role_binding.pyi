import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MembershipRbacRoleBindingArgs", "MembershipRbacRoleBinding"]

@pulumi.input_type
class MembershipRbacRoleBindingArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        membership_id: pulumi.Input[_builtins.str],
        membership_rbac_role_binding_id: pulumi.Input[_builtins.str],
        role: pulumi.Input[MembershipRbacRoleBindingRoleArgs],
        user: pulumi.Input[_builtins.str],
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> pulumi.Input[_builtins.str]: ...
    @membership_id.setter
    def membership_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="membershipRbacRoleBindingId")
    def membership_rbac_role_binding_id(self) -> pulumi.Input[_builtins.str]: ...
    @membership_rbac_role_binding_id.setter
    def membership_rbac_role_binding_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[MembershipRbacRoleBindingRoleArgs]: ...
    @role.setter
    def role(self, value: pulumi.Input[MembershipRbacRoleBindingRoleArgs]): ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Input[_builtins.str]: ...
    @user.setter
    def user(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _MembershipRbacRoleBindingState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_id: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_rbac_role_binding_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[MembershipRbacRoleBindingRoleArgs]] = ...,
        states: Optional[
            pulumi.Input[Sequence[pulumi.Input[MembershipRbacRoleBindingStateArgs]]]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership_id.setter
    def membership_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="membershipRbacRoleBindingId")
    def membership_rbac_role_binding_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership_rbac_role_binding_id.setter
    def membership_rbac_role_binding_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[MembershipRbacRoleBindingRoleArgs]]: ...
    @role.setter
    def role(
        self, value: Optional[pulumi.Input[MembershipRbacRoleBindingRoleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def states(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MembershipRbacRoleBindingStateArgs]]]
    ]: ...
    @states.setter
    def states(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MembershipRbacRoleBindingStateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class MembershipRbacRoleBinding(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_id: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_rbac_role_binding_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[
            pulumi.Input[
                Union[
                    MembershipRbacRoleBindingRoleArgs,
                    MembershipRbacRoleBindingRoleArgsDict,
                ]
            ]
        ] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MembershipRbacRoleBindingArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_id: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_rbac_role_binding_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[
            pulumi.Input[
                Union[
                    MembershipRbacRoleBindingRoleArgs,
                    MembershipRbacRoleBindingRoleArgsDict,
                ]
            ]
        ] = ...,
        states: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MembershipRbacRoleBindingStateArgs,
                            MembershipRbacRoleBindingStateArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> MembershipRbacRoleBinding: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="membershipRbacRoleBindingId")
    def membership_rbac_role_binding_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[outputs.MembershipRbacRoleBindingRole]: ...
    @_builtins.property
    @pulumi.getter
    def states(
        self,
    ) -> pulumi.Output[Sequence[outputs.MembershipRbacRoleBindingState]]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Output[_builtins.str]: ...
