import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AllowedAudiencesValidationResponse",
    "AllowedPrincipalsResponse",
    "ApiConnectionDefinitionResponseProperties",
    "ApiConnectionTestLinkResponse",
    "ApiOAuthSettingsParameterResponse",
    "ApiOAuthSettingsResponse",
    "ApiReferenceResponse",
    "ApiResourceBackendServiceResponse",
    "ApiResourceDefinitionsResponse",
    "AppLogsConfigurationResponse",
    "AppRegistrationResponse",
    "AppleRegistrationResponse",
    "AppleResponse",
    "ApplicationLogsConfigResponse",
    "ArcConfigurationResponse",
    "ArmIdWrapperResponse",
    "ArmPlanResponse",
    "AseV3NetworkingConfigurationResponse",
    "AuthPlatformResponse",
    "AzureActiveDirectoryLoginResponse",
    "AzureActiveDirectoryRegistrationResponse",
    "AzureActiveDirectoryResponse",
    "AzureActiveDirectoryValidationResponse",
    "AzureBlobStorageApplicationLogsConfigResponse",
    "AzureBlobStorageHttpLogsConfigResponse",
    "AzureResourceErrorInfoResponse",
    "AzureStaticWebAppsRegistrationResponse",
    "AzureStaticWebAppsResponse",
    "AzureStorageInfoValueResponse",
    "AzureTableStorageApplicationLogsConfigResponse",
    "BackupItemResponse",
    "BackupScheduleResponse",
    "BlobStorageTokenStoreResponse",
    "CapabilityResponse",
    "ClientRegistrationResponse",
    "ConnStringValueTypePairResponse",
    "ConnectionErrorResponse",
    "ConnectionGatewayDefinitionResponseProperties",
    "ConnectionGatewayReferenceResponse",
    "ConnectionParameterResponse",
    "ConnectionStatusDefinitionResponse",
    "ConsentLinkDefinitionResponse",
    "ContainerAppsConfigurationResponse",
    "CookieExpirationResponse",
    "CustomApiPropertiesDefinitionResponse",
    "CustomDnsSuffixConfigurationResponse",
    "CustomOpenIdConnectProviderResponse",
    "DaprConfigResponse",
    "DatabaseBackupSettingResponse",
    "DatabaseConnectionOverviewResponse",
    "DefaultAuthorizationPolicyResponse",
    "EnabledConfigResponse",
    "EnvironmentVariableResponse",
    "ErrorEntityResponse",
    "ExpressionResponse",
    "ExpressionRootResponse",
    "ExtendedLocationResponse",
    "FacebookResponse",
    "FileSystemApplicationLogsConfigResponse",
    "FileSystemHttpLogsConfigResponse",
    "FileSystemTokenStoreResponse",
    "ForwardProxyResponse",
    "FrontEndConfigurationResponse",
    "FunctionAppConfigResponse",
    "FunctionsAlwaysReadyConfigResponse",
    "FunctionsDeploymentResponse",
    "FunctionsDeploymentResponseAuthentication",
    "FunctionsDeploymentResponseStorage",
    "FunctionsRuntimeResponse",
    "FunctionsScaleAndConcurrencyResponse",
    "FunctionsScaleAndConcurrencyResponseHttp",
    "FunctionsScaleAndConcurrencyResponseTriggers",
    "GitHubActionCodeConfigurationResponse",
    "GitHubActionConfigurationResponse",
    "GitHubActionContainerConfigurationResponse",
    "GitHubResponse",
    "GlobalValidationResponse",
    "GoogleResponse",
    "HostNameSslStateResponse",
    "HostingEnvironmentProfileResponse",
    "HttpLogsConfigResponse",
    "HttpSettingsResponse",
    "HttpSettingsRoutesResponse",
    "IdentifierResponse",
    "IdentityProvidersResponse",
    "JwtClaimChecksResponse",
    "KubeEnvironmentProfileResponse",
    "LegacyMicrosoftAccountResponse",
    "LogAnalyticsConfigurationResponse",
    "LoginResponse",
    "LoginRoutesResponse",
    "LoginScopesResponse",
    "ManagedServiceIdentityResponse",
    "NameValuePairResponse",
    "NonceResponse",
    "OpenIdConnectClientCredentialResponse",
    "OpenIdConnectConfigResponse",
    "OpenIdConnectLoginResponse",
    "OpenIdConnectRegistrationResponse",
    "OutboundVnetRoutingResponse",
    "PrivateLinkConnectionStateResponse",
    "RemotePrivateEndpointConnectionResponse",
    "ResourceConfigResponse",
    ...,
    "ServerFarmInstanceResponse",
    "SiteDnsConfigResponse",
    "SkuCapacityResponse",
    "SkuDescriptionResponse",
    "SlotSwapStatusResponse",
    "StaticSiteBuildPropertiesResponse",
    ...,
    "StaticSiteLinkedBackendResponse",
    "StaticSiteTemplateOptionsResponse",
    "StaticSiteUserARMResourceResponse",
    "StaticSiteUserProvidedFunctionAppResponse",
    "TokenStoreResponse",
    "TwitterRegistrationResponse",
    "TwitterResponse",
    "UserAssignedIdentityResponse",
    "VirtualNetworkProfileResponse",
    "VnetRouteResponse",
    "VolumeMountResponse",
    "WorkflowEnvelopeResponseProperties",
    "WorkflowHealthResponse",
    "WorkflowTriggerListCallbackUrlQueriesResponse",
    "WsdlDefinitionResponse",
    "WsdlServiceResponse",
]

@pulumi.output_type
class AllowedAudiencesValidationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allowed_audiences: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AllowedPrincipalsResponse(dict):
    def __init__(
        __self__,
        *,
        groups: Optional[Sequence[_builtins.str]] = ...,
        identities: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ApiConnectionDefinitionResponseProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api: Optional[outputs.ApiReferenceResponse] = ...,
        changed_time: Optional[_builtins.str] = ...,
        created_time: Optional[_builtins.str] = ...,
        custom_parameter_values: Optional[Mapping[str, _builtins.str]] = ...,
        display_name: Optional[_builtins.str] = ...,
        non_secret_parameter_values: Optional[Mapping[str, _builtins.str]] = ...,
        parameter_values: Optional[Mapping[str, _builtins.str]] = ...,
        statuses: Optional[Sequence[outputs.ConnectionStatusDefinitionResponse]] = ...,
        test_links: Optional[Sequence[outputs.ApiConnectionTestLinkResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def api(self) -> Optional[outputs.ApiReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customParameterValues")
    def custom_parameter_values(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nonSecretParameterValues")
    def non_secret_parameter_values(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="parameterValues")
    def parameter_values(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[Sequence[outputs.ConnectionStatusDefinitionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="testLinks")
    def test_links(
        self,
    ) -> Optional[Sequence[outputs.ApiConnectionTestLinkResponse]]: ...

@pulumi.output_type
class ApiConnectionTestLinkResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        method: Optional[_builtins.str] = ...,
        request_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestUri")
    def request_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApiOAuthSettingsParameterResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        options: Optional[Any] = ...,
        ui_definition: Optional[Any] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="uiDefinition")
    def ui_definition(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApiOAuthSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        custom_parameters: Optional[
            Mapping[str, outputs.ApiOAuthSettingsParameterResponse]
        ] = ...,
        identity_provider: Optional[_builtins.str] = ...,
        properties: Optional[Any] = ...,
        redirect_url: Optional[_builtins.str] = ...,
        scopes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customParameters")
    def custom_parameters(
        self,
    ) -> Optional[Mapping[str, outputs.ApiOAuthSettingsParameterResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="identityProvider")
    def identity_provider(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="redirectUrl")
    def redirect_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ApiReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        brand_color: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        icon_uri: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        swagger: Optional[Any] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="brandColor")
    def brand_color(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iconUri")
    def icon_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def swagger(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApiResourceBackendServiceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, service_url: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceUrl")
    def service_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApiResourceDefinitionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        modified_swagger_url: Optional[_builtins.str] = ...,
        original_swagger_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modifiedSwaggerUrl")
    def modified_swagger_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="originalSwaggerUrl")
    def original_swagger_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppLogsConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: Optional[_builtins.str] = ...,
        log_analytics_configuration: Optional[
            outputs.LogAnalyticsConfigurationResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logAnalyticsConfiguration")
    def log_analytics_configuration(
        self,
    ) -> Optional[outputs.LogAnalyticsConfigurationResponse]: ...

@pulumi.output_type
class AppRegistrationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_id: Optional[_builtins.str] = ...,
        app_secret_setting_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appSecretSettingName")
    def app_secret_setting_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppleRegistrationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        client_secret_setting_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppleResponse(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        login: Optional[outputs.LoginScopesResponse] = ...,
        registration: Optional[outputs.AppleRegistrationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.LoginScopesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.AppleRegistrationResponse]: ...

@pulumi.output_type
class ApplicationLogsConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_blob_storage: Optional[
            outputs.AzureBlobStorageApplicationLogsConfigResponse
        ] = ...,
        azure_table_storage: Optional[
            outputs.AzureTableStorageApplicationLogsConfigResponse
        ] = ...,
        file_system: Optional[outputs.FileSystemApplicationLogsConfigResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureBlobStorage")
    def azure_blob_storage(
        self,
    ) -> Optional[outputs.AzureBlobStorageApplicationLogsConfigResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureTableStorage")
    def azure_table_storage(
        self,
    ) -> Optional[outputs.AzureTableStorageApplicationLogsConfigResponse]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystem")
    def file_system(
        self,
    ) -> Optional[outputs.FileSystemApplicationLogsConfigResponse]: ...

@pulumi.output_type
class ArcConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        artifact_storage_access_mode: Optional[_builtins.str] = ...,
        artifact_storage_class_name: Optional[_builtins.str] = ...,
        artifact_storage_mount_path: Optional[_builtins.str] = ...,
        artifact_storage_node_name: Optional[_builtins.str] = ...,
        artifacts_storage_type: Optional[_builtins.str] = ...,
        front_end_service_configuration: Optional[
            outputs.FrontEndConfigurationResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactStorageAccessMode")
    def artifact_storage_access_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="artifactStorageClassName")
    def artifact_storage_class_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="artifactStorageMountPath")
    def artifact_storage_mount_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="artifactStorageNodeName")
    def artifact_storage_node_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="artifactsStorageType")
    def artifacts_storage_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="frontEndServiceConfiguration")
    def front_end_service_configuration(
        self,
    ) -> Optional[outputs.FrontEndConfigurationResponse]: ...

@pulumi.output_type
class ArmIdWrapperResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class ArmPlanResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        product: Optional[_builtins.str] = ...,
        promotion_code: Optional[_builtins.str] = ...,
        publisher: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def product(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AseV3NetworkingConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        external_inbound_ip_addresses: Sequence[_builtins.str],
        id: _builtins.str,
        internal_inbound_ip_addresses: Sequence[_builtins.str],
        linux_outbound_ip_addresses: Sequence[_builtins.str],
        name: _builtins.str,
        type: _builtins.str,
        windows_outbound_ip_addresses: Sequence[_builtins.str],
        allow_new_private_endpoint_connections: Optional[_builtins.bool] = ...,
        ftp_enabled: Optional[_builtins.bool] = ...,
        inbound_ip_address_override: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
        remote_debug_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalInboundIpAddresses")
    def external_inbound_ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="internalInboundIpAddresses")
    def internal_inbound_ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linuxOutboundIpAddresses")
    def linux_outbound_ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="windowsOutboundIpAddresses")
    def windows_outbound_ip_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowNewPrivateEndpointConnections")
    def allow_new_private_endpoint_connections(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ftpEnabled")
    def ftp_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="inboundIpAddressOverride")
    def inbound_ip_address_override(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remoteDebugEnabled")
    def remote_debug_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AuthPlatformResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        config_file_path: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
        runtime_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configFilePath")
    def config_file_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureActiveDirectoryLoginResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_www_authenticate: Optional[_builtins.bool] = ...,
        login_parameters: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableWWWAuthenticate")
    def disable_www_authenticate(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="loginParameters")
    def login_parameters(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AzureActiveDirectoryRegistrationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        client_secret_certificate_issuer: Optional[_builtins.str] = ...,
        client_secret_certificate_subject_alternative_name: Optional[
            _builtins.str
        ] = ...,
        client_secret_certificate_thumbprint: Optional[_builtins.str] = ...,
        client_secret_setting_name: Optional[_builtins.str] = ...,
        open_id_issuer: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretCertificateIssuer")
    def client_secret_certificate_issuer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretCertificateSubjectAlternativeName")
    def client_secret_certificate_subject_alternative_name(
        self,
    ) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretCertificateThumbprint")
    def client_secret_certificate_thumbprint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="openIdIssuer")
    def open_id_issuer(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureActiveDirectoryResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        is_auto_provisioned: Optional[_builtins.bool] = ...,
        login: Optional[outputs.AzureActiveDirectoryLoginResponse] = ...,
        registration: Optional[outputs.AzureActiveDirectoryRegistrationResponse] = ...,
        validation: Optional[outputs.AzureActiveDirectoryValidationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isAutoProvisioned")
    def is_auto_provisioned(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.AzureActiveDirectoryLoginResponse]: ...
    @_builtins.property
    @pulumi.getter
    def registration(
        self,
    ) -> Optional[outputs.AzureActiveDirectoryRegistrationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def validation(
        self,
    ) -> Optional[outputs.AzureActiveDirectoryValidationResponse]: ...

@pulumi.output_type
class AzureActiveDirectoryValidationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_audiences: Optional[Sequence[_builtins.str]] = ...,
        default_authorization_policy: Optional[
            outputs.DefaultAuthorizationPolicyResponse
        ] = ...,
        jwt_claim_checks: Optional[outputs.JwtClaimChecksResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultAuthorizationPolicy")
    def default_authorization_policy(
        self,
    ) -> Optional[outputs.DefaultAuthorizationPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="jwtClaimChecks")
    def jwt_claim_checks(self) -> Optional[outputs.JwtClaimChecksResponse]: ...

@pulumi.output_type
class AzureBlobStorageApplicationLogsConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        level: Optional[_builtins.str] = ...,
        retention_in_days: Optional[_builtins.int] = ...,
        sas_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sasUrl")
    def sas_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureBlobStorageHttpLogsConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        retention_in_days: Optional[_builtins.int] = ...,
        sas_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="sasUrl")
    def sas_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureResourceErrorInfoResponse(dict):
    def __init__(
        __self__,
        *,
        code: _builtins.str,
        message: _builtins.str,
        details: Optional[Sequence[outputs.AzureResourceErrorInfoResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[outputs.AzureResourceErrorInfoResponse]]: ...

@pulumi.output_type
class AzureStaticWebAppsRegistrationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureStaticWebAppsResponse(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        registration: Optional[outputs.AzureStaticWebAppsRegistrationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def registration(
        self,
    ) -> Optional[outputs.AzureStaticWebAppsRegistrationResponse]: ...

@pulumi.output_type
class AzureStorageInfoValueResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        state: _builtins.str,
        access_key: Optional[_builtins.str] = ...,
        account_name: Optional[_builtins.str] = ...,
        mount_path: Optional[_builtins.str] = ...,
        protocol: Optional[_builtins.str] = ...,
        share_name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureTableStorageApplicationLogsConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, sas_url: _builtins.str, level: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sasUrl")
    def sas_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BackupItemResponse(dict):
    def __init__(
        __self__,
        *,
        backup_id: _builtins.int,
        blob_name: _builtins.str,
        correlation_id: _builtins.str,
        created: _builtins.str,
        databases: Sequence[outputs.DatabaseBackupSettingResponse],
        finished_time_stamp: _builtins.str,
        id: _builtins.str,
        last_restore_time_stamp: _builtins.str,
        log: _builtins.str,
        name: _builtins.str,
        scheduled: _builtins.bool,
        size_in_bytes: _builtins.float,
        status: _builtins.str,
        storage_account_url: _builtins.str,
        type: _builtins.str,
        website_size_in_bytes: _builtins.float,
        kind: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="blobName")
    def blob_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def created(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Sequence[outputs.DatabaseBackupSettingResponse]: ...
    @_builtins.property
    @pulumi.getter(name="finishedTimeStamp")
    def finished_time_stamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastRestoreTimeStamp")
    def last_restore_time_stamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def log(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scheduled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountUrl")
    def storage_account_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="websiteSizeInBytes")
    def website_size_in_bytes(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BackupScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        frequency_interval: Optional[_builtins.int] = ...,
        frequency_unit: Optional[_builtins.str] = ...,
        keep_at_least_one_backup: Optional[_builtins.bool] = ...,
        last_execution_time: _builtins.str,
        retention_period_in_days: Optional[_builtins.int] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="frequencyInterval")
    def frequency_interval(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="frequencyUnit")
    def frequency_unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keepAtLeastOneBackup")
    def keep_at_least_one_backup(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="lastExecutionTime")
    def last_execution_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriodInDays")
    def retention_period_in_days(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BlobStorageTokenStoreResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, sas_url_setting_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sasUrlSettingName")
    def sas_url_setting_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CapabilityResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        reason: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClientRegistrationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: Optional[_builtins.str] = ...,
        client_secret_setting_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnStringValueTypePairResponse(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionErrorResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        type: _builtins.str,
        code: Optional[_builtins.str] = ...,
        etag: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ConnectionGatewayDefinitionResponseProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        backend_uri: Optional[_builtins.str] = ...,
        connection_gateway_installation: Optional[
            outputs.ConnectionGatewayReferenceResponse
        ] = ...,
        contact_information: Optional[Sequence[_builtins.str]] = ...,
        description: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        machine_name: Optional[_builtins.str] = ...,
        status: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendUri")
    def backend_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionGatewayInstallation")
    def connection_gateway_installation(
        self,
    ) -> Optional[outputs.ConnectionGatewayReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="contactInformation")
    def contact_information(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[Any]: ...

@pulumi.output_type
class ConnectionGatewayReferenceResponse(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionParameterResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        o_auth_settings: Optional[outputs.ApiOAuthSettingsResponse] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oAuthSettings")
    def o_auth_settings(self) -> Optional[outputs.ApiOAuthSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionStatusDefinitionResponse(dict):
    def __init__(
        __self__,
        *,
        error: Optional[outputs.ConnectionErrorResponse] = ...,
        status: Optional[_builtins.str] = ...,
        target: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ConnectionErrorResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConsentLinkDefinitionResponse(dict):
    def __init__(
        __self__,
        *,
        display_name: Optional[_builtins.str] = ...,
        first_party_login_uri: Optional[_builtins.str] = ...,
        link: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstPartyLoginUri")
    def first_party_login_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ContainerAppsConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_subnet_resource_id: Optional[_builtins.str] = ...,
        control_plane_subnet_resource_id: Optional[_builtins.str] = ...,
        dapr_ai_instrumentation_key: Optional[_builtins.str] = ...,
        docker_bridge_cidr: Optional[_builtins.str] = ...,
        platform_reserved_cidr: Optional[_builtins.str] = ...,
        platform_reserved_dns_ip: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appSubnetResourceId")
    def app_subnet_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="controlPlaneSubnetResourceId")
    def control_plane_subnet_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="daprAIInstrumentationKey")
    def dapr_ai_instrumentation_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dockerBridgeCidr")
    def docker_bridge_cidr(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformReservedCidr")
    def platform_reserved_cidr(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformReservedDnsIP")
    def platform_reserved_dns_ip(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CookieExpirationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        convention: Optional[_builtins.str] = ...,
        time_to_expiration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def convention(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeToExpiration")
    def time_to_expiration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomApiPropertiesDefinitionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_definitions: Optional[outputs.ApiResourceDefinitionsResponse] = ...,
        api_type: Optional[_builtins.str] = ...,
        backend_service: Optional[outputs.ApiResourceBackendServiceResponse] = ...,
        brand_color: Optional[_builtins.str] = ...,
        capabilities: Optional[Sequence[_builtins.str]] = ...,
        connection_parameters: Optional[
            Mapping[str, outputs.ConnectionParameterResponse]
        ] = ...,
        description: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        icon_uri: Optional[_builtins.str] = ...,
        runtime_urls: Optional[Sequence[_builtins.str]] = ...,
        swagger: Optional[Any] = ...,
        wsdl_definition: Optional[outputs.WsdlDefinitionResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiDefinitions")
    def api_definitions(self) -> Optional[outputs.ApiResourceDefinitionsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="apiType")
    def api_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backendService")
    def backend_service(
        self,
    ) -> Optional[outputs.ApiResourceBackendServiceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="brandColor")
    def brand_color(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionParameters")
    def connection_parameters(
        self,
    ) -> Optional[Mapping[str, outputs.ConnectionParameterResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iconUri")
    def icon_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeUrls")
    def runtime_urls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def swagger(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="wsdlDefinition")
    def wsdl_definition(self) -> Optional[outputs.WsdlDefinitionResponse]: ...

@pulumi.output_type
class CustomDnsSuffixConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        provisioning_details: _builtins.str,
        provisioning_state: _builtins.str,
        type: _builtins.str,
        certificate_url: Optional[_builtins.str] = ...,
        dns_suffix: Optional[_builtins.str] = ...,
        key_vault_reference_identity: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningDetails")
    def provisioning_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultReferenceIdentity")
    def key_vault_reference_identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CustomOpenIdConnectProviderResponse(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        login: Optional[outputs.OpenIdConnectLoginResponse] = ...,
        registration: Optional[outputs.OpenIdConnectRegistrationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.OpenIdConnectLoginResponse]: ...
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.OpenIdConnectRegistrationResponse]: ...

@pulumi.output_type
class DaprConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_id: Optional[_builtins.str] = ...,
        app_port: Optional[_builtins.int] = ...,
        enable_api_logging: Optional[_builtins.bool] = ...,
        enabled: Optional[_builtins.bool] = ...,
        http_max_request_size: Optional[_builtins.int] = ...,
        http_read_buffer_size: Optional[_builtins.int] = ...,
        log_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appPort")
    def app_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="enableApiLogging")
    def enable_api_logging(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="httpMaxRequestSize")
    def http_max_request_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="httpReadBufferSize")
    def http_read_buffer_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatabaseBackupSettingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_type: _builtins.str,
        connection_string: Optional[_builtins.str] = ...,
        connection_string_name: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionStringName")
    def connection_string_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatabaseConnectionOverviewResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        configuration_files: Sequence[
            outputs.StaticSiteDatabaseConnectionConfigurationFileOverviewResponse
        ],
        connection_identity: _builtins.str,
        name: _builtins.str,
        region: _builtins.str,
        resource_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationFiles")
    def configuration_files(
        self,
    ) -> Sequence[
        outputs.StaticSiteDatabaseConnectionConfigurationFileOverviewResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="connectionIdentity")
    def connection_identity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> _builtins.str: ...

@pulumi.output_type
class DefaultAuthorizationPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_applications: Optional[Sequence[_builtins.str]] = ...,
        allowed_principals: Optional[outputs.AllowedPrincipalsResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedApplications")
    def allowed_applications(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedPrincipals")
    def allowed_principals(self) -> Optional[outputs.AllowedPrincipalsResponse]: ...

@pulumi.output_type
class EnabledConfigResponse(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class EnvironmentVariableResponse(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class ErrorEntityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        details: Optional[Sequence[outputs.ErrorEntityResponse]] = ...,
        extended_code: Optional[_builtins.str] = ...,
        inner_errors: Optional[Sequence[outputs.ErrorEntityResponse]] = ...,
        message: Optional[_builtins.str] = ...,
        message_template: Optional[_builtins.str] = ...,
        parameters: Optional[Sequence[_builtins.str]] = ...,
        target: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[outputs.ErrorEntityResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="extendedCode")
    def extended_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="innerErrors")
    def inner_errors(self) -> Optional[Sequence[outputs.ErrorEntityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="messageTemplate")
    def message_template(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExpressionResponse(dict):
    def __init__(
        __self__,
        *,
        error: Optional[outputs.AzureResourceErrorInfoResponse] = ...,
        subexpressions: Optional[Sequence[outputs.ExpressionResponse]] = ...,
        text: Optional[_builtins.str] = ...,
        value: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.AzureResourceErrorInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def subexpressions(self) -> Optional[Sequence[outputs.ExpressionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]: ...

@pulumi.output_type
class ExpressionRootResponse(dict):
    def __init__(
        __self__,
        *,
        error: Optional[outputs.AzureResourceErrorInfoResponse] = ...,
        path: Optional[_builtins.str] = ...,
        subexpressions: Optional[Sequence[outputs.ExpressionResponse]] = ...,
        text: Optional[_builtins.str] = ...,
        value: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.AzureResourceErrorInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subexpressions(self) -> Optional[Sequence[outputs.ExpressionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]: ...

@pulumi.output_type
class ExtendedLocationResponse(dict):
    def __init__(
        __self__, *, type: _builtins.str, name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FacebookResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        graph_api_version: Optional[_builtins.str] = ...,
        login: Optional[outputs.LoginScopesResponse] = ...,
        registration: Optional[outputs.AppRegistrationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="graphApiVersion")
    def graph_api_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.LoginScopesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.AppRegistrationResponse]: ...

@pulumi.output_type
class FileSystemApplicationLogsConfigResponse(dict):
    def __init__(__self__, *, level: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FileSystemHttpLogsConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        retention_in_days: Optional[_builtins.int] = ...,
        retention_in_mb: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="retentionInMb")
    def retention_in_mb(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FileSystemTokenStoreResponse(dict):
    def __init__(__self__, *, directory: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def directory(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ForwardProxyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        convention: Optional[_builtins.str] = ...,
        custom_host_header_name: Optional[_builtins.str] = ...,
        custom_proto_header_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def convention(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customHostHeaderName")
    def custom_host_header_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customProtoHeaderName")
    def custom_proto_header_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FrontEndConfigurationResponse(dict):
    def __init__(__self__, *, kind: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FunctionAppConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deployment: Optional[outputs.FunctionsDeploymentResponse] = ...,
        runtime: Optional[outputs.FunctionsRuntimeResponse] = ...,
        scale_and_concurrency: Optional[
            outputs.FunctionsScaleAndConcurrencyResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> Optional[outputs.FunctionsDeploymentResponse]: ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[outputs.FunctionsRuntimeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="scaleAndConcurrency")
    def scale_and_concurrency(
        self,
    ) -> Optional[outputs.FunctionsScaleAndConcurrencyResponse]: ...

@pulumi.output_type
class FunctionsAlwaysReadyConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_count: Optional[_builtins.int] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FunctionsDeploymentResponse(dict):
    def __init__(
        __self__, *, storage: Optional[outputs.FunctionsDeploymentResponseStorage] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[outputs.FunctionsDeploymentResponseStorage]: ...

@pulumi.output_type
class FunctionsDeploymentResponseAuthentication(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        storage_account_connection_string_name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
        user_assigned_identity_resource_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountConnectionStringName")
    def storage_account_connection_string_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FunctionsDeploymentResponseStorage(dict):
    def __init__(
        __self__,
        *,
        authentication: Optional[
            outputs.FunctionsDeploymentResponseAuthentication
        ] = ...,
        type: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authentication(
        self,
    ) -> Optional[outputs.FunctionsDeploymentResponseAuthentication]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FunctionsRuntimeResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FunctionsScaleAndConcurrencyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        always_ready: Optional[
            Sequence[outputs.FunctionsAlwaysReadyConfigResponse]
        ] = ...,
        instance_memory_mb: Optional[_builtins.int] = ...,
        maximum_instance_count: Optional[_builtins.int] = ...,
        triggers: Optional[outputs.FunctionsScaleAndConcurrencyResponseTriggers] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alwaysReady")
    def always_ready(
        self,
    ) -> Optional[Sequence[outputs.FunctionsAlwaysReadyConfigResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceMemoryMB")
    def instance_memory_mb(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maximumInstanceCount")
    def maximum_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def triggers(
        self,
    ) -> Optional[outputs.FunctionsScaleAndConcurrencyResponseTriggers]: ...

@pulumi.output_type
class FunctionsScaleAndConcurrencyResponseHttp(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, per_instance_concurrency: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="perInstanceConcurrency")
    def per_instance_concurrency(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FunctionsScaleAndConcurrencyResponseTriggers(dict):
    def __init__(
        __self__,
        *,
        http: Optional[outputs.FunctionsScaleAndConcurrencyResponseHttp] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def http(self) -> Optional[outputs.FunctionsScaleAndConcurrencyResponseHttp]: ...

@pulumi.output_type
class GitHubActionCodeConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        runtime_stack: Optional[_builtins.str] = ...,
        runtime_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="runtimeStack")
    def runtime_stack(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GitHubActionConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        code_configuration: Optional[
            outputs.GitHubActionCodeConfigurationResponse
        ] = ...,
        container_configuration: Optional[
            outputs.GitHubActionContainerConfigurationResponse
        ] = ...,
        generate_workflow_file: Optional[_builtins.bool] = ...,
        is_linux: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codeConfiguration")
    def code_configuration(
        self,
    ) -> Optional[outputs.GitHubActionCodeConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="containerConfiguration")
    def container_configuration(
        self,
    ) -> Optional[outputs.GitHubActionContainerConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="generateWorkflowFile")
    def generate_workflow_file(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isLinux")
    def is_linux(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class GitHubActionContainerConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_name: Optional[_builtins.str] = ...,
        password: Optional[_builtins.str] = ...,
        server_url: Optional[_builtins.str] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverUrl")
    def server_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GitHubResponse(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        login: Optional[outputs.LoginScopesResponse] = ...,
        registration: Optional[outputs.ClientRegistrationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.LoginScopesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.ClientRegistrationResponse]: ...

@pulumi.output_type
class GlobalValidationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        excluded_paths: Optional[Sequence[_builtins.str]] = ...,
        redirect_to_provider: Optional[_builtins.str] = ...,
        require_authentication: Optional[_builtins.bool] = ...,
        unauthenticated_client_action: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="excludedPaths")
    def excluded_paths(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="redirectToProvider")
    def redirect_to_provider(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requireAuthentication")
    def require_authentication(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="unauthenticatedClientAction")
    def unauthenticated_client_action(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GoogleResponse(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        login: Optional[outputs.LoginScopesResponse] = ...,
        registration: Optional[outputs.ClientRegistrationResponse] = ...,
        validation: Optional[outputs.AllowedAudiencesValidationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.LoginScopesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.ClientRegistrationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def validation(self) -> Optional[outputs.AllowedAudiencesValidationResponse]: ...

@pulumi.output_type
class HostNameSslStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_type: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        ssl_state: Optional[_builtins.str] = ...,
        thumbprint: Optional[_builtins.str] = ...,
        to_update: Optional[_builtins.bool] = ...,
        virtual_ip: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostType")
    def host_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslState")
    def ssl_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="toUpdate")
    def to_update(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="virtualIP")
    def virtual_ip(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HostingEnvironmentProfileResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class HttpLogsConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_blob_storage: Optional[
            outputs.AzureBlobStorageHttpLogsConfigResponse
        ] = ...,
        file_system: Optional[outputs.FileSystemHttpLogsConfigResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureBlobStorage")
    def azure_blob_storage(
        self,
    ) -> Optional[outputs.AzureBlobStorageHttpLogsConfigResponse]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystem")
    def file_system(self) -> Optional[outputs.FileSystemHttpLogsConfigResponse]: ...

@pulumi.output_type
class HttpSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        forward_proxy: Optional[outputs.ForwardProxyResponse] = ...,
        require_https: Optional[_builtins.bool] = ...,
        routes: Optional[outputs.HttpSettingsRoutesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="forwardProxy")
    def forward_proxy(self) -> Optional[outputs.ForwardProxyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="requireHttps")
    def require_https(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[outputs.HttpSettingsRoutesResponse]: ...

@pulumi.output_type
class HttpSettingsRoutesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, api_prefix: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiPrefix")
    def api_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IdentifierResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        type: _builtins.str,
        kind: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IdentityProvidersResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        apple: Optional[outputs.AppleResponse] = ...,
        azure_active_directory: Optional[outputs.AzureActiveDirectoryResponse] = ...,
        azure_static_web_apps: Optional[outputs.AzureStaticWebAppsResponse] = ...,
        custom_open_id_connect_providers: Optional[
            Mapping[str, outputs.CustomOpenIdConnectProviderResponse]
        ] = ...,
        facebook: Optional[outputs.FacebookResponse] = ...,
        git_hub: Optional[outputs.GitHubResponse] = ...,
        google: Optional[outputs.GoogleResponse] = ...,
        legacy_microsoft_account: Optional[
            outputs.LegacyMicrosoftAccountResponse
        ] = ...,
        twitter: Optional[outputs.TwitterResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def apple(self) -> Optional[outputs.AppleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureActiveDirectory")
    def azure_active_directory(
        self,
    ) -> Optional[outputs.AzureActiveDirectoryResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureStaticWebApps")
    def azure_static_web_apps(self) -> Optional[outputs.AzureStaticWebAppsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="customOpenIdConnectProviders")
    def custom_open_id_connect_providers(
        self,
    ) -> Optional[Mapping[str, outputs.CustomOpenIdConnectProviderResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def facebook(self) -> Optional[outputs.FacebookResponse]: ...
    @_builtins.property
    @pulumi.getter(name="gitHub")
    def git_hub(self) -> Optional[outputs.GitHubResponse]: ...
    @_builtins.property
    @pulumi.getter
    def google(self) -> Optional[outputs.GoogleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="legacyMicrosoftAccount")
    def legacy_microsoft_account(
        self,
    ) -> Optional[outputs.LegacyMicrosoftAccountResponse]: ...
    @_builtins.property
    @pulumi.getter
    def twitter(self) -> Optional[outputs.TwitterResponse]: ...

@pulumi.output_type
class JwtClaimChecksResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_client_applications: Optional[Sequence[_builtins.str]] = ...,
        allowed_groups: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedClientApplications")
    def allowed_client_applications(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedGroups")
    def allowed_groups(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class KubeEnvironmentProfileResponse(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        type: _builtins.str,
        id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LegacyMicrosoftAccountResponse(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        login: Optional[outputs.LoginScopesResponse] = ...,
        registration: Optional[outputs.ClientRegistrationResponse] = ...,
        validation: Optional[outputs.AllowedAudiencesValidationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.LoginScopesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.ClientRegistrationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def validation(self) -> Optional[outputs.AllowedAudiencesValidationResponse]: ...

@pulumi.output_type
class LogAnalyticsConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, customer_id: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LoginResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_external_redirect_urls: Optional[Sequence[_builtins.str]] = ...,
        cookie_expiration: Optional[outputs.CookieExpirationResponse] = ...,
        nonce: Optional[outputs.NonceResponse] = ...,
        preserve_url_fragments_for_logins: Optional[_builtins.bool] = ...,
        routes: Optional[outputs.LoginRoutesResponse] = ...,
        token_store: Optional[outputs.TokenStoreResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedExternalRedirectUrls")
    def allowed_external_redirect_urls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cookieExpiration")
    def cookie_expiration(self) -> Optional[outputs.CookieExpirationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def nonce(self) -> Optional[outputs.NonceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="preserveUrlFragmentsForLogins")
    def preserve_url_fragments_for_logins(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[outputs.LoginRoutesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="tokenStore")
    def token_store(self) -> Optional[outputs.TokenStoreResponse]: ...

@pulumi.output_type
class LoginRoutesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, logout_endpoint: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logoutEndpoint")
    def logout_endpoint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LoginScopesResponse(dict):
    def __init__(
        __self__, *, scopes: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
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
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[Mapping[str, outputs.UserAssignedIdentityResponse]]: ...

@pulumi.output_type
class NameValuePairResponse(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NonceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        nonce_expiration_interval: Optional[_builtins.str] = ...,
        validate_nonce: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nonceExpirationInterval")
    def nonce_expiration_interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="validateNonce")
    def validate_nonce(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class OpenIdConnectClientCredentialResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_secret_setting_name: Optional[_builtins.str] = ...,
        method: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OpenIdConnectConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_endpoint: Optional[_builtins.str] = ...,
        certification_uri: Optional[_builtins.str] = ...,
        issuer: Optional[_builtins.str] = ...,
        token_endpoint: Optional[_builtins.str] = ...,
        well_known_open_id_configuration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificationUri")
    def certification_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="wellKnownOpenIdConfiguration")
    def well_known_open_id_configuration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OpenIdConnectLoginResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name_claim_type: Optional[_builtins.str] = ...,
        scopes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nameClaimType")
    def name_claim_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class OpenIdConnectRegistrationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_credential: Optional[
            outputs.OpenIdConnectClientCredentialResponse
        ] = ...,
        client_id: Optional[_builtins.str] = ...,
        open_id_connect_configuration: Optional[
            outputs.OpenIdConnectConfigResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientCredential")
    def client_credential(
        self,
    ) -> Optional[outputs.OpenIdConnectClientCredentialResponse]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="openIdConnectConfiguration")
    def open_id_connect_configuration(
        self,
    ) -> Optional[outputs.OpenIdConnectConfigResponse]: ...

@pulumi.output_type
class OutboundVnetRoutingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        all_traffic: Optional[_builtins.bool] = ...,
        application_traffic: Optional[_builtins.bool] = ...,
        backup_restore_traffic: Optional[_builtins.bool] = ...,
        content_share_traffic: Optional[_builtins.bool] = ...,
        image_pull_traffic: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allTraffic")
    def all_traffic(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="applicationTraffic")
    def application_traffic(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="backupRestoreTraffic")
    def backup_restore_traffic(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="contentShareTraffic")
    def content_share_traffic(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="imagePullTraffic")
    def image_pull_traffic(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class PrivateLinkConnectionStateResponse(dict):
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
class RemotePrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        provisioning_state: _builtins.str,
        type: _builtins.str,
        ip_addresses: Optional[Sequence[_builtins.str]] = ...,
        kind: Optional[_builtins.str] = ...,
        private_endpoint: Optional[outputs.ArmIdWrapperResponse] = ...,
        private_link_service_connection_state: Optional[
            outputs.PrivateLinkConnectionStateResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.ArmIdWrapperResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[outputs.PrivateLinkConnectionStateResponse]: ...

@pulumi.output_type
class ResourceConfigResponse(dict):
    def __init__(
        __self__,
        *,
        cpu: Optional[_builtins.float] = ...,
        memory: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResponseMessageEnvelopeRemotePrivateEndpointConnectionResponse(dict):
    def __init__(
        __self__,
        *,
        error: Optional[outputs.ErrorEntityResponse] = ...,
        id: Optional[_builtins.str] = ...,
        identity: Optional[outputs.ManagedServiceIdentityResponse] = ...,
        location: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        plan: Optional[outputs.ArmPlanResponse] = ...,
        properties: Optional[outputs.RemotePrivateEndpointConnectionResponse] = ...,
        sku: Optional[outputs.SkuDescriptionResponse] = ...,
        status: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
        type: Optional[_builtins.str] = ...,
        zones: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ErrorEntityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[outputs.ArmPlanResponse]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[outputs.RemotePrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ServerFarmInstanceResponse(dict):
    def __init__(
        __self__,
        *,
        instance_name: Optional[_builtins.str] = ...,
        ip_address: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SiteDnsConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dns_legacy_sort_order: _builtins.bool,
        dns_alt_server: Optional[_builtins.str] = ...,
        dns_max_cache_timeout: Optional[_builtins.int] = ...,
        dns_retry_attempt_count: Optional[_builtins.int] = ...,
        dns_retry_attempt_timeout: Optional[_builtins.int] = ...,
        dns_servers: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dnsLegacySortOrder")
    def dns_legacy_sort_order(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="dnsAltServer")
    def dns_alt_server(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsMaxCacheTimeout")
    def dns_max_cache_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dnsRetryAttemptCount")
    def dns_retry_attempt_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dnsRetryAttemptTimeout")
    def dns_retry_attempt_timeout(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SkuCapacityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default: Optional[_builtins.int] = ...,
        elastic_maximum: Optional[_builtins.int] = ...,
        maximum: Optional[_builtins.int] = ...,
        minimum: Optional[_builtins.int] = ...,
        scale_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="elasticMaximum")
    def elastic_maximum(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scaleType")
    def scale_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SkuDescriptionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capabilities: Optional[Sequence[outputs.CapabilityResponse]] = ...,
        capacity: Optional[_builtins.int] = ...,
        family: Optional[_builtins.str] = ...,
        locations: Optional[Sequence[_builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        size: Optional[_builtins.str] = ...,
        sku_capacity: Optional[outputs.SkuCapacityResponse] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Optional[Sequence[outputs.CapabilityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skuCapacity")
    def sku_capacity(self) -> Optional[outputs.SkuCapacityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SlotSwapStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_slot_name: _builtins.str,
        source_slot_name: _builtins.str,
        timestamp_utc: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationSlotName")
    def destination_slot_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceSlotName")
    def source_slot_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timestampUtc")
    def timestamp_utc(self) -> _builtins.str: ...

@pulumi.output_type
class StaticSiteBuildPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_build_command: Optional[_builtins.str] = ...,
        api_location: Optional[_builtins.str] = ...,
        app_artifact_location: Optional[_builtins.str] = ...,
        app_build_command: Optional[_builtins.str] = ...,
        app_location: Optional[_builtins.str] = ...,
        github_action_secret_name_override: Optional[_builtins.str] = ...,
        output_location: Optional[_builtins.str] = ...,
        skip_github_action_workflow_generation: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiBuildCommand")
    def api_build_command(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="apiLocation")
    def api_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appArtifactLocation")
    def app_artifact_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appBuildCommand")
    def app_build_command(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appLocation")
    def app_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="githubActionSecretNameOverride")
    def github_action_secret_name_override(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputLocation")
    def output_location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipGithubActionWorkflowGeneration")
    def skip_github_action_workflow_generation(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class StaticSiteDatabaseConnectionConfigurationFileOverviewResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        contents: _builtins.str,
        file_name: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def contents(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class StaticSiteLinkedBackendResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_on: _builtins.str,
        provisioning_state: _builtins.str,
        backend_resource_id: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="backendResourceId")
    def backend_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StaticSiteTemplateOptionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        is_private: Optional[_builtins.bool] = ...,
        owner: Optional[_builtins.str] = ...,
        repository_name: Optional[_builtins.str] = ...,
        template_repository_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isPrivate")
    def is_private(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="templateRepositoryUrl")
    def template_repository_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StaticSiteUserARMResourceResponse(dict):
    def __init__(
        __self__,
        *,
        display_name: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        provider: _builtins.str,
        type: _builtins.str,
        user_id: _builtins.str,
        kind: Optional[_builtins.str] = ...,
        roles: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def provider(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StaticSiteUserProvidedFunctionAppResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_on: _builtins.str,
        id: _builtins.str,
        name: _builtins.str,
        type: _builtins.str,
        function_app_region: Optional[_builtins.str] = ...,
        function_app_resource_id: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="functionAppRegion")
    def function_app_region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="functionAppResourceId")
    def function_app_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TokenStoreResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        azure_blob_storage: Optional[outputs.BlobStorageTokenStoreResponse] = ...,
        enabled: Optional[_builtins.bool] = ...,
        file_system: Optional[outputs.FileSystemTokenStoreResponse] = ...,
        token_refresh_extension_hours: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureBlobStorage")
    def azure_blob_storage(self) -> Optional[outputs.BlobStorageTokenStoreResponse]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystem")
    def file_system(self) -> Optional[outputs.FileSystemTokenStoreResponse]: ...
    @_builtins.property
    @pulumi.getter(name="tokenRefreshExtensionHours")
    def token_refresh_extension_hours(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class TwitterRegistrationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        consumer_key: Optional[_builtins.str] = ...,
        consumer_secret_setting_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="consumerKey")
    def consumer_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="consumerSecretSettingName")
    def consumer_secret_setting_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TwitterResponse(dict):
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        registration: Optional[outputs.TwitterRegistrationResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.TwitterRegistrationResponse]: ...

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

@pulumi.output_type
class VirtualNetworkProfileResponse(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        type: _builtins.str,
        subnet: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VnetRouteResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        type: _builtins.str,
        end_address: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
        route_type: Optional[_builtins.str] = ...,
        start_address: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endAddress")
    def end_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routeType")
    def route_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startAddress")
    def start_address(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class VolumeMountResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_mount_path: _builtins.str,
        volume_sub_path: _builtins.str,
        data: Optional[_builtins.str] = ...,
        read_only: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerMountPath")
    def container_mount_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="volumeSubPath")
    def volume_sub_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class WorkflowEnvelopeResponseProperties(dict):
    def __init__(
        __self__,
        *,
        files: Optional[Mapping[str, Any]] = ...,
        flow_state: Optional[_builtins.str] = ...,
        health: Optional[outputs.WorkflowHealthResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def files(self) -> Optional[Mapping[str, Any]]: ...
    @_builtins.property
    @pulumi.getter(name="flowState")
    def flow_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def health(self) -> Optional[outputs.WorkflowHealthResponse]: ...

@pulumi.output_type
class WorkflowHealthResponse(dict):
    def __init__(
        __self__,
        *,
        state: _builtins.str,
        error: Optional[outputs.ErrorEntityResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ErrorEntityResponse]: ...

@pulumi.output_type
class WorkflowTriggerListCallbackUrlQueriesResponse(dict):
    def __init__(
        __self__,
        *,
        api_version: Optional[_builtins.str] = ...,
        se: Optional[_builtins.str] = ...,
        sig: Optional[_builtins.str] = ...,
        sp: Optional[_builtins.str] = ...,
        sv: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def se(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sig(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sp(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sv(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WsdlDefinitionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        content: Optional[_builtins.str] = ...,
        import_method: Optional[_builtins.str] = ...,
        service: Optional[outputs.WsdlServiceResponse] = ...,
        url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="importMethod")
    def import_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[outputs.WsdlServiceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WsdlServiceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        qualified_name: _builtins.str,
        endpoint_qualified_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="qualifiedName")
    def qualified_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointQualifiedNames")
    def endpoint_qualified_names(self) -> Optional[Sequence[_builtins.str]]: ...
