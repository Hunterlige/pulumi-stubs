import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointResponse",
    "PrivateLinkServiceConnectionStateResponse",
    "ServiceAccessPolicyEntryResponse",
    "ServiceAuthenticationConfigurationInfoResponse",
    "ServiceCorsConfigurationInfoResponse",
    "ServiceCosmosDbConfigurationInfoResponse",
    "ServiceExportConfigurationInfoResponse",
    "ServicesPropertiesResponse",
    "ServicesResourceResponseIdentity",
    "SystemDataResponse",
]

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse,
        provisioning_state: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...,
    ) -> None: ...
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
class ServiceAccessPolicyEntryResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, object_id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceAuthenticationConfigurationInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audience: Optional[_builtins.str] = ...,
        authority: Optional[_builtins.str] = ...,
        smart_proxy_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="smartProxyEnabled")
    def smart_proxy_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ServiceCorsConfigurationInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_credentials: Optional[_builtins.bool] = ...,
        headers: Optional[Sequence[_builtins.str]] = ...,
        max_age: Optional[_builtins.float] = ...,
        methods: Optional[Sequence[_builtins.str]] = ...,
        origins: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def origins(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServiceCosmosDbConfigurationInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_vault_key_uri: Optional[_builtins.str] = ...,
        offer_throughput: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultKeyUri")
    def key_vault_key_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="offerThroughput")
    def offer_throughput(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ServiceExportConfigurationInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, storage_account_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicesPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        access_policies: Optional[
            Sequence[outputs.ServiceAccessPolicyEntryResponse]
        ] = ...,
        authentication_configuration: Optional[
            outputs.ServiceAuthenticationConfigurationInfoResponse
        ] = ...,
        cors_configuration: Optional[
            outputs.ServiceCorsConfigurationInfoResponse
        ] = ...,
        cosmos_db_configuration: Optional[
            outputs.ServiceCosmosDbConfigurationInfoResponse
        ] = ...,
        export_configuration: Optional[
            outputs.ServiceExportConfigurationInfoResponse
        ] = ...,
        private_endpoint_connections: Optional[
            Sequence[outputs.PrivateEndpointConnectionResponse]
        ] = ...,
        public_network_access: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessPolicies")
    def access_policies(
        self,
    ) -> Optional[Sequence[outputs.ServiceAccessPolicyEntryResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> Optional[outputs.ServiceAuthenticationConfigurationInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(
        self,
    ) -> Optional[outputs.ServiceCorsConfigurationInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="cosmosDbConfiguration")
    def cosmos_db_configuration(
        self,
    ) -> Optional[outputs.ServiceCosmosDbConfigurationInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="exportConfiguration")
    def export_configuration(
        self,
    ) -> Optional[outputs.ServiceExportConfigurationInfoResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Optional[Sequence[outputs.PrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServicesResourceResponseIdentity(dict):
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
