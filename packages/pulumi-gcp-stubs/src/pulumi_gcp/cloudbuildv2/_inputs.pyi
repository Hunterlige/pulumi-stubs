import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
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
    "ConnectionGitlabConfigServiceDirectoryConfigArgs",
    ...,
    "ConnectionIAMBindingConditionArgs",
    "ConnectionIAMBindingConditionArgsDict",
    "ConnectionIAMMemberConditionArgs",
    "ConnectionIAMMemberConditionArgsDict",
    "ConnectionInstallationStateArgs",
    "ConnectionInstallationStateArgsDict",
]

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
    ssl_ca: NotRequired[pulumi.Input[_builtins.str]]

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
        ssl_ca: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="sslCa")
    def ssl_ca(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_ca.setter
    def ssl_ca(self, value: Optional[pulumi.Input[_builtins.str]]): ...

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

class ConnectionGithubConfigArgsDict(TypedDict):
    app_installation_id: NotRequired[pulumi.Input[_builtins.int]]
    authorizer_credential: NotRequired[
        pulumi.Input[ConnectionGithubConfigAuthorizerCredentialArgsDict]
    ]

@pulumi.input_type
class ConnectionGithubConfigArgs:
    def __init__(
        __self__,
        *,
        app_installation_id: Optional[pulumi.Input[_builtins.int]] = ...,
        authorizer_credential: Optional[
            pulumi.Input[ConnectionGithubConfigAuthorizerCredentialArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appInstallationId")
    def app_installation_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @app_installation_id.setter
    def app_installation_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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

class ConnectionGithubConfigAuthorizerCredentialArgsDict(TypedDict):
    oauth_token_secret_version: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionGithubConfigAuthorizerCredentialArgs:
    def __init__(
        __self__,
        *,
        oauth_token_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oauthTokenSecretVersion")
    def oauth_token_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oauth_token_secret_version.setter
    def oauth_token_secret_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionGithubEnterpriseConfigArgsDict(TypedDict):
    host_uri: pulumi.Input[_builtins.str]
    app_id: NotRequired[pulumi.Input[_builtins.int]]
    app_installation_id: NotRequired[pulumi.Input[_builtins.int]]
    app_slug: NotRequired[pulumi.Input[_builtins.str]]
    private_key_secret_version: NotRequired[pulumi.Input[_builtins.str]]
    service_directory_config: NotRequired[
        pulumi.Input[ConnectionGithubEnterpriseConfigServiceDirectoryConfigArgsDict]
    ]
    ssl_ca: NotRequired[pulumi.Input[_builtins.str]]
    webhook_secret_secret_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionGithubEnterpriseConfigArgs:
    def __init__(
        __self__,
        *,
        host_uri: pulumi.Input[_builtins.str],
        app_id: Optional[pulumi.Input[_builtins.int]] = ...,
        app_installation_id: Optional[pulumi.Input[_builtins.int]] = ...,
        app_slug: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory_config: Optional[
            pulumi.Input[ConnectionGithubEnterpriseConfigServiceDirectoryConfigArgs]
        ] = ...,
        ssl_ca: Optional[pulumi.Input[_builtins.str]] = ...,
        webhook_secret_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> pulumi.Input[_builtins.str]: ...
    @host_uri.setter
    def host_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="appInstallationId")
    def app_installation_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @app_installation_id.setter
    def app_installation_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="appSlug")
    def app_slug(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_slug.setter
    def app_slug(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateKeySecretVersion")
    def private_key_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_key_secret_version.setter
    def private_key_secret_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
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
    @pulumi.getter(name="sslCa")
    def ssl_ca(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_ca.setter
    def ssl_ca(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    host_uri: NotRequired[pulumi.Input[_builtins.str]]
    server_version: NotRequired[pulumi.Input[_builtins.str]]
    service_directory_config: NotRequired[
        pulumi.Input[ConnectionGitlabConfigServiceDirectoryConfigArgsDict]
    ]
    ssl_ca: NotRequired[pulumi.Input[_builtins.str]]

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
        host_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        server_version: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory_config: Optional[
            pulumi.Input[ConnectionGitlabConfigServiceDirectoryConfigArgs]
        ] = ...,
        ssl_ca: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_uri.setter
    def host_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverVersion")
    def server_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_version.setter
    def server_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionGitlabConfigServiceDirectoryConfigArgs]]: ...
    @service_directory_config.setter
    def service_directory_config(
        self,
        value: Optional[pulumi.Input[ConnectionGitlabConfigServiceDirectoryConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslCa")
    def ssl_ca(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_ca.setter
    def ssl_ca(self, value: Optional[pulumi.Input[_builtins.str]]): ...

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

class ConnectionGitlabConfigServiceDirectoryConfigArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionGitlabConfigServiceDirectoryConfigArgs:
    def __init__(__self__, *, service: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionIAMBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionIAMBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionIAMMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionIAMMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

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
