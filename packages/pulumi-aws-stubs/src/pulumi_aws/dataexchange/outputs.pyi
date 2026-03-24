import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EventActionAction",
    "EventActionActionExportRevisionToS3",
    "EventActionActionExportRevisionToS3Encryption",
    ...,
    "EventActionEvent",
    "EventActionEventRevisionPublished",
    "RevisionAssetsAsset",
    "RevisionAssetsAssetCreateS3DataAccessFromS3Bucket",
    ...,
    ...,
    "RevisionAssetsAssetImportAssetsFromS3",
    "RevisionAssetsAssetImportAssetsFromS3AssetSource",
    "RevisionAssetsAssetImportAssetsFromSignedUrl",
    "RevisionAssetsTimeouts",
]

@pulumi.output_type
class EventActionAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, export_revision_to_s3: outputs.EventActionActionExportRevisionToS3
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exportRevisionToS3")
    def export_revision_to_s3(self) -> outputs.EventActionActionExportRevisionToS3: ...

@pulumi.output_type
class EventActionActionExportRevisionToS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        revision_destination: outputs.EventActionActionExportRevisionToS3RevisionDestination,
        encryption: Optional[
            outputs.EventActionActionExportRevisionToS3Encryption
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="revisionDestination")
    def revision_destination(
        self,
    ) -> outputs.EventActionActionExportRevisionToS3RevisionDestination: ...
    @_builtins.property
    @pulumi.getter
    def encryption(
        self,
    ) -> Optional[outputs.EventActionActionExportRevisionToS3Encryption]: ...

@pulumi.output_type
class EventActionActionExportRevisionToS3Encryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_arn: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventActionActionExportRevisionToS3RevisionDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, bucket: _builtins.str, key_pattern: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyPattern")
    def key_pattern(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EventActionEvent(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, revision_published: outputs.EventActionEventRevisionPublished
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="revisionPublished")
    def revision_published(self) -> outputs.EventActionEventRevisionPublished: ...

@pulumi.output_type
class EventActionEventRevisionPublished(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, data_set_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> _builtins.str: ...

@pulumi.output_type
class RevisionAssetsAsset(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: Optional[_builtins.str] = ...,
        create_s3_data_access_from_s3_bucket: Optional[
            outputs.RevisionAssetsAssetCreateS3DataAccessFromS3Bucket
        ] = ...,
        created_at: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        import_assets_from_s3: Optional[
            outputs.RevisionAssetsAssetImportAssetsFromS3
        ] = ...,
        import_assets_from_signed_url: Optional[
            outputs.RevisionAssetsAssetImportAssetsFromSignedUrl
        ] = ...,
        name: Optional[_builtins.str] = ...,
        updated_at: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createS3DataAccessFromS3Bucket")
    def create_s3_data_access_from_s3_bucket(
        self,
    ) -> Optional[outputs.RevisionAssetsAssetCreateS3DataAccessFromS3Bucket]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="importAssetsFromS3")
    def import_assets_from_s3(
        self,
    ) -> Optional[outputs.RevisionAssetsAssetImportAssetsFromS3]: ...
    @_builtins.property
    @pulumi.getter(name="importAssetsFromSignedUrl")
    def import_assets_from_signed_url(
        self,
    ) -> Optional[outputs.RevisionAssetsAssetImportAssetsFromSignedUrl]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RevisionAssetsAssetCreateS3DataAccessFromS3Bucket(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_point_alias: Optional[_builtins.str] = ...,
        access_point_arn: Optional[_builtins.str] = ...,
        asset_source: Optional[
            outputs.RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPointAlias")
    def access_point_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accessPointArn")
    def access_point_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="assetSource")
    def asset_source(
        self,
    ) -> Optional[
        outputs.RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSource
    ]: ...

@pulumi.output_type
class RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        key_prefixes: Optional[Sequence[_builtins.str]] = ...,
        keys: Optional[Sequence[_builtins.str]] = ...,
        kms_keys_to_grants: Optional[
            Sequence[
                outputs.RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrant
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyPrefixes")
    def key_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeysToGrants")
    def kms_keys_to_grants(
        self,
    ) -> Optional[
        Sequence[
            outputs.RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrant
        ]
    ]: ...

@pulumi.output_type
class RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrant(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...

@pulumi.output_type
class RevisionAssetsAssetImportAssetsFromS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        asset_source: Optional[
            outputs.RevisionAssetsAssetImportAssetsFromS3AssetSource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assetSource")
    def asset_source(
        self,
    ) -> Optional[outputs.RevisionAssetsAssetImportAssetsFromS3AssetSource]: ...

@pulumi.output_type
class RevisionAssetsAssetImportAssetsFromS3AssetSource(dict):
    def __init__(__self__, *, bucket: _builtins.str, key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...

@pulumi.output_type
class RevisionAssetsAssetImportAssetsFromSignedUrl(dict):
    def __init__(__self__, *, filename: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filename(self) -> _builtins.str: ...

@pulumi.output_type
class RevisionAssetsTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
