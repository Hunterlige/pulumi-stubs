

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
__all__ = ['AzureMonitorWorkspaceIntegrationResponse', 'DashboardDefinitionPropertiesResponse', 'EnterpriseConfigurationsResponse', 'GrafanaConfigurationsResponse', 'GrafanaIntegrationsResponse', 'GrafanaPluginResponse', 'IntegrationFabricPropertiesResponse', 'ManagedGrafanaPropertiesResponse', 'ManagedPrivateEndpointConnectionStateResponse', 'ManagedServiceIdentityResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'ResourceSkuResponse', 'SecurityResponse', 'SmtpResponse', 'SnapshotsResponse', 'SystemDataResponse', 'UserAssignedIdentityResponse', 'UsersResponse']
@pulumi.output_type
class AzureMonitorWorkspaceIntegrationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_monitor_workspace_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureMonitorWorkspaceResourceId")
    def azure_monitor_workspace_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DashboardDefinitionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, serialized_data: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serializedData")
    def serialized_data(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnterpriseConfigurationsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, marketplace_auto_renew: Optional[_builtins.str] = ..., marketplace_plan_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplaceAutoRenew")
    def marketplace_auto_renew(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplacePlanId")
    def marketplace_plan_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GrafanaConfigurationsResponse(dict):
    
    def __init__(__self__, *, security: Optional[outputs.SecurityResponse] = ..., smtp: Optional[outputs.SmtpResponse] = ..., snapshots: Optional[outputs.SnapshotsResponse] = ..., users: Optional[outputs.UsersResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def security(self) -> Optional[outputs.SecurityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def smtp(self) -> Optional[outputs.SmtpResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def snapshots(self) -> Optional[outputs.SnapshotsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def users(self) -> Optional[outputs.UsersResponse]:
        
        ...
    


@pulumi.output_type
class GrafanaIntegrationsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_monitor_workspace_integrations: Optional[Sequence[outputs.AzureMonitorWorkspaceIntegrationResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureMonitorWorkspaceIntegrations")
    def azure_monitor_workspace_integrations(self) -> Optional[Sequence[outputs.AzureMonitorWorkspaceIntegrationResponse]]:
        ...
    


@pulumi.output_type
class GrafanaPluginResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, plugin_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pluginId")
    def plugin_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IntegrationFabricPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, data_source_resource_id: Optional[_builtins.str] = ..., scenarios: Optional[Sequence[_builtins.str]] = ..., target_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceResourceId")
    def data_source_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scenarios(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedGrafanaPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, endpoint: _builtins.str, grafana_version: _builtins.str, outbound_ips: Sequence[_builtins.str], private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionResponse], provisioning_state: _builtins.str, api_key: Optional[_builtins.str] = ..., auto_generated_domain_name_label_scope: Optional[_builtins.str] = ..., deterministic_outbound_ip: Optional[_builtins.str] = ..., enterprise_configurations: Optional[outputs.EnterpriseConfigurationsResponse] = ..., grafana_configurations: Optional[outputs.GrafanaConfigurationsResponse] = ..., grafana_integrations: Optional[outputs.GrafanaIntegrationsResponse] = ..., grafana_major_version: Optional[_builtins.str] = ..., grafana_plugins: Optional[Mapping[str, outputs.GrafanaPluginResponse]] = ..., public_network_access: Optional[_builtins.str] = ..., zone_redundancy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grafanaVersion")
    def grafana_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundIPs")
    def outbound_ips(self) -> Sequence[_builtins.str]:
        
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
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoGeneratedDomainNameLabelScope")
    def auto_generated_domain_name_label_scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deterministicOutboundIP")
    def deterministic_outbound_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enterpriseConfigurations")
    def enterprise_configurations(self) -> Optional[outputs.EnterpriseConfigurationsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grafanaConfigurations")
    def grafana_configurations(self) -> Optional[outputs.GrafanaConfigurationsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grafanaIntegrations")
    def grafana_integrations(self) -> Optional[outputs.GrafanaIntegrationsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grafanaMajorVersion")
    def grafana_major_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grafanaPlugins")
    def grafana_plugins(self) -> Optional[Mapping[str, outputs.GrafanaPluginResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneRedundancy")
    def zone_redundancy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedPrivateEndpointConnectionStateResponse(dict):
    
    def __init__(__self__, *, description: _builtins.str, status: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
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
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse, provisioning_state: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, group_ids: Optional[Sequence[_builtins.str]] = ..., private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...) -> None:
        
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
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
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
class ResourceSkuResponse(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class SecurityResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, csrf_always_check: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="csrfAlwaysCheck")
    def csrf_always_check(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SmtpResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., from_address: Optional[_builtins.str] = ..., from_name: Optional[_builtins.str] = ..., host: Optional[_builtins.str] = ..., password: Optional[_builtins.str] = ..., skip_verify: Optional[_builtins.bool] = ..., start_tls_policy: Optional[_builtins.str] = ..., user: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromAddress")
    def from_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromName")
    def from_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipVerify")
    def skip_verify(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTLSPolicy")
    def start_tls_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SnapshotsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalEnabled")
    def external_enabled(self) -> Optional[_builtins.bool]:
        
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
class UsersResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, viewers_can_edit: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="viewersCanEdit")
    def viewers_can_edit(self) -> Optional[_builtins.bool]:
        
        ...
    


