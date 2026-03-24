

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
__all__ = ['AzureNetAppFilesStoreResponse', 'AzureStorageBlobStoreResponse', 'BookshelfKeyVaultPropertiesResponse', 'BookshelfPropertiesResponse', 'ChatModelDeploymentPropertiesResponse', 'IdentityResponse', 'KeyVaultPropertiesResponse', 'MoboBrokerResourceResponse', 'NodePoolPropertiesResponse', 'PrivateEndpointConnectionPropertiesResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'ProjectPropertiesResponse', 'ProjectSettingsResponse', 'StorageAssetPropertiesResponse', 'StorageContainerPropertiesResponse', 'SupercomputerIdentitiesResponse', 'SupercomputerPropertiesResponse', 'SystemDataResponse', 'ToolPropertiesResponse', 'UserAssignedIdentityResponse', 'WithMoboBrokerResourcesResponse', 'WorkspacePropertiesResponse']
@pulumi.output_type
class AzureNetAppFilesStoreResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kind: _builtins.str, net_app_volume_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="netAppVolumeId")
    def net_app_volume_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AzureStorageBlobStoreResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kind: _builtins.str, storage_account_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class BookshelfKeyVaultPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity_client_id: _builtins.str, key_name: _builtins.str, key_vault_uri: _builtins.str, key_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BookshelfPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bookshelf_uri: _builtins.str, managed_on_behalf_of_configuration: outputs.WithMoboBrokerResourcesResponse, managed_resource_group: _builtins.str, private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionResponse], provisioning_state: _builtins.str, customer_managed_keys: Optional[_builtins.str] = ..., key_vault_properties: Optional[outputs.BookshelfKeyVaultPropertiesResponse] = ..., log_analytics_cluster_id: Optional[_builtins.str] = ..., private_endpoint_subnet_id: Optional[_builtins.str] = ..., public_network_access: Optional[_builtins.str] = ..., search_subnet_id: Optional[_builtins.str] = ..., workload_identities: Optional[Mapping[str, outputs.UserAssignedIdentityResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bookshelfUri")
    def bookshelf_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedOnBehalfOfConfiguration")
    def managed_on_behalf_of_configuration(self) -> outputs.WithMoboBrokerResourcesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourceGroup")
    def managed_resource_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeys")
    def customer_managed_keys(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[outputs.BookshelfKeyVaultPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logAnalyticsClusterId")
    def log_analytics_cluster_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointSubnetId")
    def private_endpoint_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchSubnetId")
    def search_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentities")
    def workload_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class ChatModelDeploymentPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, model_format: _builtins.str, model_name: _builtins.str, provisioning_state: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelFormat")
    def model_format(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, id: _builtins.str, principal_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class KeyVaultPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_name: _builtins.str, key_vault_uri: _builtins.str, key_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MoboBrokerResourceResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NodePoolPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_node_count: _builtins.int, provisioning_state: _builtins.str, subnet_id: _builtins.str, vm_size: _builtins.str, min_node_count: Optional[_builtins.int] = ..., scale_set_priority: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleSetPriority")
    def scale_set_priority(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_ids: Sequence[_builtins.str], private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse, provisioning_state: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]:
        
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
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]:
        
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
class ProjectPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, foundry_project_endpoint: _builtins.str, provisioning_state: _builtins.str, settings: Optional[outputs.ProjectSettingsResponse] = ..., storage_container_ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="foundryProjectEndpoint")
    def foundry_project_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[outputs.ProjectSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerIds")
    def storage_container_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ProjectSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, behavior_preferences: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="behaviorPreferences")
    def behavior_preferences(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StorageAssetPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: _builtins.str, provisioning_state: _builtins.str, path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StorageContainerPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, storage_store: Any) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageStore")
    def storage_store(self) -> Any:
        
        ...
    


@pulumi.output_type
class SupercomputerIdentitiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cluster_identity: outputs.IdentityResponse, kubelet_identity: outputs.IdentityResponse, workload_identities: Optional[Mapping[str, outputs.UserAssignedIdentityResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentity")
    def cluster_identity(self) -> outputs.IdentityResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubeletIdentity")
    def kubelet_identity(self) -> outputs.IdentityResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadIdentities")
    def workload_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class SupercomputerPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identities: outputs.SupercomputerIdentitiesResponse, managed_on_behalf_of_configuration: outputs.WithMoboBrokerResourcesResponse, managed_resource_group: _builtins.str, provisioning_state: _builtins.str, subnet_id: _builtins.str, customer_managed_keys: Optional[_builtins.str] = ..., disk_encryption_set_id: Optional[_builtins.str] = ..., log_analytics_cluster_id: Optional[_builtins.str] = ..., management_subnet_id: Optional[_builtins.str] = ..., outbound_type: Optional[_builtins.str] = ..., system_sku: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> outputs.SupercomputerIdentitiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedOnBehalfOfConfiguration")
    def managed_on_behalf_of_configuration(self) -> outputs.WithMoboBrokerResourcesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourceGroup")
    def managed_resource_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeys")
    def customer_managed_keys(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logAnalyticsClusterId")
    def log_analytics_cluster_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementSubnetId")
    def management_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundType")
    def outbound_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemSku")
    def system_sku(self) -> Optional[_builtins.str]:
        
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
class ToolPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, definition_content: Any, provisioning_state: _builtins.str, version: _builtins.str, environment_variables: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="definitionContent")
    def definition_content(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Mapping[str, _builtins.str]]:
        
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
    


@pulumi.output_type
class WithMoboBrokerResourcesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mobo_broker_resources: Sequence[outputs.MoboBrokerResourceResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moboBrokerResources")
    def mobo_broker_resources(self) -> Sequence[outputs.MoboBrokerResourceResponse]:
        
        ...
    


@pulumi.output_type
class WorkspacePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, managed_on_behalf_of_configuration: outputs.WithMoboBrokerResourcesResponse, managed_resource_group: _builtins.str, private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionResponse], provisioning_state: _builtins.str, workspace_api_uri: _builtins.str, workspace_identity: outputs.IdentityResponse, workspace_ui_uri: _builtins.str, agent_subnet_id: Optional[_builtins.str] = ..., customer_managed_keys: Optional[_builtins.str] = ..., key_vault_properties: Optional[outputs.KeyVaultPropertiesResponse] = ..., log_analytics_cluster_id: Optional[_builtins.str] = ..., private_endpoint_subnet_id: Optional[_builtins.str] = ..., public_network_access: Optional[_builtins.str] = ..., supercomputer_ids: Optional[Sequence[_builtins.str]] = ..., workspace_subnet_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedOnBehalfOfConfiguration")
    def managed_on_behalf_of_configuration(self) -> outputs.WithMoboBrokerResourcesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedResourceGroup")
    def managed_resource_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceApiUri")
    def workspace_api_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceIdentity")
    def workspace_identity(self) -> outputs.IdentityResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceUiUri")
    def workspace_ui_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentSubnetId")
    def agent_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeys")
    def customer_managed_keys(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[outputs.KeyVaultPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logAnalyticsClusterId")
    def log_analytics_cluster_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointSubnetId")
    def private_endpoint_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supercomputerIds")
    def supercomputer_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceSubnetId")
    def workspace_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    


