import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AuthConfigArgs", "AuthConfig"]

@pulumi.input_type
class AuthConfigArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        client_certificate: Optional[
            pulumi.Input[AuthConfigClientCertificateArgs]
        ] = ...,
        decrypted_credential: Optional[
            pulumi.Input[AuthConfigDecryptedCredentialArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_notification_durations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        override_valid_time: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(
        self,
    ) -> Optional[pulumi.Input[AuthConfigClientCertificateArgs]]: ...
    @client_certificate.setter
    def client_certificate(
        self, value: Optional[pulumi.Input[AuthConfigClientCertificateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="decryptedCredential")
    def decrypted_credential(
        self,
    ) -> Optional[pulumi.Input[AuthConfigDecryptedCredentialArgs]]: ...
    @decrypted_credential.setter
    def decrypted_credential(
        self, value: Optional[pulumi.Input[AuthConfigDecryptedCredentialArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryNotificationDurations")
    def expiry_notification_durations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @expiry_notification_durations.setter
    def expiry_notification_durations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="overrideValidTime")
    def override_valid_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @override_valid_time.setter
    def override_valid_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AuthConfigState:
    def __init__(
        __self__,
        *,
        certificate_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_certificate: Optional[
            pulumi.Input[AuthConfigClientCertificateArgs]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        creator_email: Optional[pulumi.Input[_builtins.str]] = ...,
        credential_type: Optional[pulumi.Input[_builtins.str]] = ...,
        decrypted_credential: Optional[
            pulumi.Input[AuthConfigDecryptedCredentialArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted_credential: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_notification_durations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        last_modifier_email: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        override_valid_time: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        valid_time: Optional[pulumi.Input[_builtins.str]] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(
        self,
    ) -> Optional[pulumi.Input[AuthConfigClientCertificateArgs]]: ...
    @client_certificate.setter
    def client_certificate(
        self, value: Optional[pulumi.Input[AuthConfigClientCertificateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="creatorEmail")
    def creator_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creator_email.setter
    def creator_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="credentialType")
    def credential_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credential_type.setter
    def credential_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="decryptedCredential")
    def decrypted_credential(
        self,
    ) -> Optional[pulumi.Input[AuthConfigDecryptedCredentialArgs]]: ...
    @decrypted_credential.setter
    def decrypted_credential(
        self, value: Optional[pulumi.Input[AuthConfigDecryptedCredentialArgs]]
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
    @pulumi.getter(name="encryptedCredential")
    def encrypted_credential(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encrypted_credential.setter
    def encrypted_credential(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expiryNotificationDurations")
    def expiry_notification_durations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @expiry_notification_durations.setter
    def expiry_notification_durations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastModifierEmail")
    def last_modifier_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modifier_email.setter
    def last_modifier_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="overrideValidTime")
    def override_valid_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @override_valid_time.setter
    def override_valid_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="validTime")
    def valid_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @valid_time.setter
    def valid_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:applicationintegration/authConfig:AuthConfig")
class AuthConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        client_certificate: Optional[
            pulumi.Input[
                Union[
                    AuthConfigClientCertificateArgs, AuthConfigClientCertificateArgsDict
                ]
            ]
        ] = ...,
        decrypted_credential: Optional[
            pulumi.Input[
                Union[
                    AuthConfigDecryptedCredentialArgs,
                    AuthConfigDecryptedCredentialArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_notification_durations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        override_valid_time: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AuthConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        certificate_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_certificate: Optional[
            pulumi.Input[
                Union[
                    AuthConfigClientCertificateArgs, AuthConfigClientCertificateArgsDict
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        creator_email: Optional[pulumi.Input[_builtins.str]] = ...,
        credential_type: Optional[pulumi.Input[_builtins.str]] = ...,
        decrypted_credential: Optional[
            pulumi.Input[
                Union[
                    AuthConfigDecryptedCredentialArgs,
                    AuthConfigDecryptedCredentialArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted_credential: Optional[pulumi.Input[_builtins.str]] = ...,
        expiry_notification_durations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        last_modifier_email: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        override_valid_time: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        valid_time: Optional[pulumi.Input[_builtins.str]] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AuthConfig: ...
    @_builtins.property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(
        self,
    ) -> pulumi.Output[Optional[outputs.AuthConfigClientCertificate]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creatorEmail")
    def creator_email(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="credentialType")
    def credential_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="decryptedCredential")
    def decrypted_credential(
        self,
    ) -> pulumi.Output[Optional[outputs.AuthConfigDecryptedCredential]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptedCredential")
    def encrypted_credential(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expiryNotificationDurations")
    def expiry_notification_durations(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifierEmail")
    def last_modifier_email(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="overrideValidTime")
    def override_valid_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validTime")
    def valid_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> pulumi.Output[Optional[_builtins.str]]: ...
