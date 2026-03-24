

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
__all__ = ['AccessPolicyEntry', 'AccessPolicyEntryResponse', 'ActionResponse', 'IPRuleResponse', 'KeyAttributesResponse', 'KeyReleasePolicyResponse', 'KeyRotationPolicyAttributesResponse', 'LifetimeActionResponse', 'MHSMGeoReplicatedRegionResponse', 'MHSMIPRuleResponse', 'MHSMNetworkRuleSetResponse', 'MHSMPrivateEndpointConnectionItemResponse', 'MHSMPrivateEndpointResponse', 'MHSMPrivateLinkServiceConnectionStateResponse', 'MHSMVirtualNetworkRuleResponse', 'ManagedHSMSecurityDomainPropertiesResponse', 'ManagedHsmPropertiesResponse', 'ManagedHsmSkuResponse', 'ManagedServiceIdentityResponse', 'NetworkRuleSetResponse', 'Permissions', 'PermissionsResponse', 'PrivateEndpointConnectionItemResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'RotationPolicyResponse', 'SecretAttributesResponse', 'SecretPropertiesResponse', 'SkuResponse', 'SystemDataResponse', 'TriggerResponse', 'UserAssignedIdentityResponse', 'VaultPropertiesResponse', 'VirtualNetworkRuleResponse']
@pulumi.output_type
class AccessPolicyEntry(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, object_id: _builtins.str, permissions: outputs.Permissions, tenant_id: _builtins.str, application_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> outputs.Permissions:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AccessPolicyEntryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, object_id: _builtins.str, permissions: outputs.PermissionsResponse, tenant_id: _builtins.str, application_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> outputs.PermissionsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ActionResponse(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IPRuleResponse(dict):
    
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class KeyAttributesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created: _builtins.float, recovery_level: _builtins.str, updated: _builtins.float, enabled: Optional[_builtins.bool] = ..., expires: Optional[_builtins.float] = ..., exportable: Optional[_builtins.bool] = ..., not_before: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryLevel")
    def recovery_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def updated(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expires(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def exportable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class KeyReleasePolicyResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content_type: Optional[_builtins.str] = ..., data: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class KeyRotationPolicyAttributesResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created: _builtins.float, updated: _builtins.float, expiry_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def updated(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LifetimeActionResponse(dict):
    def __init__(__self__, *, action: Optional[outputs.ActionResponse] = ..., trigger: Optional[outputs.TriggerResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[outputs.ActionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[outputs.TriggerResponse]:
        
        ...
    


@pulumi.output_type
class MHSMGeoReplicatedRegionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, is_primary: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MHSMIPRuleResponse(dict):
    
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MHSMNetworkRuleSetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bypass: Optional[_builtins.str] = ..., default_action: Optional[_builtins.str] = ..., ip_rules: Optional[Sequence[outputs.MHSMIPRuleResponse]] = ..., virtual_network_rules: Optional[Sequence[outputs.MHSMVirtualNetworkRuleResponse]] = ...) -> None:
        
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
    def ip_rules(self) -> Optional[Sequence[outputs.MHSMIPRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Optional[Sequence[outputs.MHSMVirtualNetworkRuleResponse]]:
        
        ...
    


@pulumi.output_type
class MHSMPrivateEndpointConnectionItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., private_endpoint: Optional[outputs.MHSMPrivateEndpointResponse] = ..., private_link_service_connection_state: Optional[outputs.MHSMPrivateLinkServiceConnectionStateResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.MHSMPrivateEndpointResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[outputs.MHSMPrivateLinkServiceConnectionStateResponse]:
        
        ...
    


@pulumi.output_type
class MHSMPrivateEndpointResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class MHSMPrivateLinkServiceConnectionStateResponse(dict):
    
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
class MHSMVirtualNetworkRuleResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagedHSMSecurityDomainPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, activation_status: _builtins.str, activation_status_message: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationStatus")
    def activation_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationStatusMessage")
    def activation_status_message(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagedHsmPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hsm_uri: _builtins.str, private_endpoint_connections: Sequence[outputs.MHSMPrivateEndpointConnectionItemResponse], provisioning_state: _builtins.str, scheduled_purge_date: _builtins.str, security_domain_properties: outputs.ManagedHSMSecurityDomainPropertiesResponse, status_message: _builtins.str, enable_purge_protection: Optional[_builtins.bool] = ..., enable_soft_delete: Optional[_builtins.bool] = ..., initial_admin_object_ids: Optional[Sequence[_builtins.str]] = ..., network_acls: Optional[outputs.MHSMNetworkRuleSetResponse] = ..., public_network_access: Optional[_builtins.str] = ..., regions: Optional[Sequence[outputs.MHSMGeoReplicatedRegionResponse]] = ..., soft_delete_retention_in_days: Optional[_builtins.int] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmUri")
    def hsm_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.MHSMPrivateEndpointConnectionItemResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledPurgeDate")
    def scheduled_purge_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityDomainProperties")
    def security_domain_properties(self) -> outputs.ManagedHSMSecurityDomainPropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePurgeProtection")
    def enable_purge_protection(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSoftDelete")
    def enable_soft_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialAdminObjectIds")
    def initial_admin_object_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional[outputs.MHSMNetworkRuleSetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[outputs.MHSMGeoReplicatedRegionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionInDays")
    def soft_delete_retention_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedHsmSkuResponse(dict):
    
    def __init__(__self__, *, family: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
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
class NetworkRuleSetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bypass: Optional[_builtins.str] = ..., default_action: Optional[_builtins.str] = ..., ip_rules: Optional[Sequence[outputs.IPRuleResponse]] = ..., virtual_network_rules: Optional[Sequence[outputs.VirtualNetworkRuleResponse]] = ...) -> None:
        
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
    def ip_rules(self) -> Optional[Sequence[outputs.IPRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Optional[Sequence[outputs.VirtualNetworkRuleResponse]]:
        
        ...
    


@pulumi.output_type
class Permissions(dict):
    
    def __init__(__self__, *, certificates: Optional[Sequence[_builtins.str]] = ..., keys: Optional[Sequence[_builtins.str]] = ..., secrets: Optional[Sequence[_builtins.str]] = ..., storage: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PermissionsResponse(dict):
    
    def __init__(__self__, *, certificates: Optional[Sequence[_builtins.str]] = ..., keys: Optional[Sequence[_builtins.str]] = ..., secrets: Optional[Sequence[_builtins.str]] = ..., storage: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., private_endpoint: Optional[outputs.PrivateEndpointResponse] = ..., private_link_service_connection_state: Optional[outputs.PrivateLinkServiceConnectionStateResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
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
class RotationPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attributes: Optional[outputs.KeyRotationPolicyAttributesResponse] = ..., lifetime_actions: Optional[Sequence[outputs.LifetimeActionResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[outputs.KeyRotationPolicyAttributesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifetimeActions")
    def lifetime_actions(self) -> Optional[Sequence[outputs.LifetimeActionResponse]]:
        
        ...
    


@pulumi.output_type
class SecretAttributesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created: _builtins.int, updated: _builtins.int, enabled: Optional[_builtins.bool] = ..., expires: Optional[_builtins.int] = ..., not_before: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def updated(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expires(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SecretPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secret_uri: _builtins.str, secret_uri_with_version: _builtins.str, attributes: Optional[outputs.SecretAttributesResponse] = ..., content_type: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretUriWithVersion")
    def secret_uri_with_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[outputs.SecretAttributesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, family: _builtins.str, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> _builtins.str:
        
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
class TriggerResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, time_after_create: Optional[_builtins.str] = ..., time_before_expiry: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeAfterCreate")
    def time_after_create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeBeforeExpiry")
    def time_before_expiry(self) -> Optional[_builtins.str]:
        
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
class VaultPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hsm_pool_resource_id: _builtins.str, private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionItemResponse], provisioning_state: _builtins.str, sku: outputs.SkuResponse, tenant_id: _builtins.str, vault_uri: _builtins.str, access_policies: Optional[Sequence[outputs.AccessPolicyEntryResponse]] = ..., enable_purge_protection: Optional[_builtins.bool] = ..., enable_rbac_authorization: Optional[_builtins.bool] = ..., enable_soft_delete: Optional[_builtins.bool] = ..., enabled_for_deployment: Optional[_builtins.bool] = ..., enabled_for_disk_encryption: Optional[_builtins.bool] = ..., enabled_for_template_deployment: Optional[_builtins.bool] = ..., network_acls: Optional[outputs.NetworkRuleSetResponse] = ..., public_network_access: Optional[_builtins.str] = ..., soft_delete_retention_in_days: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmPoolResourceId")
    def hsm_pool_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionItemResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vaultUri")
    def vault_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[Sequence[outputs.AccessPolicyEntryResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePurgeProtection")
    def enable_purge_protection(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRbacAuthorization")
    def enable_rbac_authorization(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSoftDelete")
    def enable_soft_delete(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledForDeployment")
    def enabled_for_deployment(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledForDiskEncryption")
    def enabled_for_disk_encryption(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledForTemplateDeployment")
    def enabled_for_template_deployment(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional[outputs.NetworkRuleSetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionInDays")
    def soft_delete_retention_in_days(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VirtualNetworkRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, ignore_missing_vnet_service_endpoint: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(self) -> Optional[_builtins.bool]:
        
        ...
    


