import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UserArgs", "User"]

@pulumi.input_type
class UserArgs:
    def __init__(
        __self__,
        *,
        email: pulumi.Input[_builtins.str],
        first_name: pulumi.Input[_builtins.str],
        last_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
        app_type: Optional[pulumi.Input[Union[_builtins.str, AppType]]] = ...,
        confirmation: Optional[pulumi.Input[Union[_builtins.str, Confirmation]]] = ...,
        identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserIdentityContractArgs]]]
        ] = ...,
        note: Optional[pulumi.Input[_builtins.str]] = ...,
        notify: Optional[pulumi.Input[_builtins.bool]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, UserState]]] = ...,
        user_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]: ...
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Input[_builtins.str]: ...
    @first_name.setter
    def first_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Input[_builtins.str]: ...
    @last_name.setter
    def last_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appType")
    def app_type(self) -> Optional[pulumi.Input[Union[_builtins.str, AppType]]]: ...
    @app_type.setter
    def app_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AppType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def confirmation(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, Confirmation]]]: ...
    @confirmation.setter
    def confirmation(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Confirmation]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserIdentityContractArgs]]]]: ...
    @identities.setter
    def identities(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[UserIdentityContractArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def note(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @note.setter
    def note(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def notify(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @notify.setter
    def notify(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, UserState]]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, UserState]]]): ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:apimanagement:User")
class User(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_type: Optional[pulumi.Input[Union[_builtins.str, AppType]]] = ...,
        confirmation: Optional[pulumi.Input[Union[_builtins.str, Confirmation]]] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        first_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[UserIdentityContractArgs, UserIdentityContractArgsDict]
                    ]
                ]
            ]
        ] = ...,
        last_name: Optional[pulumi.Input[_builtins.str]] = ...,
        note: Optional[pulumi.Input[_builtins.str]] = ...,
        notify: Optional[pulumi.Input[_builtins.bool]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, UserState]]] = ...,
        user_id: Optional[pulumi.Input[_builtins.str]] = ...,
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
    ) -> User: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def groups(
        self,
    ) -> pulumi.Output[Sequence[outputs.GroupContractPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.UserIdentityContractResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def note(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="registrationDate")
    def registration_date(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
