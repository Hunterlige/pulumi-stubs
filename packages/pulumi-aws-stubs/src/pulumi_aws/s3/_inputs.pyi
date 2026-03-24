

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from .. import _utilities, iam
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccessPointPublicAccessBlockConfigurationArgs', 'AccessPointPublicAccessBlockConfigurationArgsDict', 'AccessPointVpcConfigurationArgs', 'AccessPointVpcConfigurationArgsDict', 'AnalyticsConfigurationFilterArgs', 'AnalyticsConfigurationFilterArgsDict', 'AnalyticsConfigurationStorageClassAnalysisArgs', 'AnalyticsConfigurationStorageClassAnalysisArgsDict', ..., ..., ..., ..., ..., ..., 'BucketAbacAbacStatusArgs', 'BucketAbacAbacStatusArgsDict', 'BucketAclAccessControlPolicyArgs', 'BucketAclAccessControlPolicyArgsDict', 'BucketAclAccessControlPolicyGrantArgs', 'BucketAclAccessControlPolicyGrantArgsDict', 'BucketAclAccessControlPolicyGrantGranteeArgs', 'BucketAclAccessControlPolicyGrantGranteeArgsDict', 'BucketAclAccessControlPolicyOwnerArgs', 'BucketAclAccessControlPolicyOwnerArgsDict', 'BucketAclV2AccessControlPolicyArgs', 'BucketAclV2AccessControlPolicyArgsDict', 'BucketAclV2AccessControlPolicyGrantArgs', 'BucketAclV2AccessControlPolicyGrantArgsDict', 'BucketAclV2AccessControlPolicyGrantGranteeArgs', 'BucketAclV2AccessControlPolicyGrantGranteeArgsDict', 'BucketAclV2AccessControlPolicyOwnerArgs', 'BucketAclV2AccessControlPolicyOwnerArgsDict', 'BucketCorsConfigurationCorsRuleArgs', 'BucketCorsConfigurationCorsRuleArgsDict', 'BucketCorsConfigurationV2CorsRuleArgs', 'BucketCorsConfigurationV2CorsRuleArgsDict', 'BucketCorsRuleArgs', 'BucketCorsRuleArgsDict', 'BucketGrantArgs', 'BucketGrantArgsDict', 'BucketIntelligentTieringConfigurationFilterArgs', ..., 'BucketIntelligentTieringConfigurationTieringArgs', ..., 'BucketLifecycleConfigurationRuleArgs', 'BucketLifecycleConfigurationRuleArgsDict', ..., ..., 'BucketLifecycleConfigurationRuleExpirationArgs', 'BucketLifecycleConfigurationRuleExpirationArgsDict', 'BucketLifecycleConfigurationRuleFilterArgs', 'BucketLifecycleConfigurationRuleFilterArgsDict', 'BucketLifecycleConfigurationRuleFilterAndArgs', 'BucketLifecycleConfigurationRuleFilterAndArgsDict', 'BucketLifecycleConfigurationRuleFilterTagArgs', 'BucketLifecycleConfigurationRuleFilterTagArgsDict', ..., ..., ..., ..., 'BucketLifecycleConfigurationRuleTransitionArgs', 'BucketLifecycleConfigurationRuleTransitionArgsDict', 'BucketLifecycleConfigurationTimeoutsArgs', 'BucketLifecycleConfigurationTimeoutsArgsDict', 'BucketLifecycleConfigurationV2RuleArgs', 'BucketLifecycleConfigurationV2RuleArgsDict', ..., ..., 'BucketLifecycleConfigurationV2RuleExpirationArgs', ..., 'BucketLifecycleConfigurationV2RuleFilterArgs', 'BucketLifecycleConfigurationV2RuleFilterArgsDict', 'BucketLifecycleConfigurationV2RuleFilterAndArgs', ..., 'BucketLifecycleConfigurationV2RuleFilterTagArgs', ..., ..., ..., ..., ..., 'BucketLifecycleConfigurationV2RuleTransitionArgs', ..., 'BucketLifecycleConfigurationV2TimeoutsArgs', 'BucketLifecycleConfigurationV2TimeoutsArgsDict', 'BucketLifecycleRuleArgs', 'BucketLifecycleRuleArgsDict', 'BucketLifecycleRuleExpirationArgs', 'BucketLifecycleRuleExpirationArgsDict', 'BucketLifecycleRuleNoncurrentVersionExpirationArgs', ..., 'BucketLifecycleRuleNoncurrentVersionTransitionArgs', ..., 'BucketLifecycleRuleTransitionArgs', 'BucketLifecycleRuleTransitionArgsDict', 'BucketLoggingArgs', 'BucketLoggingArgsDict', 'BucketLoggingTargetGrantArgs', 'BucketLoggingTargetGrantArgsDict', 'BucketLoggingTargetGrantGranteeArgs', 'BucketLoggingTargetGrantGranteeArgsDict', 'BucketLoggingTargetObjectKeyFormatArgs', 'BucketLoggingTargetObjectKeyFormatArgsDict', ..., ..., 'BucketLoggingTargetObjectKeyFormatSimplePrefixArgs', ..., 'BucketLoggingV2TargetGrantArgs', 'BucketLoggingV2TargetGrantArgsDict', 'BucketLoggingV2TargetGrantGranteeArgs', 'BucketLoggingV2TargetGrantGranteeArgsDict', 'BucketLoggingV2TargetObjectKeyFormatArgs', 'BucketLoggingV2TargetObjectKeyFormatArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'BucketMetadataConfigurationTimeoutsArgs', 'BucketMetadataConfigurationTimeoutsArgsDict', 'BucketMetricFilterArgs', 'BucketMetricFilterArgsDict', 'BucketNotificationLambdaFunctionArgs', 'BucketNotificationLambdaFunctionArgsDict', 'BucketNotificationQueueArgs', 'BucketNotificationQueueArgsDict', 'BucketNotificationTopicArgs', 'BucketNotificationTopicArgsDict', 'BucketObjectLockConfigurationArgs', 'BucketObjectLockConfigurationArgsDict', 'BucketObjectLockConfigurationRuleArgs', 'BucketObjectLockConfigurationRuleArgsDict', ..., ..., 'BucketObjectLockConfigurationV2RuleArgs', 'BucketObjectLockConfigurationV2RuleArgsDict', ..., ..., 'BucketObjectv2OverrideProviderArgs', 'BucketObjectv2OverrideProviderArgsDict', 'BucketObjectv2OverrideProviderDefaultTagsArgs', 'BucketObjectv2OverrideProviderDefaultTagsArgsDict', 'BucketOwnershipControlsRuleArgs', 'BucketOwnershipControlsRuleArgsDict', 'BucketReplicationConfigRuleArgs', 'BucketReplicationConfigRuleArgsDict', ..., ..., 'BucketReplicationConfigRuleDestinationArgs', 'BucketReplicationConfigRuleDestinationArgsDict', ..., ..., ..., ..., 'BucketReplicationConfigRuleDestinationMetricsArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., 'BucketReplicationConfigRuleFilterArgs', 'BucketReplicationConfigRuleFilterArgsDict', 'BucketReplicationConfigRuleFilterAndArgs', 'BucketReplicationConfigRuleFilterAndArgsDict', 'BucketReplicationConfigRuleFilterTagArgs', 'BucketReplicationConfigRuleFilterTagArgsDict', ..., ..., ..., ..., ..., ..., 'BucketReplicationConfigurationArgs', 'BucketReplicationConfigurationArgsDict', 'BucketReplicationConfigurationRuleArgs', 'BucketReplicationConfigurationRuleArgsDict', 'BucketReplicationConfigurationRuleDestinationArgs', ..., ..., ..., ..., ..., ..., ..., 'BucketReplicationConfigurationRuleFilterArgs', 'BucketReplicationConfigurationRuleFilterArgsDict', ..., ..., ..., ..., 'BucketServerSideEncryptionConfigurationArgs', 'BucketServerSideEncryptionConfigurationArgsDict', 'BucketServerSideEncryptionConfigurationRuleArgs', ..., ..., ..., 'BucketServerSideEncryptionConfigurationV2RuleArgs', ..., ..., ..., 'BucketV2CorsRuleArgs', 'BucketV2CorsRuleArgsDict', 'BucketV2GrantArgs', 'BucketV2GrantArgsDict', 'BucketV2LifecycleRuleArgs', 'BucketV2LifecycleRuleArgsDict', 'BucketV2LifecycleRuleExpirationArgs', 'BucketV2LifecycleRuleExpirationArgsDict', ..., ..., ..., ..., 'BucketV2LifecycleRuleTransitionArgs', 'BucketV2LifecycleRuleTransitionArgsDict', 'BucketV2LoggingArgs', 'BucketV2LoggingArgsDict', 'BucketV2ObjectLockConfigurationArgs', 'BucketV2ObjectLockConfigurationArgsDict', 'BucketV2ObjectLockConfigurationRuleArgs', 'BucketV2ObjectLockConfigurationRuleArgsDict', ..., ..., 'BucketV2ReplicationConfigurationArgs', 'BucketV2ReplicationConfigurationArgsDict', 'BucketV2ReplicationConfigurationRuleArgs', 'BucketV2ReplicationConfigurationRuleArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'BucketV2ReplicationConfigurationRuleFilterArgs', 'BucketV2ReplicationConfigurationRuleFilterArgsDict', ..., ..., ..., ..., 'BucketV2ServerSideEncryptionConfigurationArgs', 'BucketV2ServerSideEncryptionConfigurationArgsDict', 'BucketV2ServerSideEncryptionConfigurationRuleArgs', ..., ..., ..., 'BucketV2VersioningArgs', 'BucketV2VersioningArgsDict', 'BucketV2WebsiteArgs', 'BucketV2WebsiteArgsDict', 'BucketVersioningArgs', 'BucketVersioningArgsDict', 'BucketVersioningV2VersioningConfigurationArgs', 'BucketVersioningV2VersioningConfigurationArgsDict', 'BucketVersioningVersioningConfigurationArgs', 'BucketVersioningVersioningConfigurationArgsDict', 'BucketWebsiteArgs', 'BucketWebsiteArgsDict', 'BucketWebsiteConfigurationErrorDocumentArgs', 'BucketWebsiteConfigurationErrorDocumentArgsDict', 'BucketWebsiteConfigurationIndexDocumentArgs', 'BucketWebsiteConfigurationIndexDocumentArgsDict', ..., ..., 'BucketWebsiteConfigurationRoutingRuleArgs', 'BucketWebsiteConfigurationRoutingRuleArgsDict', 'BucketWebsiteConfigurationRoutingRuleConditionArgs', ..., 'BucketWebsiteConfigurationRoutingRuleRedirectArgs', ..., 'BucketWebsiteConfigurationV2ErrorDocumentArgs', 'BucketWebsiteConfigurationV2ErrorDocumentArgsDict', 'BucketWebsiteConfigurationV2IndexDocumentArgs', 'BucketWebsiteConfigurationV2IndexDocumentArgsDict', ..., ..., 'BucketWebsiteConfigurationV2RoutingRuleArgs', 'BucketWebsiteConfigurationV2RoutingRuleArgsDict', ..., ..., ..., ..., 'DirectoryBucketLocationArgs', 'DirectoryBucketLocationArgsDict', 'InventoryDestinationArgs', 'InventoryDestinationArgsDict', 'InventoryDestinationBucketArgs', 'InventoryDestinationBucketArgsDict', 'InventoryDestinationBucketEncryptionArgs', 'InventoryDestinationBucketEncryptionArgsDict', 'InventoryDestinationBucketEncryptionSseKmsArgs', 'InventoryDestinationBucketEncryptionSseKmsArgsDict', 'InventoryDestinationBucketEncryptionSseS3Args', 'InventoryDestinationBucketEncryptionSseS3ArgsDict', 'InventoryFilterArgs', 'InventoryFilterArgsDict', 'InventoryScheduleArgs', 'InventoryScheduleArgsDict', 'ObjectCopyGrantArgs', 'ObjectCopyGrantArgsDict', 'ObjectCopyOverrideProviderArgs', 'ObjectCopyOverrideProviderArgsDict', 'ObjectCopyOverrideProviderDefaultTagsArgs', 'ObjectCopyOverrideProviderDefaultTagsArgsDict', 'PolicyDocumentArgs', 'PolicyDocumentArgsDict', 'VectorsIndexEncryptionConfigurationArgs', 'VectorsIndexEncryptionConfigurationArgsDict', 'VectorsIndexMetadataConfigurationArgs', 'VectorsIndexMetadataConfigurationArgsDict', 'VectorsVectorBucketEncryptionConfigurationArgs', 'VectorsVectorBucketEncryptionConfigurationArgsDict']
class AccessPointPublicAccessBlockConfigurationArgsDict(TypedDict):
    block_public_acls: NotRequired[pulumi.Input[_builtins.bool]]
    block_public_policy: NotRequired[pulumi.Input[_builtins.bool]]
    ignore_public_acls: NotRequired[pulumi.Input[_builtins.bool]]
    restrict_public_buckets: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class AccessPointPublicAccessBlockConfigurationArgs:
    def __init__(__self__, *, block_public_acls: Optional[pulumi.Input[_builtins.bool]] = ..., block_public_policy: Optional[pulumi.Input[_builtins.bool]] = ..., ignore_public_acls: Optional[pulumi.Input[_builtins.bool]] = ..., restrict_public_buckets: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockPublicAcls")
    def block_public_acls(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @block_public_acls.setter
    def block_public_acls(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockPublicPolicy")
    def block_public_policy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @block_public_policy.setter
    def block_public_policy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignorePublicAcls")
    def ignore_public_acls(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_public_acls.setter
    def ignore_public_acls(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictPublicBuckets")
    def restrict_public_buckets(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @restrict_public_buckets.setter
    def restrict_public_buckets(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class AccessPointVpcConfigurationArgsDict(TypedDict):
    vpc_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class AccessPointVpcConfigurationArgs:
    def __init__(__self__, *, vpc_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class AnalyticsConfigurationFilterArgsDict(TypedDict):
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AnalyticsConfigurationFilterArgs:
    def __init__(__self__, *, prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AnalyticsConfigurationStorageClassAnalysisArgsDict(TypedDict):
    data_export: pulumi.Input[AnalyticsConfigurationStorageClassAnalysisDataExportArgsDict]


@pulumi.input_type
class AnalyticsConfigurationStorageClassAnalysisArgs:
    def __init__(__self__, *, data_export: pulumi.Input[AnalyticsConfigurationStorageClassAnalysisDataExportArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExport")
    def data_export(self) -> pulumi.Input[AnalyticsConfigurationStorageClassAnalysisDataExportArgs]:
        
        ...
    
    @data_export.setter
    def data_export(self, value: pulumi.Input[AnalyticsConfigurationStorageClassAnalysisDataExportArgs]): # -> None:
        ...
    


class AnalyticsConfigurationStorageClassAnalysisDataExportArgsDict(TypedDict):
    destination: pulumi.Input[AnalyticsConfigurationStorageClassAnalysisDataExportDestinationArgsDict]
    output_schema_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AnalyticsConfigurationStorageClassAnalysisDataExportArgs:
    def __init__(__self__, *, destination: pulumi.Input[AnalyticsConfigurationStorageClassAnalysisDataExportDestinationArgs], output_schema_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[AnalyticsConfigurationStorageClassAnalysisDataExportDestinationArgs]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[AnalyticsConfigurationStorageClassAnalysisDataExportDestinationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputSchemaVersion")
    def output_schema_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @output_schema_version.setter
    def output_schema_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AnalyticsConfigurationStorageClassAnalysisDataExportDestinationArgsDict(TypedDict):
    s3_bucket_destination: pulumi.Input[AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationArgsDict]


@pulumi.input_type
class AnalyticsConfigurationStorageClassAnalysisDataExportDestinationArgs:
    def __init__(__self__, *, s3_bucket_destination: pulumi.Input[AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketDestination")
    def s3_bucket_destination(self) -> pulumi.Input[AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationArgs]:
        
        ...
    
    @s3_bucket_destination.setter
    def s3_bucket_destination(self, value: pulumi.Input[AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationArgs]): # -> None:
        ...
    


class AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    bucket_account_id: NotRequired[pulumi.Input[_builtins.str]]
    format: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AnalyticsConfigurationStorageClassAnalysisDataExportDestinationS3BucketDestinationArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], bucket_account_id: Optional[pulumi.Input[_builtins.str]] = ..., format: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_account_id.setter
    def bucket_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketAbacAbacStatusArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketAbacAbacStatusArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketAclAccessControlPolicyArgsDict(TypedDict):
    owner: pulumi.Input[BucketAclAccessControlPolicyOwnerArgsDict]
    grants: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketAclAccessControlPolicyGrantArgsDict]]]]


@pulumi.input_type
class BucketAclAccessControlPolicyArgs:
    def __init__(__self__, *, owner: pulumi.Input[BucketAclAccessControlPolicyOwnerArgs], grants: Optional[pulumi.Input[Sequence[pulumi.Input[BucketAclAccessControlPolicyGrantArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Input[BucketAclAccessControlPolicyOwnerArgs]:
        
        ...
    
    @owner.setter
    def owner(self, value: pulumi.Input[BucketAclAccessControlPolicyOwnerArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def grants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketAclAccessControlPolicyGrantArgs]]]]:
        
        ...
    
    @grants.setter
    def grants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketAclAccessControlPolicyGrantArgs]]]]): # -> None:
        ...
    


class BucketAclAccessControlPolicyGrantArgsDict(TypedDict):
    permission: pulumi.Input[_builtins.str]
    grantee: NotRequired[pulumi.Input[BucketAclAccessControlPolicyGrantGranteeArgsDict]]


@pulumi.input_type
class BucketAclAccessControlPolicyGrantArgs:
    def __init__(__self__, *, permission: pulumi.Input[_builtins.str], grantee: Optional[pulumi.Input[BucketAclAccessControlPolicyGrantGranteeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permission(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @permission.setter
    def permission(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> Optional[pulumi.Input[BucketAclAccessControlPolicyGrantGranteeArgs]]:
        
        ...
    
    @grantee.setter
    def grantee(self, value: Optional[pulumi.Input[BucketAclAccessControlPolicyGrantGranteeArgs]]): # -> None:
        ...
    


class BucketAclAccessControlPolicyGrantGranteeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    email_address: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketAclAccessControlPolicyGrantGranteeArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ..., email_address: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    @_utilities.deprecated(...)
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketAclAccessControlPolicyOwnerArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketAclAccessControlPolicyOwnerArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    @_utilities.deprecated(...)
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketAclV2AccessControlPolicyArgsDict(TypedDict):
    owner: pulumi.Input[BucketAclV2AccessControlPolicyOwnerArgsDict]
    grants: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketAclV2AccessControlPolicyGrantArgsDict]]]]


@pulumi.input_type
class BucketAclV2AccessControlPolicyArgs:
    def __init__(__self__, *, owner: pulumi.Input[BucketAclV2AccessControlPolicyOwnerArgs], grants: Optional[pulumi.Input[Sequence[pulumi.Input[BucketAclV2AccessControlPolicyGrantArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Input[BucketAclV2AccessControlPolicyOwnerArgs]:
        
        ...
    
    @owner.setter
    def owner(self, value: pulumi.Input[BucketAclV2AccessControlPolicyOwnerArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def grants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketAclV2AccessControlPolicyGrantArgs]]]]:
        
        ...
    
    @grants.setter
    def grants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketAclV2AccessControlPolicyGrantArgs]]]]): # -> None:
        ...
    


class BucketAclV2AccessControlPolicyGrantArgsDict(TypedDict):
    permission: pulumi.Input[_builtins.str]
    grantee: NotRequired[pulumi.Input[BucketAclV2AccessControlPolicyGrantGranteeArgsDict]]


@pulumi.input_type
class BucketAclV2AccessControlPolicyGrantArgs:
    def __init__(__self__, *, permission: pulumi.Input[_builtins.str], grantee: Optional[pulumi.Input[BucketAclV2AccessControlPolicyGrantGranteeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permission(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @permission.setter
    def permission(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> Optional[pulumi.Input[BucketAclV2AccessControlPolicyGrantGranteeArgs]]:
        
        ...
    
    @grantee.setter
    def grantee(self, value: Optional[pulumi.Input[BucketAclV2AccessControlPolicyGrantGranteeArgs]]): # -> None:
        ...
    


class BucketAclV2AccessControlPolicyGrantGranteeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    email_address: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketAclV2AccessControlPolicyGrantGranteeArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ..., email_address: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    @_utilities.deprecated(...)
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketAclV2AccessControlPolicyOwnerArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketAclV2AccessControlPolicyOwnerArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    @_utilities.deprecated(...)
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketCorsConfigurationCorsRuleArgsDict(TypedDict):
    allowed_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allowed_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    expose_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    max_age_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketCorsConfigurationCorsRuleArgs:
    def __init__(__self__, *, allowed_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], allowed_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., expose_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., max_age_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_methods.setter
    def allowed_methods(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_origins.setter
    def allowed_origins(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_headers.setter
    def allowed_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @expose_headers.setter
    def expose_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_age_seconds.setter
    def max_age_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketCorsConfigurationV2CorsRuleArgsDict(TypedDict):
    allowed_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allowed_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    expose_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    max_age_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketCorsConfigurationV2CorsRuleArgs:
    def __init__(__self__, *, allowed_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], allowed_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., expose_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., max_age_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_methods.setter
    def allowed_methods(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_origins.setter
    def allowed_origins(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_headers.setter
    def allowed_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @expose_headers.setter
    def expose_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_age_seconds.setter
    def max_age_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketCorsRuleArgsDict(TypedDict):
    allowed_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allowed_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    expose_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_age_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketCorsRuleArgs:
    def __init__(__self__, *, allowed_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], allowed_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., expose_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., max_age_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_methods.setter
    def allowed_methods(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_origins.setter
    def allowed_origins(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_headers.setter
    def allowed_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @expose_headers.setter
    def expose_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_age_seconds.setter
    def max_age_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketGrantArgsDict(TypedDict):
    permissions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    type: pulumi.Input[_builtins.str]
    id: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketGrantArgs:
    def __init__(__self__, *, permissions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], type: pulumi.Input[_builtins.str], id: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @permissions.setter
    def permissions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketIntelligentTieringConfigurationFilterArgsDict(TypedDict):
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class BucketIntelligentTieringConfigurationFilterArgs:
    def __init__(__self__, *, prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class BucketIntelligentTieringConfigurationTieringArgsDict(TypedDict):
    access_tier: pulumi.Input[_builtins.str]
    days: pulumi.Input[_builtins.int]


@pulumi.input_type
class BucketIntelligentTieringConfigurationTieringArgs:
    def __init__(__self__, *, access_tier: pulumi.Input[_builtins.str], days: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @access_tier.setter
    def access_tier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @days.setter
    def days(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class BucketLifecycleConfigurationRuleArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]
    abort_incomplete_multipart_upload: NotRequired[pulumi.Input[BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadArgsDict]]
    expiration: NotRequired[pulumi.Input[BucketLifecycleConfigurationRuleExpirationArgsDict]]
    filter: NotRequired[pulumi.Input[BucketLifecycleConfigurationRuleFilterArgsDict]]
    noncurrent_version_expiration: NotRequired[pulumi.Input[BucketLifecycleConfigurationRuleNoncurrentVersionExpirationArgsDict]]
    noncurrent_version_transitions: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleNoncurrentVersionTransitionArgsDict]]]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    transitions: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleTransitionArgsDict]]]]


@pulumi.input_type
class BucketLifecycleConfigurationRuleArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], status: pulumi.Input[_builtins.str], abort_incomplete_multipart_upload: Optional[pulumi.Input[BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadArgs]] = ..., expiration: Optional[pulumi.Input[BucketLifecycleConfigurationRuleExpirationArgs]] = ..., filter: Optional[pulumi.Input[BucketLifecycleConfigurationRuleFilterArgs]] = ..., noncurrent_version_expiration: Optional[pulumi.Input[BucketLifecycleConfigurationRuleNoncurrentVersionExpirationArgs]] = ..., noncurrent_version_transitions: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleNoncurrentVersionTransitionArgs]]]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., transitions: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleTransitionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="abortIncompleteMultipartUpload")
    def abort_incomplete_multipart_upload(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadArgs]]:
        
        ...
    
    @abort_incomplete_multipart_upload.setter
    def abort_incomplete_multipart_upload(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationRuleExpirationArgs]]:
        
        ...
    
    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationRuleExpirationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationRuleFilterArgs]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationRuleFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionExpiration")
    def noncurrent_version_expiration(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationRuleNoncurrentVersionExpirationArgs]]:
        
        ...
    
    @noncurrent_version_expiration.setter
    def noncurrent_version_expiration(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationRuleNoncurrentVersionExpirationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionTransitions")
    def noncurrent_version_transitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleNoncurrentVersionTransitionArgs]]]]:
        
        ...
    
    @noncurrent_version_transitions.setter
    def noncurrent_version_transitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleNoncurrentVersionTransitionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""Specify a prefix using 'filter' instead""")
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleTransitionArgs]]]]:
        
        ...
    
    @transitions.setter
    def transitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationRuleTransitionArgs]]]]): # -> None:
        ...
    


class BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadArgsDict(TypedDict):
    days_after_initiation: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketLifecycleConfigurationRuleAbortIncompleteMultipartUploadArgs:
    def __init__(__self__, *, days_after_initiation: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysAfterInitiation")
    def days_after_initiation(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days_after_initiation.setter
    def days_after_initiation(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketLifecycleConfigurationRuleExpirationArgsDict(TypedDict):
    date: NotRequired[pulumi.Input[_builtins.str]]
    days: NotRequired[pulumi.Input[_builtins.int]]
    expired_object_delete_marker: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class BucketLifecycleConfigurationRuleExpirationArgs:
    def __init__(__self__, *, date: Optional[pulumi.Input[_builtins.str]] = ..., days: Optional[pulumi.Input[_builtins.int]] = ..., expired_object_delete_marker: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @date.setter
    def date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiredObjectDeleteMarker")
    def expired_object_delete_marker(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @expired_object_delete_marker.setter
    def expired_object_delete_marker(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class BucketLifecycleConfigurationRuleFilterArgsDict(TypedDict):
    and_: NotRequired[pulumi.Input[BucketLifecycleConfigurationRuleFilterAndArgsDict]]
    object_size_greater_than: NotRequired[pulumi.Input[_builtins.int]]
    object_size_less_than: NotRequired[pulumi.Input[_builtins.int]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tag: NotRequired[pulumi.Input[BucketLifecycleConfigurationRuleFilterTagArgsDict]]


@pulumi.input_type
class BucketLifecycleConfigurationRuleFilterArgs:
    def __init__(__self__, *, and_: Optional[pulumi.Input[BucketLifecycleConfigurationRuleFilterAndArgs]] = ..., object_size_greater_than: Optional[pulumi.Input[_builtins.int]] = ..., object_size_less_than: Optional[pulumi.Input[_builtins.int]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., tag: Optional[pulumi.Input[BucketLifecycleConfigurationRuleFilterTagArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationRuleFilterAndArgs]]:
        
        ...
    
    @and_.setter
    def and_(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationRuleFilterAndArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectSizeGreaterThan")
    def object_size_greater_than(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @object_size_greater_than.setter
    def object_size_greater_than(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectSizeLessThan")
    def object_size_less_than(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @object_size_less_than.setter
    def object_size_less_than(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationRuleFilterTagArgs]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationRuleFilterTagArgs]]): # -> None:
        ...
    


class BucketLifecycleConfigurationRuleFilterAndArgsDict(TypedDict):
    object_size_greater_than: NotRequired[pulumi.Input[_builtins.int]]
    object_size_less_than: NotRequired[pulumi.Input[_builtins.int]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class BucketLifecycleConfigurationRuleFilterAndArgs:
    def __init__(__self__, *, object_size_greater_than: Optional[pulumi.Input[_builtins.int]] = ..., object_size_less_than: Optional[pulumi.Input[_builtins.int]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectSizeGreaterThan")
    def object_size_greater_than(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @object_size_greater_than.setter
    def object_size_greater_than(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectSizeLessThan")
    def object_size_less_than(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @object_size_less_than.setter
    def object_size_less_than(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class BucketLifecycleConfigurationRuleFilterTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketLifecycleConfigurationRuleFilterTagArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketLifecycleConfigurationRuleNoncurrentVersionExpirationArgsDict(TypedDict):
    noncurrent_days: pulumi.Input[_builtins.int]
    newer_noncurrent_versions: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketLifecycleConfigurationRuleNoncurrentVersionExpirationArgs:
    def __init__(__self__, *, noncurrent_days: pulumi.Input[_builtins.int], newer_noncurrent_versions: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentDays")
    def noncurrent_days(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @noncurrent_days.setter
    def noncurrent_days(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="newerNoncurrentVersions")
    def newer_noncurrent_versions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @newer_noncurrent_versions.setter
    def newer_noncurrent_versions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketLifecycleConfigurationRuleNoncurrentVersionTransitionArgsDict(TypedDict):
    noncurrent_days: pulumi.Input[_builtins.int]
    storage_class: pulumi.Input[_builtins.str]
    newer_noncurrent_versions: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketLifecycleConfigurationRuleNoncurrentVersionTransitionArgs:
    def __init__(__self__, *, noncurrent_days: pulumi.Input[_builtins.int], storage_class: pulumi.Input[_builtins.str], newer_noncurrent_versions: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentDays")
    def noncurrent_days(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @noncurrent_days.setter
    def noncurrent_days(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="newerNoncurrentVersions")
    def newer_noncurrent_versions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @newer_noncurrent_versions.setter
    def newer_noncurrent_versions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketLifecycleConfigurationRuleTransitionArgsDict(TypedDict):
    storage_class: pulumi.Input[_builtins.str]
    date: NotRequired[pulumi.Input[_builtins.str]]
    days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketLifecycleConfigurationRuleTransitionArgs:
    def __init__(__self__, *, storage_class: pulumi.Input[_builtins.str], date: Optional[pulumi.Input[_builtins.str]] = ..., days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @date.setter
    def date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketLifecycleConfigurationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketLifecycleConfigurationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketLifecycleConfigurationV2RuleArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]
    abort_incomplete_multipart_upload: NotRequired[pulumi.Input[BucketLifecycleConfigurationV2RuleAbortIncompleteMultipartUploadArgsDict]]
    expiration: NotRequired[pulumi.Input[BucketLifecycleConfigurationV2RuleExpirationArgsDict]]
    filter: NotRequired[pulumi.Input[BucketLifecycleConfigurationV2RuleFilterArgsDict]]
    noncurrent_version_expiration: NotRequired[pulumi.Input[BucketLifecycleConfigurationV2RuleNoncurrentVersionExpirationArgsDict]]
    noncurrent_version_transitions: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleNoncurrentVersionTransitionArgsDict]]]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    transitions: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleTransitionArgsDict]]]]


@pulumi.input_type
class BucketLifecycleConfigurationV2RuleArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], status: pulumi.Input[_builtins.str], abort_incomplete_multipart_upload: Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleAbortIncompleteMultipartUploadArgs]] = ..., expiration: Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleExpirationArgs]] = ..., filter: Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleFilterArgs]] = ..., noncurrent_version_expiration: Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleNoncurrentVersionExpirationArgs]] = ..., noncurrent_version_transitions: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleNoncurrentVersionTransitionArgs]]]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., transitions: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleTransitionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="abortIncompleteMultipartUpload")
    def abort_incomplete_multipart_upload(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleAbortIncompleteMultipartUploadArgs]]:
        
        ...
    
    @abort_incomplete_multipart_upload.setter
    def abort_incomplete_multipart_upload(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleAbortIncompleteMultipartUploadArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleExpirationArgs]]:
        
        ...
    
    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleExpirationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleFilterArgs]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionExpiration")
    def noncurrent_version_expiration(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleNoncurrentVersionExpirationArgs]]:
        
        ...
    
    @noncurrent_version_expiration.setter
    def noncurrent_version_expiration(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleNoncurrentVersionExpirationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionTransitions")
    def noncurrent_version_transitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleNoncurrentVersionTransitionArgs]]]]:
        
        ...
    
    @noncurrent_version_transitions.setter
    def noncurrent_version_transitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleNoncurrentVersionTransitionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""Specify a prefix using 'filter' instead""")
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleTransitionArgs]]]]:
        
        ...
    
    @transitions.setter
    def transitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleConfigurationV2RuleTransitionArgs]]]]): # -> None:
        ...
    


class BucketLifecycleConfigurationV2RuleAbortIncompleteMultipartUploadArgsDict(TypedDict):
    days_after_initiation: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketLifecycleConfigurationV2RuleAbortIncompleteMultipartUploadArgs:
    def __init__(__self__, *, days_after_initiation: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysAfterInitiation")
    def days_after_initiation(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days_after_initiation.setter
    def days_after_initiation(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketLifecycleConfigurationV2RuleExpirationArgsDict(TypedDict):
    date: NotRequired[pulumi.Input[_builtins.str]]
    days: NotRequired[pulumi.Input[_builtins.int]]
    expired_object_delete_marker: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class BucketLifecycleConfigurationV2RuleExpirationArgs:
    def __init__(__self__, *, date: Optional[pulumi.Input[_builtins.str]] = ..., days: Optional[pulumi.Input[_builtins.int]] = ..., expired_object_delete_marker: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @date.setter
    def date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiredObjectDeleteMarker")
    def expired_object_delete_marker(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @expired_object_delete_marker.setter
    def expired_object_delete_marker(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class BucketLifecycleConfigurationV2RuleFilterArgsDict(TypedDict):
    and_: NotRequired[pulumi.Input[BucketLifecycleConfigurationV2RuleFilterAndArgsDict]]
    object_size_greater_than: NotRequired[pulumi.Input[_builtins.int]]
    object_size_less_than: NotRequired[pulumi.Input[_builtins.int]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tag: NotRequired[pulumi.Input[BucketLifecycleConfigurationV2RuleFilterTagArgsDict]]


@pulumi.input_type
class BucketLifecycleConfigurationV2RuleFilterArgs:
    def __init__(__self__, *, and_: Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleFilterAndArgs]] = ..., object_size_greater_than: Optional[pulumi.Input[_builtins.int]] = ..., object_size_less_than: Optional[pulumi.Input[_builtins.int]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., tag: Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleFilterTagArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleFilterAndArgs]]:
        
        ...
    
    @and_.setter
    def and_(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleFilterAndArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectSizeGreaterThan")
    def object_size_greater_than(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @object_size_greater_than.setter
    def object_size_greater_than(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectSizeLessThan")
    def object_size_less_than(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @object_size_less_than.setter
    def object_size_less_than(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleFilterTagArgs]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[BucketLifecycleConfigurationV2RuleFilterTagArgs]]): # -> None:
        ...
    


class BucketLifecycleConfigurationV2RuleFilterAndArgsDict(TypedDict):
    object_size_greater_than: NotRequired[pulumi.Input[_builtins.int]]
    object_size_less_than: NotRequired[pulumi.Input[_builtins.int]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class BucketLifecycleConfigurationV2RuleFilterAndArgs:
    def __init__(__self__, *, object_size_greater_than: Optional[pulumi.Input[_builtins.int]] = ..., object_size_less_than: Optional[pulumi.Input[_builtins.int]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectSizeGreaterThan")
    def object_size_greater_than(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @object_size_greater_than.setter
    def object_size_greater_than(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectSizeLessThan")
    def object_size_less_than(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @object_size_less_than.setter
    def object_size_less_than(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class BucketLifecycleConfigurationV2RuleFilterTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketLifecycleConfigurationV2RuleFilterTagArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketLifecycleConfigurationV2RuleNoncurrentVersionExpirationArgsDict(TypedDict):
    noncurrent_days: pulumi.Input[_builtins.int]
    newer_noncurrent_versions: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketLifecycleConfigurationV2RuleNoncurrentVersionExpirationArgs:
    def __init__(__self__, *, noncurrent_days: pulumi.Input[_builtins.int], newer_noncurrent_versions: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentDays")
    def noncurrent_days(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @noncurrent_days.setter
    def noncurrent_days(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="newerNoncurrentVersions")
    def newer_noncurrent_versions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @newer_noncurrent_versions.setter
    def newer_noncurrent_versions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketLifecycleConfigurationV2RuleNoncurrentVersionTransitionArgsDict(TypedDict):
    noncurrent_days: pulumi.Input[_builtins.int]
    storage_class: pulumi.Input[_builtins.str]
    newer_noncurrent_versions: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketLifecycleConfigurationV2RuleNoncurrentVersionTransitionArgs:
    def __init__(__self__, *, noncurrent_days: pulumi.Input[_builtins.int], storage_class: pulumi.Input[_builtins.str], newer_noncurrent_versions: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentDays")
    def noncurrent_days(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @noncurrent_days.setter
    def noncurrent_days(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="newerNoncurrentVersions")
    def newer_noncurrent_versions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @newer_noncurrent_versions.setter
    def newer_noncurrent_versions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketLifecycleConfigurationV2RuleTransitionArgsDict(TypedDict):
    storage_class: pulumi.Input[_builtins.str]
    date: NotRequired[pulumi.Input[_builtins.str]]
    days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketLifecycleConfigurationV2RuleTransitionArgs:
    def __init__(__self__, *, storage_class: pulumi.Input[_builtins.str], date: Optional[pulumi.Input[_builtins.str]] = ..., days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @date.setter
    def date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketLifecycleConfigurationV2TimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketLifecycleConfigurationV2TimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketLifecycleRuleArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    abort_incomplete_multipart_upload_days: NotRequired[pulumi.Input[_builtins.int]]
    expiration: NotRequired[pulumi.Input[BucketLifecycleRuleExpirationArgsDict]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    noncurrent_version_expiration: NotRequired[pulumi.Input[BucketLifecycleRuleNoncurrentVersionExpirationArgsDict]]
    noncurrent_version_transitions: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleNoncurrentVersionTransitionArgsDict]]]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    transitions: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleTransitionArgsDict]]]]


@pulumi.input_type
class BucketLifecycleRuleArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], abort_incomplete_multipart_upload_days: Optional[pulumi.Input[_builtins.int]] = ..., expiration: Optional[pulumi.Input[BucketLifecycleRuleExpirationArgs]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., noncurrent_version_expiration: Optional[pulumi.Input[BucketLifecycleRuleNoncurrentVersionExpirationArgs]] = ..., noncurrent_version_transitions: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleNoncurrentVersionTransitionArgs]]]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transitions: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleTransitionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="abortIncompleteMultipartUploadDays")
    def abort_incomplete_multipart_upload_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @abort_incomplete_multipart_upload_days.setter
    def abort_incomplete_multipart_upload_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[BucketLifecycleRuleExpirationArgs]]:
        
        ...
    
    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[BucketLifecycleRuleExpirationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionExpiration")
    def noncurrent_version_expiration(self) -> Optional[pulumi.Input[BucketLifecycleRuleNoncurrentVersionExpirationArgs]]:
        
        ...
    
    @noncurrent_version_expiration.setter
    def noncurrent_version_expiration(self, value: Optional[pulumi.Input[BucketLifecycleRuleNoncurrentVersionExpirationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionTransitions")
    def noncurrent_version_transitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleNoncurrentVersionTransitionArgs]]]]:
        
        ...
    
    @noncurrent_version_transitions.setter
    def noncurrent_version_transitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleNoncurrentVersionTransitionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleTransitionArgs]]]]:
        
        ...
    
    @transitions.setter
    def transitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketLifecycleRuleTransitionArgs]]]]): # -> None:
        ...
    


class BucketLifecycleRuleExpirationArgsDict(TypedDict):
    date: NotRequired[pulumi.Input[_builtins.str]]
    days: NotRequired[pulumi.Input[_builtins.int]]
    expired_object_delete_marker: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class BucketLifecycleRuleExpirationArgs:
    def __init__(__self__, *, date: Optional[pulumi.Input[_builtins.str]] = ..., days: Optional[pulumi.Input[_builtins.int]] = ..., expired_object_delete_marker: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @date.setter
    def date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiredObjectDeleteMarker")
    def expired_object_delete_marker(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @expired_object_delete_marker.setter
    def expired_object_delete_marker(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class BucketLifecycleRuleNoncurrentVersionExpirationArgsDict(TypedDict):
    days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketLifecycleRuleNoncurrentVersionExpirationArgs:
    def __init__(__self__, *, days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketLifecycleRuleNoncurrentVersionTransitionArgsDict(TypedDict):
    storage_class: pulumi.Input[_builtins.str]
    days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketLifecycleRuleNoncurrentVersionTransitionArgs:
    def __init__(__self__, *, storage_class: pulumi.Input[_builtins.str], days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketLifecycleRuleTransitionArgsDict(TypedDict):
    storage_class: pulumi.Input[_builtins.str]
    date: NotRequired[pulumi.Input[_builtins.str]]
    days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketLifecycleRuleTransitionArgs:
    def __init__(__self__, *, storage_class: pulumi.Input[_builtins.str], date: Optional[pulumi.Input[_builtins.str]] = ..., days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @date.setter
    def date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketLoggingArgsDict(TypedDict):
    target_bucket: pulumi.Input[_builtins.str]
    target_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketLoggingArgs:
    def __init__(__self__, *, target_bucket: pulumi.Input[_builtins.str], target_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetBucket")
    def target_bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_bucket.setter
    def target_bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPrefix")
    def target_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_prefix.setter
    def target_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketLoggingTargetGrantArgsDict(TypedDict):
    grantee: pulumi.Input[BucketLoggingTargetGrantGranteeArgsDict]
    permission: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketLoggingTargetGrantArgs:
    def __init__(__self__, *, grantee: pulumi.Input[BucketLoggingTargetGrantGranteeArgs], permission: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> pulumi.Input[BucketLoggingTargetGrantGranteeArgs]:
        
        ...
    
    @grantee.setter
    def grantee(self, value: pulumi.Input[BucketLoggingTargetGrantGranteeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permission(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @permission.setter
    def permission(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketLoggingTargetGrantGranteeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    email_address: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketLoggingTargetGrantGranteeArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ..., email_address: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    @_utilities.deprecated(...)
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketLoggingTargetObjectKeyFormatArgsDict(TypedDict):
    partitioned_prefix: NotRequired[pulumi.Input[BucketLoggingTargetObjectKeyFormatPartitionedPrefixArgsDict]]
    simple_prefix: NotRequired[pulumi.Input[BucketLoggingTargetObjectKeyFormatSimplePrefixArgsDict]]


@pulumi.input_type
class BucketLoggingTargetObjectKeyFormatArgs:
    def __init__(__self__, *, partitioned_prefix: Optional[pulumi.Input[BucketLoggingTargetObjectKeyFormatPartitionedPrefixArgs]] = ..., simple_prefix: Optional[pulumi.Input[BucketLoggingTargetObjectKeyFormatSimplePrefixArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionedPrefix")
    def partitioned_prefix(self) -> Optional[pulumi.Input[BucketLoggingTargetObjectKeyFormatPartitionedPrefixArgs]]:
        
        ...
    
    @partitioned_prefix.setter
    def partitioned_prefix(self, value: Optional[pulumi.Input[BucketLoggingTargetObjectKeyFormatPartitionedPrefixArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="simplePrefix")
    def simple_prefix(self) -> Optional[pulumi.Input[BucketLoggingTargetObjectKeyFormatSimplePrefixArgs]]:
        
        ...
    
    @simple_prefix.setter
    def simple_prefix(self, value: Optional[pulumi.Input[BucketLoggingTargetObjectKeyFormatSimplePrefixArgs]]): # -> None:
        ...
    


class BucketLoggingTargetObjectKeyFormatPartitionedPrefixArgsDict(TypedDict):
    partition_date_source: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketLoggingTargetObjectKeyFormatPartitionedPrefixArgs:
    def __init__(__self__, *, partition_date_source: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionDateSource")
    def partition_date_source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @partition_date_source.setter
    def partition_date_source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketLoggingTargetObjectKeyFormatSimplePrefixArgsDict(TypedDict):
    ...


@pulumi.input_type
class BucketLoggingTargetObjectKeyFormatSimplePrefixArgs:
    def __init__(__self__) -> None:
        ...
    


class BucketLoggingV2TargetGrantArgsDict(TypedDict):
    grantee: pulumi.Input[BucketLoggingV2TargetGrantGranteeArgsDict]
    permission: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketLoggingV2TargetGrantArgs:
    def __init__(__self__, *, grantee: pulumi.Input[BucketLoggingV2TargetGrantGranteeArgs], permission: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> pulumi.Input[BucketLoggingV2TargetGrantGranteeArgs]:
        
        ...
    
    @grantee.setter
    def grantee(self, value: pulumi.Input[BucketLoggingV2TargetGrantGranteeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permission(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @permission.setter
    def permission(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketLoggingV2TargetGrantGranteeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    email_address: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketLoggingV2TargetGrantGranteeArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ..., email_address: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    @_utilities.deprecated(...)
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketLoggingV2TargetObjectKeyFormatArgsDict(TypedDict):
    partitioned_prefix: NotRequired[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatPartitionedPrefixArgsDict]]
    simple_prefix: NotRequired[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatSimplePrefixArgsDict]]


@pulumi.input_type
class BucketLoggingV2TargetObjectKeyFormatArgs:
    def __init__(__self__, *, partitioned_prefix: Optional[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatPartitionedPrefixArgs]] = ..., simple_prefix: Optional[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatSimplePrefixArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionedPrefix")
    def partitioned_prefix(self) -> Optional[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatPartitionedPrefixArgs]]:
        
        ...
    
    @partitioned_prefix.setter
    def partitioned_prefix(self, value: Optional[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatPartitionedPrefixArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="simplePrefix")
    def simple_prefix(self) -> Optional[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatSimplePrefixArgs]]:
        
        ...
    
    @simple_prefix.setter
    def simple_prefix(self, value: Optional[pulumi.Input[BucketLoggingV2TargetObjectKeyFormatSimplePrefixArgs]]): # -> None:
        ...
    


class BucketLoggingV2TargetObjectKeyFormatPartitionedPrefixArgsDict(TypedDict):
    partition_date_source: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketLoggingV2TargetObjectKeyFormatPartitionedPrefixArgs:
    def __init__(__self__, *, partition_date_source: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionDateSource")
    def partition_date_source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @partition_date_source.setter
    def partition_date_source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketLoggingV2TargetObjectKeyFormatSimplePrefixArgsDict(TypedDict):
    ...


@pulumi.input_type
class BucketLoggingV2TargetObjectKeyFormatSimplePrefixArgs:
    def __init__(__self__) -> None:
        ...
    


class BucketMetadataConfigurationMetadataConfigurationArgsDict(TypedDict):
    inventory_table_configuration: pulumi.Input[BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationArgsDict]
    journal_table_configuration: pulumi.Input[BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationArgsDict]
    destinations: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationDestinationArgsDict]]]]


@pulumi.input_type
class BucketMetadataConfigurationMetadataConfigurationArgs:
    def __init__(__self__, *, inventory_table_configuration: pulumi.Input[BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationArgs], journal_table_configuration: pulumi.Input[BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationArgs], destinations: Optional[pulumi.Input[Sequence[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationDestinationArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inventoryTableConfiguration")
    def inventory_table_configuration(self) -> pulumi.Input[BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationArgs]:
        
        ...
    
    @inventory_table_configuration.setter
    def inventory_table_configuration(self, value: pulumi.Input[BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="journalTableConfiguration")
    def journal_table_configuration(self) -> pulumi.Input[BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationArgs]:
        
        ...
    
    @journal_table_configuration.setter
    def journal_table_configuration(self, value: pulumi.Input[BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationDestinationArgs]]]]:
        
        ...
    
    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationDestinationArgs]]]]): # -> None:
        ...
    


class BucketMetadataConfigurationMetadataConfigurationDestinationArgsDict(TypedDict):
    table_bucket_arn: pulumi.Input[_builtins.str]
    table_bucket_type: pulumi.Input[_builtins.str]
    table_namespace: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketMetadataConfigurationMetadataConfigurationDestinationArgs:
    def __init__(__self__, *, table_bucket_arn: pulumi.Input[_builtins.str], table_bucket_type: pulumi.Input[_builtins.str], table_namespace: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableBucketArn")
    def table_bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_bucket_arn.setter
    def table_bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableBucketType")
    def table_bucket_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_bucket_type.setter
    def table_bucket_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableNamespace")
    def table_namespace(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_namespace.setter
    def table_namespace(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationArgsDict(TypedDict):
    configuration_state: pulumi.Input[_builtins.str]
    encryption_configuration: NotRequired[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationEncryptionConfigurationArgsDict]]
    table_arn: NotRequired[pulumi.Input[_builtins.str]]
    table_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationArgs:
    def __init__(__self__, *, configuration_state: pulumi.Input[_builtins.str], encryption_configuration: Optional[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationEncryptionConfigurationArgs]] = ..., table_arn: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @configuration_state.setter
    def configuration_state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_arn.setter
    def table_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationEncryptionConfigurationArgsDict(TypedDict):
    sse_algorithm: pulumi.Input[_builtins.str]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketMetadataConfigurationMetadataConfigurationInventoryTableConfigurationEncryptionConfigurationArgs:
    def __init__(__self__, *, sse_algorithm: pulumi.Input[_builtins.str], kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sse_algorithm.setter
    def sse_algorithm(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationArgsDict(TypedDict):
    record_expiration: pulumi.Input[BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationRecordExpirationArgsDict]
    encryption_configuration: NotRequired[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationEncryptionConfigurationArgsDict]]
    table_arn: NotRequired[pulumi.Input[_builtins.str]]
    table_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationArgs:
    def __init__(__self__, *, record_expiration: pulumi.Input[BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationRecordExpirationArgs], encryption_configuration: Optional[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationEncryptionConfigurationArgs]] = ..., table_arn: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordExpiration")
    def record_expiration(self) -> pulumi.Input[BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationRecordExpirationArgs]:
        
        ...
    
    @record_expiration.setter
    def record_expiration(self, value: pulumi.Input[BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationRecordExpirationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableArn")
    def table_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_arn.setter
    def table_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationEncryptionConfigurationArgsDict(TypedDict):
    sse_algorithm: pulumi.Input[_builtins.str]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationEncryptionConfigurationArgs:
    def __init__(__self__, *, sse_algorithm: pulumi.Input[_builtins.str], kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sse_algorithm.setter
    def sse_algorithm(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationRecordExpirationArgsDict(TypedDict):
    expiration: pulumi.Input[_builtins.str]
    days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketMetadataConfigurationMetadataConfigurationJournalTableConfigurationRecordExpirationArgs:
    def __init__(__self__, *, expiration: pulumi.Input[_builtins.str], days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expiration.setter
    def expiration(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketMetadataConfigurationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketMetadataConfigurationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketMetricFilterArgsDict(TypedDict):
    access_point: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class BucketMetricFilterArgs:
    def __init__(__self__, *, access_point: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPoint")
    def access_point(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_point.setter
    def access_point(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class BucketNotificationLambdaFunctionArgsDict(TypedDict):
    events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    filter_prefix: NotRequired[pulumi.Input[_builtins.str]]
    filter_suffix: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    lambda_function_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketNotificationLambdaFunctionArgs:
    def __init__(__self__, *, events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], filter_prefix: Optional[pulumi.Input[_builtins.str]] = ..., filter_suffix: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., lambda_function_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @events.setter
    def events(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPrefix")
    def filter_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_prefix.setter
    def filter_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterSuffix")
    def filter_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_suffix.setter
    def filter_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @lambda_function_arn.setter
    def lambda_function_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketNotificationQueueArgsDict(TypedDict):
    events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    queue_arn: pulumi.Input[_builtins.str]
    filter_prefix: NotRequired[pulumi.Input[_builtins.str]]
    filter_suffix: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketNotificationQueueArgs:
    def __init__(__self__, *, events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], queue_arn: pulumi.Input[_builtins.str], filter_prefix: Optional[pulumi.Input[_builtins.str]] = ..., filter_suffix: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @events.setter
    def events(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueArn")
    def queue_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @queue_arn.setter
    def queue_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPrefix")
    def filter_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_prefix.setter
    def filter_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterSuffix")
    def filter_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_suffix.setter
    def filter_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketNotificationTopicArgsDict(TypedDict):
    events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    topic_arn: pulumi.Input[_builtins.str]
    filter_prefix: NotRequired[pulumi.Input[_builtins.str]]
    filter_suffix: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketNotificationTopicArgs:
    def __init__(__self__, *, events: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], topic_arn: pulumi.Input[_builtins.str], filter_prefix: Optional[pulumi.Input[_builtins.str]] = ..., filter_suffix: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def events(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @events.setter
    def events(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @topic_arn.setter
    def topic_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPrefix")
    def filter_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_prefix.setter
    def filter_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterSuffix")
    def filter_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_suffix.setter
    def filter_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketObjectLockConfigurationArgsDict(TypedDict):
    object_lock_enabled: NotRequired[pulumi.Input[_builtins.str]]
    rule: NotRequired[pulumi.Input[BucketObjectLockConfigurationRuleArgsDict]]


@pulumi.input_type
class BucketObjectLockConfigurationArgs:
    def __init__(__self__, *, object_lock_enabled: Optional[pulumi.Input[_builtins.str]] = ..., rule: Optional[pulumi.Input[BucketObjectLockConfigurationRuleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockEnabled")
    @_utilities.deprecated(...)
    def object_lock_enabled(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_lock_enabled.setter
    def object_lock_enabled(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def rule(self) -> Optional[pulumi.Input[BucketObjectLockConfigurationRuleArgs]]:
        
        ...
    
    @rule.setter
    def rule(self, value: Optional[pulumi.Input[BucketObjectLockConfigurationRuleArgs]]): # -> None:
        ...
    


class BucketObjectLockConfigurationRuleArgsDict(TypedDict):
    default_retention: pulumi.Input[BucketObjectLockConfigurationRuleDefaultRetentionArgsDict]


@pulumi.input_type
class BucketObjectLockConfigurationRuleArgs:
    def __init__(__self__, *, default_retention: pulumi.Input[BucketObjectLockConfigurationRuleDefaultRetentionArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRetention")
    def default_retention(self) -> pulumi.Input[BucketObjectLockConfigurationRuleDefaultRetentionArgs]:
        
        ...
    
    @default_retention.setter
    def default_retention(self, value: pulumi.Input[BucketObjectLockConfigurationRuleDefaultRetentionArgs]): # -> None:
        ...
    


class BucketObjectLockConfigurationRuleDefaultRetentionArgsDict(TypedDict):
    days: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    years: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketObjectLockConfigurationRuleDefaultRetentionArgs:
    def __init__(__self__, *, days: Optional[pulumi.Input[_builtins.int]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., years: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def years(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @years.setter
    def years(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketObjectLockConfigurationV2RuleArgsDict(TypedDict):
    default_retention: pulumi.Input[BucketObjectLockConfigurationV2RuleDefaultRetentionArgsDict]


@pulumi.input_type
class BucketObjectLockConfigurationV2RuleArgs:
    def __init__(__self__, *, default_retention: pulumi.Input[BucketObjectLockConfigurationV2RuleDefaultRetentionArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRetention")
    def default_retention(self) -> pulumi.Input[BucketObjectLockConfigurationV2RuleDefaultRetentionArgs]:
        
        ...
    
    @default_retention.setter
    def default_retention(self, value: pulumi.Input[BucketObjectLockConfigurationV2RuleDefaultRetentionArgs]): # -> None:
        ...
    


class BucketObjectLockConfigurationV2RuleDefaultRetentionArgsDict(TypedDict):
    days: NotRequired[pulumi.Input[_builtins.int]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    years: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketObjectLockConfigurationV2RuleDefaultRetentionArgs:
    def __init__(__self__, *, days: Optional[pulumi.Input[_builtins.int]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., years: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def years(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @years.setter
    def years(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketObjectv2OverrideProviderArgsDict(TypedDict):
    default_tags: NotRequired[pulumi.Input[BucketObjectv2OverrideProviderDefaultTagsArgsDict]]


@pulumi.input_type
class BucketObjectv2OverrideProviderArgs:
    def __init__(__self__, *, default_tags: Optional[pulumi.Input[BucketObjectv2OverrideProviderDefaultTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTags")
    def default_tags(self) -> Optional[pulumi.Input[BucketObjectv2OverrideProviderDefaultTagsArgs]]:
        
        ...
    
    @default_tags.setter
    def default_tags(self, value: Optional[pulumi.Input[BucketObjectv2OverrideProviderDefaultTagsArgs]]): # -> None:
        ...
    


class BucketObjectv2OverrideProviderDefaultTagsArgsDict(TypedDict):
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class BucketObjectv2OverrideProviderDefaultTagsArgs:
    def __init__(__self__, *, tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class BucketOwnershipControlsRuleArgsDict(TypedDict):
    object_ownership: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketOwnershipControlsRuleArgs:
    def __init__(__self__, *, object_ownership: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectOwnership")
    def object_ownership(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @object_ownership.setter
    def object_ownership(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketReplicationConfigRuleArgsDict(TypedDict):
    destination: pulumi.Input[BucketReplicationConfigRuleDestinationArgsDict]
    status: pulumi.Input[_builtins.str]
    delete_marker_replication: NotRequired[pulumi.Input[BucketReplicationConfigRuleDeleteMarkerReplicationArgsDict]]
    existing_object_replication: NotRequired[pulumi.Input[BucketReplicationConfigRuleExistingObjectReplicationArgsDict]]
    filter: NotRequired[pulumi.Input[BucketReplicationConfigRuleFilterArgsDict]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    priority: NotRequired[pulumi.Input[_builtins.int]]
    source_selection_criteria: NotRequired[pulumi.Input[BucketReplicationConfigRuleSourceSelectionCriteriaArgsDict]]


@pulumi.input_type
class BucketReplicationConfigRuleArgs:
    def __init__(__self__, *, destination: pulumi.Input[BucketReplicationConfigRuleDestinationArgs], status: pulumi.Input[_builtins.str], delete_marker_replication: Optional[pulumi.Input[BucketReplicationConfigRuleDeleteMarkerReplicationArgs]] = ..., existing_object_replication: Optional[pulumi.Input[BucketReplicationConfigRuleExistingObjectReplicationArgs]] = ..., filter: Optional[pulumi.Input[BucketReplicationConfigRuleFilterArgs]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., source_selection_criteria: Optional[pulumi.Input[BucketReplicationConfigRuleSourceSelectionCriteriaArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[BucketReplicationConfigRuleDestinationArgs]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[BucketReplicationConfigRuleDestinationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteMarkerReplication")
    def delete_marker_replication(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleDeleteMarkerReplicationArgs]]:
        
        ...
    
    @delete_marker_replication.setter
    def delete_marker_replication(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleDeleteMarkerReplicationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="existingObjectReplication")
    def existing_object_replication(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleExistingObjectReplicationArgs]]:
        
        ...
    
    @existing_object_replication.setter
    def existing_object_replication(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleExistingObjectReplicationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleFilterArgs]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""prefix is deprecated. Use filter instead.""")
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSelectionCriteria")
    def source_selection_criteria(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleSourceSelectionCriteriaArgs]]:
        
        ...
    
    @source_selection_criteria.setter
    def source_selection_criteria(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleSourceSelectionCriteriaArgs]]): # -> None:
        ...
    


class BucketReplicationConfigRuleDeleteMarkerReplicationArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketReplicationConfigRuleDeleteMarkerReplicationArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketReplicationConfigRuleDestinationArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    access_control_translation: NotRequired[pulumi.Input[BucketReplicationConfigRuleDestinationAccessControlTranslationArgsDict]]
    account: NotRequired[pulumi.Input[_builtins.str]]
    encryption_configuration: NotRequired[pulumi.Input[BucketReplicationConfigRuleDestinationEncryptionConfigurationArgsDict]]
    metrics: NotRequired[pulumi.Input[BucketReplicationConfigRuleDestinationMetricsArgsDict]]
    replication_time: NotRequired[pulumi.Input[BucketReplicationConfigRuleDestinationReplicationTimeArgsDict]]
    storage_class: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketReplicationConfigRuleDestinationArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], access_control_translation: Optional[pulumi.Input[BucketReplicationConfigRuleDestinationAccessControlTranslationArgs]] = ..., account: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configuration: Optional[pulumi.Input[BucketReplicationConfigRuleDestinationEncryptionConfigurationArgs]] = ..., metrics: Optional[pulumi.Input[BucketReplicationConfigRuleDestinationMetricsArgs]] = ..., replication_time: Optional[pulumi.Input[BucketReplicationConfigRuleDestinationReplicationTimeArgs]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlTranslation")
    def access_control_translation(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleDestinationAccessControlTranslationArgs]]:
        
        ...
    
    @access_control_translation.setter
    def access_control_translation(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleDestinationAccessControlTranslationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account.setter
    def account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleDestinationEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleDestinationEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleDestinationMetricsArgs]]:
        
        ...
    
    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleDestinationMetricsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTime")
    def replication_time(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleDestinationReplicationTimeArgs]]:
        
        ...
    
    @replication_time.setter
    def replication_time(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleDestinationReplicationTimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketReplicationConfigRuleDestinationAccessControlTranslationArgsDict(TypedDict):
    owner: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketReplicationConfigRuleDestinationAccessControlTranslationArgs:
    def __init__(__self__, *, owner: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @owner.setter
    def owner(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketReplicationConfigRuleDestinationEncryptionConfigurationArgsDict(TypedDict):
    replica_kms_key_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketReplicationConfigRuleDestinationEncryptionConfigurationArgs:
    def __init__(__self__, *, replica_kms_key_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaKmsKeyId")
    def replica_kms_key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @replica_kms_key_id.setter
    def replica_kms_key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketReplicationConfigRuleDestinationMetricsArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]
    event_threshold: NotRequired[pulumi.Input[BucketReplicationConfigRuleDestinationMetricsEventThresholdArgsDict]]


@pulumi.input_type
class BucketReplicationConfigRuleDestinationMetricsArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str], event_threshold: Optional[pulumi.Input[BucketReplicationConfigRuleDestinationMetricsEventThresholdArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventThreshold")
    def event_threshold(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleDestinationMetricsEventThresholdArgs]]:
        
        ...
    
    @event_threshold.setter
    def event_threshold(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleDestinationMetricsEventThresholdArgs]]): # -> None:
        ...
    


class BucketReplicationConfigRuleDestinationMetricsEventThresholdArgsDict(TypedDict):
    minutes: pulumi.Input[_builtins.int]


@pulumi.input_type
class BucketReplicationConfigRuleDestinationMetricsEventThresholdArgs:
    def __init__(__self__, *, minutes: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class BucketReplicationConfigRuleDestinationReplicationTimeArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]
    time: pulumi.Input[BucketReplicationConfigRuleDestinationReplicationTimeTimeArgsDict]


@pulumi.input_type
class BucketReplicationConfigRuleDestinationReplicationTimeArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str], time: pulumi.Input[BucketReplicationConfigRuleDestinationReplicationTimeTimeArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> pulumi.Input[BucketReplicationConfigRuleDestinationReplicationTimeTimeArgs]:
        
        ...
    
    @time.setter
    def time(self, value: pulumi.Input[BucketReplicationConfigRuleDestinationReplicationTimeTimeArgs]): # -> None:
        ...
    


class BucketReplicationConfigRuleDestinationReplicationTimeTimeArgsDict(TypedDict):
    minutes: pulumi.Input[_builtins.int]


@pulumi.input_type
class BucketReplicationConfigRuleDestinationReplicationTimeTimeArgs:
    def __init__(__self__, *, minutes: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class BucketReplicationConfigRuleExistingObjectReplicationArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketReplicationConfigRuleExistingObjectReplicationArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketReplicationConfigRuleFilterArgsDict(TypedDict):
    and_: NotRequired[pulumi.Input[BucketReplicationConfigRuleFilterAndArgsDict]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tag: NotRequired[pulumi.Input[BucketReplicationConfigRuleFilterTagArgsDict]]


@pulumi.input_type
class BucketReplicationConfigRuleFilterArgs:
    def __init__(__self__, *, and_: Optional[pulumi.Input[BucketReplicationConfigRuleFilterAndArgs]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., tag: Optional[pulumi.Input[BucketReplicationConfigRuleFilterTagArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleFilterAndArgs]]:
        
        ...
    
    @and_.setter
    def and_(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleFilterAndArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleFilterTagArgs]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleFilterTagArgs]]): # -> None:
        ...
    


class BucketReplicationConfigRuleFilterAndArgsDict(TypedDict):
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class BucketReplicationConfigRuleFilterAndArgs:
    def __init__(__self__, *, prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class BucketReplicationConfigRuleFilterTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketReplicationConfigRuleFilterTagArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketReplicationConfigRuleSourceSelectionCriteriaArgsDict(TypedDict):
    replica_modifications: NotRequired[pulumi.Input[BucketReplicationConfigRuleSourceSelectionCriteriaReplicaModificationsArgsDict]]
    sse_kms_encrypted_objects: NotRequired[pulumi.Input[BucketReplicationConfigRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgsDict]]


@pulumi.input_type
class BucketReplicationConfigRuleSourceSelectionCriteriaArgs:
    def __init__(__self__, *, replica_modifications: Optional[pulumi.Input[BucketReplicationConfigRuleSourceSelectionCriteriaReplicaModificationsArgs]] = ..., sse_kms_encrypted_objects: Optional[pulumi.Input[BucketReplicationConfigRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaModifications")
    def replica_modifications(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleSourceSelectionCriteriaReplicaModificationsArgs]]:
        
        ...
    
    @replica_modifications.setter
    def replica_modifications(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleSourceSelectionCriteriaReplicaModificationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseKmsEncryptedObjects")
    def sse_kms_encrypted_objects(self) -> Optional[pulumi.Input[BucketReplicationConfigRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgs]]:
        
        ...
    
    @sse_kms_encrypted_objects.setter
    def sse_kms_encrypted_objects(self, value: Optional[pulumi.Input[BucketReplicationConfigRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgs]]): # -> None:
        ...
    


class BucketReplicationConfigRuleSourceSelectionCriteriaReplicaModificationsArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketReplicationConfigRuleSourceSelectionCriteriaReplicaModificationsArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketReplicationConfigRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketReplicationConfigRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketReplicationConfigurationArgsDict(TypedDict):
    role: pulumi.Input[_builtins.str]
    rules: pulumi.Input[Sequence[pulumi.Input[BucketReplicationConfigurationRuleArgsDict]]]


@pulumi.input_type
class BucketReplicationConfigurationArgs:
    def __init__(__self__, *, role: pulumi.Input[_builtins.str], rules: pulumi.Input[Sequence[pulumi.Input[BucketReplicationConfigurationRuleArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input[BucketReplicationConfigurationRuleArgs]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input[BucketReplicationConfigurationRuleArgs]]]): # -> None:
        ...
    


class BucketReplicationConfigurationRuleArgsDict(TypedDict):
    destination: pulumi.Input[BucketReplicationConfigurationRuleDestinationArgsDict]
    status: pulumi.Input[_builtins.str]
    delete_marker_replication_status: NotRequired[pulumi.Input[_builtins.str]]
    filter: NotRequired[pulumi.Input[BucketReplicationConfigurationRuleFilterArgsDict]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    priority: NotRequired[pulumi.Input[_builtins.int]]
    source_selection_criteria: NotRequired[pulumi.Input[BucketReplicationConfigurationRuleSourceSelectionCriteriaArgsDict]]


@pulumi.input_type
class BucketReplicationConfigurationRuleArgs:
    def __init__(__self__, *, destination: pulumi.Input[BucketReplicationConfigurationRuleDestinationArgs], status: pulumi.Input[_builtins.str], delete_marker_replication_status: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[BucketReplicationConfigurationRuleFilterArgs]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., source_selection_criteria: Optional[pulumi.Input[BucketReplicationConfigurationRuleSourceSelectionCriteriaArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[BucketReplicationConfigurationRuleDestinationArgs]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[BucketReplicationConfigurationRuleDestinationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteMarkerReplicationStatus")
    def delete_marker_replication_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_marker_replication_status.setter
    def delete_marker_replication_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[BucketReplicationConfigurationRuleFilterArgs]]:
        
        ...
    
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[BucketReplicationConfigurationRuleFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSelectionCriteria")
    def source_selection_criteria(self) -> Optional[pulumi.Input[BucketReplicationConfigurationRuleSourceSelectionCriteriaArgs]]:
        
        ...
    
    @source_selection_criteria.setter
    def source_selection_criteria(self, value: Optional[pulumi.Input[BucketReplicationConfigurationRuleSourceSelectionCriteriaArgs]]): # -> None:
        ...
    


class BucketReplicationConfigurationRuleDestinationArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    access_control_translation: NotRequired[pulumi.Input[BucketReplicationConfigurationRuleDestinationAccessControlTranslationArgsDict]]
    account_id: NotRequired[pulumi.Input[_builtins.str]]
    metrics: NotRequired[pulumi.Input[BucketReplicationConfigurationRuleDestinationMetricsArgsDict]]
    replica_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    replication_time: NotRequired[pulumi.Input[BucketReplicationConfigurationRuleDestinationReplicationTimeArgsDict]]
    storage_class: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketReplicationConfigurationRuleDestinationArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], access_control_translation: Optional[pulumi.Input[BucketReplicationConfigurationRuleDestinationAccessControlTranslationArgs]] = ..., account_id: Optional[pulumi.Input[_builtins.str]] = ..., metrics: Optional[pulumi.Input[BucketReplicationConfigurationRuleDestinationMetricsArgs]] = ..., replica_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., replication_time: Optional[pulumi.Input[BucketReplicationConfigurationRuleDestinationReplicationTimeArgs]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlTranslation")
    def access_control_translation(self) -> Optional[pulumi.Input[BucketReplicationConfigurationRuleDestinationAccessControlTranslationArgs]]:
        
        ...
    
    @access_control_translation.setter
    def access_control_translation(self, value: Optional[pulumi.Input[BucketReplicationConfigurationRuleDestinationAccessControlTranslationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input[BucketReplicationConfigurationRuleDestinationMetricsArgs]]:
        
        ...
    
    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input[BucketReplicationConfigurationRuleDestinationMetricsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaKmsKeyId")
    def replica_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replica_kms_key_id.setter
    def replica_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTime")
    def replication_time(self) -> Optional[pulumi.Input[BucketReplicationConfigurationRuleDestinationReplicationTimeArgs]]:
        
        ...
    
    @replication_time.setter
    def replication_time(self, value: Optional[pulumi.Input[BucketReplicationConfigurationRuleDestinationReplicationTimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketReplicationConfigurationRuleDestinationAccessControlTranslationArgsDict(TypedDict):
    owner: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketReplicationConfigurationRuleDestinationAccessControlTranslationArgs:
    def __init__(__self__, *, owner: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @owner.setter
    def owner(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketReplicationConfigurationRuleDestinationMetricsArgsDict(TypedDict):
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketReplicationConfigurationRuleDestinationMetricsArgs:
    def __init__(__self__, *, minutes: Optional[pulumi.Input[_builtins.int]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketReplicationConfigurationRuleDestinationReplicationTimeArgsDict(TypedDict):
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketReplicationConfigurationRuleDestinationReplicationTimeArgs:
    def __init__(__self__, *, minutes: Optional[pulumi.Input[_builtins.int]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketReplicationConfigurationRuleFilterArgsDict(TypedDict):
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class BucketReplicationConfigurationRuleFilterArgs:
    def __init__(__self__, *, prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class BucketReplicationConfigurationRuleSourceSelectionCriteriaArgsDict(TypedDict):
    sse_kms_encrypted_objects: NotRequired[pulumi.Input[BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgsDict]]


@pulumi.input_type
class BucketReplicationConfigurationRuleSourceSelectionCriteriaArgs:
    def __init__(__self__, *, sse_kms_encrypted_objects: Optional[pulumi.Input[BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseKmsEncryptedObjects")
    def sse_kms_encrypted_objects(self) -> Optional[pulumi.Input[BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgs]]:
        
        ...
    
    @sse_kms_encrypted_objects.setter
    def sse_kms_encrypted_objects(self, value: Optional[pulumi.Input[BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgs]]): # -> None:
        ...
    


class BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]


@pulumi.input_type
class BucketReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectsArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class BucketServerSideEncryptionConfigurationArgsDict(TypedDict):
    rule: pulumi.Input[BucketServerSideEncryptionConfigurationRuleArgsDict]


@pulumi.input_type
class BucketServerSideEncryptionConfigurationArgs:
    def __init__(__self__, *, rule: pulumi.Input[BucketServerSideEncryptionConfigurationRuleArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rule(self) -> pulumi.Input[BucketServerSideEncryptionConfigurationRuleArgs]:
        
        ...
    
    @rule.setter
    def rule(self, value: pulumi.Input[BucketServerSideEncryptionConfigurationRuleArgs]): # -> None:
        ...
    


class BucketServerSideEncryptionConfigurationRuleArgsDict(TypedDict):
    apply_server_side_encryption_by_default: NotRequired[pulumi.Input[BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgsDict]]
    blocked_encryption_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    bucket_key_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class BucketServerSideEncryptionConfigurationRuleArgs:
    def __init__(__self__, *, apply_server_side_encryption_by_default: Optional[pulumi.Input[BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs]] = ..., blocked_encryption_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., bucket_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyServerSideEncryptionByDefault")
    def apply_server_side_encryption_by_default(self) -> Optional[pulumi.Input[BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs]]:
        
        ...
    
    @apply_server_side_encryption_by_default.setter
    def apply_server_side_encryption_by_default(self, value: Optional[pulumi.Input[BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockedEncryptionTypes")
    def blocked_encryption_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @blocked_encryption_types.setter
    def blocked_encryption_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bucket_key_enabled.setter
    def bucket_key_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgsDict(TypedDict):
    sse_algorithm: pulumi.Input[_builtins.str]
    kms_master_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs:
    def __init__(__self__, *, sse_algorithm: pulumi.Input[_builtins.str], kms_master_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sse_algorithm.setter
    def sse_algorithm(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_master_key_id.setter
    def kms_master_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketServerSideEncryptionConfigurationV2RuleArgsDict(TypedDict):
    apply_server_side_encryption_by_default: NotRequired[pulumi.Input[BucketServerSideEncryptionConfigurationV2RuleApplyServerSideEncryptionByDefaultArgsDict]]
    blocked_encryption_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    bucket_key_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class BucketServerSideEncryptionConfigurationV2RuleArgs:
    def __init__(__self__, *, apply_server_side_encryption_by_default: Optional[pulumi.Input[BucketServerSideEncryptionConfigurationV2RuleApplyServerSideEncryptionByDefaultArgs]] = ..., blocked_encryption_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., bucket_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyServerSideEncryptionByDefault")
    def apply_server_side_encryption_by_default(self) -> Optional[pulumi.Input[BucketServerSideEncryptionConfigurationV2RuleApplyServerSideEncryptionByDefaultArgs]]:
        
        ...
    
    @apply_server_side_encryption_by_default.setter
    def apply_server_side_encryption_by_default(self, value: Optional[pulumi.Input[BucketServerSideEncryptionConfigurationV2RuleApplyServerSideEncryptionByDefaultArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockedEncryptionTypes")
    def blocked_encryption_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @blocked_encryption_types.setter
    def blocked_encryption_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bucket_key_enabled.setter
    def bucket_key_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class BucketServerSideEncryptionConfigurationV2RuleApplyServerSideEncryptionByDefaultArgsDict(TypedDict):
    sse_algorithm: pulumi.Input[_builtins.str]
    kms_master_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketServerSideEncryptionConfigurationV2RuleApplyServerSideEncryptionByDefaultArgs:
    def __init__(__self__, *, sse_algorithm: pulumi.Input[_builtins.str], kms_master_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sse_algorithm.setter
    def sse_algorithm(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_master_key_id.setter
    def kms_master_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketV2CorsRuleArgsDict(TypedDict):
    allowed_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allowed_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    expose_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_age_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketV2CorsRuleArgs:
    def __init__(__self__, *, allowed_methods: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], allowed_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., expose_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., max_age_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_methods.setter
    def allowed_methods(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_origins.setter
    def allowed_origins(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_headers.setter
    def allowed_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @expose_headers.setter
    def expose_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_age_seconds.setter
    def max_age_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketV2GrantArgsDict(TypedDict):
    permissions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    type: pulumi.Input[_builtins.str]
    id: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketV2GrantArgs:
    def __init__(__self__, *, permissions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], type: pulumi.Input[_builtins.str], id: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @permissions.setter
    def permissions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketV2LifecycleRuleArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    abort_incomplete_multipart_upload_days: NotRequired[pulumi.Input[_builtins.int]]
    expirations: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleExpirationArgsDict]]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    noncurrent_version_expirations: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleNoncurrentVersionExpirationArgsDict]]]]
    noncurrent_version_transitions: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleNoncurrentVersionTransitionArgsDict]]]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    transitions: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleTransitionArgsDict]]]]


@pulumi.input_type
class BucketV2LifecycleRuleArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], abort_incomplete_multipart_upload_days: Optional[pulumi.Input[_builtins.int]] = ..., expirations: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleExpirationArgs]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., noncurrent_version_expirations: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleNoncurrentVersionExpirationArgs]]]] = ..., noncurrent_version_transitions: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleNoncurrentVersionTransitionArgs]]]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., transitions: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleTransitionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="abortIncompleteMultipartUploadDays")
    def abort_incomplete_multipart_upload_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @abort_incomplete_multipart_upload_days.setter
    def abort_incomplete_multipart_upload_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expirations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleExpirationArgs]]]]:
        
        ...
    
    @expirations.setter
    def expirations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleExpirationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionExpirations")
    def noncurrent_version_expirations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleNoncurrentVersionExpirationArgs]]]]:
        
        ...
    
    @noncurrent_version_expirations.setter
    def noncurrent_version_expirations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleNoncurrentVersionExpirationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentVersionTransitions")
    def noncurrent_version_transitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleNoncurrentVersionTransitionArgs]]]]:
        
        ...
    
    @noncurrent_version_transitions.setter
    def noncurrent_version_transitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleNoncurrentVersionTransitionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleTransitionArgs]]]]:
        
        ...
    
    @transitions.setter
    def transitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2LifecycleRuleTransitionArgs]]]]): # -> None:
        ...
    


class BucketV2LifecycleRuleExpirationArgsDict(TypedDict):
    date: NotRequired[pulumi.Input[_builtins.str]]
    days: NotRequired[pulumi.Input[_builtins.int]]
    expired_object_delete_marker: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class BucketV2LifecycleRuleExpirationArgs:
    def __init__(__self__, *, date: Optional[pulumi.Input[_builtins.str]] = ..., days: Optional[pulumi.Input[_builtins.int]] = ..., expired_object_delete_marker: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @date.setter
    def date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiredObjectDeleteMarker")
    def expired_object_delete_marker(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @expired_object_delete_marker.setter
    def expired_object_delete_marker(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class BucketV2LifecycleRuleNoncurrentVersionExpirationArgsDict(TypedDict):
    days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketV2LifecycleRuleNoncurrentVersionExpirationArgs:
    def __init__(__self__, *, days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketV2LifecycleRuleNoncurrentVersionTransitionArgsDict(TypedDict):
    storage_class: pulumi.Input[_builtins.str]
    days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketV2LifecycleRuleNoncurrentVersionTransitionArgs:
    def __init__(__self__, *, storage_class: pulumi.Input[_builtins.str], days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketV2LifecycleRuleTransitionArgsDict(TypedDict):
    storage_class: pulumi.Input[_builtins.str]
    date: NotRequired[pulumi.Input[_builtins.str]]
    days: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketV2LifecycleRuleTransitionArgs:
    def __init__(__self__, *, storage_class: pulumi.Input[_builtins.str], date: Optional[pulumi.Input[_builtins.str]] = ..., days: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @date.setter
    def date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketV2LoggingArgsDict(TypedDict):
    target_bucket: pulumi.Input[_builtins.str]
    target_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketV2LoggingArgs:
    def __init__(__self__, *, target_bucket: pulumi.Input[_builtins.str], target_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetBucket")
    def target_bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_bucket.setter
    def target_bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPrefix")
    def target_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_prefix.setter
    def target_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketV2ObjectLockConfigurationArgsDict(TypedDict):
    object_lock_enabled: NotRequired[pulumi.Input[_builtins.str]]
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketV2ObjectLockConfigurationRuleArgsDict]]]]


@pulumi.input_type
class BucketV2ObjectLockConfigurationArgs:
    def __init__(__self__, *, object_lock_enabled: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ObjectLockConfigurationRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectLockEnabled")
    @_utilities.deprecated(...)
    def object_lock_enabled(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_lock_enabled.setter
    def object_lock_enabled(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ObjectLockConfigurationRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ObjectLockConfigurationRuleArgs]]]]): # -> None:
        ...
    


class BucketV2ObjectLockConfigurationRuleArgsDict(TypedDict):
    default_retentions: pulumi.Input[Sequence[pulumi.Input[BucketV2ObjectLockConfigurationRuleDefaultRetentionArgsDict]]]


@pulumi.input_type
class BucketV2ObjectLockConfigurationRuleArgs:
    def __init__(__self__, *, default_retentions: pulumi.Input[Sequence[pulumi.Input[BucketV2ObjectLockConfigurationRuleDefaultRetentionArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRetentions")
    def default_retentions(self) -> pulumi.Input[Sequence[pulumi.Input[BucketV2ObjectLockConfigurationRuleDefaultRetentionArgs]]]:
        
        ...
    
    @default_retentions.setter
    def default_retentions(self, value: pulumi.Input[Sequence[pulumi.Input[BucketV2ObjectLockConfigurationRuleDefaultRetentionArgs]]]): # -> None:
        ...
    


class BucketV2ObjectLockConfigurationRuleDefaultRetentionArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]
    days: NotRequired[pulumi.Input[_builtins.int]]
    years: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketV2ObjectLockConfigurationRuleDefaultRetentionArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str], days: Optional[pulumi.Input[_builtins.int]] = ..., years: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def years(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @years.setter
    def years(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketV2ReplicationConfigurationArgsDict(TypedDict):
    role: pulumi.Input[_builtins.str]
    rules: pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleArgsDict]]]


@pulumi.input_type
class BucketV2ReplicationConfigurationArgs:
    def __init__(__self__, *, role: pulumi.Input[_builtins.str], rules: pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleArgs]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleArgs]]]): # -> None:
        ...
    


class BucketV2ReplicationConfigurationRuleArgsDict(TypedDict):
    destinations: pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationArgsDict]]]
    status: pulumi.Input[_builtins.str]
    delete_marker_replication_status: NotRequired[pulumi.Input[_builtins.str]]
    filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleFilterArgsDict]]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    priority: NotRequired[pulumi.Input[_builtins.int]]
    source_selection_criterias: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaArgsDict]]]]


@pulumi.input_type
class BucketV2ReplicationConfigurationRuleArgs:
    def __init__(__self__, *, destinations: pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationArgs]]], status: pulumi.Input[_builtins.str], delete_marker_replication_status: Optional[pulumi.Input[_builtins.str]] = ..., filters: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleFilterArgs]]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ..., priority: Optional[pulumi.Input[_builtins.int]] = ..., source_selection_criterias: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationArgs]]]:
        
        ...
    
    @destinations.setter
    def destinations(self, value: pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteMarkerReplicationStatus")
    def delete_marker_replication_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_marker_replication_status.setter
    def delete_marker_replication_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleFilterArgs]]]]:
        
        ...
    
    @filters.setter
    def filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleFilterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSelectionCriterias")
    def source_selection_criterias(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaArgs]]]]:
        
        ...
    
    @source_selection_criterias.setter
    def source_selection_criterias(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaArgs]]]]): # -> None:
        ...
    


class BucketV2ReplicationConfigurationRuleDestinationArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    access_control_translations: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationAccessControlTranslationArgsDict]]]]
    account_id: NotRequired[pulumi.Input[_builtins.str]]
    metrics: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationMetricArgsDict]]]]
    replica_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    replication_times: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationReplicationTimeArgsDict]]]]
    storage_class: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketV2ReplicationConfigurationRuleDestinationArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], access_control_translations: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationAccessControlTranslationArgs]]]] = ..., account_id: Optional[pulumi.Input[_builtins.str]] = ..., metrics: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationMetricArgs]]]] = ..., replica_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., replication_times: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationReplicationTimeArgs]]]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessControlTranslations")
    def access_control_translations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationAccessControlTranslationArgs]]]]:
        
        ...
    
    @access_control_translations.setter
    def access_control_translations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationAccessControlTranslationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationMetricArgs]]]]:
        
        ...
    
    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationMetricArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaKmsKeyId")
    def replica_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replica_kms_key_id.setter
    def replica_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationTimes")
    def replication_times(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationReplicationTimeArgs]]]]:
        
        ...
    
    @replication_times.setter
    def replication_times(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleDestinationReplicationTimeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketV2ReplicationConfigurationRuleDestinationAccessControlTranslationArgsDict(TypedDict):
    owner: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketV2ReplicationConfigurationRuleDestinationAccessControlTranslationArgs:
    def __init__(__self__, *, owner: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @owner.setter
    def owner(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketV2ReplicationConfigurationRuleDestinationMetricArgsDict(TypedDict):
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketV2ReplicationConfigurationRuleDestinationMetricArgs:
    def __init__(__self__, *, minutes: Optional[pulumi.Input[_builtins.int]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketV2ReplicationConfigurationRuleDestinationReplicationTimeArgsDict(TypedDict):
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketV2ReplicationConfigurationRuleDestinationReplicationTimeArgs:
    def __init__(__self__, *, minutes: Optional[pulumi.Input[_builtins.int]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketV2ReplicationConfigurationRuleFilterArgsDict(TypedDict):
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class BucketV2ReplicationConfigurationRuleFilterArgs:
    def __init__(__self__, *, prefix: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaArgsDict(TypedDict):
    sse_kms_encrypted_objects: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectArgsDict]]]]


@pulumi.input_type
class BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaArgs:
    def __init__(__self__, *, sse_kms_encrypted_objects: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseKmsEncryptedObjects")
    def sse_kms_encrypted_objects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectArgs]]]]:
        
        ...
    
    @sse_kms_encrypted_objects.setter
    def sse_kms_encrypted_objects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectArgs]]]]): # -> None:
        ...
    


class BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]


@pulumi.input_type
class BucketV2ReplicationConfigurationRuleSourceSelectionCriteriaSseKmsEncryptedObjectArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class BucketV2ServerSideEncryptionConfigurationArgsDict(TypedDict):
    rules: pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationRuleArgsDict]]]


@pulumi.input_type
class BucketV2ServerSideEncryptionConfigurationArgs:
    def __init__(__self__, *, rules: pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationRuleArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationRuleArgs]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationRuleArgs]]]): # -> None:
        ...
    


class BucketV2ServerSideEncryptionConfigurationRuleArgsDict(TypedDict):
    apply_server_side_encryption_by_defaults: pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgsDict]]]
    bucket_key_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class BucketV2ServerSideEncryptionConfigurationRuleArgs:
    def __init__(__self__, *, apply_server_side_encryption_by_defaults: pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs]]], bucket_key_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyServerSideEncryptionByDefaults")
    def apply_server_side_encryption_by_defaults(self) -> pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs]]]:
        
        ...
    
    @apply_server_side_encryption_by_defaults.setter
    def apply_server_side_encryption_by_defaults(self, value: pulumi.Input[Sequence[pulumi.Input[BucketV2ServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketKeyEnabled")
    def bucket_key_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @bucket_key_enabled.setter
    def bucket_key_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class BucketV2ServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgsDict(TypedDict):
    sse_algorithm: pulumi.Input[_builtins.str]
    kms_master_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketV2ServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs:
    def __init__(__self__, *, sse_algorithm: pulumi.Input[_builtins.str], kms_master_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sse_algorithm.setter
    def sse_algorithm(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_master_key_id.setter
    def kms_master_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketV2VersioningArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    mfa_delete: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class BucketV2VersioningArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., mfa_delete: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mfaDelete")
    def mfa_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @mfa_delete.setter
    def mfa_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class BucketV2WebsiteArgsDict(TypedDict):
    error_document: NotRequired[pulumi.Input[_builtins.str]]
    index_document: NotRequired[pulumi.Input[_builtins.str]]
    redirect_all_requests_to: NotRequired[pulumi.Input[_builtins.str]]
    routing_rules: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketV2WebsiteArgs:
    def __init__(__self__, *, error_document: Optional[pulumi.Input[_builtins.str]] = ..., index_document: Optional[pulumi.Input[_builtins.str]] = ..., redirect_all_requests_to: Optional[pulumi.Input[_builtins.str]] = ..., routing_rules: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorDocument")
    def error_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_document.setter
    def error_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexDocument")
    def index_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @index_document.setter
    def index_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_all_requests_to.setter
    def redirect_all_requests_to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @routing_rules.setter
    def routing_rules(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketVersioningArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    mfa_delete: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class BucketVersioningArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., mfa_delete: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mfaDelete")
    def mfa_delete(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @mfa_delete.setter
    def mfa_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class BucketVersioningV2VersioningConfigurationArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]
    mfa_delete: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketVersioningV2VersioningConfigurationArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str], mfa_delete: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mfaDelete")
    def mfa_delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mfa_delete.setter
    def mfa_delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketVersioningVersioningConfigurationArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]
    mfa_delete: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketVersioningVersioningConfigurationArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str], mfa_delete: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mfaDelete")
    def mfa_delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mfa_delete.setter
    def mfa_delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketWebsiteArgsDict(TypedDict):
    error_document: NotRequired[pulumi.Input[_builtins.str]]
    index_document: NotRequired[pulumi.Input[_builtins.str]]
    redirect_all_requests_to: NotRequired[pulumi.Input[_builtins.str]]
    routing_rules: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketWebsiteArgs:
    def __init__(__self__, *, error_document: Optional[pulumi.Input[_builtins.str]] = ..., index_document: Optional[pulumi.Input[_builtins.str]] = ..., redirect_all_requests_to: Optional[pulumi.Input[_builtins.str]] = ..., routing_rules: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorDocument")
    def error_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @error_document.setter
    def error_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexDocument")
    def index_document(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @index_document.setter
    def index_document(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectAllRequestsTo")
    def redirect_all_requests_to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_all_requests_to.setter
    def redirect_all_requests_to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @routing_rules.setter
    def routing_rules(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketWebsiteConfigurationErrorDocumentArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketWebsiteConfigurationErrorDocumentArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketWebsiteConfigurationIndexDocumentArgsDict(TypedDict):
    suffix: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketWebsiteConfigurationIndexDocumentArgs:
    def __init__(__self__, *, suffix: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketWebsiteConfigurationRedirectAllRequestsToArgsDict(TypedDict):
    host_name: pulumi.Input[_builtins.str]
    protocol: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketWebsiteConfigurationRedirectAllRequestsToArgs:
    def __init__(__self__, *, host_name: pulumi.Input[_builtins.str], protocol: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host_name.setter
    def host_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketWebsiteConfigurationRoutingRuleArgsDict(TypedDict):
    redirect: pulumi.Input[BucketWebsiteConfigurationRoutingRuleRedirectArgsDict]
    condition: NotRequired[pulumi.Input[BucketWebsiteConfigurationRoutingRuleConditionArgsDict]]


@pulumi.input_type
class BucketWebsiteConfigurationRoutingRuleArgs:
    def __init__(__self__, *, redirect: pulumi.Input[BucketWebsiteConfigurationRoutingRuleRedirectArgs], condition: Optional[pulumi.Input[BucketWebsiteConfigurationRoutingRuleConditionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def redirect(self) -> pulumi.Input[BucketWebsiteConfigurationRoutingRuleRedirectArgs]:
        
        ...
    
    @redirect.setter
    def redirect(self, value: pulumi.Input[BucketWebsiteConfigurationRoutingRuleRedirectArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[BucketWebsiteConfigurationRoutingRuleConditionArgs]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[BucketWebsiteConfigurationRoutingRuleConditionArgs]]): # -> None:
        ...
    


class BucketWebsiteConfigurationRoutingRuleConditionArgsDict(TypedDict):
    http_error_code_returned_equals: NotRequired[pulumi.Input[_builtins.str]]
    key_prefix_equals: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketWebsiteConfigurationRoutingRuleConditionArgs:
    def __init__(__self__, *, http_error_code_returned_equals: Optional[pulumi.Input[_builtins.str]] = ..., key_prefix_equals: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpErrorCodeReturnedEquals")
    def http_error_code_returned_equals(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_error_code_returned_equals.setter
    def http_error_code_returned_equals(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPrefixEquals")
    def key_prefix_equals(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_prefix_equals.setter
    def key_prefix_equals(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketWebsiteConfigurationRoutingRuleRedirectArgsDict(TypedDict):
    host_name: NotRequired[pulumi.Input[_builtins.str]]
    http_redirect_code: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    replace_key_prefix_with: NotRequired[pulumi.Input[_builtins.str]]
    replace_key_with: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketWebsiteConfigurationRoutingRuleRedirectArgs:
    def __init__(__self__, *, host_name: Optional[pulumi.Input[_builtins.str]] = ..., http_redirect_code: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., replace_key_prefix_with: Optional[pulumi.Input[_builtins.str]] = ..., replace_key_with: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpRedirectCode")
    def http_redirect_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_redirect_code.setter
    def http_redirect_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceKeyPrefixWith")
    def replace_key_prefix_with(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replace_key_prefix_with.setter
    def replace_key_prefix_with(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceKeyWith")
    def replace_key_with(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replace_key_with.setter
    def replace_key_with(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketWebsiteConfigurationV2ErrorDocumentArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketWebsiteConfigurationV2ErrorDocumentArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketWebsiteConfigurationV2IndexDocumentArgsDict(TypedDict):
    suffix: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketWebsiteConfigurationV2IndexDocumentArgs:
    def __init__(__self__, *, suffix: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def suffix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @suffix.setter
    def suffix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketWebsiteConfigurationV2RedirectAllRequestsToArgsDict(TypedDict):
    host_name: pulumi.Input[_builtins.str]
    protocol: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketWebsiteConfigurationV2RedirectAllRequestsToArgs:
    def __init__(__self__, *, host_name: pulumi.Input[_builtins.str], protocol: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host_name.setter
    def host_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketWebsiteConfigurationV2RoutingRuleArgsDict(TypedDict):
    redirect: pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleRedirectArgsDict]
    condition: NotRequired[pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleConditionArgsDict]]


@pulumi.input_type
class BucketWebsiteConfigurationV2RoutingRuleArgs:
    def __init__(__self__, *, redirect: pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleRedirectArgs], condition: Optional[pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleConditionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def redirect(self) -> pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleRedirectArgs]:
        
        ...
    
    @redirect.setter
    def redirect(self, value: pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleRedirectArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleConditionArgs]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[BucketWebsiteConfigurationV2RoutingRuleConditionArgs]]): # -> None:
        ...
    


class BucketWebsiteConfigurationV2RoutingRuleConditionArgsDict(TypedDict):
    http_error_code_returned_equals: NotRequired[pulumi.Input[_builtins.str]]
    key_prefix_equals: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketWebsiteConfigurationV2RoutingRuleConditionArgs:
    def __init__(__self__, *, http_error_code_returned_equals: Optional[pulumi.Input[_builtins.str]] = ..., key_prefix_equals: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpErrorCodeReturnedEquals")
    def http_error_code_returned_equals(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_error_code_returned_equals.setter
    def http_error_code_returned_equals(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPrefixEquals")
    def key_prefix_equals(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_prefix_equals.setter
    def key_prefix_equals(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketWebsiteConfigurationV2RoutingRuleRedirectArgsDict(TypedDict):
    host_name: NotRequired[pulumi.Input[_builtins.str]]
    http_redirect_code: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    replace_key_prefix_with: NotRequired[pulumi.Input[_builtins.str]]
    replace_key_with: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketWebsiteConfigurationV2RoutingRuleRedirectArgs:
    def __init__(__self__, *, host_name: Optional[pulumi.Input[_builtins.str]] = ..., http_redirect_code: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., replace_key_prefix_with: Optional[pulumi.Input[_builtins.str]] = ..., replace_key_with: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpRedirectCode")
    def http_redirect_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_redirect_code.setter
    def http_redirect_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceKeyPrefixWith")
    def replace_key_prefix_with(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replace_key_prefix_with.setter
    def replace_key_prefix_with(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceKeyWith")
    def replace_key_with(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replace_key_with.setter
    def replace_key_with(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DirectoryBucketLocationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DirectoryBucketLocationArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InventoryDestinationArgsDict(TypedDict):
    bucket: pulumi.Input[InventoryDestinationBucketArgsDict]


@pulumi.input_type
class InventoryDestinationArgs:
    def __init__(__self__, *, bucket: pulumi.Input[InventoryDestinationBucketArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[InventoryDestinationBucketArgs]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[InventoryDestinationBucketArgs]): # -> None:
        ...
    


class InventoryDestinationBucketArgsDict(TypedDict):
    bucket_arn: pulumi.Input[_builtins.str]
    format: pulumi.Input[_builtins.str]
    account_id: NotRequired[pulumi.Input[_builtins.str]]
    encryption: NotRequired[pulumi.Input[InventoryDestinationBucketEncryptionArgsDict]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InventoryDestinationBucketArgs:
    def __init__(__self__, *, bucket_arn: pulumi.Input[_builtins.str], format: pulumi.Input[_builtins.str], account_id: Optional[pulumi.Input[_builtins.str]] = ..., encryption: Optional[pulumi.Input[InventoryDestinationBucketEncryptionArgs]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketArn")
    def bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_arn.setter
    def bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[InventoryDestinationBucketEncryptionArgs]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[InventoryDestinationBucketEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InventoryDestinationBucketEncryptionArgsDict(TypedDict):
    sse_kms: NotRequired[pulumi.Input[InventoryDestinationBucketEncryptionSseKmsArgsDict]]
    sse_s3: NotRequired[pulumi.Input[InventoryDestinationBucketEncryptionSseS3ArgsDict]]


@pulumi.input_type
class InventoryDestinationBucketEncryptionArgs:
    def __init__(__self__, *, sse_kms: Optional[pulumi.Input[InventoryDestinationBucketEncryptionSseKmsArgs]] = ..., sse_s3: Optional[pulumi.Input[InventoryDestinationBucketEncryptionSseS3Args]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseKms")
    def sse_kms(self) -> Optional[pulumi.Input[InventoryDestinationBucketEncryptionSseKmsArgs]]:
        
        ...
    
    @sse_kms.setter
    def sse_kms(self, value: Optional[pulumi.Input[InventoryDestinationBucketEncryptionSseKmsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseS3")
    def sse_s3(self) -> Optional[pulumi.Input[InventoryDestinationBucketEncryptionSseS3Args]]:
        
        ...
    
    @sse_s3.setter
    def sse_s3(self, value: Optional[pulumi.Input[InventoryDestinationBucketEncryptionSseS3Args]]): # -> None:
        ...
    


class InventoryDestinationBucketEncryptionSseKmsArgsDict(TypedDict):
    key_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class InventoryDestinationBucketEncryptionSseKmsArgs:
    def __init__(__self__, *, key_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_id.setter
    def key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class InventoryDestinationBucketEncryptionSseS3ArgsDict(TypedDict):
    ...


@pulumi.input_type
class InventoryDestinationBucketEncryptionSseS3Args:
    def __init__(__self__) -> None:
        ...
    


class InventoryFilterArgsDict(TypedDict):
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InventoryFilterArgs:
    def __init__(__self__, *, prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InventoryScheduleArgsDict(TypedDict):
    frequency: pulumi.Input[_builtins.str]


@pulumi.input_type
class InventoryScheduleArgs:
    def __init__(__self__, *, frequency: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @frequency.setter
    def frequency(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ObjectCopyGrantArgsDict(TypedDict):
    permissions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    type: pulumi.Input[_builtins.str]
    email: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ObjectCopyGrantArgs:
    def __init__(__self__, *, permissions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], type: pulumi.Input[_builtins.str], email: Optional[pulumi.Input[_builtins.str]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @permissions.setter
    def permissions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ObjectCopyOverrideProviderArgsDict(TypedDict):
    default_tags: NotRequired[pulumi.Input[ObjectCopyOverrideProviderDefaultTagsArgsDict]]


@pulumi.input_type
class ObjectCopyOverrideProviderArgs:
    def __init__(__self__, *, default_tags: Optional[pulumi.Input[ObjectCopyOverrideProviderDefaultTagsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTags")
    def default_tags(self) -> Optional[pulumi.Input[ObjectCopyOverrideProviderDefaultTagsArgs]]:
        
        ...
    
    @default_tags.setter
    def default_tags(self, value: Optional[pulumi.Input[ObjectCopyOverrideProviderDefaultTagsArgs]]): # -> None:
        ...
    


class ObjectCopyOverrideProviderDefaultTagsArgsDict(TypedDict):
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ObjectCopyOverrideProviderDefaultTagsArgs:
    def __init__(__self__, *, tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class PolicyDocumentArgsDict(TypedDict):
    
    statement: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgsDict]]]
    version: pulumi.Input[iam.PolicyDocumentVersion]
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PolicyDocumentArgs:
    def __init__(__self__, *, statement: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]], version: pulumi.Input[iam.PolicyDocumentVersion], id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="Statement")
    def statement(self) -> pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]]:
        ...
    
    @statement.setter
    def statement(self, value: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="Version")
    def version(self) -> pulumi.Input[iam.PolicyDocumentVersion]:
        ...
    
    @version.setter
    def version(self, value: pulumi.Input[iam.PolicyDocumentVersion]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="Id")
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VectorsIndexEncryptionConfigurationArgsDict(TypedDict):
    kms_key_arn: pulumi.Input[_builtins.str]
    sse_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class VectorsIndexEncryptionConfigurationArgs:
    def __init__(__self__, *, kms_key_arn: pulumi.Input[_builtins.str], sse_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseType")
    def sse_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sse_type.setter
    def sse_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VectorsIndexMetadataConfigurationArgsDict(TypedDict):
    non_filterable_metadata_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class VectorsIndexMetadataConfigurationArgs:
    def __init__(__self__, *, non_filterable_metadata_keys: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonFilterableMetadataKeys")
    def non_filterable_metadata_keys(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @non_filterable_metadata_keys.setter
    def non_filterable_metadata_keys(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class VectorsVectorBucketEncryptionConfigurationArgsDict(TypedDict):
    kms_key_arn: pulumi.Input[_builtins.str]
    sse_type: pulumi.Input[_builtins.str]


@pulumi.input_type
class VectorsVectorBucketEncryptionConfigurationArgs:
    def __init__(__self__, *, kms_key_arn: pulumi.Input[_builtins.str], sse_type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sseType")
    def sse_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sse_type.setter
    def sse_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


