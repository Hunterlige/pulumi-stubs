import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccountConnectorProviderOauthConfigArgs",
    "AccountConnectorProviderOauthConfigArgsDict",
    "ConnectionBitbucketCloudConfigArgs",
    "ConnectionBitbucketCloudConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ConnectionBitbucketDataCenterConfigArgs",
    "ConnectionBitbucketDataCenterConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ConnectionCryptoKeyConfigArgs",
    "ConnectionCryptoKeyConfigArgsDict",
    "ConnectionGithubConfigArgs",
    "ConnectionGithubConfigArgsDict",
    "ConnectionGithubConfigAuthorizerCredentialArgs",
    "ConnectionGithubConfigAuthorizerCredentialArgsDict",
    "ConnectionGithubEnterpriseConfigArgs",
    "ConnectionGithubEnterpriseConfigArgsDict",
    ...,
    ...,
    "ConnectionGitlabConfigArgs",
    "ConnectionGitlabConfigArgsDict",
    "ConnectionGitlabConfigAuthorizerCredentialArgs",
    "ConnectionGitlabConfigAuthorizerCredentialArgsDict",
    "ConnectionGitlabConfigReadAuthorizerCredentialArgs",
    ...,
    "ConnectionGitlabEnterpriseConfigArgs",
    "ConnectionGitlabEnterpriseConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ConnectionHttpConfigArgs",
    "ConnectionHttpConfigArgsDict",
    "ConnectionHttpConfigBasicAuthenticationArgs",
    "ConnectionHttpConfigBasicAuthenticationArgsDict",
    "ConnectionHttpConfigBearerTokenAuthenticationArgs",
    ...,
    "ConnectionHttpConfigServiceDirectoryConfigArgs",
    "ConnectionHttpConfigServiceDirectoryConfigArgsDict",
    "ConnectionInstallationStateArgs",
    "ConnectionInstallationStateArgsDict",
    "InsightsConfigArtifactConfigArgs",
    "InsightsConfigArtifactConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "InsightsConfigErrorArgs",
    "InsightsConfigErrorArgsDict",
    "InsightsConfigErrorDetailArgs",
    "InsightsConfigErrorDetailArgsDict",
    "InsightsConfigRuntimeConfigArgs",
    "InsightsConfigRuntimeConfigArgsDict",
    "InsightsConfigRuntimeConfigAppHubWorkloadArgs",
    "InsightsConfigRuntimeConfigAppHubWorkloadArgsDict",
    "InsightsConfigRuntimeConfigGkeWorkloadArgs",
    "InsightsConfigRuntimeConfigGkeWorkloadArgsDict",
    "InsightsConfigTargetProjectsArgs",
    "InsightsConfigTargetProjectsArgsDict",
]

class AccountConnectorProviderOauthConfigArgsDict(TypedDict):
    scopes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    system_provider_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AccountConnectorProviderOauthConfigArgs:
    def __init__(
        __self__,
        *,
        scopes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        system_provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @scopes.setter
    def scopes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="systemProviderId")
    def system_provider_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @system_provider_id.setter
    def system_provider_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionBitbucketCloudConfigArgsDict(TypedDict):
    authorizer_credential: pulumi.Input[
        ConnectionBitbucketCloudConfigAuthorizerCredentialArgsDict
    ]
    read_authorizer_credential: pulumi.Input[
        ConnectionBitbucketCloudConfigReadAuthorizerCredentialArgsDict
    ]
    webhook_secret_secret_version: pulumi.Input[_builtins.str]
    workspace: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionBitbucketCloudConfigArgs:
    def __init__(
        __self__,
        *,
        authorizer_credential: pulumi.Input[
            ConnectionBitbucketCloudConfigAuthorizerCredentialArgs
        ],
        read_authorizer_credential: pulumi.Input[
            ConnectionBitbucketCloudConfigReadAuthorizerCredentialArgs
        ],
        webhook_secret_secret_version: pulumi.Input[_builtins.str],
        workspace: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizerCredential")
    def authorizer_credential(
        self,
    ) -> pulumi.Input[ConnectionBitbucketCloudConfigAuthorizerCredentialArgs]: ...
    @authorizer_credential.setter
    def authorizer_credential(
        self,
        value: pulumi.Input[ConnectionBitbucketCloudConfigAuthorizerCredentialArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="readAuthorizerCredential")
    def read_authorizer_credential(
        self,
    ) -> pulumi.Input[ConnectionBitbucketCloudConfigReadAuthorizerCredentialArgs]: ...
    @read_authorizer_credential.setter
    def read_authorizer_credential(
        self,
        value: pulumi.Input[ConnectionBitbucketCloudConfigReadAuthorizerCredentialArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="webhookSecretSecretVersion")
    def webhook_secret_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @webhook_secret_secret_version.setter
    def webhook_secret_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def workspace(self) -> pulumi.Input[_builtins.str]: ...
    @workspace.setter
    def workspace(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionBitbucketCloudConfigAuthorizerCredentialArgsDict(TypedDict):
    user_token_secret_version: pulumi.Input[_builtins.str]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionBitbucketCloudConfigAuthorizerCredentialArgs:
    def __init__(
        __self__,
        *,
        user_token_secret_version: pulumi.Input[_builtins.str],
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @user_token_secret_version.setter
    def user_token_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionBitbucketCloudConfigReadAuthorizerCredentialArgsDict(TypedDict):
    user_token_secret_version: pulumi.Input[_builtins.str]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionBitbucketCloudConfigReadAuthorizerCredentialArgs:
    def __init__(
        __self__,
        *,
        user_token_secret_version: pulumi.Input[_builtins.str],
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @user_token_secret_version.setter
    def user_token_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionBitbucketDataCenterConfigArgsDict(TypedDict):
    authorizer_credential: pulumi.Input[
        ConnectionBitbucketDataCenterConfigAuthorizerCredentialArgsDict
    ]
    host_uri: pulumi.Input[_builtins.str]
    read_authorizer_credential: pulumi.Input[
        ConnectionBitbucketDataCenterConfigReadAuthorizerCredentialArgsDict
    ]
    webhook_secret_secret_version: pulumi.Input[_builtins.str]
    server_version: NotRequired[pulumi.Input[_builtins.str]]
    service_directory_config: NotRequired[
        pulumi.Input[ConnectionBitbucketDataCenterConfigServiceDirectoryConfigArgsDict]
    ]
    ssl_ca_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionBitbucketDataCenterConfigArgs:
    def __init__(
        __self__,
        *,
        authorizer_credential: pulumi.Input[
            ConnectionBitbucketDataCenterConfigAuthorizerCredentialArgs
        ],
        host_uri: pulumi.Input[_builtins.str],
        read_authorizer_credential: pulumi.Input[
            ConnectionBitbucketDataCenterConfigReadAuthorizerCredentialArgs
        ],
        webhook_secret_secret_version: pulumi.Input[_builtins.str],
        server_version: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory_config: Optional[
            pulumi.Input[ConnectionBitbucketDataCenterConfigServiceDirectoryConfigArgs]
        ] = ...,
        ssl_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizerCredential")
    def authorizer_credential(
        self,
    ) -> pulumi.Input[ConnectionBitbucketDataCenterConfigAuthorizerCredentialArgs]: ...
    @authorizer_credential.setter
    def authorizer_credential(
        self,
        value: pulumi.Input[
            ConnectionBitbucketDataCenterConfigAuthorizerCredentialArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> pulumi.Input[_builtins.str]: ...
    @host_uri.setter
    def host_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="readAuthorizerCredential")
    def read_authorizer_credential(
        self,
    ) -> pulumi.Input[
        ConnectionBitbucketDataCenterConfigReadAuthorizerCredentialArgs
    ]: ...
    @read_authorizer_credential.setter
    def read_authorizer_credential(
        self,
        value: pulumi.Input[
            ConnectionBitbucketDataCenterConfigReadAuthorizerCredentialArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="webhookSecretSecretVersion")
    def webhook_secret_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @webhook_secret_secret_version.setter
    def webhook_secret_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_version.setter
    def server_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionBitbucketDataCenterConfigServiceDirectoryConfigArgs]
    ]: ...
    @service_directory_config.setter
    def service_directory_config(
        self,
        value: Optional[
            pulumi.Input[ConnectionBitbucketDataCenterConfigServiceDirectoryConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslCaCertificate")
    def ssl_ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_ca_certificate.setter
    def ssl_ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionBitbucketDataCenterConfigAuthorizerCredentialArgsDict(TypedDict):
    user_token_secret_version: pulumi.Input[_builtins.str]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionBitbucketDataCenterConfigAuthorizerCredentialArgs:
    def __init__(
        __self__,
        *,
        user_token_secret_version: pulumi.Input[_builtins.str],
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @user_token_secret_version.setter
    def user_token_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionBitbucketDataCenterConfigReadAuthorizerCredentialArgsDict(TypedDict):
    user_token_secret_version: pulumi.Input[_builtins.str]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionBitbucketDataCenterConfigReadAuthorizerCredentialArgs:
    def __init__(
        __self__,
        *,
        user_token_secret_version: pulumi.Input[_builtins.str],
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @user_token_secret_version.setter
    def user_token_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionBitbucketDataCenterConfigServiceDirectoryConfigArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionBitbucketDataCenterConfigServiceDirectoryConfigArgs:
    def __init__(__self__, *, service: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionCryptoKeyConfigArgsDict(TypedDict):
    key_reference: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionCryptoKeyConfigArgs:
    def __init__(__self__, *, key_reference: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyReference")
    def key_reference(self) -> pulumi.Input[_builtins.str]: ...
    @key_reference.setter
    def key_reference(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionGithubConfigArgsDict(TypedDict):
    github_app: pulumi.Input[_builtins.str]
    app_installation_id: NotRequired[pulumi.Input[_builtins.str]]
    authorizer_credential: NotRequired[
        pulumi.Input[ConnectionGithubConfigAuthorizerCredentialArgsDict]
    ]
    installation_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionGithubConfigArgs:
    def __init__(
        __self__,
        *,
        github_app: pulumi.Input[_builtins.str],
        app_installation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        authorizer_credential: Optional[
            pulumi.Input[ConnectionGithubConfigAuthorizerCredentialArgs]
        ] = ...,
        installation_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="githubApp")
    def github_app(self) -> pulumi.Input[_builtins.str]: ...
    @github_app.setter
    def github_app(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appInstallationId")
    def app_installation_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_installation_id.setter
    def app_installation_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authorizerCredential")
    def authorizer_credential(
        self,
    ) -> Optional[pulumi.Input[ConnectionGithubConfigAuthorizerCredentialArgs]]: ...
    @authorizer_credential.setter
    def authorizer_credential(
        self,
        value: Optional[pulumi.Input[ConnectionGithubConfigAuthorizerCredentialArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="installationUri")
    def installation_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @installation_uri.setter
    def installation_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionGithubConfigAuthorizerCredentialArgsDict(TypedDict):
    oauth_token_secret_version: pulumi.Input[_builtins.str]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionGithubConfigAuthorizerCredentialArgs:
    def __init__(
        __self__,
        *,
        oauth_token_secret_version: pulumi.Input[_builtins.str],
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oauthTokenSecretVersion")
    def oauth_token_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @oauth_token_secret_version.setter
    def oauth_token_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionGithubEnterpriseConfigArgsDict(TypedDict):
    host_uri: pulumi.Input[_builtins.str]
    app_id: NotRequired[pulumi.Input[_builtins.str]]
    app_installation_id: NotRequired[pulumi.Input[_builtins.str]]
    app_slug: NotRequired[pulumi.Input[_builtins.str]]
    installation_uri: NotRequired[pulumi.Input[_builtins.str]]
    private_key_secret_version: NotRequired[pulumi.Input[_builtins.str]]
    server_version: NotRequired[pulumi.Input[_builtins.str]]
    service_directory_config: NotRequired[
        pulumi.Input[ConnectionGithubEnterpriseConfigServiceDirectoryConfigArgsDict]
    ]
    ssl_ca_certificate: NotRequired[pulumi.Input[_builtins.str]]
    webhook_secret_secret_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionGithubEnterpriseConfigArgs:
    def __init__(
        __self__,
        *,
        host_uri: pulumi.Input[_builtins.str],
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        app_installation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        app_slug: Optional[pulumi.Input[_builtins.str]] = ...,
        installation_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
        server_version: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory_config: Optional[
            pulumi.Input[ConnectionGithubEnterpriseConfigServiceDirectoryConfigArgs]
        ] = ...,
        ssl_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        webhook_secret_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> pulumi.Input[_builtins.str]: ...
    @host_uri.setter
    def host_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appInstallationId")
    def app_installation_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_installation_id.setter
    def app_installation_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="appSlug")
    def app_slug(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_slug.setter
    def app_slug(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="installationUri")
    def installation_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @installation_uri.setter
    def installation_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateKeySecretVersion")
    def private_key_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_key_secret_version.setter
    def private_key_secret_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_version.setter
    def server_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionGithubEnterpriseConfigServiceDirectoryConfigArgs]
    ]: ...
    @service_directory_config.setter
    def service_directory_config(
        self,
        value: Optional[
            pulumi.Input[ConnectionGithubEnterpriseConfigServiceDirectoryConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslCaCertificate")
    def ssl_ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_ca_certificate.setter
    def ssl_ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webhookSecretSecretVersion")
    def webhook_secret_secret_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @webhook_secret_secret_version.setter
    def webhook_secret_secret_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ConnectionGithubEnterpriseConfigServiceDirectoryConfigArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionGithubEnterpriseConfigServiceDirectoryConfigArgs:
    def __init__(__self__, *, service: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionGitlabConfigArgsDict(TypedDict):
    authorizer_credential: pulumi.Input[
        ConnectionGitlabConfigAuthorizerCredentialArgsDict
    ]
    read_authorizer_credential: pulumi.Input[
        ConnectionGitlabConfigReadAuthorizerCredentialArgsDict
    ]
    webhook_secret_secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionGitlabConfigArgs:
    def __init__(
        __self__,
        *,
        authorizer_credential: pulumi.Input[
            ConnectionGitlabConfigAuthorizerCredentialArgs
        ],
        read_authorizer_credential: pulumi.Input[
            ConnectionGitlabConfigReadAuthorizerCredentialArgs
        ],
        webhook_secret_secret_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizerCredential")
    def authorizer_credential(
        self,
    ) -> pulumi.Input[ConnectionGitlabConfigAuthorizerCredentialArgs]: ...
    @authorizer_credential.setter
    def authorizer_credential(
        self, value: pulumi.Input[ConnectionGitlabConfigAuthorizerCredentialArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readAuthorizerCredential")
    def read_authorizer_credential(
        self,
    ) -> pulumi.Input[ConnectionGitlabConfigReadAuthorizerCredentialArgs]: ...
    @read_authorizer_credential.setter
    def read_authorizer_credential(
        self, value: pulumi.Input[ConnectionGitlabConfigReadAuthorizerCredentialArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webhookSecretSecretVersion")
    def webhook_secret_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @webhook_secret_secret_version.setter
    def webhook_secret_secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionGitlabConfigAuthorizerCredentialArgsDict(TypedDict):
    user_token_secret_version: pulumi.Input[_builtins.str]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionGitlabConfigAuthorizerCredentialArgs:
    def __init__(
        __self__,
        *,
        user_token_secret_version: pulumi.Input[_builtins.str],
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @user_token_secret_version.setter
    def user_token_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionGitlabConfigReadAuthorizerCredentialArgsDict(TypedDict):
    user_token_secret_version: pulumi.Input[_builtins.str]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionGitlabConfigReadAuthorizerCredentialArgs:
    def __init__(
        __self__,
        *,
        user_token_secret_version: pulumi.Input[_builtins.str],
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @user_token_secret_version.setter
    def user_token_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionGitlabEnterpriseConfigArgsDict(TypedDict):
    authorizer_credential: pulumi.Input[
        ConnectionGitlabEnterpriseConfigAuthorizerCredentialArgsDict
    ]
    host_uri: pulumi.Input[_builtins.str]
    read_authorizer_credential: pulumi.Input[
        ConnectionGitlabEnterpriseConfigReadAuthorizerCredentialArgsDict
    ]
    webhook_secret_secret_version: pulumi.Input[_builtins.str]
    server_version: NotRequired[pulumi.Input[_builtins.str]]
    service_directory_config: NotRequired[
        pulumi.Input[ConnectionGitlabEnterpriseConfigServiceDirectoryConfigArgsDict]
    ]
    ssl_ca_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionGitlabEnterpriseConfigArgs:
    def __init__(
        __self__,
        *,
        authorizer_credential: pulumi.Input[
            ConnectionGitlabEnterpriseConfigAuthorizerCredentialArgs
        ],
        host_uri: pulumi.Input[_builtins.str],
        read_authorizer_credential: pulumi.Input[
            ConnectionGitlabEnterpriseConfigReadAuthorizerCredentialArgs
        ],
        webhook_secret_secret_version: pulumi.Input[_builtins.str],
        server_version: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory_config: Optional[
            pulumi.Input[ConnectionGitlabEnterpriseConfigServiceDirectoryConfigArgs]
        ] = ...,
        ssl_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizerCredential")
    def authorizer_credential(
        self,
    ) -> pulumi.Input[ConnectionGitlabEnterpriseConfigAuthorizerCredentialArgs]: ...
    @authorizer_credential.setter
    def authorizer_credential(
        self,
        value: pulumi.Input[ConnectionGitlabEnterpriseConfigAuthorizerCredentialArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> pulumi.Input[_builtins.str]: ...
    @host_uri.setter
    def host_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="readAuthorizerCredential")
    def read_authorizer_credential(
        self,
    ) -> pulumi.Input[ConnectionGitlabEnterpriseConfigReadAuthorizerCredentialArgs]: ...
    @read_authorizer_credential.setter
    def read_authorizer_credential(
        self,
        value: pulumi.Input[
            ConnectionGitlabEnterpriseConfigReadAuthorizerCredentialArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="webhookSecretSecretVersion")
    def webhook_secret_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @webhook_secret_secret_version.setter
    def webhook_secret_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_version.setter
    def server_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionGitlabEnterpriseConfigServiceDirectoryConfigArgs]
    ]: ...
    @service_directory_config.setter
    def service_directory_config(
        self,
        value: Optional[
            pulumi.Input[ConnectionGitlabEnterpriseConfigServiceDirectoryConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslCaCertificate")
    def ssl_ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_ca_certificate.setter
    def ssl_ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionGitlabEnterpriseConfigAuthorizerCredentialArgsDict(TypedDict):
    user_token_secret_version: pulumi.Input[_builtins.str]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionGitlabEnterpriseConfigAuthorizerCredentialArgs:
    def __init__(
        __self__,
        *,
        user_token_secret_version: pulumi.Input[_builtins.str],
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @user_token_secret_version.setter
    def user_token_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionGitlabEnterpriseConfigReadAuthorizerCredentialArgsDict(TypedDict):
    user_token_secret_version: pulumi.Input[_builtins.str]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionGitlabEnterpriseConfigReadAuthorizerCredentialArgs:
    def __init__(
        __self__,
        *,
        user_token_secret_version: pulumi.Input[_builtins.str],
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userTokenSecretVersion")
    def user_token_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @user_token_secret_version.setter
    def user_token_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionGitlabEnterpriseConfigServiceDirectoryConfigArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionGitlabEnterpriseConfigServiceDirectoryConfigArgs:
    def __init__(__self__, *, service: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionHttpConfigArgsDict(TypedDict):
    host_uri: pulumi.Input[_builtins.str]
    basic_authentication: NotRequired[
        pulumi.Input[ConnectionHttpConfigBasicAuthenticationArgsDict]
    ]
    bearer_token_authentication: NotRequired[
        pulumi.Input[ConnectionHttpConfigBearerTokenAuthenticationArgsDict]
    ]
    service_directory_config: NotRequired[
        pulumi.Input[ConnectionHttpConfigServiceDirectoryConfigArgsDict]
    ]
    ssl_ca_certificate: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionHttpConfigArgs:
    def __init__(
        __self__,
        *,
        host_uri: pulumi.Input[_builtins.str],
        basic_authentication: Optional[
            pulumi.Input[ConnectionHttpConfigBasicAuthenticationArgs]
        ] = ...,
        bearer_token_authentication: Optional[
            pulumi.Input[ConnectionHttpConfigBearerTokenAuthenticationArgs]
        ] = ...,
        service_directory_config: Optional[
            pulumi.Input[ConnectionHttpConfigServiceDirectoryConfigArgs]
        ] = ...,
        ssl_ca_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> pulumi.Input[_builtins.str]: ...
    @host_uri.setter
    def host_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="basicAuthentication")
    def basic_authentication(
        self,
    ) -> Optional[pulumi.Input[ConnectionHttpConfigBasicAuthenticationArgs]]: ...
    @basic_authentication.setter
    def basic_authentication(
        self, value: Optional[pulumi.Input[ConnectionHttpConfigBasicAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bearerTokenAuthentication")
    def bearer_token_authentication(
        self,
    ) -> Optional[pulumi.Input[ConnectionHttpConfigBearerTokenAuthenticationArgs]]: ...
    @bearer_token_authentication.setter
    def bearer_token_authentication(
        self,
        value: Optional[
            pulumi.Input[ConnectionHttpConfigBearerTokenAuthenticationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionHttpConfigServiceDirectoryConfigArgs]]: ...
    @service_directory_config.setter
    def service_directory_config(
        self,
        value: Optional[pulumi.Input[ConnectionHttpConfigServiceDirectoryConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslCaCertificate")
    def ssl_ca_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_ca_certificate.setter
    def ssl_ca_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionHttpConfigBasicAuthenticationArgsDict(TypedDict):
    username: pulumi.Input[_builtins.str]
    password_secret_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionHttpConfigBasicAuthenticationArgs:
    def __init__(
        __self__,
        *,
        username: pulumi.Input[_builtins.str],
        password_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="passwordSecretVersion")
    def password_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_secret_version.setter
    def password_secret_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionHttpConfigBearerTokenAuthenticationArgsDict(TypedDict):
    token_secret_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionHttpConfigBearerTokenAuthenticationArgs:
    def __init__(
        __self__, *, token_secret_version: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tokenSecretVersion")
    def token_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_secret_version.setter
    def token_secret_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionHttpConfigServiceDirectoryConfigArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionHttpConfigServiceDirectoryConfigArgs:
    def __init__(__self__, *, service: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionInstallationStateArgsDict(TypedDict):
    action_uri: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    stage: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionInstallationStateArgs:
    def __init__(
        __self__,
        *,
        action_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        stage: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionUri")
    def action_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action_uri.setter
    def action_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stage.setter
    def stage(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightsConfigArtifactConfigArgsDict(TypedDict):
    google_artifact_analysis: NotRequired[
        pulumi.Input[InsightsConfigArtifactConfigGoogleArtifactAnalysisArgsDict]
    ]
    google_artifact_registry: NotRequired[
        pulumi.Input[InsightsConfigArtifactConfigGoogleArtifactRegistryArgsDict]
    ]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightsConfigArtifactConfigArgs:
    def __init__(
        __self__,
        *,
        google_artifact_analysis: Optional[
            pulumi.Input[InsightsConfigArtifactConfigGoogleArtifactAnalysisArgs]
        ] = ...,
        google_artifact_registry: Optional[
            pulumi.Input[InsightsConfigArtifactConfigGoogleArtifactRegistryArgs]
        ] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="googleArtifactAnalysis")
    def google_artifact_analysis(
        self,
    ) -> Optional[
        pulumi.Input[InsightsConfigArtifactConfigGoogleArtifactAnalysisArgs]
    ]: ...
    @google_artifact_analysis.setter
    def google_artifact_analysis(
        self,
        value: Optional[
            pulumi.Input[InsightsConfigArtifactConfigGoogleArtifactAnalysisArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="googleArtifactRegistry")
    def google_artifact_registry(
        self,
    ) -> Optional[
        pulumi.Input[InsightsConfigArtifactConfigGoogleArtifactRegistryArgs]
    ]: ...
    @google_artifact_registry.setter
    def google_artifact_registry(
        self,
        value: Optional[
            pulumi.Input[InsightsConfigArtifactConfigGoogleArtifactRegistryArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightsConfigArtifactConfigGoogleArtifactAnalysisArgsDict(TypedDict):
    project_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightsConfigArtifactConfigGoogleArtifactAnalysisArgs:
    def __init__(__self__, *, project_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...

class InsightsConfigArtifactConfigGoogleArtifactRegistryArgsDict(TypedDict):
    artifact_registry_package: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightsConfigArtifactConfigGoogleArtifactRegistryArgs:
    def __init__(
        __self__,
        *,
        artifact_registry_package: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactRegistryPackage")
    def artifact_registry_package(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_registry_package.setter
    def artifact_registry_package(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...

class InsightsConfigErrorArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightsConfigErrorDetailArgsDict]]]
    ]
    message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightsConfigErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightsConfigErrorDetailArgs]]]
        ] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightsConfigErrorDetailArgs]]]
    ]: ...
    @details.setter
    def details(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightsConfigErrorDetailArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightsConfigErrorDetailArgsDict(TypedDict):
    detail_message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightsConfigErrorDetailArgs:
    def __init__(
        __self__, *, detail_message: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="detailMessage")
    def detail_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @detail_message.setter
    def detail_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightsConfigRuntimeConfigArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    app_hub_workload: NotRequired[
        pulumi.Input[InsightsConfigRuntimeConfigAppHubWorkloadArgsDict]
    ]
    gke_workload: NotRequired[
        pulumi.Input[InsightsConfigRuntimeConfigGkeWorkloadArgsDict]
    ]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightsConfigRuntimeConfigArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        app_hub_workload: Optional[
            pulumi.Input[InsightsConfigRuntimeConfigAppHubWorkloadArgs]
        ] = ...,
        gke_workload: Optional[
            pulumi.Input[InsightsConfigRuntimeConfigGkeWorkloadArgs]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appHubWorkload")
    def app_hub_workload(
        self,
    ) -> Optional[pulumi.Input[InsightsConfigRuntimeConfigAppHubWorkloadArgs]]: ...
    @app_hub_workload.setter
    def app_hub_workload(
        self,
        value: Optional[pulumi.Input[InsightsConfigRuntimeConfigAppHubWorkloadArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="gkeWorkload")
    def gke_workload(
        self,
    ) -> Optional[pulumi.Input[InsightsConfigRuntimeConfigGkeWorkloadArgs]]: ...
    @gke_workload.setter
    def gke_workload(
        self, value: Optional[pulumi.Input[InsightsConfigRuntimeConfigGkeWorkloadArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightsConfigRuntimeConfigAppHubWorkloadArgsDict(TypedDict):
    criticality: NotRequired[pulumi.Input[_builtins.str]]
    environment: NotRequired[pulumi.Input[_builtins.str]]
    workload: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightsConfigRuntimeConfigAppHubWorkloadArgs:
    def __init__(
        __self__,
        *,
        criticality: Optional[pulumi.Input[_builtins.str]] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        workload: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def criticality(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @criticality.setter
    def criticality(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def workload(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workload.setter
    def workload(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightsConfigRuntimeConfigGkeWorkloadArgsDict(TypedDict):
    cluster: pulumi.Input[_builtins.str]
    deployment: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightsConfigRuntimeConfigGkeWorkloadArgs:
    def __init__(
        __self__,
        *,
        cluster: pulumi.Input[_builtins.str],
        deployment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[_builtins.str]: ...
    @cluster.setter
    def cluster(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def deployment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment.setter
    def deployment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightsConfigTargetProjectsArgsDict(TypedDict):
    project_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class InsightsConfigTargetProjectsArgs:
    def __init__(
        __self__,
        *,
        project_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectIds")
    def project_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @project_ids.setter
    def project_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
