import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "RepositoryAssociationKmsKeyDetails",
    "RepositoryAssociationRepository",
    "RepositoryAssociationRepositoryBitbucket",
    "RepositoryAssociationRepositoryCodecommit",
    ...,
    "RepositoryAssociationRepositoryS3Bucket",
    "RepositoryAssociationS3RepositoryDetail",
    ...,
]

@pulumi.output_type
class RepositoryAssociationKmsKeyDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_option: Optional[_builtins.str] = ...,
        kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RepositoryAssociationRepository(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bitbucket: Optional[outputs.RepositoryAssociationRepositoryBitbucket] = ...,
        codecommit: Optional[outputs.RepositoryAssociationRepositoryCodecommit] = ...,
        github_enterprise_server: Optional[
            outputs.RepositoryAssociationRepositoryGithubEnterpriseServer
        ] = ...,
        s3_bucket: Optional[outputs.RepositoryAssociationRepositoryS3Bucket] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bitbucket(
        self,
    ) -> Optional[outputs.RepositoryAssociationRepositoryBitbucket]: ...
    @_builtins.property
    @pulumi.getter
    def codecommit(
        self,
    ) -> Optional[outputs.RepositoryAssociationRepositoryCodecommit]: ...
    @_builtins.property
    @pulumi.getter(name="githubEnterpriseServer")
    def github_enterprise_server(
        self,
    ) -> Optional[outputs.RepositoryAssociationRepositoryGithubEnterpriseServer]: ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(
        self,
    ) -> Optional[outputs.RepositoryAssociationRepositoryS3Bucket]: ...

@pulumi.output_type
class RepositoryAssociationRepositoryBitbucket(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_arn: _builtins.str,
        name: _builtins.str,
        owner: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...

@pulumi.output_type
class RepositoryAssociationRepositoryCodecommit(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class RepositoryAssociationRepositoryGithubEnterpriseServer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_arn: _builtins.str,
        name: _builtins.str,
        owner: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...

@pulumi.output_type
class RepositoryAssociationRepositoryS3Bucket(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, bucket_name: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class RepositoryAssociationS3RepositoryDetail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        code_artifacts: Optional[
            Sequence[outputs.RepositoryAssociationS3RepositoryDetailCodeArtifact]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="codeArtifacts")
    def code_artifacts(
        self,
    ) -> Optional[
        Sequence[outputs.RepositoryAssociationS3RepositoryDetailCodeArtifact]
    ]: ...

@pulumi.output_type
class RepositoryAssociationS3RepositoryDetailCodeArtifact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        build_artifacts_object_key: Optional[_builtins.str] = ...,
        source_code_artifacts_object_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="buildArtifactsObjectKey")
    def build_artifacts_object_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceCodeArtifactsObjectKey")
    def source_code_artifacts_object_key(self) -> Optional[_builtins.str]: ...
