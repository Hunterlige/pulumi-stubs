import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecretCiphertextArgs", "SecretCiphertext"]

@pulumi.input_type
class SecretCiphertextArgs:
    def __init__(
        __self__,
        *,
        crypto_key: pulumi.Input[_builtins.str],
        plaintext: pulumi.Input[_builtins.str],
        additional_authenticated_data: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key.setter
    def crypto_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def plaintext(self) -> pulumi.Input[_builtins.str]: ...
    @plaintext.setter
    def plaintext(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalAuthenticatedData")
    def additional_authenticated_data(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_authenticated_data.setter
    def additional_authenticated_data(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _SecretCiphertextState:
    def __init__(
        __self__,
        *,
        additional_authenticated_data: Optional[pulumi.Input[_builtins.str]] = ...,
        ciphertext: Optional[pulumi.Input[_builtins.str]] = ...,
        crypto_key: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalAuthenticatedData")
    def additional_authenticated_data(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_authenticated_data.setter
    def additional_authenticated_data(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def ciphertext(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ciphertext.setter
    def ciphertext(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @crypto_key.setter
    def crypto_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def plaintext(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plaintext.setter
    def plaintext(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:kms/secretCiphertext:SecretCiphertext")
class SecretCiphertext(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_authenticated_data: Optional[pulumi.Input[_builtins.str]] = ...,
        crypto_key: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecretCiphertextArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_authenticated_data: Optional[pulumi.Input[_builtins.str]] = ...,
        ciphertext: Optional[pulumi.Input[_builtins.str]] = ...,
        crypto_key: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SecretCiphertext: ...
    @_builtins.property
    @pulumi.getter(name="additionalAuthenticatedData")
    def additional_authenticated_data(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def ciphertext(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def plaintext(self) -> pulumi.Output[_builtins.str]: ...
