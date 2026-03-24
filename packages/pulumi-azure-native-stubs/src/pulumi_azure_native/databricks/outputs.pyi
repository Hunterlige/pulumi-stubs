

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
__all__ = ['AccessConnectorPropertiesResponse', 'AddressSpaceResponse', 'AutomaticClusterUpdateDefinitionResponse', 'ComplianceSecurityProfileDefinitionResponse', 'CreatedByResponse', 'DefaultCatalogPropertiesResponse', 'EncryptionEntitiesDefinitionResponse', 'EncryptionResponse', 'EncryptionV2Response', 'EncryptionV2ResponseKeyVaultProperties', 'EnhancedSecurityComplianceDefinitionResponse', 'EnhancedSecurityMonitoringDefinitionResponse', 'ManagedDiskEncryptionResponse', 'ManagedDiskEncryptionResponseKeyVaultProperties', 'ManagedIdentityConfigurationResponse', 'ManagedServiceIdentityResponse', 'PrivateEndpointConnectionPropertiesResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'SkuResponse', 'SystemDataResponse', 'UserAssignedIdentityResponse', ..., ..., 'WorkspaceCustomBooleanParameterResponse', 'WorkspaceCustomObjectParameterResponse', 'WorkspaceCustomParametersResponse', 'WorkspaceCustomStringParameterResponse', 'WorkspaceEncryptionParameterResponse', 'WorkspaceNoPublicIPBooleanParameterResponse', 'WorkspacePropertiesResponseAccessConnector', 'WorkspacePropertiesResponseEncryption', 'WorkspaceProviderAuthorizationResponse']
@pulumi.output_type
class AccessConnectorPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, refered_by: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="referedBy")
    def refered_by(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AddressSpaceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_prefixes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefixes")
    def address_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AutomaticClusterUpdateDefinitionResponse(dict):
    
    def __init__(__self__, *, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ComplianceSecurityProfileDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, compliance_standards: Optional[Sequence[_builtins.str]] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceStandards")
    def compliance_standards(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class CreatedByResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_id: _builtins.str, oid: _builtins.str, puid: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def oid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def puid(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DefaultCatalogPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, initial_name: Optional[_builtins.str] = ..., initial_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialName")
    def initial_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialType")
    def initial_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EncryptionEntitiesDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, managed_disk: Optional[outputs.ManagedDiskEncryptionResponse] = ..., managed_services: Optional[outputs.EncryptionV2Response] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedDisk")
    def managed_disk(self) -> Optional[outputs.ManagedDiskEncryptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedServices")
    def managed_services(self) -> Optional[outputs.EncryptionV2Response]:
        
        ...
    


@pulumi.output_type
class EncryptionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_name: Optional[_builtins.str] = ..., key_source: Optional[_builtins.str] = ..., key_vault_uri: Optional[_builtins.str] = ..., key_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EncryptionV2Response(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_source: _builtins.str, key_vault_properties: Optional[outputs.EncryptionV2ResponseKeyVaultProperties] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[outputs.EncryptionV2ResponseKeyVaultProperties]:
        
        ...
    


@pulumi.output_type
class EncryptionV2ResponseKeyVaultProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_name: _builtins.str, key_vault_uri: _builtins.str, key_version: _builtins.str) -> None:
        
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
    def key_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EnhancedSecurityComplianceDefinitionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, automatic_cluster_update: Optional[outputs.AutomaticClusterUpdateDefinitionResponse] = ..., compliance_security_profile: Optional[outputs.ComplianceSecurityProfileDefinitionResponse] = ..., enhanced_security_monitoring: Optional[outputs.EnhancedSecurityMonitoringDefinitionResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticClusterUpdate")
    def automatic_cluster_update(self) -> Optional[outputs.AutomaticClusterUpdateDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceSecurityProfile")
    def compliance_security_profile(self) -> Optional[outputs.ComplianceSecurityProfileDefinitionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedSecurityMonitoring")
    def enhanced_security_monitoring(self) -> Optional[outputs.EnhancedSecurityMonitoringDefinitionResponse]:
        
        ...
    


@pulumi.output_type
class EnhancedSecurityMonitoringDefinitionResponse(dict):
    
    def __init__(__self__, *, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ManagedDiskEncryptionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_source: _builtins.str, key_vault_properties: outputs.ManagedDiskEncryptionResponseKeyVaultProperties, rotation_to_latest_key_version_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> outputs.ManagedDiskEncryptionResponseKeyVaultProperties:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationToLatestKeyVersionEnabled")
    def rotation_to_latest_key_version_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ManagedDiskEncryptionResponseKeyVaultProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_name: _builtins.str, key_vault_uri: _builtins.str, key_version: _builtins.str) -> None:
        
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
    def key_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagedIdentityConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: _builtins.str) -> None:
        
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
class PrivateEndpointConnectionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse, provisioning_state: _builtins.str, group_ids: Optional[Sequence[_builtins.str]] = ..., private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...) -> None:
        
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
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, properties: outputs.PrivateEndpointConnectionPropertiesResponse, type: _builtins.str) -> None:
        
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
    @pulumi.getter
    def properties(self) -> outputs.PrivateEndpointConnectionPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
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
    
    def __init__(__self__, *, status: _builtins.str, actions_required: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
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
    


@pulumi.output_type
class VirtualNetworkPeeringPropertiesFormatResponseDatabricksVirtualNetwork(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualNetworkPeeringPropertiesFormatResponseRemoteVirtualNetwork(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkspaceCustomBooleanParameterResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str, value: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class WorkspaceCustomObjectParameterResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str, value: Any) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Any:
        
        ...
    


@pulumi.output_type
class WorkspaceCustomParametersResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_tags: outputs.WorkspaceCustomObjectParameterResponse, aml_workspace_id: Optional[outputs.WorkspaceCustomStringParameterResponse] = ..., custom_private_subnet_name: Optional[outputs.WorkspaceCustomStringParameterResponse] = ..., custom_public_subnet_name: Optional[outputs.WorkspaceCustomStringParameterResponse] = ..., custom_virtual_network_id: Optional[outputs.WorkspaceCustomStringParameterResponse] = ..., enable_no_public_ip: Optional[outputs.WorkspaceNoPublicIPBooleanParameterResponse] = ..., encryption: Optional[outputs.WorkspaceEncryptionParameterResponse] = ..., load_balancer_backend_pool_name: Optional[outputs.WorkspaceCustomStringParameterResponse] = ..., load_balancer_id: Optional[outputs.WorkspaceCustomStringParameterResponse] = ..., nat_gateway_name: Optional[outputs.WorkspaceCustomStringParameterResponse] = ..., prepare_encryption: Optional[outputs.WorkspaceCustomBooleanParameterResponse] = ..., public_ip_name: Optional[outputs.WorkspaceCustomStringParameterResponse] = ..., require_infrastructure_encryption: Optional[outputs.WorkspaceCustomBooleanParameterResponse] = ..., storage_account_name: Optional[outputs.WorkspaceCustomStringParameterResponse] = ..., storage_account_sku_name: Optional[outputs.WorkspaceCustomStringParameterResponse] = ..., vnet_address_prefix: Optional[outputs.WorkspaceCustomStringParameterResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> outputs.WorkspaceCustomObjectParameterResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amlWorkspaceId")
    def aml_workspace_id(self) -> Optional[outputs.WorkspaceCustomStringParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPrivateSubnetName")
    def custom_private_subnet_name(self) -> Optional[outputs.WorkspaceCustomStringParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPublicSubnetName")
    def custom_public_subnet_name(self) -> Optional[outputs.WorkspaceCustomStringParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customVirtualNetworkId")
    def custom_virtual_network_id(self) -> Optional[outputs.WorkspaceCustomStringParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNoPublicIp")
    def enable_no_public_ip(self) -> Optional[outputs.WorkspaceNoPublicIPBooleanParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.WorkspaceEncryptionParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerBackendPoolName")
    def load_balancer_backend_pool_name(self) -> Optional[outputs.WorkspaceCustomStringParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> Optional[outputs.WorkspaceCustomStringParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="natGatewayName")
    def nat_gateway_name(self) -> Optional[outputs.WorkspaceCustomStringParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prepareEncryption")
    def prepare_encryption(self) -> Optional[outputs.WorkspaceCustomBooleanParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpName")
    def public_ip_name(self) -> Optional[outputs.WorkspaceCustomStringParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireInfrastructureEncryption")
    def require_infrastructure_encryption(self) -> Optional[outputs.WorkspaceCustomBooleanParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[outputs.WorkspaceCustomStringParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountSkuName")
    def storage_account_sku_name(self) -> Optional[outputs.WorkspaceCustomStringParameterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vnetAddressPrefix")
    def vnet_address_prefix(self) -> Optional[outputs.WorkspaceCustomStringParameterResponse]:
        
        ...
    


@pulumi.output_type
class WorkspaceCustomStringParameterResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkspaceEncryptionParameterResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str, value: Optional[outputs.EncryptionResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.EncryptionResponse]:
        
        ...
    


@pulumi.output_type
class WorkspaceNoPublicIPBooleanParameterResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str, value: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class WorkspacePropertiesResponseAccessConnector(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, identity_type: _builtins.str, user_assigned_identity_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityId")
    def user_assigned_identity_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkspacePropertiesResponseEncryption(dict):
    
    def __init__(__self__, *, entities: outputs.EncryptionEntitiesDefinitionResponse) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entities(self) -> outputs.EncryptionEntitiesDefinitionResponse:
        
        ...
    


@pulumi.output_type
class WorkspaceProviderAuthorizationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, role_definition_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> _builtins.str:
        
        ...
    


