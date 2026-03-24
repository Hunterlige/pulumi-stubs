import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from .. import _utilities
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessPointPublicAccessBlockConfiguration",
    "AccessPointVpcConfiguration",
    "AnalyticsConfigurationFilter",
    "AnalyticsConfigurationStorageClassAnalysis",
    ...,
    ...,
    ...,
    "BucketAbacAbacStatus",
    "BucketAclAccessControlPolicy",
    "BucketAclAccessControlPolicyGrant",
    "BucketAclAccessControlPolicyGrantGrantee",
    "BucketAclAccessControlPolicyOwner",
    "BucketAclV2AccessControlPolicy",
    "BucketAclV2AccessControlPolicyGrant",
    "BucketAclV2AccessControlPolicyGrantGrantee",
    "BucketAclV2AccessControlPolicyOwner",
    "BucketCorsConfigurationCorsRule",
    "BucketCorsConfigurationV2CorsRule",
    "BucketCorsRule",
    "BucketGrant",
    "BucketIntelligentTieringConfigurationFilter",
    "BucketIntelligentTieringConfigurationTiering",
    "BucketLifecycleConfigurationRule",
    ...,
    "BucketLifecycleConfigurationRuleExpiration",
    "BucketLifecycleConfigurationRuleFilter",
    "BucketLifecycleConfigurationRuleFilterAnd",
    "BucketLifecycleConfigurationRuleFilterTag",
    ...,
    ...,
    "BucketLifecycleConfigurationRuleTransition",
    "BucketLifecycleConfigurationTimeouts",
    "BucketLifecycleConfigurationV2Rule",
    ...,
    "BucketLifecycleConfigurationV2RuleExpiration",
    "BucketLifecycleConfigurationV2RuleFilter",
    "BucketLifecycleConfigurationV2RuleFilterAnd",
    "BucketLifecycleConfigurationV2RuleFilterTag",
    ...,
    ...,
    "BucketLifecycleConfigurationV2RuleTransition",
    "BucketLifecycleConfigurationV2Timeouts",
    "BucketLifecycleRule",
    "BucketLifecycleRuleExpiration",
    "BucketLifecycleRuleNoncurrentVersionExpiration",
    "BucketLifecycleRuleNoncurrentVersionTransition",
    "BucketLifecycleRuleTransition",
    "BucketLogging",
    "BucketLoggingTargetGrant",
    "BucketLoggingTargetGrantGrantee",
    "BucketLoggingTargetObjectKeyFormat",
    ...,
    "BucketLoggingTargetObjectKeyFormatSimplePrefix",
    "BucketLoggingV2TargetGrant",
    "BucketLoggingV2TargetGrantGrantee",
    "BucketLoggingV2TargetObjectKeyFormat",
    ...,
    "BucketLoggingV2TargetObjectKeyFormatSimplePrefix",
    "BucketMetadataConfigurationMetadataConfiguration",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "BucketMetadataConfigurationTimeouts",
    "BucketMetricFilter",
    "BucketNotificationLambdaFunction",
    "BucketNotificationQueue",
    "BucketNotificationTopic",
    "BucketObjectLockConfiguration",
    "BucketObjectLockConfigurationRule",
    "BucketObjectLockConfigurationRuleDefaultRetention",
    "BucketObjectLockConfigurationV2Rule",
    ...,
    "BucketObjectv2OverrideProvider",
    "BucketObjectv2OverrideProviderDefaultTags",
    "BucketOwnershipControlsRule",
    "BucketReplicationConfigRule",
    "BucketReplicationConfigRuleDeleteMarkerReplication",
    "BucketReplicationConfigRuleDestination",
    ...,
    ...,
    "BucketReplicationConfigRuleDestinationMetrics",
    ...,
    ...,
    ...,
    ...,
    "BucketReplicationConfigRuleFilter",
    "BucketReplicationConfigRuleFilterAnd",
    "BucketReplicationConfigRuleFilterTag",
    "BucketReplicationConfigRuleSourceSelectionCriteria",
    ...,
    ...,
    "BucketReplicationConfiguration",
    "BucketReplicationConfigurationRule",
    "BucketReplicationConfigurationRuleDestination",
    ...,
    ...,
    ...,
    "BucketReplicationConfigurationRuleFilter",
    ...,
    ...,
    "BucketServerSideEncryptionConfiguration",
    "BucketServerSideEncryptionConfigurationRule",
    ...,
    "BucketServerSideEncryptionConfigurationV2Rule",
    ...,
    "BucketV2CorsRule",
    "BucketV2Grant",
    "BucketV2LifecycleRule",
    "BucketV2LifecycleRuleExpiration",
    "BucketV2LifecycleRuleNoncurrentVersionExpiration",
    "BucketV2LifecycleRuleNoncurrentVersionTransition",
    "BucketV2LifecycleRuleTransition",
    "BucketV2Logging",
    "BucketV2ObjectLockConfiguration",
    "BucketV2ObjectLockConfigurationRule",
    ...,
    "BucketV2ReplicationConfiguration",
    "BucketV2ReplicationConfigurationRule",
    "BucketV2ReplicationConfigurationRuleDestination",
    ...,
    ...,
    ...,
    "BucketV2ReplicationConfigurationRuleFilter",
    ...,
    ...,
    "BucketV2ServerSideEncryptionConfiguration",
    "BucketV2ServerSideEncryptionConfigurationRule",
    ...,
    "BucketV2Versioning",
    "BucketV2Website",
    "BucketVersioning",
    "BucketVersioningV2VersioningConfiguration",
    "BucketVersioningVersioningConfiguration",
    "BucketWebsite",
    "BucketWebsiteConfigurationErrorDocument",
    "BucketWebsiteConfigurationIndexDocument",
    "BucketWebsiteConfigurationRedirectAllRequestsTo",
    "BucketWebsiteConfigurationRoutingRule",
    "BucketWebsiteConfigurationRoutingRuleCondition",
    "BucketWebsiteConfigurationRoutingRuleRedirect",
    "BucketWebsiteConfigurationV2ErrorDocument",
    "BucketWebsiteConfigurationV2IndexDocument",
    "BucketWebsiteConfigurationV2RedirectAllRequestsTo",
    "BucketWebsiteConfigurationV2RoutingRule",
    "BucketWebsiteConfigurationV2RoutingRuleCondition",
    "BucketWebsiteConfigurationV2RoutingRuleRedirect",
    "DirectoryBucketLocation",
    "InventoryDestination",
    "InventoryDestinationBucket",
    "InventoryDestinationBucketEncryption",
    "InventoryDestinationBucketEncryptionSseKms",
    "InventoryDestinationBucketEncryptionSseS3",
    "InventoryFilter",
    "InventorySchedule",
    "ObjectCopyGrant",
    "ObjectCopyOverrideProvider",
    "ObjectCopyOverrideProviderDefaultTags",
    "VectorsIndexEncryptionConfiguration",
    "VectorsIndexMetadataConfiguration",
    "VectorsVectorBucketEncryptionConfiguration",
    "GetAccessPointPublicAccessBlockConfigurationResult",
    "GetAccessPointVpcConfigurationResult",
    "GetBucketObjectLockConfigurationRuleResult",
    ...,
    "GetBucketReplicationConfigurationRuleResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetBucketReplicationConfigurationRuleFilterResult",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

@pulumi.output_type
class AccessPointPublicAccessBlockConfiguration(dict):
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
class AccessPointVpcConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, vpc_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

@pulumi.output_type
class AnalyticsConfigurationFilter(dict):
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
class AnalyticsConfigurationStorageClassAnalysis(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_export: outputs.AnalyticsConfigurationStorageClassAnalysisDataExport,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataExport")
    def data_export(
        self,
    ) -> outputs.AnalyticsConfigurationStorageClassAnalysisDataExport: ...

@pulumi.output_type
class AnalyticsConfigurationStorageClassAnalysisDataExport(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: outputs.AnalyticsConfigurationStorageClassAnalysisDataExportDestination,
        output_schema_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(
        self,
    ) -> outputs.AnalyticsConfigurationStorageClassAnalysisDataExportDestination: ...
    @_builtins.property
    @pulumi.getter(name="outputSchemaVersion")
    def output_schema_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AnalyticsConfigurationStorageClassAnalysisDataExportDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_bucket_destination: outputs.AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketDestination")
    def s3_bucket_destination(
        self,
    ) -> outputs.AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination: ...

@pulumi.output_type
class AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestination(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        bucket_account_id: Optional[_builtins.str] = ...,
        format: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketAbacAbacStatus(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class BucketAclAccessControlPolicy(dict):
    def __init__(
        __self__,
        *,
        owner: outputs.BucketAclAccessControlPolicyOwner,
        grants: Optional[Sequence[outputs.BucketAclAccessControlPolicyGrant]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> outputs.BucketAclAccessControlPolicyOwner: ...
    @_builtins.property
    @pulumi.getter
    def grants(
        self,
    ) -> Optional[Sequence[outputs.BucketAclAccessControlPolicyGrant]]: ...

@pulumi.output_type
class BucketAclAccessControlPolicyGrant(dict):
    def __init__(
        __self__,
        *,
        permission: _builtins.str,
        grantee: Optional[outputs.BucketAclAccessControlPolicyGrantGrantee] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> Optional[outputs.BucketAclAccessControlPolicyGrantGrantee]: ...

@pulumi.output_type
class BucketAclAccessControlPolicyGrantGrantee(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        email_address: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    @_utilities.deprecated(...)
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketAclAccessControlPolicyOwner(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, id: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    @_utilities.deprecated(...)
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketAclV2AccessControlPolicy(dict):
    def __init__(
        __self__,
        *,
        owner: outputs.BucketAclV2AccessControlPolicyOwner,
        grants: Optional[Sequence[outputs.BucketAclV2AccessControlPolicyGrant]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> outputs.BucketAclV2AccessControlPolicyOwner: ...
    @_builtins.property
    @pulumi.getter
    def grants(
        self,
    ) -> Optional[Sequence[outputs.BucketAclV2AccessControlPolicyGrant]]: ...

@pulumi.output_type
class BucketAclV2AccessControlPolicyGrant(dict):
    def __init__(
        __self__,
        *,
        permission: _builtins.str,
        grantee: Optional[outputs.BucketAclV2AccessControlPolicyGrantGrantee] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def grantee(
        self,
    ) -> Optional[outputs.BucketAclV2AccessControlPolicyGrantGrantee]: ...

@pulumi.output_type
class BucketAclV2AccessControlPolicyGrantGrantee(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        email_address: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    @_utilities.deprecated(...)
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketAclV2AccessControlPolicyOwner(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, id: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    @_utilities.deprecated(...)
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketCorsConfigurationCorsRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_methods: Sequence[_builtins.str],
        allowed_origins: Sequence[_builtins.str],
        allowed_headers: Optional[Sequence[_builtins.str]] = ...,
        expose_headers: Optional[Sequence[_builtins.str]] = ...,
        id: Optional[_builtins.str] = ...,
        max_age_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketCorsConfigurationV2CorsRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_methods: Sequence[_builtins.str],
        allowed_origins: Sequence[_builtins.str],
        allowed_headers: Optional[Sequence[_builtins.str]] = ...,
        expose_headers: Optional[Sequence[_builtins.str]] = ...,
        id: Optional[_builtins.str] = ...,
        max_age_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketCorsRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_methods: Sequence[_builtins.str],
        allowed_origins: Sequence[_builtins.str],
        allowed_headers: Optional[Sequence[_builtins.str]] = ...,
        expose_headers: Optional[Sequence[_builtins.str]] = ...,
        max_age_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketGrant(dict):
    def __init__(
        __self__,
        *,
        permissions: Sequence[_builtins.str],
        type: _builtins.str,
        id: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketIntelligentTieringConfigurationFilter(dict):
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
class BucketIntelligentTieringConfigurationTiering(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, access_tier: _builtins.str, days: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> _builtins.int: ...

@pulumi.output_type
class BucketLifecycleConfigurationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        status: _builtins.str,
        abort_incomplete_multipart_upload: Optional[
            outputs.BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload
        ] = ...,
        expiration: Optional[outputs.BucketLifecycleConfigurationRuleExpiration] = ...,
        filter: Optional[outputs.BucketLifecycleConfigurationRuleFilter] = ...,
        noncurrent_version_expiration: Optional[
            outputs.BucketLifecycleConfigurationRuleNoncurrentVersionExpiration
        ] = ...,
        noncurrent_version_transitions: Optional[
            Sequence[
                outputs.BucketLifecycleConfigurationRuleNoncurrentVersionTransition
            ]
        ] = ...,
        prefix: Optional[_builtins.str] = ...,
        transitions: Optional[
            Sequence[outputs.BucketLifecycleConfigurationRuleTransition]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
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
    @pulumi.getter(name="noncurrentVersionExpiration")
    def noncurrent_version_expiration(
        self,
    ) -> Optional[
        outputs.BucketLifecycleConfigurationRuleNoncurrentVersionExpiration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionTransitions")
    def noncurrent_version_transitions(
        self,
    ) -> Optional[
        Sequence[outputs.BucketLifecycleConfigurationRuleNoncurrentVersionTransition]
    ]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""Specify a prefix using 'filter' instead""")
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def transitions(
        self,
    ) -> Optional[Sequence[outputs.BucketLifecycleConfigurationRuleTransition]]: ...

@pulumi.output_type
class BucketLifecycleConfigurationRuleAbortIncompleteMultipartUpload(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, days_after_initiation: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysAfterInitiation")
    def days_after_initiation(self) -> Optional[_builtins.int]: ...

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
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        and_: Optional[outputs.BucketLifecycleConfigurationRuleFilterAnd] = ...,
        object_size_greater_than: Optional[_builtins.int] = ...,
        object_size_less_than: Optional[_builtins.int] = ...,
        prefix: Optional[_builtins.str] = ...,
        tag: Optional[outputs.BucketLifecycleConfigurationRuleFilterTag] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[outputs.BucketLifecycleConfigurationRuleFilterAnd]: ...
    @_builtins.property
    @pulumi.getter(name="objectSizeGreaterThan")
    def object_size_greater_than(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="objectSizeLessThan")
    def object_size_less_than(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[outputs.BucketLifecycleConfigurationRuleFilterTag]: ...

@pulumi.output_type
class BucketLifecycleConfigurationRuleFilterAnd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object_size_greater_than: Optional[_builtins.int] = ...,
        object_size_less_than: Optional[_builtins.int] = ...,
        prefix: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectSizeGreaterThan")
    def object_size_greater_than(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="objectSizeLessThan")
    def object_size_less_than(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class BucketLifecycleConfigurationRuleFilterTag(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class BucketLifecycleConfigurationRuleNoncurrentVersionExpiration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        noncurrent_days: _builtins.int,
        newer_noncurrent_versions: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="noncurrentDays")
    def noncurrent_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="newerNoncurrentVersions")
    def newer_noncurrent_versions(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketLifecycleConfigurationRuleNoncurrentVersionTransition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        noncurrent_days: _builtins.int,
        storage_class: _builtins.str,
        newer_noncurrent_versions: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="noncurrentDays")
    def noncurrent_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="newerNoncurrentVersions")
    def newer_noncurrent_versions(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketLifecycleConfigurationRuleTransition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_class: _builtins.str,
        date: Optional[_builtins.str] = ...,
        days: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketLifecycleConfigurationTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketLifecycleConfigurationV2Rule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        status: _builtins.str,
        abort_incomplete_multipart_upload: Optional[
            outputs.BucketLifecycleConfigurationV2RuleAbortIncompleteMultipartUpload
        ] = ...,
        expiration: Optional[
            outputs.BucketLifecycleConfigurationV2RuleExpiration
        ] = ...,
        filter: Optional[outputs.BucketLifecycleConfigurationV2RuleFilter] = ...,
        noncurrent_version_expiration: Optional[
            outputs.BucketLifecycleConfigurationV2RuleNoncurrentVersionExpiration
        ] = ...,
        noncurrent_version_transitions: Optional[
            Sequence[
                outputs.BucketLifecycleConfigurationV2RuleNoncurrentVersionTransition
            ]
        ] = ...,
        prefix: Optional[_builtins.str] = ...,
        transitions: Optional[
            Sequence[outputs.BucketLifecycleConfigurationV2RuleTransition]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="abortIncompleteMultipartUpload")
    def abort_incomplete_multipart_upload(
        self,
    ) -> Optional[
        outputs.BucketLifecycleConfigurationV2RuleAbortIncompleteMultipartUpload
    ]: ...
    @_builtins.property
    @pulumi.getter
    def expiration(
        self,
    ) -> Optional[outputs.BucketLifecycleConfigurationV2RuleExpiration]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[outputs.BucketLifecycleConfigurationV2RuleFilter]: ...
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionExpiration")
    def noncurrent_version_expiration(
        self,
    ) -> Optional[
        outputs.BucketLifecycleConfigurationV2RuleNoncurrentVersionExpiration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionTransitions")
    def noncurrent_version_transitions(
        self,
    ) -> Optional[
        Sequence[outputs.BucketLifecycleConfigurationV2RuleNoncurrentVersionTransition]
    ]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""Specify a prefix using 'filter' instead""")
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def transitions(
        self,
    ) -> Optional[Sequence[outputs.BucketLifecycleConfigurationV2RuleTransition]]: ...

@pulumi.output_type
class BucketLifecycleConfigurationV2RuleAbortIncompleteMultipartUpload(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, days_after_initiation: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysAfterInitiation")
    def days_after_initiation(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketLifecycleConfigurationV2RuleExpiration(dict):
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
class BucketLifecycleConfigurationV2RuleFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        and_: Optional[outputs.BucketLifecycleConfigurationV2RuleFilterAnd] = ...,
        object_size_greater_than: Optional[_builtins.int] = ...,
        object_size_less_than: Optional[_builtins.int] = ...,
        prefix: Optional[_builtins.str] = ...,
        tag: Optional[outputs.BucketLifecycleConfigurationV2RuleFilterTag] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[outputs.BucketLifecycleConfigurationV2RuleFilterAnd]: ...
    @_builtins.property
    @pulumi.getter(name="objectSizeGreaterThan")
    def object_size_greater_than(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="objectSizeLessThan")
    def object_size_less_than(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[outputs.BucketLifecycleConfigurationV2RuleFilterTag]: ...

@pulumi.output_type
class BucketLifecycleConfigurationV2RuleFilterAnd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object_size_greater_than: Optional[_builtins.int] = ...,
        object_size_less_than: Optional[_builtins.int] = ...,
        prefix: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectSizeGreaterThan")
    def object_size_greater_than(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="objectSizeLessThan")
    def object_size_less_than(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class BucketLifecycleConfigurationV2RuleFilterTag(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class BucketLifecycleConfigurationV2RuleNoncurrentVersionExpiration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        noncurrent_days: _builtins.int,
        newer_noncurrent_versions: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="noncurrentDays")
    def noncurrent_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="newerNoncurrentVersions")
    def newer_noncurrent_versions(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketLifecycleConfigurationV2RuleNoncurrentVersionTransition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        noncurrent_days: _builtins.int,
        storage_class: _builtins.str,
        newer_noncurrent_versions: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="noncurrentDays")
    def noncurrent_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="newerNoncurrentVersions")
    def newer_noncurrent_versions(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketLifecycleConfigurationV2RuleTransition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_class: _builtins.str,
        date: Optional[_builtins.str] = ...,
        days: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketLifecycleConfigurationV2Timeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketLifecycleRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        abort_incomplete_multipart_upload_days: Optional[_builtins.int] = ...,
        expiration: Optional[outputs.BucketLifecycleRuleExpiration] = ...,
        id: Optional[_builtins.str] = ...,
        noncurrent_version_expiration: Optional[
            outputs.BucketLifecycleRuleNoncurrentVersionExpiration
        ] = ...,
        noncurrent_version_transitions: Optional[
            Sequence[outputs.BucketLifecycleRuleNoncurrentVersionTransition]
        ] = ...,
        prefix: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        transitions: Optional[Sequence[outputs.BucketLifecycleRuleTransition]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="abortIncompleteMultipartUploadDays")
    def abort_incomplete_multipart_upload_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[outputs.BucketLifecycleRuleExpiration]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionExpiration")
    def noncurrent_version_expiration(
        self,
    ) -> Optional[outputs.BucketLifecycleRuleNoncurrentVersionExpiration]: ...
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionTransitions")
    def noncurrent_version_transitions(
        self,
    ) -> Optional[Sequence[outputs.BucketLifecycleRuleNoncurrentVersionTransition]]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def transitions(
        self,
    ) -> Optional[Sequence[outputs.BucketLifecycleRuleTransition]]: ...

@pulumi.output_type
class BucketLifecycleRuleExpiration(dict):
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
class BucketLifecycleRuleNoncurrentVersionExpiration(dict):
    def __init__(__self__, *, days: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketLifecycleRuleNoncurrentVersionTransition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, storage_class: _builtins.str, days: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketLifecycleRuleTransition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_class: _builtins.str,
        date: Optional[_builtins.str] = ...,
        days: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketLogging(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_bucket: _builtins.str,
        target_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetBucket")
    def target_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetPrefix")
    def target_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketLoggingTargetGrant(dict):
    def __init__(
        __self__,
        *,
        grantee: outputs.BucketLoggingTargetGrantGrantee,
        permission: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> outputs.BucketLoggingTargetGrantGrantee: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> _builtins.str: ...

@pulumi.output_type
class BucketLoggingTargetGrantGrantee(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        email_address: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    @_utilities.deprecated(...)
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketLoggingTargetObjectKeyFormat(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        partitioned_prefix: Optional[
            outputs.BucketLoggingTargetObjectKeyFormatPartitionedPrefix
        ] = ...,
        simple_prefix: Optional[
            outputs.BucketLoggingTargetObjectKeyFormatSimplePrefix
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionedPrefix")
    def partitioned_prefix(
        self,
    ) -> Optional[outputs.BucketLoggingTargetObjectKeyFormatPartitionedPrefix]: ...
    @_builtins.property
    @pulumi.getter(name="simplePrefix")
    def simple_prefix(
        self,
    ) -> Optional[outputs.BucketLoggingTargetObjectKeyFormatSimplePrefix]: ...

@pulumi.output_type
class BucketLoggingTargetObjectKeyFormatPartitionedPrefix(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, partition_date_source: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionDateSource")
    def partition_date_source(self) -> _builtins.str: ...

@pulumi.output_type
class BucketLoggingTargetObjectKeyFormatSimplePrefix(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class BucketLoggingV2TargetGrant(dict):
    def __init__(
        __self__,
        *,
        grantee: outputs.BucketLoggingV2TargetGrantGrantee,
        permission: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> outputs.BucketLoggingV2TargetGrantGrantee: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> _builtins.str: ...

@pulumi.output_type
class BucketLoggingV2TargetGrantGrantee(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        display_name: Optional[_builtins.str] = ...,
        email_address: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    @_utilities.deprecated(...)
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketLoggingV2TargetObjectKeyFormat(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        partitioned_prefix: Optional[
            outputs.BucketLoggingV2TargetObjectKeyFormatPartitionedPrefix
        ] = ...,
        simple_prefix: Optional[
            outputs.BucketLoggingV2TargetObjectKeyFormatSimplePrefix
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionedPrefix")
    def partitioned_prefix(
        self,
    ) -> Optional[outputs.BucketLoggingV2TargetObjectKeyFormatPartitionedPrefix]: ...
    @_builtins.property
    @pulumi.getter(name="simplePrefix")
    def simple_prefix(
        self,
    ) -> Optional[outputs.BucketLoggingV2TargetObjectKeyFormatSimplePrefix]: ...

@pulumi.output_type
class BucketLoggingV2TargetObjectKeyFormatPartitionedPrefix(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, partition_date_source: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partitionDateSource")
    def partition_date_source(self) -> _builtins.str: ...

@pulumi.output_type
class BucketLoggingV2TargetObjectKeyFormatSimplePrefix(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class BucketMetadataConfigurationMetadataConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        inventory_table_configuration: outputs.BucketMetadataConfigurationMetadataConfigurationInventoryTableConfiguration,
        journal_table_configuration: outputs.BucketMetadataConfigurationMetadataConfigurationJournalTableConfiguration,
        destinations: Optional[
            Sequence[
                outputs.BucketMetadataConfigurationMetadataConfigurationDestination
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inventoryTableConfiguration")
    def inventory_table_configuration(
        self,
    ) -> outputs.BucketMetadataConfigurationMetadataConfigurationInventoryTableConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="journalTableConfiguration")
    def journal_table_configuration(
        self,
    ) -> outputs.BucketMetadataConfigurationMetadataConfigurationJournalTableConfiguration: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        Sequence[outputs.BucketMetadataConfigurationMetadataConfigurationDestination]
    ]: ...

@pulumi.output_type
class BucketMetadataConfigurationMetadataConfigurationDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        table_bucket_arn: _builtins.str,
        table_bucket_type: _builtins.str,
        table_namespace: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableBucketType")
    def table_bucket_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableNamespace")
    def table_namespace(self) -> _builtins.str: ...

@pulumi.output_type
class BucketMetadataConfigurationMetadataConfigurationInventoryTableConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configuration_state: _builtins.str,
        encryption_configuration: Optional[
            outputs.BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationEncryptionConfiguration
        ] = ...,
        table_arn: Optional[_builtins.str] = ...,
        table_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[
        outputs.BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationEncryptionConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationEncryptionConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sse_algorithm: _builtins.str,
        kms_key_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketMetadataConfigurationMetadataConfigurationJournalTableConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        record_expiration: outputs.BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationRecordExpiration,
        encryption_configuration: Optional[
            outputs.BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationEncryptionConfiguration
        ] = ...,
        table_arn: Optional[_builtins.str] = ...,
        table_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recordExpiration")
    def record_expiration(
        self,
    ) -> outputs.BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationRecordExpiration: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[
        outputs.BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationEncryptionConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationEncryptionConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sse_algorithm: _builtins.str,
        kms_key_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationRecordExpiration(
    dict
):
    def __init__(
        __self__, *, expiration: _builtins.str, days: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketMetadataConfigurationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketMetricFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_point: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPoint")
    def access_point(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class BucketNotificationLambdaFunction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        events: Sequence[_builtins.str],
        filter_prefix: Optional[_builtins.str] = ...,
        filter_suffix: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        lambda_function_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filterPrefix")
    def filter_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filterSuffix")
    def filter_suffix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketNotificationQueue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        events: Sequence[_builtins.str],
        queue_arn: _builtins.str,
        filter_prefix: Optional[_builtins.str] = ...,
        filter_suffix: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queueArn")
    def queue_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterPrefix")
    def filter_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filterSuffix")
    def filter_suffix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketNotificationTopic(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        events: Sequence[_builtins.str],
        topic_arn: _builtins.str,
        filter_prefix: Optional[_builtins.str] = ...,
        filter_suffix: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterPrefix")
    def filter_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filterSuffix")
    def filter_suffix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketObjectLockConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object_lock_enabled: Optional[_builtins.str] = ...,
        rule: Optional[outputs.BucketObjectLockConfigurationRule] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectLockEnabled")
    @_utilities.deprecated(...)
    def object_lock_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def rule(self) -> Optional[outputs.BucketObjectLockConfigurationRule]: ...

@pulumi.output_type
class BucketObjectLockConfigurationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_retention: outputs.BucketObjectLockConfigurationRuleDefaultRetention,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultRetention")
    def default_retention(
        self,
    ) -> outputs.BucketObjectLockConfigurationRuleDefaultRetention: ...

@pulumi.output_type
class BucketObjectLockConfigurationRuleDefaultRetention(dict):
    def __init__(
        __self__,
        *,
        days: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
        years: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def years(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketObjectLockConfigurationV2Rule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_retention: outputs.BucketObjectLockConfigurationV2RuleDefaultRetention,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultRetention")
    def default_retention(
        self,
    ) -> outputs.BucketObjectLockConfigurationV2RuleDefaultRetention: ...

@pulumi.output_type
class BucketObjectLockConfigurationV2RuleDefaultRetention(dict):
    def __init__(
        __self__,
        *,
        days: Optional[_builtins.int] = ...,
        mode: Optional[_builtins.str] = ...,
        years: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def years(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketObjectv2OverrideProvider(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_tags: Optional[outputs.BucketObjectv2OverrideProviderDefaultTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultTags")
    def default_tags(
        self,
    ) -> Optional[outputs.BucketObjectv2OverrideProviderDefaultTags]: ...

@pulumi.output_type
class BucketObjectv2OverrideProviderDefaultTags(dict):
    def __init__(
        __self__, *, tags: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class BucketOwnershipControlsRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_ownership: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectOwnership")
    def object_ownership(self) -> _builtins.str: ...

@pulumi.output_type
class BucketReplicationConfigRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: outputs.BucketReplicationConfigRuleDestination,
        status: _builtins.str,
        delete_marker_replication: Optional[
            outputs.BucketReplicationConfigRuleDeleteMarkerReplication
        ] = ...,
        existing_object_replication: Optional[
            outputs.BucketReplicationConfigRuleExistingObjectReplication
        ] = ...,
        filter: Optional[outputs.BucketReplicationConfigRuleFilter] = ...,
        id: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
        priority: Optional[_builtins.int] = ...,
        source_selection_criteria: Optional[
            outputs.BucketReplicationConfigRuleSourceSelectionCriteria
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> outputs.BucketReplicationConfigRuleDestination: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deleteMarkerReplication")
    def delete_marker_replication(
        self,
    ) -> Optional[outputs.BucketReplicationConfigRuleDeleteMarkerReplication]: ...
    @_builtins.property
    @pulumi.getter(name="existingObjectReplication")
    def existing_object_replication(
        self,
    ) -> Optional[outputs.BucketReplicationConfigRuleExistingObjectReplication]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[outputs.BucketReplicationConfigRuleFilter]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""prefix is deprecated. Use filter instead.""")
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sourceSelectionCriteria")
    def source_selection_criteria(
        self,
    ) -> Optional[outputs.BucketReplicationConfigRuleSourceSelectionCriteria]: ...

@pulumi.output_type
class BucketReplicationConfigRuleDeleteMarkerReplication(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class BucketReplicationConfigRuleDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        access_control_translation: Optional[
            outputs.BucketReplicationConfigRuleDestinationAccessControlTranslation
        ] = ...,
        account: Optional[_builtins.str] = ...,
        encryption_configuration: Optional[
            outputs.BucketReplicationConfigRuleDestinationEncryptionConfiguration
        ] = ...,
        metrics: Optional[outputs.BucketReplicationConfigRuleDestinationMetrics] = ...,
        replication_time: Optional[
            outputs.BucketReplicationConfigRuleDestinationReplicationTime
        ] = ...,
        storage_class: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessControlTranslation")
    def access_control_translation(
        self,
    ) -> Optional[
        outputs.BucketReplicationConfigRuleDestinationAccessControlTranslation
    ]: ...
    @_builtins.property
    @pulumi.getter
    def account(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> Optional[
        outputs.BucketReplicationConfigRuleDestinationEncryptionConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter
    def metrics(
        self,
    ) -> Optional[outputs.BucketReplicationConfigRuleDestinationMetrics]: ...
    @_builtins.property
    @pulumi.getter(name="replicationTime")
    def replication_time(
        self,
    ) -> Optional[outputs.BucketReplicationConfigRuleDestinationReplicationTime]: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketReplicationConfigRuleDestinationAccessControlTranslation(dict):
    def __init__(__self__, *, owner: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...

@pulumi.output_type
class BucketReplicationConfigRuleDestinationEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, replica_kms_key_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replicaKmsKeyId")
    def replica_kms_key_id(self) -> _builtins.str: ...

@pulumi.output_type
class BucketReplicationConfigRuleDestinationMetrics(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        status: _builtins.str,
        event_threshold: Optional[
            outputs.BucketReplicationConfigRuleDestinationMetricsEventThreshold
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eventThreshold")
    def event_threshold(
        self,
    ) -> Optional[
        outputs.BucketReplicationConfigRuleDestinationMetricsEventThreshold
    ]: ...

@pulumi.output_type
class BucketReplicationConfigRuleDestinationMetricsEventThreshold(dict):
    def __init__(__self__, *, minutes: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...

@pulumi.output_type
class BucketReplicationConfigRuleDestinationReplicationTime(dict):
    def __init__(
        __self__,
        *,
        status: _builtins.str,
        time: outputs.BucketReplicationConfigRuleDestinationReplicationTimeTime,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def time(
        self,
    ) -> outputs.BucketReplicationConfigRuleDestinationReplicationTimeTime: ...

@pulumi.output_type
class BucketReplicationConfigRuleDestinationReplicationTimeTime(dict):
    def __init__(__self__, *, minutes: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...

@pulumi.output_type
class BucketReplicationConfigRuleExistingObjectReplication(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class BucketReplicationConfigRuleFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        and_: Optional[outputs.BucketReplicationConfigRuleFilterAnd] = ...,
        prefix: Optional[_builtins.str] = ...,
        tag: Optional[outputs.BucketReplicationConfigRuleFilterTag] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[outputs.BucketReplicationConfigRuleFilterAnd]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[outputs.BucketReplicationConfigRuleFilterTag]: ...

@pulumi.output_type
class BucketReplicationConfigRuleFilterAnd(dict):
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
class BucketReplicationConfigRuleFilterTag(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class BucketReplicationConfigRuleSourceSelectionCriteria(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        replica_modifications: Optional[
            outputs.BucketReplicationConfigRuleSourceSelectionCriteriaReplicaModifications
        ] = ...,
        sse_kms_encrypted_objects: Optional[
            outputs.BucketReplicationConfigRuleSourceSelectionCriteriaSseKmsEncryptedObjects
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replicaModifications")
    def replica_modifications(
        self,
    ) -> Optional[
        outputs.BucketReplicationConfigRuleSourceSelectionCriteriaReplicaModifications
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sseKmsEncryptedObjects")
    def sse_kms_encrypted_objects(
        self,
    ) -> Optional[
        outputs.BucketReplicationConfigRuleSourceSelectionCriteriaSseKmsEncryptedObjects
    ]: ...

@pulumi.output_type
class BucketReplicationConfigRuleSourceSelectionCriteriaReplicaModifications(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class BucketReplicationConfigRuleSourceSelectionCriteriaSseKmsEncryptedObjects(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class BucketReplicationConfiguration(dict):
    def __init__(
        __self__,
        *,
        role: _builtins.str,
        rules: Sequence[outputs.BucketReplicationConfigurationRule],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.BucketReplicationConfigurationRule]: ...

@pulumi.output_type
class BucketReplicationConfigurationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: outputs.BucketReplicationConfigurationRuleDestination,
        status: _builtins.str,
        delete_marker_replication_status: Optional[_builtins.str] = ...,
        filter: Optional[outputs.BucketReplicationConfigurationRuleFilter] = ...,
        id: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
        priority: Optional[_builtins.int] = ...,
        source_selection_criteria: Optional[
            outputs.BucketReplicationConfigurationRuleSourceSelectionCriteria
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> outputs.BucketReplicationConfigurationRuleDestination: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deleteMarkerReplicationStatus")
    def delete_marker_replication_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[outputs.BucketReplicationConfigurationRuleFilter]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sourceSelectionCriteria")
    def source_selection_criteria(
        self,
    ) -> Optional[
        outputs.BucketReplicationConfigurationRuleSourceSelectionCriteria
    ]: ...

@pulumi.output_type
class BucketReplicationConfigurationRuleDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        access_control_translation: Optional[
            outputs.BucketReplicationConfigurationRuleDestinationAccessControlTranslation
        ] = ...,
        account_id: Optional[_builtins.str] = ...,
        metrics: Optional[
            outputs.BucketReplicationConfigurationRuleDestinationMetrics
        ] = ...,
        replica_kms_key_id: Optional[_builtins.str] = ...,
        replication_time: Optional[
            outputs.BucketReplicationConfigurationRuleDestinationReplicationTime
        ] = ...,
        storage_class: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessControlTranslation")
    def access_control_translation(
        self,
    ) -> Optional[
        outputs.BucketReplicationConfigurationRuleDestinationAccessControlTranslation
    ]: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metrics(
        self,
    ) -> Optional[outputs.BucketReplicationConfigurationRuleDestinationMetrics]: ...
    @_builtins.property
    @pulumi.getter(name="replicaKmsKeyId")
    def replica_kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationTime")
    def replication_time(
        self,
    ) -> Optional[
        outputs.BucketReplicationConfigurationRuleDestinationReplicationTime
    ]: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketReplicationConfigurationRuleDestinationAccessControlTranslation(dict):
    def __init__(__self__, *, owner: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...

@pulumi.output_type
class BucketReplicationConfigurationRuleDestinationMetrics(dict):
    def __init__(
        __self__,
        *,
        minutes: Optional[_builtins.int] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketReplicationConfigurationRuleDestinationReplicationTime(dict):
    def __init__(
        __self__,
        *,
        minutes: Optional[_builtins.int] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketReplicationConfigurationRuleFilter(dict):
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
class BucketReplicationConfigurationRuleSourceSelectionCriteria(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sse_kms_encrypted_objects: Optional[
            outputs.BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sseKmsEncryptedObjects")
    def sse_kms_encrypted_objects(
        self,
    ) -> Optional[
        outputs.BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects
    ]: ...

@pulumi.output_type
class BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjects(
    dict
):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class BucketServerSideEncryptionConfiguration(dict):
    def __init__(
        __self__, *, rule: outputs.BucketServerSideEncryptionConfigurationRule
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rule(self) -> outputs.BucketServerSideEncryptionConfigurationRule: ...

@pulumi.output_type
class BucketServerSideEncryptionConfigurationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        apply_server_side_encryption_by_default: Optional[
            outputs.BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault
        ] = ...,
        blocked_encryption_types: Optional[Sequence[_builtins.str]] = ...,
        bucket_key_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyServerSideEncryptionByDefault")
    def apply_server_side_encryption_by_default(
        self,
    ) -> Optional[
        outputs.BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault
    ]: ...
    @_builtins.property
    @pulumi.getter(name="blockedEncryptionTypes")
    def blocked_encryption_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sse_algorithm: _builtins.str,
        kms_master_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketServerSideEncryptionConfigurationV2Rule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        apply_server_side_encryption_by_default: Optional[
            outputs.BucketServerSideEncryptionConfigurationV2RuleApplyServerSideEncryptionByDefault
        ] = ...,
        blocked_encryption_types: Optional[Sequence[_builtins.str]] = ...,
        bucket_key_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyServerSideEncryptionByDefault")
    def apply_server_side_encryption_by_default(
        self,
    ) -> Optional[
        outputs.BucketServerSideEncryptionConfigurationV2RuleApplyServerSideEncryptionByDefault
    ]: ...
    @_builtins.property
    @pulumi.getter(name="blockedEncryptionTypes")
    def blocked_encryption_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class BucketServerSideEncryptionConfigurationV2RuleApplyServerSideEncryptionByDefault(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sse_algorithm: _builtins.str,
        kms_master_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketV2CorsRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_methods: Sequence[_builtins.str],
        allowed_origins: Sequence[_builtins.str],
        allowed_headers: Optional[Sequence[_builtins.str]] = ...,
        expose_headers: Optional[Sequence[_builtins.str]] = ...,
        max_age_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketV2Grant(dict):
    def __init__(
        __self__,
        *,
        permissions: Sequence[_builtins.str],
        type: _builtins.str,
        id: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketV2LifecycleRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        abort_incomplete_multipart_upload_days: Optional[_builtins.int] = ...,
        expirations: Optional[Sequence[outputs.BucketV2LifecycleRuleExpiration]] = ...,
        id: Optional[_builtins.str] = ...,
        noncurrent_version_expirations: Optional[
            Sequence[outputs.BucketV2LifecycleRuleNoncurrentVersionExpiration]
        ] = ...,
        noncurrent_version_transitions: Optional[
            Sequence[outputs.BucketV2LifecycleRuleNoncurrentVersionTransition]
        ] = ...,
        prefix: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        transitions: Optional[Sequence[outputs.BucketV2LifecycleRuleTransition]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="abortIncompleteMultipartUploadDays")
    def abort_incomplete_multipart_upload_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def expirations(
        self,
    ) -> Optional[Sequence[outputs.BucketV2LifecycleRuleExpiration]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionExpirations")
    def noncurrent_version_expirations(
        self,
    ) -> Optional[
        Sequence[outputs.BucketV2LifecycleRuleNoncurrentVersionExpiration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionTransitions")
    def noncurrent_version_transitions(
        self,
    ) -> Optional[
        Sequence[outputs.BucketV2LifecycleRuleNoncurrentVersionTransition]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def transitions(
        self,
    ) -> Optional[Sequence[outputs.BucketV2LifecycleRuleTransition]]: ...

@pulumi.output_type
class BucketV2LifecycleRuleExpiration(dict):
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
class BucketV2LifecycleRuleNoncurrentVersionExpiration(dict):
    def __init__(__self__, *, days: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketV2LifecycleRuleNoncurrentVersionTransition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, storage_class: _builtins.str, days: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketV2LifecycleRuleTransition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_class: _builtins.str,
        date: Optional[_builtins.str] = ...,
        days: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketV2Logging(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_bucket: _builtins.str,
        target_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetBucket")
    def target_bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetPrefix")
    def target_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketV2ObjectLockConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object_lock_enabled: Optional[_builtins.str] = ...,
        rules: Optional[Sequence[outputs.BucketV2ObjectLockConfigurationRule]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectLockEnabled")
    @_utilities.deprecated(...)
    def object_lock_enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def rules(
        self,
    ) -> Optional[Sequence[outputs.BucketV2ObjectLockConfigurationRule]]: ...

@pulumi.output_type
class BucketV2ObjectLockConfigurationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_retentions: Sequence[
            outputs.BucketV2ObjectLockConfigurationRuleDefaultRetention
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultRetentions")
    def default_retentions(
        self,
    ) -> Sequence[outputs.BucketV2ObjectLockConfigurationRuleDefaultRetention]: ...

@pulumi.output_type
class BucketV2ObjectLockConfigurationRuleDefaultRetention(dict):
    def __init__(
        __self__,
        *,
        mode: _builtins.str,
        days: Optional[_builtins.int] = ...,
        years: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def years(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class BucketV2ReplicationConfiguration(dict):
    def __init__(
        __self__,
        *,
        role: _builtins.str,
        rules: Sequence[outputs.BucketV2ReplicationConfigurationRule],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.BucketV2ReplicationConfigurationRule]: ...

@pulumi.output_type
class BucketV2ReplicationConfigurationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destinations: Sequence[outputs.BucketV2ReplicationConfigurationRuleDestination],
        status: _builtins.str,
        delete_marker_replication_status: Optional[_builtins.str] = ...,
        filters: Optional[
            Sequence[outputs.BucketV2ReplicationConfigurationRuleFilter]
        ] = ...,
        id: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
        priority: Optional[_builtins.int] = ...,
        source_selection_criterias: Optional[
            Sequence[
                outputs.BucketV2ReplicationConfigurationRuleSourceSelectionCriteria
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Sequence[outputs.BucketV2ReplicationConfigurationRuleDestination]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deleteMarkerReplicationStatus")
    def delete_marker_replication_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.BucketV2ReplicationConfigurationRuleFilter]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sourceSelectionCriterias")
    def source_selection_criterias(
        self,
    ) -> Optional[
        Sequence[outputs.BucketV2ReplicationConfigurationRuleSourceSelectionCriteria]
    ]: ...

@pulumi.output_type
class BucketV2ReplicationConfigurationRuleDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        access_control_translations: Optional[
            Sequence[
                outputs.BucketV2ReplicationConfigurationRuleDestinationAccessControlTranslation
            ]
        ] = ...,
        account_id: Optional[_builtins.str] = ...,
        metrics: Optional[
            Sequence[outputs.BucketV2ReplicationConfigurationRuleDestinationMetric]
        ] = ...,
        replica_kms_key_id: Optional[_builtins.str] = ...,
        replication_times: Optional[
            Sequence[
                outputs.BucketV2ReplicationConfigurationRuleDestinationReplicationTime
            ]
        ] = ...,
        storage_class: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessControlTranslations")
    def access_control_translations(
        self,
    ) -> Optional[
        Sequence[
            outputs.BucketV2ReplicationConfigurationRuleDestinationAccessControlTranslation
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metrics(
        self,
    ) -> Optional[
        Sequence[outputs.BucketV2ReplicationConfigurationRuleDestinationMetric]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="replicaKmsKeyId")
    def replica_kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationTimes")
    def replication_times(
        self,
    ) -> Optional[
        Sequence[outputs.BucketV2ReplicationConfigurationRuleDestinationReplicationTime]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketV2ReplicationConfigurationRuleDestinationAccessControlTranslation(dict):
    def __init__(__self__, *, owner: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...

@pulumi.output_type
class BucketV2ReplicationConfigurationRuleDestinationMetric(dict):
    def __init__(
        __self__,
        *,
        minutes: Optional[_builtins.int] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketV2ReplicationConfigurationRuleDestinationReplicationTime(dict):
    def __init__(
        __self__,
        *,
        minutes: Optional[_builtins.int] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketV2ReplicationConfigurationRuleFilter(dict):
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
class BucketV2ReplicationConfigurationRuleSourceSelectionCriteria(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sse_kms_encrypted_objects: Optional[
            Sequence[
                outputs.BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObject
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sseKmsEncryptedObjects")
    def sse_kms_encrypted_objects(
        self,
    ) -> Optional[
        Sequence[
            outputs.BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObject
        ]
    ]: ...

@pulumi.output_type
class BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObject(
    dict
):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class BucketV2ServerSideEncryptionConfiguration(dict):
    def __init__(
        __self__,
        *,
        rules: Sequence[outputs.BucketV2ServerSideEncryptionConfigurationRule],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Sequence[outputs.BucketV2ServerSideEncryptionConfigurationRule]: ...

@pulumi.output_type
class BucketV2ServerSideEncryptionConfigurationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        apply_server_side_encryption_by_defaults: Sequence[
            outputs.BucketV2ServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault
        ],
        bucket_key_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyServerSideEncryptionByDefaults")
    def apply_server_side_encryption_by_defaults(
        self,
    ) -> Sequence[
        outputs.BucketV2ServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault
    ]: ...
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class BucketV2ServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefault(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sse_algorithm: _builtins.str,
        kms_master_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketV2Versioning(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        mfa_delete: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="mfaDelete")
    def mfa_delete(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class BucketV2Website(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_document: Optional[_builtins.str] = ...,
        index_document: Optional[_builtins.str] = ...,
        redirect_all_requests_to: Optional[_builtins.str] = ...,
        routing_rules: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorDocument")
    def error_document(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="indexDocument")
    def index_document(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketVersioning(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        mfa_delete: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="mfaDelete")
    def mfa_delete(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class BucketVersioningV2VersioningConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, status: _builtins.str, mfa_delete: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mfaDelete")
    def mfa_delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketVersioningVersioningConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, status: _builtins.str, mfa_delete: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mfaDelete")
    def mfa_delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketWebsite(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_document: Optional[_builtins.str] = ...,
        index_document: Optional[_builtins.str] = ...,
        redirect_all_requests_to: Optional[_builtins.str] = ...,
        routing_rules: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorDocument")
    def error_document(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="indexDocument")
    def index_document(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketWebsiteConfigurationErrorDocument(dict):
    def __init__(__self__, *, key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...

@pulumi.output_type
class BucketWebsiteConfigurationIndexDocument(dict):
    def __init__(__self__, *, suffix: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> _builtins.str: ...

@pulumi.output_type
class BucketWebsiteConfigurationRedirectAllRequestsTo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, host_name: _builtins.str, protocol: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketWebsiteConfigurationRoutingRule(dict):
    def __init__(
        __self__,
        *,
        redirect: outputs.BucketWebsiteConfigurationRoutingRuleRedirect,
        condition: Optional[
            outputs.BucketWebsiteConfigurationRoutingRuleCondition
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def redirect(self) -> outputs.BucketWebsiteConfigurationRoutingRuleRedirect: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[outputs.BucketWebsiteConfigurationRoutingRuleCondition]: ...

@pulumi.output_type
class BucketWebsiteConfigurationRoutingRuleCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        http_error_code_returned_equals: Optional[_builtins.str] = ...,
        key_prefix_equals: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpErrorCodeReturnedEquals")
    def http_error_code_returned_equals(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyPrefixEquals")
    def key_prefix_equals(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketWebsiteConfigurationRoutingRuleRedirect(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_name: Optional[_builtins.str] = ...,
        http_redirect_code: Optional[_builtins.str] = ...,
        protocol: Optional[_builtins.str] = ...,
        replace_key_prefix_with: Optional[_builtins.str] = ...,
        replace_key_with: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpRedirectCode")
    def http_redirect_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replaceKeyPrefixWith")
    def replace_key_prefix_with(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replaceKeyWith")
    def replace_key_with(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketWebsiteConfigurationV2ErrorDocument(dict):
    def __init__(__self__, *, key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...

@pulumi.output_type
class BucketWebsiteConfigurationV2IndexDocument(dict):
    def __init__(__self__, *, suffix: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> _builtins.str: ...

@pulumi.output_type
class BucketWebsiteConfigurationV2RedirectAllRequestsTo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, host_name: _builtins.str, protocol: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketWebsiteConfigurationV2RoutingRule(dict):
    def __init__(
        __self__,
        *,
        redirect: outputs.BucketWebsiteConfigurationV2RoutingRuleRedirect,
        condition: Optional[
            outputs.BucketWebsiteConfigurationV2RoutingRuleCondition
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def redirect(self) -> outputs.BucketWebsiteConfigurationV2RoutingRuleRedirect: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[outputs.BucketWebsiteConfigurationV2RoutingRuleCondition]: ...

@pulumi.output_type
class BucketWebsiteConfigurationV2RoutingRuleCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        http_error_code_returned_equals: Optional[_builtins.str] = ...,
        key_prefix_equals: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpErrorCodeReturnedEquals")
    def http_error_code_returned_equals(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyPrefixEquals")
    def key_prefix_equals(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BucketWebsiteConfigurationV2RoutingRuleRedirect(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_name: Optional[_builtins.str] = ...,
        http_redirect_code: Optional[_builtins.str] = ...,
        protocol: Optional[_builtins.str] = ...,
        replace_key_prefix_with: Optional[_builtins.str] = ...,
        replace_key_with: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="httpRedirectCode")
    def http_redirect_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replaceKeyPrefixWith")
    def replace_key_prefix_with(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replaceKeyWith")
    def replace_key_with(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DirectoryBucketLocation(dict):
    def __init__(
        __self__, *, name: _builtins.str, type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InventoryDestination(dict):
    def __init__(__self__, *, bucket: outputs.InventoryDestinationBucket) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> outputs.InventoryDestinationBucket: ...

@pulumi.output_type
class InventoryDestinationBucket(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_arn: _builtins.str,
        format: _builtins.str,
        account_id: Optional[_builtins.str] = ...,
        encryption: Optional[outputs.InventoryDestinationBucketEncryption] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.InventoryDestinationBucketEncryption]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InventoryDestinationBucketEncryption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        sse_kms: Optional[outputs.InventoryDestinationBucketEncryptionSseKms] = ...,
        sse_s3: Optional[outputs.InventoryDestinationBucketEncryptionSseS3] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sseKms")
    def sse_kms(
        self,
    ) -> Optional[outputs.InventoryDestinationBucketEncryptionSseKms]: ...
    @_builtins.property
    @pulumi.getter(name="sseS3")
    def sse_s3(self) -> Optional[outputs.InventoryDestinationBucketEncryptionSseS3]: ...

@pulumi.output_type
class InventoryDestinationBucketEncryptionSseKms(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, key_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> _builtins.str: ...

@pulumi.output_type
class InventoryDestinationBucketEncryptionSseS3(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class InventoryFilter(dict):
    def __init__(__self__, *, prefix: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InventorySchedule(dict):
    def __init__(__self__, *, frequency: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> _builtins.str: ...

@pulumi.output_type
class ObjectCopyGrant(dict):
    def __init__(
        __self__,
        *,
        permissions: Sequence[_builtins.str],
        type: _builtins.str,
        email: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ObjectCopyOverrideProvider(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_tags: Optional[outputs.ObjectCopyOverrideProviderDefaultTags] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultTags")
    def default_tags(
        self,
    ) -> Optional[outputs.ObjectCopyOverrideProviderDefaultTags]: ...

@pulumi.output_type
class ObjectCopyOverrideProviderDefaultTags(dict):
    def __init__(
        __self__, *, tags: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class VectorsIndexEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, kms_key_arn: _builtins.str, sse_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sseType")
    def sse_type(self) -> _builtins.str: ...

@pulumi.output_type
class VectorsIndexMetadataConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, non_filterable_metadata_keys: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nonFilterableMetadataKeys")
    def non_filterable_metadata_keys(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class VectorsVectorBucketEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, kms_key_arn: _builtins.str, sse_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sseType")
    def sse_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetAccessPointPublicAccessBlockConfigurationResult(dict):
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
class GetAccessPointVpcConfigurationResult(dict):
    def __init__(__self__, *, vpc_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetBucketObjectLockConfigurationRuleResult(dict):
    def __init__(
        __self__,
        *,
        default_retentions: Sequence[
            outputs.GetBucketObjectLockConfigurationRuleDefaultRetentionResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultRetentions")
    def default_retentions(
        self,
    ) -> Sequence[
        outputs.GetBucketObjectLockConfigurationRuleDefaultRetentionResult
    ]: ...

@pulumi.output_type
class GetBucketObjectLockConfigurationRuleDefaultRetentionResult(dict):
    def __init__(
        __self__, *, days: _builtins.int, mode: _builtins.str, years: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def years(self) -> _builtins.int: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleResult(dict):
    def __init__(
        __self__,
        *,
        delete_marker_replications: Sequence[
            outputs.GetBucketReplicationConfigurationRuleDeleteMarkerReplicationResult
        ],
        destinations: Sequence[
            outputs.GetBucketReplicationConfigurationRuleDestinationResult
        ],
        existing_object_replications: Sequence[
            outputs.GetBucketReplicationConfigurationRuleExistingObjectReplicationResult
        ],
        filters: Sequence[outputs.GetBucketReplicationConfigurationRuleFilterResult],
        id: _builtins.str,
        prefix: _builtins.str,
        priority: _builtins.int,
        source_selection_criterias: Sequence[
            outputs.GetBucketReplicationConfigurationRuleSourceSelectionCriteriaResult
        ],
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deleteMarkerReplications")
    def delete_marker_replications(
        self,
    ) -> Sequence[
        outputs.GetBucketReplicationConfigurationRuleDeleteMarkerReplicationResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Sequence[outputs.GetBucketReplicationConfigurationRuleDestinationResult]: ...
    @_builtins.property
    @pulumi.getter(name="existingObjectReplications")
    def existing_object_replications(
        self,
    ) -> Sequence[
        outputs.GetBucketReplicationConfigurationRuleExistingObjectReplicationResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Sequence[outputs.GetBucketReplicationConfigurationRuleFilterResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sourceSelectionCriterias")
    def source_selection_criterias(
        self,
    ) -> Sequence[
        outputs.GetBucketReplicationConfigurationRuleSourceSelectionCriteriaResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleDeleteMarkerReplicationResult(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleDestinationResult(dict):
    def __init__(
        __self__,
        *,
        access_control_translations: Sequence[
            outputs.GetBucketReplicationConfigurationRuleDestinationAccessControlTranslationResult
        ],
        account: _builtins.str,
        bucket: _builtins.str,
        encryption_configurations: Sequence[
            outputs.GetBucketReplicationConfigurationRuleDestinationEncryptionConfigurationResult
        ],
        metrics: Sequence[
            outputs.GetBucketReplicationConfigurationRuleDestinationMetricResult
        ],
        replication_times: Sequence[
            outputs.GetBucketReplicationConfigurationRuleDestinationReplicationTimeResult
        ],
        storage_class: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessControlTranslations")
    def access_control_translations(
        self,
    ) -> Sequence[
        outputs.GetBucketReplicationConfigurationRuleDestinationAccessControlTranslationResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def account(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(
        self,
    ) -> Sequence[
        outputs.GetBucketReplicationConfigurationRuleDestinationEncryptionConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def metrics(
        self,
    ) -> Sequence[
        outputs.GetBucketReplicationConfigurationRuleDestinationMetricResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="replicationTimes")
    def replication_times(
        self,
    ) -> Sequence[
        outputs.GetBucketReplicationConfigurationRuleDestinationReplicationTimeResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleDestinationAccessControlTranslationResult(
    dict
):
    def __init__(__self__, *, owner: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleDestinationEncryptionConfigurationResult(
    dict
):
    def __init__(__self__, *, replica_kms_key_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replicaKmsKeyId")
    def replica_kms_key_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleDestinationMetricResult(dict):
    def __init__(
        __self__,
        *,
        event_thresholds: Sequence[
            outputs.GetBucketReplicationConfigurationRuleDestinationMetricEventThresholdResult
        ],
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventThresholds")
    def event_thresholds(
        self,
    ) -> Sequence[
        outputs.GetBucketReplicationConfigurationRuleDestinationMetricEventThresholdResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleDestinationMetricEventThresholdResult(dict):
    def __init__(__self__, *, minutes: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleDestinationReplicationTimeResult(dict):
    def __init__(
        __self__,
        *,
        status: _builtins.str,
        times: Sequence[
            outputs.GetBucketReplicationConfigurationRuleDestinationReplicationTimeTimeResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def times(
        self,
    ) -> Sequence[
        outputs.GetBucketReplicationConfigurationRuleDestinationReplicationTimeTimeResult
    ]: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleDestinationReplicationTimeTimeResult(dict):
    def __init__(__self__, *, minutes: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleExistingObjectReplicationResult(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleFilterResult(dict):
    def __init__(
        __self__,
        *,
        ands: Sequence[outputs.GetBucketReplicationConfigurationRuleFilterAndResult],
        prefix: _builtins.str,
        tags: Sequence[outputs.GetBucketReplicationConfigurationRuleFilterTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Sequence[outputs.GetBucketReplicationConfigurationRuleFilterAndResult]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Sequence[outputs.GetBucketReplicationConfigurationRuleFilterTagResult]: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleFilterAndResult(dict):
    def __init__(
        __self__,
        *,
        prefix: _builtins.str,
        tags: Sequence[outputs.GetBucketReplicationConfigurationRuleFilterAndTagResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Sequence[outputs.GetBucketReplicationConfigurationRuleFilterAndTagResult]: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleFilterAndTagResult(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleFilterTagResult(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleSourceSelectionCriteriaResult(dict):
    def __init__(
        __self__,
        *,
        replica_modifications: Sequence[
            outputs.GetBucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModificationResult
        ],
        sse_kms_encrypted_objects: Sequence[
            outputs.GetBucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replicaModifications")
    def replica_modifications(
        self,
    ) -> Sequence[
        outputs.GetBucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModificationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sseKmsEncryptedObjects")
    def sse_kms_encrypted_objects(
        self,
    ) -> Sequence[
        outputs.GetBucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectResult
    ]: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleSourceSelectionCriteriaReplicaModificationResult(
    dict
):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetBucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectResult(
    dict
):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
