

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountConnectorProviderOauthConfig', 'ConnectionBitbucketCloudConfig', 'ConnectionBitbucketCloudConfigAuthorizerCredential', ..., 'ConnectionBitbucketDataCenterConfig', ..., ..., ..., 'ConnectionCryptoKeyConfig', 'ConnectionGithubConfig', 'ConnectionGithubConfigAuthorizerCredential', 'ConnectionGithubEnterpriseConfig', ..., 'ConnectionGitlabConfig', 'ConnectionGitlabConfigAuthorizerCredential', 'ConnectionGitlabConfigReadAuthorizerCredential', 'ConnectionGitlabEnterpriseConfig', ..., ..., ..., 'ConnectionHttpConfig', 'ConnectionHttpConfigBasicAuthentication', 'ConnectionHttpConfigBearerTokenAuthentication', 'ConnectionHttpConfigServiceDirectoryConfig', 'ConnectionInstallationState', 'InsightsConfigArtifactConfig', 'InsightsConfigArtifactConfigGoogleArtifactAnalysis', 'InsightsConfigArtifactConfigGoogleArtifactRegistry', 'InsightsConfigError', 'InsightsConfigErrorDetail', 'InsightsConfigRuntimeConfig', 'InsightsConfigRuntimeConfigAppHubWorkload', 'InsightsConfigRuntimeConfigGkeWorkload', 'InsightsConfigTargetProjects']
@pulumi.output_type
class AccountConnectorProviderOauthConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scopes: Sequence[_builtins.str], system_provider_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemProviderId")
    def system_provider_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionBitbucketCloudConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorizer_credential: outputs.ConnectionBitbucketCloudConfigAuthorizerCredential, read_authorizer_credential: outputs.ConnectionBitbucketCloudConfigReadAuthorizerCredential, webhook_secret_secret_version: _builtins.str, workspace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerCredential")
    def authorizer_credential(self) -> outputs.ConnectionBitbucketCloudConfigAuthorizerCredential:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readAuthorizerCredential")
    def read_authorizer_credential(self) -> outputs.ConnectionBitbucketCloudConfigReadAuthorizerCredential:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookSecretSecretVersion")
    def webhook_secret_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def workspace(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConnectionBitbucketCloudConfigAuthorizerCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_token_secret_version: _builtins.str, username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionBitbucketCloudConfigReadAuthorizerCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_token_secret_version: _builtins.str, username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionBitbucketDataCenterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorizer_credential: outputs.ConnectionBitbucketDataCenterConfigAuthorizerCredential, host_uri: _builtins.str, read_authorizer_credential: outputs.ConnectionBitbucketDataCenterConfigReadAuthorizerCredential, webhook_secret_secret_version: _builtins.str, server_version: Optional[_builtins.str] = ..., service_directory_config: Optional[outputs.ConnectionBitbucketDataCenterConfigServiceDirectoryConfig] = ..., ssl_ca_certificate: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerCredential")
    def authorizer_credential(self) -> outputs.ConnectionBitbucketDataCenterConfigAuthorizerCredential:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readAuthorizerCredential")
    def read_authorizer_credential(self) -> outputs.ConnectionBitbucketDataCenterConfigReadAuthorizerCredential:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookSecretSecretVersion")
    def webhook_secret_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(self) -> Optional[outputs.ConnectionBitbucketDataCenterConfigServiceDirectoryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCaCertificate")
    def ssl_ca_certificate(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionBitbucketDataCenterConfigAuthorizerCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_token_secret_version: _builtins.str, username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionBitbucketDataCenterConfigReadAuthorizerCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_token_secret_version: _builtins.str, username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionBitbucketDataCenterConfigServiceDirectoryConfig(dict):
    def __init__(__self__, *, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConnectionCryptoKeyConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key_reference: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyReference")
    def key_reference(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConnectionGithubConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, github_app: _builtins.str, app_installation_id: Optional[_builtins.str] = ..., authorizer_credential: Optional[outputs.ConnectionGithubConfigAuthorizerCredential] = ..., installation_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="githubApp")
    def github_app(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appInstallationId")
    def app_installation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerCredential")
    def authorizer_credential(self) -> Optional[outputs.ConnectionGithubConfigAuthorizerCredential]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installationUri")
    def installation_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionGithubConfigAuthorizerCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oauth_token_secret_version: _builtins.str, username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthTokenSecretVersion")
    def oauth_token_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionGithubEnterpriseConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, host_uri: _builtins.str, app_id: Optional[_builtins.str] = ..., app_installation_id: Optional[_builtins.str] = ..., app_slug: Optional[_builtins.str] = ..., installation_uri: Optional[_builtins.str] = ..., private_key_secret_version: Optional[_builtins.str] = ..., server_version: Optional[_builtins.str] = ..., service_directory_config: Optional[outputs.ConnectionGithubEnterpriseConfigServiceDirectoryConfig] = ..., ssl_ca_certificate: Optional[_builtins.str] = ..., webhook_secret_secret_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appInstallationId")
    def app_installation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSlug")
    def app_slug(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="installationUri")
    def installation_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKeySecretVersion")
    def private_key_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(self) -> Optional[outputs.ConnectionGithubEnterpriseConfigServiceDirectoryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCaCertificate")
    def ssl_ca_certificate(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookSecretSecretVersion")
    def webhook_secret_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionGithubEnterpriseConfigServiceDirectoryConfig(dict):
    def __init__(__self__, *, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConnectionGitlabConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorizer_credential: outputs.ConnectionGitlabConfigAuthorizerCredential, read_authorizer_credential: outputs.ConnectionGitlabConfigReadAuthorizerCredential, webhook_secret_secret_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerCredential")
    def authorizer_credential(self) -> outputs.ConnectionGitlabConfigAuthorizerCredential:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readAuthorizerCredential")
    def read_authorizer_credential(self) -> outputs.ConnectionGitlabConfigReadAuthorizerCredential:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookSecretSecretVersion")
    def webhook_secret_secret_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConnectionGitlabConfigAuthorizerCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_token_secret_version: _builtins.str, username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionGitlabConfigReadAuthorizerCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_token_secret_version: _builtins.str, username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionGitlabEnterpriseConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorizer_credential: outputs.ConnectionGitlabEnterpriseConfigAuthorizerCredential, host_uri: _builtins.str, read_authorizer_credential: outputs.ConnectionGitlabEnterpriseConfigReadAuthorizerCredential, webhook_secret_secret_version: _builtins.str, server_version: Optional[_builtins.str] = ..., service_directory_config: Optional[outputs.ConnectionGitlabEnterpriseConfigServiceDirectoryConfig] = ..., ssl_ca_certificate: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerCredential")
    def authorizer_credential(self) -> outputs.ConnectionGitlabEnterpriseConfigAuthorizerCredential:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readAuthorizerCredential")
    def read_authorizer_credential(self) -> outputs.ConnectionGitlabEnterpriseConfigReadAuthorizerCredential:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookSecretSecretVersion")
    def webhook_secret_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(self) -> Optional[outputs.ConnectionGitlabEnterpriseConfigServiceDirectoryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCaCertificate")
    def ssl_ca_certificate(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionGitlabEnterpriseConfigAuthorizerCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_token_secret_version: _builtins.str, username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionGitlabEnterpriseConfigReadAuthorizerCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, user_token_secret_version: _builtins.str, username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionGitlabEnterpriseConfigServiceDirectoryConfig(dict):
    def __init__(__self__, *, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConnectionHttpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, host_uri: _builtins.str, basic_authentication: Optional[outputs.ConnectionHttpConfigBasicAuthentication] = ..., bearer_token_authentication: Optional[outputs.ConnectionHttpConfigBearerTokenAuthentication] = ..., service_directory_config: Optional[outputs.ConnectionHttpConfigServiceDirectoryConfig] = ..., ssl_ca_certificate: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAuthentication")
    def basic_authentication(self) -> Optional[outputs.ConnectionHttpConfigBasicAuthentication]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bearerTokenAuthentication")
    def bearer_token_authentication(self) -> Optional[outputs.ConnectionHttpConfigBearerTokenAuthentication]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(self) -> Optional[outputs.ConnectionHttpConfigServiceDirectoryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCaCertificate")
    def ssl_ca_certificate(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionHttpConfigBasicAuthentication(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, username: _builtins.str, password_secret_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSecretVersion")
    def password_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionHttpConfigBearerTokenAuthentication(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, token_secret_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenSecretVersion")
    def token_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionHttpConfigServiceDirectoryConfig(dict):
    def __init__(__self__, *, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConnectionInstallationState(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_uri: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ..., stage: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionUri")
    def action_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsConfigArtifactConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, google_artifact_analysis: Optional[outputs.InsightsConfigArtifactConfigGoogleArtifactAnalysis] = ..., google_artifact_registry: Optional[outputs.InsightsConfigArtifactConfigGoogleArtifactRegistry] = ..., uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleArtifactAnalysis")
    def google_artifact_analysis(self) -> Optional[outputs.InsightsConfigArtifactConfigGoogleArtifactAnalysis]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleArtifactRegistry")
    def google_artifact_registry(self) -> Optional[outputs.InsightsConfigArtifactConfigGoogleArtifactRegistry]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsConfigArtifactConfigGoogleArtifactAnalysis(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, project_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InsightsConfigArtifactConfigGoogleArtifactRegistry(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, artifact_registry_package: _builtins.str, project_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactRegistryPackage")
    def artifact_registry_package(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InsightsConfigError(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., details: Optional[Sequence[outputs.InsightsConfigErrorDetail]] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[outputs.InsightsConfigErrorDetail]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsConfigErrorDetail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, detail_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailMessage")
    def detail_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsConfigRuntimeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, uri: _builtins.str, app_hub_workload: Optional[outputs.InsightsConfigRuntimeConfigAppHubWorkload] = ..., gke_workload: Optional[outputs.InsightsConfigRuntimeConfigGkeWorkload] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appHubWorkload")
    def app_hub_workload(self) -> Optional[outputs.InsightsConfigRuntimeConfigAppHubWorkload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeWorkload")
    def gke_workload(self) -> Optional[outputs.InsightsConfigRuntimeConfigGkeWorkload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsConfigRuntimeConfigAppHubWorkload(dict):
    def __init__(__self__, *, criticality: Optional[_builtins.str] = ..., environment: Optional[_builtins.str] = ..., workload: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def criticality(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def workload(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsConfigRuntimeConfigGkeWorkload(dict):
    def __init__(__self__, *, cluster: _builtins.str, deployment: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightsConfigTargetProjects(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, project_ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectIds")
    def project_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


