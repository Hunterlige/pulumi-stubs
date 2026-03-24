

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BatchOperationsJobBucketListArgs', 'BatchOperationsJobBucketListArgsDict', 'BatchOperationsJobBucketListBucketsArgs', 'BatchOperationsJobBucketListBucketsArgsDict', 'BatchOperationsJobBucketListBucketsManifestArgs', ..., 'BatchOperationsJobBucketListBucketsPrefixListArgs', ..., 'BatchOperationsJobDeleteObjectArgs', 'BatchOperationsJobDeleteObjectArgsDict', 'BatchOperationsJobPutMetadataArgs', 'BatchOperationsJobPutMetadataArgsDict', 'BatchOperationsJobPutObjectHoldArgs', 'BatchOperationsJobPutObjectHoldArgsDict', 'BatchOperationsJobRewriteObjectArgs', 'BatchOperationsJobRewriteObjectArgsDict', 'BucketAutoclassArgs', 'BucketAutoclassArgsDict', 'BucketCorArgs', 'BucketCorArgsDict', 'BucketCustomPlacementConfigArgs', 'BucketCustomPlacementConfigArgsDict', 'BucketEncryptionArgs', 'BucketEncryptionArgsDict', 'BucketHierarchicalNamespaceArgs', 'BucketHierarchicalNamespaceArgsDict', 'BucketIAMBindingConditionArgs', 'BucketIAMBindingConditionArgsDict', 'BucketIAMMemberConditionArgs', 'BucketIAMMemberConditionArgsDict', 'BucketIpFilterArgs', 'BucketIpFilterArgsDict', 'BucketIpFilterPublicNetworkSourceArgs', 'BucketIpFilterPublicNetworkSourceArgsDict', 'BucketIpFilterVpcNetworkSourceArgs', 'BucketIpFilterVpcNetworkSourceArgsDict', 'BucketLifecycleRuleArgs', 'BucketLifecycleRuleArgsDict', 'BucketLifecycleRuleActionArgs', 'BucketLifecycleRuleActionArgsDict', 'BucketLifecycleRuleConditionArgs', 'BucketLifecycleRuleConditionArgsDict', 'BucketLoggingArgs', 'BucketLoggingArgsDict', 'BucketObjectContextsArgs', 'BucketObjectContextsArgsDict', 'BucketObjectContextsCustomArgs', 'BucketObjectContextsCustomArgsDict', 'BucketObjectCustomerEncryptionArgs', 'BucketObjectCustomerEncryptionArgsDict', 'BucketObjectRetentionArgs', 'BucketObjectRetentionArgsDict', 'BucketRetentionPolicyArgs', 'BucketRetentionPolicyArgsDict', 'BucketSoftDeletePolicyArgs', 'BucketSoftDeletePolicyArgsDict', 'BucketVersioningArgs', 'BucketVersioningArgsDict', 'BucketWebsiteArgs', 'BucketWebsiteArgsDict', ..., ..., 'ControlFolderIntelligenceConfigFilterArgs', 'ControlFolderIntelligenceConfigFilterArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'ControlFolderIntelligenceConfigTrialConfigArgs', 'ControlFolderIntelligenceConfigTrialConfigArgsDict', ..., ..., 'ControlOrganizationIntelligenceConfigFilterArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'ControlProjectIntelligenceConfigFilterArgs', 'ControlProjectIntelligenceConfigFilterArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'ControlProjectIntelligenceConfigTrialConfigArgs', ..., 'DefaultObjectAccessControlProjectTeamArgs', 'DefaultObjectAccessControlProjectTeamArgsDict', ..., ..., ..., ..., ..., ..., 'InsightsDatasetConfigIdentityArgs', 'InsightsDatasetConfigIdentityArgsDict', ..., ..., ..., ..., ..., ..., 'InsightsDatasetConfigLinkArgs', 'InsightsDatasetConfigLinkArgsDict', 'InsightsDatasetConfigSourceFoldersArgs', 'InsightsDatasetConfigSourceFoldersArgsDict', 'InsightsDatasetConfigSourceProjectsArgs', 'InsightsDatasetConfigSourceProjectsArgsDict', 'InsightsReportConfigCsvOptionsArgs', 'InsightsReportConfigCsvOptionsArgsDict', 'InsightsReportConfigFrequencyOptionsArgs', 'InsightsReportConfigFrequencyOptionsArgsDict', 'InsightsReportConfigFrequencyOptionsEndDateArgs', ..., 'InsightsReportConfigFrequencyOptionsStartDateArgs', ..., ..., ..., ..., ..., ..., ..., 'InsightsReportConfigParquetOptionsArgs', 'InsightsReportConfigParquetOptionsArgsDict', 'ManagedFolderIamBindingConditionArgs', 'ManagedFolderIamBindingConditionArgsDict', 'ManagedFolderIamMemberConditionArgs', 'ManagedFolderIamMemberConditionArgsDict', 'ObjectAccessControlProjectTeamArgs', 'ObjectAccessControlProjectTeamArgsDict', 'TransferAgentPoolBandwidthLimitArgs', 'TransferAgentPoolBandwidthLimitArgsDict', 'TransferJobEventStreamArgs', 'TransferJobEventStreamArgsDict', 'TransferJobLoggingConfigArgs', 'TransferJobLoggingConfigArgsDict', 'TransferJobNotificationConfigArgs', 'TransferJobNotificationConfigArgsDict', 'TransferJobReplicationSpecArgs', 'TransferJobReplicationSpecArgsDict', 'TransferJobReplicationSpecGcsDataSinkArgs', 'TransferJobReplicationSpecGcsDataSinkArgsDict', 'TransferJobReplicationSpecGcsDataSourceArgs', 'TransferJobReplicationSpecGcsDataSourceArgsDict', 'TransferJobReplicationSpecObjectConditionsArgs', 'TransferJobReplicationSpecObjectConditionsArgsDict', 'TransferJobReplicationSpecTransferOptionsArgs', 'TransferJobReplicationSpecTransferOptionsArgsDict', ..., ..., 'TransferJobScheduleArgs', 'TransferJobScheduleArgsDict', 'TransferJobScheduleScheduleEndDateArgs', 'TransferJobScheduleScheduleEndDateArgsDict', 'TransferJobScheduleScheduleStartDateArgs', 'TransferJobScheduleScheduleStartDateArgsDict', 'TransferJobScheduleStartTimeOfDayArgs', 'TransferJobScheduleStartTimeOfDayArgsDict', 'TransferJobTransferSpecArgs', 'TransferJobTransferSpecArgsDict', ..., ..., ..., ..., 'TransferJobTransferSpecAwsS3DataSourceArgs', 'TransferJobTransferSpecAwsS3DataSourceArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'TransferJobTransferSpecGcsDataSinkArgs', 'TransferJobTransferSpecGcsDataSinkArgsDict', 'TransferJobTransferSpecGcsDataSourceArgs', 'TransferJobTransferSpecGcsDataSourceArgsDict', 'TransferJobTransferSpecHdfsDataSourceArgs', 'TransferJobTransferSpecHdfsDataSourceArgsDict', 'TransferJobTransferSpecHttpDataSourceArgs', 'TransferJobTransferSpecHttpDataSourceArgsDict', 'TransferJobTransferSpecObjectConditionsArgs', 'TransferJobTransferSpecObjectConditionsArgsDict', 'TransferJobTransferSpecPosixDataSinkArgs', 'TransferJobTransferSpecPosixDataSinkArgsDict', 'TransferJobTransferSpecPosixDataSourceArgs', 'TransferJobTransferSpecPosixDataSourceArgsDict', 'TransferJobTransferSpecTransferManifestArgs', 'TransferJobTransferSpecTransferManifestArgsDict', 'TransferJobTransferSpecTransferOptionsArgs', 'TransferJobTransferSpecTransferOptionsArgsDict', ..., ...]
class BatchOperationsJobBucketListArgsDict(TypedDict):
    buckets: pulumi.Input[BatchOperationsJobBucketListBucketsArgsDict]


@pulumi.input_type
class BatchOperationsJobBucketListArgs:
    def __init__(__self__, *, buckets: pulumi.Input[BatchOperationsJobBucketListBucketsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buckets(self) -> pulumi.Input[BatchOperationsJobBucketListBucketsArgs]:
        
        ...
    
    @buckets.setter
    def buckets(self, value: pulumi.Input[BatchOperationsJobBucketListBucketsArgs]): # -> None:
        ...
    


class BatchOperationsJobBucketListBucketsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    manifest: NotRequired[pulumi.Input[BatchOperationsJobBucketListBucketsManifestArgsDict]]
    prefix_list: NotRequired[pulumi.Input[BatchOperationsJobBucketListBucketsPrefixListArgsDict]]


@pulumi.input_type
class BatchOperationsJobBucketListBucketsArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], manifest: Optional[pulumi.Input[BatchOperationsJobBucketListBucketsManifestArgs]] = ..., prefix_list: Optional[pulumi.Input[BatchOperationsJobBucketListBucketsPrefixListArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def manifest(self) -> Optional[pulumi.Input[BatchOperationsJobBucketListBucketsManifestArgs]]:
        
        ...
    
    @manifest.setter
    def manifest(self, value: Optional[pulumi.Input[BatchOperationsJobBucketListBucketsManifestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixList")
    def prefix_list(self) -> Optional[pulumi.Input[BatchOperationsJobBucketListBucketsPrefixListArgs]]:
        
        ...
    
    @prefix_list.setter
    def prefix_list(self, value: Optional[pulumi.Input[BatchOperationsJobBucketListBucketsPrefixListArgs]]): # -> None:
        ...
    


class BatchOperationsJobBucketListBucketsManifestArgsDict(TypedDict):
    manifest_location: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BatchOperationsJobBucketListBucketsManifestArgs:
    def __init__(__self__, *, manifest_location: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestLocation")
    def manifest_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @manifest_location.setter
    def manifest_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BatchOperationsJobBucketListBucketsPrefixListArgsDict(TypedDict):
    included_object_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class BatchOperationsJobBucketListBucketsPrefixListArgs:
    def __init__(__self__, *, included_object_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedObjectPrefixes")
    def included_object_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @included_object_prefixes.setter
    def included_object_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class BatchOperationsJobDeleteObjectArgsDict(TypedDict):
    permanent_object_deletion_enabled: pulumi.Input[_builtins.bool]


@pulumi.input_type
class BatchOperationsJobDeleteObjectArgs:
    def __init__(__self__, *, permanent_object_deletion_enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="permanentObjectDeletionEnabled")
    def permanent_object_deletion_enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @permanent_object_deletion_enabled.setter
    def permanent_object_deletion_enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class BatchOperationsJobPutMetadataArgsDict(TypedDict):
    cache_control: NotRequired[pulumi.Input[_builtins.str]]
    content_disposition: NotRequired[pulumi.Input[_builtins.str]]
    content_encoding: NotRequired[pulumi.Input[_builtins.str]]
    content_language: NotRequired[pulumi.Input[_builtins.str]]
    content_type: NotRequired[pulumi.Input[_builtins.str]]
    custom_metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    custom_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BatchOperationsJobPutMetadataArgs:
    def __init__(__self__, *, cache_control: Optional[pulumi.Input[_builtins.str]] = ..., content_disposition: Optional[pulumi.Input[_builtins.str]] = ..., content_encoding: Optional[pulumi.Input[_builtins.str]] = ..., content_language: Optional[pulumi.Input[_builtins.str]] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., custom_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., custom_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cache_control.setter
    def cache_control(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_disposition.setter
    def content_disposition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_encoding.setter
    def content_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_language.setter
    def content_language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customMetadata")
    def custom_metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @custom_metadata.setter
    def custom_metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customTime")
    def custom_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_time.setter
    def custom_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BatchOperationsJobPutObjectHoldArgsDict(TypedDict):
    event_based_hold: NotRequired[pulumi.Input[_builtins.str]]
    temporary_hold: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BatchOperationsJobPutObjectHoldArgs:
    def __init__(__self__, *, event_based_hold: Optional[pulumi.Input[_builtins.str]] = ..., temporary_hold: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBasedHold")
    def event_based_hold(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_based_hold.setter
    def event_based_hold(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="temporaryHold")
    def temporary_hold(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @temporary_hold.setter
    def temporary_hold(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BatchOperationsJobRewriteObjectArgsDict(TypedDict):
    kms_key: pulumi.Input[_builtins.str]


@pulumi.input_type
class BatchOperationsJobRewriteObjectArgs:
    def __init__(__self__, *, kms_key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketAutoclassArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    terminal_storage_class: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketAutoclassArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], terminal_storage_class: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminalStorageClass")
    def terminal_storage_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @terminal_storage_class.setter
    def terminal_storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketCorArgsDict(TypedDict):
    max_age_seconds: NotRequired[pulumi.Input[_builtins.int]]
    methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    origins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    response_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class BucketCorArgs:
    def __init__(__self__, *, max_age_seconds: Optional[pulumi.Input[_builtins.int]] = ..., methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., origins: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., response_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_age_seconds.setter
    def max_age_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @methods.setter
    def methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def origins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @origins.setter
    def origins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeaders")
    def response_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @response_headers.setter
    def response_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class BucketCustomPlacementConfigArgsDict(TypedDict):
    data_locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class BucketCustomPlacementConfigArgs:
    def __init__(__self__, *, data_locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLocations")
    def data_locations(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @data_locations.setter
    def data_locations(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class BucketEncryptionArgsDict(TypedDict):
    default_kms_key_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketEncryptionArgs:
    def __init__(__self__, *, default_kms_key_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKmsKeyName")
    def default_kms_key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @default_kms_key_name.setter
    def default_kms_key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketHierarchicalNamespaceArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]


@pulumi.input_type
class BucketHierarchicalNamespaceArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class BucketIAMBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketIAMBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketIAMMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketIAMMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketIpFilterArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]
    allow_all_service_agent_access: NotRequired[pulumi.Input[_builtins.bool]]
    allow_cross_org_vpcs: NotRequired[pulumi.Input[_builtins.bool]]
    public_network_source: NotRequired[pulumi.Input[BucketIpFilterPublicNetworkSourceArgsDict]]
    vpc_network_sources: NotRequired[pulumi.Input[Sequence[pulumi.Input[BucketIpFilterVpcNetworkSourceArgsDict]]]]


@pulumi.input_type
class BucketIpFilterArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str], allow_all_service_agent_access: Optional[pulumi.Input[_builtins.bool]] = ..., allow_cross_org_vpcs: Optional[pulumi.Input[_builtins.bool]] = ..., public_network_source: Optional[pulumi.Input[BucketIpFilterPublicNetworkSourceArgs]] = ..., vpc_network_sources: Optional[pulumi.Input[Sequence[pulumi.Input[BucketIpFilterVpcNetworkSourceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAllServiceAgentAccess")
    def allow_all_service_agent_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_all_service_agent_access.setter
    def allow_all_service_agent_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowCrossOrgVpcs")
    def allow_cross_org_vpcs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_cross_org_vpcs.setter
    def allow_cross_org_vpcs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkSource")
    def public_network_source(self) -> Optional[pulumi.Input[BucketIpFilterPublicNetworkSourceArgs]]:
        
        ...
    
    @public_network_source.setter
    def public_network_source(self, value: Optional[pulumi.Input[BucketIpFilterPublicNetworkSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcNetworkSources")
    def vpc_network_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BucketIpFilterVpcNetworkSourceArgs]]]]:
        
        ...
    
    @vpc_network_sources.setter
    def vpc_network_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BucketIpFilterVpcNetworkSourceArgs]]]]): # -> None:
        ...
    


class BucketIpFilterPublicNetworkSourceArgsDict(TypedDict):
    allowed_ip_cidr_ranges: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class BucketIpFilterPublicNetworkSourceArgs:
    def __init__(__self__, *, allowed_ip_cidr_ranges: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedIpCidrRanges")
    def allowed_ip_cidr_ranges(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_ip_cidr_ranges.setter
    def allowed_ip_cidr_ranges(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class BucketIpFilterVpcNetworkSourceArgsDict(TypedDict):
    allowed_ip_cidr_ranges: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    network: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketIpFilterVpcNetworkSourceArgs:
    def __init__(__self__, *, allowed_ip_cidr_ranges: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], network: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedIpCidrRanges")
    def allowed_ip_cidr_ranges(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_ip_cidr_ranges.setter
    def allowed_ip_cidr_ranges(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketLifecycleRuleArgsDict(TypedDict):
    action: pulumi.Input[BucketLifecycleRuleActionArgsDict]
    condition: pulumi.Input[BucketLifecycleRuleConditionArgsDict]


@pulumi.input_type
class BucketLifecycleRuleArgs:
    def __init__(__self__, *, action: pulumi.Input[BucketLifecycleRuleActionArgs], condition: pulumi.Input[BucketLifecycleRuleConditionArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[BucketLifecycleRuleActionArgs]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[BucketLifecycleRuleActionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Input[BucketLifecycleRuleConditionArgs]:
        
        ...
    
    @condition.setter
    def condition(self, value: pulumi.Input[BucketLifecycleRuleConditionArgs]): # -> None:
        ...
    


class BucketLifecycleRuleActionArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    storage_class: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketLifecycleRuleActionArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], storage_class: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketLifecycleRuleConditionArgsDict(TypedDict):
    age: NotRequired[pulumi.Input[_builtins.int]]
    created_before: NotRequired[pulumi.Input[_builtins.str]]
    custom_time_before: NotRequired[pulumi.Input[_builtins.str]]
    days_since_custom_time: NotRequired[pulumi.Input[_builtins.int]]
    days_since_noncurrent_time: NotRequired[pulumi.Input[_builtins.int]]
    matches_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    matches_storage_classes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    matches_suffixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    noncurrent_time_before: NotRequired[pulumi.Input[_builtins.str]]
    num_newer_versions: NotRequired[pulumi.Input[_builtins.int]]
    send_age_if_zero: NotRequired[pulumi.Input[_builtins.bool]]
    send_days_since_custom_time_if_zero: NotRequired[pulumi.Input[_builtins.bool]]
    send_days_since_noncurrent_time_if_zero: NotRequired[pulumi.Input[_builtins.bool]]
    send_num_newer_versions_if_zero: NotRequired[pulumi.Input[_builtins.bool]]
    with_state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketLifecycleRuleConditionArgs:
    def __init__(__self__, *, age: Optional[pulumi.Input[_builtins.int]] = ..., created_before: Optional[pulumi.Input[_builtins.str]] = ..., custom_time_before: Optional[pulumi.Input[_builtins.str]] = ..., days_since_custom_time: Optional[pulumi.Input[_builtins.int]] = ..., days_since_noncurrent_time: Optional[pulumi.Input[_builtins.int]] = ..., matches_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., matches_storage_classes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., matches_suffixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., noncurrent_time_before: Optional[pulumi.Input[_builtins.str]] = ..., num_newer_versions: Optional[pulumi.Input[_builtins.int]] = ..., send_age_if_zero: Optional[pulumi.Input[_builtins.bool]] = ..., send_days_since_custom_time_if_zero: Optional[pulumi.Input[_builtins.bool]] = ..., send_days_since_noncurrent_time_if_zero: Optional[pulumi.Input[_builtins.bool]] = ..., send_num_newer_versions_if_zero: Optional[pulumi.Input[_builtins.bool]] = ..., with_state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def age(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @age.setter
    def age(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBefore")
    def created_before(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_before.setter
    def created_before(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customTimeBefore")
    def custom_time_before(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_time_before.setter
    def custom_time_before(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysSinceCustomTime")
    def days_since_custom_time(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days_since_custom_time.setter
    def days_since_custom_time(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysSinceNoncurrentTime")
    def days_since_noncurrent_time(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @days_since_noncurrent_time.setter
    def days_since_noncurrent_time(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchesPrefixes")
    def matches_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @matches_prefixes.setter
    def matches_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchesStorageClasses")
    def matches_storage_classes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @matches_storage_classes.setter
    def matches_storage_classes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchesSuffixes")
    def matches_suffixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @matches_suffixes.setter
    def matches_suffixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noncurrentTimeBefore")
    def noncurrent_time_before(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @noncurrent_time_before.setter
    def noncurrent_time_before(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numNewerVersions")
    def num_newer_versions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_newer_versions.setter
    def num_newer_versions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendAgeIfZero")
    def send_age_if_zero(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @send_age_if_zero.setter
    def send_age_if_zero(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendDaysSinceCustomTimeIfZero")
    def send_days_since_custom_time_if_zero(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @send_days_since_custom_time_if_zero.setter
    def send_days_since_custom_time_if_zero(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendDaysSinceNoncurrentTimeIfZero")
    def send_days_since_noncurrent_time_if_zero(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @send_days_since_noncurrent_time_if_zero.setter
    def send_days_since_noncurrent_time_if_zero(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendNumNewerVersionsIfZero")
    def send_num_newer_versions_if_zero(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @send_num_newer_versions_if_zero.setter
    def send_num_newer_versions_if_zero(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="withState")
    def with_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @with_state.setter
    def with_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketLoggingArgsDict(TypedDict):
    log_bucket: pulumi.Input[_builtins.str]
    log_object_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketLoggingArgs:
    def __init__(__self__, *, log_bucket: pulumi.Input[_builtins.str], log_object_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logBucket")
    def log_bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_bucket.setter
    def log_bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logObjectPrefix")
    def log_object_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_object_prefix.setter
    def log_object_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketObjectContextsArgsDict(TypedDict):
    customs: pulumi.Input[Sequence[pulumi.Input[BucketObjectContextsCustomArgsDict]]]


@pulumi.input_type
class BucketObjectContextsArgs:
    def __init__(__self__, *, customs: pulumi.Input[Sequence[pulumi.Input[BucketObjectContextsCustomArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def customs(self) -> pulumi.Input[Sequence[pulumi.Input[BucketObjectContextsCustomArgs]]]:
        
        ...
    
    @customs.setter
    def customs(self, value: pulumi.Input[Sequence[pulumi.Input[BucketObjectContextsCustomArgs]]]): # -> None:
        ...
    


class BucketObjectContextsCustomArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketObjectContextsCustomArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str], create_time: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketObjectCustomerEncryptionArgsDict(TypedDict):
    encryption_key: pulumi.Input[_builtins.str]
    encryption_algorithm: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketObjectCustomerEncryptionArgs:
    def __init__(__self__, *, encryption_key: pulumi.Input[_builtins.str], encryption_algorithm: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @encryption_key.setter
    def encryption_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_algorithm.setter
    def encryption_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BucketObjectRetentionArgsDict(TypedDict):
    mode: pulumi.Input[_builtins.str]
    retain_until_time: pulumi.Input[_builtins.str]


@pulumi.input_type
class BucketObjectRetentionArgs:
    def __init__(__self__, *, mode: pulumi.Input[_builtins.str], retain_until_time: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @mode.setter
    def mode(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retainUntilTime")
    def retain_until_time(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @retain_until_time.setter
    def retain_until_time(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class BucketRetentionPolicyArgsDict(TypedDict):
    retention_period: pulumi.Input[_builtins.str]
    is_locked: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class BucketRetentionPolicyArgs:
    def __init__(__self__, *, retention_period: pulumi.Input[_builtins.str], is_locked: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @retention_period.setter
    def retention_period(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLocked")
    def is_locked(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_locked.setter
    def is_locked(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class BucketSoftDeletePolicyArgsDict(TypedDict):
    effective_time: NotRequired[pulumi.Input[_builtins.str]]
    retention_duration_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class BucketSoftDeletePolicyArgs:
    def __init__(__self__, *, effective_time: Optional[pulumi.Input[_builtins.str]] = ..., retention_duration_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effective_time.setter
    def effective_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retentionDurationSeconds")
    def retention_duration_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @retention_duration_seconds.setter
    def retention_duration_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class BucketVersioningArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]


@pulumi.input_type
class BucketVersioningArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class BucketWebsiteArgsDict(TypedDict):
    main_page_suffix: NotRequired[pulumi.Input[_builtins.str]]
    not_found_page: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BucketWebsiteArgs:
    def __init__(__self__, *, main_page_suffix: Optional[pulumi.Input[_builtins.str]] = ..., not_found_page: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mainPageSuffix")
    def main_page_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @main_page_suffix.setter
    def main_page_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notFoundPage")
    def not_found_page(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @not_found_page.setter
    def not_found_page(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ControlFolderIntelligenceConfigEffectiveIntelligenceConfigArgsDict(TypedDict):
    effective_edition: NotRequired[pulumi.Input[_builtins.str]]
    intelligence_config: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ControlFolderIntelligenceConfigEffectiveIntelligenceConfigArgs:
    def __init__(__self__, *, effective_edition: Optional[pulumi.Input[_builtins.str]] = ..., intelligence_config: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveEdition")
    def effective_edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effective_edition.setter
    def effective_edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="intelligenceConfig")
    def intelligence_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @intelligence_config.setter
    def intelligence_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ControlFolderIntelligenceConfigFilterArgsDict(TypedDict):
    excluded_cloud_storage_buckets: NotRequired[pulumi.Input[ControlFolderIntelligenceConfigFilterExcludedCloudStorageBucketsArgsDict]]
    excluded_cloud_storage_locations: NotRequired[pulumi.Input[ControlFolderIntelligenceConfigFilterExcludedCloudStorageLocationsArgsDict]]
    included_cloud_storage_buckets: NotRequired[pulumi.Input[ControlFolderIntelligenceConfigFilterIncludedCloudStorageBucketsArgsDict]]
    included_cloud_storage_locations: NotRequired[pulumi.Input[ControlFolderIntelligenceConfigFilterIncludedCloudStorageLocationsArgsDict]]


@pulumi.input_type
class ControlFolderIntelligenceConfigFilterArgs:
    def __init__(__self__, *, excluded_cloud_storage_buckets: Optional[pulumi.Input[ControlFolderIntelligenceConfigFilterExcludedCloudStorageBucketsArgs]] = ..., excluded_cloud_storage_locations: Optional[pulumi.Input[ControlFolderIntelligenceConfigFilterExcludedCloudStorageLocationsArgs]] = ..., included_cloud_storage_buckets: Optional[pulumi.Input[ControlFolderIntelligenceConfigFilterIncludedCloudStorageBucketsArgs]] = ..., included_cloud_storage_locations: Optional[pulumi.Input[ControlFolderIntelligenceConfigFilterIncludedCloudStorageLocationsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageBuckets")
    def excluded_cloud_storage_buckets(self) -> Optional[pulumi.Input[ControlFolderIntelligenceConfigFilterExcludedCloudStorageBucketsArgs]]:
        
        ...
    
    @excluded_cloud_storage_buckets.setter
    def excluded_cloud_storage_buckets(self, value: Optional[pulumi.Input[ControlFolderIntelligenceConfigFilterExcludedCloudStorageBucketsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageLocations")
    def excluded_cloud_storage_locations(self) -> Optional[pulumi.Input[ControlFolderIntelligenceConfigFilterExcludedCloudStorageLocationsArgs]]:
        
        ...
    
    @excluded_cloud_storage_locations.setter
    def excluded_cloud_storage_locations(self, value: Optional[pulumi.Input[ControlFolderIntelligenceConfigFilterExcludedCloudStorageLocationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageBuckets")
    def included_cloud_storage_buckets(self) -> Optional[pulumi.Input[ControlFolderIntelligenceConfigFilterIncludedCloudStorageBucketsArgs]]:
        
        ...
    
    @included_cloud_storage_buckets.setter
    def included_cloud_storage_buckets(self, value: Optional[pulumi.Input[ControlFolderIntelligenceConfigFilterIncludedCloudStorageBucketsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageLocations")
    def included_cloud_storage_locations(self) -> Optional[pulumi.Input[ControlFolderIntelligenceConfigFilterIncludedCloudStorageLocationsArgs]]:
        
        ...
    
    @included_cloud_storage_locations.setter
    def included_cloud_storage_locations(self, value: Optional[pulumi.Input[ControlFolderIntelligenceConfigFilterIncludedCloudStorageLocationsArgs]]): # -> None:
        ...
    


class ControlFolderIntelligenceConfigFilterExcludedCloudStorageBucketsArgsDict(TypedDict):
    bucket_id_regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ControlFolderIntelligenceConfigFilterExcludedCloudStorageBucketsArgs:
    def __init__(__self__, *, bucket_id_regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @bucket_id_regexes.setter
    def bucket_id_regexes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ControlFolderIntelligenceConfigFilterExcludedCloudStorageLocationsArgsDict(TypedDict):
    locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ControlFolderIntelligenceConfigFilterExcludedCloudStorageLocationsArgs:
    def __init__(__self__, *, locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ControlFolderIntelligenceConfigFilterIncludedCloudStorageBucketsArgsDict(TypedDict):
    bucket_id_regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ControlFolderIntelligenceConfigFilterIncludedCloudStorageBucketsArgs:
    def __init__(__self__, *, bucket_id_regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @bucket_id_regexes.setter
    def bucket_id_regexes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ControlFolderIntelligenceConfigFilterIncludedCloudStorageLocationsArgsDict(TypedDict):
    locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ControlFolderIntelligenceConfigFilterIncludedCloudStorageLocationsArgs:
    def __init__(__self__, *, locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ControlFolderIntelligenceConfigTrialConfigArgsDict(TypedDict):
    expire_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ControlFolderIntelligenceConfigTrialConfigArgs:
    def __init__(__self__, *, expire_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ControlOrganizationIntelligenceConfigEffectiveIntelligenceConfigArgsDict(TypedDict):
    effective_edition: NotRequired[pulumi.Input[_builtins.str]]
    intelligence_config: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ControlOrganizationIntelligenceConfigEffectiveIntelligenceConfigArgs:
    def __init__(__self__, *, effective_edition: Optional[pulumi.Input[_builtins.str]] = ..., intelligence_config: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveEdition")
    def effective_edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effective_edition.setter
    def effective_edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="intelligenceConfig")
    def intelligence_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @intelligence_config.setter
    def intelligence_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ControlOrganizationIntelligenceConfigFilterArgsDict(TypedDict):
    excluded_cloud_storage_buckets: NotRequired[pulumi.Input[ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageBucketsArgsDict]]
    excluded_cloud_storage_locations: NotRequired[pulumi.Input[ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageLocationsArgsDict]]
    included_cloud_storage_buckets: NotRequired[pulumi.Input[ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageBucketsArgsDict]]
    included_cloud_storage_locations: NotRequired[pulumi.Input[ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageLocationsArgsDict]]


@pulumi.input_type
class ControlOrganizationIntelligenceConfigFilterArgs:
    def __init__(__self__, *, excluded_cloud_storage_buckets: Optional[pulumi.Input[ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageBucketsArgs]] = ..., excluded_cloud_storage_locations: Optional[pulumi.Input[ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageLocationsArgs]] = ..., included_cloud_storage_buckets: Optional[pulumi.Input[ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageBucketsArgs]] = ..., included_cloud_storage_locations: Optional[pulumi.Input[ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageLocationsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageBuckets")
    def excluded_cloud_storage_buckets(self) -> Optional[pulumi.Input[ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageBucketsArgs]]:
        
        ...
    
    @excluded_cloud_storage_buckets.setter
    def excluded_cloud_storage_buckets(self, value: Optional[pulumi.Input[ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageBucketsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageLocations")
    def excluded_cloud_storage_locations(self) -> Optional[pulumi.Input[ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageLocationsArgs]]:
        
        ...
    
    @excluded_cloud_storage_locations.setter
    def excluded_cloud_storage_locations(self, value: Optional[pulumi.Input[ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageLocationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageBuckets")
    def included_cloud_storage_buckets(self) -> Optional[pulumi.Input[ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageBucketsArgs]]:
        
        ...
    
    @included_cloud_storage_buckets.setter
    def included_cloud_storage_buckets(self, value: Optional[pulumi.Input[ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageBucketsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageLocations")
    def included_cloud_storage_locations(self) -> Optional[pulumi.Input[ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageLocationsArgs]]:
        
        ...
    
    @included_cloud_storage_locations.setter
    def included_cloud_storage_locations(self, value: Optional[pulumi.Input[ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageLocationsArgs]]): # -> None:
        ...
    


class ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageBucketsArgsDict(TypedDict):
    bucket_id_regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageBucketsArgs:
    def __init__(__self__, *, bucket_id_regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @bucket_id_regexes.setter
    def bucket_id_regexes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageLocationsArgsDict(TypedDict):
    locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ControlOrganizationIntelligenceConfigFilterExcludedCloudStorageLocationsArgs:
    def __init__(__self__, *, locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageBucketsArgsDict(TypedDict):
    bucket_id_regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageBucketsArgs:
    def __init__(__self__, *, bucket_id_regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @bucket_id_regexes.setter
    def bucket_id_regexes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageLocationsArgsDict(TypedDict):
    locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ControlOrganizationIntelligenceConfigFilterIncludedCloudStorageLocationsArgs:
    def __init__(__self__, *, locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ControlOrganizationIntelligenceConfigTrialConfigArgsDict(TypedDict):
    expire_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ControlOrganizationIntelligenceConfigTrialConfigArgs:
    def __init__(__self__, *, expire_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ControlProjectIntelligenceConfigEffectiveIntelligenceConfigArgsDict(TypedDict):
    effective_edition: NotRequired[pulumi.Input[_builtins.str]]
    intelligence_config: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ControlProjectIntelligenceConfigEffectiveIntelligenceConfigArgs:
    def __init__(__self__, *, effective_edition: Optional[pulumi.Input[_builtins.str]] = ..., intelligence_config: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveEdition")
    def effective_edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effective_edition.setter
    def effective_edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="intelligenceConfig")
    def intelligence_config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @intelligence_config.setter
    def intelligence_config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ControlProjectIntelligenceConfigFilterArgsDict(TypedDict):
    excluded_cloud_storage_buckets: NotRequired[pulumi.Input[ControlProjectIntelligenceConfigFilterExcludedCloudStorageBucketsArgsDict]]
    excluded_cloud_storage_locations: NotRequired[pulumi.Input[ControlProjectIntelligenceConfigFilterExcludedCloudStorageLocationsArgsDict]]
    included_cloud_storage_buckets: NotRequired[pulumi.Input[ControlProjectIntelligenceConfigFilterIncludedCloudStorageBucketsArgsDict]]
    included_cloud_storage_locations: NotRequired[pulumi.Input[ControlProjectIntelligenceConfigFilterIncludedCloudStorageLocationsArgsDict]]


@pulumi.input_type
class ControlProjectIntelligenceConfigFilterArgs:
    def __init__(__self__, *, excluded_cloud_storage_buckets: Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterExcludedCloudStorageBucketsArgs]] = ..., excluded_cloud_storage_locations: Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterExcludedCloudStorageLocationsArgs]] = ..., included_cloud_storage_buckets: Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterIncludedCloudStorageBucketsArgs]] = ..., included_cloud_storage_locations: Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterIncludedCloudStorageLocationsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageBuckets")
    def excluded_cloud_storage_buckets(self) -> Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterExcludedCloudStorageBucketsArgs]]:
        
        ...
    
    @excluded_cloud_storage_buckets.setter
    def excluded_cloud_storage_buckets(self, value: Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterExcludedCloudStorageBucketsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCloudStorageLocations")
    def excluded_cloud_storage_locations(self) -> Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterExcludedCloudStorageLocationsArgs]]:
        
        ...
    
    @excluded_cloud_storage_locations.setter
    def excluded_cloud_storage_locations(self, value: Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterExcludedCloudStorageLocationsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageBuckets")
    def included_cloud_storage_buckets(self) -> Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterIncludedCloudStorageBucketsArgs]]:
        
        ...
    
    @included_cloud_storage_buckets.setter
    def included_cloud_storage_buckets(self, value: Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterIncludedCloudStorageBucketsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCloudStorageLocations")
    def included_cloud_storage_locations(self) -> Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterIncludedCloudStorageLocationsArgs]]:
        
        ...
    
    @included_cloud_storage_locations.setter
    def included_cloud_storage_locations(self, value: Optional[pulumi.Input[ControlProjectIntelligenceConfigFilterIncludedCloudStorageLocationsArgs]]): # -> None:
        ...
    


class ControlProjectIntelligenceConfigFilterExcludedCloudStorageBucketsArgsDict(TypedDict):
    bucket_id_regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ControlProjectIntelligenceConfigFilterExcludedCloudStorageBucketsArgs:
    def __init__(__self__, *, bucket_id_regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @bucket_id_regexes.setter
    def bucket_id_regexes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ControlProjectIntelligenceConfigFilterExcludedCloudStorageLocationsArgsDict(TypedDict):
    locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ControlProjectIntelligenceConfigFilterExcludedCloudStorageLocationsArgs:
    def __init__(__self__, *, locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ControlProjectIntelligenceConfigFilterIncludedCloudStorageBucketsArgsDict(TypedDict):
    bucket_id_regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ControlProjectIntelligenceConfigFilterIncludedCloudStorageBucketsArgs:
    def __init__(__self__, *, bucket_id_regexes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketIdRegexes")
    def bucket_id_regexes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @bucket_id_regexes.setter
    def bucket_id_regexes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ControlProjectIntelligenceConfigFilterIncludedCloudStorageLocationsArgsDict(TypedDict):
    locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ControlProjectIntelligenceConfigFilterIncludedCloudStorageLocationsArgs:
    def __init__(__self__, *, locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ControlProjectIntelligenceConfigTrialConfigArgsDict(TypedDict):
    expire_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ControlProjectIntelligenceConfigTrialConfigArgs:
    def __init__(__self__, *, expire_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DefaultObjectAccessControlProjectTeamArgsDict(TypedDict):
    project_number: NotRequired[pulumi.Input[_builtins.str]]
    team: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DefaultObjectAccessControlProjectTeamArgs:
    def __init__(__self__, *, project_number: Optional[pulumi.Input[_builtins.str]] = ..., team: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project_number.setter
    def project_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def team(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @team.setter
    def team(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InsightsDatasetConfigExcludeCloudStorageBucketsArgsDict(TypedDict):
    cloud_storage_buckets: pulumi.Input[Sequence[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageBucketsCloudStorageBucketArgsDict]]]


@pulumi.input_type
class InsightsDatasetConfigExcludeCloudStorageBucketsArgs:
    def __init__(__self__, *, cloud_storage_buckets: pulumi.Input[Sequence[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageBucketsCloudStorageBucketArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageBuckets")
    def cloud_storage_buckets(self) -> pulumi.Input[Sequence[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageBucketsCloudStorageBucketArgs]]]:
        
        ...
    
    @cloud_storage_buckets.setter
    def cloud_storage_buckets(self, value: pulumi.Input[Sequence[pulumi.Input[InsightsDatasetConfigExcludeCloudStorageBucketsCloudStorageBucketArgs]]]): # -> None:
        ...
    


class InsightsDatasetConfigExcludeCloudStorageBucketsCloudStorageBucketArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix_regex: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InsightsDatasetConfigExcludeCloudStorageBucketsCloudStorageBucketArgs:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix_regex: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefixRegex")
    def bucket_prefix_regex(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix_regex.setter
    def bucket_prefix_regex(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InsightsDatasetConfigExcludeCloudStorageLocationsArgsDict(TypedDict):
    locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class InsightsDatasetConfigExcludeCloudStorageLocationsArgs:
    def __init__(__self__, *, locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class InsightsDatasetConfigIdentityArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InsightsDatasetConfigIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InsightsDatasetConfigIncludeCloudStorageBucketsArgsDict(TypedDict):
    cloud_storage_buckets: pulumi.Input[Sequence[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageBucketsCloudStorageBucketArgsDict]]]


@pulumi.input_type
class InsightsDatasetConfigIncludeCloudStorageBucketsArgs:
    def __init__(__self__, *, cloud_storage_buckets: pulumi.Input[Sequence[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageBucketsCloudStorageBucketArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageBuckets")
    def cloud_storage_buckets(self) -> pulumi.Input[Sequence[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageBucketsCloudStorageBucketArgs]]]:
        
        ...
    
    @cloud_storage_buckets.setter
    def cloud_storage_buckets(self, value: pulumi.Input[Sequence[pulumi.Input[InsightsDatasetConfigIncludeCloudStorageBucketsCloudStorageBucketArgs]]]): # -> None:
        ...
    


class InsightsDatasetConfigIncludeCloudStorageBucketsCloudStorageBucketArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix_regex: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InsightsDatasetConfigIncludeCloudStorageBucketsCloudStorageBucketArgs:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix_regex: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefixRegex")
    def bucket_prefix_regex(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix_regex.setter
    def bucket_prefix_regex(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InsightsDatasetConfigIncludeCloudStorageLocationsArgsDict(TypedDict):
    locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class InsightsDatasetConfigIncludeCloudStorageLocationsArgs:
    def __init__(__self__, *, locations: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class InsightsDatasetConfigLinkArgsDict(TypedDict):
    dataset: NotRequired[pulumi.Input[_builtins.str]]
    linked: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class InsightsDatasetConfigLinkArgs:
    def __init__(__self__, *, dataset: Optional[pulumi.Input[_builtins.str]] = ..., linked: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def linked(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @linked.setter
    def linked(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class InsightsDatasetConfigSourceFoldersArgsDict(TypedDict):
    folder_numbers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class InsightsDatasetConfigSourceFoldersArgs:
    def __init__(__self__, *, folder_numbers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderNumbers")
    def folder_numbers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @folder_numbers.setter
    def folder_numbers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class InsightsDatasetConfigSourceProjectsArgsDict(TypedDict):
    project_numbers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class InsightsDatasetConfigSourceProjectsArgs:
    def __init__(__self__, *, project_numbers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumbers")
    def project_numbers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @project_numbers.setter
    def project_numbers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class InsightsReportConfigCsvOptionsArgsDict(TypedDict):
    delimiter: NotRequired[pulumi.Input[_builtins.str]]
    header_required: NotRequired[pulumi.Input[_builtins.bool]]
    record_separator: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InsightsReportConfigCsvOptionsArgs:
    def __init__(__self__, *, delimiter: Optional[pulumi.Input[_builtins.str]] = ..., header_required: Optional[pulumi.Input[_builtins.bool]] = ..., record_separator: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delimiter.setter
    def delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerRequired")
    def header_required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @header_required.setter
    def header_required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordSeparator")
    def record_separator(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @record_separator.setter
    def record_separator(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InsightsReportConfigFrequencyOptionsArgsDict(TypedDict):
    end_date: pulumi.Input[InsightsReportConfigFrequencyOptionsEndDateArgsDict]
    frequency: pulumi.Input[_builtins.str]
    start_date: pulumi.Input[InsightsReportConfigFrequencyOptionsStartDateArgsDict]


@pulumi.input_type
class InsightsReportConfigFrequencyOptionsArgs:
    def __init__(__self__, *, end_date: pulumi.Input[InsightsReportConfigFrequencyOptionsEndDateArgs], frequency: pulumi.Input[_builtins.str], start_date: pulumi.Input[InsightsReportConfigFrequencyOptionsStartDateArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Input[InsightsReportConfigFrequencyOptionsEndDateArgs]:
        
        ...
    
    @end_date.setter
    def end_date(self, value: pulumi.Input[InsightsReportConfigFrequencyOptionsEndDateArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @frequency.setter
    def frequency(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Input[InsightsReportConfigFrequencyOptionsStartDateArgs]:
        
        ...
    
    @start_date.setter
    def start_date(self, value: pulumi.Input[InsightsReportConfigFrequencyOptionsStartDateArgs]): # -> None:
        ...
    


class InsightsReportConfigFrequencyOptionsEndDateArgsDict(TypedDict):
    day: pulumi.Input[_builtins.int]
    month: pulumi.Input[_builtins.int]
    year: pulumi.Input[_builtins.int]


@pulumi.input_type
class InsightsReportConfigFrequencyOptionsEndDateArgs:
    def __init__(__self__, *, day: pulumi.Input[_builtins.int], month: pulumi.Input[_builtins.int], year: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @day.setter
    def day(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @month.setter
    def month(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @year.setter
    def year(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class InsightsReportConfigFrequencyOptionsStartDateArgsDict(TypedDict):
    day: pulumi.Input[_builtins.int]
    month: pulumi.Input[_builtins.int]
    year: pulumi.Input[_builtins.int]


@pulumi.input_type
class InsightsReportConfigFrequencyOptionsStartDateArgs:
    def __init__(__self__, *, day: pulumi.Input[_builtins.int], month: pulumi.Input[_builtins.int], year: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @day.setter
    def day(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @month.setter
    def month(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @year.setter
    def year(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class InsightsReportConfigObjectMetadataReportOptionsArgsDict(TypedDict):
    metadata_fields: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    storage_destination_options: pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsStorageDestinationOptionsArgsDict]
    storage_filters: NotRequired[pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsStorageFiltersArgsDict]]


@pulumi.input_type
class InsightsReportConfigObjectMetadataReportOptionsArgs:
    def __init__(__self__, *, metadata_fields: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], storage_destination_options: pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsStorageDestinationOptionsArgs], storage_filters: Optional[pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsStorageFiltersArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataFields")
    def metadata_fields(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @metadata_fields.setter
    def metadata_fields(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageDestinationOptions")
    def storage_destination_options(self) -> pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsStorageDestinationOptionsArgs]:
        
        ...
    
    @storage_destination_options.setter
    def storage_destination_options(self, value: pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsStorageDestinationOptionsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageFilters")
    def storage_filters(self) -> Optional[pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsStorageFiltersArgs]]:
        
        ...
    
    @storage_filters.setter
    def storage_filters(self, value: Optional[pulumi.Input[InsightsReportConfigObjectMetadataReportOptionsStorageFiltersArgs]]): # -> None:
        ...
    


class InsightsReportConfigObjectMetadataReportOptionsStorageDestinationOptionsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    destination_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InsightsReportConfigObjectMetadataReportOptionsStorageDestinationOptionsArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], destination_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPath")
    def destination_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_path.setter
    def destination_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InsightsReportConfigObjectMetadataReportOptionsStorageFiltersArgsDict(TypedDict):
    bucket: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class InsightsReportConfigObjectMetadataReportOptionsStorageFiltersArgs:
    def __init__(__self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InsightsReportConfigParquetOptionsArgsDict(TypedDict):
    ...


@pulumi.input_type
class InsightsReportConfigParquetOptionsArgs:
    def __init__(__self__) -> None:
        ...
    


class ManagedFolderIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedFolderIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedFolderIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedFolderIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ObjectAccessControlProjectTeamArgsDict(TypedDict):
    project_number: NotRequired[pulumi.Input[_builtins.str]]
    team: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ObjectAccessControlProjectTeamArgs:
    def __init__(__self__, *, project_number: Optional[pulumi.Input[_builtins.str]] = ..., team: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectNumber")
    def project_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project_number.setter
    def project_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def team(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @team.setter
    def team(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferAgentPoolBandwidthLimitArgsDict(TypedDict):
    limit_mbps: pulumi.Input[_builtins.str]


@pulumi.input_type
class TransferAgentPoolBandwidthLimitArgs:
    def __init__(__self__, *, limit_mbps: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="limitMbps")
    def limit_mbps(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @limit_mbps.setter
    def limit_mbps(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TransferJobEventStreamArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    event_stream_expiration_time: NotRequired[pulumi.Input[_builtins.str]]
    event_stream_start_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobEventStreamArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], event_stream_expiration_time: Optional[pulumi.Input[_builtins.str]] = ..., event_stream_start_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventStreamExpirationTime")
    def event_stream_expiration_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_stream_expiration_time.setter
    def event_stream_expiration_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventStreamStartTime")
    def event_stream_start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_stream_start_time.setter
    def event_stream_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobLoggingConfigArgsDict(TypedDict):
    enable_on_prem_gcs_transfer_logs: NotRequired[pulumi.Input[_builtins.bool]]
    log_action_states: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    log_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class TransferJobLoggingConfigArgs:
    def __init__(__self__, *, enable_on_prem_gcs_transfer_logs: Optional[pulumi.Input[_builtins.bool]] = ..., log_action_states: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., log_actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableOnPremGcsTransferLogs")
    def enable_on_prem_gcs_transfer_logs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_on_prem_gcs_transfer_logs.setter
    def enable_on_prem_gcs_transfer_logs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logActionStates")
    def log_action_states(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @log_action_states.setter
    def log_action_states(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logActions")
    def log_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @log_actions.setter
    def log_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class TransferJobNotificationConfigArgsDict(TypedDict):
    payload_format: pulumi.Input[_builtins.str]
    pubsub_topic: pulumi.Input[_builtins.str]
    event_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class TransferJobNotificationConfigArgs:
    def __init__(__self__, *, payload_format: pulumi.Input[_builtins.str], pubsub_topic: pulumi.Input[_builtins.str], event_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadFormat")
    def payload_format(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @payload_format.setter
    def payload_format(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @pubsub_topic.setter
    def pubsub_topic(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTypes")
    def event_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @event_types.setter
    def event_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class TransferJobReplicationSpecArgsDict(TypedDict):
    gcs_data_sink: NotRequired[pulumi.Input[TransferJobReplicationSpecGcsDataSinkArgsDict]]
    gcs_data_source: NotRequired[pulumi.Input[TransferJobReplicationSpecGcsDataSourceArgsDict]]
    object_conditions: NotRequired[pulumi.Input[TransferJobReplicationSpecObjectConditionsArgsDict]]
    transfer_options: NotRequired[pulumi.Input[TransferJobReplicationSpecTransferOptionsArgsDict]]


@pulumi.input_type
class TransferJobReplicationSpecArgs:
    def __init__(__self__, *, gcs_data_sink: Optional[pulumi.Input[TransferJobReplicationSpecGcsDataSinkArgs]] = ..., gcs_data_source: Optional[pulumi.Input[TransferJobReplicationSpecGcsDataSourceArgs]] = ..., object_conditions: Optional[pulumi.Input[TransferJobReplicationSpecObjectConditionsArgs]] = ..., transfer_options: Optional[pulumi.Input[TransferJobReplicationSpecTransferOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsDataSink")
    def gcs_data_sink(self) -> Optional[pulumi.Input[TransferJobReplicationSpecGcsDataSinkArgs]]:
        
        ...
    
    @gcs_data_sink.setter
    def gcs_data_sink(self, value: Optional[pulumi.Input[TransferJobReplicationSpecGcsDataSinkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsDataSource")
    def gcs_data_source(self) -> Optional[pulumi.Input[TransferJobReplicationSpecGcsDataSourceArgs]]:
        
        ...
    
    @gcs_data_source.setter
    def gcs_data_source(self, value: Optional[pulumi.Input[TransferJobReplicationSpecGcsDataSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectConditions")
    def object_conditions(self) -> Optional[pulumi.Input[TransferJobReplicationSpecObjectConditionsArgs]]:
        
        ...
    
    @object_conditions.setter
    def object_conditions(self, value: Optional[pulumi.Input[TransferJobReplicationSpecObjectConditionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferOptions")
    def transfer_options(self) -> Optional[pulumi.Input[TransferJobReplicationSpecTransferOptionsArgs]]:
        
        ...
    
    @transfer_options.setter
    def transfer_options(self, value: Optional[pulumi.Input[TransferJobReplicationSpecTransferOptionsArgs]]): # -> None:
        ...
    


class TransferJobReplicationSpecGcsDataSinkArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobReplicationSpecGcsDataSinkArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobReplicationSpecGcsDataSourceArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobReplicationSpecGcsDataSourceArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobReplicationSpecObjectConditionsArgsDict(TypedDict):
    exclude_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    include_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    last_modified_before: NotRequired[pulumi.Input[_builtins.str]]
    last_modified_since: NotRequired[pulumi.Input[_builtins.str]]
    max_time_elapsed_since_last_modification: NotRequired[pulumi.Input[_builtins.str]]
    min_time_elapsed_since_last_modification: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobReplicationSpecObjectConditionsArgs:
    def __init__(__self__, *, exclude_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., include_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., last_modified_before: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_since: Optional[pulumi.Input[_builtins.str]] = ..., max_time_elapsed_since_last_modification: Optional[pulumi.Input[_builtins.str]] = ..., min_time_elapsed_since_last_modification: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludePrefixes")
    def exclude_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exclude_prefixes.setter
    def exclude_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includePrefixes")
    def include_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @include_prefixes.setter
    def include_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBefore")
    def last_modified_before(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_before.setter
    def last_modified_before(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedSince")
    def last_modified_since(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_since.setter
    def last_modified_since(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTimeElapsedSinceLastModification")
    def max_time_elapsed_since_last_modification(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_time_elapsed_since_last_modification.setter
    def max_time_elapsed_since_last_modification(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTimeElapsedSinceLastModification")
    def min_time_elapsed_since_last_modification(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @min_time_elapsed_since_last_modification.setter
    def min_time_elapsed_since_last_modification(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobReplicationSpecTransferOptionsArgsDict(TypedDict):
    delete_objects_from_source_after_transfer: NotRequired[pulumi.Input[_builtins.bool]]
    delete_objects_unique_in_sink: NotRequired[pulumi.Input[_builtins.bool]]
    metadata_options: NotRequired[pulumi.Input[TransferJobReplicationSpecTransferOptionsMetadataOptionsArgsDict]]
    overwrite_objects_already_existing_in_sink: NotRequired[pulumi.Input[_builtins.bool]]
    overwrite_when: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobReplicationSpecTransferOptionsArgs:
    def __init__(__self__, *, delete_objects_from_source_after_transfer: Optional[pulumi.Input[_builtins.bool]] = ..., delete_objects_unique_in_sink: Optional[pulumi.Input[_builtins.bool]] = ..., metadata_options: Optional[pulumi.Input[TransferJobReplicationSpecTransferOptionsMetadataOptionsArgs]] = ..., overwrite_objects_already_existing_in_sink: Optional[pulumi.Input[_builtins.bool]] = ..., overwrite_when: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteObjectsFromSourceAfterTransfer")
    def delete_objects_from_source_after_transfer(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_objects_from_source_after_transfer.setter
    def delete_objects_from_source_after_transfer(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteObjectsUniqueInSink")
    def delete_objects_unique_in_sink(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_objects_unique_in_sink.setter
    def delete_objects_unique_in_sink(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> Optional[pulumi.Input[TransferJobReplicationSpecTransferOptionsMetadataOptionsArgs]]:
        
        ...
    
    @metadata_options.setter
    def metadata_options(self, value: Optional[pulumi.Input[TransferJobReplicationSpecTransferOptionsMetadataOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteObjectsAlreadyExistingInSink")
    def overwrite_objects_already_existing_in_sink(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @overwrite_objects_already_existing_in_sink.setter
    def overwrite_objects_already_existing_in_sink(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteWhen")
    def overwrite_when(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @overwrite_when.setter
    def overwrite_when(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobReplicationSpecTransferOptionsMetadataOptionsArgsDict(TypedDict):
    acl: NotRequired[pulumi.Input[_builtins.str]]
    gid: NotRequired[pulumi.Input[_builtins.str]]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    storage_class: NotRequired[pulumi.Input[_builtins.str]]
    symlink: NotRequired[pulumi.Input[_builtins.str]]
    temporary_hold: NotRequired[pulumi.Input[_builtins.str]]
    time_created: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobReplicationSpecTransferOptionsMetadataOptionsArgs:
    def __init__(__self__, *, acl: Optional[pulumi.Input[_builtins.str]] = ..., gid: Optional[pulumi.Input[_builtins.str]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ..., symlink: Optional[pulumi.Input[_builtins.str]] = ..., temporary_hold: Optional[pulumi.Input[_builtins.str]] = ..., time_created: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def acl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acl.setter
    def acl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def gid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gid.setter
    def gid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def symlink(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @symlink.setter
    def symlink(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="temporaryHold")
    def temporary_hold(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @temporary_hold.setter
    def temporary_hold(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobScheduleArgsDict(TypedDict):
    schedule_start_date: pulumi.Input[TransferJobScheduleScheduleStartDateArgsDict]
    repeat_interval: NotRequired[pulumi.Input[_builtins.str]]
    schedule_end_date: NotRequired[pulumi.Input[TransferJobScheduleScheduleEndDateArgsDict]]
    start_time_of_day: NotRequired[pulumi.Input[TransferJobScheduleStartTimeOfDayArgsDict]]


@pulumi.input_type
class TransferJobScheduleArgs:
    def __init__(__self__, *, schedule_start_date: pulumi.Input[TransferJobScheduleScheduleStartDateArgs], repeat_interval: Optional[pulumi.Input[_builtins.str]] = ..., schedule_end_date: Optional[pulumi.Input[TransferJobScheduleScheduleEndDateArgs]] = ..., start_time_of_day: Optional[pulumi.Input[TransferJobScheduleStartTimeOfDayArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleStartDate")
    def schedule_start_date(self) -> pulumi.Input[TransferJobScheduleScheduleStartDateArgs]:
        
        ...
    
    @schedule_start_date.setter
    def schedule_start_date(self, value: pulumi.Input[TransferJobScheduleScheduleStartDateArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repeatInterval")
    def repeat_interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repeat_interval.setter
    def repeat_interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleEndDate")
    def schedule_end_date(self) -> Optional[pulumi.Input[TransferJobScheduleScheduleEndDateArgs]]:
        
        ...
    
    @schedule_end_date.setter
    def schedule_end_date(self, value: Optional[pulumi.Input[TransferJobScheduleScheduleEndDateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeOfDay")
    def start_time_of_day(self) -> Optional[pulumi.Input[TransferJobScheduleStartTimeOfDayArgs]]:
        
        ...
    
    @start_time_of_day.setter
    def start_time_of_day(self, value: Optional[pulumi.Input[TransferJobScheduleStartTimeOfDayArgs]]): # -> None:
        ...
    


class TransferJobScheduleScheduleEndDateArgsDict(TypedDict):
    day: pulumi.Input[_builtins.int]
    month: pulumi.Input[_builtins.int]
    year: pulumi.Input[_builtins.int]


@pulumi.input_type
class TransferJobScheduleScheduleEndDateArgs:
    def __init__(__self__, *, day: pulumi.Input[_builtins.int], month: pulumi.Input[_builtins.int], year: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @day.setter
    def day(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @month.setter
    def month(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @year.setter
    def year(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class TransferJobScheduleScheduleStartDateArgsDict(TypedDict):
    day: pulumi.Input[_builtins.int]
    month: pulumi.Input[_builtins.int]
    year: pulumi.Input[_builtins.int]


@pulumi.input_type
class TransferJobScheduleScheduleStartDateArgs:
    def __init__(__self__, *, day: pulumi.Input[_builtins.int], month: pulumi.Input[_builtins.int], year: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @day.setter
    def day(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @month.setter
    def month(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @year.setter
    def year(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class TransferJobScheduleStartTimeOfDayArgsDict(TypedDict):
    hours: pulumi.Input[_builtins.int]
    minutes: pulumi.Input[_builtins.int]
    nanos: pulumi.Input[_builtins.int]
    seconds: pulumi.Input[_builtins.int]


@pulumi.input_type
class TransferJobScheduleStartTimeOfDayArgs:
    def __init__(__self__, *, hours: pulumi.Input[_builtins.int], minutes: pulumi.Input[_builtins.int], nanos: pulumi.Input[_builtins.int], seconds: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @hours.setter
    def hours(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @nanos.setter
    def nanos(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @seconds.setter
    def seconds(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class TransferJobTransferSpecArgsDict(TypedDict):
    aws_s3_compatible_data_source: NotRequired[pulumi.Input[TransferJobTransferSpecAwsS3CompatibleDataSourceArgsDict]]
    aws_s3_data_source: NotRequired[pulumi.Input[TransferJobTransferSpecAwsS3DataSourceArgsDict]]
    azure_blob_storage_data_source: NotRequired[pulumi.Input[TransferJobTransferSpecAzureBlobStorageDataSourceArgsDict]]
    gcs_data_sink: NotRequired[pulumi.Input[TransferJobTransferSpecGcsDataSinkArgsDict]]
    gcs_data_source: NotRequired[pulumi.Input[TransferJobTransferSpecGcsDataSourceArgsDict]]
    hdfs_data_source: NotRequired[pulumi.Input[TransferJobTransferSpecHdfsDataSourceArgsDict]]
    http_data_source: NotRequired[pulumi.Input[TransferJobTransferSpecHttpDataSourceArgsDict]]
    object_conditions: NotRequired[pulumi.Input[TransferJobTransferSpecObjectConditionsArgsDict]]
    posix_data_sink: NotRequired[pulumi.Input[TransferJobTransferSpecPosixDataSinkArgsDict]]
    posix_data_source: NotRequired[pulumi.Input[TransferJobTransferSpecPosixDataSourceArgsDict]]
    sink_agent_pool_name: NotRequired[pulumi.Input[_builtins.str]]
    source_agent_pool_name: NotRequired[pulumi.Input[_builtins.str]]
    transfer_manifest: NotRequired[pulumi.Input[TransferJobTransferSpecTransferManifestArgsDict]]
    transfer_options: NotRequired[pulumi.Input[TransferJobTransferSpecTransferOptionsArgsDict]]


@pulumi.input_type
class TransferJobTransferSpecArgs:
    def __init__(__self__, *, aws_s3_compatible_data_source: Optional[pulumi.Input[TransferJobTransferSpecAwsS3CompatibleDataSourceArgs]] = ..., aws_s3_data_source: Optional[pulumi.Input[TransferJobTransferSpecAwsS3DataSourceArgs]] = ..., azure_blob_storage_data_source: Optional[pulumi.Input[TransferJobTransferSpecAzureBlobStorageDataSourceArgs]] = ..., gcs_data_sink: Optional[pulumi.Input[TransferJobTransferSpecGcsDataSinkArgs]] = ..., gcs_data_source: Optional[pulumi.Input[TransferJobTransferSpecGcsDataSourceArgs]] = ..., hdfs_data_source: Optional[pulumi.Input[TransferJobTransferSpecHdfsDataSourceArgs]] = ..., http_data_source: Optional[pulumi.Input[TransferJobTransferSpecHttpDataSourceArgs]] = ..., object_conditions: Optional[pulumi.Input[TransferJobTransferSpecObjectConditionsArgs]] = ..., posix_data_sink: Optional[pulumi.Input[TransferJobTransferSpecPosixDataSinkArgs]] = ..., posix_data_source: Optional[pulumi.Input[TransferJobTransferSpecPosixDataSourceArgs]] = ..., sink_agent_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., source_agent_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., transfer_manifest: Optional[pulumi.Input[TransferJobTransferSpecTransferManifestArgs]] = ..., transfer_options: Optional[pulumi.Input[TransferJobTransferSpecTransferOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsS3CompatibleDataSource")
    def aws_s3_compatible_data_source(self) -> Optional[pulumi.Input[TransferJobTransferSpecAwsS3CompatibleDataSourceArgs]]:
        
        ...
    
    @aws_s3_compatible_data_source.setter
    def aws_s3_compatible_data_source(self, value: Optional[pulumi.Input[TransferJobTransferSpecAwsS3CompatibleDataSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsS3DataSource")
    def aws_s3_data_source(self) -> Optional[pulumi.Input[TransferJobTransferSpecAwsS3DataSourceArgs]]:
        
        ...
    
    @aws_s3_data_source.setter
    def aws_s3_data_source(self, value: Optional[pulumi.Input[TransferJobTransferSpecAwsS3DataSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBlobStorageDataSource")
    def azure_blob_storage_data_source(self) -> Optional[pulumi.Input[TransferJobTransferSpecAzureBlobStorageDataSourceArgs]]:
        
        ...
    
    @azure_blob_storage_data_source.setter
    def azure_blob_storage_data_source(self, value: Optional[pulumi.Input[TransferJobTransferSpecAzureBlobStorageDataSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsDataSink")
    def gcs_data_sink(self) -> Optional[pulumi.Input[TransferJobTransferSpecGcsDataSinkArgs]]:
        
        ...
    
    @gcs_data_sink.setter
    def gcs_data_sink(self, value: Optional[pulumi.Input[TransferJobTransferSpecGcsDataSinkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsDataSource")
    def gcs_data_source(self) -> Optional[pulumi.Input[TransferJobTransferSpecGcsDataSourceArgs]]:
        
        ...
    
    @gcs_data_source.setter
    def gcs_data_source(self, value: Optional[pulumi.Input[TransferJobTransferSpecGcsDataSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hdfsDataSource")
    def hdfs_data_source(self) -> Optional[pulumi.Input[TransferJobTransferSpecHdfsDataSourceArgs]]:
        
        ...
    
    @hdfs_data_source.setter
    def hdfs_data_source(self, value: Optional[pulumi.Input[TransferJobTransferSpecHdfsDataSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpDataSource")
    def http_data_source(self) -> Optional[pulumi.Input[TransferJobTransferSpecHttpDataSourceArgs]]:
        
        ...
    
    @http_data_source.setter
    def http_data_source(self, value: Optional[pulumi.Input[TransferJobTransferSpecHttpDataSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectConditions")
    def object_conditions(self) -> Optional[pulumi.Input[TransferJobTransferSpecObjectConditionsArgs]]:
        
        ...
    
    @object_conditions.setter
    def object_conditions(self, value: Optional[pulumi.Input[TransferJobTransferSpecObjectConditionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixDataSink")
    def posix_data_sink(self) -> Optional[pulumi.Input[TransferJobTransferSpecPosixDataSinkArgs]]:
        
        ...
    
    @posix_data_sink.setter
    def posix_data_sink(self, value: Optional[pulumi.Input[TransferJobTransferSpecPosixDataSinkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixDataSource")
    def posix_data_source(self) -> Optional[pulumi.Input[TransferJobTransferSpecPosixDataSourceArgs]]:
        
        ...
    
    @posix_data_source.setter
    def posix_data_source(self, value: Optional[pulumi.Input[TransferJobTransferSpecPosixDataSourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sinkAgentPoolName")
    def sink_agent_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sink_agent_pool_name.setter
    def sink_agent_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAgentPoolName")
    def source_agent_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_agent_pool_name.setter
    def source_agent_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferManifest")
    def transfer_manifest(self) -> Optional[pulumi.Input[TransferJobTransferSpecTransferManifestArgs]]:
        
        ...
    
    @transfer_manifest.setter
    def transfer_manifest(self, value: Optional[pulumi.Input[TransferJobTransferSpecTransferManifestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferOptions")
    def transfer_options(self) -> Optional[pulumi.Input[TransferJobTransferSpecTransferOptionsArgs]]:
        
        ...
    
    @transfer_options.setter
    def transfer_options(self, value: Optional[pulumi.Input[TransferJobTransferSpecTransferOptionsArgs]]): # -> None:
        ...
    


class TransferJobTransferSpecAwsS3CompatibleDataSourceArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    endpoint: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    s3_metadata: NotRequired[pulumi.Input[TransferJobTransferSpecAwsS3CompatibleDataSourceS3MetadataArgsDict]]


@pulumi.input_type
class TransferJobTransferSpecAwsS3CompatibleDataSourceArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], endpoint: pulumi.Input[_builtins.str], path: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_metadata: Optional[pulumi.Input[TransferJobTransferSpecAwsS3CompatibleDataSourceS3MetadataArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Metadata")
    def s3_metadata(self) -> Optional[pulumi.Input[TransferJobTransferSpecAwsS3CompatibleDataSourceS3MetadataArgs]]:
        
        ...
    
    @s3_metadata.setter
    def s3_metadata(self, value: Optional[pulumi.Input[TransferJobTransferSpecAwsS3CompatibleDataSourceS3MetadataArgs]]): # -> None:
        ...
    


class TransferJobTransferSpecAwsS3CompatibleDataSourceS3MetadataArgsDict(TypedDict):
    auth_method: NotRequired[pulumi.Input[_builtins.str]]
    list_api: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]
    request_model: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobTransferSpecAwsS3CompatibleDataSourceS3MetadataArgs:
    def __init__(__self__, *, auth_method: Optional[pulumi.Input[_builtins.str]] = ..., list_api: Optional[pulumi.Input[_builtins.str]] = ..., protocol: Optional[pulumi.Input[_builtins.str]] = ..., request_model: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authMethod")
    def auth_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_method.setter
    def auth_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listApi")
    def list_api(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @list_api.setter
    def list_api(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestModel")
    def request_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_model.setter
    def request_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobTransferSpecAwsS3DataSourceArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    aws_access_key: NotRequired[pulumi.Input[TransferJobTransferSpecAwsS3DataSourceAwsAccessKeyArgsDict]]
    cloudfront_domain: NotRequired[pulumi.Input[_builtins.str]]
    credentials_secret: NotRequired[pulumi.Input[_builtins.str]]
    managed_private_network: NotRequired[pulumi.Input[_builtins.bool]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobTransferSpecAwsS3DataSourceArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], aws_access_key: Optional[pulumi.Input[TransferJobTransferSpecAwsS3DataSourceAwsAccessKeyArgs]] = ..., cloudfront_domain: Optional[pulumi.Input[_builtins.str]] = ..., credentials_secret: Optional[pulumi.Input[_builtins.str]] = ..., managed_private_network: Optional[pulumi.Input[_builtins.bool]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., role_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccessKey")
    def aws_access_key(self) -> Optional[pulumi.Input[TransferJobTransferSpecAwsS3DataSourceAwsAccessKeyArgs]]:
        
        ...
    
    @aws_access_key.setter
    def aws_access_key(self, value: Optional[pulumi.Input[TransferJobTransferSpecAwsS3DataSourceAwsAccessKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudfrontDomain")
    def cloudfront_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloudfront_domain.setter
    def cloudfront_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsSecret")
    def credentials_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @credentials_secret.setter
    def credentials_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedPrivateNetwork")
    def managed_private_network(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @managed_private_network.setter
    def managed_private_network(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobTransferSpecAwsS3DataSourceAwsAccessKeyArgsDict(TypedDict):
    access_key_id: pulumi.Input[_builtins.str]
    secret_access_key: pulumi.Input[_builtins.str]


@pulumi.input_type
class TransferJobTransferSpecAwsS3DataSourceAwsAccessKeyArgs:
    def __init__(__self__, *, access_key_id: pulumi.Input[_builtins.str], secret_access_key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @access_key_id.setter
    def access_key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_access_key.setter
    def secret_access_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TransferJobTransferSpecAzureBlobStorageDataSourceArgsDict(TypedDict):
    container: pulumi.Input[_builtins.str]
    storage_account: pulumi.Input[_builtins.str]
    azure_credentials: NotRequired[pulumi.Input[TransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsArgsDict]]
    credentials_secret: NotRequired[pulumi.Input[_builtins.str]]
    federated_identity_config: NotRequired[pulumi.Input[TransferJobTransferSpecAzureBlobStorageDataSourceFederatedIdentityConfigArgsDict]]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobTransferSpecAzureBlobStorageDataSourceArgs:
    def __init__(__self__, *, container: pulumi.Input[_builtins.str], storage_account: pulumi.Input[_builtins.str], azure_credentials: Optional[pulumi.Input[TransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsArgs]] = ..., credentials_secret: Optional[pulumi.Input[_builtins.str]] = ..., federated_identity_config: Optional[pulumi.Input[TransferJobTransferSpecAzureBlobStorageDataSourceFederatedIdentityConfigArgs]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def container(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container.setter
    def container(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_account.setter
    def storage_account(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureCredentials")
    def azure_credentials(self) -> Optional[pulumi.Input[TransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsArgs]]:
        
        ...
    
    @azure_credentials.setter
    def azure_credentials(self, value: Optional[pulumi.Input[TransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsSecret")
    def credentials_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @credentials_secret.setter
    def credentials_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="federatedIdentityConfig")
    def federated_identity_config(self) -> Optional[pulumi.Input[TransferJobTransferSpecAzureBlobStorageDataSourceFederatedIdentityConfigArgs]]:
        
        ...
    
    @federated_identity_config.setter
    def federated_identity_config(self, value: Optional[pulumi.Input[TransferJobTransferSpecAzureBlobStorageDataSourceFederatedIdentityConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsArgsDict(TypedDict):
    sas_token: pulumi.Input[_builtins.str]


@pulumi.input_type
class TransferJobTransferSpecAzureBlobStorageDataSourceAzureCredentialsArgs:
    def __init__(__self__, *, sas_token: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasToken")
    def sas_token(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sas_token.setter
    def sas_token(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TransferJobTransferSpecAzureBlobStorageDataSourceFederatedIdentityConfigArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    tenant_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class TransferJobTransferSpecAzureBlobStorageDataSourceFederatedIdentityConfigArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], tenant_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TransferJobTransferSpecGcsDataSinkArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobTransferSpecGcsDataSinkArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobTransferSpecGcsDataSourceArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobTransferSpecGcsDataSourceArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobTransferSpecHdfsDataSourceArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]


@pulumi.input_type
class TransferJobTransferSpecHdfsDataSourceArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TransferJobTransferSpecHttpDataSourceArgsDict(TypedDict):
    list_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class TransferJobTransferSpecHttpDataSourceArgs:
    def __init__(__self__, *, list_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listUrl")
    def list_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @list_url.setter
    def list_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TransferJobTransferSpecObjectConditionsArgsDict(TypedDict):
    exclude_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    include_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    last_modified_before: NotRequired[pulumi.Input[_builtins.str]]
    last_modified_since: NotRequired[pulumi.Input[_builtins.str]]
    max_time_elapsed_since_last_modification: NotRequired[pulumi.Input[_builtins.str]]
    min_time_elapsed_since_last_modification: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobTransferSpecObjectConditionsArgs:
    def __init__(__self__, *, exclude_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., include_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., last_modified_before: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_since: Optional[pulumi.Input[_builtins.str]] = ..., max_time_elapsed_since_last_modification: Optional[pulumi.Input[_builtins.str]] = ..., min_time_elapsed_since_last_modification: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludePrefixes")
    def exclude_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @exclude_prefixes.setter
    def exclude_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includePrefixes")
    def include_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @include_prefixes.setter
    def include_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBefore")
    def last_modified_before(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_before.setter
    def last_modified_before(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedSince")
    def last_modified_since(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_since.setter
    def last_modified_since(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTimeElapsedSinceLastModification")
    def max_time_elapsed_since_last_modification(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @max_time_elapsed_since_last_modification.setter
    def max_time_elapsed_since_last_modification(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minTimeElapsedSinceLastModification")
    def min_time_elapsed_since_last_modification(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @min_time_elapsed_since_last_modification.setter
    def min_time_elapsed_since_last_modification(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobTransferSpecPosixDataSinkArgsDict(TypedDict):
    root_directory: pulumi.Input[_builtins.str]


@pulumi.input_type
class TransferJobTransferSpecPosixDataSinkArgs:
    def __init__(__self__, *, root_directory: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @root_directory.setter
    def root_directory(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TransferJobTransferSpecPosixDataSourceArgsDict(TypedDict):
    root_directory: pulumi.Input[_builtins.str]


@pulumi.input_type
class TransferJobTransferSpecPosixDataSourceArgs:
    def __init__(__self__, *, root_directory: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @root_directory.setter
    def root_directory(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TransferJobTransferSpecTransferManifestArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]


@pulumi.input_type
class TransferJobTransferSpecTransferManifestArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TransferJobTransferSpecTransferOptionsArgsDict(TypedDict):
    delete_objects_from_source_after_transfer: NotRequired[pulumi.Input[_builtins.bool]]
    delete_objects_unique_in_sink: NotRequired[pulumi.Input[_builtins.bool]]
    metadata_options: NotRequired[pulumi.Input[TransferJobTransferSpecTransferOptionsMetadataOptionsArgsDict]]
    overwrite_objects_already_existing_in_sink: NotRequired[pulumi.Input[_builtins.bool]]
    overwrite_when: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobTransferSpecTransferOptionsArgs:
    def __init__(__self__, *, delete_objects_from_source_after_transfer: Optional[pulumi.Input[_builtins.bool]] = ..., delete_objects_unique_in_sink: Optional[pulumi.Input[_builtins.bool]] = ..., metadata_options: Optional[pulumi.Input[TransferJobTransferSpecTransferOptionsMetadataOptionsArgs]] = ..., overwrite_objects_already_existing_in_sink: Optional[pulumi.Input[_builtins.bool]] = ..., overwrite_when: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteObjectsFromSourceAfterTransfer")
    def delete_objects_from_source_after_transfer(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_objects_from_source_after_transfer.setter
    def delete_objects_from_source_after_transfer(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteObjectsUniqueInSink")
    def delete_objects_unique_in_sink(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_objects_unique_in_sink.setter
    def delete_objects_unique_in_sink(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> Optional[pulumi.Input[TransferJobTransferSpecTransferOptionsMetadataOptionsArgs]]:
        
        ...
    
    @metadata_options.setter
    def metadata_options(self, value: Optional[pulumi.Input[TransferJobTransferSpecTransferOptionsMetadataOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteObjectsAlreadyExistingInSink")
    def overwrite_objects_already_existing_in_sink(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @overwrite_objects_already_existing_in_sink.setter
    def overwrite_objects_already_existing_in_sink(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteWhen")
    def overwrite_when(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @overwrite_when.setter
    def overwrite_when(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TransferJobTransferSpecTransferOptionsMetadataOptionsArgsDict(TypedDict):
    acl: NotRequired[pulumi.Input[_builtins.str]]
    gid: NotRequired[pulumi.Input[_builtins.str]]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    storage_class: NotRequired[pulumi.Input[_builtins.str]]
    symlink: NotRequired[pulumi.Input[_builtins.str]]
    temporary_hold: NotRequired[pulumi.Input[_builtins.str]]
    time_created: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TransferJobTransferSpecTransferOptionsMetadataOptionsArgs:
    def __init__(__self__, *, acl: Optional[pulumi.Input[_builtins.str]] = ..., gid: Optional[pulumi.Input[_builtins.str]] = ..., kms_key: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., storage_class: Optional[pulumi.Input[_builtins.str]] = ..., symlink: Optional[pulumi.Input[_builtins.str]] = ..., temporary_hold: Optional[pulumi.Input[_builtins.str]] = ..., time_created: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def acl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acl.setter
    def acl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def gid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gid.setter
    def gid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def symlink(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @symlink.setter
    def symlink(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="temporaryHold")
    def temporary_hold(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @temporary_hold.setter
    def temporary_hold(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_created.setter
    def time_created(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


