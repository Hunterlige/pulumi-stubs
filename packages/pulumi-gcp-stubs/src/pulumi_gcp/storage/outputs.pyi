

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BatchOperationsJobBucketList', 'BatchOperationsJobBucketListBuckets', 'BatchOperationsJobBucketListBucketsManifest', 'BatchOperationsJobBucketListBucketsPrefixList', 'BatchOperationsJobDeleteObject', 'BatchOperationsJobPutMetadata', 'BatchOperationsJobPutObjectHold', 'BatchOperationsJobRewriteObject', 'BucketAutoclass', 'BucketCor', 'BucketCustomPlacementConfig', 'BucketEncryption', 'BucketHierarchicalNamespace', 'BucketIAMBindingCondition', 'BucketIAMMemberCondition', 'BucketIpFilter', 'BucketIpFilterPublicNetworkSource', 'BucketIpFilterVpcNetworkSource', 'BucketLifecycleRule', 'BucketLifecycleRuleAction', 'BucketLifecycleRuleCondition', 'BucketLogging', 'BucketObjectContexts', 'BucketObjectContextsCustom', 'BucketObjectCustomerEncryption', 'BucketObjectRetention', 'BucketRetentionPolicy', 'BucketSoftDeletePolicy', 'BucketVersioning', 'BucketWebsite', ..., 'ControlFolderIntelligenceConfigFilter', ..., ..., ..., ..., 'ControlFolderIntelligenceConfigTrialConfig', ..., 'ControlOrganizationIntelligenceConfigFilter', ..., ..., ..., ..., 'ControlOrganizationIntelligenceConfigTrialConfig', ..., 'ControlProjectIntelligenceConfigFilter', ..., ..., ..., ..., 'ControlProjectIntelligenceConfigTrialConfig', 'DefaultObjectAccessControlProjectTeam', 'InsightsDatasetConfigExcludeCloudStorageBuckets', ..., 'InsightsDatasetConfigExcludeCloudStorageLocations', 'InsightsDatasetConfigIdentity', 'InsightsDatasetConfigIncludeCloudStorageBuckets', ..., 'InsightsDatasetConfigIncludeCloudStorageLocations', 'InsightsDatasetConfigLink', 'InsightsDatasetConfigSourceFolders', 'InsightsDatasetConfigSourceProjects', 'InsightsReportConfigCsvOptions', 'InsightsReportConfigFrequencyOptions', 'InsightsReportConfigFrequencyOptionsEndDate', 'InsightsReportConfigFrequencyOptionsStartDate', 'InsightsReportConfigObjectMetadataReportOptions', ..., ..., 'InsightsReportConfigParquetOptions', 'ManagedFolderIamBindingCondition', 'ManagedFolderIamMemberCondition', 'ObjectAccessControlProjectTeam', 'TransferAgentPoolBandwidthLimit', 'TransferJobEventStream', 'TransferJobLoggingConfig', 'TransferJobNotificationConfig', 'TransferJobReplicationSpec', 'TransferJobReplicationSpecGcsDataSink', 'TransferJobReplicationSpecGcsDataSource', 'TransferJobReplicationSpecObjectConditions', 'TransferJobReplicationSpecTransferOptions', ..., 'TransferJobSchedule', 'TransferJobScheduleScheduleEndDate', 'TransferJobScheduleScheduleStartDate', 'TransferJobScheduleStartTimeOfDay', 'TransferJobTransferSpec', 'TransferJobTransferSpecAwsS3CompatibleDataSource', ..., 'TransferJobTransferSpecAwsS3DataSource', 'TransferJobTransferSpecAwsS3DataSourceAwsAccessKey', 'TransferJobTransferSpecAzureBlobStorageDataSource', ..., ..., 'TransferJobTransferSpecGcsDataSink', 'TransferJobTransferSpecGcsDataSource', 'TransferJobTransferSpecHdfsDataSource', 'TransferJobTransferSpecHttpDataSource', 'TransferJobTransferSpecObjectConditions', 'TransferJobTransferSpecPosixDataSink', 'TransferJobTransferSpecPosixDataSource', 'TransferJobTransferSpecTransferManifest', 'TransferJobTransferSpecTransferOptions', ..., 'GetBucketAutoclassResult', 'GetBucketCorResult', 'GetBucketCustomPlacementConfigResult', 'GetBucketEncryptionResult', 'GetBucketHierarchicalNamespaceResult', 'GetBucketIpFilterResult', 'GetBucketIpFilterPublicNetworkSourceResult', 'GetBucketIpFilterVpcNetworkSourceResult', 'GetBucketLifecycleRuleResult', 'GetBucketLifecycleRuleActionResult', 'GetBucketLifecycleRuleConditionResult', 'GetBucketLoggingResult', 'GetBucketObjectContentContextResult', 'GetBucketObjectContentContextCustomResult', 'GetBucketObjectContentCustomerEncryptionResult', 'GetBucketObjectContentRetentionResult', 'GetBucketObjectContentsBucketObjectResult', 'GetBucketObjectContextResult', 'GetBucketObjectContextCustomResult', 'GetBucketObjectCustomerEncryptionResult', 'GetBucketObjectRetentionResult', 'GetBucketObjectsBucketObjectResult', 'GetBucketRetentionPolicyResult', 'GetBucketSoftDeletePolicyResult', 'GetBucketVersioningResult', 'GetBucketWebsiteResult', 'GetBucketsBucketResult', ..., 'GetControlFolderIntelligenceConfigFilterResult', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'GetControlProjectIntelligenceConfigFilterResult', ..., ..., ..., ..., ..., ..., ..., ..., 'GetInsightsDatasetConfigIdentityResult', ..., ..., ..., 'GetInsightsDatasetConfigLinkResult', 'GetInsightsDatasetConfigSourceFolderResult', 'GetInsightsDatasetConfigSourceProjectResult']
@pulumi.output_type
class BatchOperationsJobBucketList(dict):
    def __init__(__self__, *, buckets: outputs.BatchOperationsJobBucketListBuckets) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buckets(self) -> outputs.BatchOperationsJobBucketListBuckets:
        
        ...
    


@pulumi.output_type
class BatchOperationsJobBucketListBuckets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket: _builtins.str, manifest: Optional[outputs.BatchOperationsJobBucketListBucketsManifest] = ..., prefix_list: Optional[outputs.BatchOperationsJobBucketListBucketsPrefixList] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def manifest(self) -> Optional[outputs.BatchOperationsJobBucketListBucketsManifest]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixList")
    def prefix_list(self) -> Optional[outputs.BatchOperationsJobBucketListBucketsPrefixList]:
        
        ...
    


@pulumi.output_type
class BatchOperationsJobBucketListBucketsManifest(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, manifest_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestLocation")
    def manifest_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchOperationsJobBucketListBucketsPrefixList(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, included_object_prefixes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedObjectPrefixes")
    def included_object_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BatchOperationsJobDeleteObject(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, permanent_object_deletion_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permanentObjectDeletionEnabled")
    def permanent_object_deletion_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class BatchOperationsJobPutMetadata(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cache_control: Optional[_builtins.str] = ..., content_disposition: Optional[_builtins.str] = ..., content_encoding: Optional[_builtins.str] = ..., content_language: Optional[_builtins.str] = ..., content_type: Optional[_builtins.str] = ..., custom_metadata: Optional[Mapping[str, _builtins.str]] = ..., custom_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customMetadata")
    def custom_metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customTime")
    def custom_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchOperationsJobPutObjectHold(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, event_based_hold: Optional[_builtins.str] = ..., temporary_hold: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBasedHold")
    def event_based_hold(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="temporaryHold")
    def temporary_hold(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BatchOperationsJobRewriteObject(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BucketAutoclass(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: _builtins.bool, terminal_storage_class: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminalStorageClass")
    def terminal_storage_class(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BucketCor(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_age_seconds: Optional[_builtins.int] = ..., methods: Optional[Sequence[_builtins.str]] = ..., origins: Optional[Sequence[_builtins.str]] = ..., response_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def origins(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeaders")
    def response_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class BucketCustomPlacementConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLocations")
    def data_locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BucketEncryption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKmsKeyName")
    def default_kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BucketHierarchicalNamespace(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class BucketIAMBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BucketIAMMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BucketIpFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mode: _builtins.str, allow_all_service_agent_access: Optional[_builtins.bool] = ..., allow_cross_org_vpcs: Optional[_builtins.bool] = ..., public_network_source: Optional[outputs.BucketIpFilterPublicNetworkSource] = ..., vpc_network_sources: Optional[Sequence[outputs.BucketIpFilterVpcNetworkSource]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAllServiceAgentAccess")
    def allow_all_service_agent_access(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowCrossOrgVpcs")
    def allow_cross_org_vpcs(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkSource")
    def public_network_source(self) -> Optional[outputs.BucketIpFilterPublicNetworkSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcNetworkSources")
    def vpc_network_sources(self) -> Optional[Sequence[outputs.BucketIpFilterVpcNetworkSource]]:
        
        ...
    


@pulumi.output_type
class BucketIpFilterPublicNetworkSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_ip_cidr_ranges: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedIpCidrRanges")
    def allowed_ip_cidr_ranges(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BucketIpFilterVpcNetworkSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_ip_cidr_ranges: Sequence[_builtins.str], network: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedIpCidrRanges")
    def allowed_ip_cidr_ranges(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BucketLifecycleRule(dict):
    def __init__(__self__, *, action: outputs.BucketLifecycleRuleAction, condition: outputs.BucketLifecycleRuleCondition) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.BucketLifecycleRuleAction:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> outputs.BucketLifecycleRuleCondition:
        
        ...
    


@pulumi.output_type
class BucketLifecycleRuleAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, storage_class: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BucketLifecycleRuleCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, age: Optional[_builtins.int] = ..., created_before: Optional[_builtins.str] = ..., custom_time_before: Optional[_builtins.str] = ..., days_since_custom_time: Optional[_builtins.int] = ..., days_since_noncurrent_time: Optional[_builtins.int] = ..., matches_prefixes: Optional[Sequence[_builtins.str]] = ..., matches_storage_classes: Optional[Sequence[_builtins.str]] = ..., matches_suffixes: Optional[Sequence[_builtins.str]] = ..., noncurrent_time_before: Optional[_builtins.str] = ..., num_newer_versions: Optional[_builtins.int] = ..., send_age_if_zero: Optional[_builtins.bool] = ..., send_days_since_custom_time_if_zero: Optional[_builtins.bool] = ..., send_days_since_noncurrent_time_if_zero: Optional[_builtins.bool] = ..., send_num_newer_versions_if_zero: Optional[_builtins.bool] = ..., with_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def age(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBefore")
    def created_before(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customTimeBefore")
    def custom_time_before(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysSinceCustomTime")
    def days_since_custom_time(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysSinceNoncurrentTime")
    def days_since_noncurrent_time(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchesPrefixes")
    def matches_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchesStorageClasses")
    def matches_storage_classes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchesSuffixes")
    def matches_suffixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentTimeBefore")
    def noncurrent_time_before(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numNewerVersions")
    def num_newer_versions(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendAgeIfZero")
    def send_age_if_zero(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendDaysSinceCustomTimeIfZero")
    def send_days_since_custom_time_if_zero(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendDaysSinceNoncurrentTimeIfZero")
    def send_days_since_noncurrent_time_if_zero(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendNumNewerVersionsIfZero")
    def send_num_newer_versions_if_zero(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="withState")
    def with_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BucketLogging(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_bucket: _builtins.str, log_object_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logBucket")
    def log_bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logObjectPrefix")
    def log_object_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BucketObjectContexts(dict):
    def __init__(__self__, *, customs: Sequence[outputs.BucketObjectContextsCustom]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def customs(self) -> Sequence[outputs.BucketObjectContextsCustom]:
        
        ...
    


@pulumi.output_type
class BucketObjectContextsCustom(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str, create_time: Optional[_builtins.str] = ..., update_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BucketObjectCustomerEncryption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, encryption_key: _builtins.str, encryption_algorithm: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BucketObjectRetention(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mode: _builtins.str, retain_until_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainUntilTime")
    def retain_until_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BucketRetentionPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, retention_period: _builtins.str, is_locked: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLocked")
    def is_locked(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class BucketSoftDeletePolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, effective_time: Optional[_builtins.str] = ..., retention_duration_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDurationSeconds")
    def retention_duration_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BucketVersioning(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class BucketWebsite(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, main_page_suffix: Optional[_builtins.str] = ..., not_found_page: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainPageSuffix")
    def main_page_suffix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notFoundPage")
    def not_found_page(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlFolderIntelligenceConfigEffectiveIntelligenceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, effective_edition: Optional[_builtins.str] = ..., intelligence_config: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveEdition")
    def effective_edition(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intelligenceConfig")
    def intelligence_config(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlFolderIntelligenceConfigFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, excluded_cloud_storage_buckets: Optional[outputs.ControlFolderIntelligenceConfigFilterExcludedCloudStorageBuckets] = ..., excluded_cloud_storage_locations: Optional[outputs.ControlFolderIntelligenceConfigFilterExcludedCloudStorageLocations] = ..., included_cloud_storage_buckets: Optional[outputs.ControlFolderIntelligenceConfigFilterIncludedCloudStorageBuckets] = ..., included_cloud_storage_locations: Optional[outputs.ControlFolderIntelligenceConfigFilterIncludedCloudStorageLocations] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageBuckets")
    def excluded_cloud_storage_buckets(self) -> Optional[outputs.ControlFolderIntelligenceConfigFilterExcludedCloudStorageBuckets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageLocations")
    def excluded_cloud_storage_locations(self) -> Optional[outputs.ControlFolderIntelligenceConfigFilterExcludedCloudStorageLocations]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageBuckets")
    def included_cloud_storage_buckets(self) -> Optional[outputs.ControlFolderIntelligenceConfigFilterIncludedCloudStorageBuckets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageLocations")
    def included_cloud_storage_locations(self) -> Optional[outputs.ControlFolderIntelligenceConfigFilterIncludedCloudStorageLocations]:
        
        ...
    


@pulumi.output_type
class ControlFolderIntelligenceConfigFilterExcludedCloudStorageBuckets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_id_regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlFolderIntelligenceConfigFilterExcludedCloudStorageLocations(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlFolderIntelligenceConfigFilterIncludedCloudStorageBuckets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_id_regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlFolderIntelligenceConfigFilterIncludedCloudStorageLocations(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlFolderIntelligenceConfigTrialConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expire_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlOrganizationIntelligenceConfigEffectiveIntelligenceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, effective_edition: Optional[_builtins.str] = ..., intelligence_config: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveEdition")
    def effective_edition(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intelligenceConfig")
    def intelligence_config(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlOrganizationIntelligenceConfigFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, excluded_cloud_storage_buckets: Optional[outputs.ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageBuckets] = ..., excluded_cloud_storage_locations: Optional[outputs.ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageLocations] = ..., included_cloud_storage_buckets: Optional[outputs.ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageBuckets] = ..., included_cloud_storage_locations: Optional[outputs.ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageLocations] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageBuckets")
    def excluded_cloud_storage_buckets(self) -> Optional[outputs.ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageBuckets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageLocations")
    def excluded_cloud_storage_locations(self) -> Optional[outputs.ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageLocations]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageBuckets")
    def included_cloud_storage_buckets(self) -> Optional[outputs.ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageBuckets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageLocations")
    def included_cloud_storage_locations(self) -> Optional[outputs.ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageLocations]:
        
        ...
    


@pulumi.output_type
class ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageBuckets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_id_regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageLocations(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageBuckets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_id_regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageLocations(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlOrganizationIntelligenceConfigTrialConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expire_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlProjectIntelligenceConfigEffectiveIntelligenceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, effective_edition: Optional[_builtins.str] = ..., intelligence_config: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveEdition")
    def effective_edition(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intelligenceConfig")
    def intelligence_config(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlProjectIntelligenceConfigFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, excluded_cloud_storage_buckets: Optional[outputs.ControlProjectIntelligenceConfigFilterExcludedCloudStorageBuckets] = ..., excluded_cloud_storage_locations: Optional[outputs.ControlProjectIntelligenceConfigFilterExcludedCloudStorageLocations] = ..., included_cloud_storage_buckets: Optional[outputs.ControlProjectIntelligenceConfigFilterIncludedCloudStorageBuckets] = ..., included_cloud_storage_locations: Optional[outputs.ControlProjectIntelligenceConfigFilterIncludedCloudStorageLocations] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageBuckets")
    def excluded_cloud_storage_buckets(self) -> Optional[outputs.ControlProjectIntelligenceConfigFilterExcludedCloudStorageBuckets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageLocations")
    def excluded_cloud_storage_locations(self) -> Optional[outputs.ControlProjectIntelligenceConfigFilterExcludedCloudStorageLocations]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageBuckets")
    def included_cloud_storage_buckets(self) -> Optional[outputs.ControlProjectIntelligenceConfigFilterIncludedCloudStorageBuckets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageLocations")
    def included_cloud_storage_locations(self) -> Optional[outputs.ControlProjectIntelligenceConfigFilterIncludedCloudStorageLocations]:
        
        ...
    


@pulumi.output_type
class ControlProjectIntelligenceConfigFilterExcludedCloudStorageBuckets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_id_regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlProjectIntelligenceConfigFilterExcludedCloudStorageLocations(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlProjectIntelligenceConfigFilterIncludedCloudStorageBuckets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_id_regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlProjectIntelligenceConfigFilterIncludedCloudStorageLocations(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ControlProjectIntelligenceConfigTrialConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expire_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DefaultObjectAccessControlProjectTeam(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, project_number: Optional[_builtins.str] = ..., team: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def team(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsDatasetConfigExcludeCloudStorageBuckets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_storage_buckets: Sequence[outputs.InsightsDatasetConfigExcludeCloudStorageBucketsCloudStorageBucket]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageBuckets")
    def cloud_storage_buckets(self) -> Sequence[outputs.InsightsDatasetConfigExcludeCloudStorageBucketsCloudStorageBucket]:
        
        ...
    


@pulumi.output_type
class InsightsDatasetConfigExcludeCloudStorageBucketsCloudStorageBucket(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: Optional[_builtins.str] = ..., bucket_prefix_regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefixRegex")
    def bucket_prefix_regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsDatasetConfigExcludeCloudStorageLocations(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsDatasetConfigIdentity(dict):
    def __init__(__self__, *, type: _builtins.str, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsDatasetConfigIncludeCloudStorageBuckets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_storage_buckets: Sequence[outputs.InsightsDatasetConfigIncludeCloudStorageBucketsCloudStorageBucket]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageBuckets")
    def cloud_storage_buckets(self) -> Sequence[outputs.InsightsDatasetConfigIncludeCloudStorageBucketsCloudStorageBucket]:
        
        ...
    


@pulumi.output_type
class InsightsDatasetConfigIncludeCloudStorageBucketsCloudStorageBucket(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: Optional[_builtins.str] = ..., bucket_prefix_regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefixRegex")
    def bucket_prefix_regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsDatasetConfigIncludeCloudStorageLocations(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsDatasetConfigLink(dict):
    def __init__(__self__, *, dataset: Optional[_builtins.str] = ..., linked: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def linked(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class InsightsDatasetConfigSourceFolders(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, folder_numbers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderNumbers")
    def folder_numbers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class InsightsDatasetConfigSourceProjects(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, project_numbers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumbers")
    def project_numbers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class InsightsReportConfigCsvOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delimiter: Optional[_builtins.str] = ..., header_required: Optional[_builtins.bool] = ..., record_separator: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerRequired")
    def header_required(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordSeparator")
    def record_separator(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsReportConfigFrequencyOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_date: outputs.InsightsReportConfigFrequencyOptionsEndDate, frequency: _builtins.str, start_date: outputs.InsightsReportConfigFrequencyOptionsStartDate) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> outputs.InsightsReportConfigFrequencyOptionsEndDate:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> outputs.InsightsReportConfigFrequencyOptionsStartDate:
        
        ...
    


@pulumi.output_type
class InsightsReportConfigFrequencyOptionsEndDate(dict):
    def __init__(__self__, *, day: _builtins.int, month: _builtins.int, year: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightsReportConfigFrequencyOptionsStartDate(dict):
    def __init__(__self__, *, day: _builtins.int, month: _builtins.int, year: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightsReportConfigObjectMetadataReportOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metadata_fields: Sequence[_builtins.str], storage_destination_options: outputs.InsightsReportConfigObjectMetadataReportOptionsStorageDestinationOptions, storage_filters: Optional[outputs.InsightsReportConfigObjectMetadataReportOptionsStorageFilters] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataFields")
    def metadata_fields(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageDestinationOptions")
    def storage_destination_options(self) -> outputs.InsightsReportConfigObjectMetadataReportOptionsStorageDestinationOptions:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageFilters")
    def storage_filters(self) -> Optional[outputs.InsightsReportConfigObjectMetadataReportOptionsStorageFilters]:
        
        ...
    


@pulumi.output_type
class InsightsReportConfigObjectMetadataReportOptionsStorageDestinationOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket: _builtins.str, destination_path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPath")
    def destination_path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsReportConfigObjectMetadataReportOptionsStorageFilters(dict):
    def __init__(__self__, *, bucket: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsReportConfigParquetOptions(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class ManagedFolderIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedFolderIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ObjectAccessControlProjectTeam(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, project_number: Optional[_builtins.str] = ..., team: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def team(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferAgentPoolBandwidthLimit(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, limit_mbps: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="limitMbps")
    def limit_mbps(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TransferJobEventStream(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, event_stream_expiration_time: Optional[_builtins.str] = ..., event_stream_start_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventStreamExpirationTime")
    def event_stream_expiration_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventStreamStartTime")
    def event_stream_start_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_on_prem_gcs_transfer_logs: Optional[_builtins.bool] = ..., log_action_states: Optional[Sequence[_builtins.str]] = ..., log_actions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableOnPremGcsTransferLogs")
    def enable_on_prem_gcs_transfer_logs(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logActionStates")
    def log_action_states(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logActions")
    def log_actions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class TransferJobNotificationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, payload_format: _builtins.str, pubsub_topic: _builtins.str, event_types: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadFormat")
    def payload_format(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTypes")
    def event_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class TransferJobReplicationSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gcs_data_sink: Optional[outputs.TransferJobReplicationSpecGcsDataSink] = ..., gcs_data_source: Optional[outputs.TransferJobReplicationSpecGcsDataSource] = ..., object_conditions: Optional[outputs.TransferJobReplicationSpecObjectConditions] = ..., transfer_options: Optional[outputs.TransferJobReplicationSpecTransferOptions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsDataSink")
    def gcs_data_sink(self) -> Optional[outputs.TransferJobReplicationSpecGcsDataSink]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsDataSource")
    def gcs_data_source(self) -> Optional[outputs.TransferJobReplicationSpecGcsDataSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectConditions")
    def object_conditions(self) -> Optional[outputs.TransferJobReplicationSpecObjectConditions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferOptions")
    def transfer_options(self) -> Optional[outputs.TransferJobReplicationSpecTransferOptions]:
        
        ...
    


@pulumi.output_type
class TransferJobReplicationSpecGcsDataSink(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobReplicationSpecGcsDataSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobReplicationSpecObjectConditions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, exclude_prefixes: Optional[Sequence[_builtins.str]] = ..., include_prefixes: Optional[Sequence[_builtins.str]] = ..., last_modified_before: Optional[_builtins.str] = ..., last_modified_since: Optional[_builtins.str] = ..., max_time_elapsed_since_last_modification: Optional[_builtins.str] = ..., min_time_elapsed_since_last_modification: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludePrefixes")
    def exclude_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includePrefixes")
    def include_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBefore")
    def last_modified_before(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedSince")
    def last_modified_since(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTimeElapsedSinceLastModification")
    def max_time_elapsed_since_last_modification(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTimeElapsedSinceLastModification")
    def min_time_elapsed_since_last_modification(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobReplicationSpecTransferOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_objects_from_source_after_transfer: Optional[_builtins.bool] = ..., delete_objects_unique_in_sink: Optional[_builtins.bool] = ..., metadata_options: Optional[outputs.TransferJobReplicationSpecTransferOptionsMetadataOptions] = ..., overwrite_objects_already_existing_in_sink: Optional[_builtins.bool] = ..., overwrite_when: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteObjectsFromSourceAfterTransfer")
    def delete_objects_from_source_after_transfer(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteObjectsUniqueInSink")
    def delete_objects_unique_in_sink(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> Optional[outputs.TransferJobReplicationSpecTransferOptionsMetadataOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteObjectsAlreadyExistingInSink")
    def overwrite_objects_already_existing_in_sink(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteWhen")
    def overwrite_when(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobReplicationSpecTransferOptionsMetadataOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, acl: Optional[_builtins.str] = ..., gid: Optional[_builtins.str] = ..., kms_key: Optional[_builtins.str] = ..., mode: Optional[_builtins.str] = ..., storage_class: Optional[_builtins.str] = ..., symlink: Optional[_builtins.str] = ..., temporary_hold: Optional[_builtins.str] = ..., time_created: Optional[_builtins.str] = ..., uid: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def acl(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def symlink(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="temporaryHold")
    def temporary_hold(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobSchedule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, schedule_start_date: outputs.TransferJobScheduleScheduleStartDate, repeat_interval: Optional[_builtins.str] = ..., schedule_end_date: Optional[outputs.TransferJobScheduleScheduleEndDate] = ..., start_time_of_day: Optional[outputs.TransferJobScheduleStartTimeOfDay] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleStartDate")
    def schedule_start_date(self) -> outputs.TransferJobScheduleScheduleStartDate:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repeatInterval")
    def repeat_interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleEndDate")
    def schedule_end_date(self) -> Optional[outputs.TransferJobScheduleScheduleEndDate]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeOfDay")
    def start_time_of_day(self) -> Optional[outputs.TransferJobScheduleStartTimeOfDay]:
        
        ...
    


@pulumi.output_type
class TransferJobScheduleScheduleEndDate(dict):
    def __init__(__self__, *, day: _builtins.int, month: _builtins.int, year: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class TransferJobScheduleScheduleStartDate(dict):
    def __init__(__self__, *, day: _builtins.int, month: _builtins.int, year: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class TransferJobScheduleStartTimeOfDay(dict):
    def __init__(__self__, *, hours: _builtins.int, minutes: _builtins.int, nanos: _builtins.int, seconds: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_s3_compatible_data_source: Optional[outputs.TransferJobTransferSpecAwsS3CompatibleDataSource] = ..., aws_s3_data_source: Optional[outputs.TransferJobTransferSpecAwsS3DataSource] = ..., azure_blob_storage_data_source: Optional[outputs.TransferJobTransferSpecAzureBlobStorageDataSource] = ..., gcs_data_sink: Optional[outputs.TransferJobTransferSpecGcsDataSink] = ..., gcs_data_source: Optional[outputs.TransferJobTransferSpecGcsDataSource] = ..., hdfs_data_source: Optional[outputs.TransferJobTransferSpecHdfsDataSource] = ..., http_data_source: Optional[outputs.TransferJobTransferSpecHttpDataSource] = ..., object_conditions: Optional[outputs.TransferJobTransferSpecObjectConditions] = ..., posix_data_sink: Optional[outputs.TransferJobTransferSpecPosixDataSink] = ..., posix_data_source: Optional[outputs.TransferJobTransferSpecPosixDataSource] = ..., sink_agent_pool_name: Optional[_builtins.str] = ..., source_agent_pool_name: Optional[_builtins.str] = ..., transfer_manifest: Optional[outputs.TransferJobTransferSpecTransferManifest] = ..., transfer_options: Optional[outputs.TransferJobTransferSpecTransferOptions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsS3CompatibleDataSource")
    def aws_s3_compatible_data_source(self) -> Optional[outputs.TransferJobTransferSpecAwsS3CompatibleDataSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsS3DataSource")
    def aws_s3_data_source(self) -> Optional[outputs.TransferJobTransferSpecAwsS3DataSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBlobStorageDataSource")
    def azure_blob_storage_data_source(self) -> Optional[outputs.TransferJobTransferSpecAzureBlobStorageDataSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsDataSink")
    def gcs_data_sink(self) -> Optional[outputs.TransferJobTransferSpecGcsDataSink]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsDataSource")
    def gcs_data_source(self) -> Optional[outputs.TransferJobTransferSpecGcsDataSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hdfsDataSource")
    def hdfs_data_source(self) -> Optional[outputs.TransferJobTransferSpecHdfsDataSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpDataSource")
    def http_data_source(self) -> Optional[outputs.TransferJobTransferSpecHttpDataSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectConditions")
    def object_conditions(self) -> Optional[outputs.TransferJobTransferSpecObjectConditions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixDataSink")
    def posix_data_sink(self) -> Optional[outputs.TransferJobTransferSpecPosixDataSink]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixDataSource")
    def posix_data_source(self) -> Optional[outputs.TransferJobTransferSpecPosixDataSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sinkAgentPoolName")
    def sink_agent_pool_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAgentPoolName")
    def source_agent_pool_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferManifest")
    def transfer_manifest(self) -> Optional[outputs.TransferJobTransferSpecTransferManifest]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferOptions")
    def transfer_options(self) -> Optional[outputs.TransferJobTransferSpecTransferOptions]:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecAwsS3CompatibleDataSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, endpoint: _builtins.str, path: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., s3_metadata: Optional[outputs.TransferJobTransferSpecAwsS3CompatibleDataSourceS3Metadata] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Metadata")
    def s3_metadata(self) -> Optional[outputs.TransferJobTransferSpecAwsS3CompatibleDataSourceS3Metadata]:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecAwsS3CompatibleDataSourceS3Metadata(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_method: Optional[_builtins.str] = ..., list_api: Optional[_builtins.str] = ..., protocol: Optional[_builtins.str] = ..., request_model: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authMethod")
    def auth_method(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listApi")
    def list_api(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestModel")
    def request_model(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecAwsS3DataSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, aws_access_key: Optional[outputs.TransferJobTransferSpecAwsS3DataSourceAwsAccessKey] = ..., cloudfront_domain: Optional[_builtins.str] = ..., credentials_secret: Optional[_builtins.str] = ..., managed_private_network: Optional[_builtins.bool] = ..., path: Optional[_builtins.str] = ..., role_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccessKey")
    def aws_access_key(self) -> Optional[outputs.TransferJobTransferSpecAwsS3DataSourceAwsAccessKey]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudfrontDomain")
    def cloudfront_domain(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsSecret")
    def credentials_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPrivateNetwork")
    def managed_private_network(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecAwsS3DataSourceAwsAccessKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_key_id: _builtins.str, secret_access_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecAzureBlobStorageDataSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container: _builtins.str, storage_account: _builtins.str, azure_credentials: Optional[outputs.TransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials] = ..., credentials_secret: Optional[_builtins.str] = ..., federated_identity_config: Optional[outputs.TransferJobTransferSpecAzureBlobStorageDataSourceFederatedIdentityConfig] = ..., path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def container(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureCredentials")
    def azure_credentials(self) -> Optional[outputs.TransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsSecret")
    def credentials_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="federatedIdentityConfig")
    def federated_identity_config(self) -> Optional[outputs.TransferJobTransferSpecAzureBlobStorageDataSourceFederatedIdentityConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentials(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, sas_token: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecAzureBlobStorageDataSourceFederatedIdentityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, tenant_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecGcsDataSink(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecGcsDataSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecHdfsDataSource(dict):
    def __init__(__self__, *, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecHttpDataSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, list_url: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listUrl")
    def list_url(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecObjectConditions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, exclude_prefixes: Optional[Sequence[_builtins.str]] = ..., include_prefixes: Optional[Sequence[_builtins.str]] = ..., last_modified_before: Optional[_builtins.str] = ..., last_modified_since: Optional[_builtins.str] = ..., max_time_elapsed_since_last_modification: Optional[_builtins.str] = ..., min_time_elapsed_since_last_modification: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludePrefixes")
    def exclude_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includePrefixes")
    def include_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBefore")
    def last_modified_before(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedSince")
    def last_modified_since(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTimeElapsedSinceLastModification")
    def max_time_elapsed_since_last_modification(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTimeElapsedSinceLastModification")
    def min_time_elapsed_since_last_modification(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecPosixDataSink(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, root_directory: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecPosixDataSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, root_directory: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecTransferManifest(dict):
    def __init__(__self__, *, location: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecTransferOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, delete_objects_from_source_after_transfer: Optional[_builtins.bool] = ..., delete_objects_unique_in_sink: Optional[_builtins.bool] = ..., metadata_options: Optional[outputs.TransferJobTransferSpecTransferOptionsMetadataOptions] = ..., overwrite_objects_already_existing_in_sink: Optional[_builtins.bool] = ..., overwrite_when: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteObjectsFromSourceAfterTransfer")
    def delete_objects_from_source_after_transfer(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteObjectsUniqueInSink")
    def delete_objects_unique_in_sink(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> Optional[outputs.TransferJobTransferSpecTransferOptionsMetadataOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteObjectsAlreadyExistingInSink")
    def overwrite_objects_already_existing_in_sink(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteWhen")
    def overwrite_when(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TransferJobTransferSpecTransferOptionsMetadataOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, acl: Optional[_builtins.str] = ..., gid: Optional[_builtins.str] = ..., kms_key: Optional[_builtins.str] = ..., mode: Optional[_builtins.str] = ..., storage_class: Optional[_builtins.str] = ..., symlink: Optional[_builtins.str] = ..., temporary_hold: Optional[_builtins.str] = ..., time_created: Optional[_builtins.str] = ..., uid: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def acl(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def symlink(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="temporaryHold")
    def temporary_hold(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetBucketAutoclassResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool, terminal_storage_class: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminalStorageClass")
    def terminal_storage_class(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketCorResult(dict):
    def __init__(__self__, *, max_age_seconds: _builtins.int, methods: Sequence[_builtins.str], origins: Sequence[_builtins.str], response_headers: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def origins(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeaders")
    def response_headers(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetBucketCustomPlacementConfigResult(dict):
    def __init__(__self__, *, data_locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLocations")
    def data_locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetBucketEncryptionResult(dict):
    def __init__(__self__, *, default_kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKmsKeyName")
    def default_kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketHierarchicalNamespaceResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetBucketIpFilterResult(dict):
    def __init__(__self__, *, allow_all_service_agent_access: _builtins.bool, allow_cross_org_vpcs: _builtins.bool, mode: _builtins.str, public_network_sources: Sequence[outputs.GetBucketIpFilterPublicNetworkSourceResult], vpc_network_sources: Sequence[outputs.GetBucketIpFilterVpcNetworkSourceResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAllServiceAgentAccess")
    def allow_all_service_agent_access(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowCrossOrgVpcs")
    def allow_cross_org_vpcs(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkSources")
    def public_network_sources(self) -> Sequence[outputs.GetBucketIpFilterPublicNetworkSourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcNetworkSources")
    def vpc_network_sources(self) -> Sequence[outputs.GetBucketIpFilterVpcNetworkSourceResult]:
        
        ...
    


@pulumi.output_type
class GetBucketIpFilterPublicNetworkSourceResult(dict):
    def __init__(__self__, *, allowed_ip_cidr_ranges: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedIpCidrRanges")
    def allowed_ip_cidr_ranges(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetBucketIpFilterVpcNetworkSourceResult(dict):
    def __init__(__self__, *, allowed_ip_cidr_ranges: Sequence[_builtins.str], network: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedIpCidrRanges")
    def allowed_ip_cidr_ranges(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketLifecycleRuleResult(dict):
    def __init__(__self__, *, actions: Sequence[outputs.GetBucketLifecycleRuleActionResult], conditions: Sequence[outputs.GetBucketLifecycleRuleConditionResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.GetBucketLifecycleRuleActionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Sequence[outputs.GetBucketLifecycleRuleConditionResult]:
        
        ...
    


@pulumi.output_type
class GetBucketLifecycleRuleActionResult(dict):
    def __init__(__self__, *, storage_class: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketLifecycleRuleConditionResult(dict):
    def __init__(__self__, *, age: _builtins.int, created_before: _builtins.str, custom_time_before: _builtins.str, days_since_custom_time: _builtins.int, days_since_noncurrent_time: _builtins.int, matches_prefixes: Sequence[_builtins.str], matches_storage_classes: Sequence[_builtins.str], matches_suffixes: Sequence[_builtins.str], noncurrent_time_before: _builtins.str, num_newer_versions: _builtins.int, send_age_if_zero: _builtins.bool, send_days_since_custom_time_if_zero: _builtins.bool, send_days_since_noncurrent_time_if_zero: _builtins.bool, send_num_newer_versions_if_zero: _builtins.bool, with_state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def age(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBefore")
    def created_before(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customTimeBefore")
    def custom_time_before(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysSinceCustomTime")
    def days_since_custom_time(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysSinceNoncurrentTime")
    def days_since_noncurrent_time(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchesPrefixes")
    def matches_prefixes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchesStorageClasses")
    def matches_storage_classes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchesSuffixes")
    def matches_suffixes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentTimeBefore")
    def noncurrent_time_before(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numNewerVersions")
    def num_newer_versions(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendAgeIfZero")
    def send_age_if_zero(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendDaysSinceCustomTimeIfZero")
    def send_days_since_custom_time_if_zero(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendDaysSinceNoncurrentTimeIfZero")
    def send_days_since_noncurrent_time_if_zero(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendNumNewerVersionsIfZero")
    def send_num_newer_versions_if_zero(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="withState")
    def with_state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketLoggingResult(dict):
    def __init__(__self__, *, log_bucket: _builtins.str, log_object_prefix: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logBucket")
    def log_bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logObjectPrefix")
    def log_object_prefix(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketObjectContentContextResult(dict):
    def __init__(__self__, *, customs: Sequence[outputs.GetBucketObjectContentContextCustomResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def customs(self) -> Sequence[outputs.GetBucketObjectContentContextCustomResult]:
        
        ...
    


@pulumi.output_type
class GetBucketObjectContentContextCustomResult(dict):
    def __init__(__self__, *, create_time: _builtins.str, key: _builtins.str, update_time: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketObjectContentCustomerEncryptionResult(dict):
    def __init__(__self__, *, encryption_algorithm: _builtins.str, encryption_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketObjectContentRetentionResult(dict):
    def __init__(__self__, *, mode: _builtins.str, retain_until_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainUntilTime")
    def retain_until_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketObjectContentsBucketObjectResult(dict):
    def __init__(__self__, *, content: _builtins.str, content_base64: _builtins.str, content_base64sha512: _builtins.str, content_hexsha512: _builtins.str, content_type: _builtins.str, media_link: _builtins.str, name: _builtins.str, self_link: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBase64")
    def content_base64(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentBase64sha512")
    def content_base64sha512(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentHexsha512")
    def content_hexsha512(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediaLink")
    def media_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketObjectContextResult(dict):
    def __init__(__self__, *, customs: Sequence[outputs.GetBucketObjectContextCustomResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def customs(self) -> Sequence[outputs.GetBucketObjectContextCustomResult]:
        
        ...
    


@pulumi.output_type
class GetBucketObjectContextCustomResult(dict):
    def __init__(__self__, *, create_time: _builtins.str, key: _builtins.str, update_time: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketObjectCustomerEncryptionResult(dict):
    def __init__(__self__, *, encryption_algorithm: _builtins.str, encryption_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketObjectRetentionResult(dict):
    def __init__(__self__, *, mode: _builtins.str, retain_until_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainUntilTime")
    def retain_until_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketObjectsBucketObjectResult(dict):
    def __init__(__self__, *, content_type: _builtins.str, media_link: _builtins.str, name: _builtins.str, self_link: _builtins.str, storage_class: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediaLink")
    def media_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketRetentionPolicyResult(dict):
    def __init__(__self__, *, is_locked: _builtins.bool, retention_period: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLocked")
    def is_locked(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketSoftDeletePolicyResult(dict):
    def __init__(__self__, *, effective_time: _builtins.str, retention_duration_seconds: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDurationSeconds")
    def retention_duration_seconds(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class GetBucketVersioningResult(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetBucketWebsiteResult(dict):
    def __init__(__self__, *, main_page_suffix: _builtins.str, not_found_page: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainPageSuffix")
    def main_page_suffix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notFoundPage")
    def not_found_page(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetBucketsBucketResult(dict):
    def __init__(__self__, *, labels: Mapping[str, _builtins.str], location: _builtins.str, name: _builtins.str, self_link: _builtins.str, storage_class: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetControlFolderIntelligenceConfigEffectiveIntelligenceConfigResult(dict):
    def __init__(__self__, *, effective_edition: _builtins.str, intelligence_config: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveEdition")
    def effective_edition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intelligenceConfig")
    def intelligence_config(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetControlFolderIntelligenceConfigFilterResult(dict):
    def __init__(__self__, *, excluded_cloud_storage_buckets: Sequence[outputs.GetControlFolderIntelligenceConfigFilterExcludedCloudStorageBucketResult], excluded_cloud_storage_locations: Sequence[outputs.GetControlFolderIntelligenceConfigFilterExcludedCloudStorageLocationResult], included_cloud_storage_buckets: Sequence[outputs.GetControlFolderIntelligenceConfigFilterIncludedCloudStorageBucketResult], included_cloud_storage_locations: Sequence[outputs.GetControlFolderIntelligenceConfigFilterIncludedCloudStorageLocationResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageBuckets")
    def excluded_cloud_storage_buckets(self) -> Sequence[outputs.GetControlFolderIntelligenceConfigFilterExcludedCloudStorageBucketResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageLocations")
    def excluded_cloud_storage_locations(self) -> Sequence[outputs.GetControlFolderIntelligenceConfigFilterExcludedCloudStorageLocationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageBuckets")
    def included_cloud_storage_buckets(self) -> Sequence[outputs.GetControlFolderIntelligenceConfigFilterIncludedCloudStorageBucketResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageLocations")
    def included_cloud_storage_locations(self) -> Sequence[outputs.GetControlFolderIntelligenceConfigFilterIncludedCloudStorageLocationResult]:
        
        ...
    


@pulumi.output_type
class GetControlFolderIntelligenceConfigFilterExcludedCloudStorageBucketResult(dict):
    def __init__(__self__, *, bucket_id_regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetControlFolderIntelligenceConfigFilterExcludedCloudStorageLocationResult(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetControlFolderIntelligenceConfigFilterIncludedCloudStorageBucketResult(dict):
    def __init__(__self__, *, bucket_id_regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetControlFolderIntelligenceConfigFilterIncludedCloudStorageLocationResult(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetControlFolderIntelligenceConfigTrialConfigResult(dict):
    def __init__(__self__, *, expire_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetControlOrganizationIntelligenceConfigEffectiveIntelligenceConfigResult(dict):
    def __init__(__self__, *, effective_edition: _builtins.str, intelligence_config: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveEdition")
    def effective_edition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intelligenceConfig")
    def intelligence_config(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetControlOrganizationIntelligenceConfigFilterResult(dict):
    def __init__(__self__, *, excluded_cloud_storage_buckets: Sequence[outputs.GetControlOrganizationIntelligenceConfigFilterExcludedCloudStorageBucketResult], excluded_cloud_storage_locations: Sequence[outputs.GetControlOrganizationIntelligenceConfigFilterExcludedCloudStorageLocationResult], included_cloud_storage_buckets: Sequence[outputs.GetControlOrganizationIntelligenceConfigFilterIncludedCloudStorageBucketResult], included_cloud_storage_locations: Sequence[outputs.GetControlOrganizationIntelligenceConfigFilterIncludedCloudStorageLocationResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageBuckets")
    def excluded_cloud_storage_buckets(self) -> Sequence[outputs.GetControlOrganizationIntelligenceConfigFilterExcludedCloudStorageBucketResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageLocations")
    def excluded_cloud_storage_locations(self) -> Sequence[outputs.GetControlOrganizationIntelligenceConfigFilterExcludedCloudStorageLocationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageBuckets")
    def included_cloud_storage_buckets(self) -> Sequence[outputs.GetControlOrganizationIntelligenceConfigFilterIncludedCloudStorageBucketResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageLocations")
    def included_cloud_storage_locations(self) -> Sequence[outputs.GetControlOrganizationIntelligenceConfigFilterIncludedCloudStorageLocationResult]:
        
        ...
    


@pulumi.output_type
class GetControlOrganizationIntelligenceConfigFilterExcludedCloudStorageBucketResult(dict):
    def __init__(__self__, *, bucket_id_regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetControlOrganizationIntelligenceConfigFilterExcludedCloudStorageLocationResult(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetControlOrganizationIntelligenceConfigFilterIncludedCloudStorageBucketResult(dict):
    def __init__(__self__, *, bucket_id_regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetControlOrganizationIntelligenceConfigFilterIncludedCloudStorageLocationResult(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetControlOrganizationIntelligenceConfigTrialConfigResult(dict):
    def __init__(__self__, *, expire_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetControlProjectIntelligenceConfigEffectiveIntelligenceConfigResult(dict):
    def __init__(__self__, *, effective_edition: _builtins.str, intelligence_config: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveEdition")
    def effective_edition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intelligenceConfig")
    def intelligence_config(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetControlProjectIntelligenceConfigFilterResult(dict):
    def __init__(__self__, *, excluded_cloud_storage_buckets: Sequence[outputs.GetControlProjectIntelligenceConfigFilterExcludedCloudStorageBucketResult], excluded_cloud_storage_locations: Sequence[outputs.GetControlProjectIntelligenceConfigFilterExcludedCloudStorageLocationResult], included_cloud_storage_buckets: Sequence[outputs.GetControlProjectIntelligenceConfigFilterIncludedCloudStorageBucketResult], included_cloud_storage_locations: Sequence[outputs.GetControlProjectIntelligenceConfigFilterIncludedCloudStorageLocationResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageBuckets")
    def excluded_cloud_storage_buckets(self) -> Sequence[outputs.GetControlProjectIntelligenceConfigFilterExcludedCloudStorageBucketResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageLocations")
    def excluded_cloud_storage_locations(self) -> Sequence[outputs.GetControlProjectIntelligenceConfigFilterExcludedCloudStorageLocationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageBuckets")
    def included_cloud_storage_buckets(self) -> Sequence[outputs.GetControlProjectIntelligenceConfigFilterIncludedCloudStorageBucketResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageLocations")
    def included_cloud_storage_locations(self) -> Sequence[outputs.GetControlProjectIntelligenceConfigFilterIncludedCloudStorageLocationResult]:
        
        ...
    


@pulumi.output_type
class GetControlProjectIntelligenceConfigFilterExcludedCloudStorageBucketResult(dict):
    def __init__(__self__, *, bucket_id_regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetControlProjectIntelligenceConfigFilterExcludedCloudStorageLocationResult(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetControlProjectIntelligenceConfigFilterIncludedCloudStorageBucketResult(dict):
    def __init__(__self__, *, bucket_id_regexes: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetControlProjectIntelligenceConfigFilterIncludedCloudStorageLocationResult(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetControlProjectIntelligenceConfigTrialConfigResult(dict):
    def __init__(__self__, *, expire_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInsightsDatasetConfigExcludeCloudStorageBucketResult(dict):
    def __init__(__self__, *, cloud_storage_buckets: Sequence[outputs.GetInsightsDatasetConfigExcludeCloudStorageBucketCloudStorageBucketResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageBuckets")
    def cloud_storage_buckets(self) -> Sequence[outputs.GetInsightsDatasetConfigExcludeCloudStorageBucketCloudStorageBucketResult]:
        
        ...
    


@pulumi.output_type
class GetInsightsDatasetConfigExcludeCloudStorageBucketCloudStorageBucketResult(dict):
    def __init__(__self__, *, bucket_name: _builtins.str, bucket_prefix_regex: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefixRegex")
    def bucket_prefix_regex(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInsightsDatasetConfigExcludeCloudStorageLocationResult(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInsightsDatasetConfigIdentityResult(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInsightsDatasetConfigIncludeCloudStorageBucketResult(dict):
    def __init__(__self__, *, cloud_storage_buckets: Sequence[outputs.GetInsightsDatasetConfigIncludeCloudStorageBucketCloudStorageBucketResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageBuckets")
    def cloud_storage_buckets(self) -> Sequence[outputs.GetInsightsDatasetConfigIncludeCloudStorageBucketCloudStorageBucketResult]:
        
        ...
    


@pulumi.output_type
class GetInsightsDatasetConfigIncludeCloudStorageBucketCloudStorageBucketResult(dict):
    def __init__(__self__, *, bucket_name: _builtins.str, bucket_prefix_regex: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefixRegex")
    def bucket_prefix_regex(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetInsightsDatasetConfigIncludeCloudStorageLocationResult(dict):
    def __init__(__self__, *, locations: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInsightsDatasetConfigLinkResult(dict):
    def __init__(__self__, *, dataset: _builtins.str, linked: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def linked(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetInsightsDatasetConfigSourceFolderResult(dict):
    def __init__(__self__, *, folder_numbers: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderNumbers")
    def folder_numbers(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetInsightsDatasetConfigSourceProjectResult(dict):
    def __init__(__self__, *, project_numbers: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumbers")
    def project_numbers(self) -> Sequence[_builtins.str]:
        
        ...
    


