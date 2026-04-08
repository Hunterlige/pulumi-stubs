import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CertificatePropertiesResponse",
    "IotDpsPropertiesDescriptionResponse",
    "IotDpsSkuInfoResponse",
    "IotHubDefinitionDescriptionResponse",
    "IpFilterRuleResponse",
    "ManagedServiceIdentityResponse",
    "PrivateEndpointConnectionPropertiesResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointResponse",
    "PrivateLinkServiceConnectionStateResponse",
    ...,
    "SystemDataResponse",
    "UserAssignedIdentityResponse",
]

@pulumi.output_type
class CertificatePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created: _builtins.str,
        expiry: _builtins.str,
        subject: _builtins.str,
        thumbprint: _builtins.str,
        updated: _builtins.str,
        certificate: Optional[_builtins.str] = ...,
        is_verified: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expiry(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def updated(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isVerified")
    def is_verified(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class IotDpsPropertiesDescriptionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        device_provisioning_host_name: _builtins.str,
        id_scope: _builtins.str,
        service_operations_host_name: _builtins.str,
        allocation_policy: Optional[_builtins.str] = ...,
        authorization_policies: Optional[
            Sequence[
                outputs.SharedAccessSignatureAuthorizationRuleAccessRightsDescriptionResponse
            ]
        ] = ...,
        enable_data_residency: Optional[_builtins.bool] = ...,
        iot_hubs: Optional[Sequence[outputs.IotHubDefinitionDescriptionResponse]] = ...,
        ip_filter_rules: Optional[Sequence[outputs.IpFilterRuleResponse]] = ...,
        portal_operations_host_name: Optional[_builtins.str] = ...,
        private_endpoint_connections: Optional[
            Sequence[outputs.PrivateEndpointConnectionResponse]
        ] = ...,
        provisioning_state: Optional[_builtins.str] = ...,
        public_network_access: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceProvisioningHostName")
    def device_provisioning_host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="idScope")
    def id_scope(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceOperationsHostName")
    def service_operations_host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allocationPolicy")
    def allocation_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authorizationPolicies")
    def authorization_policies(
        self,
    ) -> Optional[
        Sequence[
            outputs.SharedAccessSignatureAuthorizationRuleAccessRightsDescriptionResponse
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableDataResidency")
    def enable_data_residency(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="iotHubs")
    def iot_hubs(
        self,
    ) -> Optional[Sequence[outputs.IotHubDefinitionDescriptionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="ipFilterRules")
    def ip_filter_rules(self) -> Optional[Sequence[outputs.IpFilterRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="portalOperationsHostName")
    def portal_operations_host_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Optional[Sequence[outputs.PrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IotDpsSkuInfoResponse(dict):
    def __init__(
        __self__,
        *,
        tier: _builtins.str,
        capacity: Optional[_builtins.float] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IotHubDefinitionDescriptionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_string: _builtins.str,
        location: _builtins.str,
        name: _builtins.str,
        allocation_weight: Optional[_builtins.int] = ...,
        apply_allocation_policy: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allocationWeight")
    def allocation_weight(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="applyAllocationPolicy")
    def apply_allocation_policy(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class IpFilterRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        filter_name: _builtins.str,
        ip_mask: _builtins.str,
        target: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterName")
    def filter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipMask")
    def ip_mask(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.UserAssignedIdentityResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class PrivateEndpointConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse,
        private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> outputs.PrivateLinkServiceConnectionStateResponse: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        properties: outputs.PrivateEndpointConnectionPropertiesResponse,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.PrivateEndpointConnectionPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateEndpointResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        status: _builtins.str,
        actions_required: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SharedAccessSignatureAuthorizationRuleAccessRightsDescriptionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_name: _builtins.str,
        rights: _builtins.str,
        primary_key: Optional[_builtins.str] = ...,
        secondary_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rights(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, client_id: _builtins.str, principal_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
