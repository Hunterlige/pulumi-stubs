

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AcsChatChannelResponse', 'AlexaChannelPropertiesResponse', 'AlexaChannelResponse', 'BotPropertiesResponse', 'ChannelSettingsResponse', 'ConnectionSettingParameterResponse', 'ConnectionSettingPropertiesResponse', 'DirectLineChannelPropertiesResponse', 'DirectLineChannelResponse', 'DirectLineSiteResponse', 'DirectLineSpeechChannelPropertiesResponse', 'DirectLineSpeechChannelResponse', 'EmailChannelPropertiesResponse', 'EmailChannelResponse', 'FacebookChannelPropertiesResponse', 'FacebookChannelResponse', 'FacebookPageResponse', 'KikChannelPropertiesResponse', 'KikChannelResponse', 'LineChannelPropertiesResponse', 'LineChannelResponse', 'LineRegistrationResponse', 'M365ExtensionsResponse', 'MsTeamsChannelPropertiesResponse', 'MsTeamsChannelResponse', ..., 'NetworkSecurityPerimeterConfigurationResponse', 'NetworkSecurityPerimeterResponse', 'NspAccessRulePropertiesResponse', 'NspAccessRulePropertiesSubscriptionsItemResponse', 'NspAccessRuleResponse', 'OmnichannelResponse', 'OutlookChannelResponse', 'PrivateEndpointConnectionResponse', 'PrivateEndpointResponse', 'PrivateLinkServiceConnectionStateResponse', 'ProfileResponse', 'ProvisioningIssuePropertiesResponse', 'ProvisioningIssueResponse', 'ResourceAssociationResponse', 'SearchAssistantResponse', ..., 'ServiceProviderParameterMetadataResponse', 'ServiceProviderParameterResponse', 'ServiceProviderPropertiesResponse', 'ServiceProviderResponse', 'SiteResponse', 'SkuResponse', 'SkypeChannelPropertiesResponse', 'SkypeChannelResponse', 'SlackChannelPropertiesResponse', 'SlackChannelResponse', 'SmsChannelPropertiesResponse', 'SmsChannelResponse', 'SystemDataResponse', 'TelegramChannelPropertiesResponse', 'TelegramChannelResponse', 'TelephonyChannelPropertiesResponse', 'TelephonyChannelResourceApiConfigurationResponse', 'TelephonyChannelResponse', 'TelephonyPhoneNumbersResponse', 'WebChatChannelPropertiesResponse', 'WebChatChannelResponse', 'WebChatSiteResponse']
@pulumi.output_type
class AcsChatChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AlexaChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alexa_skill_id: _builtins.str, is_enabled: _builtins.bool, service_endpoint_uri: _builtins.str, url_fragment: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alexaSkillId")
    def alexa_skill_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpointUri")
    def service_endpoint_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlFragment")
    def url_fragment(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AlexaChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.AlexaChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.AlexaChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class BotPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cmek_encryption_status: _builtins.str, configured_channels: Sequence[_builtins.str], display_name: _builtins.str, enabled_channels: Sequence[_builtins.str], endpoint: _builtins.str, endpoint_version: _builtins.str, is_developer_app_insights_api_key_set: _builtins.bool, migration_token: _builtins.str, msa_app_id: _builtins.str, network_security_perimeter_configurations: Sequence[outputs.NetworkSecurityPerimeterConfigurationResponse], private_endpoint_connections: Sequence[outputs.PrivateEndpointConnectionResponse], provisioning_state: _builtins.str, all_settings: Optional[Mapping[str, _builtins.str]] = ..., app_password_hint: Optional[_builtins.str] = ..., cmek_key_vault_url: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., developer_app_insight_key: Optional[_builtins.str] = ..., developer_app_insights_api_key: Optional[_builtins.str] = ..., developer_app_insights_application_id: Optional[_builtins.str] = ..., disable_local_auth: Optional[_builtins.bool] = ..., icon_url: Optional[_builtins.str] = ..., is_cmek_enabled: Optional[_builtins.bool] = ..., is_streaming_supported: Optional[_builtins.bool] = ..., luis_app_ids: Optional[Sequence[_builtins.str]] = ..., luis_key: Optional[_builtins.str] = ..., manifest_url: Optional[_builtins.str] = ..., msa_app_msi_resource_id: Optional[_builtins.str] = ..., msa_app_tenant_id: Optional[_builtins.str] = ..., msa_app_type: Optional[_builtins.str] = ..., open_with_hint: Optional[_builtins.str] = ..., parameters: Optional[Mapping[str, _builtins.str]] = ..., public_network_access: Optional[_builtins.str] = ..., publishing_credentials: Optional[_builtins.str] = ..., schema_transformation_version: Optional[_builtins.str] = ..., storage_resource_id: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmekEncryptionStatus")
    def cmek_encryption_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configuredChannels")
    def configured_channels(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledChannels")
    def enabled_channels(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointVersion")
    def endpoint_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDeveloperAppInsightsApiKeySet")
    def is_developer_app_insights_api_key_set(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationToken")
    def migration_token(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="msaAppId")
    def msa_app_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityPerimeterConfigurations")
    def network_security_perimeter_configurations(self) -> Sequence[outputs.NetworkSecurityPerimeterConfigurationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.PrivateEndpointConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allSettings")
    def all_settings(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appPasswordHint")
    def app_password_hint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cmekKeyVaultUrl")
    def cmek_key_vault_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerAppInsightKey")
    def developer_app_insight_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerAppInsightsApiKey")
    def developer_app_insights_api_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerAppInsightsApplicationId")
    def developer_app_insights_application_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iconUrl")
    def icon_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCmekEnabled")
    def is_cmek_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isStreamingSupported")
    def is_streaming_supported(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="luisAppIds")
    def luis_app_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="luisKey")
    def luis_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manifestUrl")
    def manifest_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="msaAppMSIResourceId")
    def msa_app_msi_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="msaAppTenantId")
    def msa_app_tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="msaAppType")
    def msa_app_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openWithHint")
    def open_with_hint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishingCredentials")
    def publishing_credentials(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaTransformationVersion")
    def schema_transformation_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageResourceId")
    def storage_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ChannelSettingsResponse(dict):
    
    def __init__(__self__, *, bot_icon_url: Optional[_builtins.str] = ..., bot_id: Optional[_builtins.str] = ..., channel_display_name: Optional[_builtins.str] = ..., channel_id: Optional[_builtins.str] = ..., disable_local_auth: Optional[_builtins.bool] = ..., extension_key1: Optional[_builtins.str] = ..., extension_key2: Optional[_builtins.str] = ..., is_enabled: Optional[_builtins.bool] = ..., require_terms_agreement: Optional[_builtins.bool] = ..., sites: Optional[Sequence[outputs.SiteResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botIconUrl")
    def bot_icon_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelDisplayName")
    def channel_display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionKey1")
    def extension_key1(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionKey2")
    def extension_key2(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireTermsAgreement")
    def require_terms_agreement(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sites(self) -> Optional[Sequence[outputs.SiteResponse]]:
        
        ...
    


@pulumi.output_type
class ConnectionSettingParameterResponse(dict):
    
    def __init__(__self__, *, key: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectionSettingPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, setting_id: _builtins.str, client_id: Optional[_builtins.str] = ..., client_secret: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., parameters: Optional[Sequence[outputs.ConnectionSettingParameterResponse]] = ..., provisioning_state: Optional[_builtins.str] = ..., scopes: Optional[_builtins.str] = ..., service_provider_display_name: Optional[_builtins.str] = ..., service_provider_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="settingId")
    def setting_id(self) -> _builtins.str:
        
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
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.ConnectionSettingParameterResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProviderDisplayName")
    def service_provider_display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProviderId")
    def service_provider_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DirectLineChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, direct_line_embed_code: Optional[_builtins.str] = ..., extension_key1: Optional[_builtins.str] = ..., extension_key2: Optional[_builtins.str] = ..., sites: Optional[Sequence[outputs.DirectLineSiteResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directLineEmbedCode")
    def direct_line_embed_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionKey1")
    def extension_key1(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionKey2")
    def extension_key2(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sites(self) -> Optional[Sequence[outputs.DirectLineSiteResponse]]:
        
        ...
    


@pulumi.output_type
class DirectLineChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.DirectLineChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.DirectLineChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class DirectLineSiteResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_enabled: _builtins.bool, is_token_enabled: _builtins.bool, key: _builtins.str, key2: _builtins.str, site_id: _builtins.str, site_name: _builtins.str, app_id: Optional[_builtins.str] = ..., e_tag: Optional[_builtins.str] = ..., is_block_user_upload_enabled: Optional[_builtins.bool] = ..., is_detailed_logging_enabled: Optional[_builtins.bool] = ..., is_endpoint_parameters_enabled: Optional[_builtins.bool] = ..., is_no_storage_enabled: Optional[_builtins.bool] = ..., is_secure_site_enabled: Optional[_builtins.bool] = ..., is_v1_enabled: Optional[_builtins.bool] = ..., is_v3_enabled: Optional[_builtins.bool] = ..., is_web_chat_speech_enabled: Optional[_builtins.bool] = ..., is_webchat_preview_enabled: Optional[_builtins.bool] = ..., tenant_id: Optional[_builtins.str] = ..., trusted_origins: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTokenEnabled")
    def is_token_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key2(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isBlockUserUploadEnabled")
    def is_block_user_upload_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDetailedLoggingEnabled")
    def is_detailed_logging_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEndpointParametersEnabled")
    def is_endpoint_parameters_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isNoStorageEnabled")
    def is_no_storage_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSecureSiteEnabled")
    def is_secure_site_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isV1Enabled")
    def is_v1_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isV3Enabled")
    def is_v3_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isWebChatSpeechEnabled")
    def is_web_chat_speech_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isWebchatPreviewEnabled")
    def is_webchat_preview_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedOrigins")
    def trusted_origins(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class DirectLineSpeechChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cognitive_service_region: Optional[_builtins.str] = ..., cognitive_service_resource_id: Optional[_builtins.str] = ..., cognitive_service_subscription_key: Optional[_builtins.str] = ..., custom_speech_model_id: Optional[_builtins.str] = ..., custom_voice_deployment_id: Optional[_builtins.str] = ..., is_default_bot_for_cog_svc_account: Optional[_builtins.bool] = ..., is_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceRegion")
    def cognitive_service_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceResourceId")
    def cognitive_service_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceSubscriptionKey")
    def cognitive_service_subscription_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customSpeechModelId")
    def custom_speech_model_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customVoiceDeploymentId")
    def custom_voice_deployment_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDefaultBotForCogSvcAccount")
    def is_default_bot_for_cog_svc_account(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class DirectLineSpeechChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.DirectLineSpeechChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.DirectLineSpeechChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class EmailChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, email_address: _builtins.str, is_enabled: _builtins.bool, auth_method: Optional[_builtins.float] = ..., magic_code: Optional[_builtins.str] = ..., password: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authMethod")
    def auth_method(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="magicCode")
    def magic_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EmailChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.EmailChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.EmailChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class FacebookChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, app_id: _builtins.str, callback_url: _builtins.str, is_enabled: _builtins.bool, verify_token: _builtins.str, app_secret: Optional[_builtins.str] = ..., pages: Optional[Sequence[outputs.FacebookPageResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callbackUrl")
    def callback_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifyToken")
    def verify_token(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSecret")
    def app_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pages(self) -> Optional[Sequence[outputs.FacebookPageResponse]]:
        
        ...
    


@pulumi.output_type
class FacebookChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.FacebookChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.FacebookChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class FacebookPageResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, access_token: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class KikChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_enabled: _builtins.bool, user_name: _builtins.str, api_key: Optional[_builtins.str] = ..., is_validated: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isValidated")
    def is_validated(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class KikChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.KikChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.KikChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class LineChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, callback_url: _builtins.str, is_validated: _builtins.bool, line_registrations: Sequence[outputs.LineRegistrationResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callbackUrl")
    def callback_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isValidated")
    def is_validated(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lineRegistrations")
    def line_registrations(self) -> Sequence[outputs.LineRegistrationResponse]:
        
        ...
    


@pulumi.output_type
class LineChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.LineChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.LineChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class LineRegistrationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, generated_id: _builtins.str, channel_access_token: Optional[_builtins.str] = ..., channel_secret: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatedId")
    def generated_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelAccessToken")
    def channel_access_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelSecret")
    def channel_secret(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class M365ExtensionsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MsTeamsChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_enabled: _builtins.bool, accepted_terms: Optional[_builtins.bool] = ..., calling_webhook: Optional[_builtins.str] = ..., deployment_environment: Optional[_builtins.str] = ..., enable_calling: Optional[_builtins.bool] = ..., incoming_call_route: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptedTerms")
    def accepted_terms(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callingWebhook")
    def calling_webhook(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentEnvironment")
    def deployment_environment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCalling")
    def enable_calling(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incomingCallRoute")
    def incoming_call_route(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class MsTeamsChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.MsTeamsChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.MsTeamsChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class NetworkSecurityPerimeterConfigurationPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_security_perimeter: outputs.NetworkSecurityPerimeterResponse, profile: outputs.ProfileResponse, resource_association: outputs.ResourceAssociationResponse, provisioning_issues: Optional[Sequence[outputs.ProvisioningIssueResponse]] = ..., provisioning_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityPerimeter")
    def network_security_perimeter(self) -> outputs.NetworkSecurityPerimeterResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def profile(self) -> outputs.ProfileResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAssociation")
    def resource_association(self) -> outputs.ResourceAssociationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningIssues")
    def provisioning_issues(self) -> Optional[Sequence[outputs.ProvisioningIssueResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class NetworkSecurityPerimeterConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, properties: Optional[outputs.NetworkSecurityPerimeterConfigurationPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.NetworkSecurityPerimeterConfigurationPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class NetworkSecurityPerimeterResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, location: Optional[_builtins.str] = ..., perimeter_guid: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="perimeterGuid")
    def perimeter_guid(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NspAccessRulePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, email_addresses: Sequence[_builtins.str], fully_qualified_domain_names: Sequence[_builtins.str], network_security_perimeters: Sequence[outputs.NetworkSecurityPerimeterResponse], phone_numbers: Sequence[_builtins.str], address_prefixes: Optional[Sequence[_builtins.str]] = ..., direction: Optional[_builtins.str] = ..., subscriptions: Optional[Sequence[outputs.NspAccessRulePropertiesSubscriptionsItemResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedDomainNames")
    def fully_qualified_domain_names(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityPerimeters")
    def network_security_perimeters(self) -> Sequence[outputs.NetworkSecurityPerimeterResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumbers")
    def phone_numbers(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefixes")
    def address_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscriptions(self) -> Optional[Sequence[outputs.NspAccessRulePropertiesSubscriptionsItemResponse]]:
        
        ...
    


@pulumi.output_type
class NspAccessRulePropertiesSubscriptionsItemResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class NspAccessRuleResponse(dict):
    
    def __init__(__self__, *, properties: outputs.NspAccessRulePropertiesResponse, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.NspAccessRulePropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OmnichannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class OutlookChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse, provisioning_state: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, group_ids: Optional[Sequence[_builtins.str]] = ..., private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> outputs.PrivateLinkServiceConnectionStateResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]:
        
        ...
    


@pulumi.output_type
class PrivateEndpointResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions_required: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProfileResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled_log_categories: Sequence[_builtins.str], access_rules: Optional[Sequence[outputs.NspAccessRuleResponse]] = ..., access_rules_version: Optional[_builtins.float] = ..., diagnostic_settings_version: Optional[_builtins.float] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledLogCategories")
    def enabled_log_categories(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRules")
    def access_rules(self) -> Optional[Sequence[outputs.NspAccessRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessRulesVersion")
    def access_rules_version(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diagnosticSettingsVersion")
    def diagnostic_settings_version(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ProvisioningIssuePropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, suggested_resource_ids: Sequence[_builtins.str], description: Optional[_builtins.str] = ..., issue_type: Optional[_builtins.str] = ..., severity: Optional[_builtins.str] = ..., suggested_access_rules: Optional[Sequence[outputs.NspAccessRuleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suggestedResourceIds")
    def suggested_resource_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issueType")
    def issue_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suggestedAccessRules")
    def suggested_access_rules(self) -> Optional[Sequence[outputs.NspAccessRuleResponse]]:
        
        ...
    


@pulumi.output_type
class ProvisioningIssueResponse(dict):
    
    def __init__(__self__, *, properties: outputs.ProvisioningIssuePropertiesResponse, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ProvisioningIssuePropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResourceAssociationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, access_mode: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SearchAssistantResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceProviderParameterMetadataConstraintsResponse(dict):
    
    def __init__(__self__, *, required: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ServiceProviderParameterMetadataResponse(dict):
    
    def __init__(__self__, *, constraints: Optional[outputs.ServiceProviderParameterMetadataConstraintsResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def constraints(self) -> Optional[outputs.ServiceProviderParameterMetadataConstraintsResponse]:
        
        ...
    


@pulumi.output_type
class ServiceProviderParameterResponse(dict):
    
    def __init__(__self__, *, default: _builtins.str, description: _builtins.str, display_name: _builtins.str, help_url: _builtins.str, metadata: outputs.ServiceProviderParameterMetadataResponse, name: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="helpUrl")
    def help_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> outputs.ServiceProviderParameterMetadataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServiceProviderPropertiesResponse(dict):
    
    def __init__(__self__, *, dev_portal_url: _builtins.str, display_name: _builtins.str, id: _builtins.str, service_provider_name: _builtins.str, icon_url: Optional[_builtins.str] = ..., parameters: Optional[Sequence[outputs.ServiceProviderParameterResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="devPortalUrl")
    def dev_portal_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProviderName")
    def service_provider_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iconUrl")
    def icon_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.ServiceProviderParameterResponse]]:
        
        ...
    


@pulumi.output_type
class ServiceProviderResponse(dict):
    
    def __init__(__self__, *, properties: Optional[outputs.ServiceProviderPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.ServiceProviderPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class SiteResponse(dict):
    
    def __init__(__self__, *, is_enabled: _builtins.bool, is_token_enabled: _builtins.bool, key: _builtins.str, key2: _builtins.str, site_id: _builtins.str, site_name: _builtins.str, app_id: Optional[_builtins.str] = ..., e_tag: Optional[_builtins.str] = ..., is_block_user_upload_enabled: Optional[_builtins.bool] = ..., is_detailed_logging_enabled: Optional[_builtins.bool] = ..., is_endpoint_parameters_enabled: Optional[_builtins.bool] = ..., is_no_storage_enabled: Optional[_builtins.bool] = ..., is_secure_site_enabled: Optional[_builtins.bool] = ..., is_v1_enabled: Optional[_builtins.bool] = ..., is_v3_enabled: Optional[_builtins.bool] = ..., is_web_chat_speech_enabled: Optional[_builtins.bool] = ..., is_webchat_preview_enabled: Optional[_builtins.bool] = ..., tenant_id: Optional[_builtins.str] = ..., trusted_origins: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTokenEnabled")
    def is_token_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key2(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isBlockUserUploadEnabled")
    def is_block_user_upload_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDetailedLoggingEnabled")
    def is_detailed_logging_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEndpointParametersEnabled")
    def is_endpoint_parameters_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isNoStorageEnabled")
    def is_no_storage_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSecureSiteEnabled")
    def is_secure_site_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isV1Enabled")
    def is_v1_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isV3Enabled")
    def is_v3_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isWebChatSpeechEnabled")
    def is_web_chat_speech_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isWebchatPreviewEnabled")
    def is_webchat_preview_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedOrigins")
    def trusted_origins(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class SkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, tier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SkypeChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_enabled: _builtins.bool, calling_web_hook: Optional[_builtins.str] = ..., enable_calling: Optional[_builtins.bool] = ..., enable_groups: Optional[_builtins.bool] = ..., enable_media_cards: Optional[_builtins.bool] = ..., enable_messaging: Optional[_builtins.bool] = ..., enable_screen_sharing: Optional[_builtins.bool] = ..., enable_video: Optional[_builtins.bool] = ..., groups_mode: Optional[_builtins.str] = ..., incoming_call_route: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="callingWebHook")
    def calling_web_hook(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCalling")
    def enable_calling(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGroups")
    def enable_groups(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMediaCards")
    def enable_media_cards(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMessaging")
    def enable_messaging(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableScreenSharing")
    def enable_screen_sharing(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableVideo")
    def enable_video(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupsMode")
    def groups_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="incomingCallRoute")
    def incoming_call_route(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SkypeChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.SkypeChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.SkypeChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class SlackChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_enabled: _builtins.bool, is_validated: _builtins.bool, last_submission_id: _builtins.str, redirect_action: _builtins.str, client_id: Optional[_builtins.str] = ..., client_secret: Optional[_builtins.str] = ..., landing_page_url: Optional[_builtins.str] = ..., register_before_o_auth_flow: Optional[_builtins.bool] = ..., scopes: Optional[_builtins.str] = ..., signing_secret: Optional[_builtins.str] = ..., verification_token: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isValidated")
    def is_validated(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastSubmissionId")
    def last_submission_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redirectAction")
    def redirect_action(self) -> _builtins.str:
        
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
    @pulumi.getter(name="landingPageUrl")
    def landing_page_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registerBeforeOAuthFlow")
    def register_before_o_auth_flow(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingSecret")
    def signing_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verificationToken")
    def verification_token(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SlackChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.SlackChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.SlackChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class SmsChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_sid: _builtins.str, is_enabled: _builtins.bool, phone: _builtins.str, auth_token: Optional[_builtins.str] = ..., is_validated: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountSID")
    def account_sid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isValidated")
    def is_validated(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class SmsChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.SmsChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.SmsChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TelegramChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_enabled: _builtins.bool, access_token: Optional[_builtins.str] = ..., is_validated: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isValidated")
    def is_validated(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class TelegramChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.TelegramChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.TelegramChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class TelephonyChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_configurations: Optional[Sequence[outputs.TelephonyChannelResourceApiConfigurationResponse]] = ..., cognitive_service_region: Optional[_builtins.str] = ..., cognitive_service_subscription_key: Optional[_builtins.str] = ..., default_locale: Optional[_builtins.str] = ..., is_enabled: Optional[_builtins.bool] = ..., phone_numbers: Optional[Sequence[outputs.TelephonyPhoneNumbersResponse]] = ..., premium_sku: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiConfigurations")
    def api_configurations(self) -> Optional[Sequence[outputs.TelephonyChannelResourceApiConfigurationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceRegion")
    def cognitive_service_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceSubscriptionKey")
    def cognitive_service_subscription_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLocale")
    def default_locale(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumbers")
    def phone_numbers(self) -> Optional[Sequence[outputs.TelephonyPhoneNumbersResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="premiumSKU")
    def premium_sku(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TelephonyChannelResourceApiConfigurationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cognitive_service_region: Optional[_builtins.str] = ..., cognitive_service_resource_id: Optional[_builtins.str] = ..., cognitive_service_subscription_key: Optional[_builtins.str] = ..., default_locale: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., provider_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceRegion")
    def cognitive_service_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceResourceId")
    def cognitive_service_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceSubscriptionKey")
    def cognitive_service_subscription_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLocale")
    def default_locale(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class TelephonyChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.TelephonyChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.TelephonyChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class TelephonyPhoneNumbersResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, acs_endpoint: Optional[_builtins.str] = ..., acs_resource_id: Optional[_builtins.str] = ..., acs_secret: Optional[_builtins.str] = ..., cognitive_service_region: Optional[_builtins.str] = ..., cognitive_service_resource_id: Optional[_builtins.str] = ..., cognitive_service_subscription_key: Optional[_builtins.str] = ..., default_locale: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., offer_type: Optional[_builtins.str] = ..., phone_number: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acsEndpoint")
    def acs_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acsResourceId")
    def acs_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acsSecret")
    def acs_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceRegion")
    def cognitive_service_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceResourceId")
    def cognitive_service_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceSubscriptionKey")
    def cognitive_service_subscription_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLocale")
    def default_locale(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="offerType")
    def offer_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebChatChannelPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, web_chat_embed_code: _builtins.str, sites: Optional[Sequence[outputs.WebChatSiteResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webChatEmbedCode")
    def web_chat_embed_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sites(self) -> Optional[Sequence[outputs.WebChatSiteResponse]]:
        
        ...
    


@pulumi.output_type
class WebChatChannelResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_name: _builtins.str, provisioning_state: _builtins.str, etag: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., properties: Optional[outputs.WebChatChannelPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.WebChatChannelPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class WebChatSiteResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_enabled: _builtins.bool, is_token_enabled: _builtins.bool, key: _builtins.str, key2: _builtins.str, site_id: _builtins.str, site_name: _builtins.str, app_id: Optional[_builtins.str] = ..., e_tag: Optional[_builtins.str] = ..., is_block_user_upload_enabled: Optional[_builtins.bool] = ..., is_detailed_logging_enabled: Optional[_builtins.bool] = ..., is_endpoint_parameters_enabled: Optional[_builtins.bool] = ..., is_no_storage_enabled: Optional[_builtins.bool] = ..., is_secure_site_enabled: Optional[_builtins.bool] = ..., is_v1_enabled: Optional[_builtins.bool] = ..., is_v3_enabled: Optional[_builtins.bool] = ..., is_web_chat_speech_enabled: Optional[_builtins.bool] = ..., is_webchat_preview_enabled: Optional[_builtins.bool] = ..., tenant_id: Optional[_builtins.str] = ..., trusted_origins: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTokenEnabled")
    def is_token_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key2(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isBlockUserUploadEnabled")
    def is_block_user_upload_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isDetailedLoggingEnabled")
    def is_detailed_logging_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEndpointParametersEnabled")
    def is_endpoint_parameters_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isNoStorageEnabled")
    def is_no_storage_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSecureSiteEnabled")
    def is_secure_site_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isV1Enabled")
    def is_v1_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isV3Enabled")
    def is_v3_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isWebChatSpeechEnabled")
    def is_web_chat_speech_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isWebchatPreviewEnabled")
    def is_webchat_preview_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedOrigins")
    def trusted_origins(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


