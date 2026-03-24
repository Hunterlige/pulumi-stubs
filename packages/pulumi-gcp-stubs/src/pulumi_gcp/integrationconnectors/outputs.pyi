import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectionAuthConfig",
    "ConnectionAuthConfigAdditionalVariable",
    ...,
    "ConnectionAuthConfigAdditionalVariableSecretValue",
    "ConnectionAuthConfigOauth2AuthCodeFlow",
    "ConnectionAuthConfigOauth2AuthCodeFlowClientSecret",
    "ConnectionAuthConfigOauth2ClientCredentials",
    ...,
    "ConnectionAuthConfigOauth2JwtBearer",
    "ConnectionAuthConfigOauth2JwtBearerClientKey",
    "ConnectionAuthConfigOauth2JwtBearerJwtClaims",
    "ConnectionAuthConfigSshPublicKey",
    "ConnectionAuthConfigSshPublicKeySshClientCert",
    "ConnectionAuthConfigSshPublicKeySshClientCertPass",
    "ConnectionAuthConfigUserPassword",
    "ConnectionAuthConfigUserPasswordPassword",
    "ConnectionConfigVariable",
    "ConnectionConfigVariableEncryptionKeyValue",
    "ConnectionConfigVariableSecretValue",
    "ConnectionConnectorVersionInfraConfig",
    "ConnectionDestinationConfig",
    "ConnectionDestinationConfigDestination",
    "ConnectionEventingConfig",
    "ConnectionEventingConfigAdditionalVariable",
    ...,
    ...,
    "ConnectionEventingConfigAuthConfig",
    ...,
    ...,
    ...,
    "ConnectionEventingConfigAuthConfigUserPassword",
    ...,
    ...,
    ...,
    "ConnectionEventingRuntimeData",
    "ConnectionEventingRuntimeDataStatus",
    "ConnectionLockConfig",
    "ConnectionLogConfig",
    "ConnectionNodeConfig",
    "ConnectionSslConfig",
    "ConnectionSslConfigAdditionalVariable",
    ...,
    "ConnectionSslConfigAdditionalVariableSecretValue",
    "ConnectionSslConfigClientCertificate",
    "ConnectionSslConfigClientPrivateKey",
    "ConnectionSslConfigClientPrivateKeyPass",
    "ConnectionSslConfigPrivateServerCertificate",
    "ConnectionStatus",
]

@pulumi.output_type
class ConnectionAuthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_type: _builtins.str,
        additional_variables: Optional[
            Sequence[outputs.ConnectionAuthConfigAdditionalVariable]
        ] = ...,
        auth_key: Optional[_builtins.str] = ...,
        oauth2_auth_code_flow: Optional[
            outputs.ConnectionAuthConfigOauth2AuthCodeFlow
        ] = ...,
        oauth2_client_credentials: Optional[
            outputs.ConnectionAuthConfigOauth2ClientCredentials
        ] = ...,
        oauth2_jwt_bearer: Optional[outputs.ConnectionAuthConfigOauth2JwtBearer] = ...,
        ssh_public_key: Optional[outputs.ConnectionAuthConfigSshPublicKey] = ...,
        user_password: Optional[outputs.ConnectionAuthConfigUserPassword] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalVariables")
    def additional_variables(
        self,
    ) -> Optional[Sequence[outputs.ConnectionAuthConfigAdditionalVariable]]: ...
    @_builtins.property
    @pulumi.getter(name="authKey")
    def auth_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauth2AuthCodeFlow")
    def oauth2_auth_code_flow(
        self,
    ) -> Optional[outputs.ConnectionAuthConfigOauth2AuthCodeFlow]: ...
    @_builtins.property
    @pulumi.getter(name="oauth2ClientCredentials")
    def oauth2_client_credentials(
        self,
    ) -> Optional[outputs.ConnectionAuthConfigOauth2ClientCredentials]: ...
    @_builtins.property
    @pulumi.getter(name="oauth2JwtBearer")
    def oauth2_jwt_bearer(
        self,
    ) -> Optional[outputs.ConnectionAuthConfigOauth2JwtBearer]: ...
    @_builtins.property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> Optional[outputs.ConnectionAuthConfigSshPublicKey]: ...
    @_builtins.property
    @pulumi.getter(name="userPassword")
    def user_password(self) -> Optional[outputs.ConnectionAuthConfigUserPassword]: ...

@pulumi.output_type
class ConnectionAuthConfigAdditionalVariable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        boolean_value: Optional[_builtins.bool] = ...,
        encryption_key_value: Optional[
            outputs.ConnectionAuthConfigAdditionalVariableEncryptionKeyValue
        ] = ...,
        integer_value: Optional[_builtins.int] = ...,
        secret_value: Optional[
            outputs.ConnectionAuthConfigAdditionalVariableSecretValue
        ] = ...,
        string_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyValue")
    def encryption_key_value(
        self,
    ) -> Optional[outputs.ConnectionAuthConfigAdditionalVariableEncryptionKeyValue]: ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="secretValue")
    def secret_value(
        self,
    ) -> Optional[outputs.ConnectionAuthConfigAdditionalVariableSecretValue]: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionAuthConfigAdditionalVariableEncryptionKeyValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, type: _builtins.str, kms_key_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionAuthConfigAdditionalVariableSecretValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionAuthConfigOauth2AuthCodeFlow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_uri: Optional[_builtins.str] = ...,
        client_id: Optional[_builtins.str] = ...,
        client_secret: Optional[
            outputs.ConnectionAuthConfigOauth2AuthCodeFlowClientSecret
        ] = ...,
        enable_pkce: Optional[_builtins.bool] = ...,
        scopes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authUri")
    def auth_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(
        self,
    ) -> Optional[outputs.ConnectionAuthConfigOauth2AuthCodeFlowClientSecret]: ...
    @_builtins.property
    @pulumi.getter(name="enablePkce")
    def enable_pkce(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ConnectionAuthConfigOauth2AuthCodeFlowClientSecret(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionAuthConfigOauth2ClientCredentials(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        client_secret: Optional[
            outputs.ConnectionAuthConfigOauth2ClientCredentialsClientSecret
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(
        self,
    ) -> Optional[outputs.ConnectionAuthConfigOauth2ClientCredentialsClientSecret]: ...

@pulumi.output_type
class ConnectionAuthConfigOauth2ClientCredentialsClientSecret(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionAuthConfigOauth2JwtBearer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_key: Optional[
            outputs.ConnectionAuthConfigOauth2JwtBearerClientKey
        ] = ...,
        jwt_claims: Optional[
            outputs.ConnectionAuthConfigOauth2JwtBearerJwtClaims
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(
        self,
    ) -> Optional[outputs.ConnectionAuthConfigOauth2JwtBearerClientKey]: ...
    @_builtins.property
    @pulumi.getter(name="jwtClaims")
    def jwt_claims(
        self,
    ) -> Optional[outputs.ConnectionAuthConfigOauth2JwtBearerJwtClaims]: ...

@pulumi.output_type
class ConnectionAuthConfigOauth2JwtBearerClientKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionAuthConfigOauth2JwtBearerJwtClaims(dict):
    def __init__(
        __self__,
        *,
        audience: Optional[_builtins.str] = ...,
        issuer: Optional[_builtins.str] = ...,
        subject: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionAuthConfigSshPublicKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        username: _builtins.str,
        cert_type: Optional[_builtins.str] = ...,
        ssh_client_cert: Optional[
            outputs.ConnectionAuthConfigSshPublicKeySshClientCert
        ] = ...,
        ssh_client_cert_pass: Optional[
            outputs.ConnectionAuthConfigSshPublicKeySshClientCertPass
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certType")
    def cert_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sshClientCert")
    def ssh_client_cert(
        self,
    ) -> Optional[outputs.ConnectionAuthConfigSshPublicKeySshClientCert]: ...
    @_builtins.property
    @pulumi.getter(name="sshClientCertPass")
    def ssh_client_cert_pass(
        self,
    ) -> Optional[outputs.ConnectionAuthConfigSshPublicKeySshClientCertPass]: ...

@pulumi.output_type
class ConnectionAuthConfigSshPublicKeySshClientCert(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionAuthConfigSshPublicKeySshClientCertPass(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionAuthConfigUserPassword(dict):
    def __init__(
        __self__,
        *,
        username: _builtins.str,
        password: Optional[outputs.ConnectionAuthConfigUserPasswordPassword] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def password(
        self,
    ) -> Optional[outputs.ConnectionAuthConfigUserPasswordPassword]: ...

@pulumi.output_type
class ConnectionAuthConfigUserPasswordPassword(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionConfigVariable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        boolean_value: Optional[_builtins.bool] = ...,
        encryption_key_value: Optional[
            outputs.ConnectionConfigVariableEncryptionKeyValue
        ] = ...,
        integer_value: Optional[_builtins.int] = ...,
        secret_value: Optional[outputs.ConnectionConfigVariableSecretValue] = ...,
        string_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyValue")
    def encryption_key_value(
        self,
    ) -> Optional[outputs.ConnectionConfigVariableEncryptionKeyValue]: ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="secretValue")
    def secret_value(self) -> Optional[outputs.ConnectionConfigVariableSecretValue]: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionConfigVariableEncryptionKeyValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, type: _builtins.str, kms_key_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionConfigVariableSecretValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionConnectorVersionInfraConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, ratelimit_threshold: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ratelimitThreshold")
    def ratelimit_threshold(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionDestinationConfig(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        destinations: Optional[
            Sequence[outputs.ConnectionDestinationConfigDestination]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[Sequence[outputs.ConnectionDestinationConfigDestination]]: ...

@pulumi.output_type
class ConnectionDestinationConfigDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        service_attachment: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionEventingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        registration_destination_config: outputs.ConnectionEventingConfigRegistrationDestinationConfig,
        additional_variables: Optional[
            Sequence[outputs.ConnectionEventingConfigAdditionalVariable]
        ] = ...,
        auth_config: Optional[outputs.ConnectionEventingConfigAuthConfig] = ...,
        enrichment_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="registrationDestinationConfig")
    def registration_destination_config(
        self,
    ) -> outputs.ConnectionEventingConfigRegistrationDestinationConfig: ...
    @_builtins.property
    @pulumi.getter(name="additionalVariables")
    def additional_variables(
        self,
    ) -> Optional[Sequence[outputs.ConnectionEventingConfigAdditionalVariable]]: ...
    @_builtins.property
    @pulumi.getter(name="authConfig")
    def auth_config(self) -> Optional[outputs.ConnectionEventingConfigAuthConfig]: ...
    @_builtins.property
    @pulumi.getter(name="enrichmentEnabled")
    def enrichment_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConnectionEventingConfigAdditionalVariable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        boolean_value: Optional[_builtins.bool] = ...,
        encryption_key_value: Optional[
            outputs.ConnectionEventingConfigAdditionalVariableEncryptionKeyValue
        ] = ...,
        integer_value: Optional[_builtins.int] = ...,
        secret_value: Optional[
            outputs.ConnectionEventingConfigAdditionalVariableSecretValue
        ] = ...,
        string_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyValue")
    def encryption_key_value(
        self,
    ) -> Optional[
        outputs.ConnectionEventingConfigAdditionalVariableEncryptionKeyValue
    ]: ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="secretValue")
    def secret_value(
        self,
    ) -> Optional[outputs.ConnectionEventingConfigAdditionalVariableSecretValue]: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionEventingConfigAdditionalVariableEncryptionKeyValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionEventingConfigAdditionalVariableSecretValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionEventingConfigAuthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_type: _builtins.str,
        user_password: outputs.ConnectionEventingConfigAuthConfigUserPassword,
        additional_variables: Optional[
            Sequence[outputs.ConnectionEventingConfigAuthConfigAdditionalVariable]
        ] = ...,
        auth_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPassword")
    def user_password(
        self,
    ) -> outputs.ConnectionEventingConfigAuthConfigUserPassword: ...
    @_builtins.property
    @pulumi.getter(name="additionalVariables")
    def additional_variables(
        self,
    ) -> Optional[
        Sequence[outputs.ConnectionEventingConfigAuthConfigAdditionalVariable]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="authKey")
    def auth_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionEventingConfigAuthConfigAdditionalVariable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        boolean_value: Optional[_builtins.bool] = ...,
        encryption_key_value: Optional[
            outputs.ConnectionEventingConfigAuthConfigAdditionalVariableEncryptionKeyValue
        ] = ...,
        integer_value: Optional[_builtins.int] = ...,
        secret_value: Optional[
            outputs.ConnectionEventingConfigAuthConfigAdditionalVariableSecretValue
        ] = ...,
        string_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyValue")
    def encryption_key_value(
        self,
    ) -> Optional[
        outputs.ConnectionEventingConfigAuthConfigAdditionalVariableEncryptionKeyValue
    ]: ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="secretValue")
    def secret_value(
        self,
    ) -> Optional[
        outputs.ConnectionEventingConfigAuthConfigAdditionalVariableSecretValue
    ]: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionEventingConfigAuthConfigAdditionalVariableEncryptionKeyValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionEventingConfigAuthConfigAdditionalVariableSecretValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionEventingConfigAuthConfigUserPassword(dict):
    def __init__(
        __self__,
        *,
        password: Optional[
            outputs.ConnectionEventingConfigAuthConfigUserPasswordPassword
        ] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(
        self,
    ) -> Optional[outputs.ConnectionEventingConfigAuthConfigUserPasswordPassword]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionEventingConfigAuthConfigUserPasswordPassword(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionEventingConfigRegistrationDestinationConfig(dict):
    def __init__(
        __self__,
        *,
        destinations: Optional[
            Sequence[
                outputs.ConnectionEventingConfigRegistrationDestinationConfigDestination
            ]
        ] = ...,
        key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        Sequence[
            outputs.ConnectionEventingConfigRegistrationDestinationConfigDestination
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionEventingConfigRegistrationDestinationConfigDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        service_attachment: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionEventingRuntimeData(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        events_listener_endpoint: Optional[_builtins.str] = ...,
        statuses: Optional[Sequence[outputs.ConnectionEventingRuntimeDataStatus]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventsListenerEndpoint")
    def events_listener_endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[Sequence[outputs.ConnectionEventingRuntimeDataStatus]]: ...

@pulumi.output_type
class ConnectionEventingRuntimeDataStatus(dict):
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionLockConfig(dict):
    def __init__(
        __self__, *, locked: _builtins.bool, reason: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def locked(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionLogConfig(dict):
    def __init__(
        __self__, *, enabled: _builtins.bool, level: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionNodeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_node_count: Optional[_builtins.int] = ...,
        min_node_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ConnectionSslConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        additional_variables: Optional[
            Sequence[outputs.ConnectionSslConfigAdditionalVariable]
        ] = ...,
        client_cert_type: Optional[_builtins.str] = ...,
        client_certificate: Optional[
            outputs.ConnectionSslConfigClientCertificate
        ] = ...,
        client_private_key: Optional[outputs.ConnectionSslConfigClientPrivateKey] = ...,
        client_private_key_pass: Optional[
            outputs.ConnectionSslConfigClientPrivateKeyPass
        ] = ...,
        private_server_certificate: Optional[
            outputs.ConnectionSslConfigPrivateServerCertificate
        ] = ...,
        server_cert_type: Optional[_builtins.str] = ...,
        trust_model: Optional[_builtins.str] = ...,
        use_ssl: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalVariables")
    def additional_variables(
        self,
    ) -> Optional[Sequence[outputs.ConnectionSslConfigAdditionalVariable]]: ...
    @_builtins.property
    @pulumi.getter(name="clientCertType")
    def client_cert_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(
        self,
    ) -> Optional[outputs.ConnectionSslConfigClientCertificate]: ...
    @_builtins.property
    @pulumi.getter(name="clientPrivateKey")
    def client_private_key(
        self,
    ) -> Optional[outputs.ConnectionSslConfigClientPrivateKey]: ...
    @_builtins.property
    @pulumi.getter(name="clientPrivateKeyPass")
    def client_private_key_pass(
        self,
    ) -> Optional[outputs.ConnectionSslConfigClientPrivateKeyPass]: ...
    @_builtins.property
    @pulumi.getter(name="privateServerCertificate")
    def private_server_certificate(
        self,
    ) -> Optional[outputs.ConnectionSslConfigPrivateServerCertificate]: ...
    @_builtins.property
    @pulumi.getter(name="serverCertType")
    def server_cert_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trustModel")
    def trust_model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useSsl")
    def use_ssl(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConnectionSslConfigAdditionalVariable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        boolean_value: Optional[_builtins.bool] = ...,
        encryption_key_value: Optional[
            outputs.ConnectionSslConfigAdditionalVariableEncryptionKeyValue
        ] = ...,
        integer_value: Optional[_builtins.int] = ...,
        secret_value: Optional[
            outputs.ConnectionSslConfigAdditionalVariableSecretValue
        ] = ...,
        string_value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyValue")
    def encryption_key_value(
        self,
    ) -> Optional[outputs.ConnectionSslConfigAdditionalVariableEncryptionKeyValue]: ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="secretValue")
    def secret_value(
        self,
    ) -> Optional[outputs.ConnectionSslConfigAdditionalVariableSecretValue]: ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionSslConfigAdditionalVariableEncryptionKeyValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionSslConfigAdditionalVariableSecretValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionSslConfigClientCertificate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionSslConfigClientPrivateKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionSslConfigClientPrivateKeyPass(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionSslConfigPrivateServerCertificate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, secret_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectionStatus(dict):
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
