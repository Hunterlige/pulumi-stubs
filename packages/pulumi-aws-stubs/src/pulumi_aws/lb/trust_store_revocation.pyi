import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TrustStoreRevocationArgs", "TrustStoreRevocation"]

@pulumi.input_type
class TrustStoreRevocationArgs:
    def __init__(
        __self__,
        *,
        revocations_s3_bucket: pulumi.Input[_builtins.str],
        revocations_s3_key: pulumi.Input[_builtins.str],
        trust_store_arn: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        revocations_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="revocationsS3Bucket")
    def revocations_s3_bucket(self) -> pulumi.Input[_builtins.str]: ...
    @revocations_s3_bucket.setter
    def revocations_s3_bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="revocationsS3Key")
    def revocations_s3_key(self) -> pulumi.Input[_builtins.str]: ...
    @revocations_s3_key.setter
    def revocations_s3_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="trustStoreArn")
    def trust_store_arn(self) -> pulumi.Input[_builtins.str]: ...
    @trust_store_arn.setter
    def trust_store_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revocationsS3ObjectVersion")
    def revocations_s3_object_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revocations_s3_object_version.setter
    def revocations_s3_object_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.input_type
class _TrustStoreRevocationState:
    def __init__(
        __self__,
        *,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        revocation_id: Optional[pulumi.Input[_builtins.int]] = ...,
        revocations_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        revocations_s3_key: Optional[pulumi.Input[_builtins.str]] = ...,
        revocations_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_store_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revocationId")
    def revocation_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @revocation_id.setter
    def revocation_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="revocationsS3Bucket")
    def revocations_s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revocations_s3_bucket.setter
    def revocations_s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revocationsS3Key")
    def revocations_s3_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revocations_s3_key.setter
    def revocations_s3_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revocationsS3ObjectVersion")
    def revocations_s3_object_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revocations_s3_object_version.setter
    def revocations_s3_object_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trustStoreArn")
    def trust_store_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trust_store_arn.setter
    def trust_store_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:lb/trustStoreRevocation:TrustStoreRevocation")
class TrustStoreRevocation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        revocations_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        revocations_s3_key: Optional[pulumi.Input[_builtins.str]] = ...,
        revocations_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_store_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TrustStoreRevocationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        revocation_id: Optional[pulumi.Input[_builtins.int]] = ...,
        revocations_s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        revocations_s3_key: Optional[pulumi.Input[_builtins.str]] = ...,
        revocations_s3_object_version: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_store_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> TrustStoreRevocation: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revocationId")
    def revocation_id(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="revocationsS3Bucket")
    def revocations_s3_bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revocationsS3Key")
    def revocations_s3_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revocationsS3ObjectVersion")
    def revocations_s3_object_version(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trustStoreArn")
    def trust_store_arn(self) -> pulumi.Output[_builtins.str]: ...
