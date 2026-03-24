import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessGrantAccessGrantsLocationConfiguration",
    "AccessGrantGrantee",
    "BucketLifecycleConfigurationRule",
    ...,
    "BucketLifecycleConfigurationRuleExpiration",
    "BucketLifecycleConfigurationRuleFilter",
    "DirectoryBucketAccessPointScopeScope",
    "MultiRegionAccessPointDetails",
    "MultiRegionAccessPointDetailsPublicAccessBlock",
    "MultiRegionAccessPointDetailsRegion",
    "MultiRegionAccessPointPolicyDetails",
    "ObjectLambdaAccessPointConfiguration",
    ...,
    ...,
    ...,
    "StorageLensConfigurationStorageLensConfiguration",
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
    "GetAccessPointsAccessPointResult",
    "GetAccessPointsAccessPointVpcConfigurationResult",
    "GetMultiRegionAccessPointPublicAccessBlockResult",
    "GetMultiRegionAccessPointRegionResult",
    "GetMultiRegionAccessPointsAccessPointResult",
    ...,
    "GetMultiRegionAccessPointsAccessPointRegionResult",
]

@pulumi.output_type
class AccessGrantAccessGrantsLocationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, s3_sub_prefix: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3SubPrefix")
    def s3_sub_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AccessGrantGrantee(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, grantee_identifier: _builtins.str, grantee_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="granteeIdentifier")
    def grantee_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="granteeType")
    def grantee_type(self) -> _builtins.str: ...

@pulumi.output_type
class BucketLifecycleConfigurationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        abort_incomplete_multipart_upload: Optional[
            outputs.BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload
        ] = ...,
        expiration: Optional[outputs.BucketLifecycleConfigurationRuleExpiration] = ...,
        filter: Optional[outputs.BucketLifecycleConfigurationRuleFilter] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="abortIncompleteMultipartUpload")
    def abort_incomplete_multipart_upload(
        self,
    ) -> Optional[
        outputs.BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload
    ]: ...
    @_builtins.property
    @pulumi.getter
    def expiration(
        self,
    ) -> Optional[outputs.BucketLifecycleConfigurationRuleExpiration]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[outputs.BucketLifecycleConfigurationRuleFilter]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, days_after_initiation: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysAfterInitiation")
    def days_after_initiation(self) -> _builtins.int: ...

@pulumi.output_type
class BucketLifecycleConfigurationRuleExpiration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        date: Optional[_builtins.str] = ...,
        days: Optional[_builtins.int] = ...,
        expired_object_delete_marker: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="expiredObjectDeleteMarker")
    def expired_object_delete_marker(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class BucketLifecycleConfigurationRuleFilter(dict):
    def __init__(
        __self__,
        *,
        prefix: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class DirectoryBucketAccessPointScopeScope(dict):
    def __init__(
        __self__,
        *,
        permissions: Optional[Sequence[_builtins.str]] = ...,
        prefixes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def prefixes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class MultiRegionAccessPointDetails(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        regions: Sequence[outputs.MultiRegionAccessPointDetailsRegion],
        public_access_block: Optional[
            outputs.MultiRegionAccessPointDetailsPublicAccessBlock
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Sequence[outputs.MultiRegionAccessPointDetailsRegion]: ...
    @_builtins.property
    @pulumi.getter(name="publicAccessBlock")
    def public_access_block(
        self,
    ) -> Optional[outputs.MultiRegionAccessPointDetailsPublicAccessBlock]: ...

@pulumi.output_type
class MultiRegionAccessPointDetailsPublicAccessBlock(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        block_public_acls: Optional[_builtins.bool] = ...,
        block_public_policy: Optional[_builtins.bool] = ...,
        ignore_public_acls: Optional[_builtins.bool] = ...,
        restrict_public_buckets: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicAcls")
    def block_public_acls(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ignorePublicAcls")
    def ignore_public_acls(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MultiRegionAccessPointDetailsRegion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        bucket_account_id: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MultiRegionAccessPointPolicyDetails(dict):
    def __init__(__self__, *, name: _builtins.str, policy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str: ...

@pulumi.output_type
class ObjectLambdaAccessPointConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        supporting_access_point: _builtins.str,
        transformation_configurations: Sequence[
            outputs.ObjectLambdaAccessPointConfigurationTransformationConfiguration
        ],
        allowed_features: Optional[Sequence[_builtins.str]] = ...,
        cloud_watch_metrics_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="supportingAccessPoint")
    def supporting_access_point(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transformationConfigurations")
    def transformation_configurations(
        self,
    ) -> Sequence[
        outputs.ObjectLambdaAccessPointConfigurationTransformationConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="allowedFeatures")
    def allowed_features(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchMetricsEnabled")
    def cloud_watch_metrics_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ObjectLambdaAccessPointConfigurationTransformationConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: Sequence[_builtins.str],
        content_transformation: outputs.ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentTransformation")
    def content_transformation(
        self,
    ) -> outputs.ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation: ...

@pulumi.output_type
class ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformation(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aws_lambda: outputs.ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsLambda")
    def aws_lambda(
        self,
    ) -> outputs.ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda: ...

@pulumi.output_type
class ObjectLambdaAccessPointConfigurationTransformationConfigurationContentTransformationAwsLambda(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        function_arn: _builtins.str,
        function_payload: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="functionPayload")
    def function_payload(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_level: outputs.StorageLensConfigurationStorageLensConfigurationAccountLevel,
        enabled: _builtins.bool,
        aws_org: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationAwsOrg
        ] = ...,
        data_export: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationDataExport
        ] = ...,
        exclude: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationExclude
        ] = ...,
        include: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationInclude
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountLevel")
    def account_level(
        self,
    ) -> outputs.StorageLensConfigurationStorageLensConfigurationAccountLevel: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="awsOrg")
    def aws_org(
        self,
    ) -> Optional[outputs.StorageLensConfigurationStorageLensConfigurationAwsOrg]: ...
    @_builtins.property
    @pulumi.getter(name="dataExport")
    def data_export(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationDataExport
    ]: ...
    @_builtins.property
    @pulumi.getter
    def exclude(
        self,
    ) -> Optional[outputs.StorageLensConfigurationStorageLensConfigurationExclude]: ...
    @_builtins.property
    @pulumi.getter
    def include(
        self,
    ) -> Optional[outputs.StorageLensConfigurationStorageLensConfigurationInclude]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_level: outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel,
        activity_metrics: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics
        ] = ...,
        advanced_cost_optimization_metrics: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics
        ] = ...,
        advanced_data_protection_metrics: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics
        ] = ...,
        detailed_status_code_metrics: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketLevel")
    def bucket_level(
        self,
    ) -> (
        outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel
    ): ...
    @_builtins.property
    @pulumi.getter(name="activityMetrics")
    def activity_metrics(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics
    ]: ...
    @_builtins.property
    @pulumi.getter(name="advancedCostOptimizationMetrics")
    def advanced_cost_optimization_metrics(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics
    ]: ...
    @_builtins.property
    @pulumi.getter(name="advancedDataProtectionMetrics")
    def advanced_data_protection_metrics(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics
    ]: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatusCodeMetrics")
    def detailed_status_code_metrics(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics
    ]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics(
    dict
):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics(
    dict
):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        activity_metrics: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics
        ] = ...,
        advanced_cost_optimization_metrics: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics
        ] = ...,
        advanced_data_protection_metrics: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics
        ] = ...,
        detailed_status_code_metrics: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics
        ] = ...,
        prefix_level: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activityMetrics")
    def activity_metrics(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics
    ]: ...
    @_builtins.property
    @pulumi.getter(name="advancedCostOptimizationMetrics")
    def advanced_cost_optimization_metrics(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics
    ]: ...
    @_builtins.property
    @pulumi.getter(name="advancedDataProtectionMetrics")
    def advanced_data_protection_metrics(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics
    ]: ...
    @_builtins.property
    @pulumi.getter(name="detailedStatusCodeMetrics")
    def detailed_status_code_metrics(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics
    ]: ...
    @_builtins.property
    @pulumi.getter(name="prefixLevel")
    def prefix_level(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel
    ]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics(
    dict
):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics(
    dict
):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics(
    dict
):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics(
    dict
):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_metrics: outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageMetrics")
    def storage_metrics(
        self,
    ) -> outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        selection_criteria: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="selectionCriteria")
    def selection_criteria(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria
    ]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        delimiter: Optional[_builtins.str] = ...,
        max_depth: Optional[_builtins.int] = ...,
        min_storage_bytes_percentage: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxDepth")
    def max_depth(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minStorageBytesPercentage")
    def min_storage_bytes_percentage(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics(
    dict
):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationAwsOrg(dict):
    def __init__(__self__, *, arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationDataExport(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_watch_metrics: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics
        ] = ...,
        s3_bucket_destination: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudWatchMetrics")
    def cloud_watch_metrics(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics
    ]: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketDestination")
    def s3_bucket_destination(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination
    ]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_id: _builtins.str,
        arn: _builtins.str,
        format: _builtins.str,
        output_schema_version: _builtins.str,
        encryption: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption
        ] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outputSchemaVersion")
    def output_schema_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def encryption(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption
    ]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sse_kms: Optional[
            outputs.StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms
        ] = ...,
        sse_s3s: Optional[
            Sequence[
                outputs.StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sseKms")
    def sse_kms(
        self,
    ) -> Optional[
        outputs.StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sseS3s")
    def sse_s3s(
        self,
    ) -> Optional[
        Sequence[
            outputs.StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3
        ]
    ]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, key_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationExclude(dict):
    def __init__(
        __self__,
        *,
        buckets: Optional[Sequence[_builtins.str]] = ...,
        regions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def buckets(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class StorageLensConfigurationStorageLensConfigurationInclude(dict):
    def __init__(
        __self__,
        *,
        buckets: Optional[Sequence[_builtins.str]] = ...,
        regions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def buckets(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetAccessPointsAccessPointResult(dict):
    def __init__(
        __self__,
        *,
        access_point_arn: _builtins.str,
        alias: _builtins.str,
        bucket: _builtins.str,
        bucket_account_id: _builtins.str,
        data_source_id: _builtins.str,
        data_source_type: _builtins.str,
        name: _builtins.str,
        network_origin: _builtins.str,
        vpc_configurations: Sequence[
            outputs.GetAccessPointsAccessPointVpcConfigurationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPointArn")
    def access_point_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkOrigin")
    def network_origin(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfigurations")
    def vpc_configurations(
        self,
    ) -> Sequence[outputs.GetAccessPointsAccessPointVpcConfigurationResult]: ...

@pulumi.output_type
class GetAccessPointsAccessPointVpcConfigurationResult(dict):
    def __init__(__self__, *, vpc_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetMultiRegionAccessPointPublicAccessBlockResult(dict):
    def __init__(
        __self__,
        *,
        block_public_acls: _builtins.bool,
        block_public_policy: _builtins.bool,
        ignore_public_acls: _builtins.bool,
        restrict_public_buckets: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicAcls")
    def block_public_acls(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ignorePublicAcls")
    def ignore_public_acls(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> _builtins.bool: ...

@pulumi.output_type
class GetMultiRegionAccessPointRegionResult(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        bucket_account_id: _builtins.str,
        region: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

@pulumi.output_type
class GetMultiRegionAccessPointsAccessPointResult(dict):
    def __init__(
        __self__,
        *,
        alias: _builtins.str,
        created_at: _builtins.str,
        name: _builtins.str,
        public_access_blocks: Sequence[
            outputs.GetMultiRegionAccessPointsAccessPointPublicAccessBlockResult
        ],
        regions: Sequence[outputs.GetMultiRegionAccessPointsAccessPointRegionResult],
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicAccessBlocks")
    def public_access_blocks(
        self,
    ) -> Sequence[
        outputs.GetMultiRegionAccessPointsAccessPointPublicAccessBlockResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Sequence[outputs.GetMultiRegionAccessPointsAccessPointRegionResult]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetMultiRegionAccessPointsAccessPointPublicAccessBlockResult(dict):
    def __init__(
        __self__,
        *,
        block_public_acls: _builtins.bool,
        block_public_policy: _builtins.bool,
        ignore_public_acls: _builtins.bool,
        restrict_public_buckets: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicAcls")
    def block_public_acls(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ignorePublicAcls")
    def ignore_public_acls(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> _builtins.bool: ...

@pulumi.output_type
class GetMultiRegionAccessPointsAccessPointRegionResult(dict):
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        bucket_account_id: _builtins.str,
        region: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
