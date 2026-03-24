

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AuthConfigClientCertificate', 'AuthConfigDecryptedCredential', 'AuthConfigDecryptedCredentialAuthToken', 'AuthConfigDecryptedCredentialJwt', ..., ..., ..., ..., ..., ..., ..., ..., 'AuthConfigDecryptedCredentialOidcToken', ..., 'AuthConfigDecryptedCredentialUsernameAndPassword', 'ClientCloudKmsConfig']
@pulumi.output_type
class AuthConfigClientCertificate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, encrypted_private_key: _builtins.str, ssl_certificate: _builtins.str, passphrase: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptedPrivateKey")
    def encrypted_private_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCertificate")
    def ssl_certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredential(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, credential_type: _builtins.str, auth_token: Optional[outputs.AuthConfigDecryptedCredentialAuthToken] = ..., jwt: Optional[outputs.AuthConfigDecryptedCredentialJwt] = ..., oauth2_authorization_code: Optional[outputs.AuthConfigDecryptedCredentialOauth2AuthorizationCode] = ..., oauth2_client_credentials: Optional[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentials] = ..., oidc_token: Optional[outputs.AuthConfigDecryptedCredentialOidcToken] = ..., service_account_credentials: Optional[outputs.AuthConfigDecryptedCredentialServiceAccountCredentials] = ..., username_and_password: Optional[outputs.AuthConfigDecryptedCredentialUsernameAndPassword] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialType")
    def credential_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> Optional[outputs.AuthConfigDecryptedCredentialAuthToken]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def jwt(self) -> Optional[outputs.AuthConfigDecryptedCredentialJwt]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2AuthorizationCode")
    def oauth2_authorization_code(self) -> Optional[outputs.AuthConfigDecryptedCredentialOauth2AuthorizationCode]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2ClientCredentials")
    def oauth2_client_credentials(self) -> Optional[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentials]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcToken")
    def oidc_token(self) -> Optional[outputs.AuthConfigDecryptedCredentialOidcToken]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountCredentials")
    def service_account_credentials(self) -> Optional[outputs.AuthConfigDecryptedCredentialServiceAccountCredentials]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usernameAndPassword")
    def username_and_password(self) -> Optional[outputs.AuthConfigDecryptedCredentialUsernameAndPassword]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialAuthToken(dict):
    def __init__(__self__, *, token: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialJwt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, jwt: Optional[_builtins.str] = ..., jwt_header: Optional[_builtins.str] = ..., jwt_payload: Optional[_builtins.str] = ..., secret: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def jwt(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwtHeader")
    def jwt_header(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwtPayload")
    def jwt_payload(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialOauth2AuthorizationCode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auth_endpoint: Optional[_builtins.str] = ..., client_id: Optional[_builtins.str] = ..., client_secret: Optional[_builtins.str] = ..., scope: Optional[_builtins.str] = ..., token_endpoint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authEndpoint")
    def auth_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialOauth2ClientCredentials(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., client_secret: Optional[_builtins.str] = ..., request_type: Optional[_builtins.str] = ..., scope: Optional[_builtins.str] = ..., token_endpoint: Optional[_builtins.str] = ..., token_params: Optional[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParams] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestType")
    def request_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenParams")
    def token_params(self) -> Optional[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParams]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParams(dict):
    def __init__(__self__, *, entries: Optional[Sequence[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntry]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entries(self) -> Optional[Sequence[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntry]]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntry(dict):
    def __init__(__self__, *, key: Optional[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKey] = ..., value: Optional[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKey]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValue]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, literal_value: Optional[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyLiteralValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="literalValue")
    def literal_value(self) -> Optional[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyLiteralValue]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryKeyLiteralValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, literal_value: Optional[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueLiteralValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="literalValue")
    def literal_value(self) -> Optional[outputs.AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueLiteralValue]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialOauth2ClientCredentialsTokenParamsEntryValueLiteralValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialOidcToken(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, audience: Optional[_builtins.str] = ..., service_account_email: Optional[_builtins.str] = ..., token: Optional[_builtins.str] = ..., token_expire_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def audience(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenExpireTime")
    def token_expire_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialServiceAccountCredentials(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scope: Optional[_builtins.str] = ..., service_account: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AuthConfigDecryptedCredentialUsernameAndPassword(dict):
    def __init__(__self__, *, password: Optional[_builtins.str] = ..., username: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ClientCloudKmsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, key: _builtins.str, kms_location: _builtins.str, kms_ring: _builtins.str, key_version: Optional[_builtins.str] = ..., kms_project_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsLocation")
    def kms_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsRing")
    def kms_ring(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsProjectId")
    def kms_project_id(self) -> Optional[_builtins.str]:
        
        ...
    


