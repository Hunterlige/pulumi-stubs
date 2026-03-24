

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
__all__ = ['CustomNamingConventionResponse', 'DecommissionedManagementGroupPropertiesResponse', 'LandingZoneAccountResourcePropertiesResponse', 'LandingZoneConfigurationResourcePropertiesResponse', 'LandingZoneManagementGroupPropertiesResponse', 'LandingZoneRegistrationResourcePropertiesResponse', 'ManagedIdentityPropertiesResponse', 'ManagedServiceIdentityResponse', 'ManagementGroupPropertiesResponse', 'PlatformManagementGroupPropertiesResponse', 'PolicyInitiativeAssignmentPropertiesResponse', 'SandboxManagementGroupPropertiesResponse', 'SystemDataResponse', 'TagsResponse', 'UserAssignedIdentityResponse']
@pulumi.output_type
class CustomNamingConventionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, formula: _builtins.str, resource_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def formula(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DecommissionedManagementGroupPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, create: _builtins.bool, policy_initiatives_assignment_properties: Sequence[outputs.PolicyInitiativeAssignmentPropertiesResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyInitiativesAssignmentProperties")
    def policy_initiatives_assignment_properties(self) -> Sequence[outputs.PolicyInitiativeAssignmentPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class LandingZoneAccountResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, storage_account: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class LandingZoneConfigurationResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authoring_status: _builtins.str, azure_bastion_creation_option: _builtins.str, ddos_protection_creation_option: _builtins.str, firewall_creation_option: _builtins.str, gateway_subnet_cidr_block: _builtins.str, hub_network_cidr_block: _builtins.str, log_analytics_workspace_creation_option: _builtins.str, log_retention_in_days: _builtins.float, managed_identity: outputs.ManagedIdentityPropertiesResponse, provisioning_state: _builtins.str, azure_bastion_subnet_cidr_block: Optional[_builtins.str] = ..., custom_naming_convention: Optional[Sequence[outputs.CustomNamingConventionResponse]] = ..., decommissioned_mg_metadata: Optional[outputs.DecommissionedManagementGroupPropertiesResponse] = ..., existing_azure_bastion_id: Optional[_builtins.str] = ..., existing_ddos_protection_id: Optional[_builtins.str] = ..., existing_log_analytics_workspace_id: Optional[_builtins.str] = ..., firewall_subnet_cidr_block: Optional[_builtins.str] = ..., landing_zones_mg_children: Optional[Sequence[outputs.LandingZoneManagementGroupPropertiesResponse]] = ..., landing_zones_mg_metadata: Optional[outputs.ManagementGroupPropertiesResponse] = ..., naming_convention_formula: Optional[_builtins.str] = ..., platform_connectivity_mg_metadata: Optional[outputs.ManagementGroupPropertiesResponse] = ..., platform_identity_mg_metadata: Optional[outputs.ManagementGroupPropertiesResponse] = ..., platform_management_mg_metadata: Optional[outputs.ManagementGroupPropertiesResponse] = ..., platform_mg_children: Optional[Sequence[outputs.PlatformManagementGroupPropertiesResponse]] = ..., platform_mg_metadata: Optional[outputs.ManagementGroupPropertiesResponse] = ..., sandbox_mg_metadata: Optional[outputs.SandboxManagementGroupPropertiesResponse] = ..., tags: Optional[Sequence[outputs.TagsResponse]] = ..., top_level_mg_metadata: Optional[outputs.ManagementGroupPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authoringStatus")
    def authoring_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBastionCreationOption")
    def azure_bastion_creation_option(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ddosProtectionCreationOption")
    def ddos_protection_creation_option(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallCreationOption")
    def firewall_creation_option(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewaySubnetCidrBlock")
    def gateway_subnet_cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubNetworkCidrBlock")
    def hub_network_cidr_block(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logAnalyticsWorkspaceCreationOption")
    def log_analytics_workspace_creation_option(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logRetentionInDays")
    def log_retention_in_days(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> outputs.ManagedIdentityPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBastionSubnetCidrBlock")
    def azure_bastion_subnet_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customNamingConvention")
    def custom_naming_convention(self) -> Optional[Sequence[outputs.CustomNamingConventionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="decommissionedMgMetadata")
    def decommissioned_mg_metadata(self) -> Optional[outputs.DecommissionedManagementGroupPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="existingAzureBastionId")
    def existing_azure_bastion_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="existingDdosProtectionId")
    def existing_ddos_protection_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="existingLogAnalyticsWorkspaceId")
    def existing_log_analytics_workspace_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallSubnetCidrBlock")
    def firewall_subnet_cidr_block(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="landingZonesMgChildren")
    def landing_zones_mg_children(self) -> Optional[Sequence[outputs.LandingZoneManagementGroupPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="landingZonesMgMetadata")
    def landing_zones_mg_metadata(self) -> Optional[outputs.ManagementGroupPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namingConventionFormula")
    def naming_convention_formula(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformConnectivityMgMetadata")
    def platform_connectivity_mg_metadata(self) -> Optional[outputs.ManagementGroupPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformIdentityMgMetadata")
    def platform_identity_mg_metadata(self) -> Optional[outputs.ManagementGroupPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformManagementMgMetadata")
    def platform_management_mg_metadata(self) -> Optional[outputs.ManagementGroupPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformMgChildren")
    def platform_mg_children(self) -> Optional[Sequence[outputs.PlatformManagementGroupPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformMgMetadata")
    def platform_mg_metadata(self) -> Optional[outputs.ManagementGroupPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sandboxMgMetadata")
    def sandbox_mg_metadata(self) -> Optional[outputs.SandboxManagementGroupPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[outputs.TagsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topLevelMgMetadata")
    def top_level_mg_metadata(self) -> Optional[outputs.ManagementGroupPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class LandingZoneManagementGroupPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, policy_initiatives_assignment_properties: Sequence[outputs.PolicyInitiativeAssignmentPropertiesResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyInitiativesAssignmentProperties")
    def policy_initiatives_assignment_properties(self) -> Sequence[outputs.PolicyInitiativeAssignmentPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class LandingZoneRegistrationResourcePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, existing_landing_zone_configuration_id: _builtins.str, existing_top_level_mg_id: _builtins.str, provisioning_state: _builtins.str, managed_identity: Optional[outputs.ManagedIdentityPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="existingLandingZoneConfigurationId")
    def existing_landing_zone_configuration_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="existingTopLevelMgId")
    def existing_top_level_mg_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[outputs.ManagedIdentityPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class ManagedIdentityPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, user_assigned_identity_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(self) -> Optional[_builtins.str]:
        
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
class ManagementGroupPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, policy_initiatives_assignment_properties: Sequence[outputs.PolicyInitiativeAssignmentPropertiesResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyInitiativesAssignmentProperties")
    def policy_initiatives_assignment_properties(self) -> Sequence[outputs.PolicyInitiativeAssignmentPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class PlatformManagementGroupPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, policy_initiatives_assignment_properties: Sequence[outputs.PolicyInitiativeAssignmentPropertiesResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyInitiativesAssignmentProperties")
    def policy_initiatives_assignment_properties(self) -> Sequence[outputs.PolicyInitiativeAssignmentPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class PolicyInitiativeAssignmentPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assignment_parameters: Any, policy_initiative_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentParameters")
    def assignment_parameters(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyInitiativeId")
    def policy_initiative_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SandboxManagementGroupPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, create: _builtins.bool, policy_initiatives_assignment_properties: Sequence[outputs.PolicyInitiativeAssignmentPropertiesResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyInitiativesAssignmentProperties")
    def policy_initiatives_assignment_properties(self) -> Sequence[outputs.PolicyInitiativeAssignmentPropertiesResponse]:
        
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
class TagsResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
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
    


