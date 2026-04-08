import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EventActionActionArgs",
    "EventActionActionArgsDict",
    "EventActionActionExportRevisionToS3Args",
    "EventActionActionExportRevisionToS3ArgsDict",
    "EventActionActionExportRevisionToS3EncryptionArgs",
    ...,
    ...,
    ...,
    "EventActionEventArgs",
    "EventActionEventArgsDict",
    "EventActionEventRevisionPublishedArgs",
    "EventActionEventRevisionPublishedArgsDict",
    "RevisionAssetsAssetArgs",
    "RevisionAssetsAssetArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "RevisionAssetsAssetImportAssetsFromS3Args",
    "RevisionAssetsAssetImportAssetsFromS3ArgsDict",
    ...,
    ...,
    "RevisionAssetsAssetImportAssetsFromSignedUrlArgs",
    ...,
    "RevisionAssetsTimeoutsArgs",
    "RevisionAssetsTimeoutsArgsDict",
]

class EventActionActionArgsDict(TypedDict):
    export_revision_to_s3: pulumi.Input[EventActionActionExportRevisionToS3ArgsDict]

@pulumi.input_type
class EventActionActionArgs:
    def __init__(
        __self__,
        *,
        export_revision_to_s3: pulumi.Input[EventActionActionExportRevisionToS3Args],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exportRevisionToS3")
    def export_revision_to_s3(
        self,
    ) -> pulumi.Input[EventActionActionExportRevisionToS3Args]: ...
    @export_revision_to_s3.setter
    def export_revision_to_s3(
        self, value: pulumi.Input[EventActionActionExportRevisionToS3Args]
    ): ...

class EventActionActionExportRevisionToS3ArgsDict(TypedDict):
    revision_destination: pulumi.Input[
        EventActionActionExportRevisionToS3RevisionDestinationArgsDict
    ]
    encryption: NotRequired[
        pulumi.Input[EventActionActionExportRevisionToS3EncryptionArgsDict]
    ]

@pulumi.input_type
class EventActionActionExportRevisionToS3Args:
    def __init__(
        __self__,
        *,
        revision_destination: pulumi.Input[
            EventActionActionExportRevisionToS3RevisionDestinationArgs
        ],
        encryption: Optional[
            pulumi.Input[EventActionActionExportRevisionToS3EncryptionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="revisionDestination")
    def revision_destination(
        self,
    ) -> pulumi.Input[EventActionActionExportRevisionToS3RevisionDestinationArgs]: ...
    @revision_destination.setter
    def revision_destination(
        self,
        value: pulumi.Input[EventActionActionExportRevisionToS3RevisionDestinationArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def encryption(
        self,
    ) -> Optional[pulumi.Input[EventActionActionExportRevisionToS3EncryptionArgs]]: ...
    @encryption.setter
    def encryption(
        self,
        value: Optional[
            pulumi.Input[EventActionActionExportRevisionToS3EncryptionArgs]
        ],
    ): ...

class EventActionActionExportRevisionToS3EncryptionArgsDict(TypedDict):
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventActionActionExportRevisionToS3EncryptionArgs:
    def __init__(
        __self__,
        *,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventActionActionExportRevisionToS3RevisionDestinationArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    key_pattern: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EventActionActionExportRevisionToS3RevisionDestinationArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        key_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyPattern")
    def key_pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_pattern.setter
    def key_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventActionEventArgsDict(TypedDict):
    revision_published: pulumi.Input[EventActionEventRevisionPublishedArgsDict]

@pulumi.input_type
class EventActionEventArgs:
    def __init__(
        __self__,
        *,
        revision_published: pulumi.Input[EventActionEventRevisionPublishedArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="revisionPublished")
    def revision_published(
        self,
    ) -> pulumi.Input[EventActionEventRevisionPublishedArgs]: ...
    @revision_published.setter
    def revision_published(
        self, value: pulumi.Input[EventActionEventRevisionPublishedArgs]
    ): ...

class EventActionEventRevisionPublishedArgsDict(TypedDict):
    data_set_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventActionEventRevisionPublishedArgs:
    def __init__(__self__, *, data_set_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Input[_builtins.str]: ...
    @data_set_id.setter
    def data_set_id(self, value: pulumi.Input[_builtins.str]): ...

class RevisionAssetsAssetArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]
    create_s3_data_access_from_s3_bucket: NotRequired[
        pulumi.Input[RevisionAssetsAssetCreateS3DataAccessFromS3BucketArgsDict]
    ]
    created_at: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    import_assets_from_s3: NotRequired[
        pulumi.Input[RevisionAssetsAssetImportAssetsFromS3ArgsDict]
    ]
    import_assets_from_signed_url: NotRequired[
        pulumi.Input[RevisionAssetsAssetImportAssetsFromSignedUrlArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    updated_at: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RevisionAssetsAssetArgs:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        create_s3_data_access_from_s3_bucket: Optional[
            pulumi.Input[RevisionAssetsAssetCreateS3DataAccessFromS3BucketArgs]
        ] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        import_assets_from_s3: Optional[
            pulumi.Input[RevisionAssetsAssetImportAssetsFromS3Args]
        ] = ...,
        import_assets_from_signed_url: Optional[
            pulumi.Input[RevisionAssetsAssetImportAssetsFromSignedUrlArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        updated_at: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createS3DataAccessFromS3Bucket")
    def create_s3_data_access_from_s3_bucket(
        self,
    ) -> Optional[
        pulumi.Input[RevisionAssetsAssetCreateS3DataAccessFromS3BucketArgs]
    ]: ...
    @create_s3_data_access_from_s3_bucket.setter
    def create_s3_data_access_from_s3_bucket(
        self,
        value: Optional[
            pulumi.Input[RevisionAssetsAssetCreateS3DataAccessFromS3BucketArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="importAssetsFromS3")
    def import_assets_from_s3(
        self,
    ) -> Optional[pulumi.Input[RevisionAssetsAssetImportAssetsFromS3Args]]: ...
    @import_assets_from_s3.setter
    def import_assets_from_s3(
        self, value: Optional[pulumi.Input[RevisionAssetsAssetImportAssetsFromS3Args]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="importAssetsFromSignedUrl")
    def import_assets_from_signed_url(
        self,
    ) -> Optional[pulumi.Input[RevisionAssetsAssetImportAssetsFromSignedUrlArgs]]: ...
    @import_assets_from_signed_url.setter
    def import_assets_from_signed_url(
        self,
        value: Optional[pulumi.Input[RevisionAssetsAssetImportAssetsFromSignedUrlArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RevisionAssetsAssetCreateS3DataAccessFromS3BucketArgsDict(TypedDict):
    access_point_alias: NotRequired[pulumi.Input[_builtins.str]]
    access_point_arn: NotRequired[pulumi.Input[_builtins.str]]
    asset_source: NotRequired[
        pulumi.Input[
            RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceArgsDict
        ]
    ]

@pulumi.input_type
class RevisionAssetsAssetCreateS3DataAccessFromS3BucketArgs:
    def __init__(
        __self__,
        *,
        access_point_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        access_point_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        asset_source: Optional[
            pulumi.Input[
                RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPointAlias")
    def access_point_alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_point_alias.setter
    def access_point_alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="accessPointArn")
    def access_point_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_point_arn.setter
    def access_point_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="assetSource")
    def asset_source(
        self,
    ) -> Optional[
        pulumi.Input[RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceArgs]
    ]: ...
    @asset_source.setter
    def asset_source(
        self,
        value: Optional[
            pulumi.Input[
                RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceArgs
            ]
        ],
    ): ...

class RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    key_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    kms_keys_to_grants: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrantArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        key_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        keys: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        kms_keys_to_grants: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrantArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyPrefixes")
    def key_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @key_prefixes.setter
    def key_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @keys.setter
    def keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeysToGrants")
    def kms_keys_to_grants(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrantArgs
                ]
            ]
        ]
    ]: ...
    @kms_keys_to_grants.setter
    def kms_keys_to_grants(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrantArgs
                    ]
                ]
            ]
        ],
    ): ...

class RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrantArgsDict(
    TypedDict
):
    kms_key_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class RevisionAssetsAssetCreateS3DataAccessFromS3BucketAssetSourceKmsKeysToGrantArgs:
    def __init__(__self__, *, kms_key_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: pulumi.Input[_builtins.str]): ...

class RevisionAssetsAssetImportAssetsFromS3ArgsDict(TypedDict):
    asset_source: NotRequired[
        pulumi.Input[RevisionAssetsAssetImportAssetsFromS3AssetSourceArgsDict]
    ]

@pulumi.input_type
class RevisionAssetsAssetImportAssetsFromS3Args:
    def __init__(
        __self__,
        *,
        asset_source: Optional[
            pulumi.Input[RevisionAssetsAssetImportAssetsFromS3AssetSourceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assetSource")
    def asset_source(
        self,
    ) -> Optional[
        pulumi.Input[RevisionAssetsAssetImportAssetsFromS3AssetSourceArgs]
    ]: ...
    @asset_source.setter
    def asset_source(
        self,
        value: Optional[
            pulumi.Input[RevisionAssetsAssetImportAssetsFromS3AssetSourceArgs]
        ],
    ): ...

class RevisionAssetsAssetImportAssetsFromS3AssetSourceArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]

@pulumi.input_type
class RevisionAssetsAssetImportAssetsFromS3AssetSourceArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
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

class RevisionAssetsAssetImportAssetsFromSignedUrlArgsDict(TypedDict):
    filename: pulumi.Input[_builtins.str]

@pulumi.input_type
class RevisionAssetsAssetImportAssetsFromSignedUrlArgs:
    def __init__(__self__, *, filename: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filename(self) -> pulumi.Input[_builtins.str]: ...
    @filename.setter
    def filename(self, value: pulumi.Input[_builtins.str]): ...

class RevisionAssetsTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RevisionAssetsTimeoutsArgs:
    def __init__(
        __self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
