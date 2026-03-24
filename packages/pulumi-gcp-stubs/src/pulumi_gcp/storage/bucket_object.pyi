import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BucketObjectArgs", "BucketObject"]

@pulumi.input_type
class BucketObjectArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        cache_control: Optional[pulumi.Input[_builtins.str]] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        content_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
        content_encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        content_language: Optional[pulumi.Input[_builtins.str]] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        contexts: Optional[pulumi.Input[BucketObjectContextsArgs]] = ...,
        customer_encryption: Optional[
            pulumi.Input[BucketObjectCustomerEncryptionArgs]
        ] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        detect_md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        event_based_hold: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_empty_content_type: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        retention: Optional[pulumi.Input[BucketObjectRetentionArgs]] = ...,
        source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = ...,
        source_md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        temporary_hold: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cache_control.setter
    def cache_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_disposition.setter
    def content_disposition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_encoding.setter
    def content_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_language.setter
    def content_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def contexts(self) -> Optional[pulumi.Input[BucketObjectContextsArgs]]: ...
    @contexts.setter
    def contexts(self, value: Optional[pulumi.Input[BucketObjectContextsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="customerEncryption")
    def customer_encryption(
        self,
    ) -> Optional[pulumi.Input[BucketObjectCustomerEncryptionArgs]]: ...
    @customer_encryption.setter
    def customer_encryption(
        self, value: Optional[pulumi.Input[BucketObjectCustomerEncryptionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="detectMd5hash")
    def detect_md5hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @detect_md5hash.setter
    def detect_md5hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventBasedHold")
    def event_based_hold(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @event_based_hold.setter
    def event_based_hold(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="forceEmptyContentType")
    def force_empty_content_type(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_empty_content_type.setter
    def force_empty_content_type(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def retention(self) -> Optional[pulumi.Input[BucketObjectRetentionArgs]]: ...
    @retention.setter
    def retention(self, value: Optional[pulumi.Input[BucketObjectRetentionArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]: ...
    @source.setter
    def source(
        self, value: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceMd5hash")
    def source_md5hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_md5hash.setter
    def source_md5hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="temporaryHold")
    def temporary_hold(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @temporary_hold.setter
    def temporary_hold(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _BucketObjectState:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_control: Optional[pulumi.Input[_builtins.str]] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        content_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
        content_encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        content_language: Optional[pulumi.Input[_builtins.str]] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        contexts: Optional[pulumi.Input[BucketObjectContextsArgs]] = ...,
        crc32c: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_encryption: Optional[
            pulumi.Input[BucketObjectCustomerEncryptionArgs]
        ] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        detect_md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        event_based_hold: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_empty_content_type: Optional[pulumi.Input[_builtins.bool]] = ...,
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        md5hexhash: Optional[pulumi.Input[_builtins.str]] = ...,
        media_link: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_name: Optional[pulumi.Input[_builtins.str]] = ...,
        retention: Optional[pulumi.Input[BucketObjectRetentionArgs]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = ...,
        source_md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        temporary_hold: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cache_control.setter
    def cache_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_disposition.setter
    def content_disposition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_encoding.setter
    def content_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_language.setter
    def content_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def contexts(self) -> Optional[pulumi.Input[BucketObjectContextsArgs]]: ...
    @contexts.setter
    def contexts(self, value: Optional[pulumi.Input[BucketObjectContextsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def crc32c(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @crc32c.setter
    def crc32c(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerEncryption")
    def customer_encryption(
        self,
    ) -> Optional[pulumi.Input[BucketObjectCustomerEncryptionArgs]]: ...
    @customer_encryption.setter
    def customer_encryption(
        self, value: Optional[pulumi.Input[BucketObjectCustomerEncryptionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="detectMd5hash")
    def detect_md5hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @detect_md5hash.setter
    def detect_md5hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventBasedHold")
    def event_based_hold(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @event_based_hold.setter
    def event_based_hold(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="forceEmptyContentType")
    def force_empty_content_type(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_empty_content_type.setter
    def force_empty_content_type(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def md5hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @md5hash.setter
    def md5hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def md5hexhash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @md5hexhash.setter
    def md5hexhash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mediaLink")
    def media_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @media_link.setter
    def media_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputName")
    def output_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_name.setter
    def output_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def retention(self) -> Optional[pulumi.Input[BucketObjectRetentionArgs]]: ...
    @retention.setter
    def retention(self, value: Optional[pulumi.Input[BucketObjectRetentionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]: ...
    @source.setter
    def source(
        self, value: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceMd5hash")
    def source_md5hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_md5hash.setter
    def source_md5hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="temporaryHold")
    def temporary_hold(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @temporary_hold.setter
    def temporary_hold(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("gcp:storage/bucketObject:BucketObject")
class BucketObject(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_control: Optional[pulumi.Input[_builtins.str]] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        content_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
        content_encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        content_language: Optional[pulumi.Input[_builtins.str]] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        contexts: Optional[
            pulumi.Input[Union[BucketObjectContextsArgs, BucketObjectContextsArgsDict]]
        ] = ...,
        customer_encryption: Optional[
            pulumi.Input[
                Union[
                    BucketObjectCustomerEncryptionArgs,
                    BucketObjectCustomerEncryptionArgsDict,
                ]
            ]
        ] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        detect_md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        event_based_hold: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_empty_content_type: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        retention: Optional[
            pulumi.Input[
                Union[BucketObjectRetentionArgs, BucketObjectRetentionArgsDict]
            ]
        ] = ...,
        source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = ...,
        source_md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        temporary_hold: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BucketObjectArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_control: Optional[pulumi.Input[_builtins.str]] = ...,
        content: Optional[pulumi.Input[_builtins.str]] = ...,
        content_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
        content_encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        content_language: Optional[pulumi.Input[_builtins.str]] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        contexts: Optional[
            pulumi.Input[Union[BucketObjectContextsArgs, BucketObjectContextsArgsDict]]
        ] = ...,
        crc32c: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_encryption: Optional[
            pulumi.Input[
                Union[
                    BucketObjectCustomerEncryptionArgs,
                    BucketObjectCustomerEncryptionArgsDict,
                ]
            ]
        ] = ...,
        deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        detect_md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        event_based_hold: Optional[pulumi.Input[_builtins.bool]] = ...,
        force_empty_content_type: Optional[pulumi.Input[_builtins.bool]] = ...,
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        md5hexhash: Optional[pulumi.Input[_builtins.str]] = ...,
        media_link: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_name: Optional[pulumi.Input[_builtins.str]] = ...,
        retention: Optional[
            pulumi.Input[
                Union[BucketObjectRetentionArgs, BucketObjectRetentionArgsDict]
            ]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = ...,
        source_md5hash: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        temporary_hold: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> BucketObject: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def contexts(self) -> pulumi.Output[Optional[outputs.BucketObjectContexts]]: ...
    @_builtins.property
    @pulumi.getter
    def crc32c(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customerEncryption")
    def customer_encryption(
        self,
    ) -> pulumi.Output[Optional[outputs.BucketObjectCustomerEncryption]]: ...
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="detectMd5hash")
    def detect_md5hash(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="eventBasedHold")
    def event_based_hold(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="forceEmptyContentType")
    def force_empty_content_type(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def md5hash(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def md5hexhash(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mediaLink")
    def media_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputName")
    def output_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def retention(self) -> pulumi.Output[Optional[outputs.BucketObjectRetention]]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(
        self,
    ) -> pulumi.Output[Optional[Union[pulumi.Asset, pulumi.Archive]]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceMd5hash")
    def source_md5hash(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="temporaryHold")
    def temporary_hold(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
