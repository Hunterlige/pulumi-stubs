import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "RepositoryAssociationKmsKeyDetailsArgs",
    "RepositoryAssociationKmsKeyDetailsArgsDict",
    "RepositoryAssociationRepositoryArgs",
    "RepositoryAssociationRepositoryArgsDict",
    "RepositoryAssociationRepositoryBitbucketArgs",
    "RepositoryAssociationRepositoryBitbucketArgsDict",
    "RepositoryAssociationRepositoryCodecommitArgs",
    "RepositoryAssociationRepositoryCodecommitArgsDict",
    ...,
    ...,
    "RepositoryAssociationRepositoryS3BucketArgs",
    "RepositoryAssociationRepositoryS3BucketArgsDict",
    "RepositoryAssociationS3RepositoryDetailArgs",
    "RepositoryAssociationS3RepositoryDetailArgsDict",
    ...,
    ...,
]

class RepositoryAssociationKmsKeyDetailsArgsDict(TypedDict):
    encryption_option: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryAssociationKmsKeyDetailsArgs:
    def __init__(
        __self__,
        *,
        encryption_option: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_option.setter
    def encryption_option(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryAssociationRepositoryArgsDict(TypedDict):
    bitbucket: NotRequired[
        pulumi.Input[RepositoryAssociationRepositoryBitbucketArgsDict]
    ]
    codecommit: NotRequired[
        pulumi.Input[RepositoryAssociationRepositoryCodecommitArgsDict]
    ]
    github_enterprise_server: NotRequired[
        pulumi.Input[RepositoryAssociationRepositoryGithubEnterpriseServerArgsDict]
    ]
    s3_bucket: NotRequired[
        pulumi.Input[RepositoryAssociationRepositoryS3BucketArgsDict]
    ]
    ...

@pulumi.input_type
class RepositoryAssociationRepositoryArgs:
    def __init__(
        __self__,
        *,
        bitbucket: Optional[
            pulumi.Input[RepositoryAssociationRepositoryBitbucketArgs]
        ] = ...,
        codecommit: Optional[
            pulumi.Input[RepositoryAssociationRepositoryCodecommitArgs]
        ] = ...,
        github_enterprise_server: Optional[
            pulumi.Input[RepositoryAssociationRepositoryGithubEnterpriseServerArgs]
        ] = ...,
        s3_bucket: Optional[
            pulumi.Input[RepositoryAssociationRepositoryS3BucketArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bitbucket(
        self,
    ) -> Optional[pulumi.Input[RepositoryAssociationRepositoryBitbucketArgs]]: ...
    @bitbucket.setter
    def bitbucket(
        self,
        value: Optional[pulumi.Input[RepositoryAssociationRepositoryBitbucketArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def codecommit(
        self,
    ) -> Optional[pulumi.Input[RepositoryAssociationRepositoryCodecommitArgs]]: ...
    @codecommit.setter
    def codecommit(
        self,
        value: Optional[pulumi.Input[RepositoryAssociationRepositoryCodecommitArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="githubEnterpriseServer")
    def github_enterprise_server(
        self,
    ) -> Optional[
        pulumi.Input[RepositoryAssociationRepositoryGithubEnterpriseServerArgs]
    ]: ...
    @github_enterprise_server.setter
    def github_enterprise_server(
        self,
        value: Optional[
            pulumi.Input[RepositoryAssociationRepositoryGithubEnterpriseServerArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(
        self,
    ) -> Optional[pulumi.Input[RepositoryAssociationRepositoryS3BucketArgs]]: ...
    @s3_bucket.setter
    def s3_bucket(
        self, value: Optional[pulumi.Input[RepositoryAssociationRepositoryS3BucketArgs]]
    ): ...

class RepositoryAssociationRepositoryBitbucketArgsDict(TypedDict):
    connection_arn: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    owner: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RepositoryAssociationRepositoryBitbucketArgs:
    def __init__(
        __self__,
        *,
        connection_arn: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        owner: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> pulumi.Input[_builtins.str]: ...
    @connection_arn.setter
    def connection_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Input[_builtins.str]: ...
    @owner.setter
    def owner(self, value: pulumi.Input[_builtins.str]): ...

class RepositoryAssociationRepositoryCodecommitArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RepositoryAssociationRepositoryCodecommitArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class RepositoryAssociationRepositoryGithubEnterpriseServerArgsDict(TypedDict):
    connection_arn: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    owner: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RepositoryAssociationRepositoryGithubEnterpriseServerArgs:
    def __init__(
        __self__,
        *,
        connection_arn: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        owner: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> pulumi.Input[_builtins.str]: ...
    @connection_arn.setter
    def connection_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Input[_builtins.str]: ...
    @owner.setter
    def owner(self, value: pulumi.Input[_builtins.str]): ...

class RepositoryAssociationRepositoryS3BucketArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RepositoryAssociationRepositoryS3BucketArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class RepositoryAssociationS3RepositoryDetailArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    code_artifacts: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RepositoryAssociationS3RepositoryDetailCodeArtifactArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class RepositoryAssociationS3RepositoryDetailArgs:
    def __init__(
        __self__,
        *,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        code_artifacts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryAssociationS3RepositoryDetailCodeArtifactArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="codeArtifacts")
    def code_artifacts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[RepositoryAssociationS3RepositoryDetailCodeArtifactArgs]
            ]
        ]
    ]: ...
    @code_artifacts.setter
    def code_artifacts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryAssociationS3RepositoryDetailCodeArtifactArgs
                    ]
                ]
            ]
        ],
    ): ...

class RepositoryAssociationS3RepositoryDetailCodeArtifactArgsDict(TypedDict):
    build_artifacts_object_key: NotRequired[pulumi.Input[_builtins.str]]
    source_code_artifacts_object_key: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryAssociationS3RepositoryDetailCodeArtifactArgs:
    def __init__(
        __self__,
        *,
        build_artifacts_object_key: Optional[pulumi.Input[_builtins.str]] = ...,
        source_code_artifacts_object_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="buildArtifactsObjectKey")
    def build_artifacts_object_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build_artifacts_object_key.setter
    def build_artifacts_object_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceCodeArtifactsObjectKey")
    def source_code_artifacts_object_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_code_artifacts_object_key.setter
    def source_code_artifacts_object_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
