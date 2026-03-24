

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
__all__ = ['AllowedAudiencesValidationResponse', 'AllowedPrincipalsResponse', 'AppInsightsConfigurationResponse', 'AppLogsConfigurationResponse', 'AppRegistrationResponse', 'AppleRegistrationResponse', 'AppleResponse', 'AuthPlatformResponse', 'AzureActiveDirectoryLoginResponse', 'AzureActiveDirectoryRegistrationResponse', 'AzureActiveDirectoryResponse', 'AzureActiveDirectoryValidationResponse', 'AzureCredentialsResponse', 'AzureFilePropertiesResponse', 'AzureStaticWebAppsRegistrationResponse', 'AzureStaticWebAppsResponse', 'BlobStorageTokenStoreResponse', 'BuildConfigurationResponse', 'CertificateKeyVaultPropertiesResponse', 'CertificateResponseProperties', 'CircuitBreakerPolicyResponse', 'ClientRegistrationResponse', 'ConfigurationResponse', 'ConnectedEnvironmentStorageResponseProperties', 'ContainerAppProbeResponse', 'ContainerAppProbeResponseHttpGet', 'ContainerAppProbeResponseHttpHeaders', 'ContainerAppProbeResponseTcpSocket', 'ContainerAppResponsePatchingConfiguration', 'ContainerAppSecretResponse', 'ContainerRegistryResponse', 'ContainerRegistryWithCustomImageResponse', 'ContainerResourcesResponse', 'ContainerResponse', 'CookieExpirationResponse', 'CorsPolicyResponse', 'CustomContainerTemplateResponse', 'CustomDomainConfigurationResponse', 'CustomDomainResponse', ..., 'CustomHostnameAnalysisResultResponseDetails', 'CustomOpenIdConnectProviderResponse', 'CustomScaleRuleResponse', ..., 'DaprComponentResiliencyPolicyConfigurationResponse', ..., ..., ..., 'DaprComponentServiceBindingResponse', 'DaprConfigurationResponse', 'DaprMetadataResponse', 'DaprResponse', 'DaprResponseAppHealth', 'DaprSecretResponse', 'DaprServiceBindMetadataResponse', 'DaprSubscriptionBulkSubscribeOptionsResponse', 'DaprSubscriptionRouteRuleResponse', 'DaprSubscriptionRoutesResponse', 'DataDogConfigurationResponse', 'DefaultAuthorizationPolicyResponse', 'DestinationsConfigurationResponse', 'DiskEncryptionConfigurationResponse', 'DiskEncryptionConfigurationResponseAuth', ..., 'DotNetComponentConfigurationPropertyResponse', 'DotNetComponentServiceBindResponse', 'DynamicPoolConfigurationResponse', 'EncryptionSettingsResponse', 'EnvironmentVarResponse', 'EnvironmentVariableResponse', 'ErrorEntityResponse', 'ExtendedLocationResponse', 'FacebookResponse', 'ForwardProxyResponse', 'GitHubResponse', 'GithubActionConfigurationResponse', 'GlobalValidationResponse', 'GoogleResponse', 'HeaderMatchResponse', 'HeaderResponse', 'HttpConnectionPoolResponse', 'HttpGetResponse', 'HttpRetryPolicyResponse', 'HttpRouteActionResponse', 'HttpRouteConfigResponseProperties', 'HttpRouteMatchResponse', 'HttpRouteProvisioningErrorsResponse', 'HttpRouteResponse', 'HttpRouteRuleResponse', 'HttpRouteTargetResponse', 'HttpScaleRuleResponse', 'HttpSettingsResponse', 'HttpSettingsRoutesResponse', 'IdentityProvidersResponse', 'IdentitySettingsResponse', 'IngressConfigurationResponse', 'IngressConfigurationResponseScale', 'IngressPortMappingResponse', 'IngressResponse', 'IngressResponseStickySessions', 'InitContainerResponse', 'IpSecurityRestrictionRuleResponse', 'JavaComponentConfigurationPropertyResponse', 'JavaComponentIngressResponse', 'JavaComponentPropertiesResponseScale', 'JavaComponentServiceBindResponse', 'JobConfigurationResponse', 'JobConfigurationResponseEventTriggerConfig', 'JobConfigurationResponseManualTriggerConfig', 'JobConfigurationResponseScheduleTriggerConfig', 'JobScaleResponse', 'JobScaleRuleResponse', 'JobTemplateResponse', 'JwtClaimChecksResponse', 'KedaConfigurationResponse', 'LifecycleConfigurationResponse', 'LogAnalyticsConfigurationResponse', 'LoggerSettingResponse', 'LoginResponse', 'LoginRoutesResponse', 'LoginScopesResponse', 'LogsConfigurationResponse', 'ManagedCertificateResponseProperties', 'ManagedEnvironmentResponseEncryption', 'ManagedEnvironmentResponsePeerAuthentication', 'ManagedEnvironmentResponsePeerTrafficConfiguration', 'ManagedEnvironmentStorageResponseProperties', 'ManagedIdentitySettingResponse', 'ManagedServiceIdentityResponse', 'MetricsConfigurationResponse', 'MtlsResponse', 'NacosComponentResponse', 'NfsAzureFilePropertiesResponse', 'NonceResponse', 'OpenIdConnectClientCredentialResponse', 'OpenIdConnectConfigResponse', 'OpenIdConnectLoginResponse', 'OpenIdConnectRegistrationResponse', 'OpenTelemetryConfigurationResponse', 'OtlpConfigurationResponse', 'PreBuildStepResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'QueueScaleRuleResponse', 'RegistryCredentialsResponse', 'RegistryInfoResponse', 'RuntimeResponse', 'RuntimeResponseDotnet', 'RuntimeResponseJava', 'RuntimeResponseJavaAgent', 'RuntimeResponseLogging', 'ScaleConfigurationResponse', 'ScaleResponse', 'ScaleRuleAuthResponse', 'ScaleRuleResponse', 'ScgRouteResponse', 'ScheduledEntryResponse', 'SecretKeyVaultPropertiesResponse', 'SecretResponse', 'SecretVolumeItemResponse', 'ServiceBindResponse', 'ServiceResponse', 'SessionContainerResourcesResponse', 'SessionContainerResponse', 'SessionIngressResponse', 'SessionNetworkConfigurationResponse', 'SessionPoolSecretResponse', 'SessionProbeResponse', 'SessionProbeResponseHttpGet', 'SessionProbeResponseHttpHeaders', 'SessionProbeResponseTcpSocket', 'SessionRegistryCredentialsResponse', 'SmbStorageResponse', 'SpringBootAdminComponentResponse', 'SpringCloudConfigComponentResponse', 'SpringCloudEurekaComponentResponse', 'SpringCloudGatewayComponentResponse', 'SystemDataResponse', 'TcpConnectionPoolResponse', 'TcpRetryPolicyResponse', 'TcpScaleRuleResponse', 'TemplateResponse', 'TimeoutPolicyResponse', 'TokenStoreResponse', 'TracesConfigurationResponse', 'TrafficWeightResponse', 'TwitterRegistrationResponse', 'TwitterResponse', 'UserAssignedIdentityResponse', 'VnetConfigurationResponse', 'VolumeMountResponse', 'VolumeResponse', 'WorkflowEnvelopeResponseProperties', 'WorkflowHealthResponse', 'WorkloadProfileResponse']
@pulumi.output_type
class AllowedAudiencesValidationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_audiences: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AllowedPrincipalsResponse(dict):
    
    def __init__(__self__, *, groups: Optional[Sequence[_builtins.str]] = ..., identities: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AppInsightsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_string: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppLogsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination: Optional[_builtins.str] = ..., log_analytics_configuration: Optional[outputs.LogAnalyticsConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logAnalyticsConfiguration")
    def log_analytics_configuration(self) -> Optional[outputs.LogAnalyticsConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class AppRegistrationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, app_id: Optional[_builtins.str] = ..., app_secret_setting_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSecretSettingName")
    def app_secret_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppleRegistrationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., client_secret_setting_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppleResponse(dict):
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., login: Optional[outputs.LoginScopesResponse] = ..., registration: Optional[outputs.AppleRegistrationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.LoginScopesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.AppleRegistrationResponse]:
        
        ...
    


@pulumi.output_type
class AuthPlatformResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., runtime_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureActiveDirectoryLoginResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disable_www_authenticate: Optional[_builtins.bool] = ..., login_parameters: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableWWWAuthenticate")
    def disable_www_authenticate(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginParameters")
    def login_parameters(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AzureActiveDirectoryRegistrationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., client_secret_certificate_issuer: Optional[_builtins.str] = ..., client_secret_certificate_subject_alternative_name: Optional[_builtins.str] = ..., client_secret_certificate_thumbprint: Optional[_builtins.str] = ..., client_secret_setting_name: Optional[_builtins.str] = ..., open_id_issuer: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretCertificateIssuer")
    def client_secret_certificate_issuer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretCertificateSubjectAlternativeName")
    def client_secret_certificate_subject_alternative_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretCertificateThumbprint")
    def client_secret_certificate_thumbprint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openIdIssuer")
    def open_id_issuer(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureActiveDirectoryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., is_auto_provisioned: Optional[_builtins.bool] = ..., login: Optional[outputs.AzureActiveDirectoryLoginResponse] = ..., registration: Optional[outputs.AzureActiveDirectoryRegistrationResponse] = ..., validation: Optional[outputs.AzureActiveDirectoryValidationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAutoProvisioned")
    def is_auto_provisioned(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.AzureActiveDirectoryLoginResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.AzureActiveDirectoryRegistrationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def validation(self) -> Optional[outputs.AzureActiveDirectoryValidationResponse]:
        
        ...
    


@pulumi.output_type
class AzureActiveDirectoryValidationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_audiences: Optional[Sequence[_builtins.str]] = ..., default_authorization_policy: Optional[outputs.DefaultAuthorizationPolicyResponse] = ..., jwt_claim_checks: Optional[outputs.JwtClaimChecksResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAuthorizationPolicy")
    def default_authorization_policy(self) -> Optional[outputs.DefaultAuthorizationPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwtClaimChecks")
    def jwt_claim_checks(self) -> Optional[outputs.JwtClaimChecksResponse]:
        
        ...
    


@pulumi.output_type
class AzureCredentialsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subscription_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureFilePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_mode: Optional[_builtins.str] = ..., account_key: Optional[_builtins.str] = ..., account_key_vault_properties: Optional[outputs.SecretKeyVaultPropertiesResponse] = ..., account_name: Optional[_builtins.str] = ..., share_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKeyVaultProperties")
    def account_key_vault_properties(self) -> Optional[outputs.SecretKeyVaultPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureStaticWebAppsRegistrationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AzureStaticWebAppsResponse(dict):
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., registration: Optional[outputs.AzureStaticWebAppsRegistrationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.AzureStaticWebAppsRegistrationResponse]:
        
        ...
    


@pulumi.output_type
class BlobStorageTokenStoreResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, blob_container_uri: Optional[_builtins.str] = ..., client_id: Optional[_builtins.str] = ..., managed_identity_resource_id: Optional[_builtins.str] = ..., sas_url_setting_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobContainerUri")
    def blob_container_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentityResourceId")
    def managed_identity_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasUrlSettingName")
    def sas_url_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BuildConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, base_os: Optional[_builtins.str] = ..., environment_variables: Optional[Sequence[outputs.EnvironmentVariableResponse]] = ..., platform: Optional[_builtins.str] = ..., platform_version: Optional[_builtins.str] = ..., pre_build_steps: Optional[Sequence[outputs.PreBuildStepResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseOs")
    def base_os(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Sequence[outputs.EnvironmentVariableResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preBuildSteps")
    def pre_build_steps(self) -> Optional[Sequence[outputs.PreBuildStepResponse]]:
        
        ...
    


@pulumi.output_type
class CertificateKeyVaultPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity: Optional[_builtins.str] = ..., key_vault_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CertificateResponseProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment_errors: _builtins.str, expiration_date: _builtins.str, issue_date: _builtins.str, issuer: _builtins.str, provisioning_state: _builtins.str, public_key_hash: _builtins.str, subject_alternative_names: Sequence[_builtins.str], subject_name: _builtins.str, thumbprint: _builtins.str, valid: _builtins.bool, certificate_key_vault_properties: Optional[outputs.CertificateKeyVaultPropertiesResponse] = ..., certificate_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentErrors")
    def deployment_errors(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issueDate")
    def issue_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKeyHash")
    def public_key_hash(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectAlternativeNames")
    def subject_alternative_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def valid(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateKeyVaultProperties")
    def certificate_key_vault_properties(self) -> Optional[outputs.CertificateKeyVaultPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateType")
    def certificate_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CircuitBreakerPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, consecutive_errors: Optional[_builtins.int] = ..., interval_in_seconds: Optional[_builtins.int] = ..., max_ejection_percent: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consecutiveErrors")
    def consecutive_errors(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intervalInSeconds")
    def interval_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxEjectionPercent")
    def max_ejection_percent(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ClientRegistrationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., client_secret_setting_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active_revisions_mode: Optional[_builtins.str] = ..., dapr: Optional[outputs.DaprResponse] = ..., identity_settings: Optional[Sequence[outputs.IdentitySettingsResponse]] = ..., ingress: Optional[outputs.IngressResponse] = ..., max_inactive_revisions: Optional[_builtins.int] = ..., registries: Optional[Sequence[outputs.RegistryCredentialsResponse]] = ..., revision_transition_threshold: Optional[_builtins.int] = ..., runtime: Optional[outputs.RuntimeResponse] = ..., secrets: Optional[Sequence[outputs.SecretResponse]] = ..., service: Optional[outputs.ServiceResponse] = ..., target_label: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeRevisionsMode")
    def active_revisions_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dapr(self) -> Optional[outputs.DaprResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identitySettings")
    def identity_settings(self) -> Optional[Sequence[outputs.IdentitySettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[outputs.IngressResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInactiveRevisions")
    def max_inactive_revisions(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registries(self) -> Optional[Sequence[outputs.RegistryCredentialsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionTransitionThreshold")
    def revision_transition_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[outputs.RuntimeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[outputs.SecretResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[outputs.ServiceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLabel")
    def target_label(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectedEnvironmentStorageResponseProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deployment_errors: _builtins.str, provisioning_state: _builtins.str, azure_file: Optional[outputs.AzureFilePropertiesResponse] = ..., smb: Optional[outputs.SmbStorageResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentErrors")
    def deployment_errors(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFile")
    def azure_file(self) -> Optional[outputs.AzureFilePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def smb(self) -> Optional[outputs.SmbStorageResponse]:
        
        ...
    


@pulumi.output_type
class ContainerAppProbeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_threshold: Optional[_builtins.int] = ..., http_get: Optional[outputs.ContainerAppProbeResponseHttpGet] = ..., initial_delay_seconds: Optional[_builtins.int] = ..., period_seconds: Optional[_builtins.int] = ..., success_threshold: Optional[_builtins.int] = ..., tcp_socket: Optional[outputs.ContainerAppProbeResponseTcpSocket] = ..., termination_grace_period_seconds: Optional[_builtins.float] = ..., timeout_seconds: Optional[_builtins.int] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[outputs.ContainerAppProbeResponseHttpGet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(self) -> Optional[outputs.ContainerAppProbeResponseTcpSocket]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationGracePeriodSeconds")
    def termination_grace_period_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContainerAppProbeResponseHttpGet(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, port: _builtins.int, host: Optional[_builtins.str] = ..., http_headers: Optional[Sequence[outputs.ContainerAppProbeResponseHttpHeaders]] = ..., path: Optional[_builtins.str] = ..., scheme: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[Sequence[outputs.ContainerAppProbeResponseHttpHeaders]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContainerAppProbeResponseHttpHeaders(dict):
    
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ContainerAppProbeResponseTcpSocket(dict):
    
    def __init__(__self__, *, port: _builtins.int, host: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContainerAppResponsePatchingConfiguration(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, patching_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchingMode")
    def patching_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContainerAppSecretResponse(dict):
    
    def __init__(__self__, *, identity: _builtins.str, key_vault_url: _builtins.str, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ContainerRegistryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_registry_server: _builtins.str, identity_resource_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerRegistryServer")
    def container_registry_server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityResourceId")
    def identity_resource_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ContainerRegistryWithCustomImageResponse(dict):
    
    def __init__(__self__, *, server: _builtins.str, image: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContainerResourcesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ephemeral_storage: _builtins.str, cpu: Optional[_builtins.float] = ..., gpu: Optional[_builtins.float] = ..., memory: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gpu(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, args: Optional[Sequence[_builtins.str]] = ..., command: Optional[Sequence[_builtins.str]] = ..., env: Optional[Sequence[outputs.EnvironmentVarResponse]] = ..., image: Optional[_builtins.str] = ..., image_type: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., probes: Optional[Sequence[outputs.ContainerAppProbeResponse]] = ..., resources: Optional[outputs.ContainerResourcesResponse] = ..., volume_mounts: Optional[Sequence[outputs.VolumeMountResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def env(self) -> Optional[Sequence[outputs.EnvironmentVarResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def probes(self) -> Optional[Sequence[outputs.ContainerAppProbeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[outputs.ContainerResourcesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[Sequence[outputs.VolumeMountResponse]]:
        
        ...
    


@pulumi.output_type
class CookieExpirationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, convention: Optional[_builtins.str] = ..., time_to_expiration: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def convention(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToExpiration")
    def time_to_expiration(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CorsPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_origins: Sequence[_builtins.str], allow_credentials: Optional[_builtins.bool] = ..., allowed_headers: Optional[Sequence[_builtins.str]] = ..., allowed_methods: Optional[Sequence[_builtins.str]] = ..., expose_headers: Optional[Sequence[_builtins.str]] = ..., max_age: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class CustomContainerTemplateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, containers: Optional[Sequence[outputs.SessionContainerResponse]] = ..., ingress: Optional[outputs.SessionIngressResponse] = ..., registry_credentials: Optional[outputs.SessionRegistryCredentialsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[Sequence[outputs.SessionContainerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[outputs.SessionIngressResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryCredentials")
    def registry_credentials(self) -> Optional[outputs.SessionRegistryCredentialsResponse]:
        
        ...
    


@pulumi.output_type
class CustomDomainConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_domain_verification_id: _builtins.str, expiration_date: _builtins.str, subject_name: _builtins.str, thumbprint: _builtins.str, certificate_key_vault_properties: Optional[outputs.CertificateKeyVaultPropertiesResponse] = ..., certificate_password: Optional[_builtins.str] = ..., certificate_value: Optional[_builtins.str] = ..., dns_suffix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomainVerificationId")
    def custom_domain_verification_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateKeyVaultProperties")
    def certificate_key_vault_properties(self) -> Optional[outputs.CertificateKeyVaultPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificatePassword")
    def certificate_password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateValue")
    def certificate_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CustomDomainResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, binding_type: Optional[_builtins.str] = ..., certificate_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bindingType")
    def binding_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CustomHostnameAnalysisResultResponseCustomDomainVerificationFailureInfo(dict):
    
    def __init__(__self__, *, code: _builtins.str, message: _builtins.str, target: _builtins.str, details: Optional[Sequence[outputs.CustomHostnameAnalysisResultResponseDetails]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[outputs.CustomHostnameAnalysisResultResponseDetails]]:
        
        ...
    


@pulumi.output_type
class CustomHostnameAnalysisResultResponseDetails(dict):
    
    def __init__(__self__, *, code: _builtins.str, message: _builtins.str, target: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CustomOpenIdConnectProviderResponse(dict):
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., login: Optional[outputs.OpenIdConnectLoginResponse] = ..., registration: Optional[outputs.OpenIdConnectRegistrationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.OpenIdConnectLoginResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.OpenIdConnectRegistrationResponse]:
        
        ...
    


@pulumi.output_type
class CustomScaleRuleResponse(dict):
    
    def __init__(__self__, *, auth: Optional[Sequence[outputs.ScaleRuleAuthResponse]] = ..., identity: Optional[_builtins.str] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[Sequence[outputs.ScaleRuleAuthResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DaprComponentResiliencyPolicyCircuitBreakerPolicyConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, consecutive_errors: Optional[_builtins.int] = ..., interval_in_seconds: Optional[_builtins.int] = ..., timeout_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consecutiveErrors")
    def consecutive_errors(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intervalInSeconds")
    def interval_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DaprComponentResiliencyPolicyConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, circuit_breaker_policy: Optional[outputs.DaprComponentResiliencyPolicyCircuitBreakerPolicyConfigurationResponse] = ..., http_retry_policy: Optional[outputs.DaprComponentResiliencyPolicyHttpRetryPolicyConfigurationResponse] = ..., timeout_policy: Optional[outputs.DaprComponentResiliencyPolicyTimeoutPolicyConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitBreakerPolicy")
    def circuit_breaker_policy(self) -> Optional[outputs.DaprComponentResiliencyPolicyCircuitBreakerPolicyConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpRetryPolicy")
    def http_retry_policy(self) -> Optional[outputs.DaprComponentResiliencyPolicyHttpRetryPolicyConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutPolicy")
    def timeout_policy(self) -> Optional[outputs.DaprComponentResiliencyPolicyTimeoutPolicyConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class DaprComponentResiliencyPolicyHttpRetryBackOffConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, initial_delay_in_milliseconds: Optional[_builtins.int] = ..., max_interval_in_milliseconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelayInMilliseconds")
    def initial_delay_in_milliseconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIntervalInMilliseconds")
    def max_interval_in_milliseconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DaprComponentResiliencyPolicyHttpRetryPolicyConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_retries: Optional[_builtins.int] = ..., retry_back_off: Optional[outputs.DaprComponentResiliencyPolicyHttpRetryBackOffConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryBackOff")
    def retry_back_off(self) -> Optional[outputs.DaprComponentResiliencyPolicyHttpRetryBackOffConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class DaprComponentResiliencyPolicyTimeoutPolicyConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, response_timeout_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseTimeoutInSeconds")
    def response_timeout_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DaprComponentServiceBindingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metadata: Optional[outputs.DaprServiceBindMetadataResponse] = ..., name: Optional[_builtins.str] = ..., service_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.DaprServiceBindMetadataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DaprConfigurationResponse(dict):
    
    def __init__(__self__, *, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DaprMetadataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., secret_ref: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DaprResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, app_health: Optional[outputs.DaprResponseAppHealth] = ..., app_id: Optional[_builtins.str] = ..., app_port: Optional[_builtins.int] = ..., app_protocol: Optional[_builtins.str] = ..., enable_api_logging: Optional[_builtins.bool] = ..., enabled: Optional[_builtins.bool] = ..., http_max_request_size: Optional[_builtins.int] = ..., http_read_buffer_size: Optional[_builtins.int] = ..., log_level: Optional[_builtins.str] = ..., max_concurrency: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appHealth")
    def app_health(self) -> Optional[outputs.DaprResponseAppHealth]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appPort")
    def app_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appProtocol")
    def app_protocol(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableApiLogging")
    def enable_api_logging(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMaxRequestSize")
    def http_max_request_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpReadBufferSize")
    def http_read_buffer_size(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DaprResponseAppHealth(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., path: Optional[_builtins.str] = ..., probe_interval_seconds: Optional[_builtins.int] = ..., probe_timeout_milliseconds: Optional[_builtins.int] = ..., threshold: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="probeIntervalSeconds")
    def probe_interval_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="probeTimeoutMilliseconds")
    def probe_timeout_milliseconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DaprSecretResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DaprServiceBindMetadataResponse(dict):
    
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
class DaprSubscriptionBulkSubscribeOptionsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., max_await_duration_ms: Optional[_builtins.int] = ..., max_messages_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAwaitDurationMs")
    def max_await_duration_ms(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxMessagesCount")
    def max_messages_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DaprSubscriptionRouteRuleResponse(dict):
    
    def __init__(__self__, *, match: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DaprSubscriptionRoutesResponse(dict):
    
    def __init__(__self__, *, default: Optional[_builtins.str] = ..., rules: Optional[Sequence[outputs.DaprSubscriptionRouteRuleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.DaprSubscriptionRouteRuleResponse]]:
        
        ...
    


@pulumi.output_type
class DataDogConfigurationResponse(dict):
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., site: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def site(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DefaultAuthorizationPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_applications: Optional[Sequence[_builtins.str]] = ..., allowed_principals: Optional[outputs.AllowedPrincipalsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedApplications")
    def allowed_applications(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedPrincipals")
    def allowed_principals(self) -> Optional[outputs.AllowedPrincipalsResponse]:
        
        ...
    


@pulumi.output_type
class DestinationsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_dog_configuration: Optional[outputs.DataDogConfigurationResponse] = ..., otlp_configurations: Optional[Sequence[outputs.OtlpConfigurationResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDogConfiguration")
    def data_dog_configuration(self) -> Optional[outputs.DataDogConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="otlpConfigurations")
    def otlp_configurations(self) -> Optional[Sequence[outputs.OtlpConfigurationResponse]]:
        
        ...
    


@pulumi.output_type
class DiskEncryptionConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_vault_configuration: Optional[outputs.DiskEncryptionConfigurationResponseKeyVaultConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultConfiguration")
    def key_vault_configuration(self) -> Optional[outputs.DiskEncryptionConfigurationResponseKeyVaultConfiguration]:
        
        ...
    


@pulumi.output_type
class DiskEncryptionConfigurationResponseAuth(dict):
    
    def __init__(__self__, *, identity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DiskEncryptionConfigurationResponseKeyVaultConfiguration(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth: Optional[outputs.DiskEncryptionConfigurationResponseAuth] = ..., key_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[outputs.DiskEncryptionConfigurationResponseAuth]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUrl")
    def key_url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DotNetComponentConfigurationPropertyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, property_name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DotNetComponentServiceBindResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., service_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DynamicPoolConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lifecycle_configuration: Optional[outputs.LifecycleConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfiguration")
    def lifecycle_configuration(self) -> Optional[outputs.LifecycleConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class EncryptionSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_app_auth_encryption_secret_name: Optional[_builtins.str] = ..., container_app_auth_signing_secret_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAppAuthEncryptionSecretName")
    def container_app_auth_encryption_secret_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAppAuthSigningSecretName")
    def container_app_auth_signing_secret_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentVarResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., secret_ref: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EnvironmentVariableResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ErrorEntityResponse(dict):
    
    def __init__(__self__, *, code: Optional[_builtins.str] = ..., details: Optional[Sequence[outputs.ErrorEntityResponse]] = ..., extended_code: Optional[_builtins.str] = ..., inner_errors: Optional[Sequence[outputs.ErrorEntityResponse]] = ..., message: Optional[_builtins.str] = ..., message_template: Optional[_builtins.str] = ..., parameters: Optional[Sequence[_builtins.str]] = ..., target: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[outputs.ErrorEntityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedCode")
    def extended_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="innerErrors")
    def inner_errors(self) -> Optional[Sequence[outputs.ErrorEntityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageTemplate")
    def message_template(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExtendedLocationResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FacebookResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., graph_api_version: Optional[_builtins.str] = ..., login: Optional[outputs.LoginScopesResponse] = ..., registration: Optional[outputs.AppRegistrationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="graphApiVersion")
    def graph_api_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.LoginScopesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.AppRegistrationResponse]:
        
        ...
    


@pulumi.output_type
class ForwardProxyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, convention: Optional[_builtins.str] = ..., custom_host_header_name: Optional[_builtins.str] = ..., custom_proto_header_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def convention(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHostHeaderName")
    def custom_host_header_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProtoHeaderName")
    def custom_proto_header_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GitHubResponse(dict):
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., login: Optional[outputs.LoginScopesResponse] = ..., registration: Optional[outputs.ClientRegistrationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.LoginScopesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.ClientRegistrationResponse]:
        
        ...
    


@pulumi.output_type
class GithubActionConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_credentials: Optional[outputs.AzureCredentialsResponse] = ..., build_environment_variables: Optional[Sequence[outputs.EnvironmentVariableResponse]] = ..., context_path: Optional[_builtins.str] = ..., dockerfile_path: Optional[_builtins.str] = ..., image: Optional[_builtins.str] = ..., os: Optional[_builtins.str] = ..., publish_type: Optional[_builtins.str] = ..., registry_info: Optional[outputs.RegistryInfoResponse] = ..., runtime_stack: Optional[_builtins.str] = ..., runtime_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureCredentials")
    def azure_credentials(self) -> Optional[outputs.AzureCredentialsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildEnvironmentVariables")
    def build_environment_variables(self) -> Optional[Sequence[outputs.EnvironmentVariableResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contextPath")
    def context_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerfilePath")
    def dockerfile_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def os(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishType")
    def publish_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryInfo")
    def registry_info(self) -> Optional[outputs.RegistryInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeStack")
    def runtime_stack(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GlobalValidationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, excluded_paths: Optional[Sequence[_builtins.str]] = ..., redirect_to_provider: Optional[_builtins.str] = ..., unauthenticated_client_action: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedPaths")
    def excluded_paths(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectToProvider")
    def redirect_to_provider(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unauthenticatedClientAction")
    def unauthenticated_client_action(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GoogleResponse(dict):
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., login: Optional[outputs.LoginScopesResponse] = ..., registration: Optional[outputs.ClientRegistrationResponse] = ..., validation: Optional[outputs.AllowedAudiencesValidationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.LoginScopesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.ClientRegistrationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def validation(self) -> Optional[outputs.AllowedAudiencesValidationResponse]:
        
        ...
    


@pulumi.output_type
class HeaderMatchResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, exact_match: Optional[_builtins.str] = ..., header: Optional[_builtins.str] = ..., prefix_match: Optional[_builtins.str] = ..., regex_match: Optional[_builtins.str] = ..., suffix_match: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexMatch")
    def regex_match(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suffixMatch")
    def suffix_match(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HeaderResponse(dict):
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HttpConnectionPoolResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, http1_max_pending_requests: Optional[_builtins.int] = ..., http2_max_requests: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="http1MaxPendingRequests")
    def http1_max_pending_requests(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="http2MaxRequests")
    def http2_max_requests(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class HttpGetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, url: _builtins.str, file_name: Optional[_builtins.str] = ..., headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class HttpRetryPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, errors: Optional[Sequence[_builtins.str]] = ..., headers: Optional[Sequence[outputs.HeaderMatchResponse]] = ..., http_status_codes: Optional[Sequence[_builtins.int]] = ..., initial_delay_in_milliseconds: Optional[_builtins.float] = ..., max_interval_in_milliseconds: Optional[_builtins.float] = ..., max_retries: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.HeaderMatchResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpStatusCodes")
    def http_status_codes(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelayInMilliseconds")
    def initial_delay_in_milliseconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIntervalInMilliseconds")
    def max_interval_in_milliseconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class HttpRouteActionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, prefix_rewrite: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixRewrite")
    def prefix_rewrite(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HttpRouteConfigResponseProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fqdn: _builtins.str, provisioning_errors: Sequence[outputs.HttpRouteProvisioningErrorsResponse], provisioning_state: _builtins.str, custom_domains: Optional[Sequence[outputs.CustomDomainResponse]] = ..., rules: Optional[Sequence[outputs.HttpRouteRuleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningErrors")
    def provisioning_errors(self) -> Sequence[outputs.HttpRouteProvisioningErrorsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Optional[Sequence[outputs.CustomDomainResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.HttpRouteRuleResponse]]:
        
        ...
    


@pulumi.output_type
class HttpRouteMatchResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, case_sensitive: Optional[_builtins.bool] = ..., path: Optional[_builtins.str] = ..., path_separated_prefix: Optional[_builtins.str] = ..., prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caseSensitive")
    def case_sensitive(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathSeparatedPrefix")
    def path_separated_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HttpRouteProvisioningErrorsResponse(dict):
    
    def __init__(__self__, *, message: _builtins.str, timestamp: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class HttpRouteResponse(dict):
    
    def __init__(__self__, *, action: Optional[outputs.HttpRouteActionResponse] = ..., match: Optional[outputs.HttpRouteMatchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[outputs.HttpRouteActionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[outputs.HttpRouteMatchResponse]:
        
        ...
    


@pulumi.output_type
class HttpRouteRuleResponse(dict):
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., routes: Optional[Sequence[outputs.HttpRouteResponse]] = ..., targets: Optional[Sequence[outputs.HttpRouteTargetResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[Sequence[outputs.HttpRouteResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Optional[Sequence[outputs.HttpRouteTargetResponse]]:
        
        ...
    


@pulumi.output_type
class HttpRouteTargetResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_app: _builtins.str, label: Optional[_builtins.str] = ..., revision: Optional[_builtins.str] = ..., weight: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerApp")
    def container_app(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class HttpScaleRuleResponse(dict):
    
    def __init__(__self__, *, auth: Optional[Sequence[outputs.ScaleRuleAuthResponse]] = ..., identity: Optional[_builtins.str] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[Sequence[outputs.ScaleRuleAuthResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class HttpSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, forward_proxy: Optional[outputs.ForwardProxyResponse] = ..., require_https: Optional[_builtins.bool] = ..., routes: Optional[outputs.HttpSettingsRoutesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardProxy")
    def forward_proxy(self) -> Optional[outputs.ForwardProxyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireHttps")
    def require_https(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[outputs.HttpSettingsRoutesResponse]:
        
        ...
    


@pulumi.output_type
class HttpSettingsRoutesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiPrefix")
    def api_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IdentityProvidersResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, apple: Optional[outputs.AppleResponse] = ..., azure_active_directory: Optional[outputs.AzureActiveDirectoryResponse] = ..., azure_static_web_apps: Optional[outputs.AzureStaticWebAppsResponse] = ..., custom_open_id_connect_providers: Optional[Mapping[str, outputs.CustomOpenIdConnectProviderResponse]] = ..., facebook: Optional[outputs.FacebookResponse] = ..., git_hub: Optional[outputs.GitHubResponse] = ..., google: Optional[outputs.GoogleResponse] = ..., twitter: Optional[outputs.TwitterResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def apple(self) -> Optional[outputs.AppleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureActiveDirectory")
    def azure_active_directory(self) -> Optional[outputs.AzureActiveDirectoryResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureStaticWebApps")
    def azure_static_web_apps(self) -> Optional[outputs.AzureStaticWebAppsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customOpenIdConnectProviders")
    def custom_open_id_connect_providers(self) -> Optional[Mapping[str, outputs.CustomOpenIdConnectProviderResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def facebook(self) -> Optional[outputs.FacebookResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitHub")
    def git_hub(self) -> Optional[outputs.GitHubResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def google(self) -> Optional[outputs.GoogleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def twitter(self) -> Optional[outputs.TwitterResponse]:
        
        ...
    


@pulumi.output_type
class IdentitySettingsResponse(dict):
    
    def __init__(__self__, *, identity: _builtins.str, lifecycle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifecycle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IngressConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, header_count_limit: Optional[_builtins.int] = ..., request_idle_timeout: Optional[_builtins.int] = ..., scale: Optional[outputs.IngressConfigurationResponseScale] = ..., termination_grace_period_seconds: Optional[_builtins.int] = ..., workload_profile_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerCountLimit")
    def header_count_limit(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestIdleTimeout")
    def request_idle_timeout(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[outputs.IngressConfigurationResponseScale]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationGracePeriodSeconds")
    def termination_grace_period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadProfileName")
    def workload_profile_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IngressConfigurationResponseScale(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_replicas: Optional[_builtins.int] = ..., min_replicas: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxReplicas")
    def max_replicas(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minReplicas")
    def min_replicas(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class IngressPortMappingResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external: _builtins.bool, target_port: _builtins.int, exposed_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def external(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPort")
    def target_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposedPort")
    def exposed_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class IngressResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fqdn: _builtins.str, additional_port_mappings: Optional[Sequence[outputs.IngressPortMappingResponse]] = ..., allow_insecure: Optional[_builtins.bool] = ..., client_certificate_mode: Optional[_builtins.str] = ..., cors_policy: Optional[outputs.CorsPolicyResponse] = ..., custom_domains: Optional[Sequence[outputs.CustomDomainResponse]] = ..., exposed_port: Optional[_builtins.int] = ..., external: Optional[_builtins.bool] = ..., ip_security_restrictions: Optional[Sequence[outputs.IpSecurityRestrictionRuleResponse]] = ..., sticky_sessions: Optional[outputs.IngressResponseStickySessions] = ..., target_port: Optional[_builtins.int] = ..., target_port_http_scheme: Optional[_builtins.str] = ..., traffic: Optional[Sequence[outputs.TrafficWeightResponse]] = ..., transport: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalPortMappings")
    def additional_port_mappings(self) -> Optional[Sequence[outputs.IngressPortMappingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateMode")
    def client_certificate_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsPolicy")
    def cors_policy(self) -> Optional[outputs.CorsPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Optional[Sequence[outputs.CustomDomainResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposedPort")
    def exposed_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def external(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSecurityRestrictions")
    def ip_security_restrictions(self) -> Optional[Sequence[outputs.IpSecurityRestrictionRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stickySessions")
    def sticky_sessions(self) -> Optional[outputs.IngressResponseStickySessions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPort")
    def target_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPortHttpScheme")
    def target_port_http_scheme(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def traffic(self) -> Optional[Sequence[outputs.TrafficWeightResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transport(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IngressResponseStickySessions(dict):
    
    def __init__(__self__, *, affinity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def affinity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InitContainerResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, args: Optional[Sequence[_builtins.str]] = ..., command: Optional[Sequence[_builtins.str]] = ..., env: Optional[Sequence[outputs.EnvironmentVarResponse]] = ..., image: Optional[_builtins.str] = ..., image_type: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resources: Optional[outputs.ContainerResourcesResponse] = ..., volume_mounts: Optional[Sequence[outputs.VolumeMountResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def env(self) -> Optional[Sequence[outputs.EnvironmentVarResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[outputs.ContainerResourcesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[Sequence[outputs.VolumeMountResponse]]:
        
        ...
    


@pulumi.output_type
class IpSecurityRestrictionRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: _builtins.str, ip_address_range: _builtins.str, name: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressRange")
    def ip_address_range(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JavaComponentConfigurationPropertyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, property_name: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JavaComponentIngressResponse(dict):
    
    def __init__(__self__, *, fqdn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class JavaComponentPropertiesResponseScale(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_replicas: Optional[_builtins.int] = ..., min_replicas: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxReplicas")
    def max_replicas(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minReplicas")
    def min_replicas(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class JavaComponentServiceBindResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., service_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, replica_timeout: _builtins.int, trigger_type: Optional[_builtins.str] = ..., event_trigger_config: Optional[outputs.JobConfigurationResponseEventTriggerConfig] = ..., identity_settings: Optional[Sequence[outputs.IdentitySettingsResponse]] = ..., manual_trigger_config: Optional[outputs.JobConfigurationResponseManualTriggerConfig] = ..., registries: Optional[Sequence[outputs.RegistryCredentialsResponse]] = ..., replica_retry_limit: Optional[_builtins.int] = ..., schedule_trigger_config: Optional[outputs.JobConfigurationResponseScheduleTriggerConfig] = ..., secrets: Optional[Sequence[outputs.SecretResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaTimeout")
    def replica_timeout(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTriggerConfig")
    def event_trigger_config(self) -> Optional[outputs.JobConfigurationResponseEventTriggerConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identitySettings")
    def identity_settings(self) -> Optional[Sequence[outputs.IdentitySettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualTriggerConfig")
    def manual_trigger_config(self) -> Optional[outputs.JobConfigurationResponseManualTriggerConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registries(self) -> Optional[Sequence[outputs.RegistryCredentialsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaRetryLimit")
    def replica_retry_limit(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleTriggerConfig")
    def schedule_trigger_config(self) -> Optional[outputs.JobConfigurationResponseScheduleTriggerConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[outputs.SecretResponse]]:
        
        ...
    


@pulumi.output_type
class JobConfigurationResponseEventTriggerConfig(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, parallelism: Optional[_builtins.int] = ..., replica_completion_count: Optional[_builtins.int] = ..., scale: Optional[outputs.JobScaleResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCompletionCount")
    def replica_completion_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[outputs.JobScaleResponse]:
        
        ...
    


@pulumi.output_type
class JobConfigurationResponseManualTriggerConfig(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, parallelism: Optional[_builtins.int] = ..., replica_completion_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCompletionCount")
    def replica_completion_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class JobConfigurationResponseScheduleTriggerConfig(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cron_expression: _builtins.str, parallelism: Optional[_builtins.int] = ..., replica_completion_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cronExpression")
    def cron_expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCompletionCount")
    def replica_completion_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class JobScaleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_executions: Optional[_builtins.int] = ..., min_executions: Optional[_builtins.int] = ..., polling_interval: Optional[_builtins.int] = ..., rules: Optional[Sequence[outputs.JobScaleRuleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxExecutions")
    def max_executions(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minExecutions")
    def min_executions(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pollingInterval")
    def polling_interval(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.JobScaleRuleResponse]]:
        
        ...
    


@pulumi.output_type
class JobScaleRuleResponse(dict):
    
    def __init__(__self__, *, auth: Optional[Sequence[outputs.ScaleRuleAuthResponse]] = ..., identity: Optional[_builtins.str] = ..., metadata: Optional[Any] = ..., name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[Sequence[outputs.ScaleRuleAuthResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JobTemplateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, containers: Optional[Sequence[outputs.ContainerResponse]] = ..., init_containers: Optional[Sequence[outputs.InitContainerResponse]] = ..., volumes: Optional[Sequence[outputs.VolumeResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[Sequence[outputs.ContainerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initContainers")
    def init_containers(self) -> Optional[Sequence[outputs.InitContainerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence[outputs.VolumeResponse]]:
        
        ...
    


@pulumi.output_type
class JwtClaimChecksResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_client_applications: Optional[Sequence[_builtins.str]] = ..., allowed_groups: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedClientApplications")
    def allowed_client_applications(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedGroups")
    def allowed_groups(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class KedaConfigurationResponse(dict):
    
    def __init__(__self__, *, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class LifecycleConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cooldown_period_in_seconds: Optional[_builtins.int] = ..., lifecycle_type: Optional[_builtins.str] = ..., max_alive_period_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cooldownPeriodInSeconds")
    def cooldown_period_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleType")
    def lifecycle_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAlivePeriodInSeconds")
    def max_alive_period_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class LogAnalyticsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, customer_id: Optional[_builtins.str] = ..., dynamic_json_columns: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicJsonColumns")
    def dynamic_json_columns(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class LoggerSettingResponse(dict):
    
    def __init__(__self__, *, level: _builtins.str, logger: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logger(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class LoginResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_external_redirect_urls: Optional[Sequence[_builtins.str]] = ..., cookie_expiration: Optional[outputs.CookieExpirationResponse] = ..., nonce: Optional[outputs.NonceResponse] = ..., preserve_url_fragments_for_logins: Optional[_builtins.bool] = ..., routes: Optional[outputs.LoginRoutesResponse] = ..., token_store: Optional[outputs.TokenStoreResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedExternalRedirectUrls")
    def allowed_external_redirect_urls(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookieExpiration")
    def cookie_expiration(self) -> Optional[outputs.CookieExpirationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nonce(self) -> Optional[outputs.NonceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveUrlFragmentsForLogins")
    def preserve_url_fragments_for_logins(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[outputs.LoginRoutesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenStore")
    def token_store(self) -> Optional[outputs.TokenStoreResponse]:
        
        ...
    


@pulumi.output_type
class LoginRoutesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, logout_endpoint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logoutEndpoint")
    def logout_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class LoginScopesResponse(dict):
    
    def __init__(__self__, *, scopes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class LogsConfigurationResponse(dict):
    
    def __init__(__self__, *, destinations: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ManagedCertificateResponseProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error: _builtins.str, provisioning_state: _builtins.str, validation_token: _builtins.str, domain_control_validation: Optional[_builtins.str] = ..., subject_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationToken")
    def validation_token(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainControlValidation")
    def domain_control_validation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedEnvironmentResponseEncryption(dict):
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ManagedEnvironmentResponsePeerAuthentication(dict):
    
    def __init__(__self__, *, mtls: Optional[outputs.MtlsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtls(self) -> Optional[outputs.MtlsResponse]:
        
        ...
    


@pulumi.output_type
class ManagedEnvironmentResponsePeerTrafficConfiguration(dict):
    
    def __init__(__self__, *, encryption: Optional[outputs.ManagedEnvironmentResponseEncryption] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.ManagedEnvironmentResponseEncryption]:
        
        ...
    


@pulumi.output_type
class ManagedEnvironmentStorageResponseProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_file: Optional[outputs.AzureFilePropertiesResponse] = ..., nfs_azure_file: Optional[outputs.NfsAzureFilePropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFile")
    def azure_file(self) -> Optional[outputs.AzureFilePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nfsAzureFile")
    def nfs_azure_file(self) -> Optional[outputs.NfsAzureFilePropertiesResponse]:
        
        ...
    


@pulumi.output_type
class ManagedIdentitySettingResponse(dict):
    
    def __init__(__self__, *, identity: _builtins.str, lifecycle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifecycle(self) -> Optional[_builtins.str]:
        
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
class MetricsConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destinations: Optional[Sequence[_builtins.str]] = ..., include_keda: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeKeda")
    def include_keda(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class MtlsResponse(dict):
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class NacosComponentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, component_type: _builtins.str, provisioning_state: _builtins.str, configurations: Optional[Sequence[outputs.JavaComponentConfigurationPropertyResponse]] = ..., ingress: Optional[outputs.JavaComponentIngressResponse] = ..., scale: Optional[outputs.JavaComponentPropertiesResponseScale] = ..., service_binds: Optional[Sequence[outputs.JavaComponentServiceBindResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence[outputs.JavaComponentConfigurationPropertyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[outputs.JavaComponentIngressResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[outputs.JavaComponentPropertiesResponseScale]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[Sequence[outputs.JavaComponentServiceBindResponse]]:
        
        ...
    


@pulumi.output_type
class NfsAzureFilePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_mode: Optional[_builtins.str] = ..., server: Optional[_builtins.str] = ..., share_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NonceResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, nonce_expiration_interval: Optional[_builtins.str] = ..., validate_nonce: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonceExpirationInterval")
    def nonce_expiration_interval(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateNonce")
    def validate_nonce(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class OpenIdConnectClientCredentialResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_secret_setting_name: Optional[_builtins.str] = ..., method: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OpenIdConnectConfigResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorization_endpoint: Optional[_builtins.str] = ..., certification_uri: Optional[_builtins.str] = ..., issuer: Optional[_builtins.str] = ..., token_endpoint: Optional[_builtins.str] = ..., well_known_open_id_configuration: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificationUri")
    def certification_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wellKnownOpenIdConfiguration")
    def well_known_open_id_configuration(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OpenIdConnectLoginResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name_claim_type: Optional[_builtins.str] = ..., scopes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameClaimType")
    def name_claim_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class OpenIdConnectRegistrationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_credential: Optional[outputs.OpenIdConnectClientCredentialResponse] = ..., client_id: Optional[_builtins.str] = ..., open_id_connect_configuration: Optional[outputs.OpenIdConnectConfigResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCredential")
    def client_credential(self) -> Optional[outputs.OpenIdConnectClientCredentialResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openIdConnectConfiguration")
    def open_id_connect_configuration(self) -> Optional[outputs.OpenIdConnectConfigResponse]:
        
        ...
    


@pulumi.output_type
class OpenTelemetryConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destinations_configuration: Optional[outputs.DestinationsConfigurationResponse] = ..., logs_configuration: Optional[outputs.LogsConfigurationResponse] = ..., metrics_configuration: Optional[outputs.MetricsConfigurationResponse] = ..., traces_configuration: Optional[outputs.TracesConfigurationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationsConfiguration")
    def destinations_configuration(self) -> Optional[outputs.DestinationsConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsConfiguration")
    def logs_configuration(self) -> Optional[outputs.LogsConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsConfiguration")
    def metrics_configuration(self) -> Optional[outputs.MetricsConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tracesConfiguration")
    def traces_configuration(self) -> Optional[outputs.TracesConfigurationResponse]:
        
        ...
    


@pulumi.output_type
class OtlpConfigurationResponse(dict):
    
    def __init__(__self__, *, endpoint: Optional[_builtins.str] = ..., headers: Optional[Sequence[outputs.HeaderResponse]] = ..., insecure: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.HeaderResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def insecure(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreBuildStepResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., http_get: Optional[outputs.HttpGetResponse] = ..., scripts: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[outputs.HttpGetResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scripts(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_ids: Sequence[_builtins.str], id: _builtins.str, name: _builtins.str, private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse, provisioning_state: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]:
        
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
class QueueScaleRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_name: Optional[_builtins.str] = ..., auth: Optional[Sequence[outputs.ScaleRuleAuthResponse]] = ..., identity: Optional[_builtins.str] = ..., queue_length: Optional[_builtins.int] = ..., queue_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[Sequence[outputs.ScaleRuleAuthResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueLength")
    def queue_length(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RegistryCredentialsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity: Optional[_builtins.str] = ..., password_secret_ref: Optional[_builtins.str] = ..., server: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSecretRef")
    def password_secret_ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RegistryInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, registry_url: Optional[_builtins.str] = ..., registry_user_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryUrl")
    def registry_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryUserName")
    def registry_user_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuntimeResponse(dict):
    
    def __init__(__self__, *, dotnet: Optional[outputs.RuntimeResponseDotnet] = ..., java: Optional[outputs.RuntimeResponseJava] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dotnet(self) -> Optional[outputs.RuntimeResponseDotnet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def java(self) -> Optional[outputs.RuntimeResponseJava]:
        
        ...
    


@pulumi.output_type
class RuntimeResponseDotnet(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto_configure_data_protection: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoConfigureDataProtection")
    def auto_configure_data_protection(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RuntimeResponseJava(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_metrics: Optional[_builtins.bool] = ..., java_agent: Optional[outputs.RuntimeResponseJavaAgent] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMetrics")
    def enable_metrics(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="javaAgent")
    def java_agent(self) -> Optional[outputs.RuntimeResponseJavaAgent]:
        
        ...
    


@pulumi.output_type
class RuntimeResponseJavaAgent(dict):
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., logging: Optional[outputs.RuntimeResponseLogging] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[outputs.RuntimeResponseLogging]:
        
        ...
    


@pulumi.output_type
class RuntimeResponseLogging(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, logger_settings: Optional[Sequence[outputs.LoggerSettingResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggerSettings")
    def logger_settings(self) -> Optional[Sequence[outputs.LoggerSettingResponse]]:
        
        ...
    


@pulumi.output_type
class ScaleConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_concurrent_sessions: Optional[_builtins.int] = ..., ready_session_instances: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentSessions")
    def max_concurrent_sessions(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readySessionInstances")
    def ready_session_instances(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ScaleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cooldown_period: Optional[_builtins.int] = ..., max_replicas: Optional[_builtins.int] = ..., min_replicas: Optional[_builtins.int] = ..., polling_interval: Optional[_builtins.int] = ..., rules: Optional[Sequence[outputs.ScaleRuleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cooldownPeriod")
    def cooldown_period(self) -> Optional[_builtins.int]:
        
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
    @pulumi.getter(name="pollingInterval")
    def polling_interval(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[Sequence[outputs.ScaleRuleResponse]]:
        
        ...
    


@pulumi.output_type
class ScaleRuleAuthResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, secret_ref: Optional[_builtins.str] = ..., trigger_parameter: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerParameter")
    def trigger_parameter(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ScaleRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_queue: Optional[outputs.QueueScaleRuleResponse] = ..., custom: Optional[outputs.CustomScaleRuleResponse] = ..., http: Optional[outputs.HttpScaleRuleResponse] = ..., name: Optional[_builtins.str] = ..., tcp: Optional[outputs.TcpScaleRuleResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureQueue")
    def azure_queue(self) -> Optional[outputs.QueueScaleRuleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def custom(self) -> Optional[outputs.CustomScaleRuleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def http(self) -> Optional[outputs.HttpScaleRuleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tcp(self) -> Optional[outputs.TcpScaleRuleResponse]:
        
        ...
    


@pulumi.output_type
class ScgRouteResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, uri: _builtins.str, filters: Optional[Sequence[_builtins.str]] = ..., order: Optional[_builtins.float] = ..., predicates: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def predicates(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ScheduledEntryResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, duration_hours: _builtins.int, start_hour_utc: _builtins.int, week_day: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationHours")
    def duration_hours(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startHourUtc")
    def start_hour_utc(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekDay")
    def week_day(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SecretKeyVaultPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity: Optional[_builtins.str] = ..., key_vault_url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecretResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity: Optional[_builtins.str] = ..., key_vault_url: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecretVolumeItemResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, path: Optional[_builtins.str] = ..., secret_ref: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceBindResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_type: Optional[_builtins.str] = ..., customized_keys: Optional[Mapping[str, _builtins.str]] = ..., name: Optional[_builtins.str] = ..., service_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientType")
    def client_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customizedKeys")
    def customized_keys(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceResponse(dict):
    
    def __init__(__self__, *, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SessionContainerResourcesResponse(dict):
    
    def __init__(__self__, *, cpu: Optional[_builtins.float] = ..., memory: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SessionContainerResponse(dict):
    
    def __init__(__self__, *, args: Optional[Sequence[_builtins.str]] = ..., command: Optional[Sequence[_builtins.str]] = ..., env: Optional[Sequence[outputs.EnvironmentVarResponse]] = ..., image: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., probes: Optional[Sequence[outputs.SessionProbeResponse]] = ..., resources: Optional[outputs.SessionContainerResourcesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def env(self) -> Optional[Sequence[outputs.EnvironmentVarResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def probes(self) -> Optional[Sequence[outputs.SessionProbeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[outputs.SessionContainerResourcesResponse]:
        
        ...
    


@pulumi.output_type
class SessionIngressResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPort")
    def target_port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SessionNetworkConfigurationResponse(dict):
    
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SessionPoolSecretResponse(dict):
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SessionProbeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_threshold: Optional[_builtins.int] = ..., http_get: Optional[outputs.SessionProbeResponseHttpGet] = ..., initial_delay_seconds: Optional[_builtins.int] = ..., period_seconds: Optional[_builtins.int] = ..., success_threshold: Optional[_builtins.int] = ..., tcp_socket: Optional[outputs.SessionProbeResponseTcpSocket] = ..., termination_grace_period_seconds: Optional[_builtins.float] = ..., timeout_seconds: Optional[_builtins.int] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[outputs.SessionProbeResponseHttpGet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(self) -> Optional[outputs.SessionProbeResponseTcpSocket]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationGracePeriodSeconds")
    def termination_grace_period_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SessionProbeResponseHttpGet(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, port: _builtins.int, host: Optional[_builtins.str] = ..., http_headers: Optional[Sequence[outputs.SessionProbeResponseHttpHeaders]] = ..., path: Optional[_builtins.str] = ..., scheme: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[Sequence[outputs.SessionProbeResponseHttpHeaders]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SessionProbeResponseHttpHeaders(dict):
    
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SessionProbeResponseTcpSocket(dict):
    
    def __init__(__self__, *, port: _builtins.int, host: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SessionRegistryCredentialsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity: Optional[_builtins.str] = ..., password_secret_ref: Optional[_builtins.str] = ..., server: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSecretRef")
    def password_secret_ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SmbStorageResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_mode: Optional[_builtins.str] = ..., domain: Optional[_builtins.str] = ..., host: Optional[_builtins.str] = ..., password: Optional[_builtins.str] = ..., share_name: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SpringBootAdminComponentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, component_type: _builtins.str, provisioning_state: _builtins.str, configurations: Optional[Sequence[outputs.JavaComponentConfigurationPropertyResponse]] = ..., ingress: Optional[outputs.JavaComponentIngressResponse] = ..., scale: Optional[outputs.JavaComponentPropertiesResponseScale] = ..., service_binds: Optional[Sequence[outputs.JavaComponentServiceBindResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence[outputs.JavaComponentConfigurationPropertyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[outputs.JavaComponentIngressResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[outputs.JavaComponentPropertiesResponseScale]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[Sequence[outputs.JavaComponentServiceBindResponse]]:
        
        ...
    


@pulumi.output_type
class SpringCloudConfigComponentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, component_type: _builtins.str, provisioning_state: _builtins.str, configurations: Optional[Sequence[outputs.JavaComponentConfigurationPropertyResponse]] = ..., scale: Optional[outputs.JavaComponentPropertiesResponseScale] = ..., service_binds: Optional[Sequence[outputs.JavaComponentServiceBindResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence[outputs.JavaComponentConfigurationPropertyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[outputs.JavaComponentPropertiesResponseScale]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[Sequence[outputs.JavaComponentServiceBindResponse]]:
        
        ...
    


@pulumi.output_type
class SpringCloudEurekaComponentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, component_type: _builtins.str, provisioning_state: _builtins.str, configurations: Optional[Sequence[outputs.JavaComponentConfigurationPropertyResponse]] = ..., ingress: Optional[outputs.JavaComponentIngressResponse] = ..., scale: Optional[outputs.JavaComponentPropertiesResponseScale] = ..., service_binds: Optional[Sequence[outputs.JavaComponentServiceBindResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence[outputs.JavaComponentConfigurationPropertyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[outputs.JavaComponentIngressResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[outputs.JavaComponentPropertiesResponseScale]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[Sequence[outputs.JavaComponentServiceBindResponse]]:
        
        ...
    


@pulumi.output_type
class SpringCloudGatewayComponentResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, component_type: _builtins.str, provisioning_state: _builtins.str, configurations: Optional[Sequence[outputs.JavaComponentConfigurationPropertyResponse]] = ..., ingress: Optional[outputs.JavaComponentIngressResponse] = ..., scale: Optional[outputs.JavaComponentPropertiesResponseScale] = ..., service_binds: Optional[Sequence[outputs.JavaComponentServiceBindResponse]] = ..., spring_cloud_gateway_routes: Optional[Sequence[outputs.ScgRouteResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[Sequence[outputs.JavaComponentConfigurationPropertyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[outputs.JavaComponentIngressResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[outputs.JavaComponentPropertiesResponseScale]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[Sequence[outputs.JavaComponentServiceBindResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="springCloudGatewayRoutes")
    def spring_cloud_gateway_routes(self) -> Optional[Sequence[outputs.ScgRouteResponse]]:
        
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
class TcpConnectionPoolResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_connections: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class TcpRetryPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_connect_attempts: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConnectAttempts")
    def max_connect_attempts(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class TcpScaleRuleResponse(dict):
    
    def __init__(__self__, *, auth: Optional[Sequence[outputs.ScaleRuleAuthResponse]] = ..., identity: Optional[_builtins.str] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[Sequence[outputs.ScaleRuleAuthResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class TemplateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, containers: Optional[Sequence[outputs.ContainerResponse]] = ..., init_containers: Optional[Sequence[outputs.InitContainerResponse]] = ..., revision_suffix: Optional[_builtins.str] = ..., scale: Optional[outputs.ScaleResponse] = ..., service_binds: Optional[Sequence[outputs.ServiceBindResponse]] = ..., termination_grace_period_seconds: Optional[_builtins.float] = ..., volumes: Optional[Sequence[outputs.VolumeResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[Sequence[outputs.ContainerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initContainers")
    def init_containers(self) -> Optional[Sequence[outputs.InitContainerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionSuffix")
    def revision_suffix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[outputs.ScaleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[Sequence[outputs.ServiceBindResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationGracePeriodSeconds")
    def termination_grace_period_seconds(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence[outputs.VolumeResponse]]:
        
        ...
    


@pulumi.output_type
class TimeoutPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connection_timeout_in_seconds: Optional[_builtins.int] = ..., response_timeout_in_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTimeoutInSeconds")
    def connection_timeout_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseTimeoutInSeconds")
    def response_timeout_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class TokenStoreResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, azure_blob_storage: Optional[outputs.BlobStorageTokenStoreResponse] = ..., enabled: Optional[_builtins.bool] = ..., token_refresh_extension_hours: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBlobStorage")
    def azure_blob_storage(self) -> Optional[outputs.BlobStorageTokenStoreResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenRefreshExtensionHours")
    def token_refresh_extension_hours(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class TracesConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destinations: Optional[Sequence[_builtins.str]] = ..., include_dapr: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeDapr")
    def include_dapr(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class TrafficWeightResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, label: Optional[_builtins.str] = ..., latest_revision: Optional[_builtins.bool] = ..., revision_name: Optional[_builtins.str] = ..., weight: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestRevision")
    def latest_revision(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionName")
    def revision_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class TwitterRegistrationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, consumer_key: Optional[_builtins.str] = ..., consumer_secret_setting_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerKey")
    def consumer_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerSecretSettingName")
    def consumer_secret_setting_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TwitterResponse(dict):
    
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ..., registration: Optional[outputs.TwitterRegistrationResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[outputs.TwitterRegistrationResponse]:
        
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
class VnetConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, docker_bridge_cidr: Optional[_builtins.str] = ..., infrastructure_subnet_id: Optional[_builtins.str] = ..., internal: Optional[_builtins.bool] = ..., platform_reserved_cidr: Optional[_builtins.str] = ..., platform_reserved_dns_ip: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerBridgeCidr")
    def docker_bridge_cidr(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureSubnetId")
    def infrastructure_subnet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def internal(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformReservedCidr")
    def platform_reserved_cidr(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformReservedDnsIP")
    def platform_reserved_dns_ip(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VolumeMountResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mount_path: Optional[_builtins.str] = ..., sub_path: Optional[_builtins.str] = ..., volume_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class VolumeResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mount_options: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., secrets: Optional[Sequence[outputs.SecretVolumeItemResponse]] = ..., storage_name: Optional[_builtins.str] = ..., storage_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[outputs.SecretVolumeItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageName")
    def storage_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowEnvelopeResponseProperties(dict):
    
    def __init__(__self__, *, files: Optional[Any] = ..., flow_state: Optional[_builtins.str] = ..., health: Optional[outputs.WorkflowHealthResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def files(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowState")
    def flow_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> Optional[outputs.WorkflowHealthResponse]:
        
        ...
    


@pulumi.output_type
class WorkflowHealthResponse(dict):
    
    def __init__(__self__, *, state: _builtins.str, error: Optional[outputs.ErrorEntityResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[outputs.ErrorEntityResponse]:
        
        ...
    


@pulumi.output_type
class WorkloadProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, workload_profile_type: _builtins.str, enable_fips: Optional[_builtins.bool] = ..., maximum_count: Optional[_builtins.int] = ..., minimum_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadProfileType")
    def workload_profile_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFips")
    def enable_fips(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumCount")
    def maximum_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumCount")
    def minimum_count(self) -> Optional[_builtins.int]:
        
        ...
    


