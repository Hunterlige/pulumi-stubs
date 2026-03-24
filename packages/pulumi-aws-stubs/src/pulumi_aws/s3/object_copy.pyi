import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ObjectCopyArgs", "ObjectCopy"]

@pulumi.input_type
class ObjectCopyArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        source: pulumi.Input[_builtins.str],
        acl: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cache_control: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        content_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
        content_encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        content_language: Optional[pulumi.Input[_builtins.str]] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_match: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_modified_since: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_none_match: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_unmodified_since: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_key: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_key_md5: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_source_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        expires: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        grants: Optional[
            pulumi.Input[Sequence[pulumi.Input[ObjectCopyGrantArgs]]]
        ] = ...,
        kms_encryption_context: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        metadata_directive: Optional[pulumi.Input[_builtins.str]] = ...,
        object_lock_legal_hold_status: Optional[pulumi.Input[_builtins.str]] = ...,
        object_lock_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        object_lock_retain_until_date: Optional[pulumi.Input[_builtins.str]] = ...,
        override_provider: Optional[pulumi.Input[ObjectCopyOverrideProviderArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_payer: Optional[pulumi.Input[_builtins.str]] = ...,
        server_side_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        source_customer_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        source_customer_key: Optional[pulumi.Input[_builtins.str]] = ...,
        source_customer_key_md5: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        tagging_directive: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        website_redirect: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def acl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acl.setter
    def acl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bucket_key_enabled.setter
    def bucket_key_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cache_control.setter
    def cache_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="checksumAlgorithm")
    def checksum_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checksum_algorithm.setter
    def checksum_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="copyIfMatch")
    def copy_if_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @copy_if_match.setter
    def copy_if_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="copyIfModifiedSince")
    def copy_if_modified_since(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @copy_if_modified_since.setter
    def copy_if_modified_since(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="copyIfNoneMatch")
    def copy_if_none_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @copy_if_none_match.setter
    def copy_if_none_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="copyIfUnmodifiedSince")
    def copy_if_unmodified_since(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @copy_if_unmodified_since.setter
    def copy_if_unmodified_since(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerAlgorithm")
    def customer_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_algorithm.setter
    def customer_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerKey")
    def customer_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_key.setter
    def customer_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerKeyMd5")
    def customer_key_md5(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_key_md5.setter
    def customer_key_md5(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expectedSourceBucketOwner")
    def expected_source_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_source_bucket_owner.setter
    def expected_source_bucket_owner(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def expires(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expires.setter
    def expires(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def grants(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ObjectCopyGrantArgs]]]]: ...
    @grants.setter
    def grants(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ObjectCopyGrantArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsEncryptionContext")
    def kms_encryption_context(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_encryption_context.setter
    def kms_encryption_context(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="metadataDirective")
    def metadata_directive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metadata_directive.setter
    def metadata_directive(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectLockLegalHoldStatus")
    def object_lock_legal_hold_status(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_lock_legal_hold_status.setter
    def object_lock_legal_hold_status(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="objectLockMode")
    def object_lock_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_lock_mode.setter
    def object_lock_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectLockRetainUntilDate")
    def object_lock_retain_until_date(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_lock_retain_until_date.setter
    def object_lock_retain_until_date(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="overrideProvider")
    def override_provider(
        self,
    ) -> Optional[pulumi.Input[ObjectCopyOverrideProviderArgs]]: ...
    @override_provider.setter
    def override_provider(
        self, value: Optional[pulumi.Input[ObjectCopyOverrideProviderArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestPayer")
    def request_payer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_payer.setter
    def request_payer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_side_encryption.setter
    def server_side_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceCustomerAlgorithm")
    def source_customer_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_customer_algorithm.setter
    def source_customer_algorithm(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceCustomerKey")
    def source_customer_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_customer_key.setter
    def source_customer_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceCustomerKeyMd5")
    def source_customer_key_md5(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_customer_key_md5.setter
    def source_customer_key_md5(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="taggingDirective")
    def tagging_directive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tagging_directive.setter
    def tagging_directive(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="websiteRedirect")
    def website_redirect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @website_redirect.setter
    def website_redirect(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ObjectCopyState:
    def __init__(
        __self__,
        *,
        acl: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cache_control: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_crc32: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_crc32c: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_crc64nvme: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_sha1: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_sha256: Optional[pulumi.Input[_builtins.str]] = ...,
        content_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
        content_encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        content_language: Optional[pulumi.Input[_builtins.str]] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_match: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_modified_since: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_none_match: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_unmodified_since: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_key: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_key_md5: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_source_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        expiration: Optional[pulumi.Input[_builtins.str]] = ...,
        expires: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        grants: Optional[
            pulumi.Input[Sequence[pulumi.Input[ObjectCopyGrantArgs]]]
        ] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_encryption_context: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_modified: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        metadata_directive: Optional[pulumi.Input[_builtins.str]] = ...,
        object_lock_legal_hold_status: Optional[pulumi.Input[_builtins.str]] = ...,
        object_lock_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        object_lock_retain_until_date: Optional[pulumi.Input[_builtins.str]] = ...,
        override_provider: Optional[pulumi.Input[ObjectCopyOverrideProviderArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_charged: Optional[pulumi.Input[_builtins.bool]] = ...,
        request_payer: Optional[pulumi.Input[_builtins.str]] = ...,
        server_side_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        source_customer_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        source_customer_key: Optional[pulumi.Input[_builtins.str]] = ...,
        source_customer_key_md5: Optional[pulumi.Input[_builtins.str]] = ...,
        source_version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        tagging_directive: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        website_redirect: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def acl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acl.setter
    def acl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @bucket_key_enabled.setter
    def bucket_key_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cache_control.setter
    def cache_control(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="checksumAlgorithm")
    def checksum_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checksum_algorithm.setter
    def checksum_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="checksumCrc32")
    def checksum_crc32(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checksum_crc32.setter
    def checksum_crc32(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="checksumCrc32c")
    def checksum_crc32c(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checksum_crc32c.setter
    def checksum_crc32c(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="checksumCrc64nvme")
    def checksum_crc64nvme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checksum_crc64nvme.setter
    def checksum_crc64nvme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="checksumSha1")
    def checksum_sha1(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checksum_sha1.setter
    def checksum_sha1(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="checksumSha256")
    def checksum_sha256(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checksum_sha256.setter
    def checksum_sha256(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="copyIfMatch")
    def copy_if_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @copy_if_match.setter
    def copy_if_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="copyIfModifiedSince")
    def copy_if_modified_since(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @copy_if_modified_since.setter
    def copy_if_modified_since(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="copyIfNoneMatch")
    def copy_if_none_match(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @copy_if_none_match.setter
    def copy_if_none_match(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="copyIfUnmodifiedSince")
    def copy_if_unmodified_since(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @copy_if_unmodified_since.setter
    def copy_if_unmodified_since(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customerAlgorithm")
    def customer_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_algorithm.setter
    def customer_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerKey")
    def customer_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_key.setter
    def customer_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerKeyMd5")
    def customer_key_md5(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_key_md5.setter
    def customer_key_md5(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="expectedSourceBucketOwner")
    def expected_source_bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expected_source_bucket_owner.setter
    def expected_source_bucket_owner(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expires(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expires.setter
    def expires(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def grants(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ObjectCopyGrantArgs]]]]: ...
    @grants.setter
    def grants(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ObjectCopyGrantArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsEncryptionContext")
    def kms_encryption_context(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_encryption_context.setter
    def kms_encryption_context(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modified.setter
    def last_modified(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="metadataDirective")
    def metadata_directive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metadata_directive.setter
    def metadata_directive(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectLockLegalHoldStatus")
    def object_lock_legal_hold_status(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_lock_legal_hold_status.setter
    def object_lock_legal_hold_status(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="objectLockMode")
    def object_lock_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_lock_mode.setter
    def object_lock_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectLockRetainUntilDate")
    def object_lock_retain_until_date(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_lock_retain_until_date.setter
    def object_lock_retain_until_date(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="overrideProvider")
    def override_provider(
        self,
    ) -> Optional[pulumi.Input[ObjectCopyOverrideProviderArgs]]: ...
    @override_provider.setter
    def override_provider(
        self, value: Optional[pulumi.Input[ObjectCopyOverrideProviderArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestCharged")
    def request_charged(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @request_charged.setter
    def request_charged(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requestPayer")
    def request_payer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_payer.setter
    def request_payer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_side_encryption.setter
    def server_side_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceCustomerAlgorithm")
    def source_customer_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_customer_algorithm.setter
    def source_customer_algorithm(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceCustomerKey")
    def source_customer_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_customer_key.setter
    def source_customer_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceCustomerKeyMd5")
    def source_customer_key_md5(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_customer_key_md5.setter
    def source_customer_key_md5(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceVersionId")
    def source_version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_version_id.setter
    def source_version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="taggingDirective")
    def tagging_directive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tagging_directive.setter
    def tagging_directive(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="websiteRedirect")
    def website_redirect(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @website_redirect.setter
    def website_redirect(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:s3/objectCopy:ObjectCopy")
class ObjectCopy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        acl: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cache_control: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        content_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
        content_encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        content_language: Optional[pulumi.Input[_builtins.str]] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_match: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_modified_since: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_none_match: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_unmodified_since: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_key: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_key_md5: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_source_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        expires: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        grants: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ObjectCopyGrantArgs, ObjectCopyGrantArgsDict]]
                ]
            ]
        ] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_encryption_context: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        metadata_directive: Optional[pulumi.Input[_builtins.str]] = ...,
        object_lock_legal_hold_status: Optional[pulumi.Input[_builtins.str]] = ...,
        object_lock_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        object_lock_retain_until_date: Optional[pulumi.Input[_builtins.str]] = ...,
        override_provider: Optional[
            pulumi.Input[
                Union[
                    ObjectCopyOverrideProviderArgs, ObjectCopyOverrideProviderArgsDict
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_payer: Optional[pulumi.Input[_builtins.str]] = ...,
        server_side_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        source_customer_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        source_customer_key: Optional[pulumi.Input[_builtins.str]] = ...,
        source_customer_key_md5: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        tagging_directive: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        website_redirect: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ObjectCopyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        acl: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cache_control: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_crc32: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_crc32c: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_crc64nvme: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_sha1: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum_sha256: Optional[pulumi.Input[_builtins.str]] = ...,
        content_disposition: Optional[pulumi.Input[_builtins.str]] = ...,
        content_encoding: Optional[pulumi.Input[_builtins.str]] = ...,
        content_language: Optional[pulumi.Input[_builtins.str]] = ...,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_match: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_modified_since: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_none_match: Optional[pulumi.Input[_builtins.str]] = ...,
        copy_if_unmodified_since: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_key: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_key_md5: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        expected_source_bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        expiration: Optional[pulumi.Input[_builtins.str]] = ...,
        expires: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        grants: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ObjectCopyGrantArgs, ObjectCopyGrantArgsDict]]
                ]
            ]
        ] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_encryption_context: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        last_modified: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        metadata_directive: Optional[pulumi.Input[_builtins.str]] = ...,
        object_lock_legal_hold_status: Optional[pulumi.Input[_builtins.str]] = ...,
        object_lock_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        object_lock_retain_until_date: Optional[pulumi.Input[_builtins.str]] = ...,
        override_provider: Optional[
            pulumi.Input[
                Union[
                    ObjectCopyOverrideProviderArgs, ObjectCopyOverrideProviderArgsDict
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        request_charged: Optional[pulumi.Input[_builtins.bool]] = ...,
        request_payer: Optional[pulumi.Input[_builtins.str]] = ...,
        server_side_encryption: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        source_customer_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        source_customer_key: Optional[pulumi.Input[_builtins.str]] = ...,
        source_customer_key_md5: Optional[pulumi.Input[_builtins.str]] = ...,
        source_version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        tagging_directive: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        website_redirect: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ObjectCopy: ...
    @_builtins.property
    @pulumi.getter
    def acl(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="checksumAlgorithm")
    def checksum_algorithm(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="checksumCrc32")
    def checksum_crc32(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="checksumCrc32c")
    def checksum_crc32c(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="checksumCrc64nvme")
    def checksum_crc64nvme(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="checksumSha1")
    def checksum_sha1(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="checksumSha256")
    def checksum_sha256(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="copyIfMatch")
    def copy_if_match(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="copyIfModifiedSince")
    def copy_if_modified_since(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="copyIfNoneMatch")
    def copy_if_none_match(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="copyIfUnmodifiedSince")
    def copy_if_unmodified_since(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="customerAlgorithm")
    def customer_algorithm(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customerKey")
    def customer_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="customerKeyMd5")
    def customer_key_md5(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="expectedSourceBucketOwner")
    def expected_source_bucket_owner(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def expires(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def grants(self) -> pulumi.Output[Optional[Sequence[outputs.ObjectCopyGrant]]]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsEncryptionContext")
    def kms_encryption_context(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="metadataDirective")
    def metadata_directive(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="objectLockLegalHoldStatus")
    def object_lock_legal_hold_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectLockMode")
    def object_lock_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectLockRetainUntilDate")
    def object_lock_retain_until_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="overrideProvider")
    def override_provider(
        self,
    ) -> pulumi.Output[Optional[outputs.ObjectCopyOverrideProvider]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestCharged")
    def request_charged(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="requestPayer")
    def request_payer(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceCustomerAlgorithm")
    def source_customer_algorithm(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceCustomerKey")
    def source_customer_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceCustomerKeyMd5")
    def source_customer_key_md5(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceVersionId")
    def source_version_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="taggingDirective")
    def tagging_directive(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="websiteRedirect")
    def website_redirect(self) -> pulumi.Output[_builtins.str]: ...
