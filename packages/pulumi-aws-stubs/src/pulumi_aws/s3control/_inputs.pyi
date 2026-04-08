import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessGrantAccessGrantsLocationConfigurationArgs",
    ...,
    "AccessGrantGranteeArgs",
    "AccessGrantGranteeArgsDict",
    "BucketLifecycleConfigurationRuleArgs",
    "BucketLifecycleConfigurationRuleArgsDict",
    ...,
    ...,
    "BucketLifecycleConfigurationRuleExpirationArgs",
    "BucketLifecycleConfigurationRuleExpirationArgsDict",
    "BucketLifecycleConfigurationRuleFilterArgs",
    "BucketLifecycleConfigurationRuleFilterArgsDict",
    "DirectoryBucketAccessPointScopeScopeArgs",
    "DirectoryBucketAccessPointScopeScopeArgsDict",
    "MultiRegionAccessPointDetailsArgs",
    "MultiRegionAccessPointDetailsArgsDict",
    "MultiRegionAccessPointDetailsPublicAccessBlockArgs",
    ...,
    "MultiRegionAccessPointDetailsRegionArgs",
    "MultiRegionAccessPointDetailsRegionArgsDict",
    "MultiRegionAccessPointPolicyDetailsArgs",
    "MultiRegionAccessPointPolicyDetailsArgsDict",
    "ObjectLambdaAccessPointConfigurationArgs",
    "ObjectLambdaAccessPointConfigurationArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

class AccessGrantAccessGrantsLocationConfigurationArgsDict(TypedDict):
    s3_sub_prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccessGrantAccessGrantsLocationConfigurationArgs:
    def __init__(
        __self__, *, s3_sub_prefix: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3SubPrefix")
    def s3_sub_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_sub_prefix.setter
    def s3_sub_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessGrantGranteeArgsDict(TypedDict):
    grantee_identifier: pulumi.Input[_builtins.str]
    grantee_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AccessGrantGranteeArgs:
    def __init__(
        __self__,
        *,
        grantee_identifier: pulumi.Input[_builtins.str],
        grantee_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="granteeIdentifier")
    def grantee_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @grantee_identifier.setter
    def grantee_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="granteeType")
    def grantee_type(self) -> pulumi.Input[_builtins.str]: ...
    @grantee_type.setter
    def grantee_type(self, value: pulumi.Input[_builtins.str]): ...

class BucketLifecycleConfigurationRuleArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    abort_incomplete_multipart_upload: NotRequired[
        pulumi.Input[
            BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadArgsDict
        ]
    ]
    expiration: NotRequired[
        pulumi.Input[BucketLifecycleConfigurationRuleExpirationArgsDict]
    ]
    filter: NotRequired[pulumi.Input[BucketLifecycleConfigurationRuleFilterArgsDict]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BucketLifecycleConfigurationRuleArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        abort_incomplete_multipart_upload: Optional[
            pulumi.Input[
                BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadArgs
            ]
        ] = ...,
        expiration: Optional[
            pulumi.Input[BucketLifecycleConfigurationRuleExpirationArgs]
        ] = ...,
        filter: Optional[
            pulumi.Input[BucketLifecycleConfigurationRuleFilterArgs]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="abortIncompleteMultipartUpload")
    def abort_incomplete_multipart_upload(
        self,
    ) -> Optional[
        pulumi.Input[BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadArgs]
    ]: ...
    @abort_incomplete_multipart_upload.setter
    def abort_incomplete_multipart_upload(
        self,
        value: Optional[
            pulumi.Input[
                BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def expiration(
        self,
    ) -> Optional[pulumi.Input[BucketLifecycleConfigurationRuleExpirationArgs]]: ...
    @expiration.setter
    def expiration(
        self,
        value: Optional[pulumi.Input[BucketLifecycleConfigurationRuleExpirationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> Optional[pulumi.Input[BucketLifecycleConfigurationRuleFilterArgs]]: ...
    @filter.setter
    def filter(
        self, value: Optional[pulumi.Input[BucketLifecycleConfigurationRuleFilterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadArgsDict(TypedDict):
    days_after_initiation: pulumi.Input[_builtins.int]

@pulumi.input_type
class BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadArgs:
    def __init__(
        __self__, *, days_after_initiation: pulumi.Input[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysAfterInitiation")
    def days_after_initiation(self) -> pulumi.Input[_builtins.int]: ...
    @days_after_initiation.setter
    def days_after_initiation(self, value: pulumi.Input[_builtins.int]): ...

class BucketLifecycleConfigurationRuleExpirationArgsDict(TypedDict):
    date: NotRequired[pulumi.Input[_builtins.str]]
    days: NotRequired[pulumi.Input[_builtins.int]]
    expired_object_delete_marker: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class BucketLifecycleConfigurationRuleExpirationArgs:
    def __init__(
        __self__,
        *,
        date: Optional[pulumi.Input[_builtins.str]] = ...,
        days: Optional[pulumi.Input[_builtins.int]] = ...,
        expired_object_delete_marker: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @date.setter
    def date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="expiredObjectDeleteMarker")
    def expired_object_delete_marker(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @expired_object_delete_marker.setter
    def expired_object_delete_marker(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class BucketLifecycleConfigurationRuleFilterArgsDict(TypedDict):
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class BucketLifecycleConfigurationRuleFilterArgs:
    def __init__(
        __self__,
        *,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class DirectoryBucketAccessPointScopeScopeArgsDict(TypedDict):
    permissions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DirectoryBucketAccessPointScopeScopeArgs:
    def __init__(
        __self__,
        *,
        permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @permissions.setter
    def permissions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @prefixes.setter
    def prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class MultiRegionAccessPointDetailsArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    regions: pulumi.Input[
        Sequence[pulumi.Input[MultiRegionAccessPointDetailsRegionArgsDict]]
    ]
    public_access_block: NotRequired[
        pulumi.Input[MultiRegionAccessPointDetailsPublicAccessBlockArgsDict]
    ]

@pulumi.input_type
class MultiRegionAccessPointDetailsArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        regions: pulumi.Input[
            Sequence[pulumi.Input[MultiRegionAccessPointDetailsRegionArgs]]
        ],
        public_access_block: Optional[
            pulumi.Input[MultiRegionAccessPointDetailsPublicAccessBlockArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[MultiRegionAccessPointDetailsRegionArgs]]
    ]: ...
    @regions.setter
    def regions(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[MultiRegionAccessPointDetailsRegionArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicAccessBlock")
    def public_access_block(
        self,
    ) -> Optional[pulumi.Input[MultiRegionAccessPointDetailsPublicAccessBlockArgs]]: ...
    @public_access_block.setter
    def public_access_block(
        self,
        value: Optional[
            pulumi.Input[MultiRegionAccessPointDetailsPublicAccessBlockArgs]
        ],
    ): ...

class MultiRegionAccessPointDetailsPublicAccessBlockArgsDict(TypedDict):
    block_public_acls: NotRequired[pulumi.Input[_builtins.bool]]
    block_public_policy: NotRequired[pulumi.Input[_builtins.bool]]
    ignore_public_acls: NotRequired[pulumi.Input[_builtins.bool]]
    restrict_public_buckets: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class MultiRegionAccessPointDetailsPublicAccessBlockArgs:
    def __init__(
        __self__,
        *,
        block_public_acls: Optional[pulumi.Input[_builtins.bool]] = ...,
        block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_public_acls: Optional[pulumi.Input[_builtins.bool]] = ...,
        restrict_public_buckets: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicAcls")
    def block_public_acls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @block_public_acls.setter
    def block_public_acls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @block_public_policy.setter
    def block_public_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ignorePublicAcls")
    def ignore_public_acls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_public_acls.setter
    def ignore_public_acls(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @restrict_public_buckets.setter
    def restrict_public_buckets(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class MultiRegionAccessPointDetailsRegionArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    bucket_account_id: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MultiRegionAccessPointDetailsRegionArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        bucket_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_account_id.setter
    def bucket_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MultiRegionAccessPointPolicyDetailsArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    policy: pulumi.Input[_builtins.str]

@pulumi.input_type
class MultiRegionAccessPointPolicyDetailsArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        policy: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Input[_builtins.str]: ...
    @policy.setter
    def policy(self, value: pulumi.Input[_builtins.str]): ...

class ObjectLambdaAccessPointConfigurationArgsDict(TypedDict):
    supporting_access_point: pulumi.Input[_builtins.str]
    transformation_configurations: pulumi.Input[
        Sequence[
            pulumi.Input[
                ObjectLambdaAccessPointConfigurationTransformationConfigurationArgsDict
            ]
        ]
    ]
    allowed_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cloud_watch_metrics_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ObjectLambdaAccessPointConfigurationArgs:
    def __init__(
        __self__,
        *,
        supporting_access_point: pulumi.Input[_builtins.str],
        transformation_configurations: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ObjectLambdaAccessPointConfigurationTransformationConfigurationArgs
                ]
            ]
        ],
        allowed_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cloud_watch_metrics_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="supportingAccessPoint")
    def supporting_access_point(self) -> pulumi.Input[_builtins.str]: ...
    @supporting_access_point.setter
    def supporting_access_point(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="transformationConfigurations")
    def transformation_configurations(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                ObjectLambdaAccessPointConfigurationTransformationConfigurationArgs
            ]
        ]
    ]: ...
    @transformation_configurations.setter
    def transformation_configurations(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ObjectLambdaAccessPointConfigurationTransformationConfigurationArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedFeatures")
    def allowed_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_features.setter
    def allowed_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchMetricsEnabled")
    def cloud_watch_metrics_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cloud_watch_metrics_enabled.setter
    def cloud_watch_metrics_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ObjectLambdaAccessPointConfigurationTransformationConfigurationArgsDict(
    TypedDict
):
    actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    content_transformation: pulumi.Input[
        ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationArgsDict
    ]

@pulumi.input_type
class ObjectLambdaAccessPointConfigurationTransformationConfigurationArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        content_transformation: pulumi.Input[
            ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="contentTransformation")
    def content_transformation(
        self,
    ) -> pulumi.Input[
        ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationArgs
    ]: ...
    @content_transformation.setter
    def content_transformation(
        self,
        value: pulumi.Input[
            ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationArgs
        ],
    ): ...

class ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationArgsDict(
    TypedDict
):
    aws_lambda: pulumi.Input[
        ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambdaArgsDict
    ]

@pulumi.input_type
class ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationArgs:
    def __init__(
        __self__,
        *,
        aws_lambda: pulumi.Input[
            ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambdaArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsLambda")
    def aws_lambda(
        self,
    ) -> pulumi.Input[
        ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambdaArgs
    ]: ...
    @aws_lambda.setter
    def aws_lambda(
        self,
        value: pulumi.Input[
            ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambdaArgs
        ],
    ): ...

class ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambdaArgsDict(
    TypedDict
):
    function_arn: pulumi.Input[_builtins.str]
    function_payload: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambdaArgs:
    def __init__(
        __self__,
        *,
        function_arn: pulumi.Input[_builtins.str],
        function_payload: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Input[_builtins.str]: ...
    @function_arn.setter
    def function_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="functionPayload")
    def function_payload(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @function_payload.setter
    def function_payload(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageLensConfigurationStorageLensConfigurationArgsDict(TypedDict):
    account_level: pulumi.Input[
        StorageLensConfigurationStorageLensConfigurationAccountLevelArgsDict
    ]
    enabled: pulumi.Input[_builtins.bool]
    aws_org: NotRequired[
        pulumi.Input[StorageLensConfigurationStorageLensConfigurationAwsOrgArgsDict]
    ]
    data_export: NotRequired[
        pulumi.Input[StorageLensConfigurationStorageLensConfigurationDataExportArgsDict]
    ]
    exclude: NotRequired[
        pulumi.Input[StorageLensConfigurationStorageLensConfigurationExcludeArgsDict]
    ]
    include: NotRequired[
        pulumi.Input[StorageLensConfigurationStorageLensConfigurationIncludeArgsDict]
    ]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationArgs:
    def __init__(
        __self__,
        *,
        account_level: pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelArgs
        ],
        enabled: pulumi.Input[_builtins.bool],
        aws_org: Optional[
            pulumi.Input[StorageLensConfigurationStorageLensConfigurationAwsOrgArgs]
        ] = ...,
        data_export: Optional[
            pulumi.Input[StorageLensConfigurationStorageLensConfigurationDataExportArgs]
        ] = ...,
        exclude: Optional[
            pulumi.Input[StorageLensConfigurationStorageLensConfigurationExcludeArgs]
        ] = ...,
        include: Optional[
            pulumi.Input[StorageLensConfigurationStorageLensConfigurationIncludeArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountLevel")
    def account_level(
        self,
    ) -> pulumi.Input[
        StorageLensConfigurationStorageLensConfigurationAccountLevelArgs
    ]: ...
    @account_level.setter
    def account_level(
        self,
        value: pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="awsOrg")
    def aws_org(
        self,
    ) -> Optional[
        pulumi.Input[StorageLensConfigurationStorageLensConfigurationAwsOrgArgs]
    ]: ...
    @aws_org.setter
    def aws_org(
        self,
        value: Optional[
            pulumi.Input[StorageLensConfigurationStorageLensConfigurationAwsOrgArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataExport")
    def data_export(
        self,
    ) -> Optional[
        pulumi.Input[StorageLensConfigurationStorageLensConfigurationDataExportArgs]
    ]: ...
    @data_export.setter
    def data_export(
        self,
        value: Optional[
            pulumi.Input[StorageLensConfigurationStorageLensConfigurationDataExportArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def exclude(
        self,
    ) -> Optional[
        pulumi.Input[StorageLensConfigurationStorageLensConfigurationExcludeArgs]
    ]: ...
    @exclude.setter
    def exclude(
        self,
        value: Optional[
            pulumi.Input[StorageLensConfigurationStorageLensConfigurationExcludeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def include(
        self,
    ) -> Optional[
        pulumi.Input[StorageLensConfigurationStorageLensConfigurationIncludeArgs]
    ]: ...
    @include.setter
    def include(
        self,
        value: Optional[
            pulumi.Input[StorageLensConfigurationStorageLensConfigurationIncludeArgs]
        ],
    ): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelArgsDict(TypedDict):
    bucket_level: pulumi.Input[
        StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelArgsDict
    ]
    activity_metrics: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsArgsDict
        ]
    ]
    advanced_cost_optimization_metrics: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetricsArgsDict
        ]
    ]
    advanced_data_protection_metrics: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetricsArgsDict
        ]
    ]
    detailed_status_code_metrics: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetricsArgsDict
        ]
    ]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelArgs:
    def __init__(
        __self__,
        *,
        bucket_level: pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelArgs
        ],
        activity_metrics: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsArgs
            ]
        ] = ...,
        advanced_cost_optimization_metrics: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetricsArgs
            ]
        ] = ...,
        advanced_data_protection_metrics: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetricsArgs
            ]
        ] = ...,
        detailed_status_code_metrics: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetricsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketLevel")
    def bucket_level(
        self,
    ) -> pulumi.Input[
        StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelArgs
    ]: ...
    @bucket_level.setter
    def bucket_level(
        self,
        value: pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="activityMetrics")
    def activity_metrics(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsArgs
        ]
    ]: ...
    @activity_metrics.setter
    def activity_metrics(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="advancedCostOptimizationMetrics")
    def advanced_cost_optimization_metrics(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetricsArgs
        ]
    ]: ...
    @advanced_cost_optimization_metrics.setter
    def advanced_cost_optimization_metrics(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetricsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="advancedDataProtectionMetrics")
    def advanced_data_protection_metrics(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetricsArgs
        ]
    ]: ...
    @advanced_data_protection_metrics.setter
    def advanced_data_protection_metrics(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetricsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="detailedStatusCodeMetrics")
    def detailed_status_code_metrics(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetricsArgs
        ]
    ]: ...
    @detailed_status_code_metrics.setter
    def detailed_status_code_metrics(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetricsArgs
            ]
        ],
    ): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsArgsDict(
    TypedDict
):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetricsArgsDict(
    TypedDict
):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetricsArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetricsArgsDict(
    TypedDict
):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetricsArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelArgsDict(
    TypedDict
):
    activity_metrics: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsArgsDict
        ]
    ]
    advanced_cost_optimization_metrics: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetricsArgsDict
        ]
    ]
    advanced_data_protection_metrics: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetricsArgsDict
        ]
    ]
    detailed_status_code_metrics: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetricsArgsDict
        ]
    ]
    prefix_level: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelArgsDict
        ]
    ]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelArgs:
    def __init__(
        __self__,
        *,
        activity_metrics: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsArgs
            ]
        ] = ...,
        advanced_cost_optimization_metrics: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetricsArgs
            ]
        ] = ...,
        advanced_data_protection_metrics: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetricsArgs
            ]
        ] = ...,
        detailed_status_code_metrics: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetricsArgs
            ]
        ] = ...,
        prefix_level: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activityMetrics")
    def activity_metrics(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsArgs
        ]
    ]: ...
    @activity_metrics.setter
    def activity_metrics(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="advancedCostOptimizationMetrics")
    def advanced_cost_optimization_metrics(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetricsArgs
        ]
    ]: ...
    @advanced_cost_optimization_metrics.setter
    def advanced_cost_optimization_metrics(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetricsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="advancedDataProtectionMetrics")
    def advanced_data_protection_metrics(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetricsArgs
        ]
    ]: ...
    @advanced_data_protection_metrics.setter
    def advanced_data_protection_metrics(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetricsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="detailedStatusCodeMetrics")
    def detailed_status_code_metrics(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetricsArgs
        ]
    ]: ...
    @detailed_status_code_metrics.setter
    def detailed_status_code_metrics(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetricsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="prefixLevel")
    def prefix_level(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelArgs
        ]
    ]: ...
    @prefix_level.setter
    def prefix_level(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelArgs
            ]
        ],
    ): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsArgsDict(
    TypedDict
):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetricsArgsDict(
    TypedDict
):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetricsArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetricsArgsDict(
    TypedDict
):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetricsArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetricsArgsDict(
    TypedDict
):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetricsArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelArgsDict(
    TypedDict
):
    storage_metrics: pulumi.Input[
        StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsArgsDict
    ]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelArgs:
    def __init__(
        __self__,
        *,
        storage_metrics: pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageMetrics")
    def storage_metrics(
        self,
    ) -> pulumi.Input[
        StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsArgs
    ]: ...
    @storage_metrics.setter
    def storage_metrics(
        self,
        value: pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsArgs
        ],
    ): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsArgsDict(
    TypedDict
):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    selection_criteria: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaArgsDict
        ]
    ]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        selection_criteria: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="selectionCriteria")
    def selection_criteria(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaArgs
        ]
    ]: ...
    @selection_criteria.setter
    def selection_criteria(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaArgs
            ]
        ],
    ): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaArgsDict(
    TypedDict
):
    delimiter: NotRequired[pulumi.Input[_builtins.str]]
    max_depth: NotRequired[pulumi.Input[_builtins.int]]
    min_storage_bytes_percentage: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaArgs:
    def __init__(
        __self__,
        *,
        delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        max_depth: Optional[pulumi.Input[_builtins.int]] = ...,
        min_storage_bytes_percentage: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delimiter.setter
    def delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxDepth")
    def max_depth(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_depth.setter
    def max_depth(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minStorageBytesPercentage")
    def min_storage_bytes_percentage(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min_storage_bytes_percentage.setter
    def min_storage_bytes_percentage(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class StorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetricsArgsDict(
    TypedDict
):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetricsArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class StorageLensConfigurationStorageLensConfigurationAwsOrgArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationAwsOrgArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...

class StorageLensConfigurationStorageLensConfigurationDataExportArgsDict(TypedDict):
    cloud_watch_metrics: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsArgsDict
        ]
    ]
    s3_bucket_destination: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationArgsDict
        ]
    ]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationDataExportArgs:
    def __init__(
        __self__,
        *,
        cloud_watch_metrics: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsArgs
            ]
        ] = ...,
        s3_bucket_destination: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchMetrics")
    def cloud_watch_metrics(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsArgs
        ]
    ]: ...
    @cloud_watch_metrics.setter
    def cloud_watch_metrics(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3BucketDestination")
    def s3_bucket_destination(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationArgs
        ]
    ]: ...
    @s3_bucket_destination.setter
    def s3_bucket_destination(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationArgs
            ]
        ],
    ): ...

class StorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsArgsDict(
    TypedDict
):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationArgsDict(
    TypedDict
):
    account_id: pulumi.Input[_builtins.str]
    arn: pulumi.Input[_builtins.str]
    format: pulumi.Input[_builtins.str]
    output_schema_version: pulumi.Input[_builtins.str]
    encryption: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionArgsDict
        ]
    ]
    prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationArgs:
    def __init__(
        __self__,
        *,
        account_id: pulumi.Input[_builtins.str],
        arn: pulumi.Input[_builtins.str],
        format: pulumi.Input[_builtins.str],
        output_schema_version: pulumi.Input[_builtins.str],
        encryption: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionArgs
            ]
        ] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[_builtins.str]: ...
    @account_id.setter
    def account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]: ...
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="outputSchemaVersion")
    def output_schema_version(self) -> pulumi.Input[_builtins.str]: ...
    @output_schema_version.setter
    def output_schema_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def encryption(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionArgs
        ]
    ]: ...
    @encryption.setter
    def encryption(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionArgsDict(
    TypedDict
):
    sse_kms: NotRequired[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsArgsDict
        ]
    ]
    sse_s3s: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3ArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionArgs:
    def __init__(
        __self__,
        *,
        sse_kms: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsArgs
            ]
        ] = ...,
        sse_s3s: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3Args
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sseKms")
    def sse_kms(
        self,
    ) -> Optional[
        pulumi.Input[
            StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsArgs
        ]
    ]: ...
    @sse_kms.setter
    def sse_kms(
        self,
        value: Optional[
            pulumi.Input[
                StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sseS3s")
    def sse_s3s(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3Args
                ]
            ]
        ]
    ]: ...
    @sse_s3s.setter
    def sse_s3s(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3Args
                    ]
                ]
            ]
        ],
    ): ...

class StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsArgsDict(
    TypedDict
):
    key_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsArgs:
    def __init__(__self__, *, key_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[_builtins.str]: ...
    @key_id.setter
    def key_id(self, value: pulumi.Input[_builtins.str]): ...

class StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3ArgsDict(
    TypedDict
): ...

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3Args:
    def __init__(__self__) -> None: ...

class StorageLensConfigurationStorageLensConfigurationExcludeArgsDict(TypedDict):
    buckets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationExcludeArgs:
    def __init__(
        __self__,
        *,
        buckets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def buckets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @buckets.setter
    def buckets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class StorageLensConfigurationStorageLensConfigurationIncludeArgsDict(TypedDict):
    buckets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class StorageLensConfigurationStorageLensConfigurationIncludeArgs:
    def __init__(
        __self__,
        *,
        buckets: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def buckets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @buckets.setter
    def buckets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
