import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UserArgs", "User"]

@pulumi.input_type
class UserArgs:
    def __init__(
        __self__,
        *,
        instance_id: pulumi.Input[_builtins.str],
        phone_config: pulumi.Input[UserPhoneConfigArgs],
        routing_profile_id: pulumi.Input[_builtins.str],
        security_profile_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        directory_user_id: Optional[pulumi.Input[_builtins.str]] = ...,
        hierarchy_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_info: Optional[pulumi.Input[UserIdentityInfoArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[_builtins.str]: ...
    @instance_id.setter
    def instance_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="phoneConfig")
    def phone_config(self) -> pulumi.Input[UserPhoneConfigArgs]: ...
    @phone_config.setter
    def phone_config(self, value: pulumi.Input[UserPhoneConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="routingProfileId")
    def routing_profile_id(self) -> pulumi.Input[_builtins.str]: ...
    @routing_profile_id.setter
    def routing_profile_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="securityProfileIds")
    def security_profile_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_profile_ids.setter
    def security_profile_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="directoryUserId")
    def directory_user_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_user_id.setter
    def directory_user_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hierarchyGroupId")
    def hierarchy_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hierarchy_group_id.setter
    def hierarchy_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityInfo")
    def identity_info(self) -> Optional[pulumi.Input[UserIdentityInfoArgs]]: ...
    @identity_info.setter
    def identity_info(self, value: Optional[pulumi.Input[UserIdentityInfoArgs]]): ...
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _UserState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_user_id: Optional[pulumi.Input[_builtins.str]] = ...,
        hierarchy_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_info: Optional[pulumi.Input[UserIdentityInfoArgs]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_config: Optional[pulumi.Input[UserPhoneConfigArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_profile_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        user_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="directoryUserId")
    def directory_user_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_user_id.setter
    def directory_user_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hierarchyGroupId")
    def hierarchy_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hierarchy_group_id.setter
    def hierarchy_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityInfo")
    def identity_info(self) -> Optional[pulumi.Input[UserIdentityInfoArgs]]: ...
    @identity_info.setter
    def identity_info(self, value: Optional[pulumi.Input[UserIdentityInfoArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="phoneConfig")
    def phone_config(self) -> Optional[pulumi.Input[UserPhoneConfigArgs]]: ...
    @phone_config.setter
    def phone_config(self, value: Optional[pulumi.Input[UserPhoneConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingProfileId")
    def routing_profile_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_profile_id.setter
    def routing_profile_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityProfileIds")
    def security_profile_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_profile_ids.setter
    def security_profile_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:connect/user:User")
class User(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        directory_user_id: Optional[pulumi.Input[_builtins.str]] = ...,
        hierarchy_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_info: Optional[
            pulumi.Input[Union[UserIdentityInfoArgs, UserIdentityInfoArgsDict]]
        ] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_config: Optional[
            pulumi.Input[Union[UserPhoneConfigArgs, UserPhoneConfigArgsDict]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_profile_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
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
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_user_id: Optional[pulumi.Input[_builtins.str]] = ...,
        hierarchy_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_info: Optional[
            pulumi.Input[Union[UserIdentityInfoArgs, UserIdentityInfoArgsDict]]
        ] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_config: Optional[
            pulumi.Input[Union[UserPhoneConfigArgs, UserPhoneConfigArgsDict]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_profile_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        user_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> User: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="directoryUserId")
    def directory_user_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hierarchyGroupId")
    def hierarchy_group_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="identityInfo")
    def identity_info(self) -> pulumi.Output[Optional[outputs.UserIdentityInfo]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="phoneConfig")
    def phone_config(self) -> pulumi.Output[outputs.UserPhoneConfig]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingProfileId")
    def routing_profile_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityProfileIds")
    def security_profile_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[_builtins.str]: ...
