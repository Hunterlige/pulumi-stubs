import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApiKeyAuthCredentialsResponse",
    "ApiPropertiesResponse",
    "DataConnectorPropertiesResponse",
    "ErrorAdditionalInfoResponse",
    "ErrorDetailResponse",
    "ErrorResponseResponse",
    "IdentityResponse",
    "KeyVaultPropertiesResponse",
    "OAuthClientCredentialsResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointResponse",
    "PrivateLinkServiceConnectionStateResponse",
    "SensorIntegrationResponse",
    "SolutionPropertiesResponse",
    "SystemDataResponse",
]

@pulumi.output_type
class ApiKeyAuthCredentialsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, api_key: outputs.KeyVaultPropertiesResponse, kind: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> outputs.KeyVaultPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...

@pulumi.output_type
class ApiPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, api_freshness_time_in_minutes: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiFreshnessTimeInMinutes")
    def api_freshness_time_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DataConnectorPropertiesResponse(dict):
    def __init__(__self__, *, credentials: Any) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Any: ...

@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    def __init__(__self__, *, info: Any, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def info(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorDetailResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_info: Sequence[outputs.ErrorAdditionalInfoResponse],
        code: _builtins.str,
        details: Sequence[outputs.ErrorDetailResponse],
        message: _builtins.str,
        target: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence[outputs.ErrorAdditionalInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.ErrorDetailResponse]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorResponseResponse(dict):
    def __init__(
        __self__, *, error: Optional[outputs.ErrorDetailResponse] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ErrorDetailResponse]: ...

@pulumi.output_type
class IdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class KeyVaultPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_name: _builtins.str,
        key_vault_uri: _builtins.str,
        key_version: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> _builtins.str: ...

@pulumi.output_type
class OAuthClientCredentialsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        client_secret: outputs.KeyVaultPropertiesResponse,
        kind: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> outputs.KeyVaultPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_ids: Sequence[_builtins.str],
        id: _builtins.str,
        name: _builtins.str,
        private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse,
        provisioning_state: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> outputs.PrivateLinkServiceConnectionStateResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]: ...

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
        actions_required: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SensorIntegrationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        enabled: Optional[_builtins.str] = ...,
        provisioning_info: Optional[outputs.ErrorResponseResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningInfo")
    def provisioning_info(self) -> Optional[outputs.ErrorResponseResponse]: ...

@pulumi.output_type
class SolutionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        marketplace_publisher_id: _builtins.str,
        offer_id: _builtins.str,
        partner_id: _builtins.str,
        plan_id: _builtins.str,
        saas_subscription_id: _builtins.str,
        saas_subscription_name: _builtins.str,
        term_id: _builtins.str,
        role_assignment_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="marketplacePublisherId")
    def marketplace_publisher_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partnerId")
    def partner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="saasSubscriptionId")
    def saas_subscription_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="saasSubscriptionName")
    def saas_subscription_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="termId")
    def term_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleAssignmentId")
    def role_assignment_id(self) -> Optional[_builtins.str]: ...

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
