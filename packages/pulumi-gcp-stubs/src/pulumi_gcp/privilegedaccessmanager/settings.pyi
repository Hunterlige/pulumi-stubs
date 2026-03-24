import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SettingsArgs", "Settings"]

@pulumi.input_type
class SettingsArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        parent: pulumi.Input[_builtins.str],
        email_notification_settings: Optional[
            pulumi.Input[SettingsEmailNotificationSettingsArgs]
        ] = ...,
        service_account_approver_settings: Optional[
            pulumi.Input[SettingsServiceAccountApproverSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]: ...
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="emailNotificationSettings")
    def email_notification_settings(
        self,
    ) -> Optional[pulumi.Input[SettingsEmailNotificationSettingsArgs]]: ...
    @email_notification_settings.setter
    def email_notification_settings(
        self, value: Optional[pulumi.Input[SettingsEmailNotificationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountApproverSettings")
    def service_account_approver_settings(
        self,
    ) -> Optional[pulumi.Input[SettingsServiceAccountApproverSettingsArgs]]: ...
    @service_account_approver_settings.setter
    def service_account_approver_settings(
        self, value: Optional[pulumi.Input[SettingsServiceAccountApproverSettingsArgs]]
    ): ...

@pulumi.input_type
class _SettingsState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        email_notification_settings: Optional[
            pulumi.Input[SettingsEmailNotificationSettingsArgs]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_approver_settings: Optional[
            pulumi.Input[SettingsServiceAccountApproverSettingsArgs]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="emailNotificationSettings")
    def email_notification_settings(
        self,
    ) -> Optional[pulumi.Input[SettingsEmailNotificationSettingsArgs]]: ...
    @email_notification_settings.setter
    def email_notification_settings(
        self, value: Optional[pulumi.Input[SettingsEmailNotificationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountApproverSettings")
    def service_account_approver_settings(
        self,
    ) -> Optional[pulumi.Input[SettingsServiceAccountApproverSettingsArgs]]: ...
    @service_account_approver_settings.setter
    def service_account_approver_settings(
        self, value: Optional[pulumi.Input[SettingsServiceAccountApproverSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:privilegedaccessmanager/settings:Settings")
class Settings(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        email_notification_settings: Optional[
            pulumi.Input[
                Union[
                    SettingsEmailNotificationSettingsArgs,
                    SettingsEmailNotificationSettingsArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_approver_settings: Optional[
            pulumi.Input[
                Union[
                    SettingsServiceAccountApproverSettingsArgs,
                    SettingsServiceAccountApproverSettingsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SettingsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        email_notification_settings: Optional[
            pulumi.Input[
                Union[
                    SettingsEmailNotificationSettingsArgs,
                    SettingsEmailNotificationSettingsArgsDict,
                ]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_approver_settings: Optional[
            pulumi.Input[
                Union[
                    SettingsServiceAccountApproverSettingsArgs,
                    SettingsServiceAccountApproverSettingsArgsDict,
                ]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Settings: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emailNotificationSettings")
    def email_notification_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.SettingsEmailNotificationSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountApproverSettings")
    def service_account_approver_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.SettingsServiceAccountApproverSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
