import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AcceptedAudiencesResponse",
    "AzureSkuResponse",
    "CalloutPolicyResponse",
    "DatabasePrincipalResponse",
    "DatabaseStatisticsResponse",
    "FollowerDatabaseDefinitionResponse",
    "IdentityResponse",
    "IdentityResponseUserAssignedIdentities",
    "KeyVaultPropertiesResponse",
    "LanguageExtensionResponse",
    "LanguageExtensionsListResponse",
    "MigrationClusterPropertiesResponse",
    "OptimizedAutoscaleResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointPropertyResponse",
    "PrivateLinkServiceConnectionStatePropertyResponse",
    "SuspensionDetailsResponse",
    "SystemDataResponse",
    "TableLevelSharingPropertiesResponse",
    "TrustedExternalTenantResponse",
    "VirtualNetworkConfigurationResponse",
]

@pulumi.output_type
class AcceptedAudiencesResponse(dict):
    def __init__(__self__, *, value: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureSkuResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        tier: _builtins.str,
        capacity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CalloutPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        callout_id: _builtins.str,
        callout_type: Optional[_builtins.str] = ...,
        callout_uri_regex: Optional[_builtins.str] = ...,
        outbound_access: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="calloutId")
    def callout_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="calloutType")
    def callout_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="calloutUriRegex")
    def callout_uri_regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outboundAccess")
    def outbound_access(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatabasePrincipalResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        role: _builtins.str,
        tenant_name: _builtins.str,
        type: _builtins.str,
        app_id: Optional[_builtins.str] = ...,
        email: Optional[_builtins.str] = ...,
        fqn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantName")
    def tenant_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fqn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatabaseStatisticsResponse(dict):
    def __init__(__self__, *, size: Optional[_builtins.float] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class FollowerDatabaseDefinitionResponse(dict):
    def __init__(
        __self__,
        *,
        attached_database_configuration_name: _builtins.str,
        cluster_resource_id: _builtins.str,
        database_name: _builtins.str,
        database_share_origin: _builtins.str,
        table_level_sharing_properties: outputs.TableLevelSharingPropertiesResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attachedDatabaseConfigurationName")
    def attached_database_configuration_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="databaseShareOrigin")
    def database_share_origin(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tableLevelSharingProperties")
    def table_level_sharing_properties(
        self,
    ) -> outputs.TableLevelSharingPropertiesResponse: ...

@pulumi.output_type
class IdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: _builtins.str,
        user_assigned_identities: Optional[
            Mapping[str, outputs.IdentityResponseUserAssignedIdentities]
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
    ) -> Optional[Mapping[str, outputs.IdentityResponseUserAssignedIdentities]]: ...

@pulumi.output_type
class IdentityResponseUserAssignedIdentities(dict):
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

@pulumi.output_type
class KeyVaultPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_name: Optional[_builtins.str] = ...,
        key_vault_uri: Optional[_builtins.str] = ...,
        key_version: Optional[_builtins.str] = ...,
        user_identity: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userIdentity")
    def user_identity(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LanguageExtensionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        language_extension_custom_image_name: Optional[_builtins.str] = ...,
        language_extension_image_name: Optional[_builtins.str] = ...,
        language_extension_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="languageExtensionCustomImageName")
    def language_extension_custom_image_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="languageExtensionImageName")
    def language_extension_image_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="languageExtensionName")
    def language_extension_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LanguageExtensionsListResponse(dict):
    def __init__(
        __self__, *, value: Optional[Sequence[outputs.LanguageExtensionResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.LanguageExtensionResponse]]: ...

@pulumi.output_type
class MigrationClusterPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_ingestion_uri: _builtins.str,
        id: _builtins.str,
        role: _builtins.str,
        uri: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataIngestionUri")
    def data_ingestion_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class OptimizedAutoscaleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_enabled: _builtins.bool,
        maximum: _builtins.int,
        minimum: _builtins.int,
        version: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_id: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        private_endpoint: outputs.PrivateEndpointPropertyResponse,
        private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStatePropertyResponse,
        provisioning_state: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupId")
    def group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> outputs.PrivateEndpointPropertyResponse: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> outputs.PrivateLinkServiceConnectionStatePropertyResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateEndpointPropertyResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateLinkServiceConnectionStatePropertyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions_required: _builtins.str,
        description: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SuspensionDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, suspension_start_date: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="suspensionStartDate")
    def suspension_start_date(self) -> Optional[_builtins.str]: ...

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
class TableLevelSharingPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        external_tables_to_exclude: Optional[Sequence[_builtins.str]] = ...,
        external_tables_to_include: Optional[Sequence[_builtins.str]] = ...,
        functions_to_exclude: Optional[Sequence[_builtins.str]] = ...,
        functions_to_include: Optional[Sequence[_builtins.str]] = ...,
        materialized_views_to_exclude: Optional[Sequence[_builtins.str]] = ...,
        materialized_views_to_include: Optional[Sequence[_builtins.str]] = ...,
        tables_to_exclude: Optional[Sequence[_builtins.str]] = ...,
        tables_to_include: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalTablesToExclude")
    def external_tables_to_exclude(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="externalTablesToInclude")
    def external_tables_to_include(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="functionsToExclude")
    def functions_to_exclude(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="functionsToInclude")
    def functions_to_include(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="materializedViewsToExclude")
    def materialized_views_to_exclude(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="materializedViewsToInclude")
    def materialized_views_to_include(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tablesToExclude")
    def tables_to_exclude(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tablesToInclude")
    def tables_to_include(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class TrustedExternalTenantResponse(dict):
    def __init__(__self__, *, value: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VirtualNetworkConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_management_public_ip_id: _builtins.str,
        engine_public_ip_id: _builtins.str,
        subnet_id: _builtins.str,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataManagementPublicIpId")
    def data_management_public_ip_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enginePublicIpId")
    def engine_public_ip_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
