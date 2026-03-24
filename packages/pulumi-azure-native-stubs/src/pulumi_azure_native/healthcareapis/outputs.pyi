

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
__all__ = ['AnalyticsConnectorDataLakeDataDestinationResponse', 'AnalyticsConnectorFhirServiceDataSourceResponse', 'AnalyticsConnectorFhirToParquetMappingResponse', 'CorsConfigurationResponse', 'DicomServiceAuthenticationConfigurationResponse', 'EncryptionResponse', 'EncryptionResponseCustomerManagedKeyEncryption', 'FhirServiceAcrConfigurationResponse', 'FhirServiceAuthenticationConfigurationResponse', 'FhirServiceCorsConfigurationResponse', 'FhirServiceExportConfigurationResponse', 'FhirServiceImportConfigurationResponse', 'ImplementationGuidesConfigurationResponse', 'IotEventHubIngestionEndpointConfigurationResponse', 'IotMappingPropertiesResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'ResourceVersionPolicyConfigurationResponse', 'ServiceAccessPolicyEntryResponse', 'ServiceAcrConfigurationInfoResponse', 'ServiceAuthenticationConfigurationInfoResponse', 'ServiceCorsConfigurationInfoResponse', 'ServiceCosmosDbConfigurationInfoResponse', 'ServiceExportConfigurationInfoResponse', 'ServiceImportConfigurationInfoResponse', 'ServiceManagedIdentityResponseIdentity', 'ServiceOciArtifactEntryResponse', 'ServicesPropertiesResponse', 'ServicesResourceResponseIdentity', 'SmartIdentityProviderApplicationResponse', 'SmartIdentityProviderConfigurationResponse', 'StorageConfigurationResponse', 'SystemDataResponse', 'UserAssignedIdentityResponse', 'WorkspaceResponseProperties']
@pulumi.output_type
class AnalyticsConnectorDataLakeDataDestinationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_lake_name: _builtins.str, type: _builtins.str, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLakeName")
    def data_lake_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AnalyticsConnectorFhirServiceDataSourceResponse(dict):
    
    def __init__(__self__, *, kind: _builtins.str, type: _builtins.str, url: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AnalyticsConnectorFhirToParquetMappingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, extension_schema_reference: Optional[_builtins.str] = ..., filter_configuration_reference: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionSchemaReference")
    def extension_schema_reference(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterConfigurationReference")
    def filter_configuration_reference(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CorsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_credentials: Optional[_builtins.bool] = ..., headers: Optional[Sequence[_builtins.str]] = ..., max_age: Optional[_builtins.int] = ..., methods: Optional[Sequence[_builtins.str]] = ..., origins: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def origins(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class DicomServiceAuthenticationConfigurationResponse(dict):
    
    def __init__(__self__, *, audiences: Sequence[_builtins.str], authority: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audiences(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authority(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EncryptionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, customer_managed_key_encryption: Optional[outputs.EncryptionResponseCustomerManagedKeyEncryption] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKeyEncryption")
    def customer_managed_key_encryption(self) -> Optional[outputs.EncryptionResponseCustomerManagedKeyEncryption]:
        
        ...
    


@pulumi.output_type
class EncryptionResponseCustomerManagedKeyEncryption(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_encryption_key_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyEncryptionKeyUrl")
    def key_encryption_key_url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FhirServiceAcrConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, login_servers: Optional[Sequence[_builtins.str]] = ..., oci_artifacts: Optional[Sequence[outputs.ServiceOciArtifactEntryResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginServers")
    def login_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociArtifacts")
    def oci_artifacts(self) -> Optional[Sequence[outputs.ServiceOciArtifactEntryResponse]]:
        
        ...
    


@pulumi.output_type
class FhirServiceAuthenticationConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, audience: Optional[_builtins.str] = ..., authority: Optional[_builtins.str] = ..., smart_identity_providers: Optional[Sequence[outputs.SmartIdentityProviderConfigurationResponse]] = ..., smart_proxy_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smartIdentityProviders")
    def smart_identity_providers(self) -> Optional[Sequence[outputs.SmartIdentityProviderConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smartProxyEnabled")
    def smart_proxy_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class FhirServiceCorsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_credentials: Optional[_builtins.bool] = ..., headers: Optional[Sequence[_builtins.str]] = ..., max_age: Optional[_builtins.int] = ..., methods: Optional[Sequence[_builtins.str]] = ..., origins: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def origins(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class FhirServiceExportConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, storage_account_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FhirServiceImportConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., initial_import_mode: Optional[_builtins.bool] = ..., integration_data_store: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialImportMode")
    def initial_import_mode(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationDataStore")
    def integration_data_store(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ImplementationGuidesConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, us_core_missing_data: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usCoreMissingData")
    def us_core_missing_data(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class IotEventHubIngestionEndpointConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, consumer_group: Optional[_builtins.str] = ..., event_hub_name: Optional[_builtins.str] = ..., fully_qualified_event_hub_namespace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedEventHubNamespace")
    def fully_qualified_event_hub_namespace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IotMappingPropertiesResponse(dict):
    
    def __init__(__self__, *, content: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[Any]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse, provisioning_state: _builtins.str, type: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...) -> None:
        
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
class ResourceVersionPolicyConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default: Optional[_builtins.str] = ..., resource_type_overrides: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypeOverrides")
    def resource_type_overrides(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class ServiceAccessPolicyEntryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, object_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServiceAcrConfigurationInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, login_servers: Optional[Sequence[_builtins.str]] = ..., oci_artifacts: Optional[Sequence[outputs.ServiceOciArtifactEntryResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginServers")
    def login_servers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ociArtifacts")
    def oci_artifacts(self) -> Optional[Sequence[outputs.ServiceOciArtifactEntryResponse]]:
        
        ...
    


@pulumi.output_type
class ServiceAuthenticationConfigurationInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, audience: Optional[_builtins.str] = ..., authority: Optional[_builtins.str] = ..., smart_proxy_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smartProxyEnabled")
    def smart_proxy_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ServiceCorsConfigurationInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_credentials: Optional[_builtins.bool] = ..., headers: Optional[Sequence[_builtins.str]] = ..., max_age: Optional[_builtins.int] = ..., methods: Optional[Sequence[_builtins.str]] = ..., origins: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def origins(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ServiceCosmosDbConfigurationInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cross_tenant_cmk_application_id: Optional[_builtins.str] = ..., key_vault_key_uri: Optional[_builtins.str] = ..., offer_throughput: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossTenantCmkApplicationId")
    def cross_tenant_cmk_application_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultKeyUri")
    def key_vault_key_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offerThroughput")
    def offer_throughput(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ServiceExportConfigurationInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, storage_account_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceImportConfigurationInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., initial_import_mode: Optional[_builtins.bool] = ..., integration_data_store: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialImportMode")
    def initial_import_mode(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationDataStore")
    def integration_data_store(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceManagedIdentityResponseIdentity(dict):
    
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
class ServiceOciArtifactEntryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, digest: Optional[_builtins.str] = ..., image_name: Optional[_builtins.str] = ..., login_server: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def digest(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginServer")
    def login_server(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServicesPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, access_policies: Optional[Sequence[outputs.ServiceAccessPolicyEntryResponse]] = ..., acr_configuration: Optional[outputs.ServiceAcrConfigurationInfoResponse] = ..., authentication_configuration: Optional[outputs.ServiceAuthenticationConfigurationInfoResponse] = ..., cors_configuration: Optional[outputs.ServiceCorsConfigurationInfoResponse] = ..., cosmos_db_configuration: Optional[outputs.ServiceCosmosDbConfigurationInfoResponse] = ..., export_configuration: Optional[outputs.ServiceExportConfigurationInfoResponse] = ..., import_configuration: Optional[outputs.ServiceImportConfigurationInfoResponse] = ..., private_endpoint_connections: Optional[Sequence[outputs.PrivateEndpointConnectionResponse]] = ..., public_network_access: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[Sequence[outputs.ServiceAccessPolicyEntryResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acrConfiguration")
    def acr_configuration(self) -> Optional[outputs.ServiceAcrConfigurationInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> Optional[outputs.ServiceAuthenticationConfigurationInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> Optional[outputs.ServiceCorsConfigurationInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cosmosDbConfiguration")
    def cosmos_db_configuration(self) -> Optional[outputs.ServiceCosmosDbConfigurationInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportConfiguration")
    def export_configuration(self) -> Optional[outputs.ServiceExportConfigurationInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importConfiguration")
    def import_configuration(self) -> Optional[outputs.ServiceImportConfigurationInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[Sequence[outputs.PrivateEndpointConnectionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServicesResourceResponseIdentity(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, tenant_id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
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
    


@pulumi.output_type
class SmartIdentityProviderApplicationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_data_actions: Optional[Sequence[_builtins.str]] = ..., audience: Optional[_builtins.str] = ..., client_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedDataActions")
    def allowed_data_actions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SmartIdentityProviderConfigurationResponse(dict):
    
    def __init__(__self__, *, applications: Optional[Sequence[outputs.SmartIdentityProviderApplicationResponse]] = ..., authority: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def applications(self) -> Optional[Sequence[outputs.SmartIdentityProviderApplicationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authority(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class StorageConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, file_system_name: Optional[_builtins.str] = ..., storage_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemName")
    def file_system_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageResourceId")
    def storage_resource_id(self) -> Optional[_builtins.str]:
        
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
class WorkspaceResponseProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionResponse], provisioning_state: _builtins.str, public_network_access: _builtins.str) -> None:
        
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
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> _builtins.str:
        
        ...
    


