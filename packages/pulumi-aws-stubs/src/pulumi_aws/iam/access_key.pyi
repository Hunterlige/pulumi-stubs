import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccessKeyArgs", "AccessKey"]

@pulumi.input_type
class AccessKeyArgs:
    def __init__(
        __self__,
        *,
        user: pulumi.Input[_builtins.str],
        pgp_key: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Input[_builtins.str]: ...
    @user.setter
    def user(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pgp_key.setter
    def pgp_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AccessKeyState:
    def __init__(
        __self__,
        *,
        create_date: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted_ses_smtp_password_v4: Optional[pulumi.Input[_builtins.str]] = ...,
        key_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        pgp_key: Optional[pulumi.Input[_builtins.str]] = ...,
        secret: Optional[pulumi.Input[_builtins.str]] = ...,
        ses_smtp_password_v4: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createDate")
    def create_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_date.setter
    def create_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptedSecret")
    def encrypted_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encrypted_secret.setter
    def encrypted_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptedSesSmtpPasswordV4")
    def encrypted_ses_smtp_password_v4(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encrypted_ses_smtp_password_v4.setter
    def encrypted_ses_smtp_password_v4(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyFingerprint")
    def key_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_fingerprint.setter
    def key_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pgp_key.setter
    def pgp_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret.setter
    def secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sesSmtpPasswordV4")
    def ses_smtp_password_v4(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ses_smtp_password_v4.setter
    def ses_smtp_password_v4(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:iam/accessKey:AccessKey")
class AccessKey(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        pgp_key: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccessKeyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_date: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted_ses_smtp_password_v4: Optional[pulumi.Input[_builtins.str]] = ...,
        key_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        pgp_key: Optional[pulumi.Input[_builtins.str]] = ...,
        secret: Optional[pulumi.Input[_builtins.str]] = ...,
        ses_smtp_password_v4: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        user: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AccessKey: ...
    @_builtins.property
    @pulumi.getter(name="createDate")
    def create_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptedSecret")
    def encrypted_secret(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptedSesSmtpPasswordV4")
    def encrypted_ses_smtp_password_v4(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyFingerprint")
    def key_fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sesSmtpPasswordV4")
    def ses_smtp_password_v4(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Output[_builtins.str]: ...
