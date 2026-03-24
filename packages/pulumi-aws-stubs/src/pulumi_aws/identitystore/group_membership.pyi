import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GroupMembershipArgs", "GroupMembership"]

@pulumi.input_type
class GroupMembershipArgs:
    def __init__(
        __self__,
        *,
        group_id: pulumi.Input[_builtins.str],
        identity_store_id: pulumi.Input[_builtins.str],
        member_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[_builtins.str]: ...
    @group_id.setter
    def group_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> pulumi.Input[_builtins.str]: ...
    @identity_store_id.setter
    def identity_store_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Input[_builtins.str]: ...
    @member_id.setter
    def member_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _GroupMembershipState:
    def __init__(
        __self__,
        *,
        group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        member_id: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_store_id.setter
    def identity_store_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memberId")
    def member_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @member_id.setter
    def member_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership_id.setter
    def membership_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:identitystore/groupMembership:GroupMembership")
class GroupMembership(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        member_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
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
        group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_store_id: Optional[pulumi.Input[_builtins.str]] = ...,
        member_id: Optional[pulumi.Input[_builtins.str]] = ...,
        membership_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> GroupMembership: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="identityStoreId")
    def identity_store_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memberId")
    def member_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="membershipId")
    def membership_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
