

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CloudEndpointChangeEnumerationActivityResponse', 'CloudEndpointChangeEnumerationStatusResponse', 'CloudEndpointLastChangeEnumerationStatusResponse', 'CloudTieringCachePerformanceResponse', 'CloudTieringDatePolicyStatusResponse', 'CloudTieringFilesNotTieringResponse', 'CloudTieringLowDiskModeResponse', 'CloudTieringSpaceSavingsResponse', 'CloudTieringVolumeFreeSpacePolicyStatusResponse', 'FilesNotTieringErrorResponse', 'ManagedServiceIdentityResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', ..., 'ServerEndpointCloudTieringStatusResponse', 'ServerEndpointFilesNotSyncingErrorResponse', 'ServerEndpointProvisioningStatusResponse', 'ServerEndpointProvisioningStepStatusResponse', 'ServerEndpointRecallErrorResponse', 'ServerEndpointRecallStatusResponse', 'ServerEndpointSyncActivityStatusResponse', 'ServerEndpointSyncSessionStatusResponse', 'ServerEndpointSyncStatusResponse', 'SystemDataResponse', 'UserAssignedIdentityResponse']
@pulumi.output_type
class CloudEndpointChangeEnumerationActivityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deletes_progress_percent: _builtins.int, last_updated_timestamp: _builtins.str, minutes_remaining: _builtins.int, operation_state: _builtins.str, processed_directories_count: _builtins.float, processed_files_count: _builtins.float, progress_percent: _builtins.int, started_timestamp: _builtins.str, status_code: _builtins.int, total_counts_state: _builtins.str, total_directories_count: _builtins.float, total_files_count: _builtins.float, total_size_bytes: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletesProgressPercent")
    def deletes_progress_percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minutesRemaining")
    def minutes_remaining(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationState")
    def operation_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processedDirectoriesCount")
    def processed_directories_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processedFilesCount")
    def processed_files_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="progressPercent")
    def progress_percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedTimestamp")
    def started_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalCountsState")
    def total_counts_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalDirectoriesCount")
    def total_directories_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalFilesCount")
    def total_files_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalSizeBytes")
    def total_size_bytes(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class CloudEndpointChangeEnumerationStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, activity: outputs.CloudEndpointChangeEnumerationActivityResponse, last_enumeration_status: outputs.CloudEndpointLastChangeEnumerationStatusResponse, last_updated_timestamp: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def activity(self) -> outputs.CloudEndpointChangeEnumerationActivityResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastEnumerationStatus")
    def last_enumeration_status(self) -> outputs.CloudEndpointLastChangeEnumerationStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CloudEndpointLastChangeEnumerationStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, completed_timestamp: _builtins.str, namespace_directories_count: _builtins.float, namespace_files_count: _builtins.float, namespace_size_bytes: _builtins.float, next_run_timestamp: _builtins.str, started_timestamp: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="completedTimestamp")
    def completed_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceDirectoriesCount")
    def namespace_directories_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceFilesCount")
    def namespace_files_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceSizeBytes")
    def namespace_size_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRunTimestamp")
    def next_run_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedTimestamp")
    def started_timestamp(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CloudTieringCachePerformanceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cache_hit_bytes: _builtins.float, cache_hit_bytes_percent: _builtins.int, cache_miss_bytes: _builtins.float, last_updated_timestamp: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheHitBytes")
    def cache_hit_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheHitBytesPercent")
    def cache_hit_bytes_percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheMissBytes")
    def cache_miss_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CloudTieringDatePolicyStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_updated_timestamp: _builtins.str, tiered_files_most_recent_access_timestamp: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tieredFilesMostRecentAccessTimestamp")
    def tiered_files_most_recent_access_timestamp(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CloudTieringFilesNotTieringResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, errors: Sequence[outputs.FilesNotTieringErrorResponse], last_updated_timestamp: _builtins.str, total_file_count: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[outputs.FilesNotTieringErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalFileCount")
    def total_file_count(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class CloudTieringLowDiskModeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_updated_timestamp: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CloudTieringSpaceSavingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cached_size_bytes: _builtins.float, last_updated_timestamp: _builtins.str, space_savings_bytes: _builtins.float, space_savings_percent: _builtins.int, total_size_cloud_bytes: _builtins.float, volume_size_bytes: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachedSizeBytes")
    def cached_size_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spaceSavingsBytes")
    def space_savings_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spaceSavingsPercent")
    def space_savings_percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalSizeCloudBytes")
    def total_size_cloud_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSizeBytes")
    def volume_size_bytes(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class CloudTieringVolumeFreeSpacePolicyStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, current_volume_free_space_percent: _builtins.int, effective_volume_free_space_policy: _builtins.int, last_updated_timestamp: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentVolumeFreeSpacePercent")
    def current_volume_free_space_percent(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveVolumeFreeSpacePolicy")
    def effective_volume_free_space_policy(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FilesNotTieringErrorResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_code: _builtins.int, file_count: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileCount")
    def file_count(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: _builtins.str, user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedIdentityResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_ids: Sequence[_builtins.str], id: _builtins.str, name: _builtins.str, private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse, provisioning_state: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> outputs.PrivateLinkServiceConnectionStateResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions_required: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServerEndpointBackgroundDataDownloadActivityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, downloaded_bytes: _builtins.float, percent_progress: _builtins.int, started_timestamp: _builtins.str, timestamp: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="downloadedBytes")
    def downloaded_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="percentProgress")
    def percent_progress(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedTimestamp")
    def started_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServerEndpointCloudTieringStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cache_performance: outputs.CloudTieringCachePerformanceResponse, date_policy_status: outputs.CloudTieringDatePolicyStatusResponse, files_not_tiering: outputs.CloudTieringFilesNotTieringResponse, health: _builtins.str, health_last_updated_timestamp: _builtins.str, last_cloud_tiering_result: _builtins.int, last_success_timestamp: _builtins.str, last_updated_timestamp: _builtins.str, low_disk_mode: outputs.CloudTieringLowDiskModeResponse, space_savings: outputs.CloudTieringSpaceSavingsResponse, volume_free_space_policy_status: outputs.CloudTieringVolumeFreeSpacePolicyStatusResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachePerformance")
    def cache_performance(self) -> outputs.CloudTieringCachePerformanceResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datePolicyStatus")
    def date_policy_status(self) -> outputs.CloudTieringDatePolicyStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filesNotTiering")
    def files_not_tiering(self) -> outputs.CloudTieringFilesNotTieringResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthLastUpdatedTimestamp")
    def health_last_updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastCloudTieringResult")
    def last_cloud_tiering_result(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessTimestamp")
    def last_success_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lowDiskMode")
    def low_disk_mode(self) -> outputs.CloudTieringLowDiskModeResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spaceSavings")
    def space_savings(self) -> outputs.CloudTieringSpaceSavingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeFreeSpacePolicyStatus")
    def volume_free_space_policy_status(self) -> outputs.CloudTieringVolumeFreeSpacePolicyStatusResponse:
        
        ...
    


@pulumi.output_type
class ServerEndpointFilesNotSyncingErrorResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_code: _builtins.int, persistent_count: _builtins.float, transient_count: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistentCount")
    def persistent_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transientCount")
    def transient_count(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class ServerEndpointProvisioningStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_status: _builtins.str, provisioning_step_statuses: Sequence[outputs.ServerEndpointProvisioningStepStatusResponse], provisioning_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningStatus")
    def provisioning_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningStepStatuses")
    def provisioning_step_statuses(self) -> Sequence[outputs.ServerEndpointProvisioningStepStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningType")
    def provisioning_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServerEndpointProvisioningStepStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_information: Mapping[str, _builtins.str], end_time: _builtins.str, error_code: _builtins.int, minutes_left: _builtins.int, name: _builtins.str, progress_percentage: _builtins.int, start_time: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalInformation")
    def additional_information(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minutesLeft")
    def minutes_left(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="progressPercentage")
    def progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServerEndpointRecallErrorResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, count: _builtins.float, error_code: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ServerEndpointRecallStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last_updated_timestamp: _builtins.str, recall_errors: Sequence[outputs.ServerEndpointRecallErrorResponse], total_recall_errors_count: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recallErrors")
    def recall_errors(self) -> Sequence[outputs.ServerEndpointRecallErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalRecallErrorsCount")
    def total_recall_errors_count(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class ServerEndpointSyncActivityStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, applied_bytes: _builtins.float, applied_item_count: _builtins.float, per_item_error_count: _builtins.float, session_minutes_remaining: _builtins.int, sync_mode: _builtins.str, timestamp: _builtins.str, total_bytes: _builtins.float, total_item_count: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedBytes")
    def applied_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appliedItemCount")
    def applied_item_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perItemErrorCount")
    def per_item_error_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionMinutesRemaining")
    def session_minutes_remaining(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncMode")
    def sync_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalBytes")
    def total_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalItemCount")
    def total_item_count(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class ServerEndpointSyncSessionStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, files_not_syncing_errors: Sequence[outputs.ServerEndpointFilesNotSyncingErrorResponse], last_sync_mode: _builtins.str, last_sync_per_item_error_count: _builtins.float, last_sync_result: _builtins.int, last_sync_success_timestamp: _builtins.str, last_sync_timestamp: _builtins.str, persistent_files_not_syncing_count: _builtins.float, transient_files_not_syncing_count: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filesNotSyncingErrors")
    def files_not_syncing_errors(self) -> Sequence[outputs.ServerEndpointFilesNotSyncingErrorResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSyncMode")
    def last_sync_mode(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSyncPerItemErrorCount")
    def last_sync_per_item_error_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSyncResult")
    def last_sync_result(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSyncSuccessTimestamp")
    def last_sync_success_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSyncTimestamp")
    def last_sync_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistentFilesNotSyncingCount")
    def persistent_files_not_syncing_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transientFilesNotSyncingCount")
    def transient_files_not_syncing_count(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class ServerEndpointSyncStatusResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, background_data_download_activity: outputs.ServerEndpointBackgroundDataDownloadActivityResponse, combined_health: _builtins.str, download_activity: outputs.ServerEndpointSyncActivityStatusResponse, download_health: _builtins.str, download_status: outputs.ServerEndpointSyncSessionStatusResponse, last_updated_timestamp: _builtins.str, offline_data_transfer_status: _builtins.str, sync_activity: _builtins.str, total_persistent_files_not_syncing_count: _builtins.float, upload_activity: outputs.ServerEndpointSyncActivityStatusResponse, upload_health: _builtins.str, upload_status: outputs.ServerEndpointSyncSessionStatusResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backgroundDataDownloadActivity")
    def background_data_download_activity(self) -> outputs.ServerEndpointBackgroundDataDownloadActivityResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="combinedHealth")
    def combined_health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="downloadActivity")
    def download_activity(self) -> outputs.ServerEndpointSyncActivityStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="downloadHealth")
    def download_health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="downloadStatus")
    def download_status(self) -> outputs.ServerEndpointSyncSessionStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offlineDataTransferStatus")
    def offline_data_transfer_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncActivity")
    def sync_activity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalPersistentFilesNotSyncingCount")
    def total_persistent_files_not_syncing_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadActivity")
    def upload_activity(self) -> outputs.ServerEndpointSyncActivityStatusResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadHealth")
    def upload_health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadStatus")
    def upload_status(self) -> outputs.ServerEndpointSyncSessionStatusResponse:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, principal_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    


