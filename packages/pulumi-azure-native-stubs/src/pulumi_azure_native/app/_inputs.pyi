

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AllowedAudiencesValidationArgs', 'AllowedAudiencesValidationArgsDict', 'AllowedPrincipalsArgs', 'AllowedPrincipalsArgsDict', 'AppInsightsConfigurationArgs', 'AppInsightsConfigurationArgsDict', 'AppLogsConfigurationArgs', 'AppLogsConfigurationArgsDict', 'AppRegistrationArgs', 'AppRegistrationArgsDict', 'AppleRegistrationArgs', 'AppleRegistrationArgsDict', 'AppleArgs', 'AppleArgsDict', 'AuthPlatformArgs', 'AuthPlatformArgsDict', 'AzureActiveDirectoryLoginArgs', 'AzureActiveDirectoryLoginArgsDict', 'AzureActiveDirectoryRegistrationArgs', 'AzureActiveDirectoryRegistrationArgsDict', 'AzureActiveDirectoryValidationArgs', 'AzureActiveDirectoryValidationArgsDict', 'AzureActiveDirectoryArgs', 'AzureActiveDirectoryArgsDict', 'AzureCredentialsArgs', 'AzureCredentialsArgsDict', 'AzureFilePropertiesArgs', 'AzureFilePropertiesArgsDict', 'AzureStaticWebAppsRegistrationArgs', 'AzureStaticWebAppsRegistrationArgsDict', 'AzureStaticWebAppsArgs', 'AzureStaticWebAppsArgsDict', 'BlobStorageTokenStoreArgs', 'BlobStorageTokenStoreArgsDict', 'BuildConfigurationArgs', 'BuildConfigurationArgsDict', 'CertificateKeyVaultPropertiesArgs', 'CertificateKeyVaultPropertiesArgsDict', 'CertificatePropertiesArgs', 'CertificatePropertiesArgsDict', 'CircuitBreakerPolicyArgs', 'CircuitBreakerPolicyArgsDict', 'ClientRegistrationArgs', 'ClientRegistrationArgsDict', 'ConfigurationArgs', 'ConfigurationArgsDict', 'ConnectedEnvironmentStoragePropertiesArgs', 'ConnectedEnvironmentStoragePropertiesArgsDict', 'ContainerAppPatchingConfigurationArgs', 'ContainerAppPatchingConfigurationArgsDict', 'ContainerAppProbeHttpGetArgs', 'ContainerAppProbeHttpGetArgsDict', 'ContainerAppProbeHttpHeadersArgs', 'ContainerAppProbeHttpHeadersArgsDict', 'ContainerAppProbeTcpSocketArgs', 'ContainerAppProbeTcpSocketArgsDict', 'ContainerAppProbeArgs', 'ContainerAppProbeArgsDict', 'ContainerRegistryWithCustomImageArgs', 'ContainerRegistryWithCustomImageArgsDict', 'ContainerRegistryArgs', 'ContainerRegistryArgsDict', 'ContainerResourcesArgs', 'ContainerResourcesArgsDict', 'ContainerArgs', 'ContainerArgsDict', 'CookieExpirationArgs', 'CookieExpirationArgsDict', 'CorsPolicyArgs', 'CorsPolicyArgsDict', 'CustomContainerTemplateArgs', 'CustomContainerTemplateArgsDict', 'CustomDomainConfigurationArgs', 'CustomDomainConfigurationArgsDict', 'CustomDomainArgs', 'CustomDomainArgsDict', 'CustomOpenIdConnectProviderArgs', 'CustomOpenIdConnectProviderArgsDict', 'CustomScaleRuleArgs', 'CustomScaleRuleArgsDict', 'DaprAppHealthArgs', 'DaprAppHealthArgsDict', ..., ..., 'DaprComponentResiliencyPolicyConfigurationArgs', 'DaprComponentResiliencyPolicyConfigurationArgsDict', ..., ..., ..., ..., ..., ..., 'DaprComponentServiceBindingArgs', 'DaprComponentServiceBindingArgsDict', 'DaprMetadataArgs', 'DaprMetadataArgsDict', 'DaprServiceBindMetadataArgs', 'DaprServiceBindMetadataArgsDict', 'DaprSubscriptionBulkSubscribeOptionsArgs', 'DaprSubscriptionBulkSubscribeOptionsArgsDict', 'DaprSubscriptionRouteRuleArgs', 'DaprSubscriptionRouteRuleArgsDict', 'DaprSubscriptionRoutesArgs', 'DaprSubscriptionRoutesArgsDict', 'DaprArgs', 'DaprArgsDict', 'DataDogConfigurationArgs', 'DataDogConfigurationArgsDict', 'DefaultAuthorizationPolicyArgs', 'DefaultAuthorizationPolicyArgsDict', 'DestinationsConfigurationArgs', 'DestinationsConfigurationArgsDict', 'DiskEncryptionConfigurationAuthArgs', 'DiskEncryptionConfigurationAuthArgsDict', ..., ..., 'DiskEncryptionConfigurationArgs', 'DiskEncryptionConfigurationArgsDict', 'DotNetComponentConfigurationPropertyArgs', 'DotNetComponentConfigurationPropertyArgsDict', 'DotNetComponentServiceBindArgs', 'DotNetComponentServiceBindArgsDict', 'DynamicPoolConfigurationArgs', 'DynamicPoolConfigurationArgsDict', 'EncryptionSettingsArgs', 'EncryptionSettingsArgsDict', 'EnvironmentVariableArgs', 'EnvironmentVariableArgsDict', 'EnvironmentVarArgs', 'EnvironmentVarArgsDict', 'ExtendedLocationArgs', 'ExtendedLocationArgsDict', 'FacebookArgs', 'FacebookArgsDict', 'ForwardProxyArgs', 'ForwardProxyArgsDict', 'GitHubArgs', 'GitHubArgsDict', 'GithubActionConfigurationArgs', 'GithubActionConfigurationArgsDict', 'GlobalValidationArgs', 'GlobalValidationArgsDict', 'GoogleArgs', 'GoogleArgsDict', 'HeaderMatchArgs', 'HeaderMatchArgsDict', 'HeaderArgs', 'HeaderArgsDict', 'HttpConnectionPoolArgs', 'HttpConnectionPoolArgsDict', 'HttpGetArgs', 'HttpGetArgsDict', 'HttpRetryPolicyArgs', 'HttpRetryPolicyArgsDict', 'HttpRouteActionArgs', 'HttpRouteActionArgsDict', 'HttpRouteConfigPropertiesArgs', 'HttpRouteConfigPropertiesArgsDict', 'HttpRouteMatchArgs', 'HttpRouteMatchArgsDict', 'HttpRouteRuleArgs', 'HttpRouteRuleArgsDict', 'HttpRouteTargetArgs', 'HttpRouteTargetArgsDict', 'HttpRouteArgs', 'HttpRouteArgsDict', 'HttpScaleRuleArgs', 'HttpScaleRuleArgsDict', 'HttpSettingsRoutesArgs', 'HttpSettingsRoutesArgsDict', 'HttpSettingsArgs', 'HttpSettingsArgsDict', 'IdentityProvidersArgs', 'IdentityProvidersArgsDict', 'IdentitySettingsArgs', 'IdentitySettingsArgsDict', 'IngressConfigurationScaleArgs', 'IngressConfigurationScaleArgsDict', 'IngressConfigurationArgs', 'IngressConfigurationArgsDict', 'IngressPortMappingArgs', 'IngressPortMappingArgsDict', 'IngressStickySessionsArgs', 'IngressStickySessionsArgsDict', 'IngressArgs', 'IngressArgsDict', 'InitContainerArgs', 'InitContainerArgsDict', 'IpSecurityRestrictionRuleArgs', 'IpSecurityRestrictionRuleArgsDict', 'JavaComponentConfigurationPropertyArgs', 'JavaComponentConfigurationPropertyArgsDict', 'JavaComponentPropertiesScaleArgs', 'JavaComponentPropertiesScaleArgsDict', 'JavaComponentServiceBindArgs', 'JavaComponentServiceBindArgsDict', 'JobConfigurationEventTriggerConfigArgs', 'JobConfigurationEventTriggerConfigArgsDict', 'JobConfigurationManualTriggerConfigArgs', 'JobConfigurationManualTriggerConfigArgsDict', 'JobConfigurationScheduleTriggerConfigArgs', 'JobConfigurationScheduleTriggerConfigArgsDict', 'JobConfigurationArgs', 'JobConfigurationArgsDict', 'JobScaleRuleArgs', 'JobScaleRuleArgsDict', 'JobScaleArgs', 'JobScaleArgsDict', 'JobTemplateArgs', 'JobTemplateArgsDict', 'JwtClaimChecksArgs', 'JwtClaimChecksArgsDict', 'LifecycleConfigurationArgs', 'LifecycleConfigurationArgsDict', 'LogAnalyticsConfigurationArgs', 'LogAnalyticsConfigurationArgsDict', 'LoggerSettingArgs', 'LoggerSettingArgsDict', 'LoginRoutesArgs', 'LoginRoutesArgsDict', 'LoginScopesArgs', 'LoginScopesArgsDict', 'LoginArgs', 'LoginArgsDict', 'LogsConfigurationArgs', 'LogsConfigurationArgsDict', 'ManagedCertificatePropertiesArgs', 'ManagedCertificatePropertiesArgsDict', 'ManagedEnvironmentEncryptionArgs', 'ManagedEnvironmentEncryptionArgsDict', 'ManagedEnvironmentPeerAuthenticationArgs', 'ManagedEnvironmentPeerAuthenticationArgsDict', 'ManagedEnvironmentPeerTrafficConfigurationArgs', 'ManagedEnvironmentPeerTrafficConfigurationArgsDict', 'ManagedEnvironmentStoragePropertiesArgs', 'ManagedEnvironmentStoragePropertiesArgsDict', 'ManagedIdentitySettingArgs', 'ManagedIdentitySettingArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'MetricsConfigurationArgs', 'MetricsConfigurationArgsDict', 'MtlsArgs', 'MtlsArgsDict', 'NacosComponentArgs', 'NacosComponentArgsDict', 'NfsAzureFilePropertiesArgs', 'NfsAzureFilePropertiesArgsDict', 'NonceArgs', 'NonceArgsDict', 'OpenIdConnectClientCredentialArgs', 'OpenIdConnectClientCredentialArgsDict', 'OpenIdConnectConfigArgs', 'OpenIdConnectConfigArgsDict', 'OpenIdConnectLoginArgs', 'OpenIdConnectLoginArgsDict', 'OpenIdConnectRegistrationArgs', 'OpenIdConnectRegistrationArgsDict', 'OpenTelemetryConfigurationArgs', 'OpenTelemetryConfigurationArgsDict', 'OtlpConfigurationArgs', 'OtlpConfigurationArgsDict', 'PreBuildStepArgs', 'PreBuildStepArgsDict', 'PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict', 'QueueScaleRuleArgs', 'QueueScaleRuleArgsDict', 'RegistryCredentialsArgs', 'RegistryCredentialsArgsDict', 'RegistryInfoArgs', 'RegistryInfoArgsDict', 'RuntimeDotnetArgs', 'RuntimeDotnetArgsDict', 'RuntimeJavaAgentArgs', 'RuntimeJavaAgentArgsDict', 'RuntimeJavaArgs', 'RuntimeJavaArgsDict', 'RuntimeLoggingArgs', 'RuntimeLoggingArgsDict', 'RuntimeArgs', 'RuntimeArgsDict', 'ScaleConfigurationArgs', 'ScaleConfigurationArgsDict', 'ScaleRuleAuthArgs', 'ScaleRuleAuthArgsDict', 'ScaleRuleArgs', 'ScaleRuleArgsDict', 'ScaleArgs', 'ScaleArgsDict', 'ScgRouteArgs', 'ScgRouteArgsDict', 'ScheduledEntryArgs', 'ScheduledEntryArgsDict', 'SecretKeyVaultPropertiesArgs', 'SecretKeyVaultPropertiesArgsDict', 'SecretVolumeItemArgs', 'SecretVolumeItemArgsDict', 'SecretArgs', 'SecretArgsDict', 'ServiceBindArgs', 'ServiceBindArgsDict', 'ServiceArgs', 'ServiceArgsDict', 'SessionContainerResourcesArgs', 'SessionContainerResourcesArgsDict', 'SessionContainerArgs', 'SessionContainerArgsDict', 'SessionIngressArgs', 'SessionIngressArgsDict', 'SessionNetworkConfigurationArgs', 'SessionNetworkConfigurationArgsDict', 'SessionPoolSecretArgs', 'SessionPoolSecretArgsDict', 'SessionProbeHttpGetArgs', 'SessionProbeHttpGetArgsDict', 'SessionProbeHttpHeadersArgs', 'SessionProbeHttpHeadersArgsDict', 'SessionProbeTcpSocketArgs', 'SessionProbeTcpSocketArgsDict', 'SessionProbeArgs', 'SessionProbeArgsDict', 'SessionRegistryCredentialsArgs', 'SessionRegistryCredentialsArgsDict', 'SmbStorageArgs', 'SmbStorageArgsDict', 'SpringBootAdminComponentArgs', 'SpringBootAdminComponentArgsDict', 'SpringCloudConfigComponentArgs', 'SpringCloudConfigComponentArgsDict', 'SpringCloudEurekaComponentArgs', 'SpringCloudEurekaComponentArgsDict', 'SpringCloudGatewayComponentArgs', 'SpringCloudGatewayComponentArgsDict', 'TcpConnectionPoolArgs', 'TcpConnectionPoolArgsDict', 'TcpRetryPolicyArgs', 'TcpRetryPolicyArgsDict', 'TcpScaleRuleArgs', 'TcpScaleRuleArgsDict', 'TemplateArgs', 'TemplateArgsDict', 'TimeoutPolicyArgs', 'TimeoutPolicyArgsDict', 'TokenStoreArgs', 'TokenStoreArgsDict', 'TracesConfigurationArgs', 'TracesConfigurationArgsDict', 'TrafficWeightArgs', 'TrafficWeightArgsDict', 'TwitterRegistrationArgs', 'TwitterRegistrationArgsDict', 'TwitterArgs', 'TwitterArgsDict', 'VnetConfigurationArgs', 'VnetConfigurationArgsDict', 'VolumeMountArgs', 'VolumeMountArgsDict', 'VolumeArgs', 'VolumeArgsDict', 'WorkloadProfileArgs', 'WorkloadProfileArgsDict']
class AllowedAudiencesValidationArgsDict(TypedDict):
    
    allowed_audiences: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AllowedAudiencesValidationArgs:
    def __init__(__self__, *, allowed_audiences: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_audiences.setter
    def allowed_audiences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AllowedPrincipalsArgsDict(TypedDict):
    
    groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AllowedPrincipalsArgs:
    def __init__(__self__, *, groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @groups.setter
    def groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @identities.setter
    def identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AppInsightsConfigurationArgsDict(TypedDict):
    
    connection_string: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppInsightsConfigurationArgs:
    def __init__(__self__, *, connection_string: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_string.setter
    def connection_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AppLogsConfigurationArgsDict(TypedDict):
    
    destination: NotRequired[pulumi.Input[_builtins.str]]
    log_analytics_configuration: NotRequired[pulumi.Input[LogAnalyticsConfigurationArgsDict]]


@pulumi.input_type
class AppLogsConfigurationArgs:
    def __init__(__self__, *, destination: Optional[pulumi.Input[_builtins.str]] = ..., log_analytics_configuration: Optional[pulumi.Input[LogAnalyticsConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logAnalyticsConfiguration")
    def log_analytics_configuration(self) -> Optional[pulumi.Input[LogAnalyticsConfigurationArgs]]:
        
        ...
    
    @log_analytics_configuration.setter
    def log_analytics_configuration(self, value: Optional[pulumi.Input[LogAnalyticsConfigurationArgs]]): # -> None:
        ...
    


class AppRegistrationArgsDict(TypedDict):
    
    app_id: NotRequired[pulumi.Input[_builtins.str]]
    app_secret_setting_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppRegistrationArgs:
    def __init__(__self__, *, app_id: Optional[pulumi.Input[_builtins.str]] = ..., app_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSecretSettingName")
    def app_secret_setting_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_secret_setting_name.setter
    def app_secret_setting_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AppleRegistrationArgsDict(TypedDict):
    
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_setting_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppleRegistrationArgs:
    def __init__(__self__, *, client_id: Optional[pulumi.Input[_builtins.str]] = ..., client_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AppleArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    login: NotRequired[pulumi.Input[LoginScopesArgsDict]]
    registration: NotRequired[pulumi.Input[AppleRegistrationArgsDict]]


@pulumi.input_type
class AppleArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., login: Optional[pulumi.Input[LoginScopesArgs]] = ..., registration: Optional[pulumi.Input[AppleRegistrationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[LoginScopesArgs]]:
        
        ...
    
    @login.setter
    def login(self, value: Optional[pulumi.Input[LoginScopesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[pulumi.Input[AppleRegistrationArgs]]:
        
        ...
    
    @registration.setter
    def registration(self, value: Optional[pulumi.Input[AppleRegistrationArgs]]): # -> None:
        ...
    


class AuthPlatformArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    runtime_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AuthPlatformArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., runtime_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_version.setter
    def runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AzureActiveDirectoryLoginArgsDict(TypedDict):
    
    disable_www_authenticate: NotRequired[pulumi.Input[_builtins.bool]]
    login_parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class AzureActiveDirectoryLoginArgs:
    def __init__(__self__, *, disable_www_authenticate: Optional[pulumi.Input[_builtins.bool]] = ..., login_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableWWWAuthenticate")
    def disable_www_authenticate(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_www_authenticate.setter
    def disable_www_authenticate(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginParameters")
    def login_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @login_parameters.setter
    def login_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class AzureActiveDirectoryRegistrationArgsDict(TypedDict):
    
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_certificate_issuer: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_certificate_subject_alternative_name: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_certificate_thumbprint: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_setting_name: NotRequired[pulumi.Input[_builtins.str]]
    open_id_issuer: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AzureActiveDirectoryRegistrationArgs:
    def __init__(__self__, *, client_id: Optional[pulumi.Input[_builtins.str]] = ..., client_secret_certificate_issuer: Optional[pulumi.Input[_builtins.str]] = ..., client_secret_certificate_subject_alternative_name: Optional[pulumi.Input[_builtins.str]] = ..., client_secret_certificate_thumbprint: Optional[pulumi.Input[_builtins.str]] = ..., client_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ..., open_id_issuer: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretCertificateIssuer")
    def client_secret_certificate_issuer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret_certificate_issuer.setter
    def client_secret_certificate_issuer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretCertificateSubjectAlternativeName")
    def client_secret_certificate_subject_alternative_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret_certificate_subject_alternative_name.setter
    def client_secret_certificate_subject_alternative_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretCertificateThumbprint")
    def client_secret_certificate_thumbprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret_certificate_thumbprint.setter
    def client_secret_certificate_thumbprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openIdIssuer")
    def open_id_issuer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @open_id_issuer.setter
    def open_id_issuer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AzureActiveDirectoryValidationArgsDict(TypedDict):
    
    allowed_audiences: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    default_authorization_policy: NotRequired[pulumi.Input[DefaultAuthorizationPolicyArgsDict]]
    jwt_claim_checks: NotRequired[pulumi.Input[JwtClaimChecksArgsDict]]


@pulumi.input_type
class AzureActiveDirectoryValidationArgs:
    def __init__(__self__, *, allowed_audiences: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., default_authorization_policy: Optional[pulumi.Input[DefaultAuthorizationPolicyArgs]] = ..., jwt_claim_checks: Optional[pulumi.Input[JwtClaimChecksArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_audiences.setter
    def allowed_audiences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAuthorizationPolicy")
    def default_authorization_policy(self) -> Optional[pulumi.Input[DefaultAuthorizationPolicyArgs]]:
        
        ...
    
    @default_authorization_policy.setter
    def default_authorization_policy(self, value: Optional[pulumi.Input[DefaultAuthorizationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwtClaimChecks")
    def jwt_claim_checks(self) -> Optional[pulumi.Input[JwtClaimChecksArgs]]:
        
        ...
    
    @jwt_claim_checks.setter
    def jwt_claim_checks(self, value: Optional[pulumi.Input[JwtClaimChecksArgs]]): # -> None:
        ...
    


class AzureActiveDirectoryArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_auto_provisioned: NotRequired[pulumi.Input[_builtins.bool]]
    login: NotRequired[pulumi.Input[AzureActiveDirectoryLoginArgsDict]]
    registration: NotRequired[pulumi.Input[AzureActiveDirectoryRegistrationArgsDict]]
    validation: NotRequired[pulumi.Input[AzureActiveDirectoryValidationArgsDict]]


@pulumi.input_type
class AzureActiveDirectoryArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., is_auto_provisioned: Optional[pulumi.Input[_builtins.bool]] = ..., login: Optional[pulumi.Input[AzureActiveDirectoryLoginArgs]] = ..., registration: Optional[pulumi.Input[AzureActiveDirectoryRegistrationArgs]] = ..., validation: Optional[pulumi.Input[AzureActiveDirectoryValidationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAutoProvisioned")
    def is_auto_provisioned(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_auto_provisioned.setter
    def is_auto_provisioned(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[AzureActiveDirectoryLoginArgs]]:
        
        ...
    
    @login.setter
    def login(self, value: Optional[pulumi.Input[AzureActiveDirectoryLoginArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[pulumi.Input[AzureActiveDirectoryRegistrationArgs]]:
        
        ...
    
    @registration.setter
    def registration(self, value: Optional[pulumi.Input[AzureActiveDirectoryRegistrationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def validation(self) -> Optional[pulumi.Input[AzureActiveDirectoryValidationArgs]]:
        
        ...
    
    @validation.setter
    def validation(self, value: Optional[pulumi.Input[AzureActiveDirectoryValidationArgs]]): # -> None:
        ...
    


class AzureCredentialsArgsDict(TypedDict):
    
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    kind: NotRequired[pulumi.Input[_builtins.str]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AzureCredentialsArgs:
    def __init__(__self__, *, client_id: Optional[pulumi.Input[_builtins.str]] = ..., client_secret: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AzureFilePropertiesArgsDict(TypedDict):
    
    access_mode: NotRequired[pulumi.Input[Union[_builtins.str, AccessMode]]]
    account_key: NotRequired[pulumi.Input[_builtins.str]]
    account_key_vault_properties: NotRequired[pulumi.Input[SecretKeyVaultPropertiesArgsDict]]
    account_name: NotRequired[pulumi.Input[_builtins.str]]
    share_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AzureFilePropertiesArgs:
    def __init__(__self__, *, access_mode: Optional[pulumi.Input[Union[_builtins.str, AccessMode]]] = ..., account_key: Optional[pulumi.Input[_builtins.str]] = ..., account_key_vault_properties: Optional[pulumi.Input[SecretKeyVaultPropertiesArgs]] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., share_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AccessMode]]]:
        
        ...
    
    @access_mode.setter
    def access_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, AccessMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_key.setter
    def account_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKeyVaultProperties")
    def account_key_vault_properties(self) -> Optional[pulumi.Input[SecretKeyVaultPropertiesArgs]]:
        
        ...
    
    @account_key_vault_properties.setter
    def account_key_vault_properties(self, value: Optional[pulumi.Input[SecretKeyVaultPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @share_name.setter
    def share_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AzureStaticWebAppsRegistrationArgsDict(TypedDict):
    
    client_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AzureStaticWebAppsRegistrationArgs:
    def __init__(__self__, *, client_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AzureStaticWebAppsArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    registration: NotRequired[pulumi.Input[AzureStaticWebAppsRegistrationArgsDict]]


@pulumi.input_type
class AzureStaticWebAppsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., registration: Optional[pulumi.Input[AzureStaticWebAppsRegistrationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[pulumi.Input[AzureStaticWebAppsRegistrationArgs]]:
        
        ...
    
    @registration.setter
    def registration(self, value: Optional[pulumi.Input[AzureStaticWebAppsRegistrationArgs]]): # -> None:
        ...
    


class BlobStorageTokenStoreArgsDict(TypedDict):
    
    blob_container_uri: NotRequired[pulumi.Input[_builtins.str]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    managed_identity_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    sas_url_setting_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class BlobStorageTokenStoreArgs:
    def __init__(__self__, *, blob_container_uri: Optional[pulumi.Input[_builtins.str]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., managed_identity_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., sas_url_setting_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobContainerUri")
    def blob_container_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blob_container_uri.setter
    def blob_container_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentityResourceId")
    def managed_identity_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_identity_resource_id.setter
    def managed_identity_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sasUrlSettingName")
    def sas_url_setting_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sas_url_setting_name.setter
    def sas_url_setting_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class BuildConfigurationArgsDict(TypedDict):
    
    base_os: NotRequired[pulumi.Input[_builtins.str]]
    environment_variables: NotRequired[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgsDict]]]]
    platform: NotRequired[pulumi.Input[_builtins.str]]
    platform_version: NotRequired[pulumi.Input[_builtins.str]]
    pre_build_steps: NotRequired[pulumi.Input[Sequence[pulumi.Input[PreBuildStepArgsDict]]]]


@pulumi.input_type
class BuildConfigurationArgs:
    def __init__(__self__, *, base_os: Optional[pulumi.Input[_builtins.str]] = ..., environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]] = ..., platform: Optional[pulumi.Input[_builtins.str]] = ..., platform_version: Optional[pulumi.Input[_builtins.str]] = ..., pre_build_steps: Optional[pulumi.Input[Sequence[pulumi.Input[PreBuildStepArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseOs")
    def base_os(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @base_os.setter
    def base_os(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]]:
        
        ...
    
    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform_version.setter
    def platform_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preBuildSteps")
    def pre_build_steps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PreBuildStepArgs]]]]:
        
        ...
    
    @pre_build_steps.setter
    def pre_build_steps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PreBuildStepArgs]]]]): # -> None:
        ...
    


class CertificateKeyVaultPropertiesArgsDict(TypedDict):
    
    identity: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CertificateKeyVaultPropertiesArgs:
    def __init__(__self__, *, identity: Optional[pulumi.Input[_builtins.str]] = ..., key_vault_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_url.setter
    def key_vault_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CertificatePropertiesArgsDict(TypedDict):
    
    certificate_key_vault_properties: NotRequired[pulumi.Input[CertificateKeyVaultPropertiesArgsDict]]
    certificate_type: NotRequired[pulumi.Input[Union[_builtins.str, CertificateType]]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CertificatePropertiesArgs:
    def __init__(__self__, *, certificate_key_vault_properties: Optional[pulumi.Input[CertificateKeyVaultPropertiesArgs]] = ..., certificate_type: Optional[pulumi.Input[Union[_builtins.str, CertificateType]]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateKeyVaultProperties")
    def certificate_key_vault_properties(self) -> Optional[pulumi.Input[CertificateKeyVaultPropertiesArgs]]:
        
        ...
    
    @certificate_key_vault_properties.setter
    def certificate_key_vault_properties(self, value: Optional[pulumi.Input[CertificateKeyVaultPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateType")
    def certificate_type(self) -> Optional[pulumi.Input[Union[_builtins.str, CertificateType]]]:
        
        ...
    
    @certificate_type.setter
    def certificate_type(self, value: Optional[pulumi.Input[Union[_builtins.str, CertificateType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CircuitBreakerPolicyArgsDict(TypedDict):
    
    consecutive_errors: NotRequired[pulumi.Input[_builtins.int]]
    interval_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    max_ejection_percent: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CircuitBreakerPolicyArgs:
    def __init__(__self__, *, consecutive_errors: Optional[pulumi.Input[_builtins.int]] = ..., interval_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., max_ejection_percent: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consecutiveErrors")
    def consecutive_errors(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @consecutive_errors.setter
    def consecutive_errors(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="intervalInSeconds")
    def interval_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @interval_in_seconds.setter
    def interval_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxEjectionPercent")
    def max_ejection_percent(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_ejection_percent.setter
    def max_ejection_percent(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ClientRegistrationArgsDict(TypedDict):
    
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_setting_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClientRegistrationArgs:
    def __init__(__self__, *, client_id: Optional[pulumi.Input[_builtins.str]] = ..., client_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConfigurationArgsDict(TypedDict):
    
    active_revisions_mode: NotRequired[pulumi.Input[Union[_builtins.str, ActiveRevisionsMode]]]
    dapr: NotRequired[pulumi.Input[DaprArgsDict]]
    identity_settings: NotRequired[pulumi.Input[Sequence[pulumi.Input[IdentitySettingsArgsDict]]]]
    ingress: NotRequired[pulumi.Input[IngressArgsDict]]
    max_inactive_revisions: NotRequired[pulumi.Input[_builtins.int]]
    registries: NotRequired[pulumi.Input[Sequence[pulumi.Input[RegistryCredentialsArgsDict]]]]
    revision_transition_threshold: NotRequired[pulumi.Input[_builtins.int]]
    runtime: NotRequired[pulumi.Input[RuntimeArgsDict]]
    secrets: NotRequired[pulumi.Input[Sequence[pulumi.Input[SecretArgsDict]]]]
    service: NotRequired[pulumi.Input[ServiceArgsDict]]
    target_label: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConfigurationArgs:
    def __init__(__self__, *, active_revisions_mode: Optional[pulumi.Input[Union[_builtins.str, ActiveRevisionsMode]]] = ..., dapr: Optional[pulumi.Input[DaprArgs]] = ..., identity_settings: Optional[pulumi.Input[Sequence[pulumi.Input[IdentitySettingsArgs]]]] = ..., ingress: Optional[pulumi.Input[IngressArgs]] = ..., max_inactive_revisions: Optional[pulumi.Input[_builtins.int]] = ..., registries: Optional[pulumi.Input[Sequence[pulumi.Input[RegistryCredentialsArgs]]]] = ..., revision_transition_threshold: Optional[pulumi.Input[_builtins.int]] = ..., runtime: Optional[pulumi.Input[RuntimeArgs]] = ..., secrets: Optional[pulumi.Input[Sequence[pulumi.Input[SecretArgs]]]] = ..., service: Optional[pulumi.Input[ServiceArgs]] = ..., target_label: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeRevisionsMode")
    def active_revisions_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, ActiveRevisionsMode]]]:
        
        ...
    
    @active_revisions_mode.setter
    def active_revisions_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, ActiveRevisionsMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dapr(self) -> Optional[pulumi.Input[DaprArgs]]:
        
        ...
    
    @dapr.setter
    def dapr(self, value: Optional[pulumi.Input[DaprArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identitySettings")
    def identity_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IdentitySettingsArgs]]]]:
        
        ...
    
    @identity_settings.setter
    def identity_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IdentitySettingsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[pulumi.Input[IngressArgs]]:
        
        ...
    
    @ingress.setter
    def ingress(self, value: Optional[pulumi.Input[IngressArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxInactiveRevisions")
    def max_inactive_revisions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_inactive_revisions.setter
    def max_inactive_revisions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def registries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegistryCredentialsArgs]]]]:
        
        ...
    
    @registries.setter
    def registries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegistryCredentialsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionTransitionThreshold")
    def revision_transition_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @revision_transition_threshold.setter
    def revision_transition_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[RuntimeArgs]]:
        
        ...
    
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[RuntimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecretArgs]]]]:
        
        ...
    
    @secrets.setter
    def secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecretArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[ServiceArgs]]:
        
        ...
    
    @service.setter
    def service(self, value: Optional[pulumi.Input[ServiceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetLabel")
    def target_label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_label.setter
    def target_label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectedEnvironmentStoragePropertiesArgsDict(TypedDict):
    
    azure_file: NotRequired[pulumi.Input[AzureFilePropertiesArgsDict]]
    smb: NotRequired[pulumi.Input[SmbStorageArgsDict]]


@pulumi.input_type
class ConnectedEnvironmentStoragePropertiesArgs:
    def __init__(__self__, *, azure_file: Optional[pulumi.Input[AzureFilePropertiesArgs]] = ..., smb: Optional[pulumi.Input[SmbStorageArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFile")
    def azure_file(self) -> Optional[pulumi.Input[AzureFilePropertiesArgs]]:
        
        ...
    
    @azure_file.setter
    def azure_file(self, value: Optional[pulumi.Input[AzureFilePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def smb(self) -> Optional[pulumi.Input[SmbStorageArgs]]:
        
        ...
    
    @smb.setter
    def smb(self, value: Optional[pulumi.Input[SmbStorageArgs]]): # -> None:
        ...
    


class ContainerAppPatchingConfigurationArgsDict(TypedDict):
    
    patching_mode: NotRequired[pulumi.Input[Union[_builtins.str, PatchingMode]]]


@pulumi.input_type
class ContainerAppPatchingConfigurationArgs:
    def __init__(__self__, *, patching_mode: Optional[pulumi.Input[Union[_builtins.str, PatchingMode]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="patchingMode")
    def patching_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, PatchingMode]]]:
        
        ...
    
    @patching_mode.setter
    def patching_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, PatchingMode]]]): # -> None:
        ...
    


class ContainerAppProbeHttpGetArgsDict(TypedDict):
    
    port: pulumi.Input[_builtins.int]
    host: NotRequired[pulumi.Input[_builtins.str]]
    http_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[ContainerAppProbeHttpHeadersArgsDict]]]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    scheme: NotRequired[pulumi.Input[Union[_builtins.str, Scheme]]]


@pulumi.input_type
class ContainerAppProbeHttpGetArgs:
    def __init__(__self__, *, port: pulumi.Input[_builtins.int], host: Optional[pulumi.Input[_builtins.str]] = ..., http_headers: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerAppProbeHttpHeadersArgs]]]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., scheme: Optional[pulumi.Input[Union[_builtins.str, Scheme]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContainerAppProbeHttpHeadersArgs]]]]:
        
        ...
    
    @http_headers.setter
    def http_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerAppProbeHttpHeadersArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[pulumi.Input[Union[_builtins.str, Scheme]]]:
        
        ...
    
    @scheme.setter
    def scheme(self, value: Optional[pulumi.Input[Union[_builtins.str, Scheme]]]): # -> None:
        ...
    


class ContainerAppProbeHttpHeadersArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class ContainerAppProbeHttpHeadersArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ContainerAppProbeTcpSocketArgsDict(TypedDict):
    
    port: pulumi.Input[_builtins.int]
    host: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContainerAppProbeTcpSocketArgs:
    def __init__(__self__, *, port: pulumi.Input[_builtins.int], host: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContainerAppProbeArgsDict(TypedDict):
    
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    http_get: NotRequired[pulumi.Input[ContainerAppProbeHttpGetArgsDict]]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    success_threshold: NotRequired[pulumi.Input[_builtins.int]]
    tcp_socket: NotRequired[pulumi.Input[ContainerAppProbeTcpSocketArgsDict]]
    termination_grace_period_seconds: NotRequired[pulumi.Input[_builtins.float]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, Type]]]


@pulumi.input_type
class ContainerAppProbeArgs:
    def __init__(__self__, *, failure_threshold: Optional[pulumi.Input[_builtins.int]] = ..., http_get: Optional[pulumi.Input[ContainerAppProbeHttpGetArgs]] = ..., initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ..., period_seconds: Optional[pulumi.Input[_builtins.int]] = ..., success_threshold: Optional[pulumi.Input[_builtins.int]] = ..., tcp_socket: Optional[pulumi.Input[ContainerAppProbeTcpSocketArgs]] = ..., termination_grace_period_seconds: Optional[pulumi.Input[_builtins.float]] = ..., timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, Type]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[pulumi.Input[ContainerAppProbeHttpGetArgs]]:
        
        ...
    
    @http_get.setter
    def http_get(self, value: Optional[pulumi.Input[ContainerAppProbeHttpGetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @success_threshold.setter
    def success_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(self) -> Optional[pulumi.Input[ContainerAppProbeTcpSocketArgs]]:
        
        ...
    
    @tcp_socket.setter
    def tcp_socket(self, value: Optional[pulumi.Input[ContainerAppProbeTcpSocketArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationGracePeriodSeconds")
    def termination_grace_period_seconds(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @termination_grace_period_seconds.setter
    def termination_grace_period_seconds(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, Type]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, Type]]]): # -> None:
        ...
    


class ContainerRegistryWithCustomImageArgsDict(TypedDict):
    
    server: pulumi.Input[_builtins.str]
    image: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContainerRegistryWithCustomImageArgs:
    def __init__(__self__, *, server: pulumi.Input[_builtins.str], image: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server.setter
    def server(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContainerRegistryArgsDict(TypedDict):
    
    container_registry_server: pulumi.Input[_builtins.str]
    identity_resource_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class ContainerRegistryArgs:
    def __init__(__self__, *, container_registry_server: pulumi.Input[_builtins.str], identity_resource_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerRegistryServer")
    def container_registry_server(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container_registry_server.setter
    def container_registry_server(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityResourceId")
    def identity_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identity_resource_id.setter
    def identity_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ContainerResourcesArgsDict(TypedDict):
    
    cpu: NotRequired[pulumi.Input[_builtins.float]]
    gpu: NotRequired[pulumi.Input[_builtins.float]]
    memory: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContainerResourcesArgs:
    def __init__(__self__, *, cpu: Optional[pulumi.Input[_builtins.float]] = ..., gpu: Optional[pulumi.Input[_builtins.float]] = ..., memory: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def gpu(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @gpu.setter
    def gpu(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContainerArgsDict(TypedDict):
    
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    command: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    env: NotRequired[pulumi.Input[Sequence[pulumi.Input[EnvironmentVarArgsDict]]]]
    image: NotRequired[pulumi.Input[_builtins.str]]
    image_type: NotRequired[pulumi.Input[Union[_builtins.str, ImageType]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    probes: NotRequired[pulumi.Input[Sequence[pulumi.Input[ContainerAppProbeArgsDict]]]]
    resources: NotRequired[pulumi.Input[ContainerResourcesArgsDict]]
    volume_mounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgsDict]]]]


@pulumi.input_type
class ContainerArgs:
    def __init__(__self__, *, args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., command: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., env: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVarArgs]]]] = ..., image: Optional[pulumi.Input[_builtins.str]] = ..., image_type: Optional[pulumi.Input[Union[_builtins.str, ImageType]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., probes: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerAppProbeArgs]]]] = ..., resources: Optional[pulumi.Input[ContainerResourcesArgs]] = ..., volume_mounts: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @args.setter
    def args(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @command.setter
    def command(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def env(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVarArgs]]]]:
        
        ...
    
    @env.setter
    def env(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVarArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ImageType]]]:
        
        ...
    
    @image_type.setter
    def image_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ImageType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def probes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContainerAppProbeArgs]]]]:
        
        ...
    
    @probes.setter
    def probes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerAppProbeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[ContainerResourcesArgs]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[ContainerResourcesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]]:
        
        ...
    
    @volume_mounts.setter
    def volume_mounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]]): # -> None:
        ...
    


class CookieExpirationArgsDict(TypedDict):
    
    convention: NotRequired[pulumi.Input[CookieExpirationConvention]]
    time_to_expiration: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CookieExpirationArgs:
    def __init__(__self__, *, convention: Optional[pulumi.Input[CookieExpirationConvention]] = ..., time_to_expiration: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def convention(self) -> Optional[pulumi.Input[CookieExpirationConvention]]:
        
        ...
    
    @convention.setter
    def convention(self, value: Optional[pulumi.Input[CookieExpirationConvention]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToExpiration")
    def time_to_expiration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_to_expiration.setter
    def time_to_expiration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CorsPolicyArgsDict(TypedDict):
    
    allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    allow_credentials: NotRequired[pulumi.Input[_builtins.bool]]
    allowed_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_methods: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    expose_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    max_age: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CorsPolicyArgs:
    def __init__(__self__, *, allowed_origins: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], allow_credentials: Optional[pulumi.Input[_builtins.bool]] = ..., allowed_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allowed_methods: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., expose_headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., max_age: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @allowed_origins.setter
    def allowed_origins(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_credentials.setter
    def allow_credentials(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_headers.setter
    def allowed_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_methods.setter
    def allowed_methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @expose_headers.setter
    def expose_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_age.setter
    def max_age(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CustomContainerTemplateArgsDict(TypedDict):
    
    containers: NotRequired[pulumi.Input[Sequence[pulumi.Input[SessionContainerArgsDict]]]]
    ingress: NotRequired[pulumi.Input[SessionIngressArgsDict]]
    registry_credentials: NotRequired[pulumi.Input[SessionRegistryCredentialsArgsDict]]


@pulumi.input_type
class CustomContainerTemplateArgs:
    def __init__(__self__, *, containers: Optional[pulumi.Input[Sequence[pulumi.Input[SessionContainerArgs]]]] = ..., ingress: Optional[pulumi.Input[SessionIngressArgs]] = ..., registry_credentials: Optional[pulumi.Input[SessionRegistryCredentialsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SessionContainerArgs]]]]:
        
        ...
    
    @containers.setter
    def containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SessionContainerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[pulumi.Input[SessionIngressArgs]]:
        
        ...
    
    @ingress.setter
    def ingress(self, value: Optional[pulumi.Input[SessionIngressArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryCredentials")
    def registry_credentials(self) -> Optional[pulumi.Input[SessionRegistryCredentialsArgs]]:
        
        ...
    
    @registry_credentials.setter
    def registry_credentials(self, value: Optional[pulumi.Input[SessionRegistryCredentialsArgs]]): # -> None:
        ...
    


class CustomDomainConfigurationArgsDict(TypedDict):
    
    certificate_key_vault_properties: NotRequired[pulumi.Input[CertificateKeyVaultPropertiesArgsDict]]
    certificate_password: NotRequired[pulumi.Input[_builtins.str]]
    certificate_value: NotRequired[pulumi.Input[_builtins.str]]
    dns_suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomDomainConfigurationArgs:
    def __init__(__self__, *, certificate_key_vault_properties: Optional[pulumi.Input[CertificateKeyVaultPropertiesArgs]] = ..., certificate_password: Optional[pulumi.Input[_builtins.str]] = ..., certificate_value: Optional[pulumi.Input[_builtins.str]] = ..., dns_suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateKeyVaultProperties")
    def certificate_key_vault_properties(self) -> Optional[pulumi.Input[CertificateKeyVaultPropertiesArgs]]:
        
        ...
    
    @certificate_key_vault_properties.setter
    def certificate_key_vault_properties(self, value: Optional[pulumi.Input[CertificateKeyVaultPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificatePassword")
    def certificate_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_password.setter
    def certificate_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateValue")
    def certificate_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_value.setter
    def certificate_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_suffix.setter
    def dns_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CustomDomainArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    binding_type: NotRequired[pulumi.Input[Union[_builtins.str, BindingType]]]
    certificate_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomDomainArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], binding_type: Optional[pulumi.Input[Union[_builtins.str, BindingType]]] = ..., certificate_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bindingType")
    def binding_type(self) -> Optional[pulumi.Input[Union[_builtins.str, BindingType]]]:
        
        ...
    
    @binding_type.setter
    def binding_type(self, value: Optional[pulumi.Input[Union[_builtins.str, BindingType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CustomOpenIdConnectProviderArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    login: NotRequired[pulumi.Input[OpenIdConnectLoginArgsDict]]
    registration: NotRequired[pulumi.Input[OpenIdConnectRegistrationArgsDict]]


@pulumi.input_type
class CustomOpenIdConnectProviderArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., login: Optional[pulumi.Input[OpenIdConnectLoginArgs]] = ..., registration: Optional[pulumi.Input[OpenIdConnectRegistrationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[OpenIdConnectLoginArgs]]:
        
        ...
    
    @login.setter
    def login(self, value: Optional[pulumi.Input[OpenIdConnectLoginArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[pulumi.Input[OpenIdConnectRegistrationArgs]]:
        
        ...
    
    @registration.setter
    def registration(self, value: Optional[pulumi.Input[OpenIdConnectRegistrationArgs]]): # -> None:
        ...
    


class CustomScaleRuleArgsDict(TypedDict):
    
    auth: NotRequired[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgsDict]]]]
    identity: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CustomScaleRuleArgs:
    def __init__(__self__, *, auth: Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]] = ..., identity: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]]:
        
        ...
    
    @auth.setter
    def auth(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DaprAppHealthArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    probe_interval_seconds: NotRequired[pulumi.Input[_builtins.int]]
    probe_timeout_milliseconds: NotRequired[pulumi.Input[_builtins.int]]
    threshold: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DaprAppHealthArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., probe_interval_seconds: Optional[pulumi.Input[_builtins.int]] = ..., probe_timeout_milliseconds: Optional[pulumi.Input[_builtins.int]] = ..., threshold: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="probeIntervalSeconds")
    def probe_interval_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @probe_interval_seconds.setter
    def probe_interval_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="probeTimeoutMilliseconds")
    def probe_timeout_milliseconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @probe_timeout_milliseconds.setter
    def probe_timeout_milliseconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DaprComponentResiliencyPolicyCircuitBreakerPolicyConfigurationArgsDict(TypedDict):
    
    consecutive_errors: NotRequired[pulumi.Input[_builtins.int]]
    interval_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DaprComponentResiliencyPolicyCircuitBreakerPolicyConfigurationArgs:
    def __init__(__self__, *, consecutive_errors: Optional[pulumi.Input[_builtins.int]] = ..., interval_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consecutiveErrors")
    def consecutive_errors(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @consecutive_errors.setter
    def consecutive_errors(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="intervalInSeconds")
    def interval_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @interval_in_seconds.setter
    def interval_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DaprComponentResiliencyPolicyConfigurationArgsDict(TypedDict):
    
    circuit_breaker_policy: NotRequired[pulumi.Input[DaprComponentResiliencyPolicyCircuitBreakerPolicyConfigurationArgsDict]]
    http_retry_policy: NotRequired[pulumi.Input[DaprComponentResiliencyPolicyHttpRetryPolicyConfigurationArgsDict]]
    timeout_policy: NotRequired[pulumi.Input[DaprComponentResiliencyPolicyTimeoutPolicyConfigurationArgsDict]]


@pulumi.input_type
class DaprComponentResiliencyPolicyConfigurationArgs:
    def __init__(__self__, *, circuit_breaker_policy: Optional[pulumi.Input[DaprComponentResiliencyPolicyCircuitBreakerPolicyConfigurationArgs]] = ..., http_retry_policy: Optional[pulumi.Input[DaprComponentResiliencyPolicyHttpRetryPolicyConfigurationArgs]] = ..., timeout_policy: Optional[pulumi.Input[DaprComponentResiliencyPolicyTimeoutPolicyConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitBreakerPolicy")
    def circuit_breaker_policy(self) -> Optional[pulumi.Input[DaprComponentResiliencyPolicyCircuitBreakerPolicyConfigurationArgs]]:
        
        ...
    
    @circuit_breaker_policy.setter
    def circuit_breaker_policy(self, value: Optional[pulumi.Input[DaprComponentResiliencyPolicyCircuitBreakerPolicyConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpRetryPolicy")
    def http_retry_policy(self) -> Optional[pulumi.Input[DaprComponentResiliencyPolicyHttpRetryPolicyConfigurationArgs]]:
        
        ...
    
    @http_retry_policy.setter
    def http_retry_policy(self, value: Optional[pulumi.Input[DaprComponentResiliencyPolicyHttpRetryPolicyConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutPolicy")
    def timeout_policy(self) -> Optional[pulumi.Input[DaprComponentResiliencyPolicyTimeoutPolicyConfigurationArgs]]:
        
        ...
    
    @timeout_policy.setter
    def timeout_policy(self, value: Optional[pulumi.Input[DaprComponentResiliencyPolicyTimeoutPolicyConfigurationArgs]]): # -> None:
        ...
    


class DaprComponentResiliencyPolicyHttpRetryBackOffConfigurationArgsDict(TypedDict):
    
    initial_delay_in_milliseconds: NotRequired[pulumi.Input[_builtins.int]]
    max_interval_in_milliseconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DaprComponentResiliencyPolicyHttpRetryBackOffConfigurationArgs:
    def __init__(__self__, *, initial_delay_in_milliseconds: Optional[pulumi.Input[_builtins.int]] = ..., max_interval_in_milliseconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelayInMilliseconds")
    def initial_delay_in_milliseconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @initial_delay_in_milliseconds.setter
    def initial_delay_in_milliseconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIntervalInMilliseconds")
    def max_interval_in_milliseconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_interval_in_milliseconds.setter
    def max_interval_in_milliseconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DaprComponentResiliencyPolicyHttpRetryPolicyConfigurationArgsDict(TypedDict):
    
    max_retries: NotRequired[pulumi.Input[_builtins.int]]
    retry_back_off: NotRequired[pulumi.Input[DaprComponentResiliencyPolicyHttpRetryBackOffConfigurationArgsDict]]


@pulumi.input_type
class DaprComponentResiliencyPolicyHttpRetryPolicyConfigurationArgs:
    def __init__(__self__, *, max_retries: Optional[pulumi.Input[_builtins.int]] = ..., retry_back_off: Optional[pulumi.Input[DaprComponentResiliencyPolicyHttpRetryBackOffConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_retries.setter
    def max_retries(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryBackOff")
    def retry_back_off(self) -> Optional[pulumi.Input[DaprComponentResiliencyPolicyHttpRetryBackOffConfigurationArgs]]:
        
        ...
    
    @retry_back_off.setter
    def retry_back_off(self, value: Optional[pulumi.Input[DaprComponentResiliencyPolicyHttpRetryBackOffConfigurationArgs]]): # -> None:
        ...
    


class DaprComponentResiliencyPolicyTimeoutPolicyConfigurationArgsDict(TypedDict):
    
    response_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DaprComponentResiliencyPolicyTimeoutPolicyConfigurationArgs:
    def __init__(__self__, *, response_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseTimeoutInSeconds")
    def response_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @response_timeout_in_seconds.setter
    def response_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DaprComponentServiceBindingArgsDict(TypedDict):
    
    metadata: NotRequired[pulumi.Input[DaprServiceBindMetadataArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    service_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DaprComponentServiceBindingArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[DaprServiceBindMetadataArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., service_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[DaprServiceBindMetadataArgs]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[DaprServiceBindMetadataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DaprMetadataArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    secret_ref: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DaprMetadataArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., secret_ref: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_ref.setter
    def secret_ref(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DaprServiceBindMetadataArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DaprServiceBindMetadataArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DaprSubscriptionBulkSubscribeOptionsArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    max_await_duration_ms: NotRequired[pulumi.Input[_builtins.int]]
    max_messages_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DaprSubscriptionBulkSubscribeOptionsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., max_await_duration_ms: Optional[pulumi.Input[_builtins.int]] = ..., max_messages_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAwaitDurationMs")
    def max_await_duration_ms(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_await_duration_ms.setter
    def max_await_duration_ms(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxMessagesCount")
    def max_messages_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_messages_count.setter
    def max_messages_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DaprSubscriptionRouteRuleArgsDict(TypedDict):
    
    match: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DaprSubscriptionRouteRuleArgs:
    def __init__(__self__, *, match: Optional[pulumi.Input[_builtins.str]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @match.setter
    def match(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DaprSubscriptionRoutesArgsDict(TypedDict):
    
    default: NotRequired[pulumi.Input[_builtins.str]]
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[DaprSubscriptionRouteRuleArgsDict]]]]


@pulumi.input_type
class DaprSubscriptionRoutesArgs:
    def __init__(__self__, *, default: Optional[pulumi.Input[_builtins.str]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[DaprSubscriptionRouteRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default.setter
    def default(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DaprSubscriptionRouteRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DaprSubscriptionRouteRuleArgs]]]]): # -> None:
        ...
    


class DaprArgsDict(TypedDict):
    
    app_health: NotRequired[pulumi.Input[DaprAppHealthArgsDict]]
    app_id: NotRequired[pulumi.Input[_builtins.str]]
    app_port: NotRequired[pulumi.Input[_builtins.int]]
    app_protocol: NotRequired[pulumi.Input[Union[_builtins.str, AppProtocol]]]
    enable_api_logging: NotRequired[pulumi.Input[_builtins.bool]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    http_max_request_size: NotRequired[pulumi.Input[_builtins.int]]
    http_read_buffer_size: NotRequired[pulumi.Input[_builtins.int]]
    log_level: NotRequired[pulumi.Input[Union[_builtins.str, LogLevel]]]
    max_concurrency: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DaprArgs:
    def __init__(__self__, *, app_health: Optional[pulumi.Input[DaprAppHealthArgs]] = ..., app_id: Optional[pulumi.Input[_builtins.str]] = ..., app_port: Optional[pulumi.Input[_builtins.int]] = ..., app_protocol: Optional[pulumi.Input[Union[_builtins.str, AppProtocol]]] = ..., enable_api_logging: Optional[pulumi.Input[_builtins.bool]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., http_max_request_size: Optional[pulumi.Input[_builtins.int]] = ..., http_read_buffer_size: Optional[pulumi.Input[_builtins.int]] = ..., log_level: Optional[pulumi.Input[Union[_builtins.str, LogLevel]]] = ..., max_concurrency: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appHealth")
    def app_health(self) -> Optional[pulumi.Input[DaprAppHealthArgs]]:
        
        ...
    
    @app_health.setter
    def app_health(self, value: Optional[pulumi.Input[DaprAppHealthArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appPort")
    def app_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @app_port.setter
    def app_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appProtocol")
    def app_protocol(self) -> Optional[pulumi.Input[Union[_builtins.str, AppProtocol]]]:
        
        ...
    
    @app_protocol.setter
    def app_protocol(self, value: Optional[pulumi.Input[Union[_builtins.str, AppProtocol]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableApiLogging")
    def enable_api_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_api_logging.setter
    def enable_api_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMaxRequestSize")
    def http_max_request_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_max_request_size.setter
    def http_max_request_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpReadBufferSize")
    def http_read_buffer_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_read_buffer_size.setter
    def http_read_buffer_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[Union[_builtins.str, LogLevel]]]:
        
        ...
    
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[Union[_builtins.str, LogLevel]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrency.setter
    def max_concurrency(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DataDogConfigurationArgsDict(TypedDict):
    
    key: NotRequired[pulumi.Input[_builtins.str]]
    site: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DataDogConfigurationArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., site: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def site(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @site.setter
    def site(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DefaultAuthorizationPolicyArgsDict(TypedDict):
    
    allowed_applications: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_principals: NotRequired[pulumi.Input[AllowedPrincipalsArgsDict]]


@pulumi.input_type
class DefaultAuthorizationPolicyArgs:
    def __init__(__self__, *, allowed_applications: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allowed_principals: Optional[pulumi.Input[AllowedPrincipalsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedApplications")
    def allowed_applications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_applications.setter
    def allowed_applications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedPrincipals")
    def allowed_principals(self) -> Optional[pulumi.Input[AllowedPrincipalsArgs]]:
        
        ...
    
    @allowed_principals.setter
    def allowed_principals(self, value: Optional[pulumi.Input[AllowedPrincipalsArgs]]): # -> None:
        ...
    


class DestinationsConfigurationArgsDict(TypedDict):
    
    data_dog_configuration: NotRequired[pulumi.Input[DataDogConfigurationArgsDict]]
    otlp_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[OtlpConfigurationArgsDict]]]]


@pulumi.input_type
class DestinationsConfigurationArgs:
    def __init__(__self__, *, data_dog_configuration: Optional[pulumi.Input[DataDogConfigurationArgs]] = ..., otlp_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[OtlpConfigurationArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDogConfiguration")
    def data_dog_configuration(self) -> Optional[pulumi.Input[DataDogConfigurationArgs]]:
        
        ...
    
    @data_dog_configuration.setter
    def data_dog_configuration(self, value: Optional[pulumi.Input[DataDogConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="otlpConfigurations")
    def otlp_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OtlpConfigurationArgs]]]]:
        
        ...
    
    @otlp_configurations.setter
    def otlp_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OtlpConfigurationArgs]]]]): # -> None:
        ...
    


class DiskEncryptionConfigurationAuthArgsDict(TypedDict):
    
    identity: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DiskEncryptionConfigurationAuthArgs:
    def __init__(__self__, *, identity: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DiskEncryptionConfigurationKeyVaultConfigurationArgsDict(TypedDict):
    
    auth: NotRequired[pulumi.Input[DiskEncryptionConfigurationAuthArgsDict]]
    key_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DiskEncryptionConfigurationKeyVaultConfigurationArgs:
    def __init__(__self__, *, auth: Optional[pulumi.Input[DiskEncryptionConfigurationAuthArgs]] = ..., key_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[DiskEncryptionConfigurationAuthArgs]]:
        
        ...
    
    @auth.setter
    def auth(self, value: Optional[pulumi.Input[DiskEncryptionConfigurationAuthArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyUrl")
    def key_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_url.setter
    def key_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DiskEncryptionConfigurationArgsDict(TypedDict):
    
    key_vault_configuration: NotRequired[pulumi.Input[DiskEncryptionConfigurationKeyVaultConfigurationArgsDict]]


@pulumi.input_type
class DiskEncryptionConfigurationArgs:
    def __init__(__self__, *, key_vault_configuration: Optional[pulumi.Input[DiskEncryptionConfigurationKeyVaultConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultConfiguration")
    def key_vault_configuration(self) -> Optional[pulumi.Input[DiskEncryptionConfigurationKeyVaultConfigurationArgs]]:
        
        ...
    
    @key_vault_configuration.setter
    def key_vault_configuration(self, value: Optional[pulumi.Input[DiskEncryptionConfigurationKeyVaultConfigurationArgs]]): # -> None:
        ...
    


class DotNetComponentConfigurationPropertyArgsDict(TypedDict):
    
    property_name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DotNetComponentConfigurationPropertyArgs:
    def __init__(__self__, *, property_name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @property_name.setter
    def property_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DotNetComponentServiceBindArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    service_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DotNetComponentServiceBindArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., service_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DynamicPoolConfigurationArgsDict(TypedDict):
    
    lifecycle_configuration: NotRequired[pulumi.Input[LifecycleConfigurationArgsDict]]


@pulumi.input_type
class DynamicPoolConfigurationArgs:
    def __init__(__self__, *, lifecycle_configuration: Optional[pulumi.Input[LifecycleConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleConfiguration")
    def lifecycle_configuration(self) -> Optional[pulumi.Input[LifecycleConfigurationArgs]]:
        
        ...
    
    @lifecycle_configuration.setter
    def lifecycle_configuration(self, value: Optional[pulumi.Input[LifecycleConfigurationArgs]]): # -> None:
        ...
    


class EncryptionSettingsArgsDict(TypedDict):
    
    container_app_auth_encryption_secret_name: NotRequired[pulumi.Input[_builtins.str]]
    container_app_auth_signing_secret_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EncryptionSettingsArgs:
    def __init__(__self__, *, container_app_auth_encryption_secret_name: Optional[pulumi.Input[_builtins.str]] = ..., container_app_auth_signing_secret_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAppAuthEncryptionSecretName")
    def container_app_auth_encryption_secret_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_app_auth_encryption_secret_name.setter
    def container_app_auth_encryption_secret_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAppAuthSigningSecretName")
    def container_app_auth_signing_secret_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_app_auth_signing_secret_name.setter
    def container_app_auth_signing_secret_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentVariableArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class EnvironmentVariableArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EnvironmentVarArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    secret_ref: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentVarArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., secret_ref: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_ref.setter
    def secret_ref(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ExtendedLocationArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]]


@pulumi.input_type
class ExtendedLocationArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationTypes]]]): # -> None:
        ...
    


class FacebookArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    graph_api_version: NotRequired[pulumi.Input[_builtins.str]]
    login: NotRequired[pulumi.Input[LoginScopesArgsDict]]
    registration: NotRequired[pulumi.Input[AppRegistrationArgsDict]]


@pulumi.input_type
class FacebookArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., graph_api_version: Optional[pulumi.Input[_builtins.str]] = ..., login: Optional[pulumi.Input[LoginScopesArgs]] = ..., registration: Optional[pulumi.Input[AppRegistrationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="graphApiVersion")
    def graph_api_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @graph_api_version.setter
    def graph_api_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[LoginScopesArgs]]:
        
        ...
    
    @login.setter
    def login(self, value: Optional[pulumi.Input[LoginScopesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[pulumi.Input[AppRegistrationArgs]]:
        
        ...
    
    @registration.setter
    def registration(self, value: Optional[pulumi.Input[AppRegistrationArgs]]): # -> None:
        ...
    


class ForwardProxyArgsDict(TypedDict):
    
    convention: NotRequired[pulumi.Input[ForwardProxyConvention]]
    custom_host_header_name: NotRequired[pulumi.Input[_builtins.str]]
    custom_proto_header_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ForwardProxyArgs:
    def __init__(__self__, *, convention: Optional[pulumi.Input[ForwardProxyConvention]] = ..., custom_host_header_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_proto_header_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def convention(self) -> Optional[pulumi.Input[ForwardProxyConvention]]:
        
        ...
    
    @convention.setter
    def convention(self, value: Optional[pulumi.Input[ForwardProxyConvention]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHostHeaderName")
    def custom_host_header_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_host_header_name.setter
    def custom_host_header_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProtoHeaderName")
    def custom_proto_header_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_proto_header_name.setter
    def custom_proto_header_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GitHubArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    login: NotRequired[pulumi.Input[LoginScopesArgsDict]]
    registration: NotRequired[pulumi.Input[ClientRegistrationArgsDict]]


@pulumi.input_type
class GitHubArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., login: Optional[pulumi.Input[LoginScopesArgs]] = ..., registration: Optional[pulumi.Input[ClientRegistrationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[LoginScopesArgs]]:
        
        ...
    
    @login.setter
    def login(self, value: Optional[pulumi.Input[LoginScopesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[pulumi.Input[ClientRegistrationArgs]]:
        
        ...
    
    @registration.setter
    def registration(self, value: Optional[pulumi.Input[ClientRegistrationArgs]]): # -> None:
        ...
    


class GithubActionConfigurationArgsDict(TypedDict):
    
    azure_credentials: NotRequired[pulumi.Input[AzureCredentialsArgsDict]]
    build_environment_variables: NotRequired[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgsDict]]]]
    context_path: NotRequired[pulumi.Input[_builtins.str]]
    dockerfile_path: NotRequired[pulumi.Input[_builtins.str]]
    github_personal_access_token: NotRequired[pulumi.Input[_builtins.str]]
    image: NotRequired[pulumi.Input[_builtins.str]]
    os: NotRequired[pulumi.Input[_builtins.str]]
    publish_type: NotRequired[pulumi.Input[_builtins.str]]
    registry_info: NotRequired[pulumi.Input[RegistryInfoArgsDict]]
    runtime_stack: NotRequired[pulumi.Input[_builtins.str]]
    runtime_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GithubActionConfigurationArgs:
    def __init__(__self__, *, azure_credentials: Optional[pulumi.Input[AzureCredentialsArgs]] = ..., build_environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]] = ..., context_path: Optional[pulumi.Input[_builtins.str]] = ..., dockerfile_path: Optional[pulumi.Input[_builtins.str]] = ..., github_personal_access_token: Optional[pulumi.Input[_builtins.str]] = ..., image: Optional[pulumi.Input[_builtins.str]] = ..., os: Optional[pulumi.Input[_builtins.str]] = ..., publish_type: Optional[pulumi.Input[_builtins.str]] = ..., registry_info: Optional[pulumi.Input[RegistryInfoArgs]] = ..., runtime_stack: Optional[pulumi.Input[_builtins.str]] = ..., runtime_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureCredentials")
    def azure_credentials(self) -> Optional[pulumi.Input[AzureCredentialsArgs]]:
        
        ...
    
    @azure_credentials.setter
    def azure_credentials(self, value: Optional[pulumi.Input[AzureCredentialsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildEnvironmentVariables")
    def build_environment_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]]:
        
        ...
    
    @build_environment_variables.setter
    def build_environment_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contextPath")
    def context_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @context_path.setter
    def context_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerfilePath")
    def dockerfile_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dockerfile_path.setter
    def dockerfile_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="githubPersonalAccessToken")
    def github_personal_access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @github_personal_access_token.setter
    def github_personal_access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def os(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @os.setter
    def os(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishType")
    def publish_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publish_type.setter
    def publish_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryInfo")
    def registry_info(self) -> Optional[pulumi.Input[RegistryInfoArgs]]:
        
        ...
    
    @registry_info.setter
    def registry_info(self, value: Optional[pulumi.Input[RegistryInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeStack")
    def runtime_stack(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_stack.setter
    def runtime_stack(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_version.setter
    def runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GlobalValidationArgsDict(TypedDict):
    
    excluded_paths: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    redirect_to_provider: NotRequired[pulumi.Input[_builtins.str]]
    unauthenticated_client_action: NotRequired[pulumi.Input[UnauthenticatedClientActionV2]]


@pulumi.input_type
class GlobalValidationArgs:
    def __init__(__self__, *, excluded_paths: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., redirect_to_provider: Optional[pulumi.Input[_builtins.str]] = ..., unauthenticated_client_action: Optional[pulumi.Input[UnauthenticatedClientActionV2]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedPaths")
    def excluded_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @excluded_paths.setter
    def excluded_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectToProvider")
    def redirect_to_provider(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_to_provider.setter
    def redirect_to_provider(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unauthenticatedClientAction")
    def unauthenticated_client_action(self) -> Optional[pulumi.Input[UnauthenticatedClientActionV2]]:
        
        ...
    
    @unauthenticated_client_action.setter
    def unauthenticated_client_action(self, value: Optional[pulumi.Input[UnauthenticatedClientActionV2]]): # -> None:
        ...
    


class GoogleArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    login: NotRequired[pulumi.Input[LoginScopesArgsDict]]
    registration: NotRequired[pulumi.Input[ClientRegistrationArgsDict]]
    validation: NotRequired[pulumi.Input[AllowedAudiencesValidationArgsDict]]


@pulumi.input_type
class GoogleArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., login: Optional[pulumi.Input[LoginScopesArgs]] = ..., registration: Optional[pulumi.Input[ClientRegistrationArgs]] = ..., validation: Optional[pulumi.Input[AllowedAudiencesValidationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[LoginScopesArgs]]:
        
        ...
    
    @login.setter
    def login(self, value: Optional[pulumi.Input[LoginScopesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[pulumi.Input[ClientRegistrationArgs]]:
        
        ...
    
    @registration.setter
    def registration(self, value: Optional[pulumi.Input[ClientRegistrationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def validation(self) -> Optional[pulumi.Input[AllowedAudiencesValidationArgs]]:
        
        ...
    
    @validation.setter
    def validation(self, value: Optional[pulumi.Input[AllowedAudiencesValidationArgs]]): # -> None:
        ...
    


class HeaderMatchArgsDict(TypedDict):
    
    exact_match: NotRequired[pulumi.Input[_builtins.str]]
    header: NotRequired[pulumi.Input[_builtins.str]]
    prefix_match: NotRequired[pulumi.Input[_builtins.str]]
    regex_match: NotRequired[pulumi.Input[_builtins.str]]
    suffix_match: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HeaderMatchArgs:
    def __init__(__self__, *, exact_match: Optional[pulumi.Input[_builtins.str]] = ..., header: Optional[pulumi.Input[_builtins.str]] = ..., prefix_match: Optional[pulumi.Input[_builtins.str]] = ..., regex_match: Optional[pulumi.Input[_builtins.str]] = ..., suffix_match: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exactMatch")
    def exact_match(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @exact_match.setter
    def exact_match(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @header.setter
    def header(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixMatch")
    def prefix_match(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix_match.setter
    def prefix_match(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexMatch")
    def regex_match(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @regex_match.setter
    def regex_match(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suffixMatch")
    def suffix_match(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @suffix_match.setter
    def suffix_match(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HeaderArgsDict(TypedDict):
    
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HeaderArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HttpConnectionPoolArgsDict(TypedDict):
    
    http1_max_pending_requests: NotRequired[pulumi.Input[_builtins.int]]
    http2_max_requests: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class HttpConnectionPoolArgs:
    def __init__(__self__, *, http1_max_pending_requests: Optional[pulumi.Input[_builtins.int]] = ..., http2_max_requests: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="http1MaxPendingRequests")
    def http1_max_pending_requests(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http1_max_pending_requests.setter
    def http1_max_pending_requests(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="http2MaxRequests")
    def http2_max_requests(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http2_max_requests.setter
    def http2_max_requests(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class HttpGetArgsDict(TypedDict):
    
    url: pulumi.Input[_builtins.str]
    file_name: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class HttpGetArgs:
    def __init__(__self__, *, url: pulumi.Input[_builtins.str], file_name: Optional[pulumi.Input[_builtins.str]] = ..., headers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_name.setter
    def file_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class HttpRetryPolicyArgsDict(TypedDict):
    
    errors: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[HeaderMatchArgsDict]]]]
    http_status_codes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    initial_delay_in_milliseconds: NotRequired[pulumi.Input[_builtins.float]]
    max_interval_in_milliseconds: NotRequired[pulumi.Input[_builtins.float]]
    max_retries: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class HttpRetryPolicyArgs:
    def __init__(__self__, *, errors: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., headers: Optional[pulumi.Input[Sequence[pulumi.Input[HeaderMatchArgs]]]] = ..., http_status_codes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., initial_delay_in_milliseconds: Optional[pulumi.Input[_builtins.float]] = ..., max_interval_in_milliseconds: Optional[pulumi.Input[_builtins.float]] = ..., max_retries: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @errors.setter
    def errors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HeaderMatchArgs]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HeaderMatchArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpStatusCodes")
    def http_status_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @http_status_codes.setter
    def http_status_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelayInMilliseconds")
    def initial_delay_in_milliseconds(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @initial_delay_in_milliseconds.setter
    def initial_delay_in_milliseconds(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxIntervalInMilliseconds")
    def max_interval_in_milliseconds(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @max_interval_in_milliseconds.setter
    def max_interval_in_milliseconds(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_retries.setter
    def max_retries(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class HttpRouteActionArgsDict(TypedDict):
    
    prefix_rewrite: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HttpRouteActionArgs:
    def __init__(__self__, *, prefix_rewrite: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixRewrite")
    def prefix_rewrite(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix_rewrite.setter
    def prefix_rewrite(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HttpRouteConfigPropertiesArgsDict(TypedDict):
    
    custom_domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[CustomDomainArgsDict]]]]
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleArgsDict]]]]


@pulumi.input_type
class HttpRouteConfigPropertiesArgs:
    def __init__(__self__, *, custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input[CustomDomainArgs]]]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomDomainArgs]]]]:
        
        ...
    
    @custom_domains.setter
    def custom_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomDomainArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteRuleArgs]]]]): # -> None:
        ...
    


class HttpRouteMatchArgsDict(TypedDict):
    
    case_sensitive: NotRequired[pulumi.Input[_builtins.bool]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    path_separated_prefix: NotRequired[pulumi.Input[_builtins.str]]
    prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HttpRouteMatchArgs:
    def __init__(__self__, *, case_sensitive: Optional[pulumi.Input[_builtins.bool]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., path_separated_prefix: Optional[pulumi.Input[_builtins.str]] = ..., prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caseSensitive")
    def case_sensitive(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @case_sensitive.setter
    def case_sensitive(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathSeparatedPrefix")
    def path_separated_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path_separated_prefix.setter
    def path_separated_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HttpRouteRuleArgsDict(TypedDict):
    
    description: NotRequired[pulumi.Input[_builtins.str]]
    routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[HttpRouteArgsDict]]]]
    targets: NotRequired[pulumi.Input[Sequence[pulumi.Input[HttpRouteTargetArgsDict]]]]


@pulumi.input_type
class HttpRouteRuleArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., routes: Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteArgs]]]] = ..., targets: Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteTargetArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteArgs]]]]:
        
        ...
    
    @routes.setter
    def routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteTargetArgs]]]]:
        
        ...
    
    @targets.setter
    def targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteTargetArgs]]]]): # -> None:
        ...
    


class HttpRouteTargetArgsDict(TypedDict):
    
    container_app: pulumi.Input[_builtins.str]
    label: NotRequired[pulumi.Input[_builtins.str]]
    revision: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class HttpRouteTargetArgs:
    def __init__(__self__, *, container_app: pulumi.Input[_builtins.str], label: Optional[pulumi.Input[_builtins.str]] = ..., revision: Optional[pulumi.Input[_builtins.str]] = ..., weight: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerApp")
    def container_app(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container_app.setter
    def container_app(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class HttpRouteArgsDict(TypedDict):
    
    action: NotRequired[pulumi.Input[HttpRouteActionArgsDict]]
    match: NotRequired[pulumi.Input[HttpRouteMatchArgsDict]]


@pulumi.input_type
class HttpRouteArgs:
    def __init__(__self__, *, action: Optional[pulumi.Input[HttpRouteActionArgs]] = ..., match: Optional[pulumi.Input[HttpRouteMatchArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[HttpRouteActionArgs]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[HttpRouteActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[pulumi.Input[HttpRouteMatchArgs]]:
        
        ...
    
    @match.setter
    def match(self, value: Optional[pulumi.Input[HttpRouteMatchArgs]]): # -> None:
        ...
    


class HttpScaleRuleArgsDict(TypedDict):
    
    auth: NotRequired[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgsDict]]]]
    identity: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class HttpScaleRuleArgs:
    def __init__(__self__, *, auth: Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]] = ..., identity: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]]:
        
        ...
    
    @auth.setter
    def auth(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class HttpSettingsRoutesArgsDict(TypedDict):
    
    api_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HttpSettingsRoutesArgs:
    def __init__(__self__, *, api_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiPrefix")
    def api_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_prefix.setter
    def api_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HttpSettingsArgsDict(TypedDict):
    
    forward_proxy: NotRequired[pulumi.Input[ForwardProxyArgsDict]]
    require_https: NotRequired[pulumi.Input[_builtins.bool]]
    routes: NotRequired[pulumi.Input[HttpSettingsRoutesArgsDict]]


@pulumi.input_type
class HttpSettingsArgs:
    def __init__(__self__, *, forward_proxy: Optional[pulumi.Input[ForwardProxyArgs]] = ..., require_https: Optional[pulumi.Input[_builtins.bool]] = ..., routes: Optional[pulumi.Input[HttpSettingsRoutesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardProxy")
    def forward_proxy(self) -> Optional[pulumi.Input[ForwardProxyArgs]]:
        
        ...
    
    @forward_proxy.setter
    def forward_proxy(self, value: Optional[pulumi.Input[ForwardProxyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireHttps")
    def require_https(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @require_https.setter
    def require_https(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[pulumi.Input[HttpSettingsRoutesArgs]]:
        
        ...
    
    @routes.setter
    def routes(self, value: Optional[pulumi.Input[HttpSettingsRoutesArgs]]): # -> None:
        ...
    


class IdentityProvidersArgsDict(TypedDict):
    
    apple: NotRequired[pulumi.Input[AppleArgsDict]]
    azure_active_directory: NotRequired[pulumi.Input[AzureActiveDirectoryArgsDict]]
    azure_static_web_apps: NotRequired[pulumi.Input[AzureStaticWebAppsArgsDict]]
    custom_open_id_connect_providers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[CustomOpenIdConnectProviderArgsDict]]]]
    facebook: NotRequired[pulumi.Input[FacebookArgsDict]]
    git_hub: NotRequired[pulumi.Input[GitHubArgsDict]]
    google: NotRequired[pulumi.Input[GoogleArgsDict]]
    twitter: NotRequired[pulumi.Input[TwitterArgsDict]]


@pulumi.input_type
class IdentityProvidersArgs:
    def __init__(__self__, *, apple: Optional[pulumi.Input[AppleArgs]] = ..., azure_active_directory: Optional[pulumi.Input[AzureActiveDirectoryArgs]] = ..., azure_static_web_apps: Optional[pulumi.Input[AzureStaticWebAppsArgs]] = ..., custom_open_id_connect_providers: Optional[pulumi.Input[Mapping[str, pulumi.Input[CustomOpenIdConnectProviderArgs]]]] = ..., facebook: Optional[pulumi.Input[FacebookArgs]] = ..., git_hub: Optional[pulumi.Input[GitHubArgs]] = ..., google: Optional[pulumi.Input[GoogleArgs]] = ..., twitter: Optional[pulumi.Input[TwitterArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def apple(self) -> Optional[pulumi.Input[AppleArgs]]:
        
        ...
    
    @apple.setter
    def apple(self, value: Optional[pulumi.Input[AppleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureActiveDirectory")
    def azure_active_directory(self) -> Optional[pulumi.Input[AzureActiveDirectoryArgs]]:
        
        ...
    
    @azure_active_directory.setter
    def azure_active_directory(self, value: Optional[pulumi.Input[AzureActiveDirectoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureStaticWebApps")
    def azure_static_web_apps(self) -> Optional[pulumi.Input[AzureStaticWebAppsArgs]]:
        
        ...
    
    @azure_static_web_apps.setter
    def azure_static_web_apps(self, value: Optional[pulumi.Input[AzureStaticWebAppsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customOpenIdConnectProviders")
    def custom_open_id_connect_providers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[CustomOpenIdConnectProviderArgs]]]]:
        
        ...
    
    @custom_open_id_connect_providers.setter
    def custom_open_id_connect_providers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[CustomOpenIdConnectProviderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def facebook(self) -> Optional[pulumi.Input[FacebookArgs]]:
        
        ...
    
    @facebook.setter
    def facebook(self, value: Optional[pulumi.Input[FacebookArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitHub")
    def git_hub(self) -> Optional[pulumi.Input[GitHubArgs]]:
        
        ...
    
    @git_hub.setter
    def git_hub(self, value: Optional[pulumi.Input[GitHubArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def google(self) -> Optional[pulumi.Input[GoogleArgs]]:
        
        ...
    
    @google.setter
    def google(self, value: Optional[pulumi.Input[GoogleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def twitter(self) -> Optional[pulumi.Input[TwitterArgs]]:
        
        ...
    
    @twitter.setter
    def twitter(self, value: Optional[pulumi.Input[TwitterArgs]]): # -> None:
        ...
    


class IdentitySettingsArgsDict(TypedDict):
    
    identity: pulumi.Input[_builtins.str]
    lifecycle: NotRequired[pulumi.Input[Union[_builtins.str, IdentitySettingsLifeCycle]]]


@pulumi.input_type
class IdentitySettingsArgs:
    def __init__(__self__, *, identity: pulumi.Input[_builtins.str], lifecycle: Optional[pulumi.Input[Union[_builtins.str, IdentitySettingsLifeCycle]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identity.setter
    def identity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifecycle(self) -> Optional[pulumi.Input[Union[_builtins.str, IdentitySettingsLifeCycle]]]:
        
        ...
    
    @lifecycle.setter
    def lifecycle(self, value: Optional[pulumi.Input[Union[_builtins.str, IdentitySettingsLifeCycle]]]): # -> None:
        ...
    


class IngressConfigurationScaleArgsDict(TypedDict):
    
    max_replicas: NotRequired[pulumi.Input[_builtins.int]]
    min_replicas: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class IngressConfigurationScaleArgs:
    def __init__(__self__, *, max_replicas: Optional[pulumi.Input[_builtins.int]] = ..., min_replicas: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxReplicas")
    def max_replicas(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_replicas.setter
    def max_replicas(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minReplicas")
    def min_replicas(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_replicas.setter
    def min_replicas(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class IngressConfigurationArgsDict(TypedDict):
    
    header_count_limit: NotRequired[pulumi.Input[_builtins.int]]
    request_idle_timeout: NotRequired[pulumi.Input[_builtins.int]]
    scale: NotRequired[pulumi.Input[IngressConfigurationScaleArgsDict]]
    termination_grace_period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    workload_profile_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IngressConfigurationArgs:
    def __init__(__self__, *, header_count_limit: Optional[pulumi.Input[_builtins.int]] = ..., request_idle_timeout: Optional[pulumi.Input[_builtins.int]] = ..., scale: Optional[pulumi.Input[IngressConfigurationScaleArgs]] = ..., termination_grace_period_seconds: Optional[pulumi.Input[_builtins.int]] = ..., workload_profile_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerCountLimit")
    def header_count_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @header_count_limit.setter
    def header_count_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestIdleTimeout")
    def request_idle_timeout(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @request_idle_timeout.setter
    def request_idle_timeout(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[IngressConfigurationScaleArgs]]:
        
        ...
    
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[IngressConfigurationScaleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationGracePeriodSeconds")
    def termination_grace_period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @termination_grace_period_seconds.setter
    def termination_grace_period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadProfileName")
    def workload_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workload_profile_name.setter
    def workload_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IngressPortMappingArgsDict(TypedDict):
    
    external: pulumi.Input[_builtins.bool]
    target_port: pulumi.Input[_builtins.int]
    exposed_port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class IngressPortMappingArgs:
    def __init__(__self__, *, external: pulumi.Input[_builtins.bool], target_port: pulumi.Input[_builtins.int], exposed_port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def external(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @external.setter
    def external(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPort")
    def target_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @target_port.setter
    def target_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposedPort")
    def exposed_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @exposed_port.setter
    def exposed_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class IngressStickySessionsArgsDict(TypedDict):
    
    affinity: NotRequired[pulumi.Input[Union[_builtins.str, Affinity]]]


@pulumi.input_type
class IngressStickySessionsArgs:
    def __init__(__self__, *, affinity: Optional[pulumi.Input[Union[_builtins.str, Affinity]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def affinity(self) -> Optional[pulumi.Input[Union[_builtins.str, Affinity]]]:
        
        ...
    
    @affinity.setter
    def affinity(self, value: Optional[pulumi.Input[Union[_builtins.str, Affinity]]]): # -> None:
        ...
    


class IngressArgsDict(TypedDict):
    
    additional_port_mappings: NotRequired[pulumi.Input[Sequence[pulumi.Input[IngressPortMappingArgsDict]]]]
    allow_insecure: NotRequired[pulumi.Input[_builtins.bool]]
    client_certificate_mode: NotRequired[pulumi.Input[Union[_builtins.str, IngressClientCertificateMode]]]
    cors_policy: NotRequired[pulumi.Input[CorsPolicyArgsDict]]
    custom_domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[CustomDomainArgsDict]]]]
    exposed_port: NotRequired[pulumi.Input[_builtins.int]]
    external: NotRequired[pulumi.Input[_builtins.bool]]
    ip_security_restrictions: NotRequired[pulumi.Input[Sequence[pulumi.Input[IpSecurityRestrictionRuleArgsDict]]]]
    sticky_sessions: NotRequired[pulumi.Input[IngressStickySessionsArgsDict]]
    target_port: NotRequired[pulumi.Input[_builtins.int]]
    target_port_http_scheme: NotRequired[pulumi.Input[Union[_builtins.str, IngressTargetPortHttpScheme]]]
    traffic: NotRequired[pulumi.Input[Sequence[pulumi.Input[TrafficWeightArgsDict]]]]
    transport: NotRequired[pulumi.Input[Union[_builtins.str, IngressTransportMethod]]]


@pulumi.input_type
class IngressArgs:
    def __init__(__self__, *, additional_port_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[IngressPortMappingArgs]]]] = ..., allow_insecure: Optional[pulumi.Input[_builtins.bool]] = ..., client_certificate_mode: Optional[pulumi.Input[Union[_builtins.str, IngressClientCertificateMode]]] = ..., cors_policy: Optional[pulumi.Input[CorsPolicyArgs]] = ..., custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input[CustomDomainArgs]]]] = ..., exposed_port: Optional[pulumi.Input[_builtins.int]] = ..., external: Optional[pulumi.Input[_builtins.bool]] = ..., ip_security_restrictions: Optional[pulumi.Input[Sequence[pulumi.Input[IpSecurityRestrictionRuleArgs]]]] = ..., sticky_sessions: Optional[pulumi.Input[IngressStickySessionsArgs]] = ..., target_port: Optional[pulumi.Input[_builtins.int]] = ..., target_port_http_scheme: Optional[pulumi.Input[Union[_builtins.str, IngressTargetPortHttpScheme]]] = ..., traffic: Optional[pulumi.Input[Sequence[pulumi.Input[TrafficWeightArgs]]]] = ..., transport: Optional[pulumi.Input[Union[_builtins.str, IngressTransportMethod]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalPortMappings")
    def additional_port_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IngressPortMappingArgs]]]]:
        
        ...
    
    @additional_port_mappings.setter
    def additional_port_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IngressPortMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_insecure.setter
    def allow_insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateMode")
    def client_certificate_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, IngressClientCertificateMode]]]:
        
        ...
    
    @client_certificate_mode.setter
    def client_certificate_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, IngressClientCertificateMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="corsPolicy")
    def cors_policy(self) -> Optional[pulumi.Input[CorsPolicyArgs]]:
        
        ...
    
    @cors_policy.setter
    def cors_policy(self, value: Optional[pulumi.Input[CorsPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CustomDomainArgs]]]]:
        
        ...
    
    @custom_domains.setter
    def custom_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CustomDomainArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="exposedPort")
    def exposed_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @exposed_port.setter
    def exposed_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def external(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @external.setter
    def external(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSecurityRestrictions")
    def ip_security_restrictions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpSecurityRestrictionRuleArgs]]]]:
        
        ...
    
    @ip_security_restrictions.setter
    def ip_security_restrictions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpSecurityRestrictionRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stickySessions")
    def sticky_sessions(self) -> Optional[pulumi.Input[IngressStickySessionsArgs]]:
        
        ...
    
    @sticky_sessions.setter
    def sticky_sessions(self, value: Optional[pulumi.Input[IngressStickySessionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPort")
    def target_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_port.setter
    def target_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPortHttpScheme")
    def target_port_http_scheme(self) -> Optional[pulumi.Input[Union[_builtins.str, IngressTargetPortHttpScheme]]]:
        
        ...
    
    @target_port_http_scheme.setter
    def target_port_http_scheme(self, value: Optional[pulumi.Input[Union[_builtins.str, IngressTargetPortHttpScheme]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def traffic(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TrafficWeightArgs]]]]:
        
        ...
    
    @traffic.setter
    def traffic(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TrafficWeightArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def transport(self) -> Optional[pulumi.Input[Union[_builtins.str, IngressTransportMethod]]]:
        
        ...
    
    @transport.setter
    def transport(self, value: Optional[pulumi.Input[Union[_builtins.str, IngressTransportMethod]]]): # -> None:
        ...
    


class InitContainerArgsDict(TypedDict):
    
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    command: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    env: NotRequired[pulumi.Input[Sequence[pulumi.Input[EnvironmentVarArgsDict]]]]
    image: NotRequired[pulumi.Input[_builtins.str]]
    image_type: NotRequired[pulumi.Input[Union[_builtins.str, ImageType]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    resources: NotRequired[pulumi.Input[ContainerResourcesArgsDict]]
    volume_mounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgsDict]]]]


@pulumi.input_type
class InitContainerArgs:
    def __init__(__self__, *, args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., command: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., env: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVarArgs]]]] = ..., image: Optional[pulumi.Input[_builtins.str]] = ..., image_type: Optional[pulumi.Input[Union[_builtins.str, ImageType]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[ContainerResourcesArgs]] = ..., volume_mounts: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @args.setter
    def args(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @command.setter
    def command(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def env(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVarArgs]]]]:
        
        ...
    
    @env.setter
    def env(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVarArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[pulumi.Input[Union[_builtins.str, ImageType]]]:
        
        ...
    
    @image_type.setter
    def image_type(self, value: Optional[pulumi.Input[Union[_builtins.str, ImageType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[ContainerResourcesArgs]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[ContainerResourcesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]]:
        
        ...
    
    @volume_mounts.setter
    def volume_mounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]]): # -> None:
        ...
    


class IpSecurityRestrictionRuleArgsDict(TypedDict):
    
    action: pulumi.Input[Union[_builtins.str, Action]]
    ip_address_range: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IpSecurityRestrictionRuleArgs:
    def __init__(__self__, *, action: pulumi.Input[Union[_builtins.str, Action]], ip_address_range: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[Union[_builtins.str, Action]]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[Union[_builtins.str, Action]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressRange")
    def ip_address_range(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_address_range.setter
    def ip_address_range(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JavaComponentConfigurationPropertyArgsDict(TypedDict):
    
    property_name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JavaComponentConfigurationPropertyArgs:
    def __init__(__self__, *, property_name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @property_name.setter
    def property_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JavaComponentPropertiesScaleArgsDict(TypedDict):
    
    max_replicas: NotRequired[pulumi.Input[_builtins.int]]
    min_replicas: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JavaComponentPropertiesScaleArgs:
    def __init__(__self__, *, max_replicas: Optional[pulumi.Input[_builtins.int]] = ..., min_replicas: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxReplicas")
    def max_replicas(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_replicas.setter
    def max_replicas(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minReplicas")
    def min_replicas(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_replicas.setter
    def min_replicas(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JavaComponentServiceBindArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    service_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JavaComponentServiceBindArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., service_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobConfigurationEventTriggerConfigArgsDict(TypedDict):
    
    parallelism: NotRequired[pulumi.Input[_builtins.int]]
    replica_completion_count: NotRequired[pulumi.Input[_builtins.int]]
    scale: NotRequired[pulumi.Input[JobScaleArgsDict]]


@pulumi.input_type
class JobConfigurationEventTriggerConfigArgs:
    def __init__(__self__, *, parallelism: Optional[pulumi.Input[_builtins.int]] = ..., replica_completion_count: Optional[pulumi.Input[_builtins.int]] = ..., scale: Optional[pulumi.Input[JobScaleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @parallelism.setter
    def parallelism(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCompletionCount")
    def replica_completion_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_completion_count.setter
    def replica_completion_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[JobScaleArgs]]:
        
        ...
    
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[JobScaleArgs]]): # -> None:
        ...
    


class JobConfigurationManualTriggerConfigArgsDict(TypedDict):
    
    parallelism: NotRequired[pulumi.Input[_builtins.int]]
    replica_completion_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobConfigurationManualTriggerConfigArgs:
    def __init__(__self__, *, parallelism: Optional[pulumi.Input[_builtins.int]] = ..., replica_completion_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @parallelism.setter
    def parallelism(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCompletionCount")
    def replica_completion_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_completion_count.setter
    def replica_completion_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobConfigurationScheduleTriggerConfigArgsDict(TypedDict):
    
    cron_expression: pulumi.Input[_builtins.str]
    parallelism: NotRequired[pulumi.Input[_builtins.int]]
    replica_completion_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobConfigurationScheduleTriggerConfigArgs:
    def __init__(__self__, *, cron_expression: pulumi.Input[_builtins.str], parallelism: Optional[pulumi.Input[_builtins.int]] = ..., replica_completion_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cronExpression")
    def cron_expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cron_expression.setter
    def cron_expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @parallelism.setter
    def parallelism(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCompletionCount")
    def replica_completion_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_completion_count.setter
    def replica_completion_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobConfigurationArgsDict(TypedDict):
    
    replica_timeout: pulumi.Input[_builtins.int]
    trigger_type: pulumi.Input[Union[_builtins.str, TriggerType]]
    event_trigger_config: NotRequired[pulumi.Input[JobConfigurationEventTriggerConfigArgsDict]]
    identity_settings: NotRequired[pulumi.Input[Sequence[pulumi.Input[IdentitySettingsArgsDict]]]]
    manual_trigger_config: NotRequired[pulumi.Input[JobConfigurationManualTriggerConfigArgsDict]]
    registries: NotRequired[pulumi.Input[Sequence[pulumi.Input[RegistryCredentialsArgsDict]]]]
    replica_retry_limit: NotRequired[pulumi.Input[_builtins.int]]
    schedule_trigger_config: NotRequired[pulumi.Input[JobConfigurationScheduleTriggerConfigArgsDict]]
    secrets: NotRequired[pulumi.Input[Sequence[pulumi.Input[SecretArgsDict]]]]


@pulumi.input_type
class JobConfigurationArgs:
    def __init__(__self__, *, replica_timeout: pulumi.Input[_builtins.int], trigger_type: Optional[pulumi.Input[Union[_builtins.str, TriggerType]]] = ..., event_trigger_config: Optional[pulumi.Input[JobConfigurationEventTriggerConfigArgs]] = ..., identity_settings: Optional[pulumi.Input[Sequence[pulumi.Input[IdentitySettingsArgs]]]] = ..., manual_trigger_config: Optional[pulumi.Input[JobConfigurationManualTriggerConfigArgs]] = ..., registries: Optional[pulumi.Input[Sequence[pulumi.Input[RegistryCredentialsArgs]]]] = ..., replica_retry_limit: Optional[pulumi.Input[_builtins.int]] = ..., schedule_trigger_config: Optional[pulumi.Input[JobConfigurationScheduleTriggerConfigArgs]] = ..., secrets: Optional[pulumi.Input[Sequence[pulumi.Input[SecretArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaTimeout")
    def replica_timeout(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @replica_timeout.setter
    def replica_timeout(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> pulumi.Input[Union[_builtins.str, TriggerType]]:
        
        ...
    
    @trigger_type.setter
    def trigger_type(self, value: pulumi.Input[Union[_builtins.str, TriggerType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventTriggerConfig")
    def event_trigger_config(self) -> Optional[pulumi.Input[JobConfigurationEventTriggerConfigArgs]]:
        
        ...
    
    @event_trigger_config.setter
    def event_trigger_config(self, value: Optional[pulumi.Input[JobConfigurationEventTriggerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identitySettings")
    def identity_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IdentitySettingsArgs]]]]:
        
        ...
    
    @identity_settings.setter
    def identity_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IdentitySettingsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualTriggerConfig")
    def manual_trigger_config(self) -> Optional[pulumi.Input[JobConfigurationManualTriggerConfigArgs]]:
        
        ...
    
    @manual_trigger_config.setter
    def manual_trigger_config(self, value: Optional[pulumi.Input[JobConfigurationManualTriggerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def registries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegistryCredentialsArgs]]]]:
        
        ...
    
    @registries.setter
    def registries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegistryCredentialsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaRetryLimit")
    def replica_retry_limit(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_retry_limit.setter
    def replica_retry_limit(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleTriggerConfig")
    def schedule_trigger_config(self) -> Optional[pulumi.Input[JobConfigurationScheduleTriggerConfigArgs]]:
        
        ...
    
    @schedule_trigger_config.setter
    def schedule_trigger_config(self, value: Optional[pulumi.Input[JobConfigurationScheduleTriggerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecretArgs]]]]:
        
        ...
    
    @secrets.setter
    def secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecretArgs]]]]): # -> None:
        ...
    


class JobScaleRuleArgsDict(TypedDict):
    
    auth: NotRequired[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgsDict]]]]
    identity: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[Any]
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobScaleRuleArgs:
    def __init__(__self__, *, auth: Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]] = ..., identity: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[Any] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]]:
        
        ...
    
    @auth.setter
    def auth(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobScaleArgsDict(TypedDict):
    
    max_executions: NotRequired[pulumi.Input[_builtins.int]]
    min_executions: NotRequired[pulumi.Input[_builtins.int]]
    polling_interval: NotRequired[pulumi.Input[_builtins.int]]
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobScaleRuleArgsDict]]]]


@pulumi.input_type
class JobScaleArgs:
    def __init__(__self__, *, max_executions: Optional[pulumi.Input[_builtins.int]] = ..., min_executions: Optional[pulumi.Input[_builtins.int]] = ..., polling_interval: Optional[pulumi.Input[_builtins.int]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[JobScaleRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxExecutions")
    def max_executions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_executions.setter
    def max_executions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minExecutions")
    def min_executions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_executions.setter
    def min_executions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pollingInterval")
    def polling_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @polling_interval.setter
    def polling_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobScaleRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobScaleRuleArgs]]]]): # -> None:
        ...
    


class JobTemplateArgsDict(TypedDict):
    
    containers: NotRequired[pulumi.Input[Sequence[pulumi.Input[ContainerArgsDict]]]]
    init_containers: NotRequired[pulumi.Input[Sequence[pulumi.Input[InitContainerArgsDict]]]]
    volumes: NotRequired[pulumi.Input[Sequence[pulumi.Input[VolumeArgsDict]]]]


@pulumi.input_type
class JobTemplateArgs:
    def __init__(__self__, *, containers: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerArgs]]]] = ..., init_containers: Optional[pulumi.Input[Sequence[pulumi.Input[InitContainerArgs]]]] = ..., volumes: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContainerArgs]]]]:
        
        ...
    
    @containers.setter
    def containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initContainers")
    def init_containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InitContainerArgs]]]]:
        
        ...
    
    @init_containers.setter
    def init_containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InitContainerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeArgs]]]]:
        
        ...
    
    @volumes.setter
    def volumes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeArgs]]]]): # -> None:
        ...
    


class JwtClaimChecksArgsDict(TypedDict):
    
    allowed_client_applications: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class JwtClaimChecksArgs:
    def __init__(__self__, *, allowed_client_applications: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., allowed_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedClientApplications")
    def allowed_client_applications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_client_applications.setter
    def allowed_client_applications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedGroups")
    def allowed_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_groups.setter
    def allowed_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class LifecycleConfigurationArgsDict(TypedDict):
    
    cooldown_period_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    lifecycle_type: NotRequired[pulumi.Input[Union[_builtins.str, LifecycleType]]]
    max_alive_period_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LifecycleConfigurationArgs:
    def __init__(__self__, *, cooldown_period_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., lifecycle_type: Optional[pulumi.Input[Union[_builtins.str, LifecycleType]]] = ..., max_alive_period_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cooldownPeriodInSeconds")
    def cooldown_period_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cooldown_period_in_seconds.setter
    def cooldown_period_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleType")
    def lifecycle_type(self) -> Optional[pulumi.Input[Union[_builtins.str, LifecycleType]]]:
        
        ...
    
    @lifecycle_type.setter
    def lifecycle_type(self, value: Optional[pulumi.Input[Union[_builtins.str, LifecycleType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAlivePeriodInSeconds")
    def max_alive_period_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_alive_period_in_seconds.setter
    def max_alive_period_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class LogAnalyticsConfigurationArgsDict(TypedDict):
    
    customer_id: NotRequired[pulumi.Input[_builtins.str]]
    dynamic_json_columns: NotRequired[pulumi.Input[_builtins.bool]]
    shared_key: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LogAnalyticsConfigurationArgs:
    def __init__(__self__, *, customer_id: Optional[pulumi.Input[_builtins.str]] = ..., dynamic_json_columns: Optional[pulumi.Input[_builtins.bool]] = ..., shared_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_id.setter
    def customer_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dynamicJsonColumns")
    def dynamic_json_columns(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @dynamic_json_columns.setter
    def dynamic_json_columns(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedKey")
    def shared_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @shared_key.setter
    def shared_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LoggerSettingArgsDict(TypedDict):
    
    level: pulumi.Input[Union[_builtins.str, Level]]
    logger: pulumi.Input[_builtins.str]


@pulumi.input_type
class LoggerSettingArgs:
    def __init__(__self__, *, level: pulumi.Input[Union[_builtins.str, Level]], logger: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def level(self) -> pulumi.Input[Union[_builtins.str, Level]]:
        
        ...
    
    @level.setter
    def level(self, value: pulumi.Input[Union[_builtins.str, Level]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def logger(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @logger.setter
    def logger(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class LoginRoutesArgsDict(TypedDict):
    
    logout_endpoint: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LoginRoutesArgs:
    def __init__(__self__, *, logout_endpoint: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logoutEndpoint")
    def logout_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logout_endpoint.setter
    def logout_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LoginScopesArgsDict(TypedDict):
    
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class LoginScopesArgs:
    def __init__(__self__, *, scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class LoginArgsDict(TypedDict):
    
    allowed_external_redirect_urls: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cookie_expiration: NotRequired[pulumi.Input[CookieExpirationArgsDict]]
    nonce: NotRequired[pulumi.Input[NonceArgsDict]]
    preserve_url_fragments_for_logins: NotRequired[pulumi.Input[_builtins.bool]]
    routes: NotRequired[pulumi.Input[LoginRoutesArgsDict]]
    token_store: NotRequired[pulumi.Input[TokenStoreArgsDict]]


@pulumi.input_type
class LoginArgs:
    def __init__(__self__, *, allowed_external_redirect_urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cookie_expiration: Optional[pulumi.Input[CookieExpirationArgs]] = ..., nonce: Optional[pulumi.Input[NonceArgs]] = ..., preserve_url_fragments_for_logins: Optional[pulumi.Input[_builtins.bool]] = ..., routes: Optional[pulumi.Input[LoginRoutesArgs]] = ..., token_store: Optional[pulumi.Input[TokenStoreArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedExternalRedirectUrls")
    def allowed_external_redirect_urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_external_redirect_urls.setter
    def allowed_external_redirect_urls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookieExpiration")
    def cookie_expiration(self) -> Optional[pulumi.Input[CookieExpirationArgs]]:
        
        ...
    
    @cookie_expiration.setter
    def cookie_expiration(self, value: Optional[pulumi.Input[CookieExpirationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nonce(self) -> Optional[pulumi.Input[NonceArgs]]:
        
        ...
    
    @nonce.setter
    def nonce(self, value: Optional[pulumi.Input[NonceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveUrlFragmentsForLogins")
    def preserve_url_fragments_for_logins(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @preserve_url_fragments_for_logins.setter
    def preserve_url_fragments_for_logins(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> Optional[pulumi.Input[LoginRoutesArgs]]:
        
        ...
    
    @routes.setter
    def routes(self, value: Optional[pulumi.Input[LoginRoutesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenStore")
    def token_store(self) -> Optional[pulumi.Input[TokenStoreArgs]]:
        
        ...
    
    @token_store.setter
    def token_store(self, value: Optional[pulumi.Input[TokenStoreArgs]]): # -> None:
        ...
    


class LogsConfigurationArgsDict(TypedDict):
    
    destinations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class LogsConfigurationArgs:
    def __init__(__self__, *, destinations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ManagedCertificatePropertiesArgsDict(TypedDict):
    
    domain_control_validation: NotRequired[pulumi.Input[Union[_builtins.str, ManagedCertificateDomainControlValidation]]]
    subject_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedCertificatePropertiesArgs:
    def __init__(__self__, *, domain_control_validation: Optional[pulumi.Input[Union[_builtins.str, ManagedCertificateDomainControlValidation]]] = ..., subject_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainControlValidation")
    def domain_control_validation(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedCertificateDomainControlValidation]]]:
        
        ...
    
    @domain_control_validation.setter
    def domain_control_validation(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedCertificateDomainControlValidation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subject_name.setter
    def subject_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedEnvironmentEncryptionArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ManagedEnvironmentEncryptionArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ManagedEnvironmentPeerAuthenticationArgsDict(TypedDict):
    
    mtls: NotRequired[pulumi.Input[MtlsArgsDict]]


@pulumi.input_type
class ManagedEnvironmentPeerAuthenticationArgs:
    def __init__(__self__, *, mtls: Optional[pulumi.Input[MtlsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtls(self) -> Optional[pulumi.Input[MtlsArgs]]:
        
        ...
    
    @mtls.setter
    def mtls(self, value: Optional[pulumi.Input[MtlsArgs]]): # -> None:
        ...
    


class ManagedEnvironmentPeerTrafficConfigurationArgsDict(TypedDict):
    
    encryption: NotRequired[pulumi.Input[ManagedEnvironmentEncryptionArgsDict]]


@pulumi.input_type
class ManagedEnvironmentPeerTrafficConfigurationArgs:
    def __init__(__self__, *, encryption: Optional[pulumi.Input[ManagedEnvironmentEncryptionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[ManagedEnvironmentEncryptionArgs]]:
        
        ...
    
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[ManagedEnvironmentEncryptionArgs]]): # -> None:
        ...
    


class ManagedEnvironmentStoragePropertiesArgsDict(TypedDict):
    
    azure_file: NotRequired[pulumi.Input[AzureFilePropertiesArgsDict]]
    nfs_azure_file: NotRequired[pulumi.Input[NfsAzureFilePropertiesArgsDict]]


@pulumi.input_type
class ManagedEnvironmentStoragePropertiesArgs:
    def __init__(__self__, *, azure_file: Optional[pulumi.Input[AzureFilePropertiesArgs]] = ..., nfs_azure_file: Optional[pulumi.Input[NfsAzureFilePropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureFile")
    def azure_file(self) -> Optional[pulumi.Input[AzureFilePropertiesArgs]]:
        
        ...
    
    @azure_file.setter
    def azure_file(self, value: Optional[pulumi.Input[AzureFilePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nfsAzureFile")
    def nfs_azure_file(self) -> Optional[pulumi.Input[NfsAzureFilePropertiesArgs]]:
        
        ...
    
    @nfs_azure_file.setter
    def nfs_azure_file(self, value: Optional[pulumi.Input[NfsAzureFilePropertiesArgs]]): # -> None:
        ...
    


class ManagedIdentitySettingArgsDict(TypedDict):
    
    identity: pulumi.Input[_builtins.str]
    lifecycle: NotRequired[pulumi.Input[Union[_builtins.str, IdentitySettingsLifeCycle]]]


@pulumi.input_type
class ManagedIdentitySettingArgs:
    def __init__(__self__, *, identity: pulumi.Input[_builtins.str], lifecycle: Optional[pulumi.Input[Union[_builtins.str, IdentitySettingsLifeCycle]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @identity.setter
    def identity(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lifecycle(self) -> Optional[pulumi.Input[Union[_builtins.str, IdentitySettingsLifeCycle]]]:
        
        ...
    
    @lifecycle.setter
    def lifecycle(self, value: Optional[pulumi.Input[Union[_builtins.str, IdentitySettingsLifeCycle]]]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class MetricsConfigurationArgsDict(TypedDict):
    
    destinations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    include_keda: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class MetricsConfigurationArgs:
    def __init__(__self__, *, destinations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., include_keda: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeKeda")
    def include_keda(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_keda.setter
    def include_keda(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class MtlsArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class MtlsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class NacosComponentArgsDict(TypedDict):
    
    component_type: pulumi.Input[_builtins.str]
    configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgsDict]]]]
    scale: NotRequired[pulumi.Input[JavaComponentPropertiesScaleArgsDict]]
    service_binds: NotRequired[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgsDict]]]]


@pulumi.input_type
class NacosComponentArgs:
    def __init__(__self__, *, component_type: pulumi.Input[_builtins.str], configurations: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]] = ..., scale: Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]] = ..., service_binds: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @component_type.setter
    def component_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]]:
        
        ...
    
    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]]:
        
        ...
    
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]]:
        
        ...
    
    @service_binds.setter
    def service_binds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]]): # -> None:
        ...
    


class NfsAzureFilePropertiesArgsDict(TypedDict):
    
    access_mode: NotRequired[pulumi.Input[Union[_builtins.str, AccessMode]]]
    server: NotRequired[pulumi.Input[_builtins.str]]
    share_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NfsAzureFilePropertiesArgs:
    def __init__(__self__, *, access_mode: Optional[pulumi.Input[Union[_builtins.str, AccessMode]]] = ..., server: Optional[pulumi.Input[_builtins.str]] = ..., share_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AccessMode]]]:
        
        ...
    
    @access_mode.setter
    def access_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, AccessMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server.setter
    def server(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @share_name.setter
    def share_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NonceArgsDict(TypedDict):
    
    nonce_expiration_interval: NotRequired[pulumi.Input[_builtins.str]]
    validate_nonce: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class NonceArgs:
    def __init__(__self__, *, nonce_expiration_interval: Optional[pulumi.Input[_builtins.str]] = ..., validate_nonce: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonceExpirationInterval")
    def nonce_expiration_interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @nonce_expiration_interval.setter
    def nonce_expiration_interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateNonce")
    def validate_nonce(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @validate_nonce.setter
    def validate_nonce(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class OpenIdConnectClientCredentialArgsDict(TypedDict):
    
    client_secret_setting_name: NotRequired[pulumi.Input[_builtins.str]]
    method: NotRequired[pulumi.Input[ClientCredentialMethod]]


@pulumi.input_type
class OpenIdConnectClientCredentialArgs:
    def __init__(__self__, *, client_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ..., method: Optional[pulumi.Input[ClientCredentialMethod]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretSettingName")
    def client_secret_setting_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret_setting_name.setter
    def client_secret_setting_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[ClientCredentialMethod]]:
        
        ...
    
    @method.setter
    def method(self, value: Optional[pulumi.Input[ClientCredentialMethod]]): # -> None:
        ...
    


class OpenIdConnectConfigArgsDict(TypedDict):
    
    authorization_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    certification_uri: NotRequired[pulumi.Input[_builtins.str]]
    issuer: NotRequired[pulumi.Input[_builtins.str]]
    token_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    well_known_open_id_configuration: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OpenIdConnectConfigArgs:
    def __init__(__self__, *, authorization_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., certification_uri: Optional[pulumi.Input[_builtins.str]] = ..., issuer: Optional[pulumi.Input[_builtins.str]] = ..., token_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., well_known_open_id_configuration: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationEndpoint")
    def authorization_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_endpoint.setter
    def authorization_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificationUri")
    def certification_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certification_uri.setter
    def certification_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="wellKnownOpenIdConfiguration")
    def well_known_open_id_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @well_known_open_id_configuration.setter
    def well_known_open_id_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OpenIdConnectLoginArgsDict(TypedDict):
    
    name_claim_type: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class OpenIdConnectLoginArgs:
    def __init__(__self__, *, name_claim_type: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameClaimType")
    def name_claim_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_claim_type.setter
    def name_claim_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class OpenIdConnectRegistrationArgsDict(TypedDict):
    
    client_credential: NotRequired[pulumi.Input[OpenIdConnectClientCredentialArgsDict]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    open_id_connect_configuration: NotRequired[pulumi.Input[OpenIdConnectConfigArgsDict]]


@pulumi.input_type
class OpenIdConnectRegistrationArgs:
    def __init__(__self__, *, client_credential: Optional[pulumi.Input[OpenIdConnectClientCredentialArgs]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., open_id_connect_configuration: Optional[pulumi.Input[OpenIdConnectConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCredential")
    def client_credential(self) -> Optional[pulumi.Input[OpenIdConnectClientCredentialArgs]]:
        
        ...
    
    @client_credential.setter
    def client_credential(self, value: Optional[pulumi.Input[OpenIdConnectClientCredentialArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openIdConnectConfiguration")
    def open_id_connect_configuration(self) -> Optional[pulumi.Input[OpenIdConnectConfigArgs]]:
        
        ...
    
    @open_id_connect_configuration.setter
    def open_id_connect_configuration(self, value: Optional[pulumi.Input[OpenIdConnectConfigArgs]]): # -> None:
        ...
    


class OpenTelemetryConfigurationArgsDict(TypedDict):
    
    destinations_configuration: NotRequired[pulumi.Input[DestinationsConfigurationArgsDict]]
    logs_configuration: NotRequired[pulumi.Input[LogsConfigurationArgsDict]]
    metrics_configuration: NotRequired[pulumi.Input[MetricsConfigurationArgsDict]]
    traces_configuration: NotRequired[pulumi.Input[TracesConfigurationArgsDict]]


@pulumi.input_type
class OpenTelemetryConfigurationArgs:
    def __init__(__self__, *, destinations_configuration: Optional[pulumi.Input[DestinationsConfigurationArgs]] = ..., logs_configuration: Optional[pulumi.Input[LogsConfigurationArgs]] = ..., metrics_configuration: Optional[pulumi.Input[MetricsConfigurationArgs]] = ..., traces_configuration: Optional[pulumi.Input[TracesConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationsConfiguration")
    def destinations_configuration(self) -> Optional[pulumi.Input[DestinationsConfigurationArgs]]:
        
        ...
    
    @destinations_configuration.setter
    def destinations_configuration(self, value: Optional[pulumi.Input[DestinationsConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logsConfiguration")
    def logs_configuration(self) -> Optional[pulumi.Input[LogsConfigurationArgs]]:
        
        ...
    
    @logs_configuration.setter
    def logs_configuration(self, value: Optional[pulumi.Input[LogsConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricsConfiguration")
    def metrics_configuration(self) -> Optional[pulumi.Input[MetricsConfigurationArgs]]:
        
        ...
    
    @metrics_configuration.setter
    def metrics_configuration(self, value: Optional[pulumi.Input[MetricsConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tracesConfiguration")
    def traces_configuration(self) -> Optional[pulumi.Input[TracesConfigurationArgs]]:
        
        ...
    
    @traces_configuration.setter
    def traces_configuration(self, value: Optional[pulumi.Input[TracesConfigurationArgs]]): # -> None:
        ...
    


class OtlpConfigurationArgsDict(TypedDict):
    
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[HeaderArgsDict]]]]
    insecure: NotRequired[pulumi.Input[_builtins.bool]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OtlpConfigurationArgs:
    def __init__(__self__, *, endpoint: Optional[pulumi.Input[_builtins.str]] = ..., headers: Optional[pulumi.Input[Sequence[pulumi.Input[HeaderArgs]]]] = ..., insecure: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HeaderArgs]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HeaderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def insecure(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @insecure.setter
    def insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PreBuildStepArgsDict(TypedDict):
    
    description: NotRequired[pulumi.Input[_builtins.str]]
    http_get: NotRequired[pulumi.Input[HttpGetArgsDict]]
    scripts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class PreBuildStepArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., http_get: Optional[pulumi.Input[HttpGetArgs]] = ..., scripts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[pulumi.Input[HttpGetArgs]]:
        
        ...
    
    @http_get.setter
    def http_get(self, value: Optional[pulumi.Input[HttpGetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scripts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scripts.setter
    def scripts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, actions_required: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]): # -> None:
        ...
    


class QueueScaleRuleArgsDict(TypedDict):
    
    account_name: NotRequired[pulumi.Input[_builtins.str]]
    auth: NotRequired[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgsDict]]]]
    identity: NotRequired[pulumi.Input[_builtins.str]]
    queue_length: NotRequired[pulumi.Input[_builtins.int]]
    queue_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class QueueScaleRuleArgs:
    def __init__(__self__, *, account_name: Optional[pulumi.Input[_builtins.str]] = ..., auth: Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]] = ..., identity: Optional[pulumi.Input[_builtins.str]] = ..., queue_length: Optional[pulumi.Input[_builtins.int]] = ..., queue_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]]:
        
        ...
    
    @auth.setter
    def auth(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueLength")
    def queue_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @queue_length.setter
    def queue_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueName")
    def queue_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @queue_name.setter
    def queue_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegistryCredentialsArgsDict(TypedDict):
    
    identity: NotRequired[pulumi.Input[_builtins.str]]
    password_secret_ref: NotRequired[pulumi.Input[_builtins.str]]
    server: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegistryCredentialsArgs:
    def __init__(__self__, *, identity: Optional[pulumi.Input[_builtins.str]] = ..., password_secret_ref: Optional[pulumi.Input[_builtins.str]] = ..., server: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSecretRef")
    def password_secret_ref(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_secret_ref.setter
    def password_secret_ref(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server.setter
    def server(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegistryInfoArgsDict(TypedDict):
    
    registry_password: NotRequired[pulumi.Input[_builtins.str]]
    registry_url: NotRequired[pulumi.Input[_builtins.str]]
    registry_user_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegistryInfoArgs:
    def __init__(__self__, *, registry_password: Optional[pulumi.Input[_builtins.str]] = ..., registry_url: Optional[pulumi.Input[_builtins.str]] = ..., registry_user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryPassword")
    def registry_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @registry_password.setter
    def registry_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryUrl")
    def registry_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @registry_url.setter
    def registry_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryUserName")
    def registry_user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @registry_user_name.setter
    def registry_user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuntimeDotnetArgsDict(TypedDict):
    
    auto_configure_data_protection: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class RuntimeDotnetArgs:
    def __init__(__self__, *, auto_configure_data_protection: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoConfigureDataProtection")
    def auto_configure_data_protection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_configure_data_protection.setter
    def auto_configure_data_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class RuntimeJavaAgentArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    logging: NotRequired[pulumi.Input[RuntimeLoggingArgsDict]]


@pulumi.input_type
class RuntimeJavaAgentArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., logging: Optional[pulumi.Input[RuntimeLoggingArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input[RuntimeLoggingArgs]]:
        
        ...
    
    @logging.setter
    def logging(self, value: Optional[pulumi.Input[RuntimeLoggingArgs]]): # -> None:
        ...
    


class RuntimeJavaArgsDict(TypedDict):
    
    enable_metrics: NotRequired[pulumi.Input[_builtins.bool]]
    java_agent: NotRequired[pulumi.Input[RuntimeJavaAgentArgsDict]]


@pulumi.input_type
class RuntimeJavaArgs:
    def __init__(__self__, *, enable_metrics: Optional[pulumi.Input[_builtins.bool]] = ..., java_agent: Optional[pulumi.Input[RuntimeJavaAgentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMetrics")
    def enable_metrics(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_metrics.setter
    def enable_metrics(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="javaAgent")
    def java_agent(self) -> Optional[pulumi.Input[RuntimeJavaAgentArgs]]:
        
        ...
    
    @java_agent.setter
    def java_agent(self, value: Optional[pulumi.Input[RuntimeJavaAgentArgs]]): # -> None:
        ...
    


class RuntimeLoggingArgsDict(TypedDict):
    
    logger_settings: NotRequired[pulumi.Input[Sequence[pulumi.Input[LoggerSettingArgsDict]]]]


@pulumi.input_type
class RuntimeLoggingArgs:
    def __init__(__self__, *, logger_settings: Optional[pulumi.Input[Sequence[pulumi.Input[LoggerSettingArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggerSettings")
    def logger_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LoggerSettingArgs]]]]:
        
        ...
    
    @logger_settings.setter
    def logger_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LoggerSettingArgs]]]]): # -> None:
        ...
    


class RuntimeArgsDict(TypedDict):
    
    dotnet: NotRequired[pulumi.Input[RuntimeDotnetArgsDict]]
    java: NotRequired[pulumi.Input[RuntimeJavaArgsDict]]


@pulumi.input_type
class RuntimeArgs:
    def __init__(__self__, *, dotnet: Optional[pulumi.Input[RuntimeDotnetArgs]] = ..., java: Optional[pulumi.Input[RuntimeJavaArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dotnet(self) -> Optional[pulumi.Input[RuntimeDotnetArgs]]:
        
        ...
    
    @dotnet.setter
    def dotnet(self, value: Optional[pulumi.Input[RuntimeDotnetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def java(self) -> Optional[pulumi.Input[RuntimeJavaArgs]]:
        
        ...
    
    @java.setter
    def java(self, value: Optional[pulumi.Input[RuntimeJavaArgs]]): # -> None:
        ...
    


class ScaleConfigurationArgsDict(TypedDict):
    
    max_concurrent_sessions: NotRequired[pulumi.Input[_builtins.int]]
    ready_session_instances: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ScaleConfigurationArgs:
    def __init__(__self__, *, max_concurrent_sessions: Optional[pulumi.Input[_builtins.int]] = ..., ready_session_instances: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentSessions")
    def max_concurrent_sessions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrent_sessions.setter
    def max_concurrent_sessions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readySessionInstances")
    def ready_session_instances(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ready_session_instances.setter
    def ready_session_instances(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ScaleRuleAuthArgsDict(TypedDict):
    
    secret_ref: NotRequired[pulumi.Input[_builtins.str]]
    trigger_parameter: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ScaleRuleAuthArgs:
    def __init__(__self__, *, secret_ref: Optional[pulumi.Input[_builtins.str]] = ..., trigger_parameter: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_ref.setter
    def secret_ref(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerParameter")
    def trigger_parameter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trigger_parameter.setter
    def trigger_parameter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ScaleRuleArgsDict(TypedDict):
    
    azure_queue: NotRequired[pulumi.Input[QueueScaleRuleArgsDict]]
    custom: NotRequired[pulumi.Input[CustomScaleRuleArgsDict]]
    http: NotRequired[pulumi.Input[HttpScaleRuleArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    tcp: NotRequired[pulumi.Input[TcpScaleRuleArgsDict]]


@pulumi.input_type
class ScaleRuleArgs:
    def __init__(__self__, *, azure_queue: Optional[pulumi.Input[QueueScaleRuleArgs]] = ..., custom: Optional[pulumi.Input[CustomScaleRuleArgs]] = ..., http: Optional[pulumi.Input[HttpScaleRuleArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., tcp: Optional[pulumi.Input[TcpScaleRuleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureQueue")
    def azure_queue(self) -> Optional[pulumi.Input[QueueScaleRuleArgs]]:
        
        ...
    
    @azure_queue.setter
    def azure_queue(self, value: Optional[pulumi.Input[QueueScaleRuleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input[CustomScaleRuleArgs]]:
        
        ...
    
    @custom.setter
    def custom(self, value: Optional[pulumi.Input[CustomScaleRuleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def http(self) -> Optional[pulumi.Input[HttpScaleRuleArgs]]:
        
        ...
    
    @http.setter
    def http(self, value: Optional[pulumi.Input[HttpScaleRuleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tcp(self) -> Optional[pulumi.Input[TcpScaleRuleArgs]]:
        
        ...
    
    @tcp.setter
    def tcp(self, value: Optional[pulumi.Input[TcpScaleRuleArgs]]): # -> None:
        ...
    


class ScaleArgsDict(TypedDict):
    
    cooldown_period: NotRequired[pulumi.Input[_builtins.int]]
    max_replicas: NotRequired[pulumi.Input[_builtins.int]]
    min_replicas: NotRequired[pulumi.Input[_builtins.int]]
    polling_interval: NotRequired[pulumi.Input[_builtins.int]]
    rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[ScaleRuleArgsDict]]]]


@pulumi.input_type
class ScaleArgs:
    def __init__(__self__, *, cooldown_period: Optional[pulumi.Input[_builtins.int]] = ..., max_replicas: Optional[pulumi.Input[_builtins.int]] = ..., min_replicas: Optional[pulumi.Input[_builtins.int]] = ..., polling_interval: Optional[pulumi.Input[_builtins.int]] = ..., rules: Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cooldownPeriod")
    def cooldown_period(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cooldown_period.setter
    def cooldown_period(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxReplicas")
    def max_replicas(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_replicas.setter
    def max_replicas(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minReplicas")
    def min_replicas(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_replicas.setter
    def min_replicas(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pollingInterval")
    def polling_interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @polling_interval.setter
    def polling_interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleArgs]]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleArgs]]]]): # -> None:
        ...
    


class ScgRouteArgsDict(TypedDict):
    
    id: pulumi.Input[_builtins.str]
    uri: pulumi.Input[_builtins.str]
    filters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    order: NotRequired[pulumi.Input[_builtins.float]]
    predicates: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ScgRouteArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], uri: pulumi.Input[_builtins.str], filters: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., order: Optional[pulumi.Input[_builtins.float]] = ..., predicates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @filters.setter
    def filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def predicates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @predicates.setter
    def predicates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ScheduledEntryArgsDict(TypedDict):
    
    duration_hours: pulumi.Input[_builtins.int]
    start_hour_utc: pulumi.Input[_builtins.int]
    week_day: pulumi.Input[WeekDay]


@pulumi.input_type
class ScheduledEntryArgs:
    def __init__(__self__, *, duration_hours: pulumi.Input[_builtins.int], start_hour_utc: pulumi.Input[_builtins.int], week_day: pulumi.Input[WeekDay]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="durationHours")
    def duration_hours(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @duration_hours.setter
    def duration_hours(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startHourUtc")
    def start_hour_utc(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @start_hour_utc.setter
    def start_hour_utc(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekDay")
    def week_day(self) -> pulumi.Input[WeekDay]:
        
        ...
    
    @week_day.setter
    def week_day(self, value: pulumi.Input[WeekDay]): # -> None:
        ...
    


class SecretKeyVaultPropertiesArgsDict(TypedDict):
    
    identity: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecretKeyVaultPropertiesArgs:
    def __init__(__self__, *, identity: Optional[pulumi.Input[_builtins.str]] = ..., key_vault_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_url.setter
    def key_vault_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecretVolumeItemArgsDict(TypedDict):
    
    path: NotRequired[pulumi.Input[_builtins.str]]
    secret_ref: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecretVolumeItemArgs:
    def __init__(__self__, *, path: Optional[pulumi.Input[_builtins.str]] = ..., secret_ref: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_ref.setter
    def secret_ref(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecretArgsDict(TypedDict):
    
    identity: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_url: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecretArgs:
    def __init__(__self__, *, identity: Optional[pulumi.Input[_builtins.str]] = ..., key_vault_url: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultUrl")
    def key_vault_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_url.setter
    def key_vault_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceBindArgsDict(TypedDict):
    
    client_type: NotRequired[pulumi.Input[_builtins.str]]
    customized_keys: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    service_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceBindArgs:
    def __init__(__self__, *, client_type: Optional[pulumi.Input[_builtins.str]] = ..., customized_keys: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., service_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientType")
    def client_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_type.setter
    def client_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customizedKeys")
    def customized_keys(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @customized_keys.setter
    def customized_keys(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceArgsDict(TypedDict):
    
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SessionContainerResourcesArgsDict(TypedDict):
    
    cpu: NotRequired[pulumi.Input[_builtins.float]]
    memory: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SessionContainerResourcesArgs:
    def __init__(__self__, *, cpu: Optional[pulumi.Input[_builtins.float]] = ..., memory: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SessionContainerArgsDict(TypedDict):
    
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    command: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    env: NotRequired[pulumi.Input[Sequence[pulumi.Input[EnvironmentVarArgsDict]]]]
    image: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    probes: NotRequired[pulumi.Input[Sequence[pulumi.Input[SessionProbeArgsDict]]]]
    resources: NotRequired[pulumi.Input[SessionContainerResourcesArgsDict]]


@pulumi.input_type
class SessionContainerArgs:
    def __init__(__self__, *, args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., command: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., env: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVarArgs]]]] = ..., image: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., probes: Optional[pulumi.Input[Sequence[pulumi.Input[SessionProbeArgs]]]] = ..., resources: Optional[pulumi.Input[SessionContainerResourcesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @args.setter
    def args(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def command(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @command.setter
    def command(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def env(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVarArgs]]]]:
        
        ...
    
    @env.setter
    def env(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVarArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def probes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SessionProbeArgs]]]]:
        
        ...
    
    @probes.setter
    def probes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SessionProbeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[SessionContainerResourcesArgs]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[SessionContainerResourcesArgs]]): # -> None:
        ...
    


class SessionIngressArgsDict(TypedDict):
    
    target_port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class SessionIngressArgs:
    def __init__(__self__, *, target_port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPort")
    def target_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_port.setter
    def target_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SessionNetworkConfigurationArgsDict(TypedDict):
    
    status: NotRequired[pulumi.Input[Union[_builtins.str, SessionNetworkStatus]]]


@pulumi.input_type
class SessionNetworkConfigurationArgs:
    def __init__(__self__, *, status: Optional[pulumi.Input[Union[_builtins.str, SessionNetworkStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionNetworkStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionNetworkStatus]]]): # -> None:
        ...
    


class SessionPoolSecretArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SessionPoolSecretArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SessionProbeHttpGetArgsDict(TypedDict):
    
    port: pulumi.Input[_builtins.int]
    host: NotRequired[pulumi.Input[_builtins.str]]
    http_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[SessionProbeHttpHeadersArgsDict]]]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    scheme: NotRequired[pulumi.Input[Union[_builtins.str, Scheme]]]


@pulumi.input_type
class SessionProbeHttpGetArgs:
    def __init__(__self__, *, port: pulumi.Input[_builtins.int], host: Optional[pulumi.Input[_builtins.str]] = ..., http_headers: Optional[pulumi.Input[Sequence[pulumi.Input[SessionProbeHttpHeadersArgs]]]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., scheme: Optional[pulumi.Input[Union[_builtins.str, Scheme]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SessionProbeHttpHeadersArgs]]]]:
        
        ...
    
    @http_headers.setter
    def http_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SessionProbeHttpHeadersArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[pulumi.Input[Union[_builtins.str, Scheme]]]:
        
        ...
    
    @scheme.setter
    def scheme(self, value: Optional[pulumi.Input[Union[_builtins.str, Scheme]]]): # -> None:
        ...
    


class SessionProbeHttpHeadersArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class SessionProbeHttpHeadersArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SessionProbeTcpSocketArgsDict(TypedDict):
    
    port: pulumi.Input[_builtins.int]
    host: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SessionProbeTcpSocketArgs:
    def __init__(__self__, *, port: pulumi.Input[_builtins.int], host: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SessionProbeArgsDict(TypedDict):
    
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    http_get: NotRequired[pulumi.Input[SessionProbeHttpGetArgsDict]]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    success_threshold: NotRequired[pulumi.Input[_builtins.int]]
    tcp_socket: NotRequired[pulumi.Input[SessionProbeTcpSocketArgsDict]]
    termination_grace_period_seconds: NotRequired[pulumi.Input[_builtins.float]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, SessionProbeType]]]


@pulumi.input_type
class SessionProbeArgs:
    def __init__(__self__, *, failure_threshold: Optional[pulumi.Input[_builtins.int]] = ..., http_get: Optional[pulumi.Input[SessionProbeHttpGetArgs]] = ..., initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ..., period_seconds: Optional[pulumi.Input[_builtins.int]] = ..., success_threshold: Optional[pulumi.Input[_builtins.int]] = ..., tcp_socket: Optional[pulumi.Input[SessionProbeTcpSocketArgs]] = ..., termination_grace_period_seconds: Optional[pulumi.Input[_builtins.float]] = ..., timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, SessionProbeType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[pulumi.Input[SessionProbeHttpGetArgs]]:
        
        ...
    
    @http_get.setter
    def http_get(self, value: Optional[pulumi.Input[SessionProbeHttpGetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @success_threshold.setter
    def success_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(self) -> Optional[pulumi.Input[SessionProbeTcpSocketArgs]]:
        
        ...
    
    @tcp_socket.setter
    def tcp_socket(self, value: Optional[pulumi.Input[SessionProbeTcpSocketArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationGracePeriodSeconds")
    def termination_grace_period_seconds(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @termination_grace_period_seconds.setter
    def termination_grace_period_seconds(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionProbeType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionProbeType]]]): # -> None:
        ...
    


class SessionRegistryCredentialsArgsDict(TypedDict):
    
    identity: NotRequired[pulumi.Input[_builtins.str]]
    password_secret_ref: NotRequired[pulumi.Input[_builtins.str]]
    server: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SessionRegistryCredentialsArgs:
    def __init__(__self__, *, identity: Optional[pulumi.Input[_builtins.str]] = ..., password_secret_ref: Optional[pulumi.Input[_builtins.str]] = ..., server: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSecretRef")
    def password_secret_ref(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_secret_ref.setter
    def password_secret_ref(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server.setter
    def server(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SmbStorageArgsDict(TypedDict):
    
    access_mode: NotRequired[pulumi.Input[Union[_builtins.str, AccessMode]]]
    domain: NotRequired[pulumi.Input[_builtins.str]]
    host: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    share_name: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SmbStorageArgs:
    def __init__(__self__, *, access_mode: Optional[pulumi.Input[Union[_builtins.str, AccessMode]]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., share_name: Optional[pulumi.Input[_builtins.str]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, AccessMode]]]:
        
        ...
    
    @access_mode.setter
    def access_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, AccessMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @share_name.setter
    def share_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SpringBootAdminComponentArgsDict(TypedDict):
    
    component_type: pulumi.Input[_builtins.str]
    configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgsDict]]]]
    scale: NotRequired[pulumi.Input[JavaComponentPropertiesScaleArgsDict]]
    service_binds: NotRequired[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgsDict]]]]


@pulumi.input_type
class SpringBootAdminComponentArgs:
    def __init__(__self__, *, component_type: pulumi.Input[_builtins.str], configurations: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]] = ..., scale: Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]] = ..., service_binds: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @component_type.setter
    def component_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]]:
        
        ...
    
    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]]:
        
        ...
    
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]]:
        
        ...
    
    @service_binds.setter
    def service_binds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]]): # -> None:
        ...
    


class SpringCloudConfigComponentArgsDict(TypedDict):
    
    component_type: pulumi.Input[_builtins.str]
    configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgsDict]]]]
    scale: NotRequired[pulumi.Input[JavaComponentPropertiesScaleArgsDict]]
    service_binds: NotRequired[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgsDict]]]]


@pulumi.input_type
class SpringCloudConfigComponentArgs:
    def __init__(__self__, *, component_type: pulumi.Input[_builtins.str], configurations: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]] = ..., scale: Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]] = ..., service_binds: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @component_type.setter
    def component_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]]:
        
        ...
    
    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]]:
        
        ...
    
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]]:
        
        ...
    
    @service_binds.setter
    def service_binds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]]): # -> None:
        ...
    


class SpringCloudEurekaComponentArgsDict(TypedDict):
    
    component_type: pulumi.Input[_builtins.str]
    configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgsDict]]]]
    scale: NotRequired[pulumi.Input[JavaComponentPropertiesScaleArgsDict]]
    service_binds: NotRequired[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgsDict]]]]


@pulumi.input_type
class SpringCloudEurekaComponentArgs:
    def __init__(__self__, *, component_type: pulumi.Input[_builtins.str], configurations: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]] = ..., scale: Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]] = ..., service_binds: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @component_type.setter
    def component_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]]:
        
        ...
    
    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]]:
        
        ...
    
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]]:
        
        ...
    
    @service_binds.setter
    def service_binds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]]): # -> None:
        ...
    


class SpringCloudGatewayComponentArgsDict(TypedDict):
    
    component_type: pulumi.Input[_builtins.str]
    configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgsDict]]]]
    scale: NotRequired[pulumi.Input[JavaComponentPropertiesScaleArgsDict]]
    service_binds: NotRequired[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgsDict]]]]
    spring_cloud_gateway_routes: NotRequired[pulumi.Input[Sequence[pulumi.Input[ScgRouteArgsDict]]]]


@pulumi.input_type
class SpringCloudGatewayComponentArgs:
    def __init__(__self__, *, component_type: pulumi.Input[_builtins.str], configurations: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]] = ..., scale: Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]] = ..., service_binds: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]] = ..., spring_cloud_gateway_routes: Optional[pulumi.Input[Sequence[pulumi.Input[ScgRouteArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentType")
    def component_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @component_type.setter
    def component_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]]:
        
        ...
    
    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentConfigurationPropertyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]]:
        
        ...
    
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[JavaComponentPropertiesScaleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]]:
        
        ...
    
    @service_binds.setter
    def service_binds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JavaComponentServiceBindArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="springCloudGatewayRoutes")
    def spring_cloud_gateway_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScgRouteArgs]]]]:
        
        ...
    
    @spring_cloud_gateway_routes.setter
    def spring_cloud_gateway_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScgRouteArgs]]]]): # -> None:
        ...
    


class TcpConnectionPoolArgsDict(TypedDict):
    
    max_connections: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TcpConnectionPoolArgs:
    def __init__(__self__, *, max_connections: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_connections.setter
    def max_connections(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TcpRetryPolicyArgsDict(TypedDict):
    
    max_connect_attempts: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TcpRetryPolicyArgs:
    def __init__(__self__, *, max_connect_attempts: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConnectAttempts")
    def max_connect_attempts(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_connect_attempts.setter
    def max_connect_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TcpScaleRuleArgsDict(TypedDict):
    
    auth: NotRequired[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgsDict]]]]
    identity: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class TcpScaleRuleArgs:
    def __init__(__self__, *, auth: Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]] = ..., identity: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]]:
        
        ...
    
    @auth.setter
    def auth(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ScaleRuleAuthArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class TemplateArgsDict(TypedDict):
    
    containers: NotRequired[pulumi.Input[Sequence[pulumi.Input[ContainerArgsDict]]]]
    init_containers: NotRequired[pulumi.Input[Sequence[pulumi.Input[InitContainerArgsDict]]]]
    revision_suffix: NotRequired[pulumi.Input[_builtins.str]]
    scale: NotRequired[pulumi.Input[ScaleArgsDict]]
    service_binds: NotRequired[pulumi.Input[Sequence[pulumi.Input[ServiceBindArgsDict]]]]
    termination_grace_period_seconds: NotRequired[pulumi.Input[_builtins.float]]
    volumes: NotRequired[pulumi.Input[Sequence[pulumi.Input[VolumeArgsDict]]]]


@pulumi.input_type
class TemplateArgs:
    def __init__(__self__, *, containers: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerArgs]]]] = ..., init_containers: Optional[pulumi.Input[Sequence[pulumi.Input[InitContainerArgs]]]] = ..., revision_suffix: Optional[pulumi.Input[_builtins.str]] = ..., scale: Optional[pulumi.Input[ScaleArgs]] = ..., service_binds: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceBindArgs]]]] = ..., termination_grace_period_seconds: Optional[pulumi.Input[_builtins.float]] = ..., volumes: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContainerArgs]]]]:
        
        ...
    
    @containers.setter
    def containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initContainers")
    def init_containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InitContainerArgs]]]]:
        
        ...
    
    @init_containers.setter
    def init_containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InitContainerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionSuffix")
    def revision_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @revision_suffix.setter
    def revision_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[ScaleArgs]]:
        
        ...
    
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[ScaleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceBinds")
    def service_binds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceBindArgs]]]]:
        
        ...
    
    @service_binds.setter
    def service_binds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceBindArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminationGracePeriodSeconds")
    def termination_grace_period_seconds(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @termination_grace_period_seconds.setter
    def termination_grace_period_seconds(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeArgs]]]]:
        
        ...
    
    @volumes.setter
    def volumes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeArgs]]]]): # -> None:
        ...
    


class TimeoutPolicyArgsDict(TypedDict):
    
    connection_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]
    response_timeout_in_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TimeoutPolicyArgs:
    def __init__(__self__, *, connection_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., response_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTimeoutInSeconds")
    def connection_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @connection_timeout_in_seconds.setter
    def connection_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseTimeoutInSeconds")
    def response_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @response_timeout_in_seconds.setter
    def response_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TokenStoreArgsDict(TypedDict):
    
    azure_blob_storage: NotRequired[pulumi.Input[BlobStorageTokenStoreArgsDict]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    token_refresh_extension_hours: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class TokenStoreArgs:
    def __init__(__self__, *, azure_blob_storage: Optional[pulumi.Input[BlobStorageTokenStoreArgs]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., token_refresh_extension_hours: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureBlobStorage")
    def azure_blob_storage(self) -> Optional[pulumi.Input[BlobStorageTokenStoreArgs]]:
        
        ...
    
    @azure_blob_storage.setter
    def azure_blob_storage(self, value: Optional[pulumi.Input[BlobStorageTokenStoreArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenRefreshExtensionHours")
    def token_refresh_extension_hours(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @token_refresh_extension_hours.setter
    def token_refresh_extension_hours(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class TracesConfigurationArgsDict(TypedDict):
    
    destinations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    include_dapr: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class TracesConfigurationArgs:
    def __init__(__self__, *, destinations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., include_dapr: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @destinations.setter
    def destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeDapr")
    def include_dapr(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_dapr.setter
    def include_dapr(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class TrafficWeightArgsDict(TypedDict):
    
    label: NotRequired[pulumi.Input[_builtins.str]]
    latest_revision: NotRequired[pulumi.Input[_builtins.bool]]
    revision_name: NotRequired[pulumi.Input[_builtins.str]]
    weight: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class TrafficWeightArgs:
    def __init__(__self__, *, label: Optional[pulumi.Input[_builtins.str]] = ..., latest_revision: Optional[pulumi.Input[_builtins.bool]] = ..., revision_name: Optional[pulumi.Input[_builtins.str]] = ..., weight: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestRevision")
    def latest_revision(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @latest_revision.setter
    def latest_revision(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="revisionName")
    def revision_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @revision_name.setter
    def revision_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @weight.setter
    def weight(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class TwitterRegistrationArgsDict(TypedDict):
    
    consumer_key: NotRequired[pulumi.Input[_builtins.str]]
    consumer_secret_setting_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TwitterRegistrationArgs:
    def __init__(__self__, *, consumer_key: Optional[pulumi.Input[_builtins.str]] = ..., consumer_secret_setting_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerKey")
    def consumer_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @consumer_key.setter
    def consumer_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerSecretSettingName")
    def consumer_secret_setting_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @consumer_secret_setting_name.setter
    def consumer_secret_setting_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TwitterArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    registration: NotRequired[pulumi.Input[TwitterRegistrationArgsDict]]


@pulumi.input_type
class TwitterArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., registration: Optional[pulumi.Input[TwitterRegistrationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def registration(self) -> Optional[pulumi.Input[TwitterRegistrationArgs]]:
        
        ...
    
    @registration.setter
    def registration(self, value: Optional[pulumi.Input[TwitterRegistrationArgs]]): # -> None:
        ...
    


class VnetConfigurationArgsDict(TypedDict):
    
    docker_bridge_cidr: NotRequired[pulumi.Input[_builtins.str]]
    infrastructure_subnet_id: NotRequired[pulumi.Input[_builtins.str]]
    internal: NotRequired[pulumi.Input[_builtins.bool]]
    platform_reserved_cidr: NotRequired[pulumi.Input[_builtins.str]]
    platform_reserved_dns_ip: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VnetConfigurationArgs:
    def __init__(__self__, *, docker_bridge_cidr: Optional[pulumi.Input[_builtins.str]] = ..., infrastructure_subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., internal: Optional[pulumi.Input[_builtins.bool]] = ..., platform_reserved_cidr: Optional[pulumi.Input[_builtins.str]] = ..., platform_reserved_dns_ip: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dockerBridgeCidr")
    def docker_bridge_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @docker_bridge_cidr.setter
    def docker_bridge_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="infrastructureSubnetId")
    def infrastructure_subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @infrastructure_subnet_id.setter
    def infrastructure_subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def internal(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @internal.setter
    def internal(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformReservedCidr")
    def platform_reserved_cidr(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform_reserved_cidr.setter
    def platform_reserved_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="platformReservedDnsIP")
    def platform_reserved_dns_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform_reserved_dns_ip.setter
    def platform_reserved_dns_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeMountArgsDict(TypedDict):
    
    mount_path: NotRequired[pulumi.Input[_builtins.str]]
    sub_path: NotRequired[pulumi.Input[_builtins.str]]
    volume_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeMountArgs:
    def __init__(__self__, *, mount_path: Optional[pulumi.Input[_builtins.str]] = ..., sub_path: Optional[pulumi.Input[_builtins.str]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mount_path.setter
    def mount_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sub_path.setter
    def sub_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeArgsDict(TypedDict):
    
    mount_options: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    secrets: NotRequired[pulumi.Input[Sequence[pulumi.Input[SecretVolumeItemArgsDict]]]]
    storage_name: NotRequired[pulumi.Input[_builtins.str]]
    storage_type: NotRequired[pulumi.Input[Union[_builtins.str, StorageType]]]


@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *, mount_options: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., secrets: Optional[pulumi.Input[Sequence[pulumi.Input[SecretVolumeItemArgs]]]] = ..., storage_name: Optional[pulumi.Input[_builtins.str]] = ..., storage_type: Optional[pulumi.Input[Union[_builtins.str, StorageType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mount_options.setter
    def mount_options(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecretVolumeItemArgs]]]]:
        
        ...
    
    @secrets.setter
    def secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SecretVolumeItemArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageName")
    def storage_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_name.setter
    def storage_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[Union[_builtins.str, StorageType]]]:
        
        ...
    
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[Union[_builtins.str, StorageType]]]): # -> None:
        ...
    


class WorkloadProfileArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    workload_profile_type: pulumi.Input[_builtins.str]
    enable_fips: NotRequired[pulumi.Input[_builtins.bool]]
    maximum_count: NotRequired[pulumi.Input[_builtins.int]]
    minimum_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class WorkloadProfileArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], workload_profile_type: pulumi.Input[_builtins.str], enable_fips: Optional[pulumi.Input[_builtins.bool]] = ..., maximum_count: Optional[pulumi.Input[_builtins.int]] = ..., minimum_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadProfileType")
    def workload_profile_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workload_profile_type.setter
    def workload_profile_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableFips")
    def enable_fips(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_fips.setter
    def enable_fips(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumCount")
    def maximum_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_count.setter
    def maximum_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumCount")
    def minimum_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minimum_count.setter
    def minimum_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


