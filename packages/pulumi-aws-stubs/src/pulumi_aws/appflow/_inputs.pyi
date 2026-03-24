

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectorProfileConnectorProfileConfigArgs', 'ConnectorProfileConnectorProfileConfigArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FlowDestinationFlowConfigArgs', 'FlowDestinationFlowConfigArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FlowMetadataCatalogConfigArgs', 'FlowMetadataCatalogConfigArgsDict', 'FlowMetadataCatalogConfigGlueDataCatalogArgs', 'FlowMetadataCatalogConfigGlueDataCatalogArgsDict', 'FlowSourceFlowConfigArgs', 'FlowSourceFlowConfigArgsDict', 'FlowSourceFlowConfigIncrementalPullConfigArgs', 'FlowSourceFlowConfigIncrementalPullConfigArgsDict', 'FlowSourceFlowConfigSourceConnectorPropertiesArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'FlowTaskArgs', 'FlowTaskArgsDict', 'FlowTaskConnectorOperatorArgs', 'FlowTaskConnectorOperatorArgsDict', 'FlowTriggerConfigArgs', 'FlowTriggerConfigArgsDict', 'FlowTriggerConfigTriggerPropertiesArgs', 'FlowTriggerConfigTriggerPropertiesArgsDict', 'FlowTriggerConfigTriggerPropertiesScheduledArgs', ...]
class ConnectorProfileConnectorProfileConfigArgsDict(TypedDict):
    connector_profile_credentials: pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsArgsDict]
    connector_profile_properties: pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesArgsDict]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigArgs:
    def __init__(__self__, *, connector_profile_credentials: pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsArgs], connector_profile_properties: pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorProfileCredentials")
    def connector_profile_credentials(self) -> pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsArgs]:
        
        ...
    
    @connector_profile_credentials.setter
    def connector_profile_credentials(self, value: pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorProfileProperties")
    def connector_profile_properties(self) -> pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesArgs]:
        
        ...
    
    @connector_profile_properties.setter
    def connector_profile_properties(self, value: pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesArgs]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsArgsDict(TypedDict):
    amplitude: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeArgsDict]]
    custom_connector: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorArgsDict]]
    datadog: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogArgsDict]]
    dynatrace: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceArgsDict]]
    google_analytics: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsArgsDict]]
    honeycode: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeArgsDict]]
    infor_nexus: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusArgsDict]]
    marketo: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoArgsDict]]
    redshift: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftArgsDict]]
    salesforce: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceArgsDict]]
    sapo_data: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataArgsDict]]
    service_now: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowArgsDict]]
    singular: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularArgsDict]]
    slack: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackArgsDict]]
    snowflake: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeArgsDict]]
    trendmicro: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroArgsDict]]
    veeva: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaArgsDict]]
    zendesk: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskArgsDict]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsArgs:
    def __init__(__self__, *, amplitude: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeArgs]] = ..., custom_connector: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorArgs]] = ..., datadog: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogArgs]] = ..., dynatrace: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceArgs]] = ..., google_analytics: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsArgs]] = ..., honeycode: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeArgs]] = ..., infor_nexus: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusArgs]] = ..., marketo: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoArgs]] = ..., redshift: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftArgs]] = ..., salesforce: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceArgs]] = ..., sapo_data: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataArgs]] = ..., service_now: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowArgs]] = ..., singular: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularArgs]] = ..., slack: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackArgs]] = ..., snowflake: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeArgs]] = ..., trendmicro: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroArgs]] = ..., veeva: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaArgs]] = ..., zendesk: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amplitude(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeArgs]]:
        
        ...
    
    @amplitude.setter
    def amplitude(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customConnector")
    def custom_connector(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorArgs]]:
        
        ...
    
    @custom_connector.setter
    def custom_connector(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def datadog(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogArgs]]:
        
        ...
    
    @datadog.setter
    def datadog(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dynatrace(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceArgs]]:
        
        ...
    
    @dynatrace.setter
    def dynatrace(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleAnalytics")
    def google_analytics(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsArgs]]:
        
        ...
    
    @google_analytics.setter
    def google_analytics(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def honeycode(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeArgs]]:
        
        ...
    
    @honeycode.setter
    def honeycode(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inforNexus")
    def infor_nexus(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusArgs]]:
        
        ...
    
    @infor_nexus.setter
    def infor_nexus(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def marketo(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoArgs]]:
        
        ...
    
    @marketo.setter
    def marketo(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def redshift(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftArgs]]:
        
        ...
    
    @redshift.setter
    def redshift(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def salesforce(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceArgs]]:
        
        ...
    
    @salesforce.setter
    def salesforce(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sapoData")
    def sapo_data(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataArgs]]:
        
        ...
    
    @sapo_data.setter
    def sapo_data(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceNow")
    def service_now(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowArgs]]:
        
        ...
    
    @service_now.setter
    def service_now(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def singular(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularArgs]]:
        
        ...
    
    @singular.setter
    def singular(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def slack(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackArgs]]:
        
        ...
    
    @slack.setter
    def slack(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def snowflake(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeArgs]]:
        
        ...
    
    @snowflake.setter
    def snowflake(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def trendmicro(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroArgs]]:
        
        ...
    
    @trendmicro.setter
    def trendmicro(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def veeva(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaArgs]]:
        
        ...
    
    @veeva.setter
    def veeva(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zendesk(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskArgs]]:
        
        ...
    
    @zendesk.setter
    def zendesk(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskArgs]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeArgsDict(TypedDict):
    api_key: pulumi.Input[_builtins.str]
    secret_key: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitudeArgs:
    def __init__(__self__, *, api_key: pulumi.Input[_builtins.str], secret_key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @api_key.setter
    def api_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_key.setter
    def secret_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorArgsDict(TypedDict):
    authentication_type: pulumi.Input[_builtins.str]
    api_key: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyArgsDict]]
    basic: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicArgsDict]]
    custom: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomArgsDict]]
    oauth2: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2ArgsDict]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorArgs:
    def __init__(__self__, *, authentication_type: pulumi.Input[_builtins.str], api_key: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyArgs]] = ..., basic: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicArgs]] = ..., custom: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomArgs]] = ..., oauth2: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2Args]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyArgs]]:
        ...
    
    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def basic(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicArgs]]:
        
        ...
    
    @basic.setter
    def basic(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def custom(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomArgs]]:
        
        ...
    
    @custom.setter
    def custom(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def oauth2(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2Args]]:
        
        ...
    
    @oauth2.setter
    def oauth2(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2Args]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyArgsDict(TypedDict):
    api_key: pulumi.Input[_builtins.str]
    api_secret_key: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorApiKeyArgs:
    def __init__(__self__, *, api_key: pulumi.Input[_builtins.str], api_secret_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @api_key.setter
    def api_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiSecretKey")
    def api_secret_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @api_secret_key.setter
    def api_secret_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorBasicArgs:
    def __init__(__self__, *, password: pulumi.Input[_builtins.str], username: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomArgsDict(TypedDict):
    custom_authentication_type: pulumi.Input[_builtins.str]
    credentials_map: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorCustomArgs:
    def __init__(__self__, *, custom_authentication_type: pulumi.Input[_builtins.str], credentials_map: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customAuthenticationType")
    def custom_authentication_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @custom_authentication_type.setter
    def custom_authentication_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="credentialsMap")
    def credentials_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @credentials_map.setter
    def credentials_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2ArgsDict(TypedDict):
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    oauth_request: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestArgsDict]]
    refresh_token: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2Args:
    def __init__(__self__, *, access_token: Optional[pulumi.Input[_builtins.str]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., client_secret: Optional[pulumi.Input[_builtins.str]] = ..., oauth_request: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestArgs]] = ..., refresh_token: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="oauthRequest")
    def oauth_request(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestArgs]]:
        ...
    
    @oauth_request.setter
    def oauth_request(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestArgsDict(TypedDict):
    auth_code: NotRequired[pulumi.Input[_builtins.str]]
    redirect_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnectorOauth2OauthRequestArgs:
    def __init__(__self__, *, auth_code: Optional[pulumi.Input[_builtins.str]] = ..., redirect_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_code.setter
    def auth_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_uri.setter
    def redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogArgsDict(TypedDict):
    api_key: pulumi.Input[_builtins.str]
    application_key: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadogArgs:
    def __init__(__self__, *, api_key: pulumi.Input[_builtins.str], application_key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @api_key.setter
    def api_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationKey")
    def application_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @application_key.setter
    def application_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceArgsDict(TypedDict):
    api_token: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatraceArgs:
    def __init__(__self__, *, api_token: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @api_token.setter
    def api_token(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    oauth_request: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestArgsDict]]
    refresh_token: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], client_secret: pulumi.Input[_builtins.str], access_token: Optional[pulumi.Input[_builtins.str]] = ..., oauth_request: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestArgs]] = ..., refresh_token: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestArgs]]:
        ...
    
    @oauth_request.setter
    def oauth_request(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestArgsDict(TypedDict):
    auth_code: NotRequired[pulumi.Input[_builtins.str]]
    redirect_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalyticsOauthRequestArgs:
    def __init__(__self__, *, auth_code: Optional[pulumi.Input[_builtins.str]] = ..., redirect_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_code.setter
    def auth_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_uri.setter
    def redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeArgsDict(TypedDict):
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    oauth_request: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestArgsDict]]
    refresh_token: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeArgs:
    def __init__(__self__, *, access_token: Optional[pulumi.Input[_builtins.str]] = ..., oauth_request: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestArgs]] = ..., refresh_token: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestArgs]]:
        ...
    
    @oauth_request.setter
    def oauth_request(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestArgsDict(TypedDict):
    auth_code: NotRequired[pulumi.Input[_builtins.str]]
    redirect_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycodeOauthRequestArgs:
    def __init__(__self__, *, auth_code: Optional[pulumi.Input[_builtins.str]] = ..., redirect_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_code.setter
    def auth_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_uri.setter
    def redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusArgsDict(TypedDict):
    access_key_id: pulumi.Input[_builtins.str]
    datakey: pulumi.Input[_builtins.str]
    secret_access_key: pulumi.Input[_builtins.str]
    user_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexusArgs:
    def __init__(__self__, *, access_key_id: pulumi.Input[_builtins.str], datakey: pulumi.Input[_builtins.str], secret_access_key: pulumi.Input[_builtins.str], user_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @access_key_id.setter
    def access_key_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def datakey(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @datakey.setter
    def datakey(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_access_key.setter
    def secret_access_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_id.setter
    def user_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    oauth_request: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestArgsDict]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], client_secret: pulumi.Input[_builtins.str], access_token: Optional[pulumi.Input[_builtins.str]] = ..., oauth_request: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestArgs]]:
        ...
    
    @oauth_request.setter
    def oauth_request(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestArgs]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestArgsDict(TypedDict):
    auth_code: NotRequired[pulumi.Input[_builtins.str]]
    redirect_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketoOauthRequestArgs:
    def __init__(__self__, *, auth_code: Optional[pulumi.Input[_builtins.str]] = ..., redirect_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_code.setter
    def auth_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_uri.setter
    def redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshiftArgs:
    def __init__(__self__, *, password: pulumi.Input[_builtins.str], username: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceArgsDict(TypedDict):
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    client_credentials_arn: NotRequired[pulumi.Input[_builtins.str]]
    jwt_token: NotRequired[pulumi.Input[_builtins.str]]
    oauth2_grant_type: NotRequired[pulumi.Input[_builtins.str]]
    oauth_request: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestArgsDict]]
    refresh_token: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceArgs:
    def __init__(__self__, *, access_token: Optional[pulumi.Input[_builtins.str]] = ..., client_credentials_arn: Optional[pulumi.Input[_builtins.str]] = ..., jwt_token: Optional[pulumi.Input[_builtins.str]] = ..., oauth2_grant_type: Optional[pulumi.Input[_builtins.str]] = ..., oauth_request: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestArgs]] = ..., refresh_token: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCredentialsArn")
    def client_credentials_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_credentials_arn.setter
    def client_credentials_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jwtToken")
    def jwt_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @jwt_token.setter
    def jwt_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2GrantType")
    def oauth2_grant_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @oauth2_grant_type.setter
    def oauth2_grant_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestArgs]]:
        ...
    
    @oauth_request.setter
    def oauth_request(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestArgsDict(TypedDict):
    auth_code: NotRequired[pulumi.Input[_builtins.str]]
    redirect_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforceOauthRequestArgs:
    def __init__(__self__, *, auth_code: Optional[pulumi.Input[_builtins.str]] = ..., redirect_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_code.setter
    def auth_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_uri.setter
    def redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataArgsDict(TypedDict):
    basic_auth_credentials: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsArgsDict]]
    oauth_credentials: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsArgsDict]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataArgs:
    def __init__(__self__, *, basic_auth_credentials: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsArgs]] = ..., oauth_credentials: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAuthCredentials")
    def basic_auth_credentials(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsArgs]]:
        
        ...
    
    @basic_auth_credentials.setter
    def basic_auth_credentials(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthCredentials")
    def oauth_credentials(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsArgs]]:
        
        ...
    
    @oauth_credentials.setter
    def oauth_credentials(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsArgs]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataBasicAuthCredentialsArgs:
    def __init__(__self__, *, password: pulumi.Input[_builtins.str], username: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    oauth_request: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestArgsDict]]
    refresh_token: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], client_secret: pulumi.Input[_builtins.str], access_token: Optional[pulumi.Input[_builtins.str]] = ..., oauth_request: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestArgs]] = ..., refresh_token: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestArgs]]:
        ...
    
    @oauth_request.setter
    def oauth_request(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestArgsDict(TypedDict):
    auth_code: NotRequired[pulumi.Input[_builtins.str]]
    redirect_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoDataOauthCredentialsOauthRequestArgs:
    def __init__(__self__, *, auth_code: Optional[pulumi.Input[_builtins.str]] = ..., redirect_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_code.setter
    def auth_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_uri.setter
    def redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNowArgs:
    def __init__(__self__, *, password: pulumi.Input[_builtins.str], username: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularArgsDict(TypedDict):
    api_key: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingularArgs:
    def __init__(__self__, *, api_key: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @api_key.setter
    def api_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    oauth_request: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestArgsDict]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], client_secret: pulumi.Input[_builtins.str], access_token: Optional[pulumi.Input[_builtins.str]] = ..., oauth_request: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestArgs]]:
        ...
    
    @oauth_request.setter
    def oauth_request(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestArgs]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestArgsDict(TypedDict):
    auth_code: NotRequired[pulumi.Input[_builtins.str]]
    redirect_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlackOauthRequestArgs:
    def __init__(__self__, *, auth_code: Optional[pulumi.Input[_builtins.str]] = ..., redirect_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_code.setter
    def auth_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_uri.setter
    def redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflakeArgs:
    def __init__(__self__, *, password: pulumi.Input[_builtins.str], username: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroArgsDict(TypedDict):
    api_secret_key: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicroArgs:
    def __init__(__self__, *, api_secret_key: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiSecretKey")
    def api_secret_key(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @api_secret_key.setter
    def api_secret_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeevaArgs:
    def __init__(__self__, *, password: pulumi.Input[_builtins.str], username: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[_builtins.str]
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    oauth_request: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestArgsDict]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], client_secret: pulumi.Input[_builtins.str], access_token: Optional[pulumi.Input[_builtins.str]] = ..., oauth_request: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthRequest")
    def oauth_request(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestArgs]]:
        ...
    
    @oauth_request.setter
    def oauth_request(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestArgs]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestArgsDict(TypedDict):
    auth_code: NotRequired[pulumi.Input[_builtins.str]]
    redirect_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendeskOauthRequestArgs:
    def __init__(__self__, *, auth_code: Optional[pulumi.Input[_builtins.str]] = ..., redirect_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authCode")
    def auth_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auth_code.setter
    def auth_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @redirect_uri.setter
    def redirect_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesArgsDict(TypedDict):
    amplitude: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeArgsDict]]
    custom_connector: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorArgsDict]]
    datadog: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogArgsDict]]
    dynatrace: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceArgsDict]]
    google_analytics: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsArgsDict]]
    honeycode: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeArgsDict]]
    infor_nexus: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusArgsDict]]
    marketo: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoArgsDict]]
    redshift: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftArgsDict]]
    salesforce: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceArgsDict]]
    sapo_data: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataArgsDict]]
    service_now: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowArgsDict]]
    singular: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularArgsDict]]
    slack: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackArgsDict]]
    snowflake: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeArgsDict]]
    trendmicro: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroArgsDict]]
    veeva: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaArgsDict]]
    zendesk: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskArgsDict]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesArgs:
    def __init__(__self__, *, amplitude: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeArgs]] = ..., custom_connector: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorArgs]] = ..., datadog: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogArgs]] = ..., dynatrace: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceArgs]] = ..., google_analytics: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsArgs]] = ..., honeycode: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeArgs]] = ..., infor_nexus: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusArgs]] = ..., marketo: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoArgs]] = ..., redshift: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftArgs]] = ..., salesforce: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceArgs]] = ..., sapo_data: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataArgs]] = ..., service_now: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowArgs]] = ..., singular: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularArgs]] = ..., slack: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackArgs]] = ..., snowflake: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeArgs]] = ..., trendmicro: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroArgs]] = ..., veeva: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaArgs]] = ..., zendesk: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amplitude(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeArgs]]:
        
        ...
    
    @amplitude.setter
    def amplitude(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customConnector")
    def custom_connector(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorArgs]]:
        
        ...
    
    @custom_connector.setter
    def custom_connector(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def datadog(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogArgs]]:
        
        ...
    
    @datadog.setter
    def datadog(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dynatrace(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceArgs]]:
        
        ...
    
    @dynatrace.setter
    def dynatrace(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleAnalytics")
    def google_analytics(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsArgs]]:
        
        ...
    
    @google_analytics.setter
    def google_analytics(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def honeycode(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeArgs]]:
        
        ...
    
    @honeycode.setter
    def honeycode(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inforNexus")
    def infor_nexus(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusArgs]]:
        
        ...
    
    @infor_nexus.setter
    def infor_nexus(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def marketo(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoArgs]]:
        
        ...
    
    @marketo.setter
    def marketo(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def redshift(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftArgs]]:
        
        ...
    
    @redshift.setter
    def redshift(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def salesforce(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceArgs]]:
        
        ...
    
    @salesforce.setter
    def salesforce(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sapoData")
    def sapo_data(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataArgs]]:
        
        ...
    
    @sapo_data.setter
    def sapo_data(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceNow")
    def service_now(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowArgs]]:
        
        ...
    
    @service_now.setter
    def service_now(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def singular(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularArgs]]:
        
        ...
    
    @singular.setter
    def singular(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def slack(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackArgs]]:
        
        ...
    
    @slack.setter
    def slack(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def snowflake(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeArgs]]:
        
        ...
    
    @snowflake.setter
    def snowflake(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def trendmicro(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroArgs]]:
        
        ...
    
    @trendmicro.setter
    def trendmicro(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def veeva(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaArgs]]:
        
        ...
    
    @veeva.setter
    def veeva(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zendesk(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskArgs]]:
        
        ...
    
    @zendesk.setter
    def zendesk(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskArgs]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeArgsDict(TypedDict):
    ...


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesAmplitudeArgs:
    def __init__(__self__) -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorArgsDict(TypedDict):
    oauth2_properties: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesArgsDict]]
    profile_properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorArgs:
    def __init__(__self__, *, oauth2_properties: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesArgs]] = ..., profile_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2Properties")
    def oauth2_properties(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesArgs]]:
        
        ...
    
    @oauth2_properties.setter
    def oauth2_properties(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileProperties")
    def profile_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @profile_properties.setter
    def profile_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesArgsDict(TypedDict):
    oauth2_grant_type: pulumi.Input[_builtins.str]
    token_url: pulumi.Input[_builtins.str]
    token_url_custom_properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesCustomConnectorOauth2PropertiesArgs:
    def __init__(__self__, *, oauth2_grant_type: pulumi.Input[_builtins.str], token_url: pulumi.Input[_builtins.str], token_url_custom_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2GrantType")
    def oauth2_grant_type(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @oauth2_grant_type.setter
    def oauth2_grant_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenUrl")
    def token_url(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @token_url.setter
    def token_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenUrlCustomProperties")
    def token_url_custom_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @token_url_custom_properties.setter
    def token_url_custom_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogArgsDict(TypedDict):
    instance_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDatadogArgs:
    def __init__(__self__, *, instance_url: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @instance_url.setter
    def instance_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceArgsDict(TypedDict):
    instance_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesDynatraceArgs:
    def __init__(__self__, *, instance_url: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @instance_url.setter
    def instance_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsArgsDict(TypedDict):
    ...


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesGoogleAnalyticsArgs:
    def __init__(__self__) -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeArgsDict(TypedDict):
    ...


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesHoneycodeArgs:
    def __init__(__self__) -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusArgsDict(TypedDict):
    instance_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesInforNexusArgs:
    def __init__(__self__, *, instance_url: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @instance_url.setter
    def instance_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoArgsDict(TypedDict):
    instance_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesMarketoArgs:
    def __init__(__self__, *, instance_url: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @instance_url.setter
    def instance_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    cluster_identifier: NotRequired[pulumi.Input[_builtins.str]]
    data_api_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    database_name: NotRequired[pulumi.Input[_builtins.str]]
    database_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesRedshiftArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., data_api_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., database_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataApiRoleArn")
    def data_api_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_api_role_arn.setter
    def data_api_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseUrl")
    def database_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_url.setter
    def database_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceArgsDict(TypedDict):
    instance_url: NotRequired[pulumi.Input[_builtins.str]]
    is_sandbox_environment: NotRequired[pulumi.Input[_builtins.bool]]
    use_privatelink_for_metadata_and_authorization: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSalesforceArgs:
    def __init__(__self__, *, instance_url: Optional[pulumi.Input[_builtins.str]] = ..., is_sandbox_environment: Optional[pulumi.Input[_builtins.bool]] = ..., use_privatelink_for_metadata_and_authorization: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @instance_url.setter
    def instance_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSandboxEnvironment")
    def is_sandbox_environment(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_sandbox_environment.setter
    def is_sandbox_environment(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePrivatelinkForMetadataAndAuthorization")
    def use_privatelink_for_metadata_and_authorization(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_privatelink_for_metadata_and_authorization.setter
    def use_privatelink_for_metadata_and_authorization(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataArgsDict(TypedDict):
    application_host_url: pulumi.Input[_builtins.str]
    application_service_path: pulumi.Input[_builtins.str]
    client_number: pulumi.Input[_builtins.str]
    port_number: pulumi.Input[_builtins.int]
    logon_language: NotRequired[pulumi.Input[_builtins.str]]
    oauth_properties: NotRequired[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesArgsDict]]
    private_link_service_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataArgs:
    def __init__(__self__, *, application_host_url: pulumi.Input[_builtins.str], application_service_path: pulumi.Input[_builtins.str], client_number: pulumi.Input[_builtins.str], port_number: pulumi.Input[_builtins.int], logon_language: Optional[pulumi.Input[_builtins.str]] = ..., oauth_properties: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesArgs]] = ..., private_link_service_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationHostUrl")
    def application_host_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @application_host_url.setter
    def application_host_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationServicePath")
    def application_service_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @application_service_path.setter
    def application_service_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientNumber")
    def client_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_number.setter
    def client_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portNumber")
    def port_number(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port_number.setter
    def port_number(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logonLanguage")
    def logon_language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @logon_language.setter
    def logon_language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthProperties")
    def oauth_properties(self) -> Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesArgs]]:
        
        ...
    
    @oauth_properties.setter
    def oauth_properties(self, value: Optional[pulumi.Input[ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceName")
    def private_link_service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @private_link_service_name.setter
    def private_link_service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesArgsDict(TypedDict):
    auth_code_url: pulumi.Input[_builtins.str]
    oauth_scopes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    token_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSapoDataOauthPropertiesArgs:
    def __init__(__self__, *, auth_code_url: pulumi.Input[_builtins.str], oauth_scopes: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], token_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authCodeUrl")
    def auth_code_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @auth_code_url.setter
    def auth_code_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthScopes")
    def oauth_scopes(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @oauth_scopes.setter
    def oauth_scopes(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenUrl")
    def token_url(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @token_url.setter
    def token_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowArgsDict(TypedDict):
    instance_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesServiceNowArgs:
    def __init__(__self__, *, instance_url: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @instance_url.setter
    def instance_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularArgsDict(TypedDict):
    ...


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSingularArgs:
    def __init__(__self__) -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackArgsDict(TypedDict):
    instance_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSlackArgs:
    def __init__(__self__, *, instance_url: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @instance_url.setter
    def instance_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    stage: pulumi.Input[_builtins.str]
    warehouse: pulumi.Input[_builtins.str]
    account_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    private_link_service_name: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesSnowflakeArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], stage: pulumi.Input[_builtins.str], warehouse: pulumi.Input[_builtins.str], account_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., private_link_service_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @stage.setter
    def stage(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def warehouse(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @warehouse.setter
    def warehouse(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceName")
    def private_link_service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @private_link_service_name.setter
    def private_link_service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroArgsDict(TypedDict):
    ...


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesTrendmicroArgs:
    def __init__(__self__) -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaArgsDict(TypedDict):
    instance_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesVeevaArgs:
    def __init__(__self__, *, instance_url: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @instance_url.setter
    def instance_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskArgsDict(TypedDict):
    instance_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConnectorProfileConnectorProfileConfigConnectorProfilePropertiesZendeskArgs:
    def __init__(__self__, *, instance_url: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @instance_url.setter
    def instance_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowDestinationFlowConfigArgsDict(TypedDict):
    connector_type: pulumi.Input[_builtins.str]
    destination_connector_properties: pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesArgsDict]
    api_version: NotRequired[pulumi.Input[_builtins.str]]
    connector_profile_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowDestinationFlowConfigArgs:
    def __init__(__self__, *, connector_type: pulumi.Input[_builtins.str], destination_connector_properties: pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesArgs], api_version: Optional[pulumi.Input[_builtins.str]] = ..., connector_profile_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connector_type.setter
    def connector_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConnectorProperties")
    def destination_connector_properties(self) -> pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesArgs]:
        
        ...
    
    @destination_connector_properties.setter
    def destination_connector_properties(self, value: pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorProfileName")
    def connector_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connector_profile_name.setter
    def connector_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesArgsDict(TypedDict):
    custom_connector: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorArgsDict]]
    customer_profiles: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesArgsDict]]
    event_bridge: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeArgsDict]]
    honeycode: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeArgsDict]]
    lookout_metrics: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsArgsDict]]
    marketo: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoArgsDict]]
    redshift: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftArgsDict]]
    s3: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3ArgsDict]]
    salesforce: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceArgsDict]]
    sapo_data: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataArgsDict]]
    snowflake: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeArgsDict]]
    upsolver: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverArgsDict]]
    zendesk: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskArgsDict]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesArgs:
    def __init__(__self__, *, custom_connector: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorArgs]] = ..., customer_profiles: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesArgs]] = ..., event_bridge: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeArgs]] = ..., honeycode: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeArgs]] = ..., lookout_metrics: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsArgs]] = ..., marketo: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoArgs]] = ..., redshift: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftArgs]] = ..., s3: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3Args]] = ..., salesforce: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceArgs]] = ..., sapo_data: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataArgs]] = ..., snowflake: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeArgs]] = ..., upsolver: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverArgs]] = ..., zendesk: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customConnector")
    def custom_connector(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorArgs]]:
        
        ...
    
    @custom_connector.setter
    def custom_connector(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerProfiles")
    def customer_profiles(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesArgs]]:
        
        ...
    
    @customer_profiles.setter
    def customer_profiles(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventBridge")
    def event_bridge(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeArgs]]:
        
        ...
    
    @event_bridge.setter
    def event_bridge(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def honeycode(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeArgs]]:
        
        ...
    
    @honeycode.setter
    def honeycode(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookoutMetrics")
    def lookout_metrics(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsArgs]]:
        ...
    
    @lookout_metrics.setter
    def lookout_metrics(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def marketo(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoArgs]]:
        
        ...
    
    @marketo.setter
    def marketo(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def redshift(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftArgs]]:
        
        ...
    
    @redshift.setter
    def redshift(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3Args]]:
        
        ...
    
    @s3.setter
    def s3(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3Args]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def salesforce(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceArgs]]:
        
        ...
    
    @salesforce.setter
    def salesforce(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sapoData")
    def sapo_data(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataArgs]]:
        
        ...
    
    @sapo_data.setter
    def sapo_data(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def snowflake(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeArgs]]:
        
        ...
    
    @snowflake.setter
    def snowflake(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def upsolver(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverArgs]]:
        
        ...
    
    @upsolver.setter
    def upsolver(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zendesk(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskArgs]]:
        
        ...
    
    @zendesk.setter
    def zendesk(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskArgs]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorArgsDict(TypedDict):
    entity_name: pulumi.Input[_builtins.str]
    custom_properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    error_handling_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigArgsDict]]
    id_field_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    write_operation_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorArgs:
    def __init__(__self__, *, entity_name: pulumi.Input[_builtins.str], custom_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., error_handling_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigArgs]] = ..., id_field_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., write_operation_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @entity_name.setter
    def entity_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @custom_properties.setter
    def custom_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigArgs]]:
        ...
    
    @error_handling_config.setter
    def error_handling_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idFieldNames")
    def id_field_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @id_field_names.setter
    def id_field_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeOperationType")
    def write_operation_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @write_operation_type.setter
    def write_operation_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    fail_on_first_destination_error: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesCustomConnectorErrorHandlingConfigArgs:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., fail_on_first_destination_error: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    object_type_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesCustomerProfilesArgs:
    def __init__(__self__, *, domain_name: pulumi.Input[_builtins.str], object_type_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectTypeName")
    def object_type_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_type_name.setter
    def object_type_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]
    error_handling_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigArgsDict]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str], error_handling_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigArgs]]:
        ...
    
    @error_handling_config.setter
    def error_handling_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigArgs]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    fail_on_first_destination_error: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesEventBridgeErrorHandlingConfigArgs:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., fail_on_first_destination_error: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]
    error_handling_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigArgsDict]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str], error_handling_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigArgs]]:
        ...
    
    @error_handling_config.setter
    def error_handling_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigArgs]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    fail_on_first_destination_error: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesHoneycodeErrorHandlingConfigArgs:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., fail_on_first_destination_error: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsArgsDict(TypedDict):
    ...


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesLookoutMetricsArgs:
    def __init__(__self__) -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]
    error_handling_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigArgsDict]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str], error_handling_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigArgs]]:
        ...
    
    @error_handling_config.setter
    def error_handling_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigArgs]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    fail_on_first_destination_error: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesMarketoErrorHandlingConfigArgs:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., fail_on_first_destination_error: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftArgsDict(TypedDict):
    intermediate_bucket_name: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    error_handling_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigArgsDict]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftArgs:
    def __init__(__self__, *, intermediate_bucket_name: pulumi.Input[_builtins.str], object: pulumi.Input[_builtins.str], bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., error_handling_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="intermediateBucketName")
    def intermediate_bucket_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @intermediate_bucket_name.setter
    def intermediate_bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigArgs]]:
        ...
    
    @error_handling_config.setter
    def error_handling_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigArgs]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    fail_on_first_destination_error: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesRedshiftErrorHandlingConfigArgs:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., fail_on_first_destination_error: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesS3ArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    s3_output_format_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigArgsDict]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesS3Args:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., s3_output_format_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3OutputFormatConfig")
    def s3_output_format_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigArgs]]:
        ...
    
    @s3_output_format_config.setter
    def s3_output_format_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigArgs]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigArgsDict(TypedDict):
    aggregation_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigArgsDict]]
    file_type: NotRequired[pulumi.Input[_builtins.str]]
    prefix_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigArgsDict]]
    preserve_source_data_typing: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigArgs:
    def __init__(__self__, *, aggregation_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigArgs]] = ..., file_type: Optional[pulumi.Input[_builtins.str]] = ..., prefix_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigArgs]] = ..., preserve_source_data_typing: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregationConfig")
    def aggregation_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigArgs]]:
        
        ...
    
    @aggregation_config.setter
    def aggregation_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileType")
    def file_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_type.setter
    def file_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixConfig")
    def prefix_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigArgs]]:
        
        ...
    
    @prefix_config.setter
    def prefix_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveSourceDataTyping")
    def preserve_source_data_typing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @preserve_source_data_typing.setter
    def preserve_source_data_typing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigArgsDict(TypedDict):
    aggregation_type: NotRequired[pulumi.Input[_builtins.str]]
    target_file_size: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigAggregationConfigArgs:
    def __init__(__self__, *, aggregation_type: Optional[pulumi.Input[_builtins.str]] = ..., target_file_size: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregationType")
    def aggregation_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aggregation_type.setter
    def aggregation_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFileSize")
    def target_file_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @target_file_size.setter
    def target_file_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigArgsDict(TypedDict):
    prefix_format: NotRequired[pulumi.Input[_builtins.str]]
    prefix_hierarchies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    prefix_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesS3S3OutputFormatConfigPrefixConfigArgs:
    def __init__(__self__, *, prefix_format: Optional[pulumi.Input[_builtins.str]] = ..., prefix_hierarchies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., prefix_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixFormat")
    def prefix_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix_format.setter
    def prefix_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixHierarchies")
    def prefix_hierarchies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @prefix_hierarchies.setter
    def prefix_hierarchies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixType")
    def prefix_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix_type.setter
    def prefix_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]
    data_transfer_api: NotRequired[pulumi.Input[_builtins.str]]
    error_handling_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigArgsDict]]
    id_field_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    write_operation_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str], data_transfer_api: Optional[pulumi.Input[_builtins.str]] = ..., error_handling_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigArgs]] = ..., id_field_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., write_operation_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTransferApi")
    def data_transfer_api(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @data_transfer_api.setter
    def data_transfer_api(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigArgs]]:
        ...
    
    @error_handling_config.setter
    def error_handling_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idFieldNames")
    def id_field_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @id_field_names.setter
    def id_field_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeOperationType")
    def write_operation_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @write_operation_type.setter
    def write_operation_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    fail_on_first_destination_error: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSalesforceErrorHandlingConfigArgs:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., fail_on_first_destination_error: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataArgsDict(TypedDict):
    object_path: pulumi.Input[_builtins.str]
    error_handling_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigArgsDict]]
    id_field_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    success_response_handling_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigArgsDict]]
    write_operation_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataArgs:
    def __init__(__self__, *, object_path: pulumi.Input[_builtins.str], error_handling_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigArgs]] = ..., id_field_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., success_response_handling_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigArgs]] = ..., write_operation_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectPath")
    def object_path(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object_path.setter
    def object_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigArgs]]:
        ...
    
    @error_handling_config.setter
    def error_handling_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idFieldNames")
    def id_field_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @id_field_names.setter
    def id_field_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="successResponseHandlingConfig")
    def success_response_handling_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigArgs]]:
        
        ...
    
    @success_response_handling_config.setter
    def success_response_handling_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeOperationType")
    def write_operation_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @write_operation_type.setter
    def write_operation_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    fail_on_first_destination_error: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataErrorHandlingConfigArgs:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., fail_on_first_destination_error: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSapoDataSuccessResponseHandlingConfigArgs:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeArgsDict(TypedDict):
    intermediate_bucket_name: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    error_handling_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigArgsDict]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeArgs:
    def __init__(__self__, *, intermediate_bucket_name: pulumi.Input[_builtins.str], object: pulumi.Input[_builtins.str], bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., error_handling_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="intermediateBucketName")
    def intermediate_bucket_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @intermediate_bucket_name.setter
    def intermediate_bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigArgs]]:
        ...
    
    @error_handling_config.setter
    def error_handling_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigArgs]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    fail_on_first_destination_error: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesSnowflakeErrorHandlingConfigArgs:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., fail_on_first_destination_error: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    s3_output_format_config: pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigArgsDict]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverArgs:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], s3_output_format_config: pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigArgs], bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3OutputFormatConfig")
    def s3_output_format_config(self) -> pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigArgs]:
        ...
    
    @s3_output_format_config.setter
    def s3_output_format_config(self, value: pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigArgsDict(TypedDict):
    prefix_config: pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigArgsDict]
    aggregation_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigArgsDict]]
    file_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigArgs:
    def __init__(__self__, *, prefix_config: pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigArgs], aggregation_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigArgs]] = ..., file_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixConfig")
    def prefix_config(self) -> pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigArgs]:
        
        ...
    
    @prefix_config.setter
    def prefix_config(self, value: pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregationConfig")
    def aggregation_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigArgs]]:
        
        ...
    
    @aggregation_config.setter
    def aggregation_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileType")
    def file_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_type.setter
    def file_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigArgsDict(TypedDict):
    aggregation_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigAggregationConfigArgs:
    def __init__(__self__, *, aggregation_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregationType")
    def aggregation_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aggregation_type.setter
    def aggregation_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigArgsDict(TypedDict):
    prefix_type: pulumi.Input[_builtins.str]
    prefix_format: NotRequired[pulumi.Input[_builtins.str]]
    prefix_hierarchies: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesUpsolverS3OutputFormatConfigPrefixConfigArgs:
    def __init__(__self__, *, prefix_type: pulumi.Input[_builtins.str], prefix_format: Optional[pulumi.Input[_builtins.str]] = ..., prefix_hierarchies: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixType")
    def prefix_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @prefix_type.setter
    def prefix_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixFormat")
    def prefix_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix_format.setter
    def prefix_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixHierarchies")
    def prefix_hierarchies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @prefix_hierarchies.setter
    def prefix_hierarchies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]
    error_handling_config: NotRequired[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigArgsDict]]
    id_field_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    write_operation_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str], error_handling_config: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigArgs]] = ..., id_field_names: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., write_operation_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorHandlingConfig")
    def error_handling_config(self) -> Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigArgs]]:
        ...
    
    @error_handling_config.setter
    def error_handling_config(self, value: Optional[pulumi.Input[FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idFieldNames")
    def id_field_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @id_field_names.setter
    def id_field_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="writeOperationType")
    def write_operation_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @write_operation_type.setter
    def write_operation_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigArgsDict(TypedDict):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    fail_on_first_destination_error: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowDestinationFlowConfigDestinationConnectorPropertiesZendeskErrorHandlingConfigArgs:
    def __init__(__self__, *, bucket_name: Optional[pulumi.Input[_builtins.str]] = ..., bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., fail_on_first_destination_error: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOnFirstDestinationError")
    def fail_on_first_destination_error(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @fail_on_first_destination_error.setter
    def fail_on_first_destination_error(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FlowMetadataCatalogConfigArgsDict(TypedDict):
    glue_data_catalog: NotRequired[pulumi.Input[FlowMetadataCatalogConfigGlueDataCatalogArgsDict]]


@pulumi.input_type
class FlowMetadataCatalogConfigArgs:
    def __init__(__self__, *, glue_data_catalog: Optional[pulumi.Input[FlowMetadataCatalogConfigGlueDataCatalogArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="glueDataCatalog")
    def glue_data_catalog(self) -> Optional[pulumi.Input[FlowMetadataCatalogConfigGlueDataCatalogArgs]]:
        ...
    
    @glue_data_catalog.setter
    def glue_data_catalog(self, value: Optional[pulumi.Input[FlowMetadataCatalogConfigGlueDataCatalogArgs]]): # -> None:
        ...
    


class FlowMetadataCatalogConfigGlueDataCatalogArgsDict(TypedDict):
    database_name: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    table_prefix: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowMetadataCatalogConfigGlueDataCatalogArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], role_arn: pulumi.Input[_builtins.str], table_prefix: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_prefix.setter
    def table_prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowSourceFlowConfigArgsDict(TypedDict):
    connector_type: pulumi.Input[_builtins.str]
    source_connector_properties: pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesArgsDict]
    api_version: NotRequired[pulumi.Input[_builtins.str]]
    connector_profile_name: NotRequired[pulumi.Input[_builtins.str]]
    incremental_pull_config: NotRequired[pulumi.Input[FlowSourceFlowConfigIncrementalPullConfigArgsDict]]


@pulumi.input_type
class FlowSourceFlowConfigArgs:
    def __init__(__self__, *, connector_type: pulumi.Input[_builtins.str], source_connector_properties: pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesArgs], api_version: Optional[pulumi.Input[_builtins.str]] = ..., connector_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., incremental_pull_config: Optional[pulumi.Input[FlowSourceFlowConfigIncrementalPullConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connector_type.setter
    def connector_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectorProperties")
    def source_connector_properties(self) -> pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesArgs]:
        
        ...
    
    @source_connector_properties.setter
    def source_connector_properties(self, value: pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorProfileName")
    def connector_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connector_profile_name.setter
    def connector_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="incrementalPullConfig")
    def incremental_pull_config(self) -> Optional[pulumi.Input[FlowSourceFlowConfigIncrementalPullConfigArgs]]:
        
        ...
    
    @incremental_pull_config.setter
    def incremental_pull_config(self, value: Optional[pulumi.Input[FlowSourceFlowConfigIncrementalPullConfigArgs]]): # -> None:
        ...
    


class FlowSourceFlowConfigIncrementalPullConfigArgsDict(TypedDict):
    datetime_type_field_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowSourceFlowConfigIncrementalPullConfigArgs:
    def __init__(__self__, *, datetime_type_field_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datetimeTypeFieldName")
    def datetime_type_field_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @datetime_type_field_name.setter
    def datetime_type_field_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesArgsDict(TypedDict):
    amplitude: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesAmplitudeArgsDict]]
    custom_connector: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorArgsDict]]
    datadog: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesDatadogArgsDict]]
    dynatrace: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesDynatraceArgsDict]]
    google_analytics: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsArgsDict]]
    infor_nexus: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesInforNexusArgsDict]]
    marketo: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesMarketoArgsDict]]
    s3: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesS3ArgsDict]]
    salesforce: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSalesforceArgsDict]]
    sapo_data: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSapoDataArgsDict]]
    service_now: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesServiceNowArgsDict]]
    singular: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSingularArgsDict]]
    slack: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSlackArgsDict]]
    trendmicro: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesTrendmicroArgsDict]]
    veeva: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesVeevaArgsDict]]
    zendesk: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesZendeskArgsDict]]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesArgs:
    def __init__(__self__, *, amplitude: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesAmplitudeArgs]] = ..., custom_connector: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorArgs]] = ..., datadog: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesDatadogArgs]] = ..., dynatrace: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesDynatraceArgs]] = ..., google_analytics: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsArgs]] = ..., infor_nexus: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesInforNexusArgs]] = ..., marketo: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesMarketoArgs]] = ..., s3: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesS3Args]] = ..., salesforce: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSalesforceArgs]] = ..., sapo_data: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSapoDataArgs]] = ..., service_now: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesServiceNowArgs]] = ..., singular: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSingularArgs]] = ..., slack: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSlackArgs]] = ..., trendmicro: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesTrendmicroArgs]] = ..., veeva: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesVeevaArgs]] = ..., zendesk: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesZendeskArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amplitude(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesAmplitudeArgs]]:
        
        ...
    
    @amplitude.setter
    def amplitude(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesAmplitudeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customConnector")
    def custom_connector(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorArgs]]:
        
        ...
    
    @custom_connector.setter
    def custom_connector(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def datadog(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesDatadogArgs]]:
        
        ...
    
    @datadog.setter
    def datadog(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesDatadogArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dynatrace(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesDynatraceArgs]]:
        
        ...
    
    @dynatrace.setter
    def dynatrace(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesDynatraceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleAnalytics")
    def google_analytics(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsArgs]]:
        
        ...
    
    @google_analytics.setter
    def google_analytics(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inforNexus")
    def infor_nexus(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesInforNexusArgs]]:
        
        ...
    
    @infor_nexus.setter
    def infor_nexus(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesInforNexusArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def marketo(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesMarketoArgs]]:
        
        ...
    
    @marketo.setter
    def marketo(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesMarketoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesS3Args]]:
        
        ...
    
    @s3.setter
    def s3(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesS3Args]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def salesforce(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSalesforceArgs]]:
        
        ...
    
    @salesforce.setter
    def salesforce(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSalesforceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sapoData")
    def sapo_data(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSapoDataArgs]]:
        
        ...
    
    @sapo_data.setter
    def sapo_data(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSapoDataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceNow")
    def service_now(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesServiceNowArgs]]:
        
        ...
    
    @service_now.setter
    def service_now(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesServiceNowArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def singular(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSingularArgs]]:
        
        ...
    
    @singular.setter
    def singular(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSingularArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def slack(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSlackArgs]]:
        
        ...
    
    @slack.setter
    def slack(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSlackArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def trendmicro(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesTrendmicroArgs]]:
        
        ...
    
    @trendmicro.setter
    def trendmicro(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesTrendmicroArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def veeva(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesVeevaArgs]]:
        
        ...
    
    @veeva.setter
    def veeva(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesVeevaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zendesk(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesZendeskArgs]]:
        
        ...
    
    @zendesk.setter
    def zendesk(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesZendeskArgs]]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesAmplitudeArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesAmplitudeArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorArgsDict(TypedDict):
    entity_name: pulumi.Input[_builtins.str]
    custom_properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesCustomConnectorArgs:
    def __init__(__self__, *, entity_name: pulumi.Input[_builtins.str], custom_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @entity_name.setter
    def entity_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @custom_properties.setter
    def custom_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesDatadogArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesDatadogArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesDynatraceArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesDynatraceArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesGoogleAnalyticsArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesInforNexusArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesInforNexusArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesMarketoArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesMarketoArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesS3ArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    bucket_prefix: pulumi.Input[_builtins.str]
    s3_input_format_config: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigArgsDict]]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesS3Args:
    def __init__(__self__, *, bucket_name: pulumi.Input[_builtins.str], bucket_prefix: pulumi.Input[_builtins.str], s3_input_format_config: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3InputFormatConfig")
    def s3_input_format_config(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigArgs]]:
        
        ...
    
    @s3_input_format_config.setter
    def s3_input_format_config(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigArgs]]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigArgsDict(TypedDict):
    s3_input_file_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesS3S3InputFormatConfigArgs:
    def __init__(__self__, *, s3_input_file_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3InputFileType")
    def s3_input_file_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_input_file_type.setter
    def s3_input_file_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesSalesforceArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]
    data_transfer_api: NotRequired[pulumi.Input[_builtins.str]]
    enable_dynamic_field_update: NotRequired[pulumi.Input[_builtins.bool]]
    include_deleted_records: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesSalesforceArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str], data_transfer_api: Optional[pulumi.Input[_builtins.str]] = ..., enable_dynamic_field_update: Optional[pulumi.Input[_builtins.bool]] = ..., include_deleted_records: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTransferApi")
    def data_transfer_api(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @data_transfer_api.setter
    def data_transfer_api(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDynamicFieldUpdate")
    def enable_dynamic_field_update(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_dynamic_field_update.setter
    def enable_dynamic_field_update(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeDeletedRecords")
    def include_deleted_records(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_deleted_records.setter
    def include_deleted_records(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesSapoDataArgsDict(TypedDict):
    object_path: pulumi.Input[_builtins.str]
    pagination_config: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSapoDataPaginationConfigArgsDict]]
    parallelism_config: NotRequired[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSapoDataParallelismConfigArgsDict]]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesSapoDataArgs:
    def __init__(__self__, *, object_path: pulumi.Input[_builtins.str], pagination_config: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSapoDataPaginationConfigArgs]] = ..., parallelism_config: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSapoDataParallelismConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectPath")
    def object_path(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object_path.setter
    def object_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="paginationConfig")
    def pagination_config(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSapoDataPaginationConfigArgs]]:
        
        ...
    
    @pagination_config.setter
    def pagination_config(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSapoDataPaginationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelismConfig")
    def parallelism_config(self) -> Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSapoDataParallelismConfigArgs]]:
        
        ...
    
    @parallelism_config.setter
    def parallelism_config(self, value: Optional[pulumi.Input[FlowSourceFlowConfigSourceConnectorPropertiesSapoDataParallelismConfigArgs]]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesSapoDataPaginationConfigArgsDict(TypedDict):
    max_page_size: pulumi.Input[_builtins.int]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesSapoDataPaginationConfigArgs:
    def __init__(__self__, *, max_page_size: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPageSize")
    def max_page_size(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_page_size.setter
    def max_page_size(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesSapoDataParallelismConfigArgsDict(TypedDict):
    max_page_size: pulumi.Input[_builtins.int]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesSapoDataParallelismConfigArgs:
    def __init__(__self__, *, max_page_size: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxPageSize")
    def max_page_size(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_page_size.setter
    def max_page_size(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesServiceNowArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesServiceNowArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesSingularArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesSingularArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesSlackArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesSlackArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesTrendmicroArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesTrendmicroArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesVeevaArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]
    document_type: NotRequired[pulumi.Input[_builtins.str]]
    include_all_versions: NotRequired[pulumi.Input[_builtins.bool]]
    include_renditions: NotRequired[pulumi.Input[_builtins.bool]]
    include_source_files: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesVeevaArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str], document_type: Optional[pulumi.Input[_builtins.str]] = ..., include_all_versions: Optional[pulumi.Input[_builtins.bool]] = ..., include_renditions: Optional[pulumi.Input[_builtins.bool]] = ..., include_source_files: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentType")
    def document_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @document_type.setter
    def document_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeAllVersions")
    def include_all_versions(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_all_versions.setter
    def include_all_versions(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeRenditions")
    def include_renditions(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_renditions.setter
    def include_renditions(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeSourceFiles")
    def include_source_files(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @include_source_files.setter
    def include_source_files(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FlowSourceFlowConfigSourceConnectorPropertiesZendeskArgsDict(TypedDict):
    object: pulumi.Input[_builtins.str]


@pulumi.input_type
class FlowSourceFlowConfigSourceConnectorPropertiesZendeskArgs:
    def __init__(__self__, *, object: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FlowTaskArgsDict(TypedDict):
    task_type: pulumi.Input[_builtins.str]
    connector_operators: NotRequired[pulumi.Input[Sequence[pulumi.Input[FlowTaskConnectorOperatorArgsDict]]]]
    destination_field: NotRequired[pulumi.Input[_builtins.str]]
    source_fields: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    task_properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class FlowTaskArgs:
    def __init__(__self__, *, task_type: pulumi.Input[_builtins.str], connector_operators: Optional[pulumi.Input[Sequence[pulumi.Input[FlowTaskConnectorOperatorArgs]]]] = ..., destination_field: Optional[pulumi.Input[_builtins.str]] = ..., source_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., task_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @task_type.setter
    def task_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorOperators")
    def connector_operators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FlowTaskConnectorOperatorArgs]]]]:
        
        ...
    
    @connector_operators.setter
    def connector_operators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FlowTaskConnectorOperatorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationField")
    def destination_field(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_field.setter
    def destination_field(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFields")
    def source_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_fields.setter
    def source_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskProperties")
    def task_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @task_properties.setter
    def task_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class FlowTaskConnectorOperatorArgsDict(TypedDict):
    amplitude: NotRequired[pulumi.Input[_builtins.str]]
    custom_connector: NotRequired[pulumi.Input[_builtins.str]]
    datadog: NotRequired[pulumi.Input[_builtins.str]]
    dynatrace: NotRequired[pulumi.Input[_builtins.str]]
    google_analytics: NotRequired[pulumi.Input[_builtins.str]]
    infor_nexus: NotRequired[pulumi.Input[_builtins.str]]
    marketo: NotRequired[pulumi.Input[_builtins.str]]
    s3: NotRequired[pulumi.Input[_builtins.str]]
    salesforce: NotRequired[pulumi.Input[_builtins.str]]
    sapo_data: NotRequired[pulumi.Input[_builtins.str]]
    service_now: NotRequired[pulumi.Input[_builtins.str]]
    singular: NotRequired[pulumi.Input[_builtins.str]]
    slack: NotRequired[pulumi.Input[_builtins.str]]
    trendmicro: NotRequired[pulumi.Input[_builtins.str]]
    veeva: NotRequired[pulumi.Input[_builtins.str]]
    zendesk: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowTaskConnectorOperatorArgs:
    def __init__(__self__, *, amplitude: Optional[pulumi.Input[_builtins.str]] = ..., custom_connector: Optional[pulumi.Input[_builtins.str]] = ..., datadog: Optional[pulumi.Input[_builtins.str]] = ..., dynatrace: Optional[pulumi.Input[_builtins.str]] = ..., google_analytics: Optional[pulumi.Input[_builtins.str]] = ..., infor_nexus: Optional[pulumi.Input[_builtins.str]] = ..., marketo: Optional[pulumi.Input[_builtins.str]] = ..., s3: Optional[pulumi.Input[_builtins.str]] = ..., salesforce: Optional[pulumi.Input[_builtins.str]] = ..., sapo_data: Optional[pulumi.Input[_builtins.str]] = ..., service_now: Optional[pulumi.Input[_builtins.str]] = ..., singular: Optional[pulumi.Input[_builtins.str]] = ..., slack: Optional[pulumi.Input[_builtins.str]] = ..., trendmicro: Optional[pulumi.Input[_builtins.str]] = ..., veeva: Optional[pulumi.Input[_builtins.str]] = ..., zendesk: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def amplitude(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @amplitude.setter
    def amplitude(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customConnector")
    def custom_connector(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_connector.setter
    def custom_connector(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def datadog(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @datadog.setter
    def datadog(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dynatrace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dynatrace.setter
    def dynatrace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleAnalytics")
    def google_analytics(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @google_analytics.setter
    def google_analytics(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inforNexus")
    def infor_nexus(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @infor_nexus.setter
    def infor_nexus(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def marketo(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @marketo.setter
    def marketo(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3.setter
    def s3(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def salesforce(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @salesforce.setter
    def salesforce(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sapoData")
    def sapo_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sapo_data.setter
    def sapo_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceNow")
    def service_now(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_now.setter
    def service_now(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def singular(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @singular.setter
    def singular(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def slack(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @slack.setter
    def slack(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def trendmicro(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trendmicro.setter
    def trendmicro(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def veeva(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @veeva.setter
    def veeva(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zendesk(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zendesk.setter
    def zendesk(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FlowTriggerConfigArgsDict(TypedDict):
    trigger_type: pulumi.Input[_builtins.str]
    trigger_properties: NotRequired[pulumi.Input[FlowTriggerConfigTriggerPropertiesArgsDict]]


@pulumi.input_type
class FlowTriggerConfigArgs:
    def __init__(__self__, *, trigger_type: pulumi.Input[_builtins.str], trigger_properties: Optional[pulumi.Input[FlowTriggerConfigTriggerPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerType")
    def trigger_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @trigger_type.setter
    def trigger_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerProperties")
    def trigger_properties(self) -> Optional[pulumi.Input[FlowTriggerConfigTriggerPropertiesArgs]]:
        
        ...
    
    @trigger_properties.setter
    def trigger_properties(self, value: Optional[pulumi.Input[FlowTriggerConfigTriggerPropertiesArgs]]): # -> None:
        ...
    


class FlowTriggerConfigTriggerPropertiesArgsDict(TypedDict):
    scheduled: NotRequired[pulumi.Input[FlowTriggerConfigTriggerPropertiesScheduledArgsDict]]


@pulumi.input_type
class FlowTriggerConfigTriggerPropertiesArgs:
    def __init__(__self__, *, scheduled: Optional[pulumi.Input[FlowTriggerConfigTriggerPropertiesScheduledArgs]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scheduled(self) -> Optional[pulumi.Input[FlowTriggerConfigTriggerPropertiesScheduledArgs]]:
        ...
    
    @scheduled.setter
    def scheduled(self, value: Optional[pulumi.Input[FlowTriggerConfigTriggerPropertiesScheduledArgs]]): # -> None:
        ...
    


class FlowTriggerConfigTriggerPropertiesScheduledArgsDict(TypedDict):
    schedule_expression: pulumi.Input[_builtins.str]
    data_pull_mode: NotRequired[pulumi.Input[_builtins.str]]
    first_execution_from: NotRequired[pulumi.Input[_builtins.str]]
    schedule_end_time: NotRequired[pulumi.Input[_builtins.str]]
    schedule_offset: NotRequired[pulumi.Input[_builtins.int]]
    schedule_start_time: NotRequired[pulumi.Input[_builtins.str]]
    timezone: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FlowTriggerConfigTriggerPropertiesScheduledArgs:
    def __init__(__self__, *, schedule_expression: pulumi.Input[_builtins.str], data_pull_mode: Optional[pulumi.Input[_builtins.str]] = ..., first_execution_from: Optional[pulumi.Input[_builtins.str]] = ..., schedule_end_time: Optional[pulumi.Input[_builtins.str]] = ..., schedule_offset: Optional[pulumi.Input[_builtins.int]] = ..., schedule_start_time: Optional[pulumi.Input[_builtins.str]] = ..., timezone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @schedule_expression.setter
    def schedule_expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPullMode")
    def data_pull_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_pull_mode.setter
    def data_pull_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstExecutionFrom")
    def first_execution_from(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_execution_from.setter
    def first_execution_from(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleEndTime")
    def schedule_end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule_end_time.setter
    def schedule_end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleOffset")
    def schedule_offset(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @schedule_offset.setter
    def schedule_offset(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleStartTime")
    def schedule_start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schedule_start_time.setter
    def schedule_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


