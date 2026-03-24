import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["UserSettingsArgs", "UserSettings"]

@pulumi.input_type
class UserSettingsArgs:
    def __init__(
        __self__,
        *,
        copy_allowed: pulumi.Input[_builtins.str],
        download_allowed: pulumi.Input[_builtins.str],
        paste_allowed: pulumi.Input[_builtins.str],
        print_allowed: pulumi.Input[_builtins.str],
        upload_allowed: pulumi.Input[_builtins.str],
        additional_encryption_context: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        cookie_synchronization_configuration: Optional[
            pulumi.Input[UserSettingsCookieSynchronizationConfigurationArgs]
        ] = ...,
        customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ...,
        deep_link_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        disconnect_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        idle_disconnect_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        toolbar_configuration: Optional[
            pulumi.Input[UserSettingsToolbarConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="copyAllowed")
    def copy_allowed(self) -> pulumi.Input[_builtins.str]: ...
    @copy_allowed.setter
    def copy_allowed(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="downloadAllowed")
    def download_allowed(self) -> pulumi.Input[_builtins.str]: ...
    @download_allowed.setter
    def download_allowed(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="pasteAllowed")
    def paste_allowed(self) -> pulumi.Input[_builtins.str]: ...
    @paste_allowed.setter
    def paste_allowed(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="printAllowed")
    def print_allowed(self) -> pulumi.Input[_builtins.str]: ...
    @print_allowed.setter
    def print_allowed(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="uploadAllowed")
    def upload_allowed(self) -> pulumi.Input[_builtins.str]: ...
    @upload_allowed.setter
    def upload_allowed(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalEncryptionContext")
    def additional_encryption_context(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @additional_encryption_context.setter
    def additional_encryption_context(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cookieSynchronizationConfiguration")
    def cookie_synchronization_configuration(
        self,
    ) -> Optional[pulumi.Input[UserSettingsCookieSynchronizationConfigurationArgs]]: ...
    @cookie_synchronization_configuration.setter
    def cookie_synchronization_configuration(
        self,
        value: Optional[
            pulumi.Input[UserSettingsCookieSynchronizationConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_managed_key.setter
    def customer_managed_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deepLinkAllowed")
    def deep_link_allowed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deep_link_allowed.setter
    def deep_link_allowed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disconnectTimeoutInMinutes")
    def disconnect_timeout_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disconnect_timeout_in_minutes.setter
    def disconnect_timeout_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="idleDisconnectTimeoutInMinutes")
    def idle_disconnect_timeout_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_disconnect_timeout_in_minutes.setter
    def idle_disconnect_timeout_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
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
    @_builtins.property
    @pulumi.getter(name="toolbarConfiguration")
    def toolbar_configuration(
        self,
    ) -> Optional[pulumi.Input[UserSettingsToolbarConfigurationArgs]]: ...
    @toolbar_configuration.setter
    def toolbar_configuration(
        self, value: Optional[pulumi.Input[UserSettingsToolbarConfigurationArgs]]
    ): ...

@pulumi.input_type
class _UserSettingsState:
    def __init__(
        __self__,
        *,
        additional_encryption_context: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        associated_portal_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cookie_synchronization_configuration: Optional[
            pulumi.Input[UserSettingsCookieSynchronizationConfigurationArgs]
        ] = ...,
        copy_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ...,
        deep_link_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        disconnect_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        download_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_disconnect_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        paste_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        print_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        toolbar_configuration: Optional[
            pulumi.Input[UserSettingsToolbarConfigurationArgs]
        ] = ...,
        upload_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        user_settings_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalEncryptionContext")
    def additional_encryption_context(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @additional_encryption_context.setter
    def additional_encryption_context(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="associatedPortalArns")
    def associated_portal_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @associated_portal_arns.setter
    def associated_portal_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cookieSynchronizationConfiguration")
    def cookie_synchronization_configuration(
        self,
    ) -> Optional[pulumi.Input[UserSettingsCookieSynchronizationConfigurationArgs]]: ...
    @cookie_synchronization_configuration.setter
    def cookie_synchronization_configuration(
        self,
        value: Optional[
            pulumi.Input[UserSettingsCookieSynchronizationConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="copyAllowed")
    def copy_allowed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @copy_allowed.setter
    def copy_allowed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_managed_key.setter
    def customer_managed_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deepLinkAllowed")
    def deep_link_allowed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deep_link_allowed.setter
    def deep_link_allowed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disconnectTimeoutInMinutes")
    def disconnect_timeout_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disconnect_timeout_in_minutes.setter
    def disconnect_timeout_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="downloadAllowed")
    def download_allowed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @download_allowed.setter
    def download_allowed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="idleDisconnectTimeoutInMinutes")
    def idle_disconnect_timeout_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @idle_disconnect_timeout_in_minutes.setter
    def idle_disconnect_timeout_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pasteAllowed")
    def paste_allowed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @paste_allowed.setter
    def paste_allowed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="printAllowed")
    def print_allowed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @print_allowed.setter
    def print_allowed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="toolbarConfiguration")
    def toolbar_configuration(
        self,
    ) -> Optional[pulumi.Input[UserSettingsToolbarConfigurationArgs]]: ...
    @toolbar_configuration.setter
    def toolbar_configuration(
        self, value: Optional[pulumi.Input[UserSettingsToolbarConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="uploadAllowed")
    def upload_allowed(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @upload_allowed.setter
    def upload_allowed(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userSettingsArn")
    def user_settings_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_settings_arn.setter
    def user_settings_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:workspacesweb/userSettings:UserSettings")
class UserSettings(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_encryption_context: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        cookie_synchronization_configuration: Optional[
            pulumi.Input[
                Union[
                    UserSettingsCookieSynchronizationConfigurationArgs,
                    UserSettingsCookieSynchronizationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        copy_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ...,
        deep_link_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        disconnect_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        download_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_disconnect_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        paste_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        print_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        toolbar_configuration: Optional[
            pulumi.Input[
                Union[
                    UserSettingsToolbarConfigurationArgs,
                    UserSettingsToolbarConfigurationArgsDict,
                ]
            ]
        ] = ...,
        upload_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: UserSettingsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_encryption_context: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        associated_portal_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cookie_synchronization_configuration: Optional[
            pulumi.Input[
                Union[
                    UserSettingsCookieSynchronizationConfigurationArgs,
                    UserSettingsCookieSynchronizationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        copy_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ...,
        deep_link_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        disconnect_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        download_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        idle_disconnect_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        paste_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        print_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        toolbar_configuration: Optional[
            pulumi.Input[
                Union[
                    UserSettingsToolbarConfigurationArgs,
                    UserSettingsToolbarConfigurationArgsDict,
                ]
            ]
        ] = ...,
        upload_allowed: Optional[pulumi.Input[_builtins.str]] = ...,
        user_settings_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> UserSettings: ...
    @_builtins.property
    @pulumi.getter(name="additionalEncryptionContext")
    def additional_encryption_context(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="associatedPortalArns")
    def associated_portal_arns(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cookieSynchronizationConfiguration")
    def cookie_synchronization_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.UserSettingsCookieSynchronizationConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="copyAllowed")
    def copy_allowed(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deepLinkAllowed")
    def deep_link_allowed(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disconnectTimeoutInMinutes")
    def disconnect_timeout_in_minutes(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="downloadAllowed")
    def download_allowed(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="idleDisconnectTimeoutInMinutes")
    def idle_disconnect_timeout_in_minutes(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="pasteAllowed")
    def paste_allowed(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="printAllowed")
    def print_allowed(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="toolbarConfiguration")
    def toolbar_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.UserSettingsToolbarConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="uploadAllowed")
    def upload_allowed(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userSettingsArn")
    def user_settings_arn(self) -> pulumi.Output[_builtins.str]: ...
