import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["S3LocationArgs", "S3Location"]

@pulumi.input_type
class S3LocationArgs:
    def __init__(
        __self__,
        *,
        s3_bucket_arn: pulumi.Input[_builtins.str],
        s3_config: pulumi.Input[S3LocationS3ConfigArgs],
        subdirectory: pulumi.Input[_builtins.str],
        agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketArn")
    def s3_bucket_arn(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket_arn.setter
    def s3_bucket_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Config")
    def s3_config(self) -> pulumi.Input[S3LocationS3ConfigArgs]: ...
    @s3_config.setter
    def s3_config(self, value: pulumi.Input[S3LocationS3ConfigArgs]): ...
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Input[_builtins.str]: ...
    @subdirectory.setter
    def subdirectory(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @agent_arns.setter
    def agent_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3StorageClass")
    def s3_storage_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_storage_class.setter
    def s3_storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _S3LocationState:
    def __init__(
        __self__,
        *,
        agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_config: Optional[pulumi.Input[S3LocationS3ConfigArgs]] = ...,
        s3_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @agent_arns.setter
    def agent_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3BucketArn")
    def s3_bucket_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_bucket_arn.setter
    def s3_bucket_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3Config")
    def s3_config(self) -> Optional[pulumi.Input[S3LocationS3ConfigArgs]]: ...
    @s3_config.setter
    def s3_config(self, value: Optional[pulumi.Input[S3LocationS3ConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="s3StorageClass")
    def s3_storage_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_storage_class.setter
    def s3_storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:datasync/s3Location:S3Location")
class S3Location(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_config: Optional[
            pulumi.Input[Union[S3LocationS3ConfigArgs, S3LocationS3ConfigArgsDict]]
        ] = ...,
        s3_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: S3LocationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_bucket_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_config: Optional[
            pulumi.Input[Union[S3LocationS3ConfigArgs, S3LocationS3ConfigArgsDict]]
        ] = ...,
        s3_storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> S3Location: ...
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketArn")
    def s3_bucket_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3Config")
    def s3_config(self) -> pulumi.Output[outputs.S3LocationS3Config]: ...
    @_builtins.property
    @pulumi.getter(name="s3StorageClass")
    def s3_storage_class(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Output[_builtins.str]: ...
