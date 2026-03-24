import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AuthConfigClientCertificateArgs",
    "AuthConfigClientCertificateArgsDict",
    "AuthConfigDecryptedCredentialArgs",
    "AuthConfigDecryptedCredentialArgsDict",
    "AuthConfigDecryptedCredentialAuthTokenArgs",
    "AuthConfigDecryptedCredentialAuthTokenArgsDict",
    "AuthConfigDecryptedCredentialJwtArgs",
    "AuthConfigDecryptedCredentialJwtArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AuthConfigDecryptedCredentialOidcTokenArgs",
    "AuthConfigDecryptedCredentialOidcTokenArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ClientCloudKmsConfigArgs",
    "ClientCloudKmsConfigArgsDict",
]

class AuthConfigClientCertificateArgsDict(TypedDict):
    encrypted_private_key: pulumi.Input[_builtins.str]
    ssl_certificate: pulumi.Input[_builtins.str]
    passphrase: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AuthConfigClientCertificateArgs:
    def __init__(
        __self__,
        *,
        encrypted_private_key: pulumi.Input[_builtins.str],
        ssl_certificate: pulumi.Input[_builtins.str],
        passphrase: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptedPrivateKey")
    def encrypted_private_key(self) -> pulumi.Input[_builtins.str]: ...
    @encrypted_private_key.setter
    def encrypted_private_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sslCertificate")
    def ssl_certificate(self) -> pulumi.Input[_builtins.str]: ...
    @ssl_certificate.setter
    def ssl_certificate(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @passphrase.setter
    def passphrase(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthConfigDecryptedCredentialArgsDict(TypedDict):
    credential_type: pulumi.Input[_builtins.str]
    auth_token: NotRequired[
        pulumi.Input[AuthConfigDecryptedCredentialAuthTokenArgsDict]
    ]
    jwt: NotRequired[pulumi.Input[AuthConfigDecryptedCredentialJwtArgsDict]]
    oauth2_authorization_code: NotRequired[
        pulumi.Input[AuthConfigDecryptedCredentialOauth2AuthorizationCodeArgsDict]
    ]
    oauth2_client_credentials: NotRequired[
        pulumi.Input[AuthConfigDecryptedCredentialOauth2ClientCredentialsArgsDict]
    ]
    oidc_token: NotRequired[
        pulumi.Input[AuthConfigDecryptedCredentialOidcTokenArgsDict]
    ]
    service_account_credentials: NotRequired[
        pulumi.Input[AuthConfigDecryptedCredentialServiceAccountCredentialsArgsDict]
    ]
    username_and_password: NotRequired[
        pulumi.Input[AuthConfigDecryptedCredentialUsernameAndPasswordArgsDict]
    ]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialArgs:
    def __init__(
        __self__,
        *,
        credential_type: pulumi.Input[_builtins.str],
        auth_token: Optional[
            pulumi.Input[AuthConfigDecryptedCredentialAuthTokenArgs]
        ] = ...,
        jwt: Optional[pulumi.Input[AuthConfigDecryptedCredentialJwtArgs]] = ...,
        oauth2_authorization_code: Optional[
            pulumi.Input[AuthConfigDecryptedCredentialOauth2AuthorizationCodeArgs]
        ] = ...,
        oauth2_client_credentials: Optional[
            pulumi.Input[AuthConfigDecryptedCredentialOauth2ClientCredentialsArgs]
        ] = ...,
        oidc_token: Optional[
            pulumi.Input[AuthConfigDecryptedCredentialOidcTokenArgs]
        ] = ...,
        service_account_credentials: Optional[
            pulumi.Input[AuthConfigDecryptedCredentialServiceAccountCredentialsArgs]
        ] = ...,
        username_and_password: Optional[
            pulumi.Input[AuthConfigDecryptedCredentialUsernameAndPasswordArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="credentialType")
    def credential_type(self) -> pulumi.Input[_builtins.str]: ...
    @credential_type.setter
    def credential_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authToken")
    def auth_token(
        self,
    ) -> Optional[pulumi.Input[AuthConfigDecryptedCredentialAuthTokenArgs]]: ...
    @auth_token.setter
    def auth_token(
        self, value: Optional[pulumi.Input[AuthConfigDecryptedCredentialAuthTokenArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def jwt(self) -> Optional[pulumi.Input[AuthConfigDecryptedCredentialJwtArgs]]: ...
    @jwt.setter
    def jwt(
        self, value: Optional[pulumi.Input[AuthConfigDecryptedCredentialJwtArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oauth2AuthorizationCode")
    def oauth2_authorization_code(
        self,
    ) -> Optional[
        pulumi.Input[AuthConfigDecryptedCredentialOauth2AuthorizationCodeArgs]
    ]: ...
    @oauth2_authorization_code.setter
    def oauth2_authorization_code(
        self,
        value: Optional[
            pulumi.Input[AuthConfigDecryptedCredentialOauth2AuthorizationCodeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="oauth2ClientCredentials")
    def oauth2_client_credentials(
        self,
    ) -> Optional[
        pulumi.Input[AuthConfigDecryptedCredentialOauth2ClientCredentialsArgs]
    ]: ...
    @oauth2_client_credentials.setter
    def oauth2_client_credentials(
        self,
        value: Optional[
            pulumi.Input[AuthConfigDecryptedCredentialOauth2ClientCredentialsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="oidcToken")
    def oidc_token(
        self,
    ) -> Optional[pulumi.Input[AuthConfigDecryptedCredentialOidcTokenArgs]]: ...
    @oidc_token.setter
    def oidc_token(
        self, value: Optional[pulumi.Input[AuthConfigDecryptedCredentialOidcTokenArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountCredentials")
    def service_account_credentials(
        self,
    ) -> Optional[
        pulumi.Input[AuthConfigDecryptedCredentialServiceAccountCredentialsArgs]
    ]: ...
    @service_account_credentials.setter
    def service_account_credentials(
        self,
        value: Optional[
            pulumi.Input[AuthConfigDecryptedCredentialServiceAccountCredentialsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="usernameAndPassword")
    def username_and_password(
        self,
    ) -> Optional[
        pulumi.Input[AuthConfigDecryptedCredentialUsernameAndPasswordArgs]
    ]: ...
    @username_and_password.setter
    def username_and_password(
        self,
        value: Optional[
            pulumi.Input[AuthConfigDecryptedCredentialUsernameAndPasswordArgs]
        ],
    ): ...

class AuthConfigDecryptedCredentialAuthTokenArgsDict(TypedDict):
    token: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialAuthTokenArgs:
    def __init__(
        __self__,
        *,
        token: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token.setter
    def token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthConfigDecryptedCredentialJwtArgsDict(TypedDict):
    jwt: NotRequired[pulumi.Input[_builtins.str]]
    jwt_header: NotRequired[pulumi.Input[_builtins.str]]
    jwt_payload: NotRequired[pulumi.Input[_builtins.str]]
    secret: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialJwtArgs:
    def __init__(
        __self__,
        *,
        jwt: Optional[pulumi.Input[_builtins.str]] = ...,
        jwt_header: Optional[pulumi.Input[_builtins.str]] = ...,
        jwt_payload: Optional[pulumi.Input[_builtins.str]] = ...,
        secret: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def jwt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @jwt.setter
    def jwt(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jwtHeader")
    def jwt_header(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @jwt_header.setter
    def jwt_header(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jwtPayload")
    def jwt_payload(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @jwt_payload.setter
    def jwt_payload(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret.setter
    def secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthConfigDecryptedCredentialOauth2AuthorizationCodeArgsDict(TypedDict):
    auth_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    token_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialOauth2AuthorizationCodeArgs:
    def __init__(
        __self__,
        *,
        auth_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        token_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authEndpoint")
    def auth_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_endpoint.setter
    def auth_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthConfigDecryptedCredentialOauth2ClientCredentialsArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    request_type: NotRequired[pulumi.Input[_builtins.str]]
    scope: NotRequired[pulumi.Input[_builtins.str]]
    token_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    token_params: NotRequired[
        pulumi.Input[
            AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        request_type: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        token_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        token_params: Optional[
            pulumi.Input[
                AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestType")
    def request_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_type.setter
    def request_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tokenParams")
    def token_params(
        self,
    ) -> Optional[
        pulumi.Input[
            AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsArgs
        ]
    ]: ...
    @token_params.setter
    def token_params(
        self,
        value: Optional[
            pulumi.Input[
                AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsArgs
            ]
        ],
    ): ...

class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsArgsDict(
    TypedDict
):
    entries: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsArgs:
    def __init__(
        __self__,
        *,
        entries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entries(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryArgs
                ]
            ]
        ]
    ]: ...
    @entries.setter
    def entries(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryArgs
                    ]
                ]
            ]
        ],
    ): ...

class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryArgsDict(
    TypedDict
):
    key: NotRequired[
        pulumi.Input[
            AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyArgsDict
        ]
    ]
    value: NotRequired[
        pulumi.Input[
            AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueArgsDict
        ]
    ]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryArgs:
    def __init__(
        __self__,
        *,
        key: Optional[
            pulumi.Input[
                AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyArgs
            ]
        ] = ...,
        value: Optional[
            pulumi.Input[
                AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(
        self,
    ) -> Optional[
        pulumi.Input[
            AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyArgs
        ]
    ]: ...
    @key.setter
    def key(
        self,
        value: Optional[
            pulumi.Input[
                AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[
        pulumi.Input[
            AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueArgs
        ]
    ]: ...
    @value.setter
    def value(
        self,
        value: Optional[
            pulumi.Input[
                AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueArgs
            ]
        ],
    ): ...

class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyArgsDict(
    TypedDict
):
    literal_value: NotRequired[
        pulumi.Input[
            AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyLiteralValueArgsDict
        ]
    ]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyArgs:
    def __init__(
        __self__,
        *,
        literal_value: Optional[
            pulumi.Input[
                AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyLiteralValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="literalValue")
    def literal_value(
        self,
    ) -> Optional[
        pulumi.Input[
            AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyLiteralValueArgs
        ]
    ]: ...
    @literal_value.setter
    def literal_value(
        self,
        value: Optional[
            pulumi.Input[
                AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyLiteralValueArgs
            ]
        ],
    ): ...

class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyLiteralValueArgsDict(
    TypedDict
):
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyLiteralValueArgs:
    def __init__(
        __self__, *, string_value: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueArgsDict(
    TypedDict
):
    literal_value: NotRequired[
        pulumi.Input[
            AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueLiteralValueArgsDict
        ]
    ]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueArgs:
    def __init__(
        __self__,
        *,
        literal_value: Optional[
            pulumi.Input[
                AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueLiteralValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="literalValue")
    def literal_value(
        self,
    ) -> Optional[
        pulumi.Input[
            AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueLiteralValueArgs
        ]
    ]: ...
    @literal_value.setter
    def literal_value(
        self,
        value: Optional[
            pulumi.Input[
                AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueLiteralValueArgs
            ]
        ],
    ): ...

class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueLiteralValueArgsDict(
    TypedDict
):
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueLiteralValueArgs:
    def __init__(
        __self__, *, string_value: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthConfigDecryptedCredentialOidcTokenArgsDict(TypedDict):
    audience: NotRequired[pulumi.Input[_builtins.str]]
    service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    token: NotRequired[pulumi.Input[_builtins.str]]
    token_expire_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialOidcTokenArgs:
    def __init__(
        __self__,
        *,
        audience: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        token: Optional[pulumi.Input[_builtins.str]] = ...,
        token_expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audience.setter
    def audience(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token.setter
    def token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tokenExpireTime")
    def token_expire_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_expire_time.setter
    def token_expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthConfigDecryptedCredentialServiceAccountCredentialsArgsDict(TypedDict):
    scope: NotRequired[pulumi.Input[_builtins.str]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialServiceAccountCredentialsArgs:
    def __init__(
        __self__,
        *,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthConfigDecryptedCredentialUsernameAndPasswordArgsDict(TypedDict):
    password: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AuthConfigDecryptedCredentialUsernameAndPasswordArgs:
    def __init__(
        __self__,
        *,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClientCloudKmsConfigArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    kms_location: pulumi.Input[_builtins.str]
    kms_ring: pulumi.Input[_builtins.str]
    key_version: NotRequired[pulumi.Input[_builtins.str]]
    kms_project_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClientCloudKmsConfigArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        kms_location: pulumi.Input[_builtins.str],
        kms_ring: pulumi.Input[_builtins.str],
        key_version: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsLocation")
    def kms_location(self) -> pulumi.Input[_builtins.str]: ...
    @kms_location.setter
    def kms_location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsRing")
    def kms_ring(self) -> pulumi.Input[_builtins.str]: ...
    @kms_ring.setter
    def kms_ring(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsProjectId")
    def kms_project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_project_id.setter
    def kms_project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
