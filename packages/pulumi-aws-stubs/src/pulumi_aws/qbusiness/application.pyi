import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplicationArgs", "Application"]

@pulumi.input_type
class ApplicationArgs:
    def __init__(
        __self__,
        *,
        attachments_configuration: pulumi.Input[
            ApplicationAttachmentsConfigurationArgs
        ],
        display_name: pulumi.Input[_builtins.str],
        iam_service_role_arn: pulumi.Input[_builtins.str],
        identity_center_instance_arn: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configuration: Optional[
            pulumi.Input[ApplicationEncryptionConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[ApplicationTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachmentsConfiguration")
    def attachments_configuration(
        self,
    ) -> pulumi.Input[ApplicationAttachmentsConfigurationArgs]: ...
    @attachments_configuration.setter
    def attachments_configuration(
        self, value: pulumi.Input[ApplicationAttachmentsConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="iamServiceRoleArn")
    def iam_service_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @iam_service_role_arn.setter
    def iam_service_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="identityCenterInstanceArn")
    def identity_center_instance_arn(self) -> pulumi.Input[_builtins.str]: ...
    @identity_center_instance_arn.setter
    def identity_center_instance_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationEncryptionConfigurationArgs]]: ...
    @encryption_configuration.setter
    def encryption_configuration(
        self, value: Optional[pulumi.Input[ApplicationEncryptionConfigurationArgs]]
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ApplicationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ApplicationTimeoutsArgs]]): ...

@pulumi.input_type
class _ApplicationState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        attachments_configuration: Optional[
            pulumi.Input[ApplicationAttachmentsConfigurationArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configuration: Optional[
            pulumi.Input[ApplicationEncryptionConfigurationArgs]
        ] = ...,
        iam_service_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_center_application_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_center_instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[ApplicationTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="attachmentsConfiguration")
    def attachments_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationAttachmentsConfigurationArgs]]: ...
    @attachments_configuration.setter
    def attachments_configuration(
        self, value: Optional[pulumi.Input[ApplicationAttachmentsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[ApplicationEncryptionConfigurationArgs]]: ...
    @encryption_configuration.setter
    def encryption_configuration(
        self, value: Optional[pulumi.Input[ApplicationEncryptionConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamServiceRoleArn")
    def iam_service_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_service_role_arn.setter
    def iam_service_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityCenterApplicationArn")
    def identity_center_application_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_center_application_arn.setter
    def identity_center_application_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="identityCenterInstanceArn")
    def identity_center_instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_center_instance_arn.setter
    def identity_center_instance_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
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
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ApplicationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ApplicationTimeoutsArgs]]): ...

@pulumi.type_token("aws:qbusiness/application:Application")
class Application(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        attachments_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationAttachmentsConfigurationArgs,
                    ApplicationAttachmentsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationEncryptionConfigurationArgs,
                    ApplicationEncryptionConfigurationArgsDict,
                ]
            ]
        ] = ...,
        iam_service_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_center_instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[ApplicationTimeoutsArgs, ApplicationTimeoutsArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplicationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        attachments_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationAttachmentsConfigurationArgs,
                    ApplicationAttachmentsConfigurationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configuration: Optional[
            pulumi.Input[
                Union[
                    ApplicationEncryptionConfigurationArgs,
                    ApplicationEncryptionConfigurationArgsDict,
                ]
            ]
        ] = ...,
        iam_service_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_center_application_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_center_instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[ApplicationTimeoutsArgs, ApplicationTimeoutsArgsDict]]
        ] = ...,
    ) -> Application: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="attachmentsConfiguration")
    def attachments_configuration(
        self,
    ) -> pulumi.Output[outputs.ApplicationAttachmentsConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.ApplicationEncryptionConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="iamServiceRoleArn")
    def iam_service_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="identityCenterApplicationArn")
    def identity_center_application_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="identityCenterInstanceArn")
    def identity_center_instance_arn(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ApplicationTimeouts]]: ...
