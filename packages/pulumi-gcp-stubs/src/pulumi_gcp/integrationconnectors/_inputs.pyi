import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectionAuthConfigArgs",
    "ConnectionAuthConfigArgsDict",
    "ConnectionAuthConfigAdditionalVariableArgs",
    "ConnectionAuthConfigAdditionalVariableArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ConnectionAuthConfigOauth2AuthCodeFlowArgs",
    "ConnectionAuthConfigOauth2AuthCodeFlowArgsDict",
    ...,
    ...,
    "ConnectionAuthConfigOauth2ClientCredentialsArgs",
    ...,
    ...,
    ...,
    "ConnectionAuthConfigOauth2JwtBearerArgs",
    "ConnectionAuthConfigOauth2JwtBearerArgsDict",
    "ConnectionAuthConfigOauth2JwtBearerClientKeyArgs",
    ...,
    "ConnectionAuthConfigOauth2JwtBearerJwtClaimsArgs",
    ...,
    "ConnectionAuthConfigSshPublicKeyArgs",
    "ConnectionAuthConfigSshPublicKeyArgsDict",
    "ConnectionAuthConfigSshPublicKeySshClientCertArgs",
    ...,
    ...,
    ...,
    "ConnectionAuthConfigUserPasswordArgs",
    "ConnectionAuthConfigUserPasswordArgsDict",
    "ConnectionAuthConfigUserPasswordPasswordArgs",
    "ConnectionAuthConfigUserPasswordPasswordArgsDict",
    "ConnectionConfigVariableArgs",
    "ConnectionConfigVariableArgsDict",
    "ConnectionConfigVariableEncryptionKeyValueArgs",
    "ConnectionConfigVariableEncryptionKeyValueArgsDict",
    "ConnectionConfigVariableSecretValueArgs",
    "ConnectionConfigVariableSecretValueArgsDict",
    "ConnectionConnectorVersionInfraConfigArgs",
    "ConnectionConnectorVersionInfraConfigArgsDict",
    "ConnectionDestinationConfigArgs",
    "ConnectionDestinationConfigArgsDict",
    "ConnectionDestinationConfigDestinationArgs",
    "ConnectionDestinationConfigDestinationArgsDict",
    "ConnectionEventingConfigArgs",
    "ConnectionEventingConfigArgsDict",
    "ConnectionEventingConfigAdditionalVariableArgs",
    "ConnectionEventingConfigAdditionalVariableArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ConnectionEventingConfigAuthConfigArgs",
    "ConnectionEventingConfigAuthConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ConnectionEventingConfigAuthConfigUserPasswordArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ConnectionEventingRuntimeDataArgs",
    "ConnectionEventingRuntimeDataArgsDict",
    "ConnectionEventingRuntimeDataStatusArgs",
    "ConnectionEventingRuntimeDataStatusArgsDict",
    "ConnectionLockConfigArgs",
    "ConnectionLockConfigArgsDict",
    "ConnectionLogConfigArgs",
    "ConnectionLogConfigArgsDict",
    "ConnectionNodeConfigArgs",
    "ConnectionNodeConfigArgsDict",
    "ConnectionSslConfigArgs",
    "ConnectionSslConfigArgsDict",
    "ConnectionSslConfigAdditionalVariableArgs",
    "ConnectionSslConfigAdditionalVariableArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ConnectionSslConfigClientCertificateArgs",
    "ConnectionSslConfigClientCertificateArgsDict",
    "ConnectionSslConfigClientPrivateKeyArgs",
    "ConnectionSslConfigClientPrivateKeyArgsDict",
    "ConnectionSslConfigClientPrivateKeyPassArgs",
    "ConnectionSslConfigClientPrivateKeyPassArgsDict",
    "ConnectionSslConfigPrivateServerCertificateArgs",
    ...,
    "ConnectionStatusArgs",
    "ConnectionStatusArgsDict",
]

class ConnectionAuthConfigArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    additional_variables: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ConnectionAuthConfigAdditionalVariableArgsDict]]
        ]
    ]
    auth_key: NotRequired[pulumi.Input[_builtins.str]]
    oauth2_auth_code_flow: NotRequired[
        pulumi.Input[ConnectionAuthConfigOauth2AuthCodeFlowArgsDict]
    ]
    oauth2_client_credentials: NotRequired[
        pulumi.Input[ConnectionAuthConfigOauth2ClientCredentialsArgsDict]
    ]
    oauth2_jwt_bearer: NotRequired[
        pulumi.Input[ConnectionAuthConfigOauth2JwtBearerArgsDict]
    ]
    ssh_public_key: NotRequired[pulumi.Input[ConnectionAuthConfigSshPublicKeyArgsDict]]
    user_password: NotRequired[pulumi.Input[ConnectionAuthConfigUserPasswordArgsDict]]

@pulumi.input_type
class ConnectionAuthConfigArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        additional_variables: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectionAuthConfigAdditionalVariableArgs]]
            ]
        ] = ...,
        auth_key: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth2_auth_code_flow: Optional[
            pulumi.Input[ConnectionAuthConfigOauth2AuthCodeFlowArgs]
        ] = ...,
        oauth2_client_credentials: Optional[
            pulumi.Input[ConnectionAuthConfigOauth2ClientCredentialsArgs]
        ] = ...,
        oauth2_jwt_bearer: Optional[
            pulumi.Input[ConnectionAuthConfigOauth2JwtBearerArgs]
        ] = ...,
        ssh_public_key: Optional[
            pulumi.Input[ConnectionAuthConfigSshPublicKeyArgs]
        ] = ...,
        user_password: Optional[
            pulumi.Input[ConnectionAuthConfigUserPasswordArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalVariables")
    def additional_variables(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConnectionAuthConfigAdditionalVariableArgs]]]
    ]: ...
    @additional_variables.setter
    def additional_variables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectionAuthConfigAdditionalVariableArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="authKey")
    def auth_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_key.setter
    def auth_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauth2AuthCodeFlow")
    def oauth2_auth_code_flow(
        self,
    ) -> Optional[pulumi.Input[ConnectionAuthConfigOauth2AuthCodeFlowArgs]]: ...
    @oauth2_auth_code_flow.setter
    def oauth2_auth_code_flow(
        self, value: Optional[pulumi.Input[ConnectionAuthConfigOauth2AuthCodeFlowArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oauth2ClientCredentials")
    def oauth2_client_credentials(
        self,
    ) -> Optional[pulumi.Input[ConnectionAuthConfigOauth2ClientCredentialsArgs]]: ...
    @oauth2_client_credentials.setter
    def oauth2_client_credentials(
        self,
        value: Optional[pulumi.Input[ConnectionAuthConfigOauth2ClientCredentialsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="oauth2JwtBearer")
    def oauth2_jwt_bearer(
        self,
    ) -> Optional[pulumi.Input[ConnectionAuthConfigOauth2JwtBearerArgs]]: ...
    @oauth2_jwt_bearer.setter
    def oauth2_jwt_bearer(
        self, value: Optional[pulumi.Input[ConnectionAuthConfigOauth2JwtBearerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(
        self,
    ) -> Optional[pulumi.Input[ConnectionAuthConfigSshPublicKeyArgs]]: ...
    @ssh_public_key.setter
    def ssh_public_key(
        self, value: Optional[pulumi.Input[ConnectionAuthConfigSshPublicKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userPassword")
    def user_password(
        self,
    ) -> Optional[pulumi.Input[ConnectionAuthConfigUserPasswordArgs]]: ...
    @user_password.setter
    def user_password(
        self, value: Optional[pulumi.Input[ConnectionAuthConfigUserPasswordArgs]]
    ): ...

class ConnectionAuthConfigAdditionalVariableArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_key_value: NotRequired[
        pulumi.Input[ConnectionAuthConfigAdditionalVariableEncryptionKeyValueArgsDict]
    ]
    integer_value: NotRequired[pulumi.Input[_builtins.int]]
    secret_value: NotRequired[
        pulumi.Input[ConnectionAuthConfigAdditionalVariableSecretValueArgsDict]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionAuthConfigAdditionalVariableArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_key_value: Optional[
            pulumi.Input[ConnectionAuthConfigAdditionalVariableEncryptionKeyValueArgs]
        ] = ...,
        integer_value: Optional[pulumi.Input[_builtins.int]] = ...,
        secret_value: Optional[
            pulumi.Input[ConnectionAuthConfigAdditionalVariableSecretValueArgs]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyValue")
    def encryption_key_value(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionAuthConfigAdditionalVariableEncryptionKeyValueArgs]
    ]: ...
    @encryption_key_value.setter
    def encryption_key_value(
        self,
        value: Optional[
            pulumi.Input[ConnectionAuthConfigAdditionalVariableEncryptionKeyValueArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secretValue")
    def secret_value(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionAuthConfigAdditionalVariableSecretValueArgs]
    ]: ...
    @secret_value.setter
    def secret_value(
        self,
        value: Optional[
            pulumi.Input[ConnectionAuthConfigAdditionalVariableSecretValueArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionAuthConfigAdditionalVariableEncryptionKeyValueArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionAuthConfigAdditionalVariableEncryptionKeyValueArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionAuthConfigAdditionalVariableSecretValueArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionAuthConfigAdditionalVariableSecretValueArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionAuthConfigOauth2AuthCodeFlowArgsDict(TypedDict):
    auth_uri: NotRequired[pulumi.Input[_builtins.str]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[
        pulumi.Input[ConnectionAuthConfigOauth2AuthCodeFlowClientSecretArgsDict]
    ]
    enable_pkce: NotRequired[pulumi.Input[_builtins.bool]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ConnectionAuthConfigOauth2AuthCodeFlowArgs:
    def __init__(
        __self__,
        *,
        auth_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[
            pulumi.Input[ConnectionAuthConfigOauth2AuthCodeFlowClientSecretArgs]
        ] = ...,
        enable_pkce: Optional[pulumi.Input[_builtins.bool]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authUri")
    def auth_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_uri.setter
    def auth_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionAuthConfigOauth2AuthCodeFlowClientSecretArgs]
    ]: ...
    @client_secret.setter
    def client_secret(
        self,
        value: Optional[
            pulumi.Input[ConnectionAuthConfigOauth2AuthCodeFlowClientSecretArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enablePkce")
    def enable_pkce(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_pkce.setter
    def enable_pkce(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ConnectionAuthConfigOauth2AuthCodeFlowClientSecretArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionAuthConfigOauth2AuthCodeFlowClientSecretArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionAuthConfigOauth2ClientCredentialsArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret: NotRequired[
        pulumi.Input[ConnectionAuthConfigOauth2ClientCredentialsClientSecretArgsDict]
    ]

@pulumi.input_type
class ConnectionAuthConfigOauth2ClientCredentialsArgs:
    def __init__(
        __self__,
        *,
        client_id: pulumi.Input[_builtins.str],
        client_secret: Optional[
            pulumi.Input[ConnectionAuthConfigOauth2ClientCredentialsClientSecretArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionAuthConfigOauth2ClientCredentialsClientSecretArgs]
    ]: ...
    @client_secret.setter
    def client_secret(
        self,
        value: Optional[
            pulumi.Input[ConnectionAuthConfigOauth2ClientCredentialsClientSecretArgs]
        ],
    ): ...

class ConnectionAuthConfigOauth2ClientCredentialsClientSecretArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionAuthConfigOauth2ClientCredentialsClientSecretArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionAuthConfigOauth2JwtBearerArgsDict(TypedDict):
    client_key: NotRequired[
        pulumi.Input[ConnectionAuthConfigOauth2JwtBearerClientKeyArgsDict]
    ]
    jwt_claims: NotRequired[
        pulumi.Input[ConnectionAuthConfigOauth2JwtBearerJwtClaimsArgsDict]
    ]

@pulumi.input_type
class ConnectionAuthConfigOauth2JwtBearerArgs:
    def __init__(
        __self__,
        *,
        client_key: Optional[
            pulumi.Input[ConnectionAuthConfigOauth2JwtBearerClientKeyArgs]
        ] = ...,
        jwt_claims: Optional[
            pulumi.Input[ConnectionAuthConfigOauth2JwtBearerJwtClaimsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(
        self,
    ) -> Optional[pulumi.Input[ConnectionAuthConfigOauth2JwtBearerClientKeyArgs]]: ...
    @client_key.setter
    def client_key(
        self,
        value: Optional[pulumi.Input[ConnectionAuthConfigOauth2JwtBearerClientKeyArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="jwtClaims")
    def jwt_claims(
        self,
    ) -> Optional[pulumi.Input[ConnectionAuthConfigOauth2JwtBearerJwtClaimsArgs]]: ...
    @jwt_claims.setter
    def jwt_claims(
        self,
        value: Optional[pulumi.Input[ConnectionAuthConfigOauth2JwtBearerJwtClaimsArgs]],
    ): ...

class ConnectionAuthConfigOauth2JwtBearerClientKeyArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionAuthConfigOauth2JwtBearerClientKeyArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionAuthConfigOauth2JwtBearerJwtClaimsArgsDict(TypedDict):
    audience: NotRequired[pulumi.Input[_builtins.str]]
    issuer: NotRequired[pulumi.Input[_builtins.str]]
    subject: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionAuthConfigOauth2JwtBearerJwtClaimsArgs:
    def __init__(
        __self__,
        *,
        audience: Optional[pulumi.Input[_builtins.str]] = ...,
        issuer: Optional[pulumi.Input[_builtins.str]] = ...,
        subject: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subject.setter
    def subject(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionAuthConfigSshPublicKeyArgsDict(TypedDict):
    username: pulumi.Input[_builtins.str]
    cert_type: NotRequired[pulumi.Input[_builtins.str]]
    ssh_client_cert: NotRequired[
        pulumi.Input[ConnectionAuthConfigSshPublicKeySshClientCertArgsDict]
    ]
    ssh_client_cert_pass: NotRequired[
        pulumi.Input[ConnectionAuthConfigSshPublicKeySshClientCertPassArgsDict]
    ]

@pulumi.input_type
class ConnectionAuthConfigSshPublicKeyArgs:
    def __init__(
        __self__,
        *,
        username: pulumi.Input[_builtins.str],
        cert_type: Optional[pulumi.Input[_builtins.str]] = ...,
        ssh_client_cert: Optional[
            pulumi.Input[ConnectionAuthConfigSshPublicKeySshClientCertArgs]
        ] = ...,
        ssh_client_cert_pass: Optional[
            pulumi.Input[ConnectionAuthConfigSshPublicKeySshClientCertPassArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certType")
    def cert_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cert_type.setter
    def cert_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sshClientCert")
    def ssh_client_cert(
        self,
    ) -> Optional[pulumi.Input[ConnectionAuthConfigSshPublicKeySshClientCertArgs]]: ...
    @ssh_client_cert.setter
    def ssh_client_cert(
        self,
        value: Optional[
            pulumi.Input[ConnectionAuthConfigSshPublicKeySshClientCertArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sshClientCertPass")
    def ssh_client_cert_pass(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionAuthConfigSshPublicKeySshClientCertPassArgs]
    ]: ...
    @ssh_client_cert_pass.setter
    def ssh_client_cert_pass(
        self,
        value: Optional[
            pulumi.Input[ConnectionAuthConfigSshPublicKeySshClientCertPassArgs]
        ],
    ): ...

class ConnectionAuthConfigSshPublicKeySshClientCertArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionAuthConfigSshPublicKeySshClientCertArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionAuthConfigSshPublicKeySshClientCertPassArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionAuthConfigSshPublicKeySshClientCertPassArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionAuthConfigUserPasswordArgsDict(TypedDict):
    username: pulumi.Input[_builtins.str]
    password: NotRequired[
        pulumi.Input[ConnectionAuthConfigUserPasswordPasswordArgsDict]
    ]

@pulumi.input_type
class ConnectionAuthConfigUserPasswordArgs:
    def __init__(
        __self__,
        *,
        username: pulumi.Input[_builtins.str],
        password: Optional[
            pulumi.Input[ConnectionAuthConfigUserPasswordPasswordArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def password(
        self,
    ) -> Optional[pulumi.Input[ConnectionAuthConfigUserPasswordPasswordArgs]]: ...
    @password.setter
    def password(
        self,
        value: Optional[pulumi.Input[ConnectionAuthConfigUserPasswordPasswordArgs]],
    ): ...

class ConnectionAuthConfigUserPasswordPasswordArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionAuthConfigUserPasswordPasswordArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionConfigVariableArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_key_value: NotRequired[
        pulumi.Input[ConnectionConfigVariableEncryptionKeyValueArgsDict]
    ]
    integer_value: NotRequired[pulumi.Input[_builtins.int]]
    secret_value: NotRequired[pulumi.Input[ConnectionConfigVariableSecretValueArgsDict]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionConfigVariableArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_key_value: Optional[
            pulumi.Input[ConnectionConfigVariableEncryptionKeyValueArgs]
        ] = ...,
        integer_value: Optional[pulumi.Input[_builtins.int]] = ...,
        secret_value: Optional[
            pulumi.Input[ConnectionConfigVariableSecretValueArgs]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyValue")
    def encryption_key_value(
        self,
    ) -> Optional[pulumi.Input[ConnectionConfigVariableEncryptionKeyValueArgs]]: ...
    @encryption_key_value.setter
    def encryption_key_value(
        self,
        value: Optional[pulumi.Input[ConnectionConfigVariableEncryptionKeyValueArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secretValue")
    def secret_value(
        self,
    ) -> Optional[pulumi.Input[ConnectionConfigVariableSecretValueArgs]]: ...
    @secret_value.setter
    def secret_value(
        self, value: Optional[pulumi.Input[ConnectionConfigVariableSecretValueArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionConfigVariableEncryptionKeyValueArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionConfigVariableEncryptionKeyValueArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionConfigVariableSecretValueArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionConfigVariableSecretValueArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionConnectorVersionInfraConfigArgsDict(TypedDict):
    ratelimit_threshold: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionConnectorVersionInfraConfigArgs:
    def __init__(
        __self__, *, ratelimit_threshold: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ratelimitThreshold")
    def ratelimit_threshold(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ratelimit_threshold.setter
    def ratelimit_threshold(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionDestinationConfigArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    destinations: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ConnectionDestinationConfigDestinationArgsDict]]
        ]
    ]

@pulumi.input_type
class ConnectionDestinationConfigArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        destinations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectionDestinationConfigDestinationArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConnectionDestinationConfigDestinationArgs]]]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectionDestinationConfigDestinationArgs]]
            ]
        ],
    ): ...

class ConnectionDestinationConfigDestinationArgsDict(TypedDict):
    host: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    service_attachment: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionDestinationConfigDestinationArgs:
    def __init__(
        __self__,
        *,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionEventingConfigArgsDict(TypedDict):
    registration_destination_config: pulumi.Input[
        ConnectionEventingConfigRegistrationDestinationConfigArgsDict
    ]
    additional_variables: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ConnectionEventingConfigAdditionalVariableArgsDict]]
        ]
    ]
    auth_config: NotRequired[pulumi.Input[ConnectionEventingConfigAuthConfigArgsDict]]
    enrichment_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ConnectionEventingConfigArgs:
    def __init__(
        __self__,
        *,
        registration_destination_config: pulumi.Input[
            ConnectionEventingConfigRegistrationDestinationConfigArgs
        ],
        additional_variables: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectionEventingConfigAdditionalVariableArgs]]
            ]
        ] = ...,
        auth_config: Optional[
            pulumi.Input[ConnectionEventingConfigAuthConfigArgs]
        ] = ...,
        enrichment_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="registrationDestinationConfig")
    def registration_destination_config(
        self,
    ) -> pulumi.Input[ConnectionEventingConfigRegistrationDestinationConfigArgs]: ...
    @registration_destination_config.setter
    def registration_destination_config(
        self,
        value: pulumi.Input[ConnectionEventingConfigRegistrationDestinationConfigArgs],
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalVariables")
    def additional_variables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ConnectionEventingConfigAdditionalVariableArgs]]
        ]
    ]: ...
    @additional_variables.setter
    def additional_variables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectionEventingConfigAdditionalVariableArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="authConfig")
    def auth_config(
        self,
    ) -> Optional[pulumi.Input[ConnectionEventingConfigAuthConfigArgs]]: ...
    @auth_config.setter
    def auth_config(
        self, value: Optional[pulumi.Input[ConnectionEventingConfigAuthConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enrichmentEnabled")
    def enrichment_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enrichment_enabled.setter
    def enrichment_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ConnectionEventingConfigAdditionalVariableArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_key_value: NotRequired[
        pulumi.Input[
            ConnectionEventingConfigAdditionalVariableEncryptionKeyValueArgsDict
        ]
    ]
    integer_value: NotRequired[pulumi.Input[_builtins.int]]
    secret_value: NotRequired[
        pulumi.Input[ConnectionEventingConfigAdditionalVariableSecretValueArgsDict]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionEventingConfigAdditionalVariableArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_key_value: Optional[
            pulumi.Input[
                ConnectionEventingConfigAdditionalVariableEncryptionKeyValueArgs
            ]
        ] = ...,
        integer_value: Optional[pulumi.Input[_builtins.int]] = ...,
        secret_value: Optional[
            pulumi.Input[ConnectionEventingConfigAdditionalVariableSecretValueArgs]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyValue")
    def encryption_key_value(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionEventingConfigAdditionalVariableEncryptionKeyValueArgs]
    ]: ...
    @encryption_key_value.setter
    def encryption_key_value(
        self,
        value: Optional[
            pulumi.Input[
                ConnectionEventingConfigAdditionalVariableEncryptionKeyValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secretValue")
    def secret_value(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionEventingConfigAdditionalVariableSecretValueArgs]
    ]: ...
    @secret_value.setter
    def secret_value(
        self,
        value: Optional[
            pulumi.Input[ConnectionEventingConfigAdditionalVariableSecretValueArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionEventingConfigAdditionalVariableEncryptionKeyValueArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionEventingConfigAdditionalVariableEncryptionKeyValueArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionEventingConfigAdditionalVariableSecretValueArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionEventingConfigAdditionalVariableSecretValueArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionEventingConfigAuthConfigArgsDict(TypedDict):
    auth_type: pulumi.Input[_builtins.str]
    user_password: pulumi.Input[ConnectionEventingConfigAuthConfigUserPasswordArgsDict]
    additional_variables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ConnectionEventingConfigAuthConfigAdditionalVariableArgsDict
                ]
            ]
        ]
    ]
    auth_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionEventingConfigAuthConfigArgs:
    def __init__(
        __self__,
        *,
        auth_type: pulumi.Input[_builtins.str],
        user_password: pulumi.Input[ConnectionEventingConfigAuthConfigUserPasswordArgs],
        additional_variables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ConnectionEventingConfigAuthConfigAdditionalVariableArgs
                    ]
                ]
            ]
        ] = ...,
        auth_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Input[_builtins.str]: ...
    @auth_type.setter
    def auth_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userPassword")
    def user_password(
        self,
    ) -> pulumi.Input[ConnectionEventingConfigAuthConfigUserPasswordArgs]: ...
    @user_password.setter
    def user_password(
        self, value: pulumi.Input[ConnectionEventingConfigAuthConfigUserPasswordArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalVariables")
    def additional_variables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ConnectionEventingConfigAuthConfigAdditionalVariableArgs]
            ]
        ]
    ]: ...
    @additional_variables.setter
    def additional_variables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ConnectionEventingConfigAuthConfigAdditionalVariableArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="authKey")
    def auth_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_key.setter
    def auth_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionEventingConfigAuthConfigAdditionalVariableArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_key_value: NotRequired[
        pulumi.Input[
            ConnectionEventingConfigAuthConfigAdditionalVariableEncryptionKeyValueArgsDict
        ]
    ]
    integer_value: NotRequired[pulumi.Input[_builtins.int]]
    secret_value: NotRequired[
        pulumi.Input[
            ConnectionEventingConfigAuthConfigAdditionalVariableSecretValueArgsDict
        ]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionEventingConfigAuthConfigAdditionalVariableArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_key_value: Optional[
            pulumi.Input[
                ConnectionEventingConfigAuthConfigAdditionalVariableEncryptionKeyValueArgs
            ]
        ] = ...,
        integer_value: Optional[pulumi.Input[_builtins.int]] = ...,
        secret_value: Optional[
            pulumi.Input[
                ConnectionEventingConfigAuthConfigAdditionalVariableSecretValueArgs
            ]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyValue")
    def encryption_key_value(
        self,
    ) -> Optional[
        pulumi.Input[
            ConnectionEventingConfigAuthConfigAdditionalVariableEncryptionKeyValueArgs
        ]
    ]: ...
    @encryption_key_value.setter
    def encryption_key_value(
        self,
        value: Optional[
            pulumi.Input[
                ConnectionEventingConfigAuthConfigAdditionalVariableEncryptionKeyValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secretValue")
    def secret_value(
        self,
    ) -> Optional[
        pulumi.Input[
            ConnectionEventingConfigAuthConfigAdditionalVariableSecretValueArgs
        ]
    ]: ...
    @secret_value.setter
    def secret_value(
        self,
        value: Optional[
            pulumi.Input[
                ConnectionEventingConfigAuthConfigAdditionalVariableSecretValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionEventingConfigAuthConfigAdditionalVariableEncryptionKeyValueArgsDict(
    TypedDict
):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionEventingConfigAuthConfigAdditionalVariableEncryptionKeyValueArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionEventingConfigAuthConfigAdditionalVariableSecretValueArgsDict(
    TypedDict
):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionEventingConfigAuthConfigAdditionalVariableSecretValueArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionEventingConfigAuthConfigUserPasswordArgsDict(TypedDict):
    password: NotRequired[
        pulumi.Input[ConnectionEventingConfigAuthConfigUserPasswordPasswordArgsDict]
    ]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionEventingConfigAuthConfigUserPasswordArgs:
    def __init__(
        __self__,
        *,
        password: Optional[
            pulumi.Input[ConnectionEventingConfigAuthConfigUserPasswordPasswordArgs]
        ] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionEventingConfigAuthConfigUserPasswordPasswordArgs]
    ]: ...
    @password.setter
    def password(
        self,
        value: Optional[
            pulumi.Input[ConnectionEventingConfigAuthConfigUserPasswordPasswordArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionEventingConfigAuthConfigUserPasswordPasswordArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionEventingConfigAuthConfigUserPasswordPasswordArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionEventingConfigRegistrationDestinationConfigArgsDict(TypedDict):
    destinations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ConnectionEventingConfigRegistrationDestinationConfigDestinationArgsDict
                ]
            ]
        ]
    ]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionEventingConfigRegistrationDestinationConfigArgs:
    def __init__(
        __self__,
        *,
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ConnectionEventingConfigRegistrationDestinationConfigDestinationArgs
                    ]
                ]
            ]
        ] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ConnectionEventingConfigRegistrationDestinationConfigDestinationArgs
                ]
            ]
        ]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ConnectionEventingConfigRegistrationDestinationConfigDestinationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionEventingConfigRegistrationDestinationConfigDestinationArgsDict(
    TypedDict
):
    host: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    service_attachment: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionEventingConfigRegistrationDestinationConfigDestinationArgs:
    def __init__(
        __self__,
        *,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionEventingRuntimeDataArgsDict(TypedDict):
    events_listener_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    statuses: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ConnectionEventingRuntimeDataStatusArgsDict]]
        ]
    ]

@pulumi.input_type
class ConnectionEventingRuntimeDataArgs:
    def __init__(
        __self__,
        *,
        events_listener_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectionEventingRuntimeDataStatusArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventsListenerEndpoint")
    def events_listener_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @events_listener_endpoint.setter
    def events_listener_endpoint(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConnectionEventingRuntimeDataStatusArgs]]]
    ]: ...
    @statuses.setter
    def statuses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectionEventingRuntimeDataStatusArgs]]
            ]
        ],
    ): ...

class ConnectionEventingRuntimeDataStatusArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionEventingRuntimeDataStatusArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionLockConfigArgsDict(TypedDict):
    locked: pulumi.Input[_builtins.bool]
    reason: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionLockConfigArgs:
    def __init__(
        __self__,
        *,
        locked: pulumi.Input[_builtins.bool],
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def locked(self) -> pulumi.Input[_builtins.bool]: ...
    @locked.setter
    def locked(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionLogConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    level: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionLogConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        level: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @level.setter
    def level(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionNodeConfigArgsDict(TypedDict):
    max_node_count: NotRequired[pulumi.Input[_builtins.int]]
    min_node_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ConnectionNodeConfigArgs:
    def __init__(
        __self__,
        *,
        max_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_node_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_node_count.setter
    def max_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_node_count.setter
    def min_node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ConnectionSslConfigArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    additional_variables: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ConnectionSslConfigAdditionalVariableArgsDict]]
        ]
    ]
    client_cert_type: NotRequired[pulumi.Input[_builtins.str]]
    client_certificate: NotRequired[
        pulumi.Input[ConnectionSslConfigClientCertificateArgsDict]
    ]
    client_private_key: NotRequired[
        pulumi.Input[ConnectionSslConfigClientPrivateKeyArgsDict]
    ]
    client_private_key_pass: NotRequired[
        pulumi.Input[ConnectionSslConfigClientPrivateKeyPassArgsDict]
    ]
    private_server_certificate: NotRequired[
        pulumi.Input[ConnectionSslConfigPrivateServerCertificateArgsDict]
    ]
    server_cert_type: NotRequired[pulumi.Input[_builtins.str]]
    trust_model: NotRequired[pulumi.Input[_builtins.str]]
    use_ssl: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ConnectionSslConfigArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        additional_variables: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectionSslConfigAdditionalVariableArgs]]
            ]
        ] = ...,
        client_cert_type: Optional[pulumi.Input[_builtins.str]] = ...,
        client_certificate: Optional[
            pulumi.Input[ConnectionSslConfigClientCertificateArgs]
        ] = ...,
        client_private_key: Optional[
            pulumi.Input[ConnectionSslConfigClientPrivateKeyArgs]
        ] = ...,
        client_private_key_pass: Optional[
            pulumi.Input[ConnectionSslConfigClientPrivateKeyPassArgs]
        ] = ...,
        private_server_certificate: Optional[
            pulumi.Input[ConnectionSslConfigPrivateServerCertificateArgs]
        ] = ...,
        server_cert_type: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_model: Optional[pulumi.Input[_builtins.str]] = ...,
        use_ssl: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalVariables")
    def additional_variables(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConnectionSslConfigAdditionalVariableArgs]]]
    ]: ...
    @additional_variables.setter
    def additional_variables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ConnectionSslConfigAdditionalVariableArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientCertType")
    def client_cert_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_cert_type.setter
    def client_cert_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(
        self,
    ) -> Optional[pulumi.Input[ConnectionSslConfigClientCertificateArgs]]: ...
    @client_certificate.setter
    def client_certificate(
        self, value: Optional[pulumi.Input[ConnectionSslConfigClientCertificateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientPrivateKey")
    def client_private_key(
        self,
    ) -> Optional[pulumi.Input[ConnectionSslConfigClientPrivateKeyArgs]]: ...
    @client_private_key.setter
    def client_private_key(
        self, value: Optional[pulumi.Input[ConnectionSslConfigClientPrivateKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientPrivateKeyPass")
    def client_private_key_pass(
        self,
    ) -> Optional[pulumi.Input[ConnectionSslConfigClientPrivateKeyPassArgs]]: ...
    @client_private_key_pass.setter
    def client_private_key_pass(
        self, value: Optional[pulumi.Input[ConnectionSslConfigClientPrivateKeyPassArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateServerCertificate")
    def private_server_certificate(
        self,
    ) -> Optional[pulumi.Input[ConnectionSslConfigPrivateServerCertificateArgs]]: ...
    @private_server_certificate.setter
    def private_server_certificate(
        self,
        value: Optional[pulumi.Input[ConnectionSslConfigPrivateServerCertificateArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverCertType")
    def server_cert_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_cert_type.setter
    def server_cert_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trustModel")
    def trust_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trust_model.setter
    def trust_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useSsl")
    def use_ssl(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_ssl.setter
    def use_ssl(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ConnectionSslConfigAdditionalVariableArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    encryption_key_value: NotRequired[
        pulumi.Input[ConnectionSslConfigAdditionalVariableEncryptionKeyValueArgsDict]
    ]
    integer_value: NotRequired[pulumi.Input[_builtins.int]]
    secret_value: NotRequired[
        pulumi.Input[ConnectionSslConfigAdditionalVariableSecretValueArgsDict]
    ]
    string_value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionSslConfigAdditionalVariableArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_key_value: Optional[
            pulumi.Input[ConnectionSslConfigAdditionalVariableEncryptionKeyValueArgs]
        ] = ...,
        integer_value: Optional[pulumi.Input[_builtins.int]] = ...,
        secret_value: Optional[
            pulumi.Input[ConnectionSslConfigAdditionalVariableSecretValueArgs]
        ] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyValue")
    def encryption_key_value(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionSslConfigAdditionalVariableEncryptionKeyValueArgs]
    ]: ...
    @encryption_key_value.setter
    def encryption_key_value(
        self,
        value: Optional[
            pulumi.Input[ConnectionSslConfigAdditionalVariableEncryptionKeyValueArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secretValue")
    def secret_value(
        self,
    ) -> Optional[
        pulumi.Input[ConnectionSslConfigAdditionalVariableSecretValueArgs]
    ]: ...
    @secret_value.setter
    def secret_value(
        self,
        value: Optional[
            pulumi.Input[ConnectionSslConfigAdditionalVariableSecretValueArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionSslConfigAdditionalVariableEncryptionKeyValueArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionSslConfigAdditionalVariableEncryptionKeyValueArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionSslConfigAdditionalVariableSecretValueArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionSslConfigAdditionalVariableSecretValueArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionSslConfigClientCertificateArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionSslConfigClientCertificateArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionSslConfigClientPrivateKeyArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionSslConfigClientPrivateKeyArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionSslConfigClientPrivateKeyPassArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionSslConfigClientPrivateKeyPassArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionSslConfigPrivateServerCertificateArgsDict(TypedDict):
    secret_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectionSslConfigPrivateServerCertificateArgs:
    def __init__(__self__, *, secret_version: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): ...

class ConnectionStatusArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionStatusArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
