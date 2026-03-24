

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
__all__ = ['AADAuthTypeConnectionPropertiesResponse', 'AbusePenaltyResponse', 'AccessKeyAuthTypeConnectionPropertiesResponse', 'AccountKeyAuthTypeConnectionPropertiesResponse', 'AccountPropertiesResponse', 'AgentProtocolVersionResponse', 'AgentReferencePropertiesResponse', 'AgentReferenceResponse', 'AgenticApplicationPropertiesResponse', 'ApiKeyAuthConnectionPropertiesResponse', 'ApiPropertiesResponse', 'ApplicationTrafficRoutingPolicyResponse', 'AssignedIdentityResponse', 'CallRateLimitResponse', 'CapabilityHostResponse', 'ChannelsBuiltInAuthorizationPolicyResponse', 'CommitmentPeriodResponse', 'CommitmentPlanAssociationResponse', 'CommitmentPlanPropertiesResponse', 'CommitmentQuotaResponse', 'ConnectionAccessKeyResponse', 'ConnectionAccountKeyResponse', 'ConnectionApiKeyResponse', 'ConnectionManagedIdentityResponse', 'ConnectionOAuth2Response', 'ConnectionPersonalAccessTokenResponse', 'ConnectionServicePrincipalResponse', 'ConnectionSharedAccessSignatureResponse', 'ConnectionUsernamePasswordResponse', 'CustomBlocklistConfigResponse', 'CustomKeysConnectionPropertiesResponse', 'CustomKeysResponse', 'CustomTopicConfigResponse', 'DeploymentCapacitySettingsResponse', 'DeploymentModelResponse', 'DeploymentPropertiesResponse', 'DeploymentScaleSettingsResponse', 'EncryptionResponse', 'EncryptionScopePropertiesResponse', 'FqdnOutboundRuleResponse', 'HostedAgentDeploymentResponse', 'IdentityResponse', 'IpRuleResponse', 'KeyVaultPropertiesResponse', 'ManagedAgentDeploymentResponse', ..., 'MultiRegionSettingsResponse', 'NetworkInjectionResponse', 'NetworkRuleSetResponse', 'NoneAuthTypeConnectionPropertiesResponse', 'OAuth2AuthTypeConnectionPropertiesResponse', ..., 'PATAuthTypeConnectionPropertiesResponse', 'PrivateEndpointConnectionPropertiesResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'ProjectCapabilityHostResponse', 'ProjectPropertiesResponse', 'QuotaLimitResponse', 'RaiBlocklistItemPropertiesResponse', 'RaiBlocklistPropertiesResponse', 'RaiExternalSafetyProviderSchemaPropertiesResponse', 'RaiMonitorConfigResponse', 'RaiPolicyContentFilterResponse', 'RaiPolicyContentFilterResponseV1', 'RaiPolicyPropertiesResponse', 'RaiPolicyPropertiesResponseV1', 'RaiToolLabelPropertiesResponse', 'RaiToolLabelPropertiesResponseAccountScope', 'RaiToolLabelPropertiesResponseProjectScopes', 'RaiTopicPropertiesResponse', 'RegionSettingResponse', 'RequestMatchPatternResponse', 'RoleBasedBuiltInAuthorizationPolicyResponse', 'SASAuthTypeConnectionPropertiesResponse', 'SafetyProviderConfigResponse', ..., 'SkuCapabilityResponse', 'SkuChangeInfoResponse', 'SkuResponse', 'SystemDataResponse', 'ThrottlingRuleResponse', 'TrafficRoutingRuleResponse', 'UserAssignedIdentityResponse', 'UserOwnedAmlWorkspaceResponse', 'UserOwnedStorageResponse', ..., 'VersionedAgentReferenceResponse', 'VirtualNetworkRuleResponse']
@pulumi.output_type
class AADAuthTypeConnectionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, created_by_workspace_arm_id: _builtins.str, group: _builtins.str, category: Optional[_builtins.str] = ..., error: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., is_shared_to_all: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., pe_requirement: Optional[_builtins.str] = ..., pe_status: Optional[_builtins.str] = ..., shared_user_list: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ..., use_workspace_managed_identity: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByWorkspaceArmId")
    def created_by_workspace_arm_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class AbusePenaltyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: Optional[_builtins.str] = ..., expiration: Optional[_builtins.str] = ..., rate_limit_percentage: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateLimitPercentage")
    def rate_limit_percentage(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AccessKeyAuthTypeConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, created_by_workspace_arm_id: _builtins.str, group: _builtins.str, category: Optional[_builtins.str] = ..., credentials: Optional[outputs.ConnectionAccessKeyResponse] = ..., error: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., is_shared_to_all: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., pe_requirement: Optional[_builtins.str] = ..., pe_status: Optional[_builtins.str] = ..., shared_user_list: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ..., use_workspace_managed_identity: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByWorkspaceArmId")
    def created_by_workspace_arm_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.ConnectionAccessKeyResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class AccountKeyAuthTypeConnectionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, created_by_workspace_arm_id: _builtins.str, group: _builtins.str, category: Optional[_builtins.str] = ..., credentials: Optional[outputs.ConnectionAccountKeyResponse] = ..., error: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., is_shared_to_all: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., pe_requirement: Optional[_builtins.str] = ..., pe_status: Optional[_builtins.str] = ..., shared_user_list: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ..., use_workspace_managed_identity: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByWorkspaceArmId")
    def created_by_workspace_arm_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.ConnectionAccountKeyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class AccountPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, abuse_penalty: outputs.AbusePenaltyResponse, call_rate_limit: outputs.CallRateLimitResponse, capabilities: Sequence[outputs.SkuCapabilityResponse], commitment_plan_associations: Sequence[outputs.CommitmentPlanAssociationResponse], date_created: _builtins.str, deletion_date: _builtins.str, endpoint: _builtins.str, endpoints: Mapping[str, _builtins.str], internal_id: _builtins.str, is_migrated: _builtins.bool, private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionResponse], provisioning_state: _builtins.str, quota_limit: outputs.QuotaLimitResponse, scheduled_purge_date: _builtins.str, sku_change_info: outputs.SkuChangeInfoResponse, allow_project_management: Optional[_builtins.bool] = ..., allowed_fqdn_list: Optional[Sequence[_builtins.str]] = ..., aml_workspace: Optional[outputs.UserOwnedAmlWorkspaceResponse] = ..., api_properties: Optional[outputs.ApiPropertiesResponse] = ..., associated_projects: Optional[Sequence[_builtins.str]] = ..., custom_sub_domain_name: Optional[_builtins.str] = ..., default_project: Optional[_builtins.str] = ..., disable_local_auth: Optional[_builtins.bool] = ..., dynamic_throttling_enabled: Optional[_builtins.bool] = ..., encryption: Optional[outputs.EncryptionResponse] = ..., locations: Optional[outputs.MultiRegionSettingsResponse] = ..., migration_token: Optional[_builtins.str] = ..., network_acls: Optional[outputs.NetworkRuleSetResponse] = ..., network_injections: Optional[Sequence[outputs.NetworkInjectionResponse]] = ..., public_network_access: Optional[_builtins.str] = ..., rai_monitor_config: Optional[outputs.RaiMonitorConfigResponse] = ..., restrict_outbound_network_access: Optional[_builtins.bool] = ..., user_owned_storage: Optional[Sequence[outputs.UserOwnedStorageResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="abusePenalty")
    def abuse_penalty(self) -> outputs.AbusePenaltyResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callRateLimit")
    def call_rate_limit(self) -> outputs.CallRateLimitResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Sequence[outputs.SkuCapabilityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitmentPlanAssociations")
    def commitment_plan_associations(self) -> Sequence[outputs.CommitmentPlanAssociationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionDate")
    def deletion_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalId")
    def internal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMigrated")
    def is_migrated(self) -> _builtins.bool:
        
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
    @pulumi.getter(name="quotaLimit")
    def quota_limit(self) -> outputs.QuotaLimitResponse:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledPurgeDate")
    def scheduled_purge_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skuChangeInfo")
    def sku_change_info(self) -> outputs.SkuChangeInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowProjectManagement")
    def allow_project_management(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedFqdnList")
    def allowed_fqdn_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amlWorkspace")
    def aml_workspace(self) -> Optional[outputs.UserOwnedAmlWorkspaceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiProperties")
    def api_properties(self) -> Optional[outputs.ApiPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedProjects")
    def associated_projects(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customSubDomainName")
    def custom_sub_domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultProject")
    def default_project(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicThrottlingEnabled")
    def dynamic_throttling_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.EncryptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[outputs.MultiRegionSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationToken")
    def migration_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional[outputs.NetworkRuleSetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInjections")
    def network_injections(self) -> Optional[Sequence[outputs.NetworkInjectionResponse]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="raiMonitorConfig")
    def rai_monitor_config(self) -> Optional[outputs.RaiMonitorConfigResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictOutboundNetworkAccess")
    def restrict_outbound_network_access(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userOwnedStorage")
    def user_owned_storage(self) -> Optional[Sequence[outputs.UserOwnedStorageResponse]]:
        
        ...
    


@pulumi.output_type
class AgentProtocolVersionResponse(dict):
    
    def __init__(__self__, *, protocol: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AgentReferencePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_id: Optional[_builtins.str] = ..., agent_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AgentReferenceResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, properties: outputs.AgentReferencePropertiesResponse, system_data: outputs.SystemDataResponse, type: _builtins.str) -> None:
        
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
    def properties(self) -> outputs.AgentReferencePropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AgenticApplicationPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_enabled: _builtins.bool, provisioning_state: _builtins.str, agent_identity_blueprint: Optional[outputs.AssignedIdentityResponse] = ..., agents: Optional[Sequence[outputs.AgentReferencePropertiesResponse]] = ..., authorization_policy: Optional[Any] = ..., base_url: Optional[_builtins.str] = ..., default_instance_identity: Optional[outputs.AssignedIdentityResponse] = ..., description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., traffic_routing_policy: Optional[outputs.ApplicationTrafficRoutingPolicyResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentIdentityBlueprint")
    def agent_identity_blueprint(self) -> Optional[outputs.AssignedIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agents(self) -> Optional[Sequence[outputs.AgentReferencePropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationPolicy")
    def authorization_policy(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultInstanceIdentity")
    def default_instance_identity(self) -> Optional[outputs.AssignedIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficRoutingPolicy")
    def traffic_routing_policy(self) -> Optional[outputs.ApplicationTrafficRoutingPolicyResponse]:
        
        ...
    


@pulumi.output_type
class ApiKeyAuthConnectionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, created_by_workspace_arm_id: _builtins.str, group: _builtins.str, category: Optional[_builtins.str] = ..., credentials: Optional[outputs.ConnectionApiKeyResponse] = ..., error: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., is_shared_to_all: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., pe_requirement: Optional[_builtins.str] = ..., pe_status: Optional[_builtins.str] = ..., shared_user_list: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ..., use_workspace_managed_identity: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByWorkspaceArmId")
    def created_by_workspace_arm_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.ConnectionApiKeyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class ApiPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aad_client_id: Optional[_builtins.str] = ..., aad_tenant_id: Optional[_builtins.str] = ..., event_hub_connection_string: Optional[_builtins.str] = ..., qna_azure_search_endpoint_id: Optional[_builtins.str] = ..., qna_azure_search_endpoint_key: Optional[_builtins.str] = ..., qna_runtime_endpoint: Optional[_builtins.str] = ..., statistics_enabled: Optional[_builtins.bool] = ..., storage_account_connection_string: Optional[_builtins.str] = ..., super_user: Optional[_builtins.str] = ..., website_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadClientId")
    def aad_client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aadTenantId")
    def aad_tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubConnectionString")
    def event_hub_connection_string(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qnaAzureSearchEndpointId")
    def qna_azure_search_endpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qnaAzureSearchEndpointKey")
    def qna_azure_search_endpoint_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qnaRuntimeEndpoint")
    def qna_runtime_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statisticsEnabled")
    def statistics_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountConnectionString")
    def storage_account_connection_string(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="superUser")
    def super_user(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="websiteName")
    def website_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ApplicationTrafficRoutingPolicyResponse(dict):
    
    def __init__(__self__, *, protocol: Optional[_builtins.str] = ..., rules: Optional[Sequence[outputs.TrafficRoutingRuleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.TrafficRoutingRuleResponse]]:
        
        ...
    


@pulumi.output_type
class AssignedIdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, kind: _builtins.str, principal_id: _builtins.str, provisioning_state: _builtins.str, tenant_id: _builtins.str, type: _builtins.str, subject: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
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
    @pulumi.getter
    def subject(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CallRateLimitResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, count: Optional[_builtins.float] = ..., renewal_period: Optional[_builtins.float] = ..., rules: Optional[Sequence[outputs.ThrottlingRuleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalPeriod")
    def renewal_period(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.ThrottlingRuleResponse]]:
        ...
    


@pulumi.output_type
class CapabilityHostResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, ai_services_connections: Optional[Sequence[_builtins.str]] = ..., capability_host_kind: Optional[_builtins.str] = ..., customer_subnet: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., storage_connections: Optional[Sequence[_builtins.str]] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., thread_storage_connections: Optional[Sequence[_builtins.str]] = ..., vector_store_connections: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aiServicesConnections")
    def ai_services_connections(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capabilityHostKind")
    def capability_host_kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerSubnet")
    def customer_subnet(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConnections")
    def storage_connections(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadStorageConnections")
    def thread_storage_connections(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorStoreConnections")
    def vector_store_connections(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ChannelsBuiltInAuthorizationPolicyResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CommitmentPeriodResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_date: _builtins.str, quota: outputs.CommitmentQuotaResponse, start_date: _builtins.str, count: Optional[_builtins.int] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def quota(self) -> outputs.CommitmentQuotaResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CommitmentPlanAssociationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, commitment_plan_id: Optional[_builtins.str] = ..., commitment_plan_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitmentPlanId")
    def commitment_plan_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitmentPlanLocation")
    def commitment_plan_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CommitmentPlanPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, last: outputs.CommitmentPeriodResponse, provisioning_issues: Sequence[_builtins.str], provisioning_state: _builtins.str, auto_renew: Optional[_builtins.bool] = ..., commitment_plan_guid: Optional[_builtins.str] = ..., current: Optional[outputs.CommitmentPeriodResponse] = ..., hosting_model: Optional[_builtins.str] = ..., next: Optional[outputs.CommitmentPeriodResponse] = ..., plan_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def last(self) -> outputs.CommitmentPeriodResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningIssues")
    def provisioning_issues(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitmentPlanGuid")
    def commitment_plan_guid(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def current(self) -> Optional[outputs.CommitmentPeriodResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostingModel")
    def hosting_model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def next(self) -> Optional[outputs.CommitmentPeriodResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="planType")
    def plan_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CommitmentQuotaResponse(dict):
    
    def __init__(__self__, *, quantity: Optional[_builtins.float] = ..., unit: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def quantity(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionAccessKeyResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_key_id: Optional[_builtins.str] = ..., secret_access_key: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ConnectionAccountKeyResponse(dict):
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ConnectionApiKeyResponse(dict):
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ConnectionManagedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ConnectionOAuth2Response(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_url: Optional[_builtins.str] = ..., client_id: Optional[_builtins.str] = ..., client_secret: Optional[_builtins.str] = ..., developer_token: Optional[_builtins.str] = ..., password: Optional[_builtins.str] = ..., refresh_token: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authUrl")
    def auth_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerToken")
    def developer_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionPersonalAccessTokenResponse(dict):
    def __init__(__self__, *, pat: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def pat(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ConnectionServicePrincipalResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., client_secret: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ConnectionSharedAccessSignatureResponse(dict):
    def __init__(__self__, *, sas: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sas(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ConnectionUsernamePasswordResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, password: Optional[_builtins.str] = ..., security_token: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class CustomBlocklistConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, blocking: Optional[_builtins.bool] = ..., blocklist_name: Optional[_builtins.str] = ..., source: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def blocking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blocklistName")
    def blocklist_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CustomKeysConnectionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, created_by_workspace_arm_id: _builtins.str, group: _builtins.str, category: Optional[_builtins.str] = ..., credentials: Optional[outputs.CustomKeysResponse] = ..., error: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., is_shared_to_all: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., pe_requirement: Optional[_builtins.str] = ..., pe_status: Optional[_builtins.str] = ..., shared_user_list: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ..., use_workspace_managed_identity: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByWorkspaceArmId")
    def created_by_workspace_arm_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.CustomKeysResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class CustomKeysResponse(dict):
    
    def __init__(__self__, *, keys: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[Mapping[str, _builtins.str]]:
        ...
    


@pulumi.output_type
class CustomTopicConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, blocking: Optional[_builtins.bool] = ..., source: Optional[_builtins.str] = ..., topic_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def blocking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentCapacitySettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, designated_capacity: Optional[_builtins.int] = ..., priority: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="designatedCapacity")
    def designated_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DeploymentModelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, call_rate_limit: outputs.CallRateLimitResponse, format: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., publisher: Optional[_builtins.str] = ..., source: Optional[_builtins.str] = ..., source_account: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callRateLimit")
    def call_rate_limit(self) -> outputs.CallRateLimitResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, call_rate_limit: outputs.CallRateLimitResponse, capabilities: Mapping[str, _builtins.str], dynamic_throttling_enabled: _builtins.bool, provisioning_state: _builtins.str, rate_limits: Sequence[outputs.ThrottlingRuleResponse], capacity_settings: Optional[outputs.DeploymentCapacitySettingsResponse] = ..., current_capacity: Optional[_builtins.int] = ..., model: Optional[outputs.DeploymentModelResponse] = ..., parent_deployment_name: Optional[_builtins.str] = ..., rai_policy_name: Optional[_builtins.str] = ..., scale_settings: Optional[outputs.DeploymentScaleSettingsResponse] = ..., spillover_deployment_name: Optional[_builtins.str] = ..., version_upgrade_option: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callRateLimit")
    def call_rate_limit(self) -> outputs.CallRateLimitResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicThrottlingEnabled")
    def dynamic_throttling_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateLimits")
    def rate_limits(self) -> Sequence[outputs.ThrottlingRuleResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacitySettings")
    def capacity_settings(self) -> Optional[outputs.DeploymentCapacitySettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentCapacity")
    def current_capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[outputs.DeploymentModelResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentDeploymentName")
    def parent_deployment_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="raiPolicyName")
    def rai_policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleSettings")
    def scale_settings(self) -> Optional[outputs.DeploymentScaleSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spilloverDeploymentName")
    def spillover_deployment_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionUpgradeOption")
    def version_upgrade_option(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentScaleSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_capacity: _builtins.int, capacity: Optional[_builtins.int] = ..., scale_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeCapacity")
    def active_capacity(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleType")
    def scale_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EncryptionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_source: Optional[_builtins.str] = ..., key_vault_properties: Optional[outputs.KeyVaultPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[outputs.KeyVaultPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class EncryptionScopePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, key_source: Optional[_builtins.str] = ..., key_vault_properties: Optional[outputs.KeyVaultPropertiesResponse] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[outputs.KeyVaultPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FqdnOutboundRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_information: _builtins.str, parent_rule_names: Sequence[_builtins.str], type: _builtins.str, category: Optional[_builtins.str] = ..., destination: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorInformation")
    def error_information(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentRuleNames")
    def parent_rule_names(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HostedAgentDeploymentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment_type: _builtins.str, provisioning_state: _builtins.str, agents: Optional[Sequence[outputs.VersionedAgentReferenceResponse]] = ..., deployment_id: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., max_replicas: Optional[_builtins.int] = ..., min_replicas: Optional[_builtins.int] = ..., protocols: Optional[Sequence[outputs.AgentProtocolVersionResponse]] = ..., state: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agents(self) -> Optional[Sequence[outputs.VersionedAgentReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxReplicas")
    def max_replicas(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minReplicas")
    def min_replicas(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Optional[Sequence[outputs.AgentProtocolVersionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class IdentityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ..., user_assigned_identities: Optional[Mapping[str, outputs.UserAssignedIdentityResponse]] = ...) -> None:
        
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
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]:
        
        ...
    


@pulumi.output_type
class IpRuleResponse(dict):
    
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class KeyVaultPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity_client_id: Optional[_builtins.str] = ..., key_name: Optional[_builtins.str] = ..., key_vault_uri: Optional[_builtins.str] = ..., key_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]:
        
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
class ManagedAgentDeploymentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment_type: _builtins.str, provisioning_state: _builtins.str, agents: Optional[Sequence[outputs.VersionedAgentReferenceResponse]] = ..., deployment_id: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., protocols: Optional[Sequence[outputs.AgentProtocolVersionResponse]] = ..., state: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agents(self) -> Optional[Sequence[outputs.VersionedAgentReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> Optional[Sequence[outputs.AgentProtocolVersionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class ManagedIdentityAuthTypeConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, created_by_workspace_arm_id: _builtins.str, group: _builtins.str, category: Optional[_builtins.str] = ..., credentials: Optional[outputs.ConnectionManagedIdentityResponse] = ..., error: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., is_shared_to_all: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., pe_requirement: Optional[_builtins.str] = ..., pe_status: Optional[_builtins.str] = ..., shared_user_list: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ..., use_workspace_managed_identity: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByWorkspaceArmId")
    def created_by_workspace_arm_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.ConnectionManagedIdentityResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class MultiRegionSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, regions: Optional[Sequence[outputs.RegionSettingResponse]] = ..., routing_method: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[outputs.RegionSettingResponse]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingMethod")
    def routing_method(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NetworkInjectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scenario: Optional[_builtins.str] = ..., subnet_arm_id: Optional[_builtins.str] = ..., use_microsoft_managed_network: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scenario(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetArmId")
    def subnet_arm_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useMicrosoftManagedNetwork")
    def use_microsoft_managed_network(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class NetworkRuleSetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bypass: Optional[_builtins.str] = ..., default_action: Optional[_builtins.str] = ..., ip_rules: Optional[Sequence[outputs.IpRuleResponse]] = ..., virtual_network_rules: Optional[Sequence[outputs.VirtualNetworkRuleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bypass(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[Sequence[outputs.IpRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Optional[Sequence[outputs.VirtualNetworkRuleResponse]]:
        
        ...
    


@pulumi.output_type
class NoneAuthTypeConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, created_by_workspace_arm_id: _builtins.str, group: _builtins.str, category: Optional[_builtins.str] = ..., error: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., is_shared_to_all: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., pe_requirement: Optional[_builtins.str] = ..., pe_status: Optional[_builtins.str] = ..., shared_user_list: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ..., use_workspace_managed_identity: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByWorkspaceArmId")
    def created_by_workspace_arm_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class OAuth2AuthTypeConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, created_by_workspace_arm_id: _builtins.str, group: _builtins.str, category: Optional[_builtins.str] = ..., credentials: Optional[outputs.ConnectionOAuth2Response] = ..., error: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., is_shared_to_all: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., pe_requirement: Optional[_builtins.str] = ..., pe_status: Optional[_builtins.str] = ..., shared_user_list: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ..., use_workspace_managed_identity: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByWorkspaceArmId")
    def created_by_workspace_arm_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.ConnectionOAuth2Response]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class OrganizationSharedBuiltInAuthorizationPolicyResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PATAuthTypeConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, created_by_workspace_arm_id: _builtins.str, group: _builtins.str, category: Optional[_builtins.str] = ..., credentials: Optional[outputs.ConnectionPersonalAccessTokenResponse] = ..., error: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., is_shared_to_all: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., pe_requirement: Optional[_builtins.str] = ..., pe_status: Optional[_builtins.str] = ..., shared_user_list: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ..., use_workspace_managed_identity: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByWorkspaceArmId")
    def created_by_workspace_arm_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.ConnectionPersonalAccessTokenResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(self) -> Optional[_builtins.bool]:
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
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, etag: _builtins.str, id: _builtins.str, name: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, location: Optional[_builtins.str] = ..., properties: Optional[outputs.PrivateEndpointConnectionPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.PrivateEndpointConnectionPropertiesResponse]:
        
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
class ProjectCapabilityHostResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, ai_services_connections: Optional[Sequence[_builtins.str]] = ..., storage_connections: Optional[Sequence[_builtins.str]] = ..., thread_storage_connections: Optional[Sequence[_builtins.str]] = ..., vector_store_connections: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aiServicesConnections")
    def ai_services_connections(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConnections")
    def storage_connections(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threadStorageConnections")
    def thread_storage_connections(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorStoreConnections")
    def vector_store_connections(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ProjectPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, endpoints: Mapping[str, _builtins.str], is_default: _builtins.bool, provisioning_state: _builtins.str, description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class QuotaLimitResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, count: Optional[_builtins.float] = ..., renewal_period: Optional[_builtins.float] = ..., rules: Optional[Sequence[outputs.ThrottlingRuleResponse]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalPeriod")
    def renewal_period(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.ThrottlingRuleResponse]]:
        ...
    


@pulumi.output_type
class RaiBlocklistItemPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_regex: Optional[_builtins.bool] = ..., pattern: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRegex")
    def is_regex(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RaiBlocklistPropertiesResponse(dict):
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RaiExternalSafetyProviderSchemaPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: _builtins.str, last_modified_at: _builtins.str, key_vault_uri: Optional[_builtins.str] = ..., managed_identity: Optional[_builtins.str] = ..., mode: Optional[_builtins.str] = ..., provider_id: Optional[_builtins.str] = ..., provider_name: Optional[_builtins.str] = ..., secret_name: Optional[_builtins.str] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentity")
    def managed_identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerId")
    def provider_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RaiMonitorConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, adx_storage_resource_id: Optional[_builtins.str] = ..., identity_client_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adxStorageResourceId")
    def adx_storage_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RaiPolicyContentFilterResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, blocking: Optional[_builtins.bool] = ..., enabled: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ..., severity_threshold: Optional[_builtins.str] = ..., source: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def blocking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="severityThreshold")
    def severity_threshold(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RaiPolicyContentFilterResponseV1(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: Optional[_builtins.str] = ..., blocking: Optional[_builtins.bool] = ..., enabled: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ..., severity_threshold: Optional[_builtins.str] = ..., source: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def blocking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="severityThreshold")
    def severity_threshold(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RaiPolicyPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, base_policy_name: Optional[_builtins.str] = ..., content_filters: Optional[Sequence[outputs.RaiPolicyContentFilterResponse]] = ..., custom_blocklists: Optional[Sequence[outputs.CustomBlocklistConfigResponse]] = ..., mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePolicyName")
    def base_policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentFilters")
    def content_filters(self) -> Optional[Sequence[outputs.RaiPolicyContentFilterResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customBlocklists")
    def custom_blocklists(self) -> Optional[Sequence[outputs.CustomBlocklistConfigResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RaiPolicyPropertiesResponseV1(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, base_policy_name: Optional[_builtins.str] = ..., content_filters: Optional[Sequence[outputs.RaiPolicyContentFilterResponseV1]] = ..., custom_blocklists: Optional[Sequence[outputs.CustomBlocklistConfigResponse]] = ..., custom_topics: Optional[Sequence[outputs.CustomTopicConfigResponse]] = ..., mode: Optional[_builtins.str] = ..., safety_providers: Optional[Sequence[outputs.SafetyProviderConfigResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basePolicyName")
    def base_policy_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentFilters")
    def content_filters(self) -> Optional[Sequence[outputs.RaiPolicyContentFilterResponseV1]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customBlocklists")
    def custom_blocklists(self) -> Optional[Sequence[outputs.CustomBlocklistConfigResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customTopics")
    def custom_topics(self) -> Optional[Sequence[outputs.CustomTopicConfigResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="safetyProviders")
    def safety_providers(self) -> Optional[Sequence[outputs.SafetyProviderConfigResponse]]:
        
        ...
    


@pulumi.output_type
class RaiToolLabelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tool_connection_name: _builtins.str, account_scope: Optional[outputs.RaiToolLabelPropertiesResponseAccountScope] = ..., project_scopes: Optional[Sequence[outputs.RaiToolLabelPropertiesResponseProjectScopes]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolConnectionName")
    def tool_connection_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountScope")
    def account_scope(self) -> Optional[outputs.RaiToolLabelPropertiesResponseAccountScope]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectScopes")
    def project_scopes(self) -> Optional[Sequence[outputs.RaiToolLabelPropertiesResponseProjectScopes]]:
        
        ...
    


@pulumi.output_type
class RaiToolLabelPropertiesResponseAccountScope(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, label_values: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelValues")
    def label_values(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class RaiToolLabelPropertiesResponseProjectScopes(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, label_values: Mapping[str, _builtins.str], project: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelValues")
    def label_values(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RaiTopicPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., failed_reason: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., sample_blob_url: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ..., topic_id: Optional[_builtins.str] = ..., topic_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failedReason")
    def failed_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleBlobUrl")
    def sample_blob_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicId")
    def topic_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RegionSettingResponse(dict):
    
    def __init__(__self__, *, customsubdomain: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., value: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def customsubdomain(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class RequestMatchPatternResponse(dict):
    def __init__(__self__, *, method: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RoleBasedBuiltInAuthorizationPolicyResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SASAuthTypeConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, created_by_workspace_arm_id: _builtins.str, group: _builtins.str, category: Optional[_builtins.str] = ..., credentials: Optional[outputs.ConnectionSharedAccessSignatureResponse] = ..., error: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., is_shared_to_all: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., pe_requirement: Optional[_builtins.str] = ..., pe_status: Optional[_builtins.str] = ..., shared_user_list: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ..., use_workspace_managed_identity: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByWorkspaceArmId")
    def created_by_workspace_arm_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.ConnectionSharedAccessSignatureResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class SafetyProviderConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, blocking: Optional[_builtins.bool] = ..., safety_provider_name: Optional[_builtins.str] = ..., source: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def blocking(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="safetyProviderName")
    def safety_provider_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServicePrincipalAuthTypeConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, created_by_workspace_arm_id: _builtins.str, group: _builtins.str, category: Optional[_builtins.str] = ..., credentials: Optional[outputs.ConnectionServicePrincipalResponse] = ..., error: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., is_shared_to_all: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., pe_requirement: Optional[_builtins.str] = ..., pe_status: Optional[_builtins.str] = ..., shared_user_list: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ..., use_workspace_managed_identity: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByWorkspaceArmId")
    def created_by_workspace_arm_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.ConnectionServicePrincipalResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class SkuCapabilityResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuChangeInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, count_of_downgrades: Optional[_builtins.float] = ..., count_of_upgrades_after_downgrades: Optional[_builtins.float] = ..., last_change_date: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countOfDowngrades")
    def count_of_downgrades(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countOfUpgradesAfterDowngrades")
    def count_of_upgrades_after_downgrades(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastChangeDate")
    def last_change_date(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, capacity: Optional[_builtins.int] = ..., family: Optional[_builtins.str] = ..., size: Optional[_builtins.str] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]:
        
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
class ThrottlingRuleResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, count: Optional[_builtins.float] = ..., dynamic_throttling_enabled: Optional[_builtins.bool] = ..., key: Optional[_builtins.str] = ..., match_patterns: Optional[Sequence[outputs.RequestMatchPatternResponse]] = ..., min_count: Optional[_builtins.float] = ..., renewal_period: Optional[_builtins.float] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicThrottlingEnabled")
    def dynamic_throttling_enabled(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Optional[Sequence[outputs.RequestMatchPatternResponse]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="renewalPeriod")
    def renewal_period(self) -> Optional[_builtins.float]:
        ...
    


@pulumi.output_type
class TrafficRoutingRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment_id: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., rule_id: Optional[_builtins.str] = ..., traffic_percentage: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trafficPercentage")
    def traffic_percentage(self) -> Optional[_builtins.int]:
        
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
class UserOwnedAmlWorkspaceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity_client_id: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UserOwnedStorageResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity_client_id: Optional[_builtins.str] = ..., resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class UsernamePasswordAuthTypeConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_type: _builtins.str, created_by_workspace_arm_id: _builtins.str, group: _builtins.str, category: Optional[_builtins.str] = ..., credentials: Optional[outputs.ConnectionUsernamePasswordResponse] = ..., error: Optional[_builtins.str] = ..., expiry_time: Optional[_builtins.str] = ..., is_shared_to_all: Optional[_builtins.bool] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., pe_requirement: Optional[_builtins.str] = ..., pe_status: Optional[_builtins.str] = ..., shared_user_list: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ..., use_workspace_managed_identity: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByWorkspaceArmId")
    def created_by_workspace_arm_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.ConnectionUsernamePasswordResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSharedToAll")
    def is_shared_to_all(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peRequirement")
    def pe_requirement(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peStatus")
    def pe_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedUserList")
    def shared_user_list(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="useWorkspaceManagedIdentity")
    def use_workspace_managed_identity(self) -> Optional[_builtins.bool]:
        ...
    


@pulumi.output_type
class VersionedAgentReferenceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_id: Optional[_builtins.str] = ..., agent_name: Optional[_builtins.str] = ..., agent_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VirtualNetworkRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, ignore_missing_vnet_service_endpoint: Optional[_builtins.bool] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


