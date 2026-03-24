import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CiphertextArgs", "Ciphertext"]

@pulumi.input_type
class CiphertextArgs:
    def __init__(
        __self__,
        *,
        key_id: pulumi.Input[_builtins.str],
        context: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        plaintext: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[_builtins.str]: ...
    @key_id.setter
    def key_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def context(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @context.setter
    def context(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def plaintext(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plaintext.setter
    def plaintext(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="plaintextWo")
    def plaintext_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plaintext_wo.setter
    def plaintext_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="plaintextWoVersion")
    def plaintext_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plaintext_wo_version.setter
    def plaintext_wo_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _CiphertextState:
    def __init__(
        __self__,
        *,
        ciphertext_blob: Optional[pulumi.Input[_builtins.str]] = ...,
        context: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ciphertextBlob")
    def ciphertext_blob(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ciphertext_blob.setter
    def ciphertext_blob(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def context(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @context.setter
    def context(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def plaintext(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plaintext.setter
    def plaintext(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="plaintextWo")
    def plaintext_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plaintext_wo.setter
    def plaintext_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="plaintextWoVersion")
    def plaintext_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plaintext_wo_version.setter
    def plaintext_wo_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:kms/ciphertext:Ciphertext")
class Ciphertext(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        context: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CiphertextArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        ciphertext_blob: Optional[pulumi.Input[_builtins.str]] = ...,
        context: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        plaintext_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Ciphertext: ...
    @_builtins.property
    @pulumi.getter(name="ciphertextBlob")
    def ciphertext_blob(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def plaintext(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="plaintextWo")
    def plaintext_wo(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="plaintextWoVersion")
    def plaintext_wo_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
