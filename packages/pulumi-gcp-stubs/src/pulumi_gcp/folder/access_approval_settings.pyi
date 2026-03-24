import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccessApprovalSettingsArgs", "AccessApprovalSettings"]

@pulumi.input_type
class AccessApprovalSettingsArgs:
    def __init__(
        __self__,
        *,
        enrolled_services: pulumi.Input[
            Sequence[pulumi.Input[AccessApprovalSettingsEnrolledServiceArgs]]
        ],
        folder_id: pulumi.Input[_builtins.str],
        active_key_version: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_emails: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enrolledServices")
    def enrolled_services(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[AccessApprovalSettingsEnrolledServiceArgs]]
    ]: ...
    @enrolled_services.setter
    def enrolled_services(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[AccessApprovalSettingsEnrolledServiceArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> pulumi.Input[_builtins.str]: ...
    @folder_id.setter
    def folder_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="activeKeyVersion")
    def active_key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @active_key_version.setter
    def active_key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationEmails")
    def notification_emails(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @notification_emails.setter
    def notification_emails(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _AccessApprovalSettingsState:
    def __init__(
        __self__,
        *,
        active_key_version: Optional[pulumi.Input[_builtins.str]] = ...,
        ancestor_has_active_key_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        enrolled_ancestor: Optional[pulumi.Input[_builtins.bool]] = ...,
        enrolled_services: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AccessApprovalSettingsEnrolledServiceArgs]]
            ]
        ] = ...,
        folder_id: Optional[pulumi.Input[_builtins.str]] = ...,
        invalid_key_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_emails: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeKeyVersion")
    def active_key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @active_key_version.setter
    def active_key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ancestorHasActiveKeyVersion")
    def ancestor_has_active_key_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ancestor_has_active_key_version.setter
    def ancestor_has_active_key_version(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enrolledAncestor")
    def enrolled_ancestor(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enrolled_ancestor.setter
    def enrolled_ancestor(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enrolledServices")
    def enrolled_services(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AccessApprovalSettingsEnrolledServiceArgs]]]
    ]: ...
    @enrolled_services.setter
    def enrolled_services(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AccessApprovalSettingsEnrolledServiceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @folder_id.setter
    def folder_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invalidKeyVersion")
    def invalid_key_version(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invalid_key_version.setter
    def invalid_key_version(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationEmails")
    def notification_emails(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @notification_emails.setter
    def notification_emails(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class AccessApprovalSettings(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        active_key_version: Optional[pulumi.Input[_builtins.str]] = ...,
        enrolled_services: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AccessApprovalSettingsEnrolledServiceArgs,
                            AccessApprovalSettingsEnrolledServiceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        folder_id: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_emails: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccessApprovalSettingsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        active_key_version: Optional[pulumi.Input[_builtins.str]] = ...,
        ancestor_has_active_key_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        enrolled_ancestor: Optional[pulumi.Input[_builtins.bool]] = ...,
        enrolled_services: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AccessApprovalSettingsEnrolledServiceArgs,
                            AccessApprovalSettingsEnrolledServiceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        folder_id: Optional[pulumi.Input[_builtins.str]] = ...,
        invalid_key_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_emails: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> AccessApprovalSettings: ...
    @_builtins.property
    @pulumi.getter(name="activeKeyVersion")
    def active_key_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ancestorHasActiveKeyVersion")
    def ancestor_has_active_key_version(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enrolledAncestor")
    def enrolled_ancestor(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enrolledServices")
    def enrolled_services(
        self,
    ) -> pulumi.Output[Sequence[outputs.AccessApprovalSettingsEnrolledService]]: ...
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="invalidKeyVersion")
    def invalid_key_version(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationEmails")
    def notification_emails(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
