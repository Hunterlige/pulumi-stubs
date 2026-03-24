import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
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
        domain_identifier: pulumi.Input[_builtins.str],
        user_identifier: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[UserProfileTimeoutsArgs]] = ...,
        user_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @domain_identifier.setter
    def domain_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userIdentifier")
    def user_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @user_identifier.setter
    def user_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[UserProfileTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[UserProfileTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_type.setter
    def user_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _UserProfileState:
    def __init__(
        __self__,
        *,
        details: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserProfileDetailArgs]]]
        ] = ...,
        domain_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[UserProfileTimeoutsArgs]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        user_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        user_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileDetailArgs]]]]: ...
    @details.setter
    def details(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[UserProfileDetailArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_identifier.setter
    def domain_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[UserProfileTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[UserProfileTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userIdentifier")
    def user_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_identifier.setter
    def user_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_type.setter
    def user_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:datazone/userProfile:UserProfile")
class UserProfile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[UserProfileTimeoutsArgs, UserProfileTimeoutsArgsDict]]
        ] = ...,
        user_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        user_type: Optional[pulumi.Input[_builtins.str]] = ...,
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
        details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[UserProfileDetailArgs, UserProfileDetailArgsDict]
                    ]
                ]
            ]
        ] = ...,
        domain_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[UserProfileTimeoutsArgs, UserProfileTimeoutsArgsDict]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        user_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        user_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> UserProfile: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> pulumi.Output[Sequence[outputs.UserProfileDetail]]: ...
    @_builtins.property
    @pulumi.getter(name="domainIdentifier")
    def domain_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.UserProfileTimeouts]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userIdentifier")
    def user_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userType")
    def user_type(self) -> pulumi.Output[_builtins.str]: ...
