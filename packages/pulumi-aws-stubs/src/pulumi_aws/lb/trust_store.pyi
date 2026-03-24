import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TrustStoreArgs", "TrustStore"]

@pulumi.input_type
class TrustStoreArgs:
    def __init__(
        __self__,
        *,
        ca_certificates_bundle_s3_bucket: pulumi.Input[_builtins.str],
        ca_certificates_bundle_s3_key: pulumi.Input[_builtins.str],
        ca_certificates_bundle_s3_object_version: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleS3Bucket")
    def ca_certificates_bundle_s3_bucket(self) -> pulumi.Input[_builtins.str]: ...
    @ca_certificates_bundle_s3_bucket.setter
    def ca_certificates_bundle_s3_bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleS3Key")
    def ca_certificates_bundle_s3_key(self) -> pulumi.Input[_builtins.str]: ...
    @ca_certificates_bundle_s3_key.setter
    def ca_certificates_bundle_s3_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleS3ObjectVersion")
    def ca_certificates_bundle_s3_object_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificates_bundle_s3_object_version.setter
    def ca_certificates_bundle_s3_object_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.input_type
class _TrustStoreState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        arn_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificates_bundle_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificates_bundle_s3_key: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificates_bundle_s3_object_version: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="arnSuffix")
    def arn_suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn_suffix.setter
    def arn_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleS3Bucket")
    def ca_certificates_bundle_s3_bucket(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificates_bundle_s3_bucket.setter
    def ca_certificates_bundle_s3_bucket(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleS3Key")
    def ca_certificates_bundle_s3_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificates_bundle_s3_key.setter
    def ca_certificates_bundle_s3_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleS3ObjectVersion")
    def ca_certificates_bundle_s3_object_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ca_certificates_bundle_s3_object_version.setter
    def ca_certificates_bundle_s3_object_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:lb/trustStore:TrustStore")
class TrustStore(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        ca_certificates_bundle_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificates_bundle_s3_key: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificates_bundle_s3_object_version: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TrustStoreArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        arn_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificates_bundle_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificates_bundle_s3_key: Optional[pulumi.Input[_builtins.str]] = ...,
        ca_certificates_bundle_s3_object_version: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> TrustStore: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="arnSuffix")
    def arn_suffix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleS3Bucket")
    def ca_certificates_bundle_s3_bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleS3Key")
    def ca_certificates_bundle_s3_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="caCertificatesBundleS3ObjectVersion")
    def ca_certificates_bundle_s3_object_version(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
