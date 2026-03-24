

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectionBitbucketCloudConfig', 'ConnectionBitbucketCloudConfigAuthorizerCredential', ..., 'ConnectionBitbucketDataCenterConfig', ..., ..., ..., 'ConnectionGithubConfig', 'ConnectionGithubConfigAuthorizerCredential', 'ConnectionGithubEnterpriseConfig', ..., 'ConnectionGitlabConfig', 'ConnectionGitlabConfigAuthorizerCredential', 'ConnectionGitlabConfigReadAuthorizerCredential', 'ConnectionGitlabConfigServiceDirectoryConfig', 'ConnectionIAMBindingCondition', 'ConnectionIAMMemberCondition', 'ConnectionInstallationState']
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
    
    def __init__(__self__, *, authorizer_credential: outputs.ConnectionBitbucketDataCenterConfigAuthorizerCredential, host_uri: _builtins.str, read_authorizer_credential: outputs.ConnectionBitbucketDataCenterConfigReadAuthorizerCredential, webhook_secret_secret_version: _builtins.str, server_version: Optional[_builtins.str] = ..., service_directory_config: Optional[outputs.ConnectionBitbucketDataCenterConfigServiceDirectoryConfig] = ..., ssl_ca: Optional[_builtins.str] = ...) -> None:
        
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
    @pulumi.getter(name="sslCa")
    def ssl_ca(self) -> Optional[_builtins.str]:
        
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
class ConnectionGithubConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, app_installation_id: Optional[_builtins.int] = ..., authorizer_credential: Optional[outputs.ConnectionGithubConfigAuthorizerCredential] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appInstallationId")
    def app_installation_id(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerCredential")
    def authorizer_credential(self) -> Optional[outputs.ConnectionGithubConfigAuthorizerCredential]:
        
        ...
    


@pulumi.output_type
class ConnectionGithubConfigAuthorizerCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oauth_token_secret_version: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthTokenSecretVersion")
    def oauth_token_secret_version(self) -> Optional[_builtins.str]:
        
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
    
    def __init__(__self__, *, host_uri: _builtins.str, app_id: Optional[_builtins.int] = ..., app_installation_id: Optional[_builtins.int] = ..., app_slug: Optional[_builtins.str] = ..., private_key_secret_version: Optional[_builtins.str] = ..., service_directory_config: Optional[outputs.ConnectionGithubEnterpriseConfigServiceDirectoryConfig] = ..., ssl_ca: Optional[_builtins.str] = ..., webhook_secret_secret_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appInstallationId")
    def app_installation_id(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSlug")
    def app_slug(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKeySecretVersion")
    def private_key_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(self) -> Optional[outputs.ConnectionGithubEnterpriseConfigServiceDirectoryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCa")
    def ssl_ca(self) -> Optional[_builtins.str]:
        
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
    
    def __init__(__self__, *, authorizer_credential: outputs.ConnectionGitlabConfigAuthorizerCredential, read_authorizer_credential: outputs.ConnectionGitlabConfigReadAuthorizerCredential, webhook_secret_secret_version: _builtins.str, host_uri: Optional[_builtins.str] = ..., server_version: Optional[_builtins.str] = ..., service_directory_config: Optional[outputs.ConnectionGitlabConfigServiceDirectoryConfig] = ..., ssl_ca: Optional[_builtins.str] = ...) -> None:
        
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
    
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(self) -> Optional[outputs.ConnectionGitlabConfigServiceDirectoryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCa")
    def ssl_ca(self) -> Optional[_builtins.str]:
        
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
class ConnectionGitlabConfigServiceDirectoryConfig(dict):
    def __init__(__self__, *, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConnectionIAMBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ConnectionIAMMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
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
    


