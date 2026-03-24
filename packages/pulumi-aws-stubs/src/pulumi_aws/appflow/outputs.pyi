import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectorProfileConnectorProfileConfig",
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
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FlowDestinationFlowConfig",
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
    "FlowMetadataCatalogConfig",
    "FlowMetadataCatalogConfigGlueDataCatalog",
    "FlowSourceFlowConfig",
    "FlowSourceFlowConfigIncrementalPullConfig",
    "FlowSourceFlowConfigSourceConnectorProperties",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FlowSourceFlowConfigSourceConnectorPropertiesS3",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "FlowSourceFlowConfigSourceConnectorPropertiesSlack",
    ...,
    "FlowSourceFlowConfigSourceConnectorPropertiesVeeva",
    ...,
    "FlowTask",
    "FlowTaskConnectorOperator",
    "FlowTriggerConfig",
    "FlowTriggerConfigTriggerProperties",
    "FlowTriggerConfigTriggerPropertiesScheduled",
]

@pulumi.output_type
class ConnectorProfileConnectorProfileConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connector_profile_credentials: outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentials,
        connector_profile_properties: outputs.ConnectorProfileConnectorProfileConfigConnectorProfileProperties,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorProfileCredentials")
    def connector_profile_credentials(
        self,
    ) -> outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentials: ...
    @_builtins.property
    @pulumi.getter(name="connectorProfileProperties")
    def connector_profile_properties(
        self,
    ) -> outputs.ConnectorProfileConnectorProfileConfigConnectorProfileProperties: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentials(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amplitude: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude
        ] = ...,
        custom_connector: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector
        ] = ...,
        datadog: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog
        ] = ...,
        dynatrace: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace
        ] = ...,
        google_analytics: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics
        ] = ...,
        honeycode: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode
        ] = ...,
        infor_nexus: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus
        ] = ...,
        marketo: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo
        ] = ...,
        redshift: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift
        ] = ...,
        salesforce: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce
        ] = ...,
        sapo_data: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData
        ] = ...,
        service_now: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow
        ] = ...,
        singular: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular
        ] = ...,
        slack: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack
        ] = ...,
        snowflake: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake
        ] = ...,
        trendmicro: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro
        ] = ...,
        veeva: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva
        ] = ...,
        zendesk: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amplitude(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customConnector")
    def custom_connector(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector
    ]: ...
    @_builtins.property
    @pulumi.getter
    def datadog(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog
    ]: ...
    @_builtins.property
    @pulumi.getter
    def dynatrace(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace
    ]: ...
    @_builtins.property
    @pulumi.getter(name="googleAnalytics")
    def google_analytics(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics
    ]: ...
    @_builtins.property
    @pulumi.getter
    def honeycode(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inforNexus")
    def infor_nexus(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus
    ]: ...
    @_builtins.property
    @pulumi.getter
    def marketo(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo
    ]: ...
    @_builtins.property
    @pulumi.getter
    def redshift(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift
    ]: ...
    @_builtins.property
    @pulumi.getter
    def salesforce(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sapoData")
    def sapo_data(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNow")
    def service_now(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow
    ]: ...
    @_builtins.property
    @pulumi.getter
    def singular(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular
    ]: ...
    @_builtins.property
    @pulumi.getter
    def slack(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack
    ]: ...
    @_builtins.property
    @pulumi.getter
    def snowflake(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake
    ]: ...
    @_builtins.property
    @pulumi.getter
    def trendmicro(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro
    ]: ...
    @_builtins.property
    @pulumi.getter
    def veeva(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva
    ]: ...
    @_builtins.property
    @pulumi.getter
    def zendesk(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk
    ]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, api_key: _builtins.str, secret_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authentication_type: _builtins.str,
        api_key: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey
        ] = ...,
        basic: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic
        ] = ...,
        custom: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom
        ] = ...,
        oauth2: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey
    ]: ...
    @_builtins.property
    @pulumi.getter
    def basic(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic
    ]: ...
    @_builtins.property
    @pulumi.getter
    def custom(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom
    ]: ...
    @_builtins.property
    @pulumi.getter
    def oauth2(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2
    ]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKey(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_key: _builtins.str,
        api_secret_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiSecretKey")
    def api_secret_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasic(
    dict
):
    def __init__(
        __self__, *, password: _builtins.str, username: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustom(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_authentication_type: _builtins.str,
        credentials_map: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customAuthenticationType")
    def custom_authentication_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="credentialsMap")
    def credentials_map(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_token: Optional[_builtins.str] = ...,
        client_id: Optional[_builtins.str] = ...,
        client_secret: Optional[_builtins.str] = ...,
        oauth_request: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest
        ] = ...,
        refresh_token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest
    ]: ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequest(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_code: Optional[_builtins.str] = ...,
        redirect_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, api_key: _builtins.str, application_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applicationKey")
    def application_key(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, api_token: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        client_secret: _builtins.str,
        access_token: Optional[_builtins.str] = ...,
        oauth_request: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest
        ] = ...,
        refresh_token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest
    ]: ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequest(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_code: Optional[_builtins.str] = ...,
        redirect_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_token: Optional[_builtins.str] = ...,
        oauth_request: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest
        ] = ...,
        refresh_token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest
    ]: ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequest(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_code: Optional[_builtins.str] = ...,
        redirect_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_key_id: _builtins.str,
        datakey: _builtins.str,
        secret_access_key: _builtins.str,
        user_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def datakey(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        client_secret: _builtins.str,
        access_token: Optional[_builtins.str] = ...,
        oauth_request: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest
    ]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequest(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_code: Optional[_builtins.str] = ...,
        redirect_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift(dict):
    def __init__(
        __self__, *, password: _builtins.str, username: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_token: Optional[_builtins.str] = ...,
        client_credentials_arn: Optional[_builtins.str] = ...,
        jwt_token: Optional[_builtins.str] = ...,
        oauth2_grant_type: Optional[_builtins.str] = ...,
        oauth_request: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest
        ] = ...,
        refresh_token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientCredentialsArn")
    def client_credentials_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jwtToken")
    def jwt_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauth2GrantType")
    def oauth2_grant_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest
    ]: ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequest(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_code: Optional[_builtins.str] = ...,
        redirect_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        basic_auth_credentials: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials
        ] = ...,
        oauth_credentials: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basicAuthCredentials")
    def basic_auth_credentials(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials
    ]: ...
    @_builtins.property
    @pulumi.getter(name="oauthCredentials")
    def oauth_credentials(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials
    ]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentials(
    dict
):
    def __init__(
        __self__, *, password: _builtins.str, username: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentials(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        client_secret: _builtins.str,
        access_token: Optional[_builtins.str] = ...,
        oauth_request: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest
        ] = ...,
        refresh_token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest
    ]: ...
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequest(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_code: Optional[_builtins.str] = ...,
        redirect_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow(dict):
    def __init__(
        __self__, *, password: _builtins.str, username: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, api_key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        client_secret: _builtins.str,
        access_token: Optional[_builtins.str] = ...,
        oauth_request: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest
    ]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequest(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_code: Optional[_builtins.str] = ...,
        redirect_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake(dict):
    def __init__(
        __self__, *, password: _builtins.str, username: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, api_secret_key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiSecretKey")
    def api_secret_key(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva(dict):
    def __init__(
        __self__, *, password: _builtins.str, username: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        client_secret: _builtins.str,
        access_token: Optional[_builtins.str] = ...,
        oauth_request: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest
    ]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequest(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_code: Optional[_builtins.str] = ...,
        redirect_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfileProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amplitude: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude
        ] = ...,
        custom_connector: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector
        ] = ...,
        datadog: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog
        ] = ...,
        dynatrace: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace
        ] = ...,
        google_analytics: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics
        ] = ...,
        honeycode: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode
        ] = ...,
        infor_nexus: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus
        ] = ...,
        marketo: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo
        ] = ...,
        redshift: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift
        ] = ...,
        salesforce: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce
        ] = ...,
        sapo_data: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData
        ] = ...,
        service_now: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow
        ] = ...,
        singular: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular
        ] = ...,
        slack: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack
        ] = ...,
        snowflake: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake
        ] = ...,
        trendmicro: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro
        ] = ...,
        veeva: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva
        ] = ...,
        zendesk: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amplitude(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customConnector")
    def custom_connector(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector
    ]: ...
    @_builtins.property
    @pulumi.getter
    def datadog(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog
    ]: ...
    @_builtins.property
    @pulumi.getter
    def dynatrace(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace
    ]: ...
    @_builtins.property
    @pulumi.getter(name="googleAnalytics")
    def google_analytics(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics
    ]: ...
    @_builtins.property
    @pulumi.getter
    def honeycode(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inforNexus")
    def infor_nexus(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus
    ]: ...
    @_builtins.property
    @pulumi.getter
    def marketo(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo
    ]: ...
    @_builtins.property
    @pulumi.getter
    def redshift(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift
    ]: ...
    @_builtins.property
    @pulumi.getter
    def salesforce(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sapoData")
    def sapo_data(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNow")
    def service_now(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow
    ]: ...
    @_builtins.property
    @pulumi.getter
    def singular(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular
    ]: ...
    @_builtins.property
    @pulumi.getter
    def slack(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack
    ]: ...
    @_builtins.property
    @pulumi.getter
    def snowflake(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake
    ]: ...
    @_builtins.property
    @pulumi.getter
    def trendmicro(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro
    ]: ...
    @_builtins.property
    @pulumi.getter
    def veeva(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva
    ]: ...
    @_builtins.property
    @pulumi.getter
    def zendesk(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk
    ]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitude(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnector(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        oauth2_properties: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties
        ] = ...,
        profile_properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oauth2Properties")
    def oauth2_properties(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties
    ]: ...
    @_builtins.property
    @pulumi.getter(name="profileProperties")
    def profile_properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2Properties(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        oauth2_grant_type: _builtins.str,
        token_url: _builtins.str,
        token_url_custom_properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oauth2GrantType")
    def oauth2_grant_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tokenUrl")
    def token_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tokenUrlCustomProperties")
    def token_url_custom_properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadog(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, instance_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatrace(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, instance_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalytics(
    dict
):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycode(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, instance_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, instance_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshift(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        role_arn: _builtins.str,
        bucket_prefix: Optional[_builtins.str] = ...,
        cluster_identifier: Optional[_builtins.str] = ...,
        data_api_role_arn: Optional[_builtins.str] = ...,
        database_name: Optional[_builtins.str] = ...,
        database_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataApiRoleArn")
    def data_api_role_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="databaseUrl")
    def database_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforce(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_url: Optional[_builtins.str] = ...,
        is_sandbox_environment: Optional[_builtins.bool] = ...,
        use_privatelink_for_metadata_and_authorization: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isSandboxEnvironment")
    def is_sandbox_environment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="usePrivatelinkForMetadataAndAuthorization")
    def use_privatelink_for_metadata_and_authorization(
        self,
    ) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoData(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_host_url: _builtins.str,
        application_service_path: _builtins.str,
        client_number: _builtins.str,
        port_number: _builtins.int,
        logon_language: Optional[_builtins.str] = ...,
        oauth_properties: Optional[
            outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties
        ] = ...,
        private_link_service_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationHostUrl")
    def application_host_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applicationServicePath")
    def application_service_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientNumber")
    def client_number(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="portNumber")
    def port_number(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="logonLanguage")
    def logon_language(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthProperties")
    def oauth_properties(
        self,
    ) -> Optional[
        outputs.ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties
    ]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceName")
    def private_link_service_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthProperties(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auth_code_url: _builtins.str,
        oauth_scopes: Sequence[_builtins.str],
        token_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authCodeUrl")
    def auth_code_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenUrl")
    def token_url(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, instance_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingular(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlack(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, instance_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflake(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        stage: _builtins.str,
        warehouse: _builtins.str,
        account_name: Optional[_builtins.str] = ...,
        bucket_prefix: Optional[_builtins.str] = ...,
        private_link_service_name: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def warehouse(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceName")
    def private_link_service_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicro(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeeva(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, instance_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendesk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, instance_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> _builtins.str: ...

@pulumi.output_type
class FlowDestinationFlowConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connector_type: _builtins.str,
        destination_connector_properties: outputs.FlowDestinationFlowConfigDestinationConnectorProperties,
        api_version: Optional[_builtins.str] = ...,
        connector_profile_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationConnectorProperties")
    def destination_connector_properties(
        self,
    ) -> outputs.FlowDestinationFlowConfigDestinationConnectorProperties: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorProfileName")
    def connector_profile_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_connector: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector
        ] = ...,
        customer_profiles: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles
        ] = ...,
        event_bridge: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge
        ] = ...,
        honeycode: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode
        ] = ...,
        lookout_metrics: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics
        ] = ...,
        marketo: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesMarketo
        ] = ...,
        redshift: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesRedshift
        ] = ...,
        s3: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesS3
        ] = ...,
        salesforce: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce
        ] = ...,
        sapo_data: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSapoData
        ] = ...,
        snowflake: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake
        ] = ...,
        upsolver: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver
        ] = ...,
        zendesk: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesZendesk
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customConnector")
    def custom_connector(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector
    ]: ...
    @_builtins.property
    @pulumi.getter(name="customerProfiles")
    def customer_profiles(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles
    ]: ...
    @_builtins.property
    @pulumi.getter(name="eventBridge")
    def event_bridge(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge
    ]: ...
    @_builtins.property
    @pulumi.getter
    def honeycode(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lookoutMetrics")
    def lookout_metrics(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics
    ]: ...
    @_builtins.property
    @pulumi.getter
    def marketo(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesMarketo
    ]: ...
    @_builtins.property
    @pulumi.getter
    def redshift(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesRedshift
    ]: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesS3
    ]: ...
    @_builtins.property
    @pulumi.getter
    def salesforce(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sapoData")
    def sapo_data(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSapoData
    ]: ...
    @_builtins.property
    @pulumi.getter
    def snowflake(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake
    ]: ...
    @_builtins.property
    @pulumi.getter
    def upsolver(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver
    ]: ...
    @_builtins.property
    @pulumi.getter
    def zendesk(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesZendesk
    ]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        entity_name: _builtins.str,
        custom_properties: Optional[Mapping[str, _builtins.str]] = ...,
        error_handling_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig
        ] = ...,
        id_field_names: Optional[Sequence[_builtins.str]] = ...,
        write_operation_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="idFieldNames")
    def id_field_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="writeOperationType")
    def write_operation_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        bucket_prefix: Optional[_builtins.str] = ...,
        fail_on_first_destination_error: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfiles(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_name: _builtins.str,
        object_type_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectTypeName")
    def object_type_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridge(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object: _builtins.str,
        error_handling_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig
    ]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        bucket_prefix: Optional[_builtins.str] = ...,
        fail_on_first_destination_error: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycode(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object: _builtins.str,
        error_handling_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig
    ]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        bucket_prefix: Optional[_builtins.str] = ...,
        fail_on_first_destination_error: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetrics(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesMarketo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object: _builtins.str,
        error_handling_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig
    ]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        bucket_prefix: Optional[_builtins.str] = ...,
        fail_on_first_destination_error: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesRedshift(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        intermediate_bucket_name: _builtins.str,
        object: _builtins.str,
        bucket_prefix: Optional[_builtins.str] = ...,
        error_handling_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="intermediateBucketName")
    def intermediate_bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig
    ]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        bucket_prefix: Optional[_builtins.str] = ...,
        fail_on_first_destination_error: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        bucket_prefix: Optional[_builtins.str] = ...,
        s3_output_format_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3OutputFormatConfig")
    def s3_output_format_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig
    ]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aggregation_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig
        ] = ...,
        file_type: Optional[_builtins.str] = ...,
        prefix_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig
        ] = ...,
        preserve_source_data_typing: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggregationConfig")
    def aggregation_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fileType")
    def file_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="prefixConfig")
    def prefix_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="preserveSourceDataTyping")
    def preserve_source_data_typing(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aggregation_type: Optional[_builtins.str] = ...,
        target_file_size: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggregationType")
    def aggregation_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetFileSize")
    def target_file_size(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        prefix_format: Optional[_builtins.str] = ...,
        prefix_hierarchies: Optional[Sequence[_builtins.str]] = ...,
        prefix_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="prefixFormat")
    def prefix_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="prefixHierarchies")
    def prefix_hierarchies(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="prefixType")
    def prefix_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforce(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object: _builtins.str,
        data_transfer_api: Optional[_builtins.str] = ...,
        error_handling_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig
        ] = ...,
        id_field_names: Optional[Sequence[_builtins.str]] = ...,
        write_operation_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataTransferApi")
    def data_transfer_api(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="idFieldNames")
    def id_field_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="writeOperationType")
    def write_operation_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        bucket_prefix: Optional[_builtins.str] = ...,
        fail_on_first_destination_error: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSapoData(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object_path: _builtins.str,
        error_handling_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig
        ] = ...,
        id_field_names: Optional[Sequence[_builtins.str]] = ...,
        success_response_handling_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig
        ] = ...,
        write_operation_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectPath")
    def object_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="idFieldNames")
    def id_field_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="successResponseHandlingConfig")
    def success_response_handling_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="writeOperationType")
    def write_operation_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        bucket_prefix: Optional[_builtins.str] = ...,
        fail_on_first_destination_error: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        bucket_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflake(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        intermediate_bucket_name: _builtins.str,
        object: _builtins.str,
        bucket_prefix: Optional[_builtins.str] = ...,
        error_handling_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="intermediateBucketName")
    def intermediate_bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig
    ]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        bucket_prefix: Optional[_builtins.str] = ...,
        fail_on_first_destination_error: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolver(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        s3_output_format_config: outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig,
        bucket_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3OutputFormatConfig")
    def s3_output_format_config(
        self,
    ) -> outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        prefix_config: outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig,
        aggregation_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig
        ] = ...,
        file_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="prefixConfig")
    def prefix_config(
        self,
    ) -> outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig: ...
    @_builtins.property
    @pulumi.getter(name="aggregationConfig")
    def aggregation_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fileType")
    def file_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, aggregation_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aggregationType")
    def aggregation_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        prefix_type: _builtins.str,
        prefix_format: Optional[_builtins.str] = ...,
        prefix_hierarchies: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="prefixType")
    def prefix_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="prefixFormat")
    def prefix_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="prefixHierarchies")
    def prefix_hierarchies(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesZendesk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object: _builtins.str,
        error_handling_config: Optional[
            outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig
        ] = ...,
        id_field_names: Optional[Sequence[_builtins.str]] = ...,
        write_operation_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(
        self,
    ) -> Optional[
        outputs.FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="idFieldNames")
    def id_field_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="writeOperationType")
    def write_operation_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: Optional[_builtins.str] = ...,
        bucket_prefix: Optional[_builtins.str] = ...,
        fail_on_first_destination_error: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FlowMetadataCatalogConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        glue_data_catalog: Optional[
            outputs.FlowMetadataCatalogConfigGlueDataCatalog
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="glueDataCatalog")
    def glue_data_catalog(
        self,
    ) -> Optional[outputs.FlowMetadataCatalogConfigGlueDataCatalog]: ...

@pulumi.output_type
class FlowMetadataCatalogConfigGlueDataCatalog(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database_name: _builtins.str,
        role_arn: _builtins.str,
        table_prefix: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> _builtins.str: ...

@pulumi.output_type
class FlowSourceFlowConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connector_type: _builtins.str,
        source_connector_properties: outputs.FlowSourceFlowConfigSourceConnectorProperties,
        api_version: Optional[_builtins.str] = ...,
        connector_profile_name: Optional[_builtins.str] = ...,
        incremental_pull_config: Optional[
            outputs.FlowSourceFlowConfigIncrementalPullConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceConnectorProperties")
    def source_connector_properties(
        self,
    ) -> outputs.FlowSourceFlowConfigSourceConnectorProperties: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectorProfileName")
    def connector_profile_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="incrementalPullConfig")
    def incremental_pull_config(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigIncrementalPullConfig]: ...

@pulumi.output_type
class FlowSourceFlowConfigIncrementalPullConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, datetime_type_field_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datetimeTypeFieldName")
    def datetime_type_field_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amplitude: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesAmplitude
        ] = ...,
        custom_connector: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesCustomConnector
        ] = ...,
        datadog: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesDatadog
        ] = ...,
        dynatrace: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesDynatrace
        ] = ...,
        google_analytics: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics
        ] = ...,
        infor_nexus: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesInforNexus
        ] = ...,
        marketo: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesMarketo
        ] = ...,
        s3: Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesS3] = ...,
        salesforce: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesSalesforce
        ] = ...,
        sapo_data: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesSapoData
        ] = ...,
        service_now: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesServiceNow
        ] = ...,
        singular: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesSingular
        ] = ...,
        slack: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesSlack
        ] = ...,
        trendmicro: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesTrendmicro
        ] = ...,
        veeva: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesVeeva
        ] = ...,
        zendesk: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesZendesk
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amplitude(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesAmplitude]: ...
    @_builtins.property
    @pulumi.getter(name="customConnector")
    def custom_connector(
        self,
    ) -> Optional[
        outputs.FlowSourceFlowConfigSourceConnectorPropertiesCustomConnector
    ]: ...
    @_builtins.property
    @pulumi.getter
    def datadog(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesDatadog]: ...
    @_builtins.property
    @pulumi.getter
    def dynatrace(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesDynatrace]: ...
    @_builtins.property
    @pulumi.getter(name="googleAnalytics")
    def google_analytics(
        self,
    ) -> Optional[
        outputs.FlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics
    ]: ...
    @_builtins.property
    @pulumi.getter(name="inforNexus")
    def infor_nexus(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesInforNexus]: ...
    @_builtins.property
    @pulumi.getter
    def marketo(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesMarketo]: ...
    @_builtins.property
    @pulumi.getter
    def s3(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesS3]: ...
    @_builtins.property
    @pulumi.getter
    def salesforce(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesSalesforce]: ...
    @_builtins.property
    @pulumi.getter(name="sapoData")
    def sapo_data(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesSapoData]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNow")
    def service_now(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesServiceNow]: ...
    @_builtins.property
    @pulumi.getter
    def singular(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesSingular]: ...
    @_builtins.property
    @pulumi.getter
    def slack(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesSlack]: ...
    @_builtins.property
    @pulumi.getter
    def trendmicro(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesTrendmicro]: ...
    @_builtins.property
    @pulumi.getter
    def veeva(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesVeeva]: ...
    @_builtins.property
    @pulumi.getter
    def zendesk(
        self,
    ) -> Optional[outputs.FlowSourceFlowConfigSourceConnectorPropertiesZendesk]: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesAmplitude(dict):
    def __init__(__self__, *, object: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesCustomConnector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        entity_name: _builtins.str,
        custom_properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesDatadog(dict):
    def __init__(__self__, *, object: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesDynatrace(dict):
    def __init__(__self__, *, object: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalytics(dict):
    def __init__(__self__, *, object: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesInforNexus(dict):
    def __init__(__self__, *, object: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesMarketo(dict):
    def __init__(__self__, *, object: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        bucket_prefix: _builtins.str,
        s3_input_format_config: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3InputFormatConfig")
    def s3_input_format_config(
        self,
    ) -> Optional[
        outputs.FlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig
    ]: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, s3_input_file_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3InputFileType")
    def s3_input_file_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesSalesforce(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object: _builtins.str,
        data_transfer_api: Optional[_builtins.str] = ...,
        enable_dynamic_field_update: Optional[_builtins.bool] = ...,
        include_deleted_records: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataTransferApi")
    def data_transfer_api(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableDynamicFieldUpdate")
    def enable_dynamic_field_update(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="includeDeletedRecords")
    def include_deleted_records(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesSapoData(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object_path: _builtins.str,
        pagination_config: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesSapoDataPaginationConfig
        ] = ...,
        parallelism_config: Optional[
            outputs.FlowSourceFlowConfigSourceConnectorPropertiesSapoDataParallelismConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="objectPath")
    def object_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="paginationConfig")
    def pagination_config(
        self,
    ) -> Optional[
        outputs.FlowSourceFlowConfigSourceConnectorPropertiesSapoDataPaginationConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="parallelismConfig")
    def parallelism_config(
        self,
    ) -> Optional[
        outputs.FlowSourceFlowConfigSourceConnectorPropertiesSapoDataParallelismConfig
    ]: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesSapoDataPaginationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_page_size: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPageSize")
    def max_page_size(self) -> _builtins.int: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesSapoDataParallelismConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, max_page_size: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxPageSize")
    def max_page_size(self) -> _builtins.int: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesServiceNow(dict):
    def __init__(__self__, *, object: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesSingular(dict):
    def __init__(__self__, *, object: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesSlack(dict):
    def __init__(__self__, *, object: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesTrendmicro(dict):
    def __init__(__self__, *, object: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesVeeva(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        object: _builtins.str,
        document_type: Optional[_builtins.str] = ...,
        include_all_versions: Optional[_builtins.bool] = ...,
        include_renditions: Optional[_builtins.bool] = ...,
        include_source_files: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="documentType")
    def document_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includeAllVersions")
    def include_all_versions(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="includeRenditions")
    def include_renditions(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="includeSourceFiles")
    def include_source_files(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FlowSourceFlowConfigSourceConnectorPropertiesZendesk(dict):
    def __init__(__self__, *, object: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> _builtins.str: ...

@pulumi.output_type
class FlowTask(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        task_type: _builtins.str,
        connector_operators: Optional[
            Sequence[outputs.FlowTaskConnectorOperator]
        ] = ...,
        destination_field: Optional[_builtins.str] = ...,
        source_fields: Optional[Sequence[_builtins.str]] = ...,
        task_properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectorOperators")
    def connector_operators(
        self,
    ) -> Optional[Sequence[outputs.FlowTaskConnectorOperator]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationField")
    def destination_field(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceFields")
    def source_fields(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="taskProperties")
    def task_properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class FlowTaskConnectorOperator(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amplitude: Optional[_builtins.str] = ...,
        custom_connector: Optional[_builtins.str] = ...,
        datadog: Optional[_builtins.str] = ...,
        dynatrace: Optional[_builtins.str] = ...,
        google_analytics: Optional[_builtins.str] = ...,
        infor_nexus: Optional[_builtins.str] = ...,
        marketo: Optional[_builtins.str] = ...,
        s3: Optional[_builtins.str] = ...,
        salesforce: Optional[_builtins.str] = ...,
        sapo_data: Optional[_builtins.str] = ...,
        service_now: Optional[_builtins.str] = ...,
        singular: Optional[_builtins.str] = ...,
        slack: Optional[_builtins.str] = ...,
        trendmicro: Optional[_builtins.str] = ...,
        veeva: Optional[_builtins.str] = ...,
        zendesk: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def amplitude(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customConnector")
    def custom_connector(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def datadog(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dynatrace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="googleAnalytics")
    def google_analytics(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inforNexus")
    def infor_nexus(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def marketo(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def salesforce(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sapoData")
    def sapo_data(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNow")
    def service_now(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def singular(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def slack(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def trendmicro(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def veeva(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zendesk(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FlowTriggerConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        trigger_type: _builtins.str,
        trigger_properties: Optional[outputs.FlowTriggerConfigTriggerProperties] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="triggerProperties")
    def trigger_properties(
        self,
    ) -> Optional[outputs.FlowTriggerConfigTriggerProperties]: ...

@pulumi.output_type
class FlowTriggerConfigTriggerProperties(dict):
    def __init__(
        __self__,
        *,
        scheduled: Optional[outputs.FlowTriggerConfigTriggerPropertiesScheduled] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def scheduled(
        self,
    ) -> Optional[outputs.FlowTriggerConfigTriggerPropertiesScheduled]: ...

@pulumi.output_type
class FlowTriggerConfigTriggerPropertiesScheduled(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        schedule_expression: _builtins.str,
        data_pull_mode: Optional[_builtins.str] = ...,
        first_execution_from: Optional[_builtins.str] = ...,
        schedule_end_time: Optional[_builtins.str] = ...,
        schedule_offset: Optional[_builtins.int] = ...,
        schedule_start_time: Optional[_builtins.str] = ...,
        timezone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPullMode")
    def data_pull_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstExecutionFrom")
    def first_execution_from(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleEndTime")
    def schedule_end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleOffset")
    def schedule_offset(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleStartTime")
    def schedule_start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> Optional[_builtins.str]: ...
