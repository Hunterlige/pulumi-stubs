

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
__all__ = ['AzStackHCIClusterPropertiesResponse', 'AzStackHCIFabricModelCustomPropertiesResponse', 'ConnectionDetailsResponse', 'DraModelPropertiesResponse', 'DraModelResponseSystemData', 'FabricAgentModelPropertiesResponse', 'FabricModelPropertiesResponse', 'FabricModelResponseSystemData', 'GroupConnectivityInformationResponse', 'HealthErrorModelResponse', 'HyperVMigrateFabricModelCustomPropertiesResponse', 'HyperVToAzStackHCIDiskInputResponse', 'HyperVToAzStackHCINicInputResponse', ..., 'HyperVToAzStackHCIProtectedDiskPropertiesResponse', ..., 'HyperVToAzStackHCIProtectedNicPropertiesResponse', ..., 'IdentityModelResponse', 'InnerHealthErrorModelResponse', 'PolicyModelPropertiesResponse', 'PolicyModelResponseSystemData', 'PrivateEndpointConnectionProxyPropertiesResponse', ..., 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionResponse', 'PrivateLinkServiceConnectionStateResponse', 'PrivateLinkServiceProxyResponse', 'ProtectedItemDynamicMemoryConfigResponse', 'ProtectedItemModelPropertiesResponse', 'ProtectedItemModelPropertiesResponseCurrentJob', ..., ..., ..., 'ProtectedItemModelResponseSystemData', 'RemotePrivateEndpointConnectionResponse', 'RemotePrivateEndpointResponse', 'ReplicationExtensionModelPropertiesResponse', 'ReplicationExtensionModelResponseSystemData', 'StorageContainerPropertiesResponse', 'SystemDataResponse', 'VMwareDraModelCustomPropertiesResponse', 'VMwareFabricAgentModelCustomPropertiesResponse', 'VMwareMigrateFabricModelCustomPropertiesResponse', 'VMwareToAzStackHCIDiskInputResponse', 'VMwareToAzStackHCINicInputResponse', ..., 'VMwareToAzStackHCIProtectedDiskPropertiesResponse', ..., 'VMwareToAzStackHCIProtectedNicPropertiesResponse', ..., 'VaultModelPropertiesResponse', 'VaultModelResponseSystemData']
@pulumi.output_type
class AzStackHCIClusterPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_name: _builtins.str, resource_name: _builtins.str, storage_account_name: _builtins.str, storage_containers: Sequence[outputs.StorageContainerPropertiesResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainers")
    def storage_containers(self) -> Sequence[outputs.StorageContainerPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class AzStackHCIFabricModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, appliance_name: Sequence[_builtins.str], az_stack_hci_site_id: _builtins.str, cluster: outputs.AzStackHCIClusterPropertiesResponse, fabric_container_id: _builtins.str, fabric_resource_id: _builtins.str, instance_type: _builtins.str, migration_hub_uri: _builtins.str, migration_solution_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applianceName")
    def appliance_name(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azStackHciSiteId")
    def az_stack_hci_site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> outputs.AzStackHCIClusterPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricContainerId")
    def fabric_container_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricResourceId")
    def fabric_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationHubUri")
    def migration_hub_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSolutionId")
    def migration_solution_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConnectionDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_id: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., link_identifier: Optional[_builtins.str] = ..., member_name: Optional[_builtins.str] = ..., private_ip_address: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkIdentifier")
    def link_identifier(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memberName")
    def member_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DraModelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authentication_identity: outputs.IdentityModelResponse, correlation_id: _builtins.str, custom_properties: outputs.VMwareDraModelCustomPropertiesResponse, health_errors: Sequence[outputs.HealthErrorModelResponse], is_responsive: _builtins.bool, last_heartbeat: _builtins.str, machine_id: _builtins.str, machine_name: _builtins.str, provisioning_state: _builtins.str, resource_access_identity: outputs.IdentityModelResponse, version_number: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationIdentity")
    def authentication_identity(self) -> outputs.IdentityModelResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> outputs.VMwareDraModelCustomPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorModelResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isResponsive")
    def is_responsive(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeat")
    def last_heartbeat(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAccessIdentity")
    def resource_access_identity(self) -> outputs.IdentityModelResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionNumber")
    def version_number(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DraModelResponseSystemData(dict):
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
class FabricAgentModelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authentication_identity: outputs.IdentityModelResponse, correlation_id: _builtins.str, custom_properties: outputs.VMwareFabricAgentModelCustomPropertiesResponse, health_errors: Sequence[outputs.HealthErrorModelResponse], is_responsive: _builtins.bool, last_heartbeat: _builtins.str, machine_id: _builtins.str, machine_name: _builtins.str, provisioning_state: _builtins.str, resource_access_identity: outputs.IdentityModelResponse, version_number: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationIdentity")
    def authentication_identity(self) -> outputs.IdentityModelResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> outputs.VMwareFabricAgentModelCustomPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorModelResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isResponsive")
    def is_responsive(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastHeartbeat")
    def last_heartbeat(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineId")
    def machine_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAccessIdentity")
    def resource_access_identity(self) -> outputs.IdentityModelResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionNumber")
    def version_number(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FabricModelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_properties: Any, health: _builtins.str, health_errors: Sequence[outputs.HealthErrorModelResponse], provisioning_state: _builtins.str, service_endpoint: _builtins.str, service_resource_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorModelResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceResourceId")
    def service_resource_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FabricModelResponseSystemData(dict):
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
class GroupConnectivityInformationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, customer_visible_fqdns: Optional[Sequence[_builtins.str]] = ..., group_id: Optional[_builtins.str] = ..., internal_fqdn: Optional[_builtins.str] = ..., member_name: Optional[_builtins.str] = ..., private_link_service_arm_region: Optional[_builtins.str] = ..., redirect_map_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerVisibleFqdns")
    def customer_visible_fqdns(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalFqdn")
    def internal_fqdn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memberName")
    def member_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceArmRegion")
    def private_link_service_arm_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectMapId")
    def redirect_map_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HealthErrorModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, category: _builtins.str, causes: _builtins.str, code: _builtins.str, creation_time: _builtins.str, health_category: _builtins.str, is_customer_resolvable: _builtins.bool, message: _builtins.str, recommendation: _builtins.str, severity: _builtins.str, source: _builtins.str, summary: _builtins.str, affected_resource_correlation_ids: Optional[Sequence[_builtins.str]] = ..., affected_resource_type: Optional[_builtins.str] = ..., child_errors: Optional[Sequence[outputs.InnerHealthErrorModelResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def causes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCategory")
    def health_category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCustomerResolvable")
    def is_customer_resolvable(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def summary(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="affectedResourceCorrelationIds")
    def affected_resource_correlation_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="affectedResourceType")
    def affected_resource_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="childErrors")
    def child_errors(self) -> Optional[Sequence[outputs.InnerHealthErrorModelResponse]]:
        
        ...
    


@pulumi.output_type
class HyperVMigrateFabricModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fabric_container_id: _builtins.str, fabric_resource_id: _builtins.str, hyper_v_site_id: _builtins.str, instance_type: _builtins.str, migration_hub_uri: _builtins.str, migration_solution_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricContainerId")
    def fabric_container_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricResourceId")
    def fabric_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hyperVSiteId")
    def hyper_v_site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationHubUri")
    def migration_hub_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSolutionId")
    def migration_solution_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class HyperVToAzStackHCIDiskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_file_format: _builtins.str, disk_id: _builtins.str, disk_size_gb: _builtins.float, is_os_disk: _builtins.bool, is_dynamic: Optional[_builtins.bool] = ..., storage_container_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskFileFormat")
    def disk_file_format(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOsDisk")
    def is_os_disk(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDynamic")
    def is_dynamic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerId")
    def storage_container_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HyperVToAzStackHCINicInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_name: _builtins.str, nic_id: _builtins.str, selection_type_for_failover: _builtins.str, target_network_id: _builtins.str, test_network_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectionTypeForFailover")
    def selection_type_for_failover(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class HyperVToAzStackHCIPolicyModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, app_consistent_frequency_in_minutes: _builtins.int, crash_consistent_frequency_in_minutes: _builtins.int, instance_type: _builtins.str, recovery_point_history_in_minutes: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistoryInMinutes")
    def recovery_point_history_in_minutes(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class HyperVToAzStackHCIProtectedDiskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_in_bytes: _builtins.float, disk_type: _builtins.str, is_dynamic: _builtins.bool, is_os_disk: _builtins.bool, migrate_disk_name: _builtins.str, seed_disk_name: _builtins.str, source_disk_id: _builtins.str, source_disk_name: _builtins.str, storage_container_id: _builtins.str, storage_container_local_path: _builtins.str, test_migrate_disk_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityInBytes")
    def capacity_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDynamic")
    def is_dynamic(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOsDisk")
    def is_os_disk(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrateDiskName")
    def migrate_disk_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedDiskName")
    def seed_disk_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskName")
    def source_disk_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerId")
    def storage_container_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerLocalPath")
    def storage_container_local_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testMigrateDiskName")
    def test_migrate_disk_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class HyperVToAzStackHCIProtectedItemModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_location: _builtins.str, custom_location_region: _builtins.str, disks_to_include: Sequence[outputs.HyperVToAzStackHCIDiskInputResponse], fabric_discovery_machine_id: _builtins.str, failover_recovery_point_id: _builtins.str, firmware_type: _builtins.str, hyper_v_generation: _builtins.str, initial_replication_progress_percentage: _builtins.int, instance_type: _builtins.str, last_recovery_point_id: _builtins.str, last_recovery_point_received: _builtins.str, last_replication_update_time: _builtins.str, nics_to_include: Sequence[outputs.HyperVToAzStackHCINicInputResponse], os_name: _builtins.str, os_type: _builtins.str, protected_disks: Sequence[outputs.HyperVToAzStackHCIProtectedDiskPropertiesResponse], protected_nics: Sequence[outputs.HyperVToAzStackHCIProtectedNicPropertiesResponse], resync_progress_percentage: _builtins.int, run_as_account_id: _builtins.str, source_appliance_name: _builtins.str, source_cpu_cores: _builtins.int, source_dra_name: _builtins.str, source_memory_in_mega_bytes: _builtins.float, source_vm_name: _builtins.str, storage_container_id: _builtins.str, target_appliance_name: _builtins.str, target_arc_cluster_custom_location_id: _builtins.str, target_az_stack_hci_cluster_name: _builtins.str, target_dra_name: _builtins.str, target_hci_cluster_id: _builtins.str, target_location: _builtins.str, target_resource_group_id: _builtins.str, target_vm_bios_id: _builtins.str, dynamic_memory_config: Optional[outputs.ProtectedItemDynamicMemoryConfigResponse] = ..., is_dynamic_ram: Optional[_builtins.bool] = ..., target_cpu_cores: Optional[_builtins.int] = ..., target_memory_in_mega_bytes: Optional[_builtins.int] = ..., target_network_id: Optional[_builtins.str] = ..., target_vm_name: Optional[_builtins.str] = ..., test_network_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeLocation")
    def active_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLocationRegion")
    def custom_location_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disksToInclude")
    def disks_to_include(self) -> Sequence[outputs.HyperVToAzStackHCIDiskInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricDiscoveryMachineId")
    def fabric_discovery_machine_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverRecoveryPointId")
    def failover_recovery_point_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firmwareType")
    def firmware_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationProgressPercentage")
    def initial_replication_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPointId")
    def last_recovery_point_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPointReceived")
    def last_recovery_point_received(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastReplicationUpdateTime")
    def last_replication_update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicsToInclude")
    def nics_to_include(self) -> Sequence[outputs.HyperVToAzStackHCINicInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedDisks")
    def protected_disks(self) -> Sequence[outputs.HyperVToAzStackHCIProtectedDiskPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedNics")
    def protected_nics(self) -> Sequence[outputs.HyperVToAzStackHCIProtectedNicPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProgressPercentage")
    def resync_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceApplianceName")
    def source_appliance_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCpuCores")
    def source_cpu_cores(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDraName")
    def source_dra_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceMemoryInMegaBytes")
    def source_memory_in_mega_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVmName")
    def source_vm_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerId")
    def storage_container_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetApplianceName")
    def target_appliance_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetArcClusterCustomLocationId")
    def target_arc_cluster_custom_location_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAzStackHciClusterName")
    def target_az_stack_hci_cluster_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDraName")
    def target_dra_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetHciClusterId")
    def target_hci_cluster_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLocation")
    def target_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupId")
    def target_resource_group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmBiosId")
    def target_vm_bios_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryConfig")
    def dynamic_memory_config(self) -> Optional[outputs.ProtectedItemDynamicMemoryConfigResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDynamicRam")
    def is_dynamic_ram(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCpuCores")
    def target_cpu_cores(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetMemoryInMegaBytes")
    def target_memory_in_mega_bytes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmName")
    def target_vm_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HyperVToAzStackHCIProtectedNicPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mac_address: _builtins.str, network_name: _builtins.str, nic_id: _builtins.str, selection_type_for_failover: _builtins.str, target_network_id: _builtins.str, test_network_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectionTypeForFailover")
    def selection_type_for_failover(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class HyperVToAzStackHCIReplicationExtensionModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, asr_service_uri: _builtins.str, az_stack_hci_fabric_arm_id: _builtins.str, az_stack_hci_site_id: _builtins.str, gateway_service_uri: _builtins.str, hyper_v_fabric_arm_id: _builtins.str, hyper_v_site_id: _builtins.str, instance_type: _builtins.str, rcm_service_uri: _builtins.str, resource_group: _builtins.str, resource_location: _builtins.str, source_gateway_service_id: _builtins.str, source_storage_container_name: _builtins.str, subscription_id: _builtins.str, target_gateway_service_id: _builtins.str, target_storage_container_name: _builtins.str, storage_account_id: Optional[_builtins.str] = ..., storage_account_sas_secret_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asrServiceUri")
    def asr_service_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azStackHciFabricArmId")
    def az_stack_hci_fabric_arm_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azStackHciSiteId")
    def az_stack_hci_site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayServiceUri")
    def gateway_service_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hyperVFabricArmId")
    def hyper_v_fabric_arm_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hyperVSiteId")
    def hyper_v_site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rcmServiceUri")
    def rcm_service_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLocation")
    def resource_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceGatewayServiceId")
    def source_gateway_service_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceStorageContainerName")
    def source_storage_container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGatewayServiceId")
    def target_gateway_service_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetStorageContainerName")
    def target_storage_container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountSasSecretName")
    def storage_account_sas_secret_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IdentityModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aad_authority: _builtins.str, application_id: _builtins.str, audience: _builtins.str, object_id: _builtins.str, tenant_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadAuthority")
    def aad_authority(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InnerHealthErrorModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, category: _builtins.str, causes: _builtins.str, code: _builtins.str, creation_time: _builtins.str, health_category: _builtins.str, is_customer_resolvable: _builtins.bool, message: _builtins.str, recommendation: _builtins.str, severity: _builtins.str, source: _builtins.str, summary: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def causes(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCategory")
    def health_category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCustomerResolvable")
    def is_customer_resolvable(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def summary(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyModelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_properties: Any, provisioning_state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyModelResponseSystemData(dict):
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
class PrivateEndpointConnectionProxyPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, remote_private_endpoint: Optional[outputs.RemotePrivateEndpointResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remotePrivateEndpoint")
    def remote_private_endpoint(self) -> Optional[outputs.RemotePrivateEndpointResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponsePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointResponse] = ..., private_link_service_connection_state: Optional[outputs.PrivateLinkServiceConnectionStateResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateLinkServiceConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_ids: Optional[Sequence[_builtins.str]] = ..., name: Optional[_builtins.str] = ..., request_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[_builtins.str]:
        
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
class PrivateLinkServiceProxyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_connectivity_information: Optional[Sequence[outputs.GroupConnectivityInformationResponse]] = ..., id: Optional[_builtins.str] = ..., remote_private_endpoint_connection: Optional[outputs.RemotePrivateEndpointConnectionResponse] = ..., remote_private_link_service_connection_state: Optional[outputs.PrivateLinkServiceConnectionStateResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupConnectivityInformation")
    def group_connectivity_information(self) -> Optional[Sequence[outputs.GroupConnectivityInformationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remotePrivateEndpointConnection")
    def remote_private_endpoint_connection(self) -> Optional[outputs.RemotePrivateEndpointConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remotePrivateLinkServiceConnectionState")
    def remote_private_link_service_connection_state(self) -> Optional[outputs.PrivateLinkServiceConnectionStateResponse]:
        
        ...
    


@pulumi.output_type
class ProtectedItemDynamicMemoryConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, maximum_memory_in_mega_bytes: _builtins.float, minimum_memory_in_mega_bytes: _builtins.float, target_memory_buffer_percentage: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumMemoryInMegaBytes")
    def maximum_memory_in_mega_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumMemoryInMegaBytes")
    def minimum_memory_in_mega_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetMemoryBufferPercentage")
    def target_memory_buffer_percentage(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ProtectedItemModelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_jobs: Sequence[_builtins.str], correlation_id: _builtins.str, current_job: outputs.ProtectedItemModelPropertiesResponseCurrentJob, custom_properties: Any, dra_id: _builtins.str, fabric_id: _builtins.str, fabric_object_id: _builtins.str, fabric_object_name: _builtins.str, health_errors: Sequence[outputs.HealthErrorModelResponse], last_failed_enable_protection_job: outputs.ProtectedItemModelPropertiesResponseLastFailedEnableProtectionJob, last_failed_planned_failover_job: outputs.ProtectedItemModelPropertiesResponseLastFailedPlannedFailoverJob, last_successful_planned_failover_time: _builtins.str, last_successful_test_failover_time: _builtins.str, last_successful_unplanned_failover_time: _builtins.str, last_test_failover_job: outputs.ProtectedItemModelPropertiesResponseLastTestFailoverJob, policy_name: _builtins.str, protection_state: _builtins.str, protection_state_description: _builtins.str, provisioning_state: _builtins.str, replication_extension_name: _builtins.str, replication_health: _builtins.str, resync_required: _builtins.bool, resynchronization_state: _builtins.str, source_fabric_provider_id: _builtins.str, target_dra_id: _builtins.str, target_fabric_id: _builtins.str, target_fabric_provider_id: _builtins.str, test_failover_state: _builtins.str, test_failover_state_description: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedJobs")
    def allowed_jobs(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentJob")
    def current_job(self) -> outputs.ProtectedItemModelPropertiesResponseCurrentJob:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="draId")
    def dra_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricId")
    def fabric_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricObjectId")
    def fabric_object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricObjectName")
    def fabric_object_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthErrors")
    def health_errors(self) -> Sequence[outputs.HealthErrorModelResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastFailedEnableProtectionJob")
    def last_failed_enable_protection_job(self) -> outputs.ProtectedItemModelPropertiesResponseLastFailedEnableProtectionJob:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastFailedPlannedFailoverJob")
    def last_failed_planned_failover_job(self) -> outputs.ProtectedItemModelPropertiesResponseLastFailedPlannedFailoverJob:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulPlannedFailoverTime")
    def last_successful_planned_failover_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulTestFailoverTime")
    def last_successful_test_failover_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSuccessfulUnplannedFailoverTime")
    def last_successful_unplanned_failover_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastTestFailoverJob")
    def last_test_failover_job(self) -> outputs.ProtectedItemModelPropertiesResponseLastTestFailoverJob:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectionStateDescription")
    def protection_state_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationExtensionName")
    def replication_extension_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationHealth")
    def replication_health(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resynchronizationState")
    def resynchronization_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFabricProviderId")
    def source_fabric_provider_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDraId")
    def target_dra_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFabricId")
    def target_fabric_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFabricProviderId")
    def target_fabric_provider_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testFailoverState")
    def test_failover_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testFailoverStateDescription")
    def test_failover_state_description(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ProtectedItemModelPropertiesResponseCurrentJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: _builtins.str, end_time: _builtins.str, id: _builtins.str, name: _builtins.str, scenario_name: _builtins.str, start_time: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
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
    @pulumi.getter(name="scenarioName")
    def scenario_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ProtectedItemModelPropertiesResponseLastFailedEnableProtectionJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: _builtins.str, end_time: _builtins.str, id: _builtins.str, name: _builtins.str, scenario_name: _builtins.str, start_time: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
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
    @pulumi.getter(name="scenarioName")
    def scenario_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ProtectedItemModelPropertiesResponseLastFailedPlannedFailoverJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: _builtins.str, end_time: _builtins.str, id: _builtins.str, name: _builtins.str, scenario_name: _builtins.str, start_time: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
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
    @pulumi.getter(name="scenarioName")
    def scenario_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ProtectedItemModelPropertiesResponseLastTestFailoverJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: _builtins.str, end_time: _builtins.str, id: _builtins.str, name: _builtins.str, scenario_name: _builtins.str, start_time: _builtins.str, state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> _builtins.str:
        
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
    @pulumi.getter(name="scenarioName")
    def scenario_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ProtectedItemModelResponseSystemData(dict):
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
class RemotePrivateEndpointConnectionResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RemotePrivateEndpointResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, connection_details: Optional[Sequence[outputs.ConnectionDetailsResponse]] = ..., manual_private_link_service_connections: Optional[Sequence[outputs.PrivateLinkServiceConnectionResponse]] = ..., private_link_service_connections: Optional[Sequence[outputs.PrivateLinkServiceConnectionResponse]] = ..., private_link_service_proxies: Optional[Sequence[outputs.PrivateLinkServiceProxyResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionDetails")
    def connection_details(self) -> Optional[Sequence[outputs.ConnectionDetailsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(self) -> Optional[Sequence[outputs.PrivateLinkServiceConnectionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnections")
    def private_link_service_connections(self) -> Optional[Sequence[outputs.PrivateLinkServiceConnectionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceProxies")
    def private_link_service_proxies(self) -> Optional[Sequence[outputs.PrivateLinkServiceProxyResponse]]:
        
        ...
    


@pulumi.output_type
class ReplicationExtensionModelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_properties: Any, provisioning_state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ReplicationExtensionModelResponseSystemData(dict):
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
class StorageContainerPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_shared_volume_path: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterSharedVolumePath")
    def cluster_shared_volume_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
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
class VMwareDraModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bios_id: _builtins.str, instance_type: _builtins.str, mars_authentication_identity: outputs.IdentityModelResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marsAuthenticationIdentity")
    def mars_authentication_identity(self) -> outputs.IdentityModelResponse:
        
        ...
    


@pulumi.output_type
class VMwareFabricAgentModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bios_id: _builtins.str, instance_type: _builtins.str, mars_authentication_identity: outputs.IdentityModelResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="biosId")
    def bios_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marsAuthenticationIdentity")
    def mars_authentication_identity(self) -> outputs.IdentityModelResponse:
        
        ...
    


@pulumi.output_type
class VMwareMigrateFabricModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, instance_type: _builtins.str, migration_solution_id: _builtins.str, vmware_site_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationSolutionId")
    def migration_solution_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareSiteId")
    def vmware_site_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VMwareToAzStackHCIDiskInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disk_file_format: _builtins.str, disk_id: _builtins.str, disk_size_gb: _builtins.float, is_os_disk: _builtins.bool, is_dynamic: Optional[_builtins.bool] = ..., storage_container_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskFileFormat")
    def disk_file_format(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOsDisk")
    def is_os_disk(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDynamic")
    def is_dynamic(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerId")
    def storage_container_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareToAzStackHCINicInputResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, label: _builtins.str, network_name: _builtins.str, nic_id: _builtins.str, selection_type_for_failover: _builtins.str, target_network_id: _builtins.str, test_network_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectionTypeForFailover")
    def selection_type_for_failover(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VMwareToAzStackHCIPolicyModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, app_consistent_frequency_in_minutes: _builtins.int, crash_consistent_frequency_in_minutes: _builtins.int, instance_type: _builtins.str, recovery_point_history_in_minutes: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appConsistentFrequencyInMinutes")
    def app_consistent_frequency_in_minutes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crashConsistentFrequencyInMinutes")
    def crash_consistent_frequency_in_minutes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryPointHistoryInMinutes")
    def recovery_point_history_in_minutes(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class VMwareToAzStackHCIProtectedDiskPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, capacity_in_bytes: _builtins.float, disk_type: _builtins.str, is_dynamic: _builtins.bool, is_os_disk: _builtins.bool, migrate_disk_name: _builtins.str, seed_disk_name: _builtins.str, source_disk_id: _builtins.str, source_disk_name: _builtins.str, storage_container_id: _builtins.str, storage_container_local_path: _builtins.str, test_migrate_disk_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityInBytes")
    def capacity_in_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDynamic")
    def is_dynamic(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOsDisk")
    def is_os_disk(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrateDiskName")
    def migrate_disk_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="seedDiskName")
    def seed_disk_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskName")
    def source_disk_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerId")
    def storage_container_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerLocalPath")
    def storage_container_local_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testMigrateDiskName")
    def test_migrate_disk_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VMwareToAzStackHCIProtectedItemModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_location: _builtins.str, custom_location_region: _builtins.str, disks_to_include: Sequence[outputs.VMwareToAzStackHCIDiskInputResponse], fabric_discovery_machine_id: _builtins.str, failover_recovery_point_id: _builtins.str, firmware_type: _builtins.str, hyper_v_generation: _builtins.str, initial_replication_progress_percentage: _builtins.int, instance_type: _builtins.str, last_recovery_point_id: _builtins.str, last_recovery_point_received: _builtins.str, last_replication_update_time: _builtins.str, migration_progress_percentage: _builtins.int, nics_to_include: Sequence[outputs.VMwareToAzStackHCINicInputResponse], os_name: _builtins.str, os_type: _builtins.str, protected_disks: Sequence[outputs.VMwareToAzStackHCIProtectedDiskPropertiesResponse], protected_nics: Sequence[outputs.VMwareToAzStackHCIProtectedNicPropertiesResponse], resume_progress_percentage: _builtins.int, resume_retry_count: _builtins.float, resync_progress_percentage: _builtins.int, resync_required: _builtins.bool, resync_retry_count: _builtins.float, resync_state: _builtins.str, run_as_account_id: _builtins.str, source_appliance_name: _builtins.str, source_cpu_cores: _builtins.int, source_dra_name: _builtins.str, source_memory_in_mega_bytes: _builtins.float, source_vm_name: _builtins.str, storage_container_id: _builtins.str, target_appliance_name: _builtins.str, target_arc_cluster_custom_location_id: _builtins.str, target_az_stack_hci_cluster_name: _builtins.str, target_dra_name: _builtins.str, target_hci_cluster_id: _builtins.str, target_location: _builtins.str, target_resource_group_id: _builtins.str, target_vm_bios_id: _builtins.str, dynamic_memory_config: Optional[outputs.ProtectedItemDynamicMemoryConfigResponse] = ..., is_dynamic_ram: Optional[_builtins.bool] = ..., perform_auto_resync: Optional[_builtins.bool] = ..., target_cpu_cores: Optional[_builtins.int] = ..., target_memory_in_mega_bytes: Optional[_builtins.int] = ..., target_network_id: Optional[_builtins.str] = ..., target_vm_name: Optional[_builtins.str] = ..., test_network_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeLocation")
    def active_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLocationRegion")
    def custom_location_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disksToInclude")
    def disks_to_include(self) -> Sequence[outputs.VMwareToAzStackHCIDiskInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fabricDiscoveryMachineId")
    def fabric_discovery_machine_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverRecoveryPointId")
    def failover_recovery_point_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firmwareType")
    def firmware_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialReplicationProgressPercentage")
    def initial_replication_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPointId")
    def last_recovery_point_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastRecoveryPointReceived")
    def last_recovery_point_received(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastReplicationUpdateTime")
    def last_replication_update_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationProgressPercentage")
    def migration_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicsToInclude")
    def nics_to_include(self) -> Sequence[outputs.VMwareToAzStackHCINicInputResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedDisks")
    def protected_disks(self) -> Sequence[outputs.VMwareToAzStackHCIProtectedDiskPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protectedNics")
    def protected_nics(self) -> Sequence[outputs.VMwareToAzStackHCIProtectedNicPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resumeProgressPercentage")
    def resume_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resumeRetryCount")
    def resume_retry_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncProgressPercentage")
    def resync_progress_percentage(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncRetryCount")
    def resync_retry_count(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resyncState")
    def resync_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceApplianceName")
    def source_appliance_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceCpuCores")
    def source_cpu_cores(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDraName")
    def source_dra_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceMemoryInMegaBytes")
    def source_memory_in_mega_bytes(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceVmName")
    def source_vm_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerId")
    def storage_container_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetApplianceName")
    def target_appliance_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetArcClusterCustomLocationId")
    def target_arc_cluster_custom_location_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAzStackHciClusterName")
    def target_az_stack_hci_cluster_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDraName")
    def target_dra_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetHciClusterId")
    def target_hci_cluster_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLocation")
    def target_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceGroupId")
    def target_resource_group_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmBiosId")
    def target_vm_bios_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicMemoryConfig")
    def dynamic_memory_config(self) -> Optional[outputs.ProtectedItemDynamicMemoryConfigResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDynamicRam")
    def is_dynamic_ram(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performAutoResync")
    def perform_auto_resync(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetCpuCores")
    def target_cpu_cores(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetMemoryInMegaBytes")
    def target_memory_in_mega_bytes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVmName")
    def target_vm_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VMwareToAzStackHCIProtectedNicPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, label: _builtins.str, mac_address: _builtins.str, network_name: _builtins.str, nic_id: _builtins.str, selection_type_for_failover: _builtins.str, target_network_id: _builtins.str, test_network_id: _builtins.str, is_primary_nic: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkName")
    def network_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectionTypeForFailover")
    def selection_type_for_failover(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetworkId")
    def target_network_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testNetworkId")
    def test_network_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPrimaryNic")
    def is_primary_nic(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VMwareToAzStackHCIReplicationExtensionModelCustomPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, asr_service_uri: _builtins.str, az_stack_hci_fabric_arm_id: _builtins.str, az_stack_hci_site_id: _builtins.str, gateway_service_uri: _builtins.str, instance_type: _builtins.str, rcm_service_uri: _builtins.str, resource_group: _builtins.str, resource_location: _builtins.str, source_gateway_service_id: _builtins.str, source_storage_container_name: _builtins.str, subscription_id: _builtins.str, target_gateway_service_id: _builtins.str, target_storage_container_name: _builtins.str, vmware_fabric_arm_id: _builtins.str, vmware_site_id: _builtins.str, storage_account_id: Optional[_builtins.str] = ..., storage_account_sas_secret_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asrServiceUri")
    def asr_service_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azStackHciFabricArmId")
    def az_stack_hci_fabric_arm_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azStackHciSiteId")
    def az_stack_hci_site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayServiceUri")
    def gateway_service_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rcmServiceUri")
    def rcm_service_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceLocation")
    def resource_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceGatewayServiceId")
    def source_gateway_service_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceStorageContainerName")
    def source_storage_container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetGatewayServiceId")
    def target_gateway_service_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetStorageContainerName")
    def target_storage_container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareFabricArmId")
    def vmware_fabric_arm_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareSiteId")
    def vmware_site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountSasSecretName")
    def storage_account_sas_secret_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VaultModelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, service_resource_id: _builtins.str, vault_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceResourceId")
    def service_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultType")
    def vault_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VaultModelResponseSystemData(dict):
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
    


