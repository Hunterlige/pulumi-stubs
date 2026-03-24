

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AdditionalCacheNodePropertiesResponse', 'AdditionalCustomerPropertiesResponse', 'BgpCidrsConfigurationResponse', 'BgpConfigurationResponse', 'CacheNodeDriveConfigurationResponse', 'CacheNodeEntityResponse', 'CacheNodeInstallPropertiesResponse', 'CacheNodeOldResponseResponse', 'CacheNodePropertyResponse', 'CustomerEntityResponse', 'CustomerPropertyResponse', 'ErrorAdditionalInfoResponse', 'ErrorDetailResponse', 'MccCacheNodeAutoUpdateHistoryPropertiesResponse', 'MccCacheNodeAutoUpdateInfoResponse', 'MccCacheNodeIssueHistoryPropertiesResponse', 'MccCacheNodeTlsCertificatePropertiesResponse', 'MccCacheNodeTlsCertificateResponse', 'MccIssueResponse', 'ProxyUrlConfigurationResponse', 'SystemDataResponse']
@pulumi.output_type
class AdditionalCacheNodePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aggregated_status_code: _builtins.int, aggregated_status_details: _builtins.str, aggregated_status_text: _builtins.str, auto_update_applied_version: _builtins.str, auto_update_last_applied_date_time: _builtins.str, auto_update_last_applied_details: _builtins.str, auto_update_last_applied_state: _builtins.str, auto_update_last_triggered_date_time: _builtins.str, auto_update_next_available_date_time: _builtins.str, auto_update_next_available_version: _builtins.str, cache_node_state: _builtins.int, cache_node_state_detailed_text: _builtins.str, cache_node_state_short_text: _builtins.str, is_provisioned: _builtins.bool, product_version: _builtins.str, auto_update_version: Optional[_builtins.str] = ..., bgp_configuration: Optional[outputs.BgpConfigurationResponse] = ..., cache_node_properties_details_issues_list: Optional[Sequence[_builtins.str]] = ..., drive_configuration: Optional[Sequence[outputs.CacheNodeDriveConfigurationResponse]] = ..., is_proxy_required: Optional[_builtins.str] = ..., optional_property1: Optional[_builtins.str] = ..., optional_property2: Optional[_builtins.str] = ..., optional_property3: Optional[_builtins.str] = ..., optional_property4: Optional[_builtins.str] = ..., optional_property5: Optional[_builtins.str] = ..., os_type: Optional[_builtins.str] = ..., proxy_url: Optional[_builtins.str] = ..., proxy_url_configuration: Optional[outputs.ProxyUrlConfigurationResponse] = ..., update_cycle_type: Optional[_builtins.str] = ..., update_info_details: Optional[_builtins.str] = ..., update_requested_date_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregatedStatusCode")
    def aggregated_status_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregatedStatusDetails")
    def aggregated_status_details(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregatedStatusText")
    def aggregated_status_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateAppliedVersion")
    def auto_update_applied_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateLastAppliedDateTime")
    def auto_update_last_applied_date_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateLastAppliedDetails")
    def auto_update_last_applied_details(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateLastAppliedState")
    def auto_update_last_applied_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateLastTriggeredDateTime")
    def auto_update_last_triggered_date_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateNextAvailableDateTime")
    def auto_update_next_available_date_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateNextAvailableVersion")
    def auto_update_next_available_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodeState")
    def cache_node_state(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodeStateDetailedText")
    def cache_node_state_detailed_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodeStateShortText")
    def cache_node_state_short_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isProvisioned")
    def is_provisioned(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productVersion")
    def product_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateVersion")
    def auto_update_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpConfiguration")
    def bgp_configuration(self) -> Optional[outputs.BgpConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodePropertiesDetailsIssuesList")
    def cache_node_properties_details_issues_list(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="driveConfiguration")
    def drive_configuration(self) -> Optional[Sequence[outputs.CacheNodeDriveConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isProxyRequired")
    def is_proxy_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalProperty1")
    def optional_property1(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalProperty2")
    def optional_property2(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalProperty3")
    def optional_property3(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalProperty4")
    def optional_property4(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalProperty5")
    def optional_property5(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyUrlConfiguration")
    def proxy_url_configuration(self) -> Optional[outputs.ProxyUrlConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateCycleType")
    def update_cycle_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateInfoDetails")
    def update_info_details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateRequestedDateTime")
    def update_requested_date_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AdditionalCustomerPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, customer_asn_estimated_egress_peek_gbps: _builtins.float, customer_org_name: _builtins.str, customer_properties_overview_average_egress_mbps: _builtins.float, customer_properties_overview_average_miss_mbps: _builtins.float, customer_properties_overview_cache_efficiency: _builtins.float, customer_properties_overview_cache_nodes_healthy_count: _builtins.int, customer_properties_overview_cache_nodes_unhealthy_count: _builtins.int, customer_properties_overview_egress_mbps_max: _builtins.float, customer_properties_overview_egress_mbps_max_date_time: _builtins.str, customer_properties_overview_miss_mbps_max: _builtins.float, customer_properties_overview_miss_mbps_max_date_time: _builtins.str, peering_db_last_update_date: _builtins.str, peering_db_last_update_time: _builtins.str, signup_phase_status_code: _builtins.int, signup_phase_status_text: _builtins.str, signup_status: _builtins.bool, signup_status_code: _builtins.int, signup_status_text: _builtins.str, customer_asn: Optional[_builtins.str] = ..., customer_email: Optional[_builtins.str] = ..., customer_entitlement_expiration: Optional[_builtins.str] = ..., customer_entitlement_sku_guid: Optional[_builtins.str] = ..., customer_entitlement_sku_id: Optional[_builtins.str] = ..., customer_entitlement_sku_name: Optional[_builtins.str] = ..., customer_transit_asn: Optional[_builtins.str] = ..., customer_transit_state: Optional[_builtins.str] = ..., optional_property1: Optional[_builtins.str] = ..., optional_property2: Optional[_builtins.str] = ..., optional_property3: Optional[_builtins.str] = ..., optional_property4: Optional[_builtins.str] = ..., optional_property5: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerAsnEstimatedEgressPeekGbps")
    def customer_asn_estimated_egress_peek_gbps(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerOrgName")
    def customer_org_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerPropertiesOverviewAverageEgressMbps")
    def customer_properties_overview_average_egress_mbps(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerPropertiesOverviewAverageMissMbps")
    def customer_properties_overview_average_miss_mbps(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerPropertiesOverviewCacheEfficiency")
    def customer_properties_overview_cache_efficiency(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerPropertiesOverviewCacheNodesHealthyCount")
    def customer_properties_overview_cache_nodes_healthy_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerPropertiesOverviewCacheNodesUnhealthyCount")
    def customer_properties_overview_cache_nodes_unhealthy_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerPropertiesOverviewEgressMbpsMax")
    def customer_properties_overview_egress_mbps_max(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerPropertiesOverviewEgressMbpsMaxDateTime")
    def customer_properties_overview_egress_mbps_max_date_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerPropertiesOverviewMissMbpsMax")
    def customer_properties_overview_miss_mbps_max(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerPropertiesOverviewMissMbpsMaxDateTime")
    def customer_properties_overview_miss_mbps_max_date_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringDbLastUpdateDate")
    def peering_db_last_update_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringDbLastUpdateTime")
    def peering_db_last_update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signupPhaseStatusCode")
    def signup_phase_status_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signupPhaseStatusText")
    def signup_phase_status_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signupStatus")
    def signup_status(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signupStatusCode")
    def signup_status_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signupStatusText")
    def signup_status_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerAsn")
    def customer_asn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerEmail")
    def customer_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerEntitlementExpiration")
    def customer_entitlement_expiration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerEntitlementSkuGuid")
    def customer_entitlement_sku_guid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerEntitlementSkuId")
    def customer_entitlement_sku_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerEntitlementSkuName")
    def customer_entitlement_sku_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerTransitAsn")
    def customer_transit_asn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerTransitState")
    def customer_transit_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalProperty1")
    def optional_property1(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalProperty2")
    def optional_property2(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalProperty3")
    def optional_property3(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalProperty4")
    def optional_property4(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionalProperty5")
    def optional_property5(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BgpCidrsConfigurationResponse(dict):
    
    def __init__(__self__, *, bgp_cidrs: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpCidrs")
    def bgp_cidrs(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BgpConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, asn_to_ip_address_mapping: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asnToIpAddressMapping")
    def asn_to_ip_address_mapping(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CacheNodeDriveConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cache_number: Optional[_builtins.int] = ..., nginx_mapping: Optional[_builtins.str] = ..., physical_path: Optional[_builtins.str] = ..., size_in_gb: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNumber")
    def cache_number(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nginxMapping")
    def nginx_mapping(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalPath")
    def physical_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeInGb")
    def size_in_gb(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class CacheNodeEntityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_space: _builtins.int, bgp_address_space: _builtins.int, bgp_cidr_blocks_count: _builtins.int, bgp_cidr_csv_last_update_time: _builtins.str, bgp_file_bytes_truncated: _builtins.int, bgp_last_reported_time: _builtins.str, bgp_number_of_records: _builtins.int, bgp_number_of_times_updated: _builtins.int, bgp_review_feedback: _builtins.str, bgp_review_state: _builtins.str, bgp_review_state_text: _builtins.str, category: _builtins.str, cidr_csv_last_update_time: _builtins.str, client_tenant_id: _builtins.str, configuration_state: _builtins.str, configuration_state_text: _builtins.str, container_configurations: _builtins.str, container_resync_trigger: _builtins.int, create_async_operation_id: _builtins.str, customer_id: _builtins.str, delete_async_operation_id: _builtins.str, image_uri: _builtins.str, is_frozen: _builtins.bool, last_sync_with_azure_timestamp: _builtins.str, last_updated_timestamp: _builtins.str, max_allowable_probability: _builtins.float, release_version: _builtins.int, review_feedback: _builtins.str, review_state: _builtins.int, review_state_text: _builtins.str, synch_with_azure_attempts_count: _builtins.int, worker_connections: _builtins.int, worker_connections_last_updated_date_time: _builtins.str, x_cid: _builtins.str, auto_update_requested_day: Optional[_builtins.int] = ..., auto_update_requested_time: Optional[_builtins.str] = ..., auto_update_requested_week: Optional[_builtins.int] = ..., auto_update_ring_type: Optional[_builtins.str] = ..., cache_node_id: Optional[_builtins.str] = ..., cache_node_name: Optional[_builtins.str] = ..., cidr_csv: Optional[Sequence[_builtins.str]] = ..., cidr_selection_type: Optional[_builtins.int] = ..., customer_asn: Optional[_builtins.int] = ..., customer_index: Optional[_builtins.str] = ..., customer_name: Optional[_builtins.str] = ..., fully_qualified_domain_name: Optional[_builtins.str] = ..., fully_qualified_resource_id: Optional[_builtins.str] = ..., ip_address: Optional[_builtins.str] = ..., is_enabled: Optional[_builtins.bool] = ..., is_enterprise_managed: Optional[_builtins.bool] = ..., max_allowable_egress_in_mbps: Optional[_builtins.int] = ..., should_migrate: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpAddressSpace")
    def bgp_address_space(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpCidrBlocksCount")
    def bgp_cidr_blocks_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpCidrCsvLastUpdateTime")
    def bgp_cidr_csv_last_update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpFileBytesTruncated")
    def bgp_file_bytes_truncated(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpLastReportedTime")
    def bgp_last_reported_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpNumberOfRecords")
    def bgp_number_of_records(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpNumberOfTimesUpdated")
    def bgp_number_of_times_updated(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpReviewFeedback")
    def bgp_review_feedback(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpReviewState")
    def bgp_review_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpReviewStateText")
    def bgp_review_state_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrCsvLastUpdateTime")
    def cidr_csv_last_update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientTenantId")
    def client_tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationStateText")
    def configuration_state_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerConfigurations")
    def container_configurations(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerResyncTrigger")
    def container_resync_trigger(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createAsyncOperationId")
    def create_async_operation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAsyncOperationId")
    def delete_async_operation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isFrozen")
    def is_frozen(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSyncWithAzureTimestamp")
    def last_sync_with_azure_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAllowableProbability")
    def max_allowable_probability(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseVersion")
    def release_version(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reviewFeedback")
    def review_feedback(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reviewState")
    def review_state(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reviewStateText")
    def review_state_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchWithAzureAttemptsCount")
    def synch_with_azure_attempts_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConnections")
    def worker_connections(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConnectionsLastUpdatedDateTime")
    def worker_connections_last_updated_date_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="xCid")
    def x_cid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateRequestedDay")
    def auto_update_requested_day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateRequestedTime")
    def auto_update_requested_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateRequestedWeek")
    def auto_update_requested_week(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateRingType")
    def auto_update_ring_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodeId")
    def cache_node_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodeName")
    def cache_node_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrCsv")
    def cidr_csv(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrSelectionType")
    def cidr_selection_type(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerAsn")
    def customer_asn(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerIndex")
    def customer_index(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerName")
    def customer_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedResourceId")
    def fully_qualified_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnterpriseManaged")
    def is_enterprise_managed(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAllowableEgressInMbps")
    def max_allowable_egress_in_mbps(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shouldMigrate")
    def should_migrate(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class CacheNodeInstallPropertiesResponse(dict):
    
    def __init__(__self__, *, primary_account_key: _builtins.str, registration_key: _builtins.str, secondary_account_key: _builtins.str, cache_node_id: Optional[_builtins.str] = ..., customer_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryAccountKey")
    def primary_account_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationKey")
    def registration_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryAccountKey")
    def secondary_account_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodeId")
    def cache_node_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CacheNodeOldResponseResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, status: _builtins.str, error: Optional[outputs.ErrorDetailResponse] = ..., status_code: Optional[_builtins.str] = ..., status_details: Optional[_builtins.str] = ..., status_text: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusText")
    def status_text(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CacheNodePropertyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, status: _builtins.str, additional_cache_node_properties: Optional[outputs.AdditionalCacheNodePropertiesResponse] = ..., cache_node: Optional[outputs.CacheNodeEntityResponse] = ..., error: Optional[outputs.ErrorDetailResponse] = ..., status_code: Optional[_builtins.str] = ..., status_details: Optional[_builtins.str] = ..., status_text: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalCacheNodeProperties")
    def additional_cache_node_properties(self) -> Optional[outputs.AdditionalCacheNodePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNode")
    def cache_node(self) -> Optional[outputs.CacheNodeEntityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusText")
    def status_text(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CustomerEntityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, create_async_operation_id: _builtins.str, customer_id: _builtins.str, delete_async_operation_id: _builtins.str, last_sync_with_azure_timestamp: _builtins.str, synch_with_azure_attempts_count: _builtins.int, client_tenant_id: Optional[_builtins.str] = ..., contact_email: Optional[_builtins.str] = ..., contact_name: Optional[_builtins.str] = ..., contact_phone: Optional[_builtins.str] = ..., customer_name: Optional[_builtins.str] = ..., fully_qualified_resource_id: Optional[_builtins.str] = ..., is_enterprise_managed: Optional[_builtins.bool] = ..., is_entitled: Optional[_builtins.bool] = ..., release_version: Optional[_builtins.int] = ..., resend_signup_code: Optional[_builtins.bool] = ..., should_migrate: Optional[_builtins.bool] = ..., verify_signup_code: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createAsyncOperationId")
    def create_async_operation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAsyncOperationId")
    def delete_async_operation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSyncWithAzureTimestamp")
    def last_sync_with_azure_timestamp(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchWithAzureAttemptsCount")
    def synch_with_azure_attempts_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientTenantId")
    def client_tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactEmail")
    def contact_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactName")
    def contact_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactPhone")
    def contact_phone(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerName")
    def customer_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedResourceId")
    def fully_qualified_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnterpriseManaged")
    def is_enterprise_managed(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEntitled")
    def is_entitled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseVersion")
    def release_version(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resendSignupCode")
    def resend_signup_code(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shouldMigrate")
    def should_migrate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifySignupCode")
    def verify_signup_code(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class CustomerPropertyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error: outputs.ErrorDetailResponse, provisioning_state: _builtins.str, status: _builtins.str, status_code: _builtins.str, status_details: _builtins.str, status_text: _builtins.str, additional_customer_properties: Optional[outputs.AdditionalCustomerPropertiesResponse] = ..., customer: Optional[outputs.CustomerEntityResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> outputs.ErrorDetailResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusText")
    def status_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalCustomerProperties")
    def additional_customer_properties(self) -> Optional[outputs.AdditionalCustomerPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def customer(self) -> Optional[outputs.CustomerEntityResponse]:
        
        ...
    


@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    
    def __init__(__self__, *, info: Any, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def info(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ErrorDetailResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_info: Sequence[outputs.ErrorAdditionalInfoResponse], code: _builtins.str, details: Sequence[outputs.ErrorDetailResponse], message: _builtins.str, target: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.ErrorAdditionalInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDetailResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MccCacheNodeAutoUpdateHistoryPropertiesResponse(dict):
    
    def __init__(__self__, *, cache_node_id: _builtins.str, customer_id: _builtins.str, auto_update_history: Optional[Sequence[outputs.MccCacheNodeAutoUpdateInfoResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodeId")
    def cache_node_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateHistory")
    def auto_update_history(self) -> Optional[Sequence[outputs.MccCacheNodeAutoUpdateInfoResponse]]:
        
        ...
    


@pulumi.output_type
class MccCacheNodeAutoUpdateInfoResponse(dict):
    
    def __init__(__self__, *, auto_update_last_applied_status: _builtins.int, auto_update_last_applied_status_detailed_text: _builtins.str, auto_update_last_applied_status_text: _builtins.str, auto_update_ring_type: _builtins.int, created_date_time_utc: _builtins.str, image_uri_before_update: _builtins.str, image_uri_targeted: _builtins.str, image_uri_terminal: _builtins.str, moved_to_terminal_state_date_time: _builtins.str, plan_change_log_text: _builtins.str, plan_id: _builtins.float, rule_requested_day: _builtins.int, rule_requested_hour: _builtins.str, rule_requested_minute: _builtins.str, rule_requested_week: _builtins.int, time_to_go_live_date_time: _builtins.str, updated_registry_date_time_utc: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateLastAppliedStatus")
    def auto_update_last_applied_status(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateLastAppliedStatusDetailedText")
    def auto_update_last_applied_status_detailed_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateLastAppliedStatusText")
    def auto_update_last_applied_status_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoUpdateRingType")
    def auto_update_ring_type(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDateTimeUtc")
    def created_date_time_utc(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUriBeforeUpdate")
    def image_uri_before_update(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUriTargeted")
    def image_uri_targeted(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUriTerminal")
    def image_uri_terminal(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="movedToTerminalStateDateTime")
    def moved_to_terminal_state_date_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planChangeLogText")
    def plan_change_log_text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleRequestedDay")
    def rule_requested_day(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleRequestedHour")
    def rule_requested_hour(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleRequestedMinute")
    def rule_requested_minute(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleRequestedWeek")
    def rule_requested_week(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToGoLiveDateTime")
    def time_to_go_live_date_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedRegistryDateTimeUtc")
    def updated_registry_date_time_utc(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MccCacheNodeIssueHistoryPropertiesResponse(dict):
    
    def __init__(__self__, *, cache_node_id: _builtins.str, customer_id: _builtins.str, mcc_issue_history: Optional[Sequence[outputs.MccIssueResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodeId")
    def cache_node_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mccIssueHistory")
    def mcc_issue_history(self) -> Optional[Sequence[outputs.MccIssueResponse]]:
        
        ...
    


@pulumi.output_type
class MccCacheNodeTlsCertificatePropertiesResponse(dict):
    
    def __init__(__self__, *, cache_node_id: _builtins.str, customer_id: _builtins.str, tls_certificate_history: Optional[Sequence[outputs.MccCacheNodeTlsCertificateResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheNodeId")
    def cache_node_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsCertificateHistory")
    def tls_certificate_history(self) -> Optional[Sequence[outputs.MccCacheNodeTlsCertificateResponse]]:
        
        ...
    


@pulumi.output_type
class MccCacheNodeTlsCertificateResponse(dict):
    
    def __init__(__self__, *, action_required: _builtins.str, certificate_file_name: _builtins.str, expiry_date: _builtins.str, not_before_date: _builtins.str, subject: _builtins.str, subject_alt_name: _builtins.str, thumbprint: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionRequired")
    def action_required(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateFileName")
    def certificate_file_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBeforeDate")
    def not_before_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAltName")
    def subject_alt_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MccIssueResponse(dict):
    
    def __init__(__self__, *, detail_string: _builtins.str, help_link: _builtins.str, issue_end_date: _builtins.str, issue_start_date: _builtins.str, mcc_issue_type: _builtins.str, toast_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailString")
    def detail_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="helpLink")
    def help_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issueEndDate")
    def issue_end_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issueStartDate")
    def issue_start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mccIssueType")
    def mcc_issue_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toastString")
    def toast_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ProxyUrlConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, proxy_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyUrl")
    def proxy_url(self) -> Optional[_builtins.str]:
        
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
    


