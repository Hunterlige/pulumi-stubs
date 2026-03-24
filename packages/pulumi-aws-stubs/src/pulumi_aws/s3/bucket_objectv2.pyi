

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BucketObjectv2Args', 'BucketObjectv2']
@pulumi.input_type
class BucketObjectv2Args:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], acl: Optional[pulumi.Input[_builtins.str]] = ..., bucket_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cache_control: Optional[pulumi.Input[_builtins.str]] = ..., checksum_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., content: Optional[pulumi.Input[_builtins.str]] = ..., content_base64: Optional[pulumi.Input[_builtins.str]] = ..., content_disposition: Optional[pulumi.Input[_builtins.str]] = ..., content_encoding: Optional[pulumi.Input[_builtins.str]] = ..., content_language: Optional[pulumi.Input[_builtins.str]] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., object_lock_legal_hold_status: Optional[pulumi.Input[_builtins.str]] = ..., object_lock_mode: Optional[pulumi.Input[_builtins.str]] = ..., object_lock_retain_until_date: Optional[pulumi.Input[_builtins.str]] = ..., override_provider: Optional[pulumi.Input[BucketObjectv2OverrideProviderArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = ..., source_hash: Optional[pulumi.Input[_builtins.str]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., website_redirect: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def acl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acl.setter
    def acl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bucket_key_enabled.setter
    def bucket_key_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_control.setter
    def cache_control(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumAlgorithm")
    def checksum_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @checksum_algorithm.setter
    def checksum_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBase64")
    def content_base64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_base64.setter
    def content_base64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_disposition.setter
    def content_disposition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_encoding.setter
    def content_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_language.setter
    def content_language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockLegalHoldStatus")
    def object_lock_legal_hold_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_lock_legal_hold_status.setter
    def object_lock_legal_hold_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockMode")
    def object_lock_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_lock_mode.setter
    def object_lock_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockRetainUntilDate")
    def object_lock_retain_until_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_lock_retain_until_date.setter
    def object_lock_retain_until_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideProvider")
    def override_provider(self) -> Optional[pulumi.Input[BucketObjectv2OverrideProviderArgs]]:
        
        ...
    
    @override_provider.setter
    def override_provider(self, value: Optional[pulumi.Input[BucketObjectv2OverrideProviderArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_side_encryption.setter
    def server_side_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceHash")
    def source_hash(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_hash.setter
    def source_hash(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteRedirect")
    def website_redirect(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @website_redirect.setter
    def website_redirect(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BucketObjectv2State:
    def __init__(__self__, *, acl: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., bucket_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cache_control: Optional[pulumi.Input[_builtins.str]] = ..., checksum_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., checksum_crc32: Optional[pulumi.Input[_builtins.str]] = ..., checksum_crc32c: Optional[pulumi.Input[_builtins.str]] = ..., checksum_crc64nvme: Optional[pulumi.Input[_builtins.str]] = ..., checksum_sha1: Optional[pulumi.Input[_builtins.str]] = ..., checksum_sha256: Optional[pulumi.Input[_builtins.str]] = ..., content: Optional[pulumi.Input[_builtins.str]] = ..., content_base64: Optional[pulumi.Input[_builtins.str]] = ..., content_disposition: Optional[pulumi.Input[_builtins.str]] = ..., content_encoding: Optional[pulumi.Input[_builtins.str]] = ..., content_language: Optional[pulumi.Input[_builtins.str]] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., object_lock_legal_hold_status: Optional[pulumi.Input[_builtins.str]] = ..., object_lock_mode: Optional[pulumi.Input[_builtins.str]] = ..., object_lock_retain_until_date: Optional[pulumi.Input[_builtins.str]] = ..., override_provider: Optional[pulumi.Input[BucketObjectv2OverrideProviderArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = ..., source_hash: Optional[pulumi.Input[_builtins.str]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., version_id: Optional[pulumi.Input[_builtins.str]] = ..., website_redirect: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def acl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acl.setter
    def acl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bucket_key_enabled.setter
    def bucket_key_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_control.setter
    def cache_control(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumAlgorithm")
    def checksum_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @checksum_algorithm.setter
    def checksum_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumCrc32")
    def checksum_crc32(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @checksum_crc32.setter
    def checksum_crc32(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumCrc32c")
    def checksum_crc32c(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @checksum_crc32c.setter
    def checksum_crc32c(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumCrc64nvme")
    def checksum_crc64nvme(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @checksum_crc64nvme.setter
    def checksum_crc64nvme(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumSha1")
    def checksum_sha1(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @checksum_sha1.setter
    def checksum_sha1(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumSha256")
    def checksum_sha256(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @checksum_sha256.setter
    def checksum_sha256(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBase64")
    def content_base64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_base64.setter
    def content_base64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_disposition.setter
    def content_disposition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_encoding.setter
    def content_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_language.setter
    def content_language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockLegalHoldStatus")
    def object_lock_legal_hold_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_lock_legal_hold_status.setter
    def object_lock_legal_hold_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockMode")
    def object_lock_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_lock_mode.setter
    def object_lock_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockRetainUntilDate")
    def object_lock_retain_until_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_lock_retain_until_date.setter
    def object_lock_retain_until_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideProvider")
    def override_provider(self) -> Optional[pulumi.Input[BucketObjectv2OverrideProviderArgs]]:
        
        ...
    
    @override_provider.setter
    def override_provider(self, value: Optional[pulumi.Input[BucketObjectv2OverrideProviderArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_side_encryption.setter
    def server_side_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceHash")
    def source_hash(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_hash.setter
    def source_hash(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteRedirect")
    def website_redirect(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @website_redirect.setter
    def website_redirect(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:s3/bucketObjectv2:BucketObjectv2")
class BucketObjectv2(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., acl: Optional[pulumi.Input[_builtins.str]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., bucket_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cache_control: Optional[pulumi.Input[_builtins.str]] = ..., checksum_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., content: Optional[pulumi.Input[_builtins.str]] = ..., content_base64: Optional[pulumi.Input[_builtins.str]] = ..., content_disposition: Optional[pulumi.Input[_builtins.str]] = ..., content_encoding: Optional[pulumi.Input[_builtins.str]] = ..., content_language: Optional[pulumi.Input[_builtins.str]] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., object_lock_legal_hold_status: Optional[pulumi.Input[_builtins.str]] = ..., object_lock_mode: Optional[pulumi.Input[_builtins.str]] = ..., object_lock_retain_until_date: Optional[pulumi.Input[_builtins.str]] = ..., override_provider: Optional[pulumi.Input[Union[BucketObjectv2OverrideProviderArgs, BucketObjectv2OverrideProviderArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = ..., source_hash: Optional[pulumi.Input[_builtins.str]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., website_redirect: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BucketObjectv2Args, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., acl: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bucket: Optional[pulumi.Input[_builtins.str]] = ..., bucket_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., cache_control: Optional[pulumi.Input[_builtins.str]] = ..., checksum_algorithm: Optional[pulumi.Input[_builtins.str]] = ..., checksum_crc32: Optional[pulumi.Input[_builtins.str]] = ..., checksum_crc32c: Optional[pulumi.Input[_builtins.str]] = ..., checksum_crc64nvme: Optional[pulumi.Input[_builtins.str]] = ..., checksum_sha1: Optional[pulumi.Input[_builtins.str]] = ..., checksum_sha256: Optional[pulumi.Input[_builtins.str]] = ..., content: Optional[pulumi.Input[_builtins.str]] = ..., content_base64: Optional[pulumi.Input[_builtins.str]] = ..., content_disposition: Optional[pulumi.Input[_builtins.str]] = ..., content_encoding: Optional[pulumi.Input[_builtins.str]] = ..., content_language: Optional[pulumi.Input[_builtins.str]] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., object_lock_legal_hold_status: Optional[pulumi.Input[_builtins.str]] = ..., object_lock_mode: Optional[pulumi.Input[_builtins.str]] = ..., object_lock_retain_until_date: Optional[pulumi.Input[_builtins.str]] = ..., override_provider: Optional[pulumi.Input[Union[BucketObjectv2OverrideProviderArgs, BucketObjectv2OverrideProviderArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_side_encryption: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = ..., source_hash: Optional[pulumi.Input[_builtins.str]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., version_id: Optional[pulumi.Input[_builtins.str]] = ..., website_redirect: Optional[pulumi.Input[_builtins.str]] = ...) -> BucketObjectv2:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def acl(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumAlgorithm")
    def checksum_algorithm(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumCrc32")
    def checksum_crc32(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumCrc32c")
    def checksum_crc32c(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumCrc64nvme")
    def checksum_crc64nvme(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumSha1")
    def checksum_sha1(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checksumSha256")
    def checksum_sha256(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBase64")
    def content_base64(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockLegalHoldStatus")
    def object_lock_legal_hold_status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockMode")
    def object_lock_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockRetainUntilDate")
    def object_lock_retain_until_date(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideProvider")
    def override_provider(self) -> pulumi.Output[Optional[outputs.BucketObjectv2OverrideProvider]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[Union[pulumi.Asset, pulumi.Archive]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceHash")
    def source_hash(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteRedirect")
    def website_redirect(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


