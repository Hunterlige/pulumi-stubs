import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UserProfileArgs", "UserProfile"]

@pulumi.input_type
class UserProfileArgs:
    def __init__(
        __self__,
        *,
        domain_id: pulumi.Input[_builtins.str],
        user_profile_name: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        single_sign_on_user_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        single_sign_on_user_value: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_settings: Optional[pulumi.Input[UserProfileUserSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Input[_builtins.str]: ...
    @domain_id.setter
    def domain_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userProfileName")
    def user_profile_name(self) -> pulumi.Input[_builtins.str]: ...
    @user_profile_name.setter
    def user_profile_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="singleSignOnUserIdentifier")
    def single_sign_on_user_identifier(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @single_sign_on_user_identifier.setter
    def single_sign_on_user_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="singleSignOnUserValue")
    def single_sign_on_user_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @single_sign_on_user_value.setter
    def single_sign_on_user_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    @pulumi.getter(name="userSettings")
    def user_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsArgs]]: ...
    @user_settings.setter
    def user_settings(
        self, value: Optional[pulumi.Input[UserProfileUserSettingsArgs]]
    ): ...

@pulumi.input_type
class _UserProfileState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        home_efs_file_system_uid: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        single_sign_on_user_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        single_sign_on_user_value: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        user_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        user_settings: Optional[pulumi.Input[UserProfileUserSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_id.setter
    def domain_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="homeEfsFileSystemUid")
    def home_efs_file_system_uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @home_efs_file_system_uid.setter
    def home_efs_file_system_uid(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="singleSignOnUserIdentifier")
    def single_sign_on_user_identifier(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @single_sign_on_user_identifier.setter
    def single_sign_on_user_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="singleSignOnUserValue")
    def single_sign_on_user_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @single_sign_on_user_value.setter
    def single_sign_on_user_value(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    @pulumi.getter(name="userProfileName")
    def user_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_profile_name.setter
    def user_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userSettings")
    def user_settings(self) -> Optional[pulumi.Input[UserProfileUserSettingsArgs]]: ...
    @user_settings.setter
    def user_settings(
        self, value: Optional[pulumi.Input[UserProfileUserSettingsArgs]]
    ): ...

@pulumi.type_token("aws:sagemaker/userProfile:UserProfile")
class UserProfile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        single_sign_on_user_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        single_sign_on_user_value: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        user_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        user_settings: Optional[
            pulumi.Input[
                Union[UserProfileUserSettingsArgs, UserProfileUserSettingsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UserProfileArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_id: Optional[pulumi.Input[_builtins.str]] = ...,
        home_efs_file_system_uid: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        single_sign_on_user_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        single_sign_on_user_value: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        user_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        user_settings: Optional[
            pulumi.Input[
                Union[UserProfileUserSettingsArgs, UserProfileUserSettingsArgsDict]
            ]
        ] = ...,
    ) -> UserProfile: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="homeEfsFileSystemUid")
    def home_efs_file_system_uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="singleSignOnUserIdentifier")
    def single_sign_on_user_identifier(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="singleSignOnUserValue")
    def single_sign_on_user_value(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="userProfileName")
    def user_profile_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userSettings")
    def user_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.UserProfileUserSettings]]: ...
